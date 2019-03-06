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
	name = models.CharField(max_length=50, unique=True)
	class_code = models.IntegerField(unique=True)
	class_slug = models.CharField(max_length=200, default=1)
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
	due_date = models.DateTimeField(null=True)
	assignment_slug = models.CharField(max_length=200, default=1)
	_class = models.ForeignKey(Class, on_delete=models.CASCADE)

	def __str__(self):
		return self.name

class GenericQuestion(models.Model):
	number = models.IntegerField()
	string_representation = models.TextField()
	assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)


	def __str__(self):
		return self.string_representation


class UniqueQuestion(models.Model):
	generic_question = models.ForeignKey(GenericQuestion, on_delete=models.CASCADE)
	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	string_representation = models.TextField()

	def __str__(self):
		return self.string_representation
