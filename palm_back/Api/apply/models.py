from django.db import models

class Apply(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=50)
    graduationYear = models.IntegerField()
    gender = models.CharField(max_length=10)
    birthDate = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='Apply/')
    university = models.CharField(max_length=50)
    major = models.CharField(max_length=50)
    majorCount = models.IntegerField()
    rank = models.IntegerField()
    percentage = models.CharField(max_length=10)  # 添加 max_length 属性
    masterUniversity = models.CharField(max_length=50)
    masterMajor = models.CharField(max_length=50)
    tutor = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=100)  # 添加 max_length 属性
    applicationType = models.CharField(max_length=50)
    firstChoice = models.CharField(max_length=50)
    secondChoice = models.CharField(max_length=50)
    thirdChoice = models.CharField(max_length=50)
    isAdjustable = models.BooleanField()
    proofs = models.CharField(max_length=255)  # 添加 max_length 属性
    status = models.CharField(max_length=50)

    # 新增 paper 相关字段
    paper1_publicationTime = models.CharField(max_length=7, null=True, blank=True)
    paper1_journalConference = models.CharField(max_length=100, null=True, blank=True)
    paper1_paperName = models.CharField(max_length=100, null=True, blank=True)
    paper1_ccfLevel = models.CharField(max_length=10, null=True, blank=True)
    paper1_awardCategory = models.CharField(max_length=50, null=True, blank=True)

    paper2_publicationTime = models.CharField(max_length=7, null=True, blank=True)
    paper2_journalConference = models.CharField(max_length=100, null=True, blank=True)
    paper2_paperName = models.CharField(max_length=100, null=True, blank=True)
    paper2_ccfLevel = models.CharField(max_length=10, null=True, blank=True)
    paper2_awardCategory = models.CharField(max_length=50, null=True, blank=True)

    paper3_publicationTime = models.CharField(max_length=7, null=True, blank=True)
    paper3_journalConference = models.CharField(max_length=100, null=True, blank=True)
    paper3_paperName = models.CharField(max_length=100, null=True, blank=True)
    paper3_ccfLevel = models.CharField(max_length=10, null=True, blank=True)
    paper3_awardCategory = models.CharField(max_length=50, null=True, blank=True)

    # 新增 award 相关字段
    award1_isLeader = models.BooleanField(null=True, blank=True)
    award1_awardTime = models.CharField(max_length=7, null=True, blank=True)
    award1_awardName = models.CharField(max_length=100, null=True, blank=True)
    award1_levelRanking = models.CharField(max_length=50, null=True, blank=True)
    award1_awardRanking = models.CharField(max_length=50, null=True, blank=True)

    award2_isLeader = models.BooleanField(null=True, blank=True)
    award2_awardTime = models.CharField(max_length=7, null=True, blank=True)
    award2_awardName = models.CharField(max_length=100, null=True, blank=True)
    award2_levelRanking = models.CharField(max_length=50, null=True, blank=True)
    award2_awardRanking = models.CharField(max_length=50, null=True, blank=True)

    award3_isLeader = models.BooleanField(null=True, blank=True)
    award3_awardTime = models.CharField(max_length=7, null=True, blank=True)
    award3_awardName = models.CharField(max_length=100, null=True, blank=True)
    award3_levelRanking = models.CharField(max_length=50, null=True, blank=True)
    award3_awardRanking = models.CharField(max_length=50, null=True, blank=True)

    universityLevel = models.CharField(max_length=50, null=True, blank=True)
    masterUniversityLevel = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        db_table = 'students'

    # def __str__(self):
    #     return self.name
