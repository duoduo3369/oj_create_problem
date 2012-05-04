from django import forms
from cup_oj.problem.models import ProblemMeta, Problem, KeywordCheckConfig
from cup_oj.sa_conn import Session
from django.utils.translation import ugettext, ugettext_lazy as _

class ProblemMetaForm(forms.Form):
    title = forms.CharField(label=_('title'))
    judge_flow = forms.CharField(label=_('judge_flow'))
    
    class Meta:
        model = ProblemMeta
        fields = ('judge_flow','title')
        
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
        fields = ('judge_flow','problem_meta_id')
        
class KeywordCheckConfigForm(forms.Form):
    session = Session()
    #value = []#get_problem_meta_id_value()
    #problem_meta_id = forms.MultipleChoiceField(label=_('problem_meta_id'), choices = ()) 
    #problem_meta_id = forms.ModelChoiceField(label=_('problem_meta_id'),empty_label="(Nothing)",queryset = )#, choices = ())
    problem_meta_id = forms.ChoiceField(label=_('problem_meta_id'), choices = ())
    code_type = forms.IntegerField(label=_('code_type'))
    word = forms.CharField(label=_("word"), max_length = 254)

    class Meta:
        model = KeywordCheckConfig
            
    def __init__(self, *args, **kwargs):
        super(KeywordCheckConfigForm, self).__init__(*args, **kwargs)
        session = Session()
        self.fields['problem_meta_id'].choices = [('', '----------')] + [(pm.id, pm.title) for pm in session.query(ProblemMeta).all()]
        #self.fields['problem_meta_id'].queryset = QuerySet(session.query(ProblemMeta).all())
        
    def save(self, commit=True):
        keyword_check_config = KeywordCheckConfig()
        keyword_check_config.problem_meta_id = int(self.cleaned_data['problem_meta_id'][0])
        keyword_check_config.code_type = self.cleaned_data['code_type']
        keyword_check_config.word = self.cleaned_data['word']
        
        session = Session()
        session.add(keyword_check_config)
        session.commit()
        session.close()
        
        return  keyword_check_config
    


