from django.db import models

# Create your models here.
class Tweet(models.Model):
    username = models.CharField(max_length=30)
    tweet = models.CharField(blank=False, null=False, max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username