#Proyecto para practicar con github.

Para poder ejecutar el backend realizar los siguientes pasos


```
cd backend
python -m venv .venv
.venv/Scripts/activate
pip install -r requirements.txt
python manage.py runserver
```
las rutas para accesar a la api son las siguientes

```
Se utiliza para generar un token
http://127.0.0.1:8000/api-token/

Se utiliza para renovar el token
http://127.0.0.1:8000/api-token-refresh/

Obtienes datos de personas unicamente si estas logueado
http://127.0.0.1:8000/api/1.0/person
```