# Django E-Commerce Website

A simple and functional e-commerce website built using Django and Python. This project demonstrates core Django concepts including authentication, product management, forms, models, CRUD operations, database relationships, and template-based web development.

## Features

- User login and logout
- User authentication
- Product dashboard
- Add products
- View product details
- Edit products
- Delete products
- Product categories
- Product stock management
- Active/inactive product status
- Low stock identification
- Product image upload
- Django ModelForm
- ForeignKey relationship between Category and Product
- SQLite database
- Responsive and simple user interface

## Technologies Used

- Python
- Django
- HTML
- CSS
- SQLite
- Bootstrap
- Django Templates

## Project Structure

```text
Ecommerce/
│
├── ecomm_app/
│   ├── migrations/
│   ├── templates/
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── Ecommerce/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Main Functionalities

### Authentication

The project includes login and logout functionality using Django's built-in authentication system.

### Product Management

Users can:

- Add a new product
- View product details
- Edit existing products
- Delete products
- Check product stock
- Check product status

### Category Management

Products are connected to categories using a Django `ForeignKey` relationship.

Example:

```python
category = models.ForeignKey(Category, on_delete=models.CASCADE)
```

This allows multiple products to belong to the same category.

### Product Status

Products can be marked as:

- Active
- Inactive

The dashboard also displays product statistics such as total products, active products, inactive products, and low-stock products.

## Installation

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Open the project

```bash
cd Ecommerce
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

Windows:

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run migrations

```bash
python manage.py migrate
```

### 7. Create a superuser

```bash
python manage.py createsuperuser
```

### 8. Start the development server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

## Future Improvements

The project can be extended with:

- Shopping cart
- Wishlist
- Order management
- Payment gateway
- User registration
- Product search
- Product filtering
- Product pagination
- Customer profile
- Order history
- REST API
- Better responsive UI

## Learning Purpose

This project was developed to practice and demonstrate Django web development concepts, including:

- Django Models
- Views
- Templates
- Forms
- ModelForms
- URL routing
- Authentication
- CRUD operations
- ForeignKey relationships
- Database operations
- Django sessions
- File uploads

## Author

**Vijay Singh**

MCA Graduate  
Python Full Stack Intern

## License

This project is created for educational and portfolio purposes.