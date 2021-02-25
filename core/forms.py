from django import forms
from django.core.mail.message import EmailMessage
from .models import Produto

class ContatoForm(forms.Form):
    nome =  forms.CharField(label='Nome',max_length=100,min_length=3)
    email =  forms.EmailField(label='E-mail',max_length=100,min_length=5)
    assunto = forms.CharField(label='Assunto',max_length=400)
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea())

    def send_email(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']

        conteudo = f'Nome: {nome}\n E-mail: {email}\n Assunto: {assunto}\n Mensagem: {mensagem}'

        mail = EmailMessage (
            subject = 'E-mail enviado pelo sistema',
            body = conteudo,
            from_email= 'contato@meudominio.com.br',
            to=['contato@meudominio.com.br','gerente@meudominio.com.br'],
            headers={'Reply-to': email}
        )
        mail.send()

class ProdutoModelForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome','preco','estoque','imagem']


