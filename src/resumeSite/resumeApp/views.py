from django.shortcuts import render, redirect, get_object_or_404
from django.template import TemplateDoesNotExist, RequestContext
from django.template.loader import render_to_string
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.conf import settings
from django.utils import timezone
from weasyprint import HTML, CSS
from weasyprint.fonts import FontConfiguration
from resumeApp.models import *
from resumeApp.forms import StudentForm, LetterForm
from django.contrib.auth.decorators import login_required
import numpy as np
import os

template_dir = 'resumeApp/resumeTemplate'
app_dir = os.path.dirname(os.path.realpath(__file__))
css_dir = app_dir + '/static/css'
fonts_dir = app_dir + '/static/fonts'


def query_student(user_id):
    try:
        student = Student.objects.get(user_id=user_id)
        context = {
            'student': student,
        }
    except Student.DoesNotExist:
        context = {
            'student': Student()
        }

    return context


@login_required
def index(request):
    is_created_resume = Student.objects.filter(
        user_id=request.user.id).exists()
    is_created_cv = Letter.objects.filter(user_id=request.user.id).exists()
    context = {
        'is_created_resume': is_created_resume,
        'is_created_cv': is_created_cv,
    }
    return render(request, 'resumeApp/index.html', context)


@login_required
def templates(request, template_no):
    '''
        View for templates
    '''
    try:
        respones_html = ''.join([template_dir, template_no, '.html'])
        context = query_student(request.user.id)
        context.update({'template_no': template_no})
        return render(request, respones_html, context)
    except TemplateDoesNotExist:
        return redirect('/templates/view/resume')


@login_required
def to_pdf(request, template_no):
    '''
        Generate PDF file
    '''
    context = query_student(request.user.id)
    context.update({
        'template_no': template_no,
        'is_pdf_view': True
    })
    html_file = ''.join([template_dir, template_no, '.html'])
    html_string = render_to_string(html_file, context)
    html = HTML(string=html_string, base_url=request.build_absolute_uri())
    css = [
        CSS(css_dir + '/screens/common_style.css'),
        CSS(css_dir + '/screens/template'+template_no+'_screen.css'),
    ]
    pdf_file = html.write_pdf(stylesheets=css)
    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="resume.pdf"'

    return response


@login_required
def cv(request, cv_lang, cv_id):
    '''
        View for CVs
    '''
    context = query_student(request.user.id)
    letter = get_object_or_404(Letter, id=cv_id, user_id=request.user.id)

    if cv_lang == 'en':
        respons_html = ''.join(['resumeApp/cv_en.html'])
    else:
        respons_html = ''.join(['resumeApp/cv_th.html'])
    context.update({
        'cv_lang': cv_lang,
        'cv_id': cv_id,
        'letter': letter
    })

    return render(request, respons_html, context)


@login_required
def delete_cv(request, cv_id):
    '''
        Delete CVs
    '''
    letter = get_object_or_404(Letter, id=cv_id, user_id=request.user.id)
    letter.delete()
    return redirect('resumeApp:view_doc', doc_type='cv')


@login_required
def to_pdf_cv(request, cv_lang, cv_id):
    '''
        Generata pdf for CVs
    '''
    context = query_student(request.user.id)
    letter = get_object_or_404(Letter, id=cv_id, user_id=request.user.id)
    context.update({
        'cv_lang': cv_lang,
        'cv_id': cv_id,
        'letter': letter,
        'is_pdf_view': True
    })

    html_file = ''.join(['resumeApp/cv_', cv_lang, '.html'])
    font_config = FontConfiguration()
    html_string = render_to_string(html_file, context)
    html = HTML(string=html_string, base_url=request.build_absolute_uri())
    css = [
        CSS(css_dir + '/scrStudenteens/common_style.css'),
        CSS(fonts_dir + '/thsarabunnew.css', font_config=font_config),
        CSS(css_dir + '/screens/cv_screen.css'),
    ]
    pdf_file = html.write_pdf(stylesheets=css, font_config=font_config)
    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="resume.pdf"'

    return response


@login_required
def view_doc(request, doc_type):
    if doc_type == 'resume':
        context = query_student(request.user.id)
    else:
        context = {
            'student': Student.objects.get(user_id=request.user.id),
            'letter': Letter.objects.filter(user_id=request.user.id)
        }
    html_file = ''.join(['resumeApp/view_', doc_type, '.html'])
    context.update({
        'number_of_template': np.arange(1, 4)
    })

    return render(request, html_file, context)


@login_required
def new_doc(request, doc_type):
    context = query_student(request.user.id)

    if request.POST:
        if doc_type == 'resume':
            cform = StudentForm(
                request,
                data=request.POST,
                files=request.FILES,
                instance=context['student']
            )
            if cform.is_valid():
                new_student = cform.save(commit=False)
                new_student.user_id = request.user.id
                new_student.save()
                cform.save_m2m()
            else:
                print('Error', cform.errors)
        else:
            cform = LetterForm(request, data=request.POST)
            if cform.is_valid():
                new_letter = cform.save(commit=False)
                new_letter.user_id = request.user.id
                new_letter.save()
                cform.save_m2m()
            else:
                print(cform.errors)

        return redirect('resumeApp:view_doc', doc_type=doc_type)

    html_file = ''.join(['resumeApp/new_', doc_type, '.html'])

    if doc_type == 'resume':
        form = StudentForm(request, instance=context['student'])
    else:
        form = LetterForm(request)

    context.update({'form': form})

    return render(request, html_file, context)


@login_required
def edit_cv(request, cv_id):
    if request.POST:
        edit_cv_object = get_object_or_404(Letter, id=cv_id)
        form = LetterForm(
            request,
            data=request.POST or None,
            instance=edit_cv_object
        )
        if form.is_valid():
            update_cv = form.save(commit=False)
            update_cv.user_id = request.user.id
            update_cv.save()
            form.save_m2m()
            cv_lang = form.cleaned_data['language']
            return redirect('resumeApp:cv', cv_lang=cv_lang, cv_id=cv_id)
        else:
            print(form.errors)

    letter = get_object_or_404(Letter, id=cv_id, user_id=request.user.id)
    form = LetterForm(request, instance=letter)
    return render(request, 'resumeApp/new_cv.html', {'form': form})


@login_required
def add_model(request, model):
    if request.POST:
        if model == 'education':
            a_branch = Branch(branch_name=request.POST['branch'])
            a_course = Course(course_name=request.POST['course'])
            a_branch.save()
            a_course.save()
            a_major = Major(
                user_id=request.user.id,
                major_name=request.POST['major'],
                branch=a_branch,
                course=a_course
            )
            a_major.save()
            education_obj = Education(
                **Education.extract_data(request, a_major))
            education_obj.save()

        elif model == 'reference':
            reference_obj = Reference(**Reference.extract_data(request)).save()

        elif model == 'language':
            language_obj = Language(**Language.extract_data(request)).save()

        elif model == 'skill':
            skill_obj = Skill(**Skill.extract_data(request)).save()

        elif model == 'experience':
            experience_obj = Experience(
                **Experience.extract_data(request)).save()

    return redirect('resumeApp:new_doc', doc_type='resume')
