# GCP Fullstack App

Mini proyecto fullstack construido con Angular y FastAPI, pensado para practicar desarrollo frontend/backend y despliegue en Google Cloud Platform.

## Tecnologías

### Frontend
- Angular
- TypeScript
- SCSS
- HttpClient
- Reactive Forms

### Backend
- FastAPI
- Python
- SQLAlchemy
- SQLite

### Deploy objetivo
- Frontend: Firebase Hosting
- Backend: Google Cloud Run

## Funcionalidades

- Listar postulaciones
- Crear postulaciones
- Eliminar postulaciones
- API REST con FastAPI
- Consumo de API desde Angular
- Base de datos local con SQLite

## Estructura del proyecto

gcp-fullstack-app/
  backend/
    app/
      main.py
      database.py
      models.py
      schemas.py
      routes.py
      dependencies.py
    requirements.txt

  frontend/
    src/
    angular.json
    package.json


## Cómo ejecutar el backend

Entrar a la carpeta del backend:

cd backend

Crear y activar entorno virtual:

python -m venv venv
venv\Scripts\activate

Instalar dependencias:

pip install -r requirements.txt

Ejecutar servidor:

uvicorn app.main:app --reload

El backend queda disponible en:

http://127.0.0.1:8000

Documentación Swagger:

http://127.0.0.1:8000/docs

## Cómo ejecutar el frontend

Entrar a la carpeta del frontend:

cd frontend

Instalar dependencias:

npm install

Ejecutar Angular:

ng serve

El frontend queda disponible en:

http://localhost:4200

## Endpoints principales
GET     /applications/
POST    /applications/
GET     /applications/{id}
PUT     /applications/{id}
DELETE  /applications/{id}
Variables y configuración

Actualmente el frontend consume el backend local desde:

http://127.0.0.1:8000/applications

Para producción, esta URL deberá cambiarse por la URL generada por Cloud Run.

## Estado del proyecto

Proyecto funcional en ambiente local.

Pendiente:

Editar postulaciones desde Angular
Preparar backend para producción
Desplegar backend en Cloud Run
Desplegar frontend en Firebase Hosting
Conectar frontend desplegado con backend desplegado