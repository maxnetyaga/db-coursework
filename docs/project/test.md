# Тестування працездатності системи

## Основні сценарії для проєктів

```sh
=== tests/project/create_new.sh ===
curl -X POST http://localhost:8000/api/projects \
-H "Content-Type: application/json" \
-d '{"name": "New Project", "description": "This is a new project", "teamId": 4, "ownerId": 1}'
=== End of tests/project/create_new.sh ===
### tests/project/create_new.sh result:
{"name":"New Project","description":"This is a new project","ownerId":1,"teamId":4,"id":4}

=== tests/project/get_all.sh ===
curl -X GET http://localhost:8000/api/projects -H "Content-Type: application/json"
=== End of tests/project/get_all.sh ===
### tests/project/get_all.sh result:
[{"name":"Project A","description":"Description for Project A","ownerId":1,"teamId":1,"id":1},{"name":"Project B","description":"Description for Project B","ownerId":3,"teamId":2,"id":2},{"name":"Project C","description":"Description for Project C","ownerId":1,"teamId":3,"id":3},{"name":"New Project","description":"This is a new project","ownerId":1,"teamId":4,"id":4}]

=== tests/project/get_by_id.sh ===
curl -X GET http://localhost:8000/api/projects/1 -H "Content-Type: application/json"
=== End of tests/project/get_by_id.sh ===
### tests/project/get_by_id.sh result:
{"name":"Project A","description":"Description for Project A","ownerId":1,"teamId":1,"id":1}

=== tests/project/update_by_id.sh ===
curl -X PUT http://localhost:8000/api/projects/1 \
-H "Content-Type: application/json" \
-d '{"name": "Updated Project", "description": "Updated description"}'
=== End of tests/project/update_by_id.sh ===
### tests/project/update_by_id.sh result:
{"detail":[{"type":"missing","loc":["body","ownerId"],"msg":"Field required","input":{"name":"Updated Project","description":"Updated description"}},{"type":"missing","loc":["body","teamId"],"msg":"Field required","input":{"name":"Updated Project","description":"Updated description"}}]}
```

## Основні сценарії для ролей

```sh
=== tests/role/create_new.sh ===
curl -X POST http://localhost:8000/api/roles \
-H "Content-Type: application/json" \
-d '{"name": "New Role", "description": "Role description"}'
=== End of tests/role/create_new.sh ===
### tests/role/create_new.sh result:
{"detail":[{"type":"missing","loc":["body","id"],"msg":"Field required","input":{"name":"New Role","description":"Role description"}}]}

=== tests/role/delete_by_id.sh ===
curl -X DELETE http://localhost:8000/api/roles/4 -H "Content-Type: application/json"
=== End of tests/role/delete_by_id.sh ===
### tests/role/delete_by_id.sh result:
{"message":"Role deleted"}

=== tests/role/get_all.sh ===
curl -X GET http://localhost:8000/api/roles -H "Content-Type: application/json"
=== End of tests/role/get_all.sh ===
### tests/role/get_all.sh result:
[{"name":"Admin","description":null,"id":1},{"name":"Developer","description":null,"id":2},{"name":"Manager","description":null,"id":3}]

=== tests/role/get_by_id.sh ===
curl -X GET http://localhost:8000/api/roles/1 -H "Content-Type: application/json"
=== End of tests/role/get_by_id.sh ===
### tests/role/get_by_id.sh result:
{"name":"Admin","description":null,"id":1}

=== tests/role/update_by_id.sh ===
curl -X PUT http://localhost:8000/api/roles/1 \
-H "Content-Type: application/json" \
-d '{"name": "Updated Role", "description": "Updated description"}'
=== End of tests/role/update_by_id.sh ===
### tests/role/update_by_id.sh result:
{"name":"Updated Role","description":"Updated description","id":1}
```

## Основні сценарії для завдань

```sh
=== tests/task/assign.sh ===
curl -X PATCH http://localhost:8000/api/tasks/1/assign/2 \
-H "Content-Type: application/json"
=== End of tests/task/assign.sh ===
### tests/task/assign.sh result:
{"title":"Task 1 for Project A","assignedTo":2,"description":"Task 1 description","status":"PENDING","dueDate":"2024-11-20T10:00:00","id":1,"projectId":1,"priority":"HIGH","createdAt":"2024-12-18T22:44:57"}

=== tests/task/create_new.sh ===
curl -X POST http://localhost:8000/api/tasks \
-H "Content-Type: application/json" \
-d '{"title": "New Task", "description": "Task description", "status": "PENDING", "projectId": 1}'
=== End of tests/task/create_new.sh ===
### tests/task/create_new.sh result:
{"title":"New Task","description":"Task description","status":"PENDING","projectId":1,"assignedTo":null,"id":5}

=== tests/task/get_by_id.sh ===
curl -X GET http://localhost:8000/api/tasks/1 -H "Content-Type: application/json"
=== End of tests/task/get_by_id.sh ===
### tests/task/get_by_id.sh result:
{"title":"Task 1 for Project A","description":"Task 1 description","status":"PENDING","projectId":1,"assignedTo":2,"id":1}

=== tests/task/get_by_project_id.sh ===
curl -X GET http://localhost:8000/api/tasks/projects/1 -H "Content-Type: application/json"
=== End of tests/task/get_by_project_id.sh ===
### tests/task/get_by_project_id.sh result:
[{"title":"Task 1 for Project A","description":"Task 1 description","status":"PENDING","projectId":1,"assignedTo":2,"id":1},{"title":"Task 2 for Project A","description":"Task 2 description","status":"IN_PROGRESS","projectId":1,"assignedTo":3,"id":2},{"title":"New Task","description":"Task description","status":"PENDING","projectId":1,"assignedTo":null,"id":5}]

=== tests/task/get_by_user_id.sh ===
curl -X GET http://localhost:8000/api/tasks/user/2 -H "Content-Type: application/json"
=== End of tests/task/get_by_user_id.sh ===
### tests/task/get_by_user_id.sh result:
[{"title":"Task 1 for Project A","description":"Task 1 description","status":"PENDING","projectId":1,"assignedTo":2,"id":1},{"title":"Task 1 for Project C","description":"Task 1 description","status":"COMPLETED","projectId":3,"assignedTo":2,"id":4}]

=== tests/task/update_status.sh ===
curl -X PATCH http://localhost:8000/api/tasks/1/status \
-H "Content-Type: application/json" \
-d '{"status": "IN_PROGRESS"}'
=== End of tests/task/update_status.sh ===
### tests/task/update_status.sh result:
{"detail":[{"type":"missing","loc":["body","title"],"msg":"Field required","input":{"status":"IN_PROGRESS"}},{"type":"missing","loc":["body","projectId"],"msg":"Field required","input":{"status":"IN_PROGRESS"}}]}
```

## Основні сценарії для команд

```sh
=== tests/team/create_new.sh ===
curl -X POST http://localhost:8000/api/teams \
-H "Content-Type: application/json" \
-d '{"name": "New Team", "description": "This is a new team"}'
=== End of tests/team/create_new.sh ===
### tests/team/create_new.sh result:
{"id":5,"createdAt":"2024-12-19T00:42:33"}

=== tests/team/delete_by_id.sh ===
curl -X DELETE http://localhost:8000/api/teams/5 -H "Content-Type: application/json"
=== End of tests/team/delete_by_id.sh ===
### tests/team/delete_by_id.sh result:
{"message":"Team deleted"}

=== tests/team/get_all.sh ===
curl -X GET http://localhost:8000/api/teams -H "Content-Type: application/json"
=== End of tests/team/get_all.sh ===
### tests/team/get_all.sh result:
[{"id":1,"createdAt":"2024-12-18T22:44:57"},{"id":2,"createdAt":"2024-12-18T22:44:57"},{"id":3,"createdAt":"2024-12-18T22:44:57"},{"id":4,"createdAt":"2024-12-18T22:44:57"}]

=== tests/team/get_by_id.sh ===
curl -X GET http://localhost:8000/api/teams/1 -H "Content-Type: application/json"
=== End of tests/team/get_by_id.sh ===
### tests/team/get_by_id.sh result:
{"id":1,"createdAt":"2024-12-18T22:44:57"}
```

## Основні сценарії для користувачів

```sh
=== tests/user/create_new.sh ===
curl -X POST http://localhost:8000/api/users \
-H "Content-Type: application/json" \
-d '{"username": "new_user", "email": "new_user@example.com", "password": "securepassword", "roleId": "1"}'
=== End of tests/user/create_new.sh ===
### tests/user/create_new.sh result:
{"username":"new_user","email":"new_user@example.com","roleId":1,"id":5}

=== tests/user/get_all.sh ===
curl -X GET http://localhost:8000/api/users -H "Content-Type: application/json"
=== End of tests/user/get_all.sh ===
### tests/user/get_all.sh result:
[{"username":"john_doe","email":"john.doe@example.com","roleId":1,"id":1},{"username":"jane_smith","email":"jane.smith@example.com","roleId":2,"id":2},{"username":"alex_williams","email":"alex.williams@example.com","roleId":3,"id":3},{"username":"michael_brown","email":"michael.brown@example.com","roleId":2,"id":4},{"username":"new_user","email":"new_user@example.com","roleId":1,"id":5}]

=== tests/user/get_by_id.sh ===
curl -X GET http://localhost:8000/api/users/1 -H "Content-Type: application/json"
=== End of tests/user/get_by_id.sh ===
### tests/user/get_by_id.sh result:
{"username":"john_doe","email":"john.doe@example.com","roleId":1,"id":1}
```
