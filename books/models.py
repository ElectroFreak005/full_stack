from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200,default="Title")
    # type = models.CharField(max_length=40)
    isbn = models.CharField(max_length=35,default="ISBN0000")
    author = models.CharField(max_length=100,default="Author")
    av_count = models.IntegerField(default=0)

    def __str__ (self):
        return f"{self.isbn} : {self.title}"

class User(models.Model):
    isbn = models.CharField(max_length=35,default="ISBN0000")
    name = models.CharField(max_length=200,default="User name")
    mail_id = models.CharField(max_length=50,default="example@example.com")
    phno = models.BigIntegerField(default=0000000000)
    resver_id = models.AutoField(primary_key=True)
    status = models.BooleanField(default=True)

    def __str__ (self):
        return f"{self.name} : {self.phno}"