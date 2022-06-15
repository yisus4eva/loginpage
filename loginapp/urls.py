from django.urls import path
from .views import tasklist, taskdetail, taskcreate, taskupdate, taskdelete, customloginview, registerpage
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('login/', customloginview.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='tasks'), name='logout'),
    path('register/', registerpage.as_view(), name='register'),
    path('', tasklist.as_view(), name='tasks'),
    path('task/<int:pk>', taskdetail.as_view(), name='task-detail'),
    path('task-create/', taskcreate.as_view(), name='task-create'),
    path('task-update/<int:pk>', taskupdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>', taskdelete.as_view(), name='task-delete'),
    path('about/', views.about, name='about'),
]