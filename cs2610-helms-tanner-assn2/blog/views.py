import datetime
from django.urls import reverse
from django.utils.timezone import make_aware
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from blog.models import Blog, Comments
from polls.models import Question


def index(request):
    blogs = Blog.objects.order_by('-posted')[:3]
    context = {'blogs': blogs, 'time': datetime.datetime.now()}
    return render(request, 'blog/index.html', context)


def archive(request):
    blogs = Blog.objects.order_by('-posted')
    comments = Comments.objects.order_by("-posted")
    context = {'blogs': blogs, 'comments': comments, 'time': datetime.datetime.now()}
    return render(request, 'blog/index.html', context)


def about(request):
    context = {'time': datetime.datetime.now()}
    return render(request, 'blog/about.html', context)


def techtipscss(request):
    context = {'time': datetime.datetime.now()}
    return render(request, 'blog/techtips+css.html', context)


def techtips(request):
    context = {'time': datetime.datetime.now()}
    return render(request, 'blog/techtips-css.html', context)


def plan(request):
    context = {'time': datetime.datetime.now()}
    return render(request, 'blog/plan.html', context)


def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    comments = Comments.objects.filter(blog=blog)
    context = {'blog': blog, 'comments': comments, 'comment_count': len(comments), 'time': datetime.datetime.now()}
    return render(request, 'blog/detail.html', context)


def comment(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    comments = Comments()
    comments.commenter = request.POST['name']
    comments.email = request.POST['email']
    comments.content = request.POST['comment']
    comments.posted = make_aware(datetime.datetime.now())
    comments.blog = blog
    comments.save()
    return HttpResponseRedirect(reverse('blog:detail', args=[blog_id]))
