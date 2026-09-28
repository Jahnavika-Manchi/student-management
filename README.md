# FastAPI Student Management API

A simple **Student Management REST API** built using **FastAPI and Pydantic**.
This project demonstrates CRUD operations, request validation, error handling, duplicate-user checking, and Swagger API testing.

## 🚀 Features

* Create a new student
* Get all students
* Get a student by ID
* Update a student
* Delete a student
* Email validation
* Name validation
* Age type validation
* Duplicate email checking
* 404 error handling when a student doesn't exist
* Interactive Swagger API documentation

## 🛠️ Technologies Used

* Python
* FastAPI
* Pydantic
* Uvicorn
* Swagger UI

## 📁 Project Structure

```text
student-management-api/
│
├── main.py
└── README.md
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to the project

```bash
cd student-management-api
```

### 3. Install dependencies

```bash
pip install fastapi uvicorn email-validator
```

## ▶️ Run the Application

Start the FastAPI server using:

```bash
uvicorn main:app --reload
```

The API will run at:

```text
http://127.0.0.1:8000
```

## 📖 Swagger Documentation

Open the following URL in your browser:

```text
http://127.0.0.1:8000/docs
```

Swagger UI allows you to test all API endpoints directly from the browser.

## 🔗 API Endpoints

| Method | Endpoint                 | Description          |
| ------ | ------------------------ | -------------------- |
| POST   | `/students`              | Create a new student |
| GET    | `/students`              | Get all students     |
| GET    | `/students/{student_id}` | Get student by ID    |
| PUT    | `/students/{student_id}` | Update a student     |
| DELETE | `/students/{student_id}` | Delete a student     |

## 📝 Create Student

### POST `/students`

Request:

```json
{
  "name": "Rahul",
  "email": "rahul@gmail.com",
  "course": "Python Full Stack",
  "age": 22
}
```

Response:

```json
{
  "id": 1,
  "name": "Rahul",
  "email": "rahul@gmail.com",
  "course": "Python Full Stack",
  "age": 22
}
```

## 🔍 Get All Students

### GET `/students`

Returns all registered students.

Example response:

```json
[
  {
    "id": 1,
    "name": "Rahul",
    "email": "rahul@gmail.com",
    "course": "Python Full Stack",
    "age": 22
  }
]
```

## 🔎 Get Student By ID

### GET `/students/{student_id}`

Example:

```text
GET /students/1
```

If the student exists, the student details are returned.

If the student doesn't exist:

```json
{
  "detail": "Student not found"
}
```

Status code:

```text
404 Not Found
```

## ✏️ Update Student

### PUT `/students/{student_id}`

Example:

```text
PUT /students/1
```

Request:

```json
{
  "name": "Rahul Kumar",
  "email": "rahulkumar@gmail.com",
  "course": "FastAPI",
  "age": 23
}
```

## 🗑️ Delete Student

### DELETE `/students/{student_id}`

Example:

```text
DELETE /students/1
```

Response:

```json
{
  "message": "Student deleted successfully"
}
```

## 🚫 Duplicate Student Validation

The API checks whether the email already exists before creating a student.

If the same email is submitted again:

```json
{
  "name": "Rahul Kumar",
  "email": "rahul@gmail.com",
  "course": "FastAPI",
  "age": 23
}
```

The API returns:

```json
{
  "detail": "User already exists"
}
```

Status code:

```text
400 Bad Request
```

## ✅ Input Validation

The API uses **Pydantic** for validation.

### Name

Name cannot be empty.

### Email

Email must be in a valid email format.

Example:

```text
rahul@gmail.com
```

### Age

Age must be an integer.

Valid:

```json
"age": 22
```

Invalid:

```json
"age": "twenty two"
```

## ❌ Error Handling

The API handles cases where a student doesn't exist.

Response:

```json
{
  "detail": "Student not found"
}
```

Status code:

```text
404
```

## 📊 CRUD Operations

```text
CREATE  → POST
READ    → GET
UPDATE  → PUT
DELETE  → DELETE
```

## 🧠 Concepts Demonstrated

* FastAPI application creation
* REST API development
* HTTP methods
* Pydantic models
* Request validation
* Path parameters
* JSON request and response
* HTTP status codes
* Exception handling
* CRUD operations
* Swagger UI
* In-memory data storage

## 🔮 Future Improvements

The current project uses an in-memory Python list for storing student data.

Future improvements could include:

* MongoDB integration
* PostgreSQL integration
* SQLAlchemy
* Authentication and authorization
* JWT authentication
* Search students by course
* Pagination
* React frontend integration
* Docker deployment

## 👨‍💻 Author

**Jaanu**

Built as a hands-on **FastAPI CRUD API project** for learning and interview preparation.

