from django.shortcuts import render, get_object_or_404, redirect
from weasyprint import HTML, CSS
from django.template.loader import get_template
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.utils import timezone
from django.contrib.auth import authenticate
from .forms import PostForm
from .models import Name_list


def plist(request):
    posts = Name_list.objects.all()
    return render(request, 'name_base/plist.html', {'posts': posts})


def inform(request, slug):
    post = get_object_or_404(Name_list, slug=slug)
    return render(request, 'name_base/inform.html', {'post': post})





def inform_pdf(request, slug):
    post = get_object_or_404(Name_list, slug=slug)
    html_string = render_to_string ('name_base/inform_pdf.html',{'post': post})
    pdf_file = HTML(string=html_string).write_pdf()
    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = 'filename="home_page.pdf"'
    return response


# Create your views here."""

def personal(request):

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('inform', slug=post.slug)
    else:
        form = PostForm()
    return render(request, 'name_base/personal.html', {'form': form})

def inform_edit(request, slug):
    post = get_object_or_404(Name_list, slug=slug)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('inform', slug=post.slug)
    else:
        form = PostForm(instance=post)
    return render(request, 'name_base/personal.html', {'form': form})

