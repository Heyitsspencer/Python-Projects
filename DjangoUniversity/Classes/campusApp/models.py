from django.db import models

# Create your models here.
class UniversityCampus(models.Model):
    campusName = models.CharField(max_length=60, default="", blank=True, null=False)
    campusID = models.IntegerField(default="", blank=True, null=False)
    state = models.CharField(max_length=2, default="", blank=True, null=False)

    # Creates model manager
    object = models.Manager()

    class Meta:
        verbose_name_plural = "University Campus"