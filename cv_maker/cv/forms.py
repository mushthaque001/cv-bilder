# forms.py

from django import forms
from .models import PersonalInfo, Education, WorkExperience, Skill

class PersonalInfoForm(forms.ModelForm):
    class Meta:
        model = PersonalInfo
        fields = ['name', 'email', 'phone', 'address']

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['school_name', 'degree', 'start_date', 'end_date', 'description']

class WorkExperienceForm(forms.ModelForm):
    class Meta:
        model = WorkExperience
        fields = ['company_name', 'position', 'start_date', 'end_date', 'responsibilities']

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['name', 'proficiency']
