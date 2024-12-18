curl -X POST http://localhost:8000/api/projects \
-H "Content-Type: application/json" \
-d '{"name": "New Project", "description": "This is a new project", "teamId": 4, "ownerId": 1}'
