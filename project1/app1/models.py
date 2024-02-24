from django.db import models

class Tasks(models.Model):
    title = models.CharField(max_length=90)
    complete = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title
     