from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200) #creating a character feild and the max amnt of characters is 200
    text = models.TextField() #creating a text box
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True) #putting a date and time next to the publish

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
