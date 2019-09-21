from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from students.views import student_profile,edit_profile
from colleges.views import predict_clg

urlpatterns = [
   path('', views.home , name='homepage'),
   path('sign_up/', views.signup , name='signup'),
   path('sign_up/student_home/', views.student , name='student'),
   path('logout/', views.logout_req , name='logout'),
   path('login/', views.login_req , name='login'),
   path('login/student_home/', views.student , name='student'),
   path('login/student_home/profile/', student_profile , name='profile'),
    path('login/student_home/profile/edit/', edit_profile, name='edit'),
    path('login/student_home/predict/', predict_clg, name='predict'),
   
   
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
