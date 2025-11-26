## Mock Razorpay Payment API (FastAPI + MongoDB)

This is a simple mock of key Razorpay payment flows built with **FastAPI** and **MongoDB**, designed to be run and tested locally (Windows friendly, VS Code + Postman).

### Tech stack
- **Backend**: FastAPI
- **Database**: MongoDB (local or Atlas)
- **Async driver**: `motor`
- **Server**: `uvicorn`

---

### 1. Setup (Windows + VS Code)

1. Open the project in VS Code:
   - Folder: `mock-payment-api`

2. (Recommended) Create and activate a virtual env in PowerShell:
   ```powershell
   cd mock-payment-api
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   ```

3. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```

4. Start MongoDB:
   - Local MongoDB running on `mongodb://localhost:27017`
   - Or use MongoDB Atlas and update the URI.

5. (Optional) Create a `.env` file in `mock-payment-api`:
   ```env
   MONGO_URI=mongodb://localhost:27017
   MONGO_DB_NAME=mock_payment_api
   ```

---

### 2. Run the API

From inside `mock-payment-api`:

```powershell
uvicorn app.main:app --reload
```

The API will be available at:
- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

---

### 3. Core flows (Razorpay style)

#### a) Create User
- **Method**: `POST /api/users`
- **Body (JSON)**:
  ```json
  {
    "name": "Test User",
    "email": "test@example.com",
    "contact": "+911234567890"
  }
  ```

#### b) Create Order (like Razorpay `orders.create`)
- **Method**: `POST /api/orders`
- **Body (JSON)**:
  ```json
  {
    "amount": 50000,
    "currency": "INR",
    "receipt": "rcpt_11",
    "user_id": "USER_ID_FROM_CREATE_USER"
  }
  ```

#### c) Capture Payment (like Razorpay `payments.capture`)
- **Method**: `POST /api/payments/capture`
- **Body (JSON)**:
  ```json
  {
    "order_id": "ORDER_ID_FROM_CREATE_ORDER",
    "amount": 50000,
    "currency": "INR"
  }
  ```

- On success:
  - A payment document is stored in `payments`.
  - The related order status is updated to `paid`.

#### d) List Orders / Payments
- `GET /api/orders`
- `GET /api/payments`

#### e) Health check
- `GET /health`

---

### 4. Postman usage

1. Start the server with `uvicorn`.
2. In Postman, create a new collection "Mock Razorpay API".
3. Add requests:
   - `POST http://127.0.0.1:8000/api/users`
   - `POST http://127.0.0.1:8000/api/orders`
   - `POST http://127.0.0.1:8000/api/payments/capture`
   - `GET http://127.0.0.1:8000/api/orders`
   - `GET http://127.0.0.1:8000/api/payments`
4. Inspect created data using MongoDB Compass or `mongosh`.

This gives you a complete local mock of basic Razorpay-like flows suitable for learning, demos, and integration testing.


