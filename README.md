# Curso-Django - Dev Pro

Código desenvolvido no módulo de Django plataforma.dev.pro.br

Aplicação disponível [aqui](https://curso-django.fly.dev/)

[![codecov](https://codecov.io/gh/gabrielwp87/curso-django/branch/main/graph/badge.svg?token=9kIHtEujlU)](https://codecov.io/gh/gabrielwp87/curso-django)

Suportada versão 3 de Python e versão 4.6 do [Bootstrap](https://getbootstrap.com/docs/4.6/getting-started/introduction/)

### <strong>Instruções para instalação</strong>:

#### Criar e ativar ambiente virtual Python (venv):

```console
python -m venv .venv
```

```console
source .venv/bin/activate
```

#### <strong>Instalar dependências</strong>:

```console
pip install -r requirements.txt
```

#### <strong>Instalar dependências, inclusive de desenvolvimento</strong>:

```console
pip install -r requirements-dev.txt
```

#### Copiar variáveis de ambiente:
```console
cp contrib/env-sample .env
```

#### Rodar Django:
```console
python manage.py runserver
```