from django.shortcuts import render_to_response
from cup_oj.problem.forms import ProblemMetaForm, KeywordCheckConfigForm
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, QueryDict
from django.template.response import TemplateResponse
from django.template import RequestContext

def get_classoject_id(obj):
    value = []
    queryset = obj.objects.all()
    for v in queryset:
        value.append(v.id)
    return value
    
def submit_success(request):
	return render_to_response('problem/submit_success.html')
								 
def problem_meta_upload(request):
    if request.method == 'POST':
        form = ProblemMetaForm(request.POST)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('submit_success'))
    else:
        form = ProblemMetaForm()
        
    return render_to_response("problem/problem_meta_upload.html", {
        'form': form,}, context_instance=RequestContext(request)) 
        
def keyword_checkconfig_upload(request):
    if request.method == 'POST':
        form = KeywordCheckConfigForm(request.POST)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('submit_success'))
    else:
        form = KeywordCheckConfigForm()
        
    return render_to_response("problem/keyword_checkconfig_upload.html", {
        'form': form,}, context_instance=RequestContext(request)) 
