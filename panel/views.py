# Panel 
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.utils.translation import ugettext
from django.conf import settings
from django.http import HttpResponse, HttpRequest, QueryDict, HttpResponseRedirect
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required

# Store y Panel Includes
from store.models import *
from store.forms import *
from store.functions import random_generator

# Python 
from decimal import Decimal
# Other Apps
import string
import json

#URL SITE 


#URL SITE 

SITE_URL = settings.SITE_URL




### Principal
def dashboard(request):

    template = "dashboard.html"
    data = { 'dev': 'Hello World', }
    return render_to_response(template, context_instance=RequestContext(request,data))