# ASOUD Web Services

## Table of Contents

- [Directory Structure](#directory-structure)
- [Configuration](#configuration)
- [Installation](#installation)


## Project Directory Structure
```bash
.
├── .env
├── .gitignore
├── Dockerfile
├── config
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── development.py
│   │   └── production.py
│   └── urls.py
├── data
│   └── nginx
│       ├── nginx.dev.conf
│       └── nginx.prod.conf
├── docker-compose.dev.yaml
├── docker-compose.prod.yaml
├── entrypoint.sh
├── manage.py
└── requirements.txt
```

## Configuration
Before running the project, make sure to set these environment variables either in a `.env` file (for local development) or through your server's environment configuration. Properly configuring these variables will ensure the smooth functioning of your project.

#### Django Project Configuration
- **SECRET_KEY**: The Django project's secret key used for cryptographic signing. Keep this key confidential and do not share it publicly.
- **LOGLEVEL**: The logging level for the Django project. It determines the severity of logs to be recorded (e.g., DEBUG, INFO, WARNING, ERROR, etc.).

#### Database Variables

- **DATABASE**: The database (e.g., MySql, PostgreSql).
- **DATABASE_NAME**: The name of the database.
- **DATABASE_USERNAME**: The username to access the database.
- **DATABASE_PASSWORD**: The password for the database user.
- **DATABASE_HOST**: The host address of the database server.
- **DATABASE_PORT**: The port number for the database server.

## Installation
To set up the Project, follow these steps:

1. **Install Docker and Docker Compose:** If you don't have Docker and Docker Compose installed, follow the instructions for your operating system:
    - [Docker Desktop for Windows](https://docs.docker.com/desktop/windows/install/)
    - [Docker Desktop for macOS](https://docs.docker.com/desktop/mac/install/)
    - [Docker Engine for Linux](https://docs.docker.com/engine/install/)

2. **Clone the repository:**
    ```bash
    git clone https://github.com/jam4li/asoud.git
    cd asoud/
    ```

3. **Choose the appropriate Docker Compose file for your environment:**
    * For development, use docker-compose.dev.yaml:
        ```bash
        docker-compose -f docker-compose.dev.yaml build
        docker-compose -f docker-compose.dev.yaml up -d
        ```

    * For production, use docker-compose.prod.yaml:
        ```bash
        docker-compose -f docker-compose.prod.yaml build
        docker-compose -f docker-compose.prod.yaml up -d
        ```

## Product Category API Endpoints

These endpoints provide hierarchical product categories tied to a job subcategory.

| Method | Endpoint | Description |
| ------ | -------- | ----------- |
| GET | `/api/v1/product/category/group/list/<sub_category_id>/` | List product category groups for a subcategory |
| GET | `/api/v1/product/category/list/<group_id>/` | List product categories within a group |
| GET | `/api/v1/product/category/sub/list/<category_id>/` | List product subcategories within a category |