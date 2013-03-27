# -*- coding: utf-8 -*-

import floppyforms as forms
from ionyweb.forms import ModuloModelForm
from .models import PageApp_CoopExchange

class PageApp_CoopExchangeForm(ModuloModelForm):

    type_exchange = forms.CharField(required=False)
    type = forms.CharField(required=False)
    free_search = forms.CharField(required=False)
    
    class Meta:
        model = PageApp_CoopExchange