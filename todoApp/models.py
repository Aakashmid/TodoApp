from django.db import models

# Create your models here.
class Tasks(models.Model):
    sno=models.AutoField(primary_key=True)
    taskDesc=models.CharField( max_length=100)
    time=models.DateTimeField( auto_now=False, auto_now_add=False)
    def __str__(self):
        return self.taskDesc[0:100]
    

    