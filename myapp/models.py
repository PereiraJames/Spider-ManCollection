from django.db import models

# Create your models here.
class Amazingspiderman(models.Model):
    comicid = models.AutoField(db_column='comicId', primary_key=True)  # Field name made lowercase.
    seriesid = models.IntegerField(db_column='seriesId', blank=True, null=True)  # Field name made lowercase.
    issueid = models.IntegerField(db_column='issueId', blank=True, null=True)  # Field name made lowercase.
    issuenumber = models.IntegerField(db_column='issueNumber', blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(max_length=45, blank=True, null=True)
    img_path = models.TextField(blank=True, null=True)
    img_extension = models.TextField(blank=True, null=True)
    state = models.CharField(max_length=45, blank=True, null=True)
    series_year = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'amazingspiderman'