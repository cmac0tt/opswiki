from opswiki.wiki.models import Page
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import HttpResponseRedirect
from django import forms
import markdown
import htmllib
from django.template import RequestContext, loader
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt, csrf_protect
# Create your views here.

def view_page(request, page_name):
    c = {}
    try:
     page = Page.objects.get(pk=page_name)
     content = page.content
    except Page.DoesNotExist:
        return render_to_response("home.html", {"page_name":page_name}, context_instance=RequestContext(request))

def upload_file(request):
    c = {}
    if request.method == 'POST':
     form = UploadFileForm(request.POST, request.FILES)
    if form.is_valid():
     handle_uploaded_file(request.FILES['file'])
    return HttpResponseRedirect('media/"{{file}}"', {'form': form})

@csrf_exempt
def upload_file_view(request):
    C = {}
    request.upload_handlers.insert(0, ProgressBarUploadHandler())
    return _upload_file_view(request)

