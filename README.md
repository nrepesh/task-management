# task-management

This project is a simple **Task Management Application** built with a FastAPI backend and a React (Vite) frontend. It allows users to create, view, and delete tasks. The project uses Docker for containerized development and deployment.

## Features

- **Backend**: Built with FastAPI, it provides endpoints for task management (add, get, delete).
- **Frontend**: Built with React and styled with Tailwind CSS, it offers a simple user interface.
- **Database**: PostgreSQL is used for task storage.
- Fully containerized using Docker.

## Prerequisites

Ensure you have the following installed on your system:

- **Docker**: [Get Docker](https://www.docker.com/)
- **Docker Compose**: Comes with Docker Desktop

## Getting Started

### Clone the Repository

```bash
git clone https://github.com/nrepesh/task-management.git
```

### Running the Project
Run the application with Docker Compose:

```bash
docker-compose up --build
```
This will start the following services:

Backend: Runs on http://localhost:8000
Frontend: Runs on http://localhost:5173
PostgreSQL: Database running internally within Docker
PGAdmin: Runs on http://localhost:5051 

## Frontend Features

- Add Task: Enter a description and click "Add Task" to add a new task.
- View Tasks: The frontend fetches and displays all tasks from the backend.
- Delete Task: Click "Delete" next to a task to remove it.

## Backend Endpoints

- **GET /tasks**: Retrieve all tasks.
- **POST /tasks**: Add a new task.
  - Request Body:
    ```json
    {
        "description": "Your task description"
    }
    ```
- **DELETE /tasks/{id}**: Delete a task by ID.

## Technologies Used

### Backend
- **FastAPI**
- **PostgreSQL**
- **SQLAlchemy**
- **Pydantic**

### Frontend
- **React (Vite)**
- **Tailwind CSS**

### Deployment
- **Docker**
- **Docker Compose**

## Troubleshooting

### Common Issues

1. **Frontend not loading:**
   - Ensure you have the correct host and port in `vite.config.js`:
     ```javascript
     export default {
         server: {
             host: "0.0.0.0",
             port: 5173,
         },
     };
     ```

2. **node_modules empty**
    - /app/node_modules in the docker-compose creates an empty folder. It avoids conflicts within the docker container where npm is installed.

3. **auto-connecting pgadmin to postgres database**
    - create a servers.json file in pgadmin_data folder
    ```
    {
    "Servers": {
        "1": {
            "Name": "Postgres Database",
            "Group": "Servers",
            "Host": "postgres-db",
            "Port": 5432,
            "Username": "manager",
            "Password": "manager1",
            "SSLMode": "prefer",
            "MaintenanceDB": "postgres"
            }
        }
    }
    ``` 