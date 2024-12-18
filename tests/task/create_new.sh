curl -X POST http://localhost:8000/api/tasks \
-H "Content-Type: application/json" \
-d '{"title": "New Task", "description": "Task description", "status": "PENDING", "projectId": 1}'
