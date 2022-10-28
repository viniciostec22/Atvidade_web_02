from django import forms
from .models import Produto


class ProdutoModelForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome','img', 'preco', 'descricao', 'categoria']
        widgets = {'descricao': forms.Textarea(attrs={'rows': 6,
                                                      'cols': 22,
                                                      'style': 'resize: none;'}),
                   }
