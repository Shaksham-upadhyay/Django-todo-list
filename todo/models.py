from django.db import models

# Create your models here.
class Todo(models.Model):
    # name=models.C
    title=models.CharField(max_length=100)
    iscompleted=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)
    completed=models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return self.title