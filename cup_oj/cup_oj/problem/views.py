from django.shortcuts import render_to_response
from cup_oj.problem.forms import CompileConfigForm, KeywordCheckConfigForm, ProblemMetaForm
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, QueryDict
from django.template.response import TemplateResponse
from django.template import RequestContext

def submit_success(request):
	return render_to_response('problem/submit_success.html')
								 
def compile_config_upload(request):
    if request.method == 'POST':
        form = CompileConfigForm(request.POST)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('submit_success'))
    else:
        form = CompileConfigForm()    
    
    return render_to_response("problem/upload.html", {
        'form': form,}, context_instance=RequestContext(request)) 
        
def keyword_checkconfig_upload(request):
    if request.method == 'POST':
        form = KeywordCheckConfigForm(request.POST)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('submit_success'))
    else:
        form = KeywordCheckConfigForm()
        
    return render_to_response("upload.html", {
        'form': form,}, context_instance=RequestContext(request)) 
        
def problem_meta_upload(request):
    if request.method == 'POST':
        form = ProblemMetaForm(request.POST)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('submit_success'))
    else:
        form = ProblemMetaForm()    
    
    return render_to_response("problem/upload.html", {
        'form': form,}, context_instance=RequestContext(request))     

