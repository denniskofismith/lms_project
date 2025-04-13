from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    is_instructor = models.BooleanField(default=False)
    is_student = models.BooleanField(default=True)
    
    def __str__(self):
        return self.user.username
    

class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    # thumbnail =  models.ImageField(upload_to='course_thumbnail/',blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.title}"
    
class Lesson(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE,related_name='lessons')
    title  = models.CharField(max_length=200)
    content = models.TextField()
    order = models.PositiveIntegerField()
    
    def __str__(self):
        return f"{self.order}. {self.title}"
    
    
class Enrollment(models.Model):
    student = models.ForeignKey(User,on_delete=models.CASCADE)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    enrolled_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.student.username} enrolled in {self.course.title}"