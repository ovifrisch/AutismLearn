from django.urls import path
from . import views
from . import teacher_views

app_name = 'main'

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("register/", views.register, name="register"),
    path("logout/", views.logout_request, name="logout"),
    path("login/", views.login_request, name="login"),
    path("about/", views.about, name="about"),
    path("new_class/", teacher_views.new_class, name="new_class"),
    path("classes/<the_slug>/", teacher_views.class_slug, name="class_slug")
]
