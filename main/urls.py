from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('registerview/', views.registerview, name='registerview'),
    path('loginview/', views.loginview, name='loginview'),
    path('registeruser/', views.registeruser, name='registeruser'),
    path('loginuser/', views.loginuser, name='loginuser'),
    path('logoutuser/', views.logoutuser, name='logoutuser'),
    path('add_information/', views.add_information, name='add_information'),
    path('select_template/', views.select_template, name='select_template'),
    path('ai/',views.ai,name='ai'),
     path('psd/',views.psd,name='psd'),
      path('eps/',views.eps,name='eps'),

      path('resumebegin/',views.resumebegin,name='resumebegin'),
       path('oldresumeadd/',views.oldresumeadd,name='oldresumeadd'),
       path('addpers/',views.addpers,name='addpers'),

       path('addedu',views.addedu,name='addedu'),
       path('addsocial/',views.addsocial,name='addsocial'),
       path('addproject/',views.addproject,name='addproject'),
       path('addcert/',views.addcert,name='addcert'),
       path('addskill/',views.addskill,name='addskill'),
       path('addaddress/',views.addaddress,name='addaddress'),
       path('addstren/',views.addstren,name='addstren'),
       path('addweak/',views.addweak,name='addweak'),
       path('addabout/',views.addabout,name='addabout'),
       path('addhobby/',views.addhobby,name='addhobby'),

       path('addphone/',views.addphone,name='addphone'),
       path('addmail/', views.addmail, name='addmail'),

       path('addjob/',views.addjob,name='addjob'),

       path('gr',views.gr, name='gr'),
    ]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += staticfiles_urlpatterns()