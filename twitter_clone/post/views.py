from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import FormView
from django.http import Http404
from .models import Post, Comment
from .forms import PostCreateForm
from django.http.response import JsonResponse
# Create your views here.


@login_required
def index(request):
    context = {"posts" : Post.objects.all().order_by('id')}
    return render(request, 'post/index.html', context)

def new(request):
    if request.method == "POST":
        post = Post.objects.create(user=request.user, text=request.POST['text'])
        return redirect(show, post.pk)
    else:
        return render(request, 'post/new.html')

def show(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        raise Http404
    if request.method == "POST":
        comment = Comment.objects.create(user=request.user, comment=request.POST['comment'], post=post)
        return redirect(show, post.pk)
    else:
        context = {"post":post}
        return render(request, 'post/show.html', context)


def edit(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        raise Http404
    if request.method == "POST":
        post.user = request.user
        post.text=request.POST['text']
        post.save()
        return redirect(show, pk)
    context = {"post":post}
    return render(request, 'post/edit.html', context)

def delete(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        raise Http404
    post.delete()
    return redirect(index)

def comment_delete(request, pk):
    try:
        comment = Comment.objects.get(pk=pk)
        post = comment.post
    except Comment.DoesNotExist:
        raise Http404
    comment.delete()
    return redirect(show,post.pk)

def like(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        raise Http404
    post.like += 1
    post.save()
    return redirect(show, pk)

def like_by_api(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        raise Http404
    post.like += 1
    post.save()
    return JsonResponse({"like":post.like})


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            input_username = form.cleaned_data.get("username")
            input_password = form.cleaned_data.get("password1")
            # ???????????????????????????
            new_user = authenticate(username=input_username, password=input_password)
            if new_user is not None:
                # ??????????????????????????????????????????
                login(request, new_user)
                return redirect("index")
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})


class UserProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'registration/profile.html'
    def get_queryset(self):
        return User.objects.get(id=self.request.user.id)
