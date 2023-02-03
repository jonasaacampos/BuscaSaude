```comandline

django-admin stratproject buscaSaudeAdmin .

```

### Create Project

- Criado diretório settings, movido settings.py do projeto para dentro dele, criados arquivos individuais de configuração
- removida rota de banco de dados do arquivo settings
- inserida rota de conexão com o banco nos aruivos de config dentro da pasta settings
- alterados metadados de linguagem e time zone no arquivo settings
- inserir variáveis de conteúdos estáticos dentro do arquivo settings
- retirar a variável ALLOWED_HOSTS do arquivo de settings e inserir nos arquivos de configuração individuais
  - [] é o mesmo que ["127.0.0.1"]
- alterar em `manage.py` a instrução para que seja considerada a configuração personalidada
  - `os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'medicSearchAdmin.settings.development')`
- Configurar arquivo de settings padrão ao rodar o servidor (escolher qual ambiente será considerado.)
  - Windows: `set DJANGO_SETTINGS_MODULE=medicSearchAdmin.settings.production`
  - Linux/Mac: `export DJANGO_SETTINGS_MODULE=medicSearchAdmin.settings.production`
- Rodar primeira mirgração `python manage.py migrate`
- Criar usuario admin `python manage.py createsuperuser`


### Create App

- Criar app `python manage startapp buscaSaude`
- adicionar o app entro da lista dos apps gerenciados pelo admin (`Projeto>settings>settings.py => lista INSTALLED_APPS`)
- criar o pacote models dentro do app
- apagar arquivo models.py da raiz do app
- após criar models, fazer as migrações `python manage makemigrations`
- consolidar a migração `python manage migrate`
- Inserir model no arquivo admin.py (`from .models import *` e `admin.site.register(Profile)`)


------

- **todo usuario necessita estar em um perfil**

### Criando as views

- remover o views.py do app
- criar pacote views dentro do app