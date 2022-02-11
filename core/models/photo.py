from django.db import models


def get_image_path(instance, filename):
    return 'user_%s' % filename


class Photo(models.Model):
    pic = models.ImageField(upload_to=get_image_path, null=False, blank=False)
    caption = models.CharField(max_length=200)

    def __str__(self):
        return str(self.caption)
