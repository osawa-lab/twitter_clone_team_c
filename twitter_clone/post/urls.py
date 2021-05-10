from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('new', views.new, name='new'),
    path('', views.index, name='index'),
    path('<int:pk>', views.show, name='show'),
    path('<int:pk>/edit', views.edit, name='edit'),
    path('<int:pk>/delete', views.delete, name='delete'),
    path('comment/<int:pk>/delete', views.comment_delete, name='comment_delete'),
    path('<int:pk>/like', views.like, name='like'),
    path('<int:pk>/like_by_api', views.like_by_api, name='like_by_api'),
    path("accounts/signup", views.signup, name="signup"),
    path('accounts/profile', views.UserProfileView.as_view(), name="profile"),
]
