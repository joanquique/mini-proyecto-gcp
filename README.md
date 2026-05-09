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

```txt
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