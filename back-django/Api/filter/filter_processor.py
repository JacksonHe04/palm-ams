from django.db.models import Q
from django.http import JsonResponse
from .models import FilterScheme
from Api.apply.models import Apply
from Api.setting.models import Major

def process_filters(request):
    # 获取所有启用的筛选方案
    enabled_schemes = FilterScheme.objects.filter(enabled=True)
    filtered_applies = set()

    for scheme in enabled_schemes:
        conditions = scheme.get_conditions()
        scheme_query = Q()

        # 处理每个筛选方案的条件
        for condition in conditions:
            field = condition['field']
            operator = condition['operator']
            value = condition['value']

            if field == '本科等级':
                scheme_query &= Q(universityLevel=value)
            elif field == '百分比':
                # 处理百分比字段，去掉%并转换为数字
                scheme_query &= Q(percentage__regex=r'^\d+')
            elif field == '专业':
                # 获取所有限制专业的专业名称
                restricted_majors = Major.objects.filter(category='限制专业').values_list('name', flat=True)
                scheme_query &= Q(major__in=restricted_majors)
            elif field == '是否为拔尖班':
                is_top = True if value == '是' else False
                scheme_query &= Q(isTopClass=is_top)

        # 获取满足基本条件的申请记录
        applies = Apply.objects.filter(scheme_query)

        # 进一步处理百分比条件
        if any(c['field'] == '百分比' for c in conditions):
            percentage_value = next(c['value'] for c in conditions if c['field'] == '百分比')
            applies = [apply for apply in applies 
                      if float(apply.percentage.rstrip('%')) <= float(percentage_value)]

        # 处理论文条件
        if any(c['field'] == '论文等级' for c in conditions):
            paper_levels = next(c['value'] for c in conditions if c['field'] == '论文等级')
            for apply in applies:
                # 检查是否有符合条件的论文
                has_valid_paper = False
                for i in range(1, 4):
                    is_first = getattr(apply, f'paper{i}_isFirst')
                    ccf_level = getattr(apply, f'paper{i}_ccfLevel')
                    if is_first and ccf_level in paper_levels:
                        has_valid_paper = True
                        break
                if has_valid_paper:
                    apply.isPaperCondition = True
                    apply.save()
                else:
                    applies.remove(apply)

        # 处理奖项条件
        if any(c['field'] in ['奖项名称', '奖项等级'] for c in conditions):
            award_names = next((c['value'] for c in conditions if c['field'] == '奖项名称'), [])
            award_levels = next((c['value'] for c in conditions if c['field'] == '奖项等级'), [])
            
            for apply in applies:
                # 检查是否有符合条件的奖项
                has_valid_award = False
                for i in range(1, 4):
                    is_leader = getattr(apply, f'award{i}_isLeader')
                    award_name = getattr(apply, f'award{i}_awardName')
                    award_ranking = getattr(apply, f'award{i}_awardRanking')
                    
                    if (is_leader and 
                        award_name in award_names and 
                        award_ranking in award_levels):
                        has_valid_award = True
                        break
                if has_valid_award:
                    apply.isAwardCondition = True
                    apply.save()
                else:
                    applies.remove(apply)

        # 更新通过筛选的申请记录
        for apply in applies:
            apply.isFilterCondition = 'true'
            apply.save()
            filtered_applies.add(apply)

    # 将结果转换为列表并序列化为JSON响应
    result = [{
        'id': apply.id,
        'name': apply.name,
        'universityLevel': apply.universityLevel,
        'percentage': apply.percentage,
        'major': apply.major,
        'isTopClass': apply.isTopClass,
        'isPaperCondition': apply.isPaperCondition,
        'isAwardCondition': apply.isAwardCondition,
        'isFilterCondition': apply.isFilterCondition
    } for apply in filtered_applies]
    
    return JsonResponse(result, safe=False)