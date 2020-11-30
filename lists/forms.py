from django.forms import ModelForm

from . import models

class BookListForm(ModelForm):
    class Meta :
        model = models.BoookList
        fields = '__all__'