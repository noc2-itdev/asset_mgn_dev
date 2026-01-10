# DRF Backend for Asset Management System

This project sets up a full-stack Django Rest Framework application, powered by:

- DRF 3.16.1
- PostgreSQL 15 (docker container or standalone)

---

## Prerequisites

- Python 3.10 or higher
- Check your Python version:
  python -V

---

## 🛠 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/noc2-itdev/asset_mgn_dev.git
```

### 2. Create and install packages in venv

```bash
python -m venv venv
venv\Scripts\activate.bat  (Os Windows)
source venv/bin/activate  (Os Linux)
python -m pip install -r requirements.txt
```

### 3. Run project Django

```bash
python manage.py runserver 0.0.0.0:8000
```

### 4. Access the application

```bash
http://localhost:8000
```

### 5. Create .env file in the root directory of your project and add the following environment variables:

```bash
DATABASE_ENGINE=django.db.backends.postgresql_psycopg2
DATABASE_NAME=asset_mgn
DATABASE_USER=noc2_user
DATABASE_PASSWORD=asset_mgn_password
DATABASE_HOST=X.X.X.X
DATABASE_PORT=5432
```

## Feature Development: Department App

### Creating Department App Feature Branch

```bash
# Switch to the department feature branch
git checkout feature/department-crud

# If the branch doesn't exist, create it
git checkout -b feature/department-crud origin/feature/department-crud

# Follow the same commit and push patterns as location app
git commit -m "feat(department): add department CRUD operations"
git push origin feature/department-crud
```

### Creating Category App Feature Branch

```bash
# Switch to the category feature branch
git checkout feature/category-crud

# If the branch doesn't exist, create it
git checkout -b feature/category-crud origin/feature/category-crud

# Follow the same commit and push patterns as location app
git commit -m "feat(category): add category CRUD operations"
git push origin feature/category-crud
```

### API Endpoints Structure

The project follows a consistent pattern for API endpoints across different apps:

### API Endpoints for Department

**Department endpoints:**
- `GET /department/` - List all departments
- `POST /department/` - Create a new department
- `GET /department/<id>/` - Get a specific department
- `PUT /department/<id>/` - Update a specific department
- `PATCH /department/<id>/` - Partially update a specific department
- `DELETE /department/<id>/` - Delete a specific department

**Category endpoints:**
- `GET /category/` - List all categories
- `POST /category/` - Create a new category
- `GET /category/<id>/` - Get a specific category
- `PUT /category/<id>/` - Update a specific category
- `PATCH /category/<id>/` - Partially update a specific category
- `DELETE /category/<id>/` - Delete a specific category
- `GET /department/name/<name>/` - Get department by name

### Implementation Details

The department app follows the same structure as the location and person apps:
- `serializers.py` - Handles data conversion between model and JSON
- `views.py` - Processes HTTP requests for department management
- `urls.py` - Defines URL patterns for the department endpoints
