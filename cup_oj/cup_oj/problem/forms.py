from django import forms
from cup_oj.problem.models import CompileConfig, KeywordCheckConfig, ProblemMeta, Problem
from cup_oj.sa_conn import Session
from django.utils.translation import ugettext, ugettext_lazy as _


class CompileConfigForm(forms.Form):   
    problem_meta_id = forms.ChoiceField(label=_('problem_meta_id'), choices = ()) 
    code_type = forms.IntegerField(label=_('code_type'))
    config = forms.CharField(label=_("config"), max_length = 254)    

    class Meta:
        model = CompileConfig
            
    def __init__(self, *args, **kwargs):
        super(CompileConfigForm, self).__init__(*args, **kwargs)
        session = Session()
        self.fields['problem_meta_id'].choices = [('', '----------')] + [(pm.id, pm.title) for pm in session.query(ProblemMeta).all()]
        
    def save(self, commit=True):
        compile_config = CompileConfig() 
        compile_config.problem_meta_id = self.cleaned_data['problem_meta_id']       
        compile_config.code_type = self.cleaned_data['code_type']
        compile_config.config = self.cleaned_data['config']        
        
        session = Session()
        session.add(compile_config)
        session.commit()
        session.close()
        
        return  compile_config
        
class KeywordCheckConfigForm(forms.Form):    
    problem_meta_id = forms.ChoiceField(label=_('problem_meta_id'), choices = ())
    code_type = forms.IntegerField(label=_('code_type'))
    word = forms.CharField(label=_("word"), max_length = 254)

    class Meta:
        model = KeywordCheckConfig
            
    def __init__(self, *args, **kwargs):
        super(KeywordCheckConfigForm, self).__init__(*args, **kwargs)
        session = Session()
        self.fields['problem_meta_id'].choices = [('', '----------')] + [(pm.id, pm.title) for pm in session.query(ProblemMeta).all()]
        
    def save(self, commit=True):
        keyword_check_config = KeywordCheckConfig()
        #keyword_check_config.problem_meta_id = int(self.cleaned_data['problem_meta_id'][0])
        keyword_check_config.problem_meta_id = self.cleaned_data['problem_meta_id']
        keyword_check_config.code_type = self.cleaned_data['code_type']                
        keyword_check_config.word = self.cleaned_data['word']
        
        session = Session()
        session.add(keyword_check_config)
        session.commit()
        session.close()
        
        return  keyword_check_config

class ProblemMetaForm(forms.Form):
    title = forms.CharField(label=_('title'))
    judge_flow = forms.CharField(label=_('judge_flow'))
    
    class Meta:
        model = ProblemMeta
        #fields = ('judge_flow','title')
        
    def save(self, commit=True):
        problem_meta = ProblemMeta()
        problem_meta.title = self.cleaned_data['title']
        problem_meta.judge_flow = self.cleaned_data['judge_flow']
        
        session = Session()
        session.add(problem_meta)
        session.commit()
        session.close()
        
        return problem_meta
        
class ProblemForm(forms.Form):
    class Meta:
        model = Problem
        #fields = ('judge_flow','problem_meta_id')
        

    


