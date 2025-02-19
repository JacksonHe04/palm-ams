from django.db import models

class Percent(models.Model):
    pOfA = models.FloatField(null=True, blank=True)
    pOfB = models.FloatField(null=True, blank=True)
    pOfC = models.FloatField(null=True, blank=True)
    pOfATop = models.FloatField(null=True, blank=True)
    pOfBTop = models.FloatField(null=True, blank=True)
    pOfCTop = models.FloatField(null=True, blank=True)
    pOfATalent = models.FloatField(null=True, blank=True)
    pOfBTalent = models.FloatField(null=True, blank=True)
    pOfCTalent = models.FloatField(null=True, blank=True)

    class Meta:
        db_table = 'percent'