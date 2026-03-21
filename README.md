# To-Do API (FastAPI)

## Giới thiệu

Đây là dự án To-Do API được xây dựng bằng FastAPI, phát triển theo từng cấp độ từ cơ bản đến nâng cao, bao gồm:

* CRUD
* Validation
* Authentication (JWT)
* Database (SQLAlchemy)
* Testing (pytest)
* Docker hóa ứng dụng

---

## Công nghệ sử dụng

* FastAPI
* Python 3.13
* SQLAlchemy
* JWT Authentication
* Passlib (hash password)
* Pytest + TestClient
* Docker & Docker Compose

---

## Cấu trúc thư mục

```
app/
├── core/
├── routers/
├── schemas/
├── services/
├── repositories/
├── models/
├── dependencies/
└── main.py

tests/
├── test_todos.py
├── test_auth.py
└── conftest.py

Dockerfile
docker-compose.yml
requirements.txt
README.md
```

---

## Cài đặt & chạy dự án

### 1. Clone project

```
git clone <repo_url>
cd project_folder
```

### 2. Tạo môi trường ảo

```
python -m venv venv
venv\Scripts\activate
```

### 3. Cài thư viện

```
pip install -r requirements.txt
```

### 4. Chạy server

```
uvicorn app.main:app --reload
```

Truy cập:

```
http://127.0.0.1:8000/docs
```

---

## Chạy bằng Docker

### 1. Mở Docker Desktop

### 2. Build và chạy

```
docker-compose up --build
```

---

## Chạy test

```
python -m pytest
```

Kết quả:

```
4 passed
```

---

## Authentication

### Register

```
POST /auth/register
```

### Login

```
POST /auth/login
```

### Lấy thông tin user

```
GET /auth/me
```

---

## API Endpoints

### Basic

* GET /
* GET /health

### To-Do

* POST /todos
* GET /todos
* GET /todos/{id}
* PATCH /todos/{id}
* DELETE /todos/{id}

---

## Tính năng nâng cao

* Filter: is_done=true/false
* Search: q=keyword
* Sort: created_at hoặc -created_at
* Pagination: limit, offset

---

## Tính năng bổ sung

* GET /todos/overdue
* GET /todos/today

---

## Kiến trúc

Dự án sử dụng mô hình phân tầng:

* Router: nhận request
* Service: xử lý logic
* Repository: thao tác database

---

## Bảo mật

* JWT Authentication
* Hash password bằng bcrypt
* Phân quyền theo user

---

## Testing

Sử dụng pytest và TestClient

Test các case:

* Tạo thành công
* Validation fail
* 404 not found
* Auth fail

---

## Các cấp độ đã hoàn thành

| Level | Nội dung            | Trạng thái |
| ----- | ------------------- | ---------- |
| 0     | Hello API           | Hoàn thành |
| 1     | CRUD RAM            | Hoàn thành |
| 2     | Validation + filter | Hoàn thành |
| 3     | Clean architecture  | Hoàn thành |
| 4     | Database + ORM      | Hoàn thành |
| 5     | Authentication      | Hoàn thành |
| 6     | Deadline + tags     | Hoàn thành |
| 7     | Testing + Docker    | Hoàn thành |
| 8     | Add features        | Hoàn thành |

---

## Lưu ý

* Có warning từ Pydantic v2 nhưng không ảnh hưởng chạy chương trình
* Có thể nâng cấp:

```
dict() -> model_dump()
```

---

## Hướng phát triển

* CI/CD
* Deploy lên server
* Viết test với JWT thật

---

## Kết luận

Dự án mô phỏng đầy đủ quy trình phát triển API backend từ cơ bản đến nâng cao, có thể dùng làm nền tảng học tập hoặc portfolio.
