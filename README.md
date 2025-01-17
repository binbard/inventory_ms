# Inventory Management System

A robust Django-based inventory management solution for efficient tracking and management of business inventory, suppliers, and sales.

## Overview

This system provides businesses with a comprehensive solution for managing their inventory operations. Built with Django, it offers real-time stock tracking and automated inventory movement validation.

## Features

- **Product Management**
  - Add and update product information
  - Track stock levels in real-time
  - Manage product categories and variants

- **Supplier Management**
  - Maintain supplier profiles
  - Track supplier performance
  - Manage supplier relationships

- **Stock Movement**
  - Automated stock level tracking
  - No manual stock adjustments allowed
  - Real-time validation of stock levels

- **Sales Tracking**
  - Record and monitor sales transactions
  - Automatic stock deduction
  - Sales history and reporting

## Installation

1. Clone the repository:
```bash
git clone https://github.com/binbard/inventory_ms
```

2. Navigate to the project directory:
```bash
cd inventory_system
```

3. Install required dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Start the development server:
```bash
python manage.py runserver 0.0.0.0:8000
```

## Deployment

The application can be deployed on various platforms:
- Heroku
- Amazon Web Services (AWS)
- Any server supporting Django applications

### Deployment Requirements
- Valid database credentials
- Secure environment variables setup

## Usage

1. Access the application through your deployment URL or localhost
2. Use the navigation bar to access different features:
   - Product Management
   - Supplier Management
   - Sales Orders
   - Stock Movement
3. Follow the intuitive interface to manage your inventory

## System Requirements

- Python 3.8+
- Django 3.2+
- Web browser with JavaScript enabled
