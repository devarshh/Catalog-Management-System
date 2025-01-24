# Catalog Management System

![License](https://img.shields.io/github/license/devarshh/Catalog-Management-System?style=flat-square)

## Overview

The **Catalog Management System** is a Python-based application designed to manage and organize product catalogs. This project simplifies tasks like adding, updating, and deleting products while providing an intuitive interface for users.

## Features

- **Product Management**:
  - Add, edit, and delete product details.
  - Store product metadata like name, description, price, and category.

- **User-Friendly Interface**:
  - Built-in frontend for seamless interactions.

- **Login Functionality**:
  - Basic authentication for secure access to the system.

- **CSV-Based Data Storage**:
  - All product data is stored in CSV files for simplicity and portability.

## Technology Stack

- **Programming Language**: Python
- **Frontend**: Custom Python-based GUI (Tkinter or similar)
- **Data Storage**: CSV files

## Prerequisites

Ensure the following tools are installed on your system:

- [Python 3.9+](https://www.python.org/downloads/)
- Required Python libraries (see Installation section)

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/devarshh/Catalog-Management-System.git
   cd Catalog-Management-System
   ```

2. **Set Up Environment**:
   - Create a virtual environment (optional but recommended):
     ```bash
     python -m venv venv
     source venv/bin/activate   # On Windows: venv\Scripts\activate
     ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**:
   - Start the backend:
     ```bash
     python backend.py
     ```
   - Launch the frontend:
     ```bash
     python frontend.py
     ```

5. **Optional**:
   - Use `main.py` to start both backend and frontend together.

## Usage

- **Login**:
  - Use the `login_frontend.py` to log in to the application.

- **Manage Products**:
  - Add, edit, or delete products from the catalog via the interface.

## Folder Structure

```plaintext
Catalog-Management-System/
├── backend.py          # Backend logic for product management
├── frontend.py         # Frontend interface for user interaction
├── login_frontend.py   # User authentication and login interface
├── main.py             # Entry point to integrate frontend and backend
├── requirements.txt    # Python dependencies
├── README.md           # Project documentation
├── catalog.csv               # Folder containing CSV files for data storage
```

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add a feature or fix"
   ```
4. Push your branch:
   ```bash
   git push origin feature/your-feature-name
   ```
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

## Contact

For questions or support, reach out to [Devarsh](https://github.com/devarshh).
