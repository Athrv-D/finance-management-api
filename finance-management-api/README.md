#  Finance Management API

A backend system built using FastAPI to manage financial records with secure authentication, role-based access control, and analytical dashboard insights.

---

##   Features

### 🔐 Authentication & Security
- User Registration & Login (JWT आधारित authentication)
- Password hashing using bcrypt
- Token-based authorization (Bearer token)

---

### 👥 Role-Based Access Control

| Role     | Permissions |
|----------|------------|
| Admin    | Full control (users + records) |
| Analyst  | Manage & view financial records |
| Viewer   | View dashboard only |

- Only one Admin allowed initially
- Admin can create users
- Inactive users are restricted from access

---

### 👤 User Management
- Create user (Admin only)
- View all users
- Activate / Deactivate users
- Prevent duplicate user registration

---

### 📊 Financial Records (CRUD)

- ➕ Add record (income / expense)
- 📋 View records
- ✏️ Update record
- ❌ Delete record
- 🔍 Filter records by:
  - Type (income / expense)
  - Category
  - Date (optional)

---

### 📈 Dashboard Analytics

- Total Income
- Total Expense
- Net Balance
- Category-wise totals
- Monthly trend analysis

---

## 🧠 Advanced Features

- Enum validation (income / expense only)
- Input validation (amount > 0, email format)
- Role-based route protection
- Clean API documentation using Swagger

---

## 🛠 Tech Stack

- **Framework:** FastAPI  
- **Database:** SQLite  
- **ORM:** SQLAlchemy  
- **Authentication:** JWT (python-jose)  
- **Password Hashing:** passlib (bcrypt)  

---

## 📂 Project Structure

app/
│
├── api/ # Routes
│ ├── auth_routes.py
│ ├── users.py
│ ├── record_routes.py
│
├── models/ # DB Models
├── schemas/ # Pydantic Schemas
├── services/ # Business Logic
├── core/ # Security & Config
├── db/ # Database setup


---

## ▶️ How to Run

```bash
# Install dependencies
pip install -r requirements.txt

# Run server
uvicorn app.main:app --reload

---

### 📌 API Documentation

After running server:

http://127.0.0.1:8000/docs

Use Swagger UI to:

- Register
- Login
- Authorize (Bearer Token)
- Test APIs

---

### ⚠️ Important Notes

1.Only first registered user becomes Admin
2.All passwords are securely hashed
3.Duplicate users are not allowed


### 🔑Authentication Flow

1.Register user
2.Login → get JWT token
3.Click Authorize in Swagger
4.Paste token
5.Access protected routes


📈 Example Use Case -

Track income and expenses
Analyze spending patterns
Monitor monthly trends
Manage users in organization


 ## Author
 
 Atharv Gupta