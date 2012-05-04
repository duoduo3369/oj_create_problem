# -*- coding:utf-8 -*-
from django.shortcuts import render_to_response
from django import forms
from django.http import HttpResponseRedirect
from CatchShow.submit.models import TextForm,BinaryForm,UploadFileForm,FileForm
#from django.core.context_processors import csrf
from django.template import RequestContext
from django.core.urlresolvers import reverse
#from django.core.files import File
from django.core.files.base import ContentFile
from django.http import settings
import os
import time

curtime = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))

def submit_type_select(request):
	curtime = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
	if request.method != 'POST':
		return render_to_response('submit.html',
							  context_instance=RequestContext(request)
							 )	
	first_select = request.POST.get('first_select')
	second_select = request.POST.get('second_select')
	if first_select == 'code':
		if second_select == 'string':
			form = TextForm({'id':curtime})
			return render_to_response('submitString.html',
							  {'form': form},
							  context_instance=RequestContext(request)
							 )
		if second_select == 'binary':
			form = BinaryForm({'id':curtime})
			return render_to_response('submitBinary.html',
							  {'form': form},
							  context_instance=RequestContext(request)
							 )
		if second_select == 'file':
			form = TextForm({'id':curtime})
			return render_to_response('submitStringToFile.html',
							  {'form': form},
							  context_instance=RequestContext(request)
							 )
	if first_select == 'file':
		form = UploadFileForm()
		if second_select == 'file':			
			return render_to_response('submitFile.html',
							  {'form': form},
							  context_instance=RequestContext(request)
							 )
		if second_select == 'string':
			return render_to_response('submitFileToString.html',
							  {'form': form},
							  context_instance=RequestContext(request)
							 )
		if second_select == 'binary':
			return render_to_response('submitFileToBinary.html',
							  {'form': form},
							  context_instance=RequestContext(request)
							 )
	return 	render_to_response('test_submit.html',
							  {'first_select': first_select , 'second_select':second_select},
							  context_instance=RequestContext(request)
							 )

def submit_string(request):
	if request.method == 'POST':		
		form = TextForm(request.POST)
		
		if form.is_valid():			
			form.save()
			return HttpResponseRedirect(reverse('CatchShow.submit.views.submitSuccess'))			
	else:
		form = TextForm()
	return render_to_response('submitString.html',
							  {'form': form},
							  context_instance=RequestContext(request)
							 )
							
							
def submit_binary(request):
	if request.method == 'POST':		
		form = BinaryForm(request.POST)
		
		if form.is_valid():			
			form.save()
			return HttpResponseRedirect(reverse('CatchShow.submit.views.submitSuccess'))			
	else:
		form = BinaryForm()
	return render_to_response('submitBinary.html',
							  {'form': form},
							  context_instance=RequestContext(request)
							 )		
							 
						 
def submit_string_to_file(request):
	if request.method == 'POST':		
		form = TextForm(request.POST)
		store = request.POST['string_text']
		store_file = ContentFile(store.encode('UTF-8'))
		if form.is_valid():
			curtime = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
			file_type = '.txt'
			file_name = curtime + file_type
			file_path = 'files/'
			handle_uploaded_file(f = store_file, filename = file_name, filepath = file_path)
			path = os.path.join(settings.MEDIA_ROOT, "%s%s" % (file_path, file_name))
			fileform = FileForm({'id':curtime,'file':path})
			if fileform.is_valid():
				fileform.save()
				return HttpResponseRedirect(reverse('CatchShow.submit.views.submitSuccess'))			
	else:
		form = TextForm()
	return render_to_response('submitString.html',
							  {'form': form},
							  context_instance=RequestContext(request)
							 )

def submit_file_to_string(request):
	if request.method == 'POST':
		form = UploadFileForm(request.POST, request.FILES)	
		if form.is_valid():
			uploadfile = request.FILES['upfile']		
			if uploadfile is None:
				return render_to_response('test.html',
									context_instance=RequestContext(request)
									)		
			content = uploadfile.read()
			ucontent = unicode(content)
			curtime = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))			
			textform = TextForm({'id':curtime,'string_text':ucontent})
			if textform.is_valid():
				textform.save()
				return HttpResponseRedirect(reverse('CatchShow.submit.views.submitSuccess'))	
	else:
		form = UploadFileForm()
		return render_to_response('submitFile.html',
							  {'form': form},
							  context_instance=RequestContext(request)
							 )
							 
def submit_file_to_binary(request):
	if request.method == 'POST':		
		form = UploadFileForm(request.POST, request.FILES)	
		if form.is_valid():
			uploadfile = request.FILES['upfile']		
			if uploadfile is None:
				return render_to_response('test.html',
									context_instance=RequestContext(request)
									)		
			content = uploadfile.read()
			ucontent = unicode(content)
						
			curtime = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
			textform = BinaryForm({'id':curtime,'binary_text':ucontent})
			if textform.is_valid():
				textform.save()
				return HttpResponseRedirect(reverse('CatchShow.submit.views.submitSuccess'))	
	else:
		form = UploadFileForm()
		return render_to_response('submitFile.html',
							  {'form': form},
							  context_instance=RequestContext(request)
							 )							 
def submitSuccess(request):
	return render_to_response('submitSuccess.html')

def handle_uploaded_file(f, filename='abc', filepath='files/'):#,root = os.path.join(settings.MEDIA_ROOT)):
	
	#path = root.join("%s%s" % (filepath, filename))
	path = os.path.join(settings.MEDIA_ROOT, "%s%s" % (filepath, filename))
	#path = os.path.join(settings.MEDIA_ROOT, "abc" )

	destination = open(path, 'wb+')

	for chunk in f.chunks():
		destination.write(chunk)
	destination.close()


def upload_file(request):
	if request.method != 'POST':
		form = UploadFileForm()
		return render_to_response('submitFile.html',
							  {'form': form},
							  context_instance=RequestContext(request)
							 )

	form = UploadFileForm(request.POST, request.FILES)	
	if form.is_valid():
		uploadfile = request.FILES['upfile']		
		if uploadfile is None:
			return render_to_response('test.html',
									context_instance=RequestContext(request)
									)		
		file_name = uploadfile.name
		file_path = 'files/'
		handle_uploaded_file(f = uploadfile, filename = file_name, filepath = file_path)
		return HttpResponseRedirect(reverse('CatchShow.submit.views.submitSuccess'))	
		#path = os.path.join(settings.MEDIA_ROOT, "%s%s" % (file_path, file_name))
		#fileform = FileForm({'file':path})
		#if fileform.is_valid():
		#	fileform.save()
		#	return HttpResponseRedirect(reverse('CatchShow.submit.views.submitSuccess'))	
			#push_to_jduge(upload_file = uploadfile)
			
			#service.set_upload_file(uploadfile)
			#service.get_file_content()
			#return render_to_response('judge.html',
			#				  {'service': service},
							  #context_instance=RequestContext(request)
			#				 )	
			#return render_to_response('submitSuccess.html',context_instance=RequestContext(request))
			#return render_to_response('submitSuccess.html',context_instance=RequestContext(request))
	return render_to_response('submitFile.html',
							  {'form': form},
							  context_instance=RequestContext(request)
							 )

class Service:
	def __init__(self,upload_file = None,content = None):
		self.upload_file = upload_file
		self.content = content
		self.file_content = None
	def set_upload_file(self,upload_file):
		self.upload_file = upload_file
	def set_content(self,content):
		self.content = content
	
	def get_file_content(self):
		#f = self.upload_file.open('r')
		self.file_content = self.upload_file.read()
		#f.close()
		
	def __unicode__(self):
		if self.upload_file is not None:
			self.content = None
			return self.file_content 
		if content is not None:
			self.upload_file = None
			return self.content
service = Service()

def push_to_jduge(upload_file = None, content = None):
	if upload_file is not None:
		
		service.set_upload_file(upload_file)
		service.get_file_content()
				
	if content is not None:
		service.set_content(content)
	return render_to_response('judge.html',
							  {'service': service},
							  #context_instance=RequestContext(request)
							 )
