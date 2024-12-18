curl -X POST http://localhost:8000/api/users \
-H "Content-Type: application/json" \
-d '{"username": "new_user", "email": "new_user@example.com", "password": "securepassword", "roleId": "1"}'
