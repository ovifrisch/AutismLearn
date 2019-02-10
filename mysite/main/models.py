from django.db import models
from django.conf import settings

class Teacher(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Student(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Class(models.Model):
    name = models.CharField(max_length=50)
    class_code = models.IntegerField(unique=True)
    students = models.ManyToManyField(Student)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, default=None)


    def __str__(self):
        return self.name

class StudentInterest(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Assignment(models.Model):
    name = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    _class = models.ForeignKey(Class, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class GenericQuestion(models.Model):
    number = models.IntegerField()
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    string_representation = models.TextField()

    def __str__(self):
        return self.string_representation


class UniqueQuestion(models.Model):
    generic_question = models.ForeignKey(GenericQuestion, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    string_representation = models.TextField()

    def __str__(self):
        return self.string_representation
