from django.shortcuts import render

# Create your views here.
# cv/views.py
from django.shortcuts import render, redirect
from .forms import PersonalInfoForm, EducationForm, WorkExperienceForm, SkillForm
from .models import PersonalInfo, Education, WorkExperience, Skill

# views.py

from django.shortcuts import render, redirect
from .forms import PersonalInfoForm, EducationForm, WorkExperienceForm, SkillForm
from .models import PersonalInfo

def create_cv(request):
    if request.method == 'POST':
        personal_form = PersonalInfoForm(request.POST, request.FILES)
        education_form = EducationForm(request.POST)
        work_form = WorkExperienceForm(request.POST)
        skill_form = SkillForm(request.POST)

        if personal_form.is_valid() and education_form.is_valid() and work_form.is_valid() and skill_form.is_valid():
            # Save personal info first, so we can use its id in the related models
            personal_info_instance = personal_form.save()

            # Set the personal_info instance in the related models
            education_form.instance.personal_info = personal_info_instance
            work_form.instance.personal_info = personal_info_instance
            skill_form.instance.personal_info = personal_info_instance

            # Save the related models
            education_form.save()
            work_form.save()
            skill_form.save()

            return redirect('view_cv')
        else:
            # Handle form errors
            print(personal_form.errors)
            print(education_form.errors)
            print(work_form.errors)
            print(skill_form.errors)
    else:
        personal_form = PersonalInfoForm()
        education_form = EducationForm()
        work_form = WorkExperienceForm()
        skill_form = SkillForm()

    return render(request, 'create_cv.html', {
        'personal_form': personal_form,
        'education_form': education_form,
        'work_form': work_form,
        'skill_form': skill_form,
    })
# views.py
# views.py
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from .models import PersonalInfo

def download_cv(request, personal_info_id):
    personal_info = PersonalInfo.objects.get(id=personal_info_id)
    
    # Use related names to get associated skills, education, and work experience
    skills = personal_info.skills.all()
    education = personal_info.education.all()
    work_experience = personal_info.work_experience.all()
    
    template = get_template('cv_template.html')
    context = {
        'personal_info': personal_info,
        'skills': skills,
        'education': education,
        'work_experience': work_experience,
    }
    html = template.render(context)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{personal_info.name}_CV.pdf"'

    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response




# views.py

def view_cv(request):
    personal_info = PersonalInfo.objects.last()  # This should grab the most recent PersonalInfo entry
    education = Education.objects.all()
    work_experience = WorkExperience.objects.all()
    skills = Skill.objects.all()

    return render(request, 'view_cv.html', {
        'personal_info': personal_info,
        'education': education,
        'work_experience': work_experience,
        'skills': skills,
    })


