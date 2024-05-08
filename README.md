# ToDoList
A simple yet powerful To-Do List API built using Django Rest Framework. Manage your tasks efficiently with features like pagination, throttling, permissions, and authentication.

## Features
- **CRUD Operations**: Perform Create, Read, Update, and Delete operations on your to-do items.
- **Pagination**: Limit the number of to-do items returned in each API response for better performance.
- **Throttling**: Prevent abuse and protect your API with rate limiting to control the number of requests per user.
- **Permissions**: Define fine-grained access control to restrict or allow users to perform certain actions based on their roles or permissions.
- **Authentication**: Secure your API endpoints with token-based authentication to ensure that only authorized users can access them.

# Getting Started
## Prerequisites
- Python 3.x
- Django
- Django Rest Framework
## Installation
**1. Clone the repository:**
   
`git clone https://github.com/yourusername/todo-list-api.git`

**2. Install dependencies:**   
`cd to_do_list`

`pip install -r requirements.txt`

**3. Apply migrations:**

`python manage.py migrate`

**6. Run the development server:**

`python manage.py runserver`

7. Access the API at **http://127.0.0.1:8000/.**

## Fork the repository
Create your feature branch (git checkout -b feature/my-feature)
Commit your changes (git commit -am 'Add my feature')
Push to the branch (git push origin feature/my-feature)
Create a new Pull Request

Please ensure that your code adheres to the project's coding conventions and includes appropriate tests.

## Acknowledgments
**Django**

**Django Rest Framework**

## Contact
For any inquiries or feedback, please contact jkishan421@gmail.com.
