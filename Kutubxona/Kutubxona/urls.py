"""
URL configuration for Kutubxona project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from asosiy.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home_page/',bosh_sahifa),
    path('mashq/',mashq),
    path('talabalar/',hamma_talabalar),
    path('bitiruvchilar/',bitiruvchilar),
    path('bitta_talaba/<int:son>/',bitta_talaba),
    path('mualliflar/',mualliflar),
    path('muallif/<int:son>/',muallif),
    path('hamma_kitoblar/',hamma_kitoblar),
    path('bitta_kitob/<int:son>/',bitta_kitob),
    path('hamma_recordlar/',hamma_recordlar),
    path('tirik_mualliflar/',tirik_mualliflar),
    path('sahifasi_kop/',kitoblar3),
    path('kitobi_kop/',mualliflar3),
    path('recordlar3/',recordlar3),
    path('tirik_m_k/',tirik_m_k),
    path('badiiy_k/',badiiy_k),
    path('qariyalar/',yoshi_katta),
    path('ontadankop/',ontadan_kop),
    path("tanlangan_record/<int:son>/",tanlangan_record),
    path('bitiruvchi_r/',bitiruvchiga_t),
    path('talaba_ochir/<int:son>/',talaba_ochir),
    path('kitob_ochir/<int:son>/',kitob_ochir),
    path('muallif_ochir/<int:son>/',muallif_ochir),
    path('record_ochir/<int:son>/',record_ochir),
    path('kutubxonachilar/',kutubxonachilar),
    path('kutubxonachi_ochir/<int:son>/',kutubxonachi_ochir),
    path('talaba_update/<int:son>/', talaba_update),
    path('kitob_update/<int:son>/', kitob_update),
    path('kutubxonachi_update/<int:son>/', kutubxonachi_update),
    path('muallif_update/<int:son>/',muallif_update),
    path('record_update/<int:son>/',record_update),
    path('',login_view),
    path('logout/',logout_view),
    path('register/',register)
]
