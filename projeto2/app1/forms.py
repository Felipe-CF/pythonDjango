from django import forms # type: ignore

class ContatoForm(forms.Form):
    nome = forms.CharField(max_length=100, label='Nome')
    email = forms.EmailField(max_length=100, label='Email')
    assunto = forms.CharField(max_length=140, label='Assunto')
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea())
     