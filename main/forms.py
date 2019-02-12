from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Teacher
from .models import Student
from .models import Class


class SignUpForm(UserCreationForm):
    type = forms.BooleanField(required=False, help_text='Are you a Student?')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=True)
        if (self.cleaned_data['type']):
            student = Student(user=user)
            student.save()
        else:
            teacher = Teacher(user=user)
            teacher.save()

        return user

    def clean(self):
        return self.cleaned_data



class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ('name', 'class_code')


class JoinClassForm(forms.Form):
    join_code = forms.IntegerField()
    join_code.label = "Enter the Class Code Your Teacher Gave You"


class AssignmentForm(forms.Form):
    assignment_name = forms.CharField(max_length=50)

    def save():
        return
