# CodeCraftHub 📚

## 📌 Project Overview

**CodeCraftHub** is a simple beginner-friendly REST API built with **Python Flask** that allows developers to track learning courses they want to complete.

It helps users manage courses without needing a database by storing all data in a simple **JSON file (`courses.json`)**.

This project is designed for learners who want to understand:

* REST API fundamentals
* CRUD operations
* JSON file storage in Python
* Flask routing and request handling

---

## 🚀 Features

* Create a new course
* View all courses
* View a single course
* Update a course
* Delete a course
* Automatic ID generation
* Input validation (status, date format, required fields)
* JSON file-based storage (no database required)
* Beginner-friendly Flask structure

---

## 🛠️ Technologies Used

* Python 3
* Flask
* JSON (file storage)
* REST API principles

---

## 📦 Installation Instructions

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/CodeCraftHub.git
cd CodeCraftHub
```

---

### 2. Install Python (if not installed)

Download Python from:
https://www.python.org/downloads/

Make sure to check:
✔ "Add Python to PATH"

---

### 3. Create virtual environment (recommended)

```bash
python -m venv venv
```

Activate it:

**Windows:**

```bash
venv\Scripts\activate
```

---

### 4. Install dependencies

```bash
pip install flask
```

OR (if requirements file exists):

```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run the Application

Start the Flask server:

```bash
python app.py
```

You will see:

```
Running on http://127.0.0.1:5000
```

---

## 🔗 API Endpoints Documentation

### 1. Create a Course

**POST** `/api/courses`

```bash
curl -X POST http://127.0.0.1:5000/api/courses ^
-H "Content-Type: application/json" ^
-d "{\"name\":\"Flask Basics\",\"description\":\"Learn Flask\",\"target_date\":\"2026-08-01\",\"status\":\"Not Started\"}"
```

---

### 2. Get All Courses

**GET** `/api/courses`

```bash
curl http://127.0.0.1:5000/api/courses
```

---

### 3. Get Single Course

**GET** `/api/courses/<id>`

```bash
curl http://127.0.0.1:5000/api/courses/1
```

---

### 4. Update Course

**PUT** `/api/courses/<id>`

```bash
curl -X PUT http://127.0.0.1:5000/api/courses/1 ^
-H "Content-Type: application/json" ^
-d "{\"name\":\"Updated Flask\",\"description\":\"Updated course\",\"target_date\":\"2026-09-01\",\"status\":\"In Progress\"}"
```

---

### 5. Delete Course

**DELETE** `/api/courses/<id>`

```bash
curl -X DELETE http://127.0.0.1:5000/api/courses/1
```

---

## 🧪 Testing Instructions

You can test the API using:

### Option 1: Curl (Command Line)

* Use the examples above

### Option 2: Postman (Recommended)

* Create a new request
* Select GET/POST/PUT/DELETE
* Paste URL
* Add JSON body for POST/PUT

### Option 3: Browser

* Only works for GET requests:

```
http://127.0.0.1:5000/api/courses
```

---

## 📁 Project Structure

```
CodeCraftHub/
│
├── app.py              # Main Flask application (API logic)
├── courses.json        # Stores course data in JSON format
├── requirements.txt    # Python dependencies
├── README.md           # Project documentation
└── venv/               # Virtual environment (optional)
```

---

## ⚠️ Troubleshooting Common Issues

### ❌ 1. "git is not recognized"

👉 Install Git from:
https://git-scm.com/downloads

---

### ❌ 2. "Flask not found"

Fix:

```bash
pip install flask
```

---

### ❌ 3. "415 Unsupported Media Type"

Cause:
Missing header

Fix:

```
Content-Type: application/json
```

---

### ❌ 4. curl not working in CMD

Use ONE line only in Windows CMD:

```bash
curl -X POST http://127.0.0.1:5000/api/courses -H "Content-Type: application/json" -d "{\"name\":\"Test\",\"description\":\"Test\",\"target_date\":\"2026-01-01\",\"status\":\"Not Started\"}"
```

---

### ❌ 5. Port already in use

Change port in `app.py`:

```python
app.run(port=5001)
```

---

## 🎯 Learning Goals

After completing this project, you will understand:

* How REST APIs work
* How CRUD operations are implemented
* How Flask handles routing
* How to store data without a database
* How JSON file storage works in Python

---

## 🚀 Future Improvements

* Add frontend dashboard (HTML/React)
* Add authentication system
* Move from JSON to SQLite database
* Deploy online (Render / Railway / Azure)
* Add course categories and progress tracking

---

## 👨‍💻 Author

Built as a learning project for mastering Flask REST APIs.

---

## 📌 License

This project is open-source and free to use for learning purposes.
