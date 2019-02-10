from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ClassForm
from django.contrib import messages


def new_class(request):
    if (request.method == "POST"):
        form = ClassForm(request.POST)
        if (form.is_valid()):
            class_ = form.save(commit=False)
            class_.teacher = request.user.teacher
            class_.save()
            name = form.cleaned_data.get('name')
            code = form.cleaned_data.get('class_code')
            messages.success(request, f"New Class Created: {name} with code {code}")
            return redirect("main:homepage")

        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}:{form.error_messages[msg]}")


    form = ClassForm()
    return render(request=request, template_name="main/new_class.html", context={"user":request.user, "form":form})
