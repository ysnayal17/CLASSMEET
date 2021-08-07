from django.contrib import admin
from Home.models import Contact
from Home.models import Study_Materials
from Home.models import Questions
from Home.models import Answers
# Register your models here.
admin.site.register(Contact)
admin.site.register(Study_Materials)
admin.site.register(Questions)
admin.site.register(Answers)

