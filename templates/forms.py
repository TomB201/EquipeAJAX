from django.forms import ModelForm
from projet1WEBA.models import *

class Form_addequipe(ModelForm):
    class Meta:
        model = Equipe
        fields = ["nom", "pays"]
        labels = {
            "nom": "Nom",
            "pays": "Pays"
        }
