Carbon Grid

An asynchronous backend data pipeline for ingesting, storing and analysing carbon intensity data.

The project demonstrates how external environmental data can be collected, processed asynchronously and exposed through APIs and dashboards.

Carbon Grid retrieves carbon intensity data from an external API, validates and stores it in a relational database, and provides endpoints for querying records, generating reports and visualising trends.

⸻

Dashboard Preview

![Carbon Grid Dashboard](images/dashboard.png)

⸻

Overview

Modern backend systems often integrate with external data sources, process incoming data asynchronously and expose structured outputs through APIs.

Carbon Grid demonstrates a simplified architecture of such a system.

The application retrieves carbon intensity data, stores it in a database and allows users to explore and analyse the data through API endpoints and a lightweight dashboard.

⸻

Core Capabilities
	•	External API integration for retrieving carbon intensity data
	•	Data ingestion pipeline with validation and normalisation
	•	Relational data storage for carbon records and regions
	•	REST API endpoints for accessing stored data
	•	Dashboard endpoint summarising key metrics
	•	Background processing using Celery workers
	•	Redis-based message queue for asynchronous tasks
	•	Scheduled ingestion using Celery Beat
	•	Asynchronous report generation
	•	Email notification after report generation
	•	Rate limiting on critical endpoints
	•	Structured logging for observability
	•	Containerised environment using Docker

⸻

Technology Stack
	•	Python
	•	Django
	•	Django REST Framework
	•	Celery
	•	Redis
	•	django-celery-beat
	•	django-celery-results
	•	Chart.js
	•	Docker

⸻

System Architecture

The system follows a typical backend architecture used in data ingestion platforms.

External Carbon API
        ↓
Django API endpoint
        ↓
Celery task queue (Redis)
        ↓
Celery worker processes task
        ↓
Data validation and normalisation
        ↓
Database storage
        ↓
API endpoints
        ↓
Dashboard / report generation


⸻

Data Ingestion Pipeline

The ingestion pipeline retrieves carbon intensity data and transforms it into structured database records.

Workflow:
	1.	A request triggers the ingestion endpoint
	2.	The endpoint pushes a background task to Celery
	3.	Redis queues the task
	4.	A Celery worker processes the task asynchronously
	5.	Data is validated and saved to the database
	6.	Logs are written for monitoring and debugging

This architecture prevents long-running operations from blocking the API server.

⸻

Asynchronous Task Processing

Background jobs are executed using Celery workers.

Tasks include:
	•	Carbon intensity ingestion
	•	Report generation
	•	Email delivery after report completion

Running these tasks outside the request lifecycle improves system responsiveness and scalability.

⸻

Scheduled Jobs

Data ingestion can run automatically using Celery Beat.

A scheduled task periodically retrieves carbon intensity data and stores it in the database, allowing the system to build a historical dataset.

⸻

API Endpoints

Ingest carbon intensity data

POST /api/ingest/

Triggers asynchronous ingestion of carbon intensity data.

⸻

Retrieve stored records

GET /api/records/

Returns stored carbon intensity records.

⸻

Dashboard summary

GET /api/dashboard-summary/

Returns aggregated data for the dashboard.

⸻

Generate report

POST /api/reports/generate/

Triggers asynchronous report generation and email delivery.

⸻

Logging

Structured logging is implemented for the ingestion pipeline.

Logs include:
	•	ingestion start events
	•	processed record counts
	•	data processing events

Logs are written to:

logs/app.log


⸻

Running the Project Locally

Clone the repository and install dependencies.

Install dependencies:

pip install -r requirements.txt

Run Django:

python manage.py runserver

Start Redis:

redis-server

Start Celery worker:

celery -A config worker -l info

Start Celery Beat scheduler:

celery -A config beat -l info

The application will be available at:

http://127.0.0.1:8000

Dashboard:

http://127.0.0.1:8000/api/dashboard/


⸻

Running with Docker

Build the container image:

docker build -t carbon-grid .

Run the container:

docker run -p 8000:8000 carbon-grid

The application will be accessible on port 8000.

⸻

Project Structure

carbon-grid
│
├ config/              Django project configuration
├ core/                Main application logic
├ templates/           Dashboard templates
├ images/              README assets
├ logs/                Application logs
│
├ Dockerfile
├ requirements.txt
├ manage.py
├ README.md


⸻

Why This Project

This project demonstrates common backend engineering patterns used in production systems:
	•	asynchronous processing
	•	background workers
	•	data ingestion pipelines
	•	scheduled jobs
	•	structured logging
	•	containerised environments

The goal is to simulate a real-world backend service that collects and processes environmental data.

⸻

Possible Extensions

Future improvements could include:
	•	production database configuration
	•	distributed worker scaling
	•	authentication and user management
	•	advanced analytics on carbon intensity data
	•	improved dashboard visualisation
	•	API documentation using OpenAPI / Swagger
	•	monitoring and metrics integration

⸻

Author

Mohamad Mirzaei
