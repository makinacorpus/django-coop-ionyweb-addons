# -*- coding: utf-8 -*-

from django.utils.translation import ugettext, ugettext_lazy as _
import floppyforms as forms
from ionyweb.forms import ModuloModelForm
from .models import PageApp_CoopExchange

class PageApp_CoopExchangeForm(ModuloModelForm):

    type_offer = forms.BooleanField(required=False, label=_('Offer'))
    type_request = forms.BooleanField(required=False, label=_('Request'))
    
    type_product = forms.BooleanField(required=False, label=_('Product'))
    type_service = forms.BooleanField(required=False, label=_('Service'))
    type_skills = forms.BooleanField(required=False, label=_('Skills'))
    type_project = forms.BooleanField(required=False, label=_('Project'))
    type_experience = forms.BooleanField(required=False, label=_('Experience'))
    
    activity = forms.CharField(required=False, label=_('Activity'))
    location = forms.CharField(required=False, label=_('Location'))
    thematic = forms.CharField(required=False, label=_('Thematic'))
    
    mode_gift = forms.BooleanField(required=False, label=_('Gift'))
    mode_swap = forms.BooleanField(required=False, label=_('Swap'))
    mode_euros = forms.BooleanField(required=False, label=_('Euros'))
    mode_mutualization = forms.BooleanField(required=False, label=_('Mutualization'))
    
    skills_voluntary = forms.BooleanField(required=False, label=_('Voluntary'))
    skills_training_work = forms.BooleanField(required=False, label=_('Training work'))
    skills_job = forms.BooleanField(required=False, label=_('Job offer'))
    skills_training = forms.BooleanField(required=False, label=_('Training'))
    
    free_search = forms.CharField(required=False, label=_('Free search'))
    
    
    class Meta:
        model = PageApp_CoopExchange