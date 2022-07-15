from django.urls import path ,include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('home',views.home,name='home'),
    path('sem1',views.sem1,name='sem1'),
    path('sem2',views.sem2,name='sem2'),
    path('sem3',views.sem3,name='sem3'),
    path('sem4',views.sem4,name='sem4'),
    path('sem5',views.sem5,name='sem5'),
    path('sem6',views.sem6,name='sem6'),
    path('sem7',views.sem7,name='sem7'),
    path('sem8',views.sem8,name='sem8'),
    # path('reg',views.register,name='registeration'),
    path('',auth_views.LoginView.as_view(template_name='login.html'),name='login')
]