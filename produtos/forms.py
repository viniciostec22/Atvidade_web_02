from django import forms
from .models import Produto, Categoria
from django.forms.widgets import ClearableFileInput

class ProdutoModelForm(forms.ModelForm):
    requerid_css_class = 'requerid'
    img = forms.ImageField(widget=ClearableFileInput, required=False)
    class Meta:
        model = Produto
        fields = ['nome','img', 'preco', 'descricao', 'categoria']
        widgets = {'descricao': forms.Textarea(attrs={'rows': 6,
                                                      'cols': 22,
                                                      'style': 'resize: none;'} ),
                   
                  }
        
class CategoriaModelForm(forms.ModelForm):
     #imagem = forms.ImageField(widget=ClearableFileInput, required=False)
     class Meta:
         model = Categoria
         fields = '__all__'
         