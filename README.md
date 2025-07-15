# User Sync

This FastAPI project allows an MSP to register tenants (Microsoft 365 / Google Workspace) and automatically sync users to a ticketing system via background job.

## Features
- Add tenants via `/tenants` POST endpoint
- Secure credential storage using Fernet
- Dockerized for easy deployment

## Usage

```bash
docker compose up --build
```

Access at: `http://localhost:8000/docs`
