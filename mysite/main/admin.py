from django.contrib import admin
from .models import Class
from .models import *

# Register your models here.

admin.site.register(Class)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(StudentInterest)
admin.site.register(Assignment)
admin.site.register(GenericQuestion)
admin.site.register(UniqueQuestion)


#
# for model in get_models(get_app('main')):
#     admin.site.register(model)
