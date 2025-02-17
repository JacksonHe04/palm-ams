from django.db import models

class Apply(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=50, null=True, blank=True)
    applicationType = models.CharField(max_length=50, null=True, blank=True)
    graduationYear = models.IntegerField(null=True, blank=True)
    university = models.CharField(max_length=50, null=True, blank=True)
    universityLevel = models.CharField(max_length=50, null=True, blank=True)
    major = models.CharField(max_length=50, null=True, blank=True)
    majorCount = models.IntegerField(null=True, blank=True)
    rank = models.IntegerField(null=True, blank=True)
    percentage = models.CharField(max_length=10, null=True, blank=True)
    masterUniversity = models.CharField(max_length=50, null=True, blank=True)
    masterUniversityLevel = models.CharField(max_length=50, null=True, blank=True)
    masterMajor = models.CharField(max_length=50, null=True, blank=True)
    tutor = models.CharField(max_length=50, null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)
    birthDate = models.CharField(max_length=20, null=True, blank=True)
    photo = models.ImageField(upload_to='apply/', null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    firstChoice = models.CharField(max_length=50, null=True, blank=True)
    secondChoice = models.CharField(max_length=50, null=True, blank=True)
    thirdChoice = models.CharField(max_length=50, null=True, blank=True)
    isAdjustable = models.BooleanField(default=True)
    proofs = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=50, null=True, blank=True)

    # Paper related fields
    paper1_publicationTime = models.CharField(max_length=7, null=True, blank=True)
    paper1_journalConference = models.CharField(max_length=100, null=True, blank=True)
    paper1_paperName = models.CharField(max_length=100, null=True, blank=True)
    paper1_ccfLevel = models.CharField(max_length=10, null=True, blank=True)
    paper1_isFirst = models.BooleanField(null=True, blank=True)

    paper2_publicationTime = models.CharField(max_length=7, null=True, blank=True)
    paper2_journalConference = models.CharField(max_length=100, null=True, blank=True)
    paper2_paperName = models.CharField(max_length=100, null=True, blank=True)
    paper2_ccfLevel = models.CharField(max_length=10, null=True, blank=True)
    paper2_isFirst = models.BooleanField(null=True, blank=True)

    paper3_publicationTime = models.CharField(max_length=7, null=True, blank=True)
    paper3_journalConference = models.CharField(max_length=100, null=True, blank=True)
    paper3_paperName = models.CharField(max_length=100, null=True, blank=True)
    paper3_ccfLevel = models.CharField(max_length=10, null=True, blank=True)
    paper3_isFirst = models.BooleanField(null=True, blank=True)

    # Award related fields
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

    # Additional fields from fieldsInApply.json
    isTopClass = models.BooleanField(null=True, blank=True)
    firstAuthorLevel = models.CharField(max_length=50, null=True, blank=True)
    isPaperCondition = models.BooleanField(null=True, blank=True)
    isAwardCondition = models.BooleanField(null=True, blank=True)
    isFilterCondition = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        db_table = 'students'

    # def __str__(self):
    #     return self.name
