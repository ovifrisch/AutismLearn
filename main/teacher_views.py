from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ClassForm
from django.contrib import messages
from .models import Class, Assignment


def create_slug(name):
	return name.lower().replace(" ", "_")

def class_slug(request, the_slug):
	class_slugs = [c.class_slug for c in Class.objects.all()]
	if (the_slug in class_slugs):
		class_ = Class.objects.get(class_slug=the_slug)
		return render(request=request, template_name="main/class.html", context={"user":request.user, "class":class_})
	else:
		return HttpResponseNotFound('<h1>Page not found</h1>')


def new_assignment(request):
	if (request.method == "POST"):
		print(request.POST)
		# assignment = Assignment()
		# assignment.name = request.POST["name"]
		# assignment.slug = create_slug(assignment.name)
		# assignment._class =
		return HttpResponse("Success!")
		# return render(request=request, template_name="main/new_assignment.html", context={"user":request.user})
	else:
		return render(request=request, template_name="main/new_assignment.html", context={"user":request.user})

def new_class(request):
	if (request.method == "POST"):
		form = ClassForm(request.POST)
		if (form.is_valid()):
			class_ = form.save(commit=False)
			name = form.cleaned_data.get('name')
			code = form.cleaned_data.get('class_code')
			class_.teacher = request.user.teacher
			class_.class_slug = create_slug(name)
			class_.save()
			messages.success(request, f"New Class Created: {name} with code {code}")
			return redirect("main:homepage")

		else:
			messages.error(request, f"class code and class name must be unique")


	form = ClassForm()
	return render(request=request, template_name="main/new_class.html", context={"user":request.user, "form":form})
