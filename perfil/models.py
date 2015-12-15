from django.db import models
from simple_history.models import HistoricalRecords
from PerfilUsuario import settings
try:
    from django.utils import simplejson as json
except:
    import simplejson as json
from django.core.exceptions import ValidationError


class User(models.Model):
	name=models.CharField(verbose_name=u'Nombre', max_length=60, blank=False, null=False)
	lastname=models.CharField(verbose_name=u'Apellido', max_length=60, blank=False, null=False)
	photo=models.ImageField(upload_to='photo',verbose_name='Foto',blank=True, null=False)
	history=HistoricalRecords()

	def to_json_dict(self):
		response={}
		response['id']=self.id
		response['name']=self.lastname+" "+self.name 
		response['photo']=self.photo
		return response


class Project(models.Model):
	name=models.CharField(max_length=30)
	user=models.ForeignKey(User)

	def to_json_dict(self):
		response={}
		response['id']=self.id
		response['name']=self.name 
		response['user']=self.user
		return response

