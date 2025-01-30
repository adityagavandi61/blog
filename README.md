# Blog Website

## Overview
This is a full-featured blog website built using Django. It allows users to create, read, update, and delete blog posts. The website supports user authentication, categorization, and comments on posts.

## Features
- User authentication (Sign Up, Login, Logout)
- Create, update, and delete blog posts
- Categorization of posts
- Commenting system
- Responsive design

## Technologies Used
- **Backend:** Django, SQLite/PostgreSQL
- **Frontend:** HTML, CSS, JavaScript, Bootstrap
- **Authentication:** Django Authentication System

## Installation
### Prerequisites
Make sure you have Python installed (version 3.x recommended). You also need to have pip installed.

### Steps
1. **Clone the repository**
   ```sh
   git clone https://github.com/yourusername/blog-website.git
   cd blog-website
   ```

2. **Create a virtual environment**
   ```sh
   python -m venv venv
   source venv/bin/activate  # For macOS/Linux
   venv\Scripts\activate    # For Windows
   ```

3. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```

4. **Apply migrations**
   ```sh
   python manage.py migrate
   ```

5. **Create a superuser (optional)**
   ```sh
   python manage.py createsuperuser
   ```

6. **Run the server**
   ```sh
   python manage.py runserver
   ```

7. Open your browser and go to `http://127.0.0.1:8000/`.

## Usage
- Users can register, log in, and write blog posts.
- Posts can be categorized, edited, and deleted.
- Users can comment on posts.

## Project Structure
```
blog-website/
│-- blog/             # Main app (handles posts, categories, comments)
│-- post/            # Authentication system (sign up, login, profile)
│-- static/           # CSS, JavaScript, images
│-- templates/        # HTML templates
│-- db.sqlite3        # Database file (if using SQLite)
│-- manage.py         # Django project manager
│-- requirements.txt  # Dependencies
```

## Contributing
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Open a pull request.

## License
This project is licensed under the MIT License. See `LICENSE` for details.

## Contact
For any issues, reach out to [your email] or open an issue on GitHub.

