from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=20,null=True,blank=True)
    roll=models.CharField(max_length=20,null=True,blank=True)
    city=models.CharField(max_length=20,null=True,blank=True)
    datetime_data=models.DateTimeField(null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Studentclean(models.Model):

    name=models.CharField(max_length=20 ,null=True,blank=True)
    roll=models.CharField(max_length=20 ,null=True,blank=True)
    city=models.CharField(max_length=20 ,null=True,blank=True)
    datetime_data = models.DateTimeField(null=True, blank=True)


class Teacher(models.Model):
    teach_id=models.CharField('techer ref number',max_length=200,null=True,blank=True)
    name = models.CharField('teacher_name',max_length=20, null=True, blank=True)
    roll = models.CharField(max_length=20, null=True, blank=True)
    city = models.CharField(max_length=20, null=True, blank=True)
    datetime_data = models.DateTimeField(null=True, blank=True)


    def save(self,*args,**kwargs):
        self.teach_id=f"{self.name}-00-{self.roll}"
        super(Teacher, self).save(*args, **kwargs)



class clean_properties(models.Model):
    listing_id = models.TextField(null=True, blank=True, unique=True)
    listing_mls_id = models.TextField(null=True, blank=True)
    name = models.CharField(max_length=20, null=True, blank=True)
    acre = models.CharField(max_length=20, null=True, blank=True)
    # agents = models.ManyToManyField('Agent', related_name='properties_of_listing')

    def __str__(self):
        return self.name

class clean_Agent(models.Model):
    listing_id = models.TextField(null=True, blank=True, unique=True)
    agent_name = models.CharField(max_length=30, null=True, blank=True)




class properties(models.Model):
    listing_id = models.TextField(null=True, blank=True)
    listing_mls_id = models.TextField(null=True, blank=True)
    name = models.CharField(max_length=20, null=True, blank=True)
    acre = models.CharField(max_length=20, null=True, blank=True)


    def __str__(self):
        return self.listing_mls_id

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # Check if there is an agent with the same listing_id
        existing_agent = Agent.objects.filter(listing_id=self.listing_id).first()

        if not existing_agent.properties.filter(pk=self.pk).exists():
            existing_agent.properties.add(self)


class Agent(models.Model):
    listing_id = models.TextField(null=True, blank=True)
    agent_name = models.CharField(max_length=30, null=True, blank=True)
    properties = models.ManyToManyField('properties', related_name='agents_of_property',null=True,blank=True)