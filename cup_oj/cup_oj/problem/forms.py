from django import forms
from cup_oj.problem.models import ProblemMeta
from django.utils.translation import ugettext, ugettext_lazy as _

class ProblemMetaForm(forms.Form):
    title = forms.CharField(label=_("title"))
    judge_flow = forms.CharField(label=_("judge_flow"))
    class Meta:
        model = ProblemMeta
        fields = ("judge_flow","title")
