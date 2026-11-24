# Preentrega 7 — Blog Django

Proyecto base de un blog web desarrollado con **Python y Django** para el curso de Coderhouse.
Continúa la temática del blog de las entregas anteriores, pero inicia un proyecto web nuevo.

## Objetivo

Configurar la estructura inicial de un proyecto Django llamado `blog_project` y una aplicación
`posts`, sin implementar todavía modelos propios, vistas, formularios ni páginas del blog.

## Estructura

```text
blog_django/
├── manage.py                    # Comandos de Django
├── requirements.txt             # Dependencia necesaria: Django
├── .gitignore                   # Archivos que no se suben a GitHub
├── README.md                    # Guía de uso
├── blog_project/
│   ├── __init__.py
│   ├── settings.py              # Apps, idioma y zona horaria
│   ├── urls.py                  # Rutas iniciales de Django
│   ├── asgi.py
│   └── wsgi.py
└── posts/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── tests.py
    ├── views.py
    └── migrations/
        └── __init__.py
```

## Requisitos

- Python 3.10 o posterior, compatible con Django 5.2 LTS (por ejemplo, Python 3.13).
- Visual Studio Code con la extensión **Python** de Microsoft (recomendado).
- Git, si vas a subir el código a GitHub.

## Cómo ejecutar el proyecto en Windows / VS Code

1. Iniciá el servidor de desarrollo:

   ```powershell
   python manage.py runserver
   ```

2. Abrí <http://127.0.0.1:8000/> para ver la página inicial de Django.
   Detené el servidor con **Ctrl + C**.


## Configuración inicial

En `blog_project/settings.py` se encuentra:

- App registrada en `INSTALLED_APPS`: `"posts.apps.PostsConfig"`.
- Idioma: `LANGUAGE_CODE = "es-ar"`.
- Zona horaria: `TIME_ZONE = "America/Argentina/Buenos_Aires"`.
- SQLite local, por defecto en Django, sin publicar `db.sqlite3`.

La clave incluida es **solo un ejemplo de desarrollo local, no una clave privada**.
No uses esta configuración en un servidor público: para producción se necesitarán
una clave secreta real suministrada por `DJANGO_SECRET_KEY` y una configuración
segura de `DEBUG`, entre otras medidas. Esta entrega se ejecuta únicamente en local.

