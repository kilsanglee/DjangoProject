from django.db import models

# Create your models here.
class Board(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    today = models.DateTimeField(auto_now_add=True)

    # cnt 추가
    cnt = models.IntegerField(default=0)

    def __str__(self):
        return self.title
