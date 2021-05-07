from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.index, name='index'),
    path('new', views.new, name='new'),
    path('edit', views.edit, name='edit'),
    path("accounts/signup", views.signup, name="signup"),
    path('accountsprofile', views.UserProfileView.as_view(), name="profile"),
]
