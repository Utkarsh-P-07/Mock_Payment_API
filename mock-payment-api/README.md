# ⚡ Mock Payment API  
A production-style Mock Payment Gateway built with **FastAPI**, **MongoDB**, and a clean Razorpay-inspired architecture.  
This project simulates order creation, payment processing, and status updates — ideal for learning backend architecture, testing payment flows, or integrating into demo apps.

---

## 🚀 Features

### ✅ Payment Gateway Features
- Create payment orders  
- Update payment status (created → processing → success/failed)  
- Generate unique order IDs  
- Store transactions in MongoDB  
- Razorpay-style flow without real payments  

### ✅ User Module
- Register users  
- Fetch user list  
- Auto timestamps  

### ✅ Modern FastAPI Structure
- Controllers (business logic)  
- Routes (API layer)  
- Models (data models)  
- Schemas (response serializers)  
- Utils (common helpers)  
- Config (DB connection)  

### ⚙ Tech Stack
- **FastAPI** (Backend)
- **MongoDB** (Database)
- **Uvicorn** (Server)
- **Pydantic** (Validation)
- **Python 3.10+**

---

## 📁 Project Structure

Mock_Payment_API/
│
├── app/
│ ├── main.py
│ ├── config/
│ │ └── database.py
│ ├── models/
│ │ ├── user.py
│ │ └── payment.py
│ ├── schemas/
│ │ ├── user_schema.py
│ │ └── payment_schema.py
│ ├── controllers/
│ │ ├── user_controller.py
│ │ └── payment_controller.py
│ ├── routes/
│ │ ├── user_routes.py
│ │ └── payment_routes.py
│ └── utils/
│ └── helpers.py
│
├── .gitignore
├── README.md
└── requirements.txt

---

## 🔧 Installation & Setup

### 1️⃣ Clone the repository
```sh
git clone https://github.com/your-username/Mock_Payment_API.git
cd Mock_Payment_API

## Create a Vertual Enviroment
python -m venv venv

## Activate it

# Windows:
venv\Scripts\activate

# Mac/Linux:
source venv/bin/activate

## Install Depndencies
pip install -r requirements.txt

## Run the FastAPI Server
uvicorn app.main:app --reload

---

🧱 Folder-Level Explanation
controllers/

Business logic (similar to service layer in MVC).

routes/

API endpoint definitions.

models/

Pydantic models representing data.

schemas/

MongoDB → Pydantic → JSON serializers.

config/

Database connection.

utils/

Helper functions, responses, utilities.