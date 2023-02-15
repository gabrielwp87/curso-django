# curso-django
Código desenvolvido no módulo de Django plataforma.dev.pro.br

Aplicação disponível [aqui](https://curso-django-production.up.railway.app/)

[![codecov](https://codecov.io/gh/gabrielwp87/curso-django/branch/main/graph/badge.svg?token=9kIHtEujlU)](https://codecov.io/gh/gabrielwp87/curso-django)

Suportada versão 3 de Python e versão 4.6 do [Bootstrap](https://getbootstrap.com/docs/4.6/getting-started/introduction/)

Para instalar:
``` console
py -3 -m venv .venv
.venv\Scripts\activate
pip install pipenv
pipenv sync

```

Para instalar com dependências de desenvolvimento:
``` console
py -3 -m venv .venv
.venv\Scripts\activate
pip install pipenv
pipenv sync --dev

```

Copiar variáveis de ambiente:
```console
cp contrib/env-sample .env

```

Rodar Django:
```console
python manage.py runserver

```
