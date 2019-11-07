# Directions to using Kalis API

After cloning project, open up your terminal, cd into the project. Then execute these commands:

```python -m venv kalisEnv```

```source ./kalisEnv/bin/activate```

If this command doesnt work, cd into the environent, cd into the scripts directory, and run ```activate.bat```

```pip install -r requirements.txt```

This set of commands sets up the database and loads all data necessary. Please run the commands *in this order*.

```python manage.py makemigrations kalisAPI```

```python manage.py migrate```

```python manage.py loaddata vitalsigns```

```python manage.py loaddata pupilresonse```

```python manage.py loaddata heartsounds```

```python manage.py loaddata breathsounds```

```python manage.py loaddata bowelsounds```

```python manage.py loaddata mentalstatus```

```python manage.py loaddata npo```

```python manage.py loaddata urinecolor```

```python manage.py loaddata urineodor```

```python manage.py loaddata edema```

```python manage.py loaddata oxygenrate```

```python manage.py loaddata patientgender```

```python manage.py loaddata patient```

```python manage.py loaddata assessment```

```python manage.py runserver```


This should get the API up and working. 

## To use this app in full, you will need to clone down the "client side" repository as well as this API repository.

[client-side application](https://github.com/AdamKnowles/kalis-client-side) via HTTP

