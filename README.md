# Django DRF + Vue Todo Application
A comprehensive todo application built with Vue.js frontend, Django backend, PostgreSQL database and Nginx as a web server.

 <img alt="preview" src="https://raw.githubusercontent.com/mertcan-tas/drf-vue-todo/refs/heads/master/frontend/public/preview.gif" style="width: 100%">

## Features
- User authentication and authorization
- Create, read, update, and delete todo items
- Responsive design for all devices
- Nginx for serving static files and load balancing

### Installation

1. Clone the repository:
```bash
git clone https://github.com/mertcan-tas/drf-vue-todo.git
cd drf-vue-todo
```

2. Create environment file:
```bash
python genenv.py .env-copy > .env
```

3. Running the Project:
```bash
docker-compose up --build
```

3. Open a Browser:
```bash
open http://0.0.0.0:8000
```


The application will be available at:
- Frontend: http://localhost:8080
- Backend API: http://localhost:8000
- Admin panel: http://localhost:8000/admin

## API Endpoints

### Authentication
- `POST /api/auth/register/`: Register a new user
- `POST /api/auth/login/`: Log in and receive an authentication token
- `POST /api/auth/token/refresh/`: Refresh authentication token
- `PUT /api/auth/change-password/`: Change user password

### Todos
- `GET /api/todos/`: List all todos
- `POST /api/todos/`: Create a new todo
- `GET /api/todos/{id}/`: Get details of a specific todo
- `PATCH /api/todos/{id}/`: Update a specific todo
- `DELETE /api/todos/{id}/`: Delete a specific todo
- `PATCH /api/todos/{id}/toggle/`: Toggle todo completion status

### User
- `GET /api/user/detail/`: Get authenticated user details

### Using the API
```bash
# Creating a new todo (with token)
curl -X POST http://localhost:8000/api/todos/ \
     -H "Authorization: Bearer your_token_here" \
     -H "Content-Type: multipart/form-data" \
     -F "memo=Complete project"

# Getting all todos
curl -X GET http://localhost:8000/api/todos/ \
     -H "Authorization: Bearer your_token_here"
```

### Response Format
Todo Item:
```json
{
  "id": 1,
  "memo": "Complete project",
  "created_at": "2025-04-21T10:30:00Z",
  "updated_at": "2025-04-21T11:45:00Z",
  "is_completed": false,
}
```

## Database Schema

### Todo Model
- `id`: Primary key
- `memo`: Todo content/description
- `created_at`: Creation timestamp
- `updated_at`: Last update timestamp
- `is_completed`: Completion status
- `user`: Related user (Foreign Key)

### User Model
- Custom Django User model with email authentication

## Local Development

### Backend Setup
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run development server
python manage.py runserver
```

### Frontend Setup
```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Run development server
npm run dev 
```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact
Project Owner - [mertcan.tas@outlook.com](mertcan.tas@outlook.com)
