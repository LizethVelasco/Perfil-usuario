from django.views.generic import TemplateView, CreateView
from django.shortcuts import render
from .models import User
from .models import Project
from django.core.urlresolvers import reverse_lazy
from .forms import PostForm
from .forms import ProjectForm
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.core.files.uploadedfile import SimpleUploadedFile


class index(CreateView):
	template_name = 'index.html'
	model=User
	success_url = reverse_lazy('Ingresar_Usuario')

def createuser(request):
    if request.method == "POST":
            form = PostForm(request.POST,request.FILES)
            if form.is_valid():
            	name=form.cleaned_data['name']
            	lastname=form.cleaned_data['lastname']
                photo=request.FILES
            	form.save()
            	return redirect ('Ingresar_proyecto')

    else:
    	form = PostForm()
    	message="Error"
    	return render_to_response("index.html",{"form":form}, context_instance = RequestContext(request))
    query=request.GET.get('q')
    vacio=""
    if query==vacio:
    	return redirect('Ingresar_proyecto')
    else:
    	return render_to_response("index.html",{"form":form}, context_instance = RequestContext(request))

class project(CreateView):
	template_name = 'project.html'
	model=Project
	success_url = reverse_lazy('Ingresar_proyecto')

def createproject(request):
    if request.method == "POST":
            form2 = ProjectForm(request.POST)
            if form2.is_valid():
            	name=form2.cleaned_data['name']
            	user=form2.cleaned_data['user']
            	form2.save()
            	return redirect ('Ingresar_proyecto')

    else:
    	form2 = PostForm()
    	message="Error"
    	return render_to_response("project.html",{"form2":form2}, context_instance = RequestContext(request))
    query=request.GET.get('q')
    vacio=""
    if query==vacio:
    	return redirect('Ingresar_proyecto')
    else:
    	return render_to_response("project.html",{"form2":form2}, context_instance = RequestContext(request))
