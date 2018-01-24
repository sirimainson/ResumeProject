from django.shortcuts import render, redirect
from django.template import TemplateDoesNotExist
from django.template.loader import render_to_string
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.conf import settings
from weasyprint import HTML, CSS
from weasyprint.fonts import FontConfiguration
from .forms import StudentForm 
import os

template_dir = 'resumeApp/resumeTemplate'
css_dir = os.getcwd() + '/resumeApp/static/css'
fonts_dir = os.getcwd() + '/resumeApp/static/fonts'


def index(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = StudentForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponse('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = StudentForm()
    return render(request, 'resumeApp/index.html', {'form': form})


def templates(request, template_no):
    '''
        View for templates
    '''
    try:
        respones_html = ''.join([template_dir, template_no, '.html'])
        context = {'template_no': template_no}
        return render(request, respones_html, context)
    except TemplateDoesNotExist:
        return redirect(templates, template_no=1)


def to_pdf(request, template_no):
    '''
        Generate PDF file
    '''
    html_file = ''.join([template_dir, template_no, '.html'])
    html_string = render_to_string(html_file, {'is_pdf_view': True})
    html = HTML(string=html_string, base_url=request.build_absolute_uri())
    css = [
        CSS(css_dir + '/screens/common_style.css'),
        CSS(css_dir + '/screens/template'+template_no+'_screen.css'),
    ]
    pdf_file = html.write_pdf(stylesheets=css)
    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="resume.pdf"'

    return response


def cv(request, cv_lang):
    '''
        View for CVs
    '''
    if cv_lang == 'en':
        respons_html = ''.join(['resumeApp/cv_en.html'])
    else:
        respons_html = ''.join(['resumeApp/cv_th.html'])
    context = {'cv_lang': cv_lang}

    return render(request, respons_html, context)

def to_pdf_cv(request, cv_lang):
    '''
        Generata pdf for CVs
    '''
    html_file = ''.join(['resumeApp/cv_', cv_lang, '.html'])
    font_config = FontConfiguration()
    html_string = render_to_string(html_file, {'is_pdf_view': True})
    html = HTML(string=html_string, base_url=request.build_absolute_uri())
    css = [
        CSS(css_dir + '/screens/common_style.css'),
        CSS(fonts_dir + '/thsarabunnew.css', font_config=font_config),
        CSS(css_dir + '/screens/cv_screen.css'),
    ]
    pdf_file = html.write_pdf(stylesheets=css, font_config=font_config)
    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="resume.pdf"'

    return response
