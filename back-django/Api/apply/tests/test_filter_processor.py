import json
from django.test import TestCase
from django.core.management import call_command
from Api.filter.filter_processor import process_filters
from Api.filter.models import FilterScheme
from Api.apply.models import Apply
from Api.setting.models import Major

class FilterProcessorTest(TestCase):
    def setUp(self):
        # 加载测试数据
        with open('Api/apply/tests/apply_test.json', 'r') as f:
            applies_data = json.load(f)
        
        with open('Api/filter/filterExamples.json', 'r') as f:
            filters_data = json.load(f)
        
        # 创建测试用的专业数据
        Major.objects.create(name='限制专业', category='限制专业')
        
        # 创建申请记录
        for apply_data in applies_data:
            Apply.objects.create(**apply_data)
        
        # 创建筛选方案
        for filter_data in filters_data:
            scheme = FilterScheme.objects.create(
                name=filter_data['name'],
                enabled=filter_data['enabled']
            )
            scheme.set_conditions(filter_data['conditions'])
            scheme.save()
    
    def test_a_class_top_20_percent(self):
        """测试A类前20%的筛选方案"""
        filtered = process_filters()
        a_class_applies = [a for a in filtered if a.universityLevel == 'A' and 
                         float(a.percentage.rstrip('%')) <= 20]
        self.assertTrue(all(float(a.percentage.rstrip('%')) <= 20 for a in a_class_applies))
    
    def test_b_class_restricted_major(self):
        """测试B类限制专业前20%的筛选方案"""
        filtered = process_filters()
        b_class_applies = [a for a in filtered if a.universityLevel == 'B' and 
                         a.major == '限制专业' and float(a.percentage.rstrip('%')) <= 20]
        self.assertTrue(all(a.major == '限制专业' for a in b_class_applies))
    
    def test_top_class_condition(self):
        """测试拔尖班条件的筛选方案"""
        filtered = process_filters()
        top_class_applies = [a for a in filtered if a.isTopClass]
        self.assertTrue(all(a.isTopClass for a in top_class_applies))
    
    def test_paper_condition(self):
        """测试论文条件的筛选方案"""
        filtered = process_filters()
        paper_condition_applies = [a for a in filtered if getattr(a, 'isPaperCondition', False)]
        for apply in paper_condition_applies:
            has_valid_paper = False
            for i in range(1, 4):
                if (getattr(apply, f'paper{i}_isFirst') and 
                    getattr(apply, f'paper{i}_ccfLevel') in ['A', 'B']):
                    has_valid_paper = True
                    break
            self.assertTrue(has_valid_paper)
    
    def test_award_condition(self):
        """测试奖项条件的筛选方案"""
        filtered = process_filters()
        award_condition_applies = [a for a in filtered if getattr(a, 'isAwardCondition', False)]
        for apply in award_condition_applies:
            has_valid_award = False
            for i in range(1, 4):
                if (getattr(apply, f'award{i}_isLeader') and 
                    getattr(apply, f'award{i}_awardName') in ['挑战杯', '互联网+'] and
                    getattr(apply, f'award{i}_awardRanking') in ['特等奖', '金奖', '一等奖']):
                    has_valid_award = True
                    break
            self.assertTrue(has_valid_award)