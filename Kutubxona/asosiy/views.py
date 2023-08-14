from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def bosh_sahifa(request):
    return render(request,'bosh_sahifa.html')

def mashq(request):
    content = {
        "ism":"Jamshid",
        "yosh":21
    }
    return render(request,'mashq.html',content)

def hamma_talabalar(request):
    if request.method == 'POST':
        forma = TalabaForm(request.POST)
        if forma.is_valid():
            Talaba.objects.create(
                ism = forma.cleaned_data.get('ism'),
                kurs = forma.cleaned_data.get('k'),
                yosh = forma.cleaned_data.get('yosh'),
                kitob_soni = forma.cleaned_data.get('k_s')
            )
        return redirect('/talabalar/')
    soz = request.GET.get('qid_soz')
    natija = Talaba.objects.all()
    if soz:
        natija = Talaba.objects.filter(ism__contains=soz)
    content = {
        "talabalar": natija,
        "forma":TalabaForm()
    }
    return render(request,'talabalar.html',content)

def bitiruvchilar(request):
    content = {
        "bitiruvchilar":Talaba.objects.filter(kurs=4)
    }
    return render(request,'mashq_uchun/bitiruvchi.html',content)

def bitta_talaba(request,son):
    content = {
        "talaba": Talaba.objects.get(id=son)
    }
    return render(request,'mashq_uchun/talaba.html',content)

def mualliflar(request):
    if request.method == 'POST':
        forma = MuallifForm(request.POST)
        if forma.is_valid():
            Muallif.objects.create(
                ism = forma.cleaned_data.get('i'),
                tugilgan_yil = forma.cleaned_data.get('t_y'),
                tirik = forma.cleaned_data.get('t'),
                kitoblari_soni = forma.cleaned_data.get('k_s'),
                jinsi = forma.cleaned_data.get('j')

            )
            # forma.save()
        return redirect('/mualliflar/')
    soz = request.GET.get('qid_soz')
    natija = Muallif.objects.all()
    if soz:
        natija = Muallif.objects.filter(ism__contains = soz)
    content = {
        "mualliflar": natija,
        "forma":MuallifForm
    }
    return render(request,'mashq_uchun/mualliflar.html',content)

def muallif(request,son):
    content = {
        "muallif":Muallif.objects.get(id=son)
    }
    return render(request,'mashq_uchun/muallif.html', content)

def hamma_kitoblar(request):
    if request.method == 'POST':
        forma = KitobForm(request.POST)
        if forma.is_valid():
        # Kitob.objects.create(
        #     nom = request.POST.get('n'),
        #     sahifa=request.POST.get('s'),
        #     janr=request.POST.get('j'),
        #     muallif=Muallif.objects.get(id=request.POST.get('m'))
        # )
            forma.save()
        return redirect('/hamma_kitoblar/')
    soz = request.GET.get('qid_soz')
    natija = Kitob.objects.all()
    if soz:
        natija=Kitob.objects.filter(nom__contains=soz)
        natija=natija|Kitob.objects.filter(muallif__ism__contains=soz)
    content = {
        "kitoblar": natija,
        "mualliflar": Muallif.objects.all(),
        "forma":KitobForm()
    }
    return render(request,'hamma_kitoblar.html',content)

def bitta_kitob(request,son):
    content = {
        "kitob":Kitob.objects.get(id=son)
    }
    return render(request,'mashq_uchun/bitta_kitob.html',content)\

def hamma_recordlar(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            if Record.talaba.user == request.user:
                if request.POST.get('q') == 'on':
                    n = True
                else:
                    n = False
                Record.objects.create(
                    talaba=Talaba.objects.get(id=request.POST.get('t')),
                    kitob=Kitob.objects.get(id=request.POST.get('k')),
                    kutubxonachi=Kutubxonachi.objects.get(id=request.POST.get('k_i')),
                    olingan_sana=request.POST.get('o_s'),
                    qaytardi=n,
                    qaytarish_sanasi=request.POST.get('q_s')
                )
                return redirect('/hamma_recordlar/')
        soz = request.GET.get('qid_soz')
        natija = Record.objects.all()
        if soz:
            natija = Record.objects.filter(talaba__ism__contains = soz)
        content = {
            "recordlar":natija,
            "tala   balar": Talaba.objects.all(),
            "kitoblar": Kitob.objects.all(),
            "kutubxonachilar":Kutubxonachi.objects.all(),
            "forma":RecordForm()
        }
        return render(request,'hamma_recordlar.html',content)

def tirik_mualliflar(request):
    content = {
        "tiriklar":Muallif.objects.filter(tirik=True)
    }
    return render(request,'mashq_uchun/tirik_mualliflar.html',content)

def kitoblar3(request):
    content = {
        "kitoblar3":Kitob.objects.all().order_by("-sahifa")[:3]
    }
    return render(request,'mashq_uchun/kitoblar3.html',content)

def mualliflar3(request):
    content = {
        "mualliflar3":Muallif.objects.all().order_by("-kitoblari_soni")[:3]
    }
    return render(request,'mashq_uchun/kitobi_kop.html',content)

def recordlar3(request):
    content = {
        "recordlar3":Record.objects.all().order_by("-olingan_sana")[:3]
    }
    return render(request,'mashq_uchun/recordlar3.html',content)

def tirik_m_k(request):
    content = {
        "tirik_m_k":Kitob.objects.filter(muallif__tirik=True)
    }
    return render(request,'mashq_uchun/tirik_m_k.html',content)

def badiiy_k(request):
    content = {
        "badiiylar":Kitob.objects.filter(janr="badiiy")
    }
    return render(request,'mashq_uchun/badiiy_k.html',content)

def yoshi_katta(request):
    content = {
        "qariyalar":Muallif.objects.all().order_by("tugilgan_yil")[:3]
    }
    return render(request,'mashq_uchun/qariya.html',content)

def ontadan_kop(request):
    content = {
        "ontadan_kop":Muallif.objects.filter(kitoblari_soni__gt=10)
    }
    return render(request,'mashq_uchun/ontadankop.html',content)

def tanlangan_record(request,son):
    content = {
        "tanlangan_record":Record.objects.get(id=son)
    }
    return render(request,'mashq_uchun/t_record.html',content)

def bitiruvchiga_t(request):
    content = {
        "bitiruvchiga_t":Record.objects.filter(talaba__kurs=4)
    }
    return render(request,'mashq_uchun/bitiruvchiga_t.html',content)

def talaba_ochir(request, son):
    Talaba.objects.get(id=son).delete()
    return redirect("/talabalar/")

def kitob_ochir(request, son):
    Kitob.objects.get(id=son).delete()
    return redirect("/hamma_kitoblar/")

def muallif_ochir(requests, son):
    Muallif.objects.get(id=son).delete()
    return redirect('/mualliflar/')

def record_ochir(requests, son):
    Record.objects.get(id=son).delete()
    return redirect('/hamma_recordlar/')


def kutubxonachilar(request):
    if request.method == 'POST':
        forma = KutubxonachiForm(request.POST)
        if forma.is_valid():
            Kutubxonachi.objects.create(
                ism = forma.cleaned_data.get('i'),
                ish_vaqti = forma.cleaned_data.get('i_v')
            )
        return redirect('/kutubxonachilar/')
    soz = request.GET.get('qid_soz')
    natija = Kutubxonachi.objects.all()
    if soz:
        natija = Kutubxonachi.objects.filter(ism__contains=soz)
    content = {
        "kutubxonachilar":natija,
        "forma":KutubxonachiForm()
    }
    return render(request,'kutubxonachilar.html',content)

def kutubxonachi_ochir(request,son):
    Kutubxonachi.objects.get(id=son).delete()
    return redirect('/kutubxonachilar/')

def talaba_update(request,son):
    if request.method == 'POST':
        Talaba.objects.filter(id=son).update(
            kurs = request.POST.get('k'),
            yosh = request.POST.get('y'),
            kitob_soni = request.POST.get('k_s')
        )
        return redirect('/talabalar/')
    content = {
        "talaba":Talaba.objects.get(id=son)
    }
    return render(request,"talaba_update.html",content)

def kitob_update(request,son):
    if request.method == 'POST':
        Kitob.objects.filter(id=son).update(
            muallif = Muallif.objects.get(id=request.POST.get('m')),
            sahifa = request.POST.get('s'),
            janr = request.POST.get('j')
        )
        return redirect('/hamma_kitoblar/')
    content = {
        "kitob":Kitob.objects.get(id=son),
        "mualliflar":Muallif.objects.all()
    }
    return render(request,"kitob_update.html",content)

def kutubxonachi_update(request, son):
    if request.method == 'POST':
        Kutubxonachi.objects.filter(id=son).update(
            ism = request.POST.get('i'),
            ish_vaqti = request.POST.get('i_v')
        )
        return redirect('/kutubxonachilar/')
    content = {
        "kutubxonachi":Kutubxonachi.objects.get(id=son)
    }
    return render(request,"kutubxonachi_update.html",content)

def muallif_update(request, son):
    if request.method == 'POST':
        if request.POST.get('t') == 'on':
            n = True
        else:
            n = False
        Muallif.objects.filter(id=son).update(
            ism=request.POST.get('i'),
            tugilgan_yil = request.POST.get('t_y'),
            tirik = n,
            kitoblari_soni = request.POST.get('k_s'),
            jinsi = request.POST.get('j')
        )
        return redirect('/mualliflar/')
    content = {
        "muallif":Muallif.objects.get(id=son)
    }
    return render(request,"muallif_update.html",content)

def record_update(request, son):
    if request.method == 'POST':
        forma = RecordForm(request.POST)
        if forma.cleaned_data.get('qaytardi') == False:
            if request.POST.get('q') == 'on':
                n = True
            else:
                n = False
            Record.objects.filter(id=son).update(
                qaytardi=n,
                qaytarish_sanasi = request.POST.get('q_s')
            )
        return redirect('/hamma_recordlar/')
    content = {
        "record":Record.objects.get(id=son),
        "forma":RecordForm()
    }
    return render(request,"record_update.html",content)

def login_view(request):
    if request.method == 'POST':
        user = authenticate(
            username = request.POST.get('l'),
            password = request.POST.get('p')
        )
        if user is not None:
            login(request,user)
            return redirect('home_page/')
        return redirect('/')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('/')

def register(request):
    if request.method == 'POST':
        u = User.objects.create_user(
            username=request.POST.get('l'),
            password=request.POST.get('p')
        )
        Talaba.objects.create(
            ism = request.POST.get('i'),
            kurs = int(request.POST.get('k')),
            universitet = request.POST.get('u'),
            user = u

        )
        return redirect('/')
    return render(request,'register.html')






