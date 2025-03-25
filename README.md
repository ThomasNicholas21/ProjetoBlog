# Blog - Django

Este é um projeto desenvolvido com Python e Django, utilizando PostgreSQL como banco de dados e Docker para facilitar a configuração e execução.

## Tecnologias Utilizadas
- Python
- Django
- PostgreSQL
- Docker
- Django Summernote
- Django Axes

## Como Executar o Projeto

### 1. Clonar o Repositório
```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

### 2. Configurar Arquivo `.env`
Crie um arquivo `.env` na raiz do projeto e defina as variáveis necessárias:
```
POSTGRES_DB=change-me
POSTGRES_USER=change-me
POSTGRES_PASSWORD=change-me
SECRET_KEY=change-me
DEBUG=change-me
ALLOWED_HOSTS=change-me
```

### 3. Construir e Subir os Containers
```bash
docker-compose up --build
```

### 4. Aplicar Migrações e Criar Superusuário
```bash
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
```

### 5. Acessar a Aplicação
- **Frontend**: `http://localhost:8000`
- **Admin**: `http://localhost:8000/admin`

## Funcionalidades
- Criação e gerenciamento de posts e páginas personalizadas.
- Customização de elementos visuais do blog.
- Gerenciamento de categorias e tags.
- Controle de acesso com Django Axes.

## Autor
Projeto desenvolvido por **Thomas Nicholas**.

