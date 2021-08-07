from django import forms
from .models import StudyMaterials


class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)


class CoursePackForm(forms.ModelForm):

    class Meta:
        model = StudyMaterials
        fields = ['instructor', 'course_title', 'course_code', 'thumbnail']