# Custom Authentication and Access Control System

This project implements a backend application with a custom authentication and authorization system, as required by the technical task.

## Implemented Features

### 1. User Management
- **Registration & Login**: Users can register and log in using email and password (JWT).
- **Profile Management**: Users can update their profile information.
- **Account Deletion**: "Soft" deletion functionality (deactivating the account).

### 2. Access Control (Rules)
- **Custom Rules System**: A flexible system to define access rules for users.
- **Rules API**: An API endpoint (`/api/v1/apps/rules/`) allows administrators to manage these rules.
    - Admins can create, read, update, and delete rules.

### 3. Technology Stack
- **Framework**: Django & Django Rest Framework (DRF)
- **Database**: PostgreSQL
- **Documentation**: Swagger/OpenAPI documentation available at `/api/docs/`

#swagger:
http://localhost:8000/api/docs/

running project:
docker compose up --build