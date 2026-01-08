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

---

## Git Workflow for Feature Development

### 1. Checkout the feature branch for location CRUD

```bash
# Fetch the latest branches from remote
git fetch origin

# Checkout the location CRUD feature branch
git checkout feature/location-crud

# If the branch doesn't exist locally, create it from the remote branch
git checkout -b feature/location-crud origin/feature/location-crud
```

### 2. Make your changes

After making changes to the code, add your files:

```bash
# Add all changes
git add .

# Or add specific files
git add <file_name>
```

### 3. Commit with conventional commit rules

This project follows conventional commits specification:

```bash
# Format: <type>(<scope>): <description>

# Examples:
git commit -m "feat(location): add location CRUD operations"
git commit -m "fix(location): fix location validation error"
git commit -m "docs(location): update location API documentation"
git commit -m "refactor(location): refactor location serializer"
git commit -m "test(location): add tests for location views"
```

Common commit types:
- `feat`: New features
- `fix`: Bug fixes
- `docs`: Documentation changes
- `style`: Code style changes (formatting, missing semicolons, etc.)
- `refactor`: Code changes that neither fixes a bug nor adds a feature
- `test`: Adding or correcting tests
- `chore`: Other changes that don't modify src or test files

### 4. Push your feature branch to origin

```bash
# Push the feature branch to remote repository
git push origin feature/location-crud

# If this is the first push, you might need to set upstream
git push --set-upstream origin feature/location-crud
```

### 5. Create a Pull Request

After pushing your changes, create a pull request from your feature branch to the main branch through the GitHub interface.

---

## API Documentation

The API endpoints for location management are available at:
- `GET /api/location/` - List all locations
- `POST /api/location/` - Create a new location
- `GET /api/location/<id>/` - Get a specific location
- `PUT /api/location/<id>/` - Update a specific location
- `PATCH /api/location/<id>/` - Partially update a specific location
- `DELETE /api/location/<id>/` - Delete a specific location
- `GET /api/location/name/<name>/` - Get location by name