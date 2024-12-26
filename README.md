# VAULTIFY-SERVER - Backend Server

<div>
    <img src="https://img.shields.io/badge/-Django-black?style=for-the-badge&logoColor=white&logo=django&color=092E20" alt="django" />
    <img src="https://img.shields.io/badge/-Python-black?style=for-the-badge&logoColor=white&logo=python&color=3776AB" alt="python" />
    <img src="https://img.shields.io/badge/-Appwrite-black?style=for-the-badge&logoColor=white&logo=appwrite&color=FD366E" alt="appwrite" />
</div>

---

## 📋 Table of Contents
- [🤖 Introduction](#-introduction)
- [⚙️ Tech Stack](#%EF%B8%8F-tech-stack)
- [🔋 Features](#-features)
- [🤸 Quick Start](#-quick-start)
- [🔗 API Endpoints](#-api-endpoints)
- [📂 Project Structure](#-project-structure)
- [🚀 More](#-more)

---

## 🤖 Introduction
This is the backend server for Horizon, a financial SaaS platform built with Django. It provides APIs for user authentication, bank account integration, transaction management, and fund transfers. The server also connects with external services like Appwrite, Plaid, and Dwolla for enhanced functionality.

---

## ⚙️ Tech Stack
- **Django** (REST Framework for API development)
- **Python**
- **Appwrite** (Authentication and Realtime Data)
- **Plaid** (Bank Account Integration)
- **Dwolla** (Fund Transfers)
- **PostgreSQL/MySQL** (Database)

---

## 🔋 Features
- **Secure Authentication:** Implements Appwrite for user management and secure access.
- **Bank Account Integration:** Uses Plaid API for linking multiple bank accounts.
- **Transaction Management:** Provides endpoints to view, filter, and paginate transactions.
- **Fund Transfers:** Integrates Dwolla API for sending and receiving funds securely.
- **Real-Time Updates:** Reflects changes dynamically using Appwrite.
- **Scalable Architecture:** Modular design ensures scalability and code reusability.

---

## 🤸 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/your-repo/horizon-backend.git
```

### 2. Navigate to the Project Directory
```bash
cd horizon-backend
```

### 3. Create a Virtual Environment
```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Configure Environment Variables
Create a `.env` file in the root directory with the following keys:
```env
APPWRITE_ENDPOINT=https://[APPWRITE-ENDPOINT]
APPWRITE_PROJECT_ID=[PROJECT_ID]
APPWRITE_API_KEY=[API_KEY]
PLAID_CLIENT_ID=[PLAID_CLIENT_ID]
PLAID_SECRET=[PLAID_SECRET]
DWOLLA_API_KEY=[DWOLLA_API_KEY]
DWOLLA_API_SECRET=[DWOLLA_API_SECRET]
DATABASE_URL=postgres://[USER]:[PASSWORD]@[HOST]:[PORT]/[DATABASE]
```

### 6. Run Database Migrations
```bash
python manage.py migrate
```

### 7. Start the Development Server
```bash
python manage.py runserver
```

### 8. Test the APIs
Access the API endpoints at `http://127.0.0.1:8000/api/`.

---

## 🔗 API Endpoints

### Authentication
- **POST /api/auth/register/**: Register a new user
- **POST /api/auth/login/**: Authenticate user and return a token

### Banks
- **GET /api/banks/**: Retrieve linked bank accounts
- **POST /api/banks/link/**: Link a new bank account

### Transactions
- **GET /api/transactions/**: View all transactions
- **GET /api/transactions/<bank_id>/**: View transactions for a specific bank

### Funds Transfer
- **POST /api/transfer/**: Transfer funds between accounts

---

## 📂 Project Structure
```
Horizon-Backend/
├── manage.py
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── apps/
│   ├── auth/
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── serializers.py
│   ├── transactions/
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── serializers.py
│   ├── banks/
│       ├── models.py
│       ├── views.py
│       ├── serializers.py
└── requirements.txt
```

---

## 🚀 More
- **Follow us on [YouTube](https://www.youtube.com/@jsmastery).**
- **Join our [Discord Community](https://discord.gg/jsmastery).**

---
