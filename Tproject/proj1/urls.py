from proj1 import views
from django.views.generic import RedirectView
from django.urls import path
from django.conf.urls import include,url

app_name='proj1'
urlpatterns=[

              
              path('user_register/',views.user_register,name='user_register'),
              url(r'^$',views.user_login,name='user_login'),
              path('test/',views.test,name='test'),
              path('questions_list/',views.questions_list,name='questions_list'),
              url(r'^results/',views.results,name='results'),

              
]