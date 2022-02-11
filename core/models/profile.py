from django.db import models


class Article(models.Model):
    user = models.ForeignKey("core.User")
    pic = models.ForeignKey("core.Photo", null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title


class Career(models.Model):
    SCHOOL = 1
    WORK = 2
    LIFE = 3
    CAREER_TYPE = ((SCHOOL, "School"), (WORK, "Work"), (LIFE, "Life"),)
    user = models.ForeignKey("core.User")
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    pic = models.ForeignKey("core.Photo", null=True, blank=True)
    career_type = models.SmallIntegerField(choices=CAREER_TYPE, default=SCHOOL)
    career_name = models.CharField(max_length=512)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.career_name

    def get_career_type(self):
        return self.CAREER_TYPE[self.career_type - 1][1]
