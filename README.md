<h1 align="center">📝 Django To-Do List App</h1>

<p align="center">
A simple and powerful task management web application built using Django.
</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Django](https://img.shields.io/badge/Django-5.x-green?style=for-the-badge&logo=django)
![SQLite](https://img.shields.io/badge/SQLite-Database-blue?style=for-the-badge&logo=sqlite)
![GitHub](https://img.shields.io/github/stars/techiebella/to-do-list?style=for-the-badge)

</p>

---

## 🌐 Live Demo

**Application:** https://todolistapp-c14l.onrender.com

> **Note:** This application is hosted on Render's free plan. If the server is inactive, the first request may take **30–60 seconds** to load.

---

## 🚀 About the Project

The Django To-Do List App is a full-stack web application that helps users organize and manage their daily tasks efficiently.

The application includes a secure authentication system, allowing users to create personal accounts and manage their own tasks. Users can create, edit, delete, and mark tasks as completed through a clean and responsive user interface.

This project was developed to strengthen Django development skills by implementing authentication, CRUD operations, template inheritance, responsive UI design, and deployment.

---

## ✨ Features

- User Registration
- User Login and Logout
- Create Tasks
- View Tasks
- Edit Tasks
- Delete Tasks
- Mark Tasks as Completed
- Responsive Design
- Light Mode
- Dark Mode
- Secure Authentication
- Bootstrap-based User Interface

---

## 🛠️ Tech Stack

| Category | Technologies |
|-----------|--------------|
| Frontend | HTML5, CSS3, Bootstrap 5 |
| Backend | Python, Django |
| Database | SQLite |
| Version Control | Git |
| Repository | GitHub |
| Deployment | Render |

---

## 📂 Project Structure

```text
to-do-list/
│
├── static/
│   └── css/
│       └── style.css
│
├── staticfiles/
│
├── tasks/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── login.html
│   ├── register.html
│   ├── task_form.html
│   └── task_list.html
│
├── todo_project/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── .gitignore
├── db.sqlite3
├── LICENSE
├── manage.py
├── README.md
└── requirements.txt
```
```

---

## 📸 Screenshots

### 🔐 Login Page (Light Mode) <p align="center"> <img src="https://github.com/user-attachments/assets/41c81116-bfa0-4fe2-be30-7d6108a4973c" width="900"/> </p> ### 🌙 Login Page (Dark Mode) <p align="center"> <img src="https://github.com/user-attachments/assets/e274e065-2549-4efd-8e20-ef65aad6f5af" width="900"/> </p> ### 📝 Register Form (Light Mode) <p align="center"> <img src="https://github.com/user-attachments/assets/1a36ae18-e960-4d54-951e-1fd9535e8f6e" width="500"/> </p> ### 🌙 Register Form (Dark Mode) <p align="center"> <img src="https://github.com/user-attachments/assets/7b8a02f7-327e-42ce-a8f6-ad86b1fb7140" width="500"/> </p> ### 🏠 Home Page (Light Mode) <p align="center"> <img src="https://github.com/user-attachments/assets/58fb7e2d-bdda-4aae-9283-7bb74bbe29b5" width="900"/> </p> ### 🌙 Home Page (Dark Mode) <p align="center"> <img src="https://github.com/user-attachments/assets/cddb527a-e655-466d-a11f-c2615b7708b0" width="900"/> </p> ### 📌 Task Form <p align="center"> <img src="https://github.com/user-attachments/assets/55124d5b-cb54-4a34-89ea-837ace2a86a2" width="500"/> </p>
---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/techiebella/to-do-list.git
```

### 2. Navigate to the Project Directory

```bash
cd to-do-list
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Apply Database Migrations

```bash
python manage.py migrate
```

### 7. Create a Superuser (Optional)

```bash
python manage.py createsuperuser
```

### 8. Run the Development Server

```bash
python manage.py runserver
```

### 9. Open the Application

```
http://127.0.0.1:8000/
```

---

## 🚀 Deployment

This project is deployed using **Render**.

Deployment steps:

1. Push the project to GitHub.
2. Create a Web Service on Render.
3. Connect the GitHub repository.
4. Install dependencies from `requirements.txt`.
5. Configure environment variables.
6. Deploy the application.

---

## 🔮 Future Improvements

- Task Categories
- Due Dates
- Priority Levels
- Search Functionality
- Task Filtering
- Email Notifications
- User Profile
- REST API
- Docker Support
- PostgreSQL Database
- Password Reset via Email

---

## 🤝 Contributing

Contributions are welcome.

If you would like to contribute:

1. Fork the repository.
2. Create a new branch.

```bash
git checkout -b feature-name
```

3. Commit your changes.

```bash
git commit -m "Add new feature"
```

4. Push the branch.

```bash
git push origin feature-name
```

5. Open a Pull Request.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👩‍💻 Author

**Eswari**

Computer Science Student | Aspiring Full Stack Developer

GitHub: https://github.com/techiebella

---

## ⭐ Support

If you found this project helpful, consider giving it a **Star** on GitHub.

It helps others discover the project and motivates future improvements.

---

<p align="center">
Made with ❤️ using Django
</p>
