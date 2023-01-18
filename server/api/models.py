from django.db import models


class Post(models.Model):
    picture = models.ImageField(upload_to="picture/images", null=False, blank=False)
    caption = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.caption
