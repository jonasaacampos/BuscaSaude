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
