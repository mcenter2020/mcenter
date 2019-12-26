from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from django.urls import reverse


from .models import Post, Tag
from .utils import ObjectDetailMixin, ObjectListMixin, ObjectCreateMixin, ObjectUpdateMixin, ObjectDeleteMixin
from .forms import TagForm, PostForm

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator

from django.db.models import Q
# Create your views here.
def posts_list(request):
    search_query = request.GET.get('search', '')
    if search_query:
        page_object = Post.objects.filter(Q(title__icontains=search_query) | Q(body__icontains=search_query))
    else:
        page_object = Post.objects.all()

    paginator = Paginator(page_object, 2)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    is_paginated = page.has_other_pages()

    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''

    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''

    context = {
        'page_object': page,
        'is_paginated': is_paginated,
        'next_url': next_url,
        'prev_url': prev_url
}

    return render(request, 'blog/posts_list.html', context=context)

class TagsList(ObjectListMixin, View):
    model = Tag
    template = 'blog/tags_list.html'



class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'blog/post_detail.html'


class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'blog/tag_detail.html'


class TagCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    model_form = TagForm
    template = 'blog/tag_create.html'
    raise_exception = False


class PostCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    model_form = PostForm
    template = 'blog/post_create_form.html'
    raise_exception = False


class TagUpdate(LoginRequiredMixin, ObjectUpdateMixin,View):
    model = Tag
    model_form = TagForm
    template = 'blog/tag_update_form.html'
    raise_exception = False

class PostUpdate(LoginRequiredMixin, ObjectUpdateMixin,View):
    model = Post
    model_form = PostForm
    template = 'blog/post_update_form.html'
    raise_exception = False


class TagDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Tag
    template = 'blog/tag_delete_form.html'
    redirect_url = 'tags_list_url'
    raise_exception = False


class PostDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Post
    template = 'blog/post_delete_form.html'
    redirect_url = 'posts_list_url'
    raise_exception = False


def names_list(request):
    n = ['Aleksey', 'Nikolay', 'Oleg']
    return render(request, 'blog/index2.html', context={'names': n})