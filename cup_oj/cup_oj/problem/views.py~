from django.shortcuts import render_to_response
from cup_oj.problem.forms import ProblemMetaForm
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, QueryDict
from django.template.response import TemplateResponse
from django.template import RequestContext

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
							 
def problem_meta_upload(request):
    if request.method == 'POST':
        form = ProblemMetaForm(request.POST)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('submitSuccess'))
    else:
        form = ProblemMetaForm()
        
    return render_to_response("problem/problem_meta.html", {
        'form': form,}, context_instance=RequestContext(request)) 
        
def submitSuccess(request):
	return render_to_response('problem/submitSuccess.html');
