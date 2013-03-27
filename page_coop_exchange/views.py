# -*- coding: utf-8 -*-

from django.template import RequestContext
from ionyweb.website.rendering.utils import render_view

from coop_local.models import Exchange
from django.conf import settings

from django.shortcuts import get_object_or_404

from ionyweb.website.rendering.medias import CSSMedia
from datetime import datetime

from .forms import PageApp_CoopExchangeForm

from django.db.models import Q

MEDIAS = (
    CSSMedia('page_coop_exchange.css'),
)

def index_view(request, page_app):
    base_url = u'%s' % (page_app.get_absolute_url())

    exchanges = Exchange.objects.all()

    if request.method == 'POST': # If the form has been submitted
        form = PageApp_CoopExchangeForm(request.POST)
        if request.POST['free_search']:
            exchanges = exchanges.filter(Q(title__contains=request.POST['free_search']) | Q(description__contains=request.POST['free_search']))
    else:
        form = PageApp_CoopExchangeForm() # An empty form

    rdict = {'exchanges': exchanges, 'object': page_app, 'base_url': base_url, 'form': form}
    
    return render_view('page_coop_exchange/index.html',
                       rdict,
                       MEDIAS,
                       context_instance=RequestContext(request))                           

def detail_view(request, page_app, pk):
    event = get_object_or_404(Exchange, pk=pk)
    base_url = u'%sp/' % (page_app.get_absolute_url())
    rdict = {'object': page_app, 'e': event, 'media_path': settings.MEDIA_URL, 'base_url': base_url}
    return render_view('page_coop_exchange/detail.html',
                       rdict,
                       MEDIAS,
                       context_instance=RequestContext(request))