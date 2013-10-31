from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=60)
    createdtm = models.DateTimeField(auto_now=True, auto_now_add=True)

    def __unicode__(self):
        return self.username+';'+self.email

#knowledge like java,javascript.c++,dba
class Knowledge(models.Model):
    name = models.CharField(max_length=100)
    number = models.SmallIntegerField()
    createdtm = models.DateTimeField(auto_now=True, auto_now_add=True)

class KnowledgePoint(models.Model):
    kpoint = models.ManyToManyField(Knowledge)
    question = models.CharField(max_length=500)
    answer = models.CharField(max_length=1000)
    createdtm = models.DateTimeField(auto_now=True, auto_now_add=True)

class KnowledgeTestRecord(models.Model):
    userid = models.IntegerField()
    knowledgeid = models.IntegerField()
    currentkgpid = models.IntegerField() #current knowledgepointid ,like 10/20
    finished = models.BooleanField() #indicate whether the test has been completed
    createdtm = models.DateTimeField(auto_now=True, auto_now_add=True)