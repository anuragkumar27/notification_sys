
# 📢 Notification Service API

A simple notification service built with **Python Flask** and **SQLite** to send and retrieve user notifications. It supports Email, SMS, and In-App notification types.

---

## 🚀 Features

- Send notifications (`POST /notifications`)
- Retrieve user notifications (`GET /users/<user_id>/notifications`)
- Supports `email`, `sms`, and `in-app` types
- Uses SQLite (via SQLAlchemy) for data persistence
- Simple HTML template for the homepage (optional)

---

## 📁 Project Structure

```
.
├── app.py
├── models.py
├── templates/
│   └── index.html
├── notifications.db
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/notification-service.git
cd notification-service
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If you don't have a `requirements.txt`, here’s what to include:

```txt
Flask
Flask-SQLAlchemy
```

You can create it using:

```bash
pip freeze > requirements.txt
```

### 4. Run the App

```bash
python app.py
```

The app will start on `http://127.0.0.1:5000/`.

---

## 🧪 API Endpoints

### 1. **Send a Notification**
```
POST /notifications
```

**Request Body (JSON):**
```json
{
  "user_id": 1,
  "message": "Your order has been shipped.",
  "type": "email"  // or "sms" or "in-app"
}
```

**Response:**
```json
{
  "notification_id": 5,
  "status": "sent"
}
```

---

### 2. **Get User Notifications**
```
GET /users/<user_id>/notifications
```

**Optional Query Params:**
- `limit` (default: 10)
- `offset` (default: 0)

**Response:**
```json
{
  "notifications": [
    {
      "id": 1,
      "message": "Welcome to the app!",
      "type": "in-app",
      "status": "sent",
      "created_at": "2024-05-17T10:30:00"
    }
  ]
}
```

---

## ✅ Assumptions

- No actual email/SMS is sent — this is a mock implementation.
- In-App notifications are stored in the database and retrievable via API.
- SQLite is used for simplicity; it can be swapped with MySQL/PostgreSQL.

---

## 📄 Bonus Features (not included)
You can extend the project with:
- Background processing with a queue (e.g., RabbitMQ, Celery)
- Retry logic for failed deliveries
- Deployed backend (e.g., on Render or Heroku)
- API documentation (e.g., Swagger UI)

---

## 📬 Contact

Made with ❤️ by [Your Name]
