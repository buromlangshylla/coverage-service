# Coverage Service API

A Django REST Framework service for managing insurance coverages and customer-selected add-ons.

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <your-repo-url>
   cd coverage-service
   ```

2. **Create and activate a virtual environment:**
   ```
   python -m venv coverage-venv
   coverage-venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

4. **Configure environment variables:**
   Create a `.env` file in the root directory:
   ```
   SECRET_KEY=coverage-secret
   DEBUG=True
   DATABASE_NAME=coverage_service.sqlite3
   ```

5. **Run migrations:**
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Start the development server:**
   ```
   python manage.py runserver
   ```

## API Endpoints

### Coverage

- `GET /api/v1/coverages/`  
  List all coverages.  
  **Filters:** `status`, `name`

- `POST /api/v1/coverages/`  
  Create a new coverage (requires authentication).

- `GET /api/v1/coverages/{id}/`  
  Retrieve a coverage by ID.

- `PUT /api/v1/coverages/{id}/`  
  Update a coverage (requires authentication).

- `DELETE /api/v1/coverages/{id}/`  
  Delete a coverage (requires authentication).

### Customer Coverage

- `GET /api/v1/customer-coverages/`  
  List all customer coverages.  
  **Filters:** `customer_id`, `policy_id`, `status`

- `POST /api/v1/customer-coverages/`  
  Create a new customer coverage (requires authentication).

- `GET /api/v1/customer-coverages/{id}/`  
  Retrieve a customer coverage by ID.

- `PUT /api/v1/customer-coverages/{id}/`  
  Update a customer coverage (requires authentication).

- `DELETE /api/v1/customer-coverages/{id}/`  
  Delete a customer coverage (requires authentication).

- `GET /api/v1/customers/{customer_id}/coverages/`  
  List all coverages purchased by a specific customer.

## Data Types

- `id`: UUID
- `name`: string
- `description`: string
- `cost`, `premium`, `max_coverage_amount`: decimal
- `currency`: string (default: "INR")
- `status`: string (choices vary by model)
- `effective_date`, `expiry_date`, `added_at`, `created_at`, `updated_at`: date/time

## API Documentation (Swagger)

- **Swagger UI:**  
  Visit [`/api/v1/swagger/`](http://127.0.0.1:8000/api/v1/swagger/) for interactive API docs.

## Postman Collection

The Postman collection for this API is included in the repository as `insurance.postman_collection.json`.

