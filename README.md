# Dungeon Estudio
> Repository for music studio project.

# Configuración de compilación
## Crear entorno virtual 
``` bash
# 1) Create virtual environment, ("env" is the name, this can be replaced by anything).
python -m venv env

# 2) Activate the environment to work.
env\Scripts\activate

# 3) Install project requirements.
pip install -r requirements.txt
```

# Usefull Commands

## Starting
python manage.py runserver

## Create APP
python manage.py startapp "Name"

## Create Superuser
python manage.py createsuperuser

## Migrations 
python manage.py makemigrations

python manage.py migrate

## Migrate Data
python manage.py dumpdata > db.json

python manage.py loaddata db.json

## Show what is installed in the virtual environment
pip freeze --local