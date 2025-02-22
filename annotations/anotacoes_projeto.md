# Django Framework

- Framework para desenvolvimento web de forma rápida, segura e escalável, que segue o padrão MVT (Model-View-Tamplate).

### MVT - Model-View-Template
- **Model:** vai gerarenciar a estrutura lógica de dados, mapeando os dados do manco de forma orientada a objeto.
- **View:** controla o que é exibido no navegador do usuário, manipulanto solicitações HTTP. Também pode enviar dados para dentro dos templates.
- **Template:** Define a apresentação visual dos dados, usando sistemas de templates do Django.

### HTTP Request (Requisição HTTP)
É a mensagem enviada do cliente (geralmente um navegador ou aplicativo) para o servidor para solicitar algum recurso, como uma página da web, um arquivo ou a execução de uma operação.

**Principais componentes de uma requisição HTTP:**
- Método HTTP: Indica a ação desejada:
    - GET: Solicita dados do servidor.
    - POST: Envia dados para o servidor.
    - PUT: Atualiza dados existentes.
    - DELETE: Remove dados no servidor.
- URL: O endereço do recurso solicitado.
- Cabeçalhos (Headers): Informações adicionais, como o tipo de conteúdo aceito (Accept), informações do cliente (User-Agent), etc.
- Corpo (Body): Dados enviados na requisição (aplicável para métodos como POST e PUT).

### HTTP Response (Resposta HTTP)
É a mensagem enviada pelo servidor ao cliente em resposta à requisição HTTP. Ela contém o resultado da solicitação, seja o conteúdo solicitado ou um status informando o que aconteceu.

- Principais componentes de uma resposta HTTP:
    - Código de status: Informa o resultado da requisição:
    - 200 OK: Sucesso.
    - 404 Not Found: Recurso não encontrado.
    - 500 Internal Server Error: Erro no servidor.
- Cabeçalhos (Headers): Informações sobre a resposta, como tipo de conteúdo (Content-Type), tamanho do conteúdo, etc.
Corpo (Body): O conteúdo da resposta, como o HTML de uma página, dados JSON, imagens, etc.

# Arquivos
## __settings.py:__ 
Toda a configuração da aplicação é feita nesse arquivo, definindo váriaveis de ambinete e configurações gerais para o funcionamento do aplicativo, como conexão com banco de dados, localização de templates, e detalhes de segurança.
- Configurações principais:
    - BASE_DIR
    - SECRET_KEY
    - DEBUG
    - ALLOWED HOSTS
- Aplicativos
    - INSTALLED_APPS
- Middlewares
    - MIDDLEWARE
- URLS E WSGI
    - ROOT_URLCONF
    - WSGI_APPLICATION
- Banco de dados
    - DATABASES
- Autentincação
    - AUTH_PASSORD_VALIDATORS
- Internacionalização
- Arquivos estáticos e mídia
    - STATIC_URL
    - STATIC_ROOT
    - STATICFILES_DIRS
    - MEDIA_URL/MEDIA_ROOT
- Outros
    - TEMPLATES
    - DEFAULT_AUTO_FIELD

# Comandos

### Iniciar projeto
```cmd
> django-admin startproject NomeProjeto
```
```cmd
>django-admin startproject NomeProjeto .
```

### Iniciar servidor
```cmd
>python manage.py runserver
```

### Iniciar um App
```cmd
>python manage.py startapp
```

### Fazer Migrations
```cmd
>python manage.py makemigrations
```
```cmd
>python manage.py migrate
```

### Criar super usuário Django
```cmd
>python manage.py createsuperuser
```
```cmd
>python manage.py changepassword USERNAME
```

### Acessar shell Django
```cmd
>python manage.py shell
```
```python
>from app.models import model
>obj = model(atribut='valor')
>obj.save() # comita modificações para base de dados
>obj.atribut = 'outro valor'
>obj.save()
>obj.delete() # delete as modificações
>obj = model.objects.get(id='1') # manager   
>obj.atribut = 'outro de outro valor' # get pega o elemento 1 e possibilita a alteração
>obj = model.objects.all() # Seleciona todos os valores
>for value in obj: value.first_name
>obj = model.objects.all().order_by('-id')
>obj = model.objects.create(first_name='Fulano') # cria direto na base de dados
```

### Coletar arquivos estáticos
Esse comando se utiliza quando a aplicação irá rodar em produção. Como Django não é um servidor, ele coleta e cria um diretório para que o mesmo seja configurado em um servidor. Para o mesmo funcionar, deve ser criado uma variável de ambiente STATIC_ROOT, indicando aonde esse diretório deve ser criado.
```cmd
>python manage.py collectstatic
```

# Conceitos
### namespace
Para evitar colisão de nomes iguais ao renderizar um arquivo HTML em tamplates, ou seja, evitar que dois templates com nome iguais sejam chamados de forma errada, se utiliza o __namespace__, no qual consiste em criar uma pasta dentro da pasta template para o arquivo em questão e declarar o seu caminho na view, exemplo: "templates/exemplo/exemplo.html". 

### URL Dinâmica
São URLs que vão incluir variáveis para definir rotas, permitindo que os valores sejam passados na URL e capturados na View correspondente. Evitando que crie URL estática para cada rota. Sendo ela configurada por padrão da seguinte maneira:
```python

# urls.py
urlpatterns = [
    path('exemplo/<exemplo:id>/', views.exemplo, name='exemplo')
]

# views.py
def exemplo(request, id):
    ...

```

### migrations / models
Sistema no qual gerencia alterações feitas no esquema do banco de dados de forma organizada eautomatizada. Permitindo que mudanças, como adicionar, alterar ou remover campos, sejam feitas sem precisar de escrever SQL manualmente.

Models são usados para definir a estrutura e comportamento dos dados armazenados no banco de dados, representando as tabelas dos bancos de dados. As classes são equivalentes as tabelas, e os atributos equivalente as colunas. No Django o ID já é criado de forma automática. 
As classes estarão herdando de Models disponibilizado pelo Django para fazer a relação com banco de dados. Os atributos estarão sendo utilizados para definir o tipo de variável que cada coluna estará utilizando.

### Admin Django
A área administrativa do Django permite ao usuário acessar o painel administrativo, onde é possível gerenciar usuários e os models criados na aplicação. Para tornar os models visíveis e manipuláveis nesse painel, é necessário registrá-los no arquivo admin.py utilizando a função decoradora ou o método admin.site.register fornecido pelo módulo administrativo do Django.

Além disso, o painel administrativo pode ser personalizado para exibir, filtrar ou ordenar campos, bem como para criar interfaces específicas para modelos complexos, usando classes como ModelAdmin.

### Media
Nas variáveis de ambiente, "media/" é tudo aquilo que o usuário envia, ou seja, é o upload de arquivos do mesmo. Para realizar tal ação é necessário configurar as variáveis de ambiente **MEDIA_ROOT** e **MEDIA_URL**, no qual específica a url e o diretório desses arquivos.

Para conseguir fazer upload, é necessário especificar no model, um field chamado **ImageField**, e nele especificar o caminho sem considerar o diretório, uma vez que ele já foi configurado nas variáveis de ambiente. Necessário passar o parâmetro **upload_to='nome/date(%Y,%m,%d)'**.
```python
class exemplo(models.Model):
    image = model.ImageFied(upload_to='nome/date')
```

Em caso de imagens, o Django depende da biblioteca pillow.
```cmd
>pip install pillow
```

Para configurar a URL de media, para que a aplicação saiba o caminho desse arquivo é necessário configurar na **url.py** no projeto, concatenando o arquivo estático com as urlpatterns.
```python
# realizar importação para urls de arquivo estático
from django.conf.urls.static import static
# importa as settings.py do projeto
from django.conf import settings

# concatena arquivo estático da MEDIA configurada no ambiente
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```
### Meta class
A classe chamada **_meta_** é chamada dentro de um model e é utilizada para definir metados que influenciam no comportamento do model, como ordenação, nomes de tabelas, nomes de exibição e outro. Permitindo personalizar e controlar aspectos de um model sem alterar a lógica principal. aplicações:
    - **ordering:** Define a ordem padrão dos registros ao serem recuperados do banco de dados.
    - **verbose_name e verbose_name_plural:** Especificam nomes legíveis para o model no singular e plural, respectivamente.
    - **db_table:** Permite definir um nome personalizado para a tabela no banco de dados.
    - **unique_together:** Estabelece uma restrição de unicidade combinada em um conjunto de campos.
    - **permissions:** Adiciona permissões personalizadas além das padrão (adicionar, alterar, deletar, visualizar).
    - **widgets:** Dicionário quer permite alterar um padrão para forms.

### local_settings
Com a finalidade de evitar que informações importantes não subam para o servidor que estará hosteando a aplicação, o **local_setings** é utilizado para que essas informações fiquem apenas no localhost. Dessa forma, deixa a aplicação com menos conflito dentro do git e com o ambiente em produção. Para realizar a configuração é necessário importar o módulo dentro do arquivo _project.settings.py_
```python
try:
    from project.local_settings import *
except ImportError: ...
```
No arquivo local_settings.py vai ter todas as variáveis de ambiente que deseja configurar apenas localmente para evitar erros ao subir a aplicação para o servidor. Exemplo:
```python
SECRET_KEY: str = 'CHANGE-ME'
DEBUG: bool = True
ALLOWED_HOSTS: list[str] = []
```

### CSRF Token Django
O CSRF (Cross-Site Request Forgery) é um tipo de ataque em que um usuário autenticado executa ações indesejadas em um site sem seu consentimento. Isso ocorre quando uma requisição indesejada é feita em nome do usuário sem que ele perceba.
O Django utiliza tokens CSRF para impedir esse tipo de ataque. Esse token é um valor único e aleatório, gerado e validado em requisições POST. Ele é incluído no projeto como um middleware, garantindo uma camada adicional de segurança.
```python
<form action="/enviar_dados/" method="POST">
    {% csrf_token %}
    <input type="text" name="nome">
    <input type="submit" value="Enviar">
</form>

```

### Form
Esse módulo Django facilita a criação de formulários e sua respectiva validação, permitindo a criação baseado no banco de dados com _ModelForm_ e outros modos. Possui métodos como __clean()__ que é utilizado para validar e processar dados, e também permite utilizar fields que representam campos de um formulário.
Campos de fields 
- *required* → Define se o campo é obrigatório (True por padrão).
- *label* → Texto exibido como rótulo do campo.
- *initial* → Valor inicial do campo.
- *widget* → Controla como o campo será renderizado no HTML.
```python
# formas de configurar widgets

# Classe Meta
class ContactForm(forms.ModelForm):
    class Meta: 
        # define qual model esse form se refere
        model = Contact
        fields = ('first_name', 'last_name', 'phone',)

        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder':'Escreva seu nome'
                }
            )
        }

# através do forms
class ContactForm(forms.ModelForm):
    first_name = forms.CharField(
        widgets=forms.TextInput(
                attrs={
                    'placeholder':'Escreva seu nome'
            }
        )
    )

# através do Python
class ContactForm(forms.ModelForm):
    # recebe qualquer argumento
    def __init__(self, args*, kwargs**):
        # inicializa a superclass com os argumentos
        super().__init__(args*, kwargs**)

        self.fields['first_name'].widgets.attrs.update(
            {
                'placeholder':'Escreva seu nome'
            }
        )

```
- *validators* → Lista de funções de validação personalizadas.
- *help_text* → Texto auxiliar exibido abaixo do campo.


### packages
Ao criar um aplicativo com Django, o mesmo realiza sugestões de como estrutarar arquivos, mas dependendo da aplicação é interessante criar packages para melhor organização. Por exemplo, um ambiente que terá muitas views, interessante separar uma package com módulos dentro.
```
-contact
    -migrations
    -templates
    -views
        - __init__.py
        - outras_views.py
```
# Django HTML
### extends
Herança de template utilizado.
```HTML
{% extends 'caminho.template' %}
```
### block & endblock
Faz trocar o valor do texto no template filho.
```HTML
{% block texto %} TEXTO {% endblock texto %}
```
### include
Utilizando juntamente a um "partials", normalmente utilizado quando está em partes, que pode ser utilizado em outro local.
```HTML
{% include 'caminho/partials/arquivo' %}
```

### load
Utilizar sempre que for utilizar arquivos staticos, irá carregar o aplicativo "django.contrib.staticfiles"
```HTML
{% load static %}
```

### variavel
Para chamar uma variavel passada no contexto da view, pode acessar seus dados dentro de chaves.
```HTML
<p><b>ID:</b> {{ contact.id }} </p>
<p><b>E-mail:</b> {{ contact.email }} </p>
<p><b>Phone:</b> {{ contact.phone }} </p>
<p><b>Created Date:</b> {{ contact.created_date }} </p>
<p><b>Description:</b> {{ contact.description }} </p>
<p><b>Category:</b> {{ contact.category.name }} </p>
```
Obs: Quando essa variável é um model e possui foreing key, é possível chamar os dados dessa foreingkey igual o ultimo exemplo catego

# Bibliotecas
### whitenoise
Servidor que pode ser utilizado para "servir" arquivos estáticos. Ele é um middleware que deve ser configurado na variável de ambiente MIDDLEWARE do django.
```cmd
>pip install whinoise
``` 
Colocar _"whitenoise.middleware.WhiteNoiseMiddleware",_ abaixo de middleware de segurança do Django.

### faker
Essa biblioteca é utilizada para preencher dados falsos dentro de uma aplicação, normalmente utilizado para testes. Essese dados incluem nomes, endereçoes, números, datas, textos e entre outros.
```cmd
>pip install faker
```
Necessário definir a localidade utilizada na aplicação por "pt_br". Exemplo de uso:
```python
from faker import Faker
from myapp.models import Contact

fake = Faker('pt_BR')

for _ in range(10):
    Contact.objects.create(
        name=fake.name(),
        phone=fake.phone_number(),
        email=fake.email(),
        address=fake.address()
    )
```
