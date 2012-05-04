# -*- coding:utf-8 -*-
from django.db import models
from django import forms
from django.forms import ModelForm,Textarea,CharField,Form,FileField,IntegerField


class Sumbit(models.Model):
    id = models.CharField(max_length=14,primary_key=True)
    #title = models.CharField(max_length=765)
    file = models.CharField(max_length=300, blank=True)
    string_text = models.TextField(blank=True)
    binary_text = models.TextField(blank=True)

    class Meta:
        db_table = u'sumbit'

class TextForm(ModelForm):
    #title = forms.CharField(max_length = 300,label = '名字')
    #string_text = forms.CharField(required=False,label='内容',widget=forms.Textarea(attrs={'rows':'8','cols':'100'}))
    string_text = CharField(required=False,label='内容',widget=Textarea(attrs={'rows':'8','cols':'100'}))  

    class Meta:
        model = Sumbit
        #fileds = ('string_text',)
        exclude = ('file','binary_text')
        #exclude = ('id','file','binary_text')
        widgets = { 
        	'string_text':Textarea(attrs={'rows':'8','cols':'100'})
        }

    def __unicode__(self):
        return self.id

class BinaryForm(ModelForm):
    #title = forms.CharField(max_length = 300,label = '名字')
    #string_text = forms.CharField(required=False,label='内容',widget=forms.Textarea(attrs={'rows':'8','cols':'100'}))
    binary_text = CharField(required=False,label='内容',widget=Textarea(attrs={'rows':'8','cols':'100'}))  

    class Meta:
        model = Sumbit
        #fileds = ('string_text',)
        exclude = ('file','string_text')
        widgets = { 
        	'binary_text':Textarea(attrs={'rows':'8','cols':'100'})
        }

    def __unicode__(self):
        return self.id
       
class FileForm(ModelForm):
    #title = forms.CharField(max_length = 300,label = '名字')
    #string_text = forms.CharField(required=False,label='内容',widget=forms.Textarea(attrs={'rows':'8','cols':'100'}))
    file = CharField(required=False,label='链接')  

    class Meta:
        model = Sumbit
        #fileds = ('string_text',)
        exclude = ('binary_text','string_text')
        

    def __unicode__(self):
        return self.id
 
class UploadFileForm(Form):
    upfile = FileField()

