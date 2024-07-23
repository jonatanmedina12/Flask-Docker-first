
# Flask Docker API

Este es un proyecto de ejemplo de una API RESTful construida con Flask y Docker. La API incluye autenticación con JWT y está documentada con Swagger.

## Estructura del Proyecto

```plaintext
Flask-Docker-first/
│
├── Crud/
│   ├── controller/
│   │   ├── api_Swagger.py
│   │   ├── auth.py
│   │   ├── routes.py
│   ├── docs/
│   │   ├── __init__.py
│   │   ├── item_delete.yml
│   │   ├── item_get.yml
│   │   ├── item_put.yml
│   │   ├── items_get.yml
│   │   ├── items_post.yml
│   ├── models/
│   │   ├── __init__.py
│
├── env/
│
├── instance/
│   ├── config.py
│
├── .gitignore
├── Dockerfile
├── LICENSE
├── main.py
├── README.md
├── requirements.txt
```

## Configuración del Proyecto

### Requisitos

- Docker
- Python 3.x

### Instalación

1. Clona este repositorio:

   ```bash
   git clone https://github.com/jonatanmedina12/Flask-Docker-first.git
   cd flask-docker-api
   ```

2. Crea y activa un entorno virtual:

   ```bash
   python -m venv env
   source env/bin/activate  # En Windows usa `env\Scripts\activate`
   ```

3. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

### Construcción y Ejecución del Contenedor Docker

1. Construye la imagen Docker:

   ```bash
   docker build -t flask-api .
   ```

2. Ejecuta el contenedor Docker:

   ```bash
   docker run -it --name flask-api -p 5000:5000 flask-api
   ```

### Acceso a la Documentación Swagger

Abre tu navegador y navega a `http://localhost:5000/apidocs/` para ver la documentación Swagger de la API.

## Uso de la API

La API proporciona los siguientes endpoints:

### Endpoints de Autenticación

- `POST /auth/register`: Registrar un nuevo usuario.
- `POST /auth/login`: Iniciar sesión y obtener un token JWT.

### Endpoints de Items

- `GET /api/items`: Obtener una lista de todos los items.
- `POST /api/items`: Crear un nuevo item.
- `GET /api/items/<int:item_id>`: Obtener un item por ID.
- `PUT /api/items/<int:item_id>`: Actualizar un item por ID.
- `DELETE /api/items/<int:item_id>`: Eliminar un item por ID.

## Ejemplo de Request

### Registro de Usuario

```http
POST /auth/register
Content-Type: application/json

{
  "username": "nuevo_usuario",
  "password": "tu_contraseña"
}
```

### Inicio de Sesión

```http
POST /auth/login
Content-Type: application/json

{
  "username": "nuevo_usuario",
  "password": "tu_contraseña"
}
```

### Crear un Nuevo Item

```http
POST /api/items
Authorization: Bearer <tu_token_jwt>
Content-Type: application/json

{
  "name": "Nuevo Item",
  "description": "Descripción del nuevo item"
}
```

