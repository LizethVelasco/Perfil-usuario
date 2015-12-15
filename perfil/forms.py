from django import forms
from .models import User
from .models import Project

class PostForm(forms.ModelForm):

	class Meta:
		model=User
		
		fields=('name','lastname','photo') #datos que se muestran en el formulario

class ProjectForm(forms.ModelForm):   

	class Meta:
		model=Project
		fields=('name','user')