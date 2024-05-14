from django import forms # type: ignore
from django.core.mail.message import EmailMessage # type: ignore

class ContatoForm(forms.Form):
    nome = forms.CharField(max_length=100, label='Nome')
    email = forms.EmailField(max_length=100, label='Email')
    assunto = forms.CharField(max_length=140, label='Assunto')
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea())

    def send_mail(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']  

        conteudo = f'Nome:{nome}\nE-mail:{email}\nAssunto:{assunto}\nMensagem:{mensagem}'

        mail = EmailMessage(
            subject='E-mail enviado pelo projeto2',
            body=conteudo,
            from_email='contato@seudominio.com.br',
            headers={'Reply-To':email},
            to=['contato@seudominio.com.br',]
        ) 
        mail.send() 