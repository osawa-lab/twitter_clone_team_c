from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from post.models import Post
# Create your views here.


@login_required
def index(request):
  posts = Post.objects.all().order_by('id')
  return render(request, 'post/index.html', {'posts': posts})

def new(request):
  return render(request, 'post/new.html')

def edit(request):
  return render(request, 'post/edit.html')


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            input_username = form.cleaned_data.get("username")
            input_password = form.cleaned_data.get("password1")
            # ユーザーを認証する
            new_user = authenticate(username=input_username, password=input_password)
            if new_user is not None:
                # ユーザーをログイン状態にする
                login(request, new_user)
                return redirect("index")
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})


class UserProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'registration/profile.html'
    def get_queryset(self):
        return User.objects.get(id=self.request.user.id)
