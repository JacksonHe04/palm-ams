from django.db import models

# Create your models here.
 

class PalmApplicant(models.Model):

    submit_time=models.CharField(max_length=100,verbose_name=u"提交时间",default="0")
    # 定义一个自增的id主键
    objid = models.AutoField(primary_key=True, verbose_name=u"编号")
    # 定义一个最大长度为32的varchar字段
    name_input = models.CharField(max_length=32, verbose_name=u"姓名")
    #性别
    GENDER_CHOICE = (
    (u"男", u'男'),
    (u'女', u'女'),
    )
    sex_input = models.CharField(max_length=2,choices = GENDER_CHOICE,verbose_name=u"性别")
    #出生年月
    birthday = models.CharField(max_length=100,verbose_name=u"出生日期", default="生日")
    #籍贯
    province = models.CharField(max_length=100, verbose_name=u"省", default="省份")
    city = models.CharField(max_length=100, verbose_name=u"市", default="城市")
    district = models.CharField(max_length=100, verbose_name=u"区", default="街道")
    #院校
    undergraduate_university_input = models.CharField(max_length=100, verbose_name=u"本科院校", default="本科学校")
    #专业
    major_input = models.CharField(max_length=100,verbose_name=u"本科专业", default="专业")
    #照片
    photo = models.ImageField(verbose_name=u"照片", upload_to='img/', default="0")
    #硕士院校
    master_university_input = models.CharField(max_length=100, verbose_name=u"硕士院校", default="硕士学校")
    #硕士导师
    mastertutor_input = models.CharField(max_length=100,verbose_name=u"硕士导师", default="本科生不填写")
    #专业排名
    grade_input = models.IntegerField(verbose_name=u"专业排名")
    #专业人数 
    gradepeople_input = models.IntegerField(verbose_name=u"专业人数")
    
    
    #手机号
    phonenumber_input = models.CharField(max_length=100,verbose_name=u"手机号码", default="手机号")
    #邮箱
    email_input = models.EmailField(verbose_name=u"邮箱", default='mail')

    #报名类型
    registrationtype_input = models.CharField(max_length=100,verbose_name=u"报名类型")
    #意向导师
    tutor_input_first = models.CharField(max_length=100, verbose_name=u"导师1", default="导师1")
    tutor_input_second = models.CharField(max_length=100, verbose_name=u"导师2", default="导师2")
    tutor_input_third = models.CharField(max_length=100, verbose_name=u"导师3", default="导师3")
    #服从调剂
    ajustment_input = models.CharField(max_length=10, verbose_name=u"服从调剂", default="0")
    #论文发表
    time_paper1 = models.CharField(max_length=100,verbose_name=u"论文发表时间1", default="0")
    journal_name1 = models.CharField(max_length=100,verbose_name=u"期刊会议名1", default="0")
    paper_name1 = models.CharField(max_length=500,verbose_name=u"论文1", default="0")
    time_paper2 = models.CharField(max_length=100,verbose_name=u"论文发表时间2", default="0")
    journal_name2 = models.CharField(max_length=100,verbose_name=u"期刊会议名2", default="0")
    paper_name2 = models.CharField(max_length=500,verbose_name=u"论文2", default="0")
    time_paper3 = models.CharField(max_length=100,verbose_name=u"论文发表时间3", default="0")
    journal_name3 = models.CharField(max_length=100,verbose_name=u"期刊会议名3", default="0")
    paper_name3 = models.CharField(max_length=500,verbose_name=u"论文3", default="0")

    #奖项荣誉
    time_award1 = models.CharField(max_length=100,verbose_name=u"获奖时间1", default="0")
    award_grade1 = models.CharField(max_length=100,verbose_name=u"获奖等级1", default="0")
    award_name1 = models.CharField(max_length=100,verbose_name=u"奖项1", default="0")
    time_award2 = models.CharField(max_length=100,verbose_name=u"获奖时间2", default="0")
    award_grade2 = models.CharField(max_length=100,verbose_name=u"获奖等级2", default="0")
    award_name2 = models.CharField(max_length=100,verbose_name=u"奖项2", default="0")
    time_award3 = models.CharField(max_length=100,verbose_name=u"获奖时间3", default="0")
    award_grade3 = models.CharField(max_length=100,verbose_name=u"获奖等级3", default="0")
    award_name3 = models.CharField(max_length=100,verbose_name=u"奖项3", default="0")
    time_award4 = models.CharField(max_length=100,verbose_name=u"获奖时间4", default="0")
    award_grade4 = models.CharField(max_length=100,verbose_name=u"获奖等级4", default="0")
    award_name4 = models.CharField(max_length=100,verbose_name=u"奖项4", default="0")
    time_award5 = models.CharField(max_length=100,verbose_name=u"获奖时间5", default="0")
    award_grade5 = models.CharField(max_length=100,verbose_name=u"获奖等级5", default="0")
    award_name5 = models.CharField(max_length=100,verbose_name=u"奖项5", default="0")
    #个人陈述
    statement_input = models.CharField(max_length=1000,verbose_name=u"个人陈述", default="个人陈述")
    #研究计划
    researchplan_input = models.CharField(max_length=1000,verbose_name=u"研究计划", default="研究计划")
