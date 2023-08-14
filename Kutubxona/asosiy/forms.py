from django import forms
from .models import *


class TalabaForm(forms.Form):
    ism = forms.CharField(min_length=5,max_length=30)
    k= forms.ChoiceField(choices=((1,1),(2,2),(3,3),(4,4)),label='Kursi:') # Label orqali fieldni nomlash mumkin
    yosh = forms.IntegerField(min_value=16,max_value=45)
    k_s = forms.IntegerField(min_value=0,max_value=8)

class MuallifForm(forms.Form):
    i = forms.CharField(max_length=30,label='Ismi:')
    t_y = forms.IntegerField(label="Tug'ilgan yili")
    t = forms.BooleanField(label='Tirik')
    k_s = forms.IntegerField(label='Kitoblari soni:')
    j = forms.ChoiceField(choices=(('erkak','erkak'),('ayol','ayol')),label='Jinsi:')

# class MuallifForm(forms.ModelForm):
#     class Meta:
#         model = Muallif
#         fields = "__all__"

class KitobForm(forms.ModelForm):
    class Meta:
        model = Kitob
        fields = ['nom','sahifa','janr','muallif']       # yoki '__all__'

class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = '__all__'

class KutubxonachiForm(forms.Form):
    i = forms.CharField(max_length=50,label='Ismi:')
    i_v = forms.CharField(max_length=20,label='Ish vaqti')