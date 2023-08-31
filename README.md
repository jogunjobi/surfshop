# Surf Shop

This Django project is designed to manage products for Uncle Bill's surf shop. It has two main user roles: vendors and admins. Vendors can upload products, while admins can approve or reject them.

## Features:

- **Vendor Registration**: Vendors can register to the platform.
- **Product Upload**: Vendors can upload products with an image, product_name and product_description.
- **Product Approval**: Admins can view products awaiting approval and approve or reject them.
- **Product Listing**: Admins can view all products, both approved and pending.

## Setup:

1. **Clone the Repository**:
   ```
   git clone https://github.com/jogunjobi/surfshop.git
   cd surfshop
   ```

2. **Install Dependencies**:

   If you use pip
   ```
   python3 -m venv env
   source env/bin/activate
   pip install -r requirements.txt
   ```

   If you use pipenv
   ```
   pipenv install
   ```

3. **Database Migrations**:
   ```
   python manage.py migrate
   ```

4. **Run the Development Server**:
   ```
   python manage.py runserver
   ```

5. Open your browser and navigate to `http://127.0.0.1:8000/`.

## Usage:

1. **Vendor**:
   - Register as a vendor.
   - Login using vendor credentials.
   - Upload products.
   - View the status of uploaded products.

2. **Admin**:
   - Login using admin credentials.
   - View products awaiting approval.
   - Approve or reject products.
   - View all products.