curl -X PUT http://localhost:8000/api/roles/1 \
-H "Content-Type: application/json" \
-d '{"name": "Updated Role", "description": "Updated description"}'
