# pizza_ordering_backend_service
Django learning project - pizza_ordering_backend_service


## Django Fundamentals
Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design
Follows Model-View-Template (MVT) architecture (similar to MVC)
Provides built-in admin interface, ORM, authentication system


## Key Components
- **Models**: Define your database schema
- **Views**: Handle request processing and business logic
- **Templates**: Render HTML dynamically
- **URLs**: Map URLs to specific views
- **Forms**: Handle user input validation


## Pizza Ordering API Setup Guide

### Final Project Structure
```
pizza_project/
│
├── data.json
├── manage.py
│
├── pizza_project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
└── pizza_api/
    ├── __init__.py
    ├── views.py
    ├── urls.py
    └── models.py
```

### Setup and Running Steps
1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

2. Install Django:
```bash
pip install django
```

3. Run migrations:
```bash
python manage.py migrate
```

4. Start the development server:
```bash
python manage.py runserver
```

### API Endpoints
- `GET /menu`: Fetch all pizzas or a specific pizza
  - Example: `http://localhost:8000/menu?name=Margherita`
- `POST /order`: Place an order
  - Example request body: `[{"id": 1, "quantity": 2}, {"id": 3, "quantity": 1}]`

### Testing the API
You can use tools like:
- Postman
- curl
- Python's `requests` library
- Web browser (for GET requests)

### Example Curl Commands
```bash
# Get all menu items
curl http://localhost:8000/menu

# Get a specific pizza
curl "http://localhost:8000/menu?name=Margherita"

# Place an order
curl -X POST -H "Content-Type: application/json" \
     -d '[{"id": 1, "quantity": 2}, {"id": 3, "quantity": 1}]' \
     http://localhost:8000/order
```