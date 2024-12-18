from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db, Base, engine
import schemas as s
import crud

app = FastAPI()

Base.metadata.create_all(bind=engine)

# Users
@app.get("/api/users", response_model=list[s.UserResponse])
def read_users(db: Session = Depends(get_db)):
    return crud.get_users(db)

@app.get("/api/users/{user_id}", response_model=s.UserResponse)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.post("/api/users", response_model=s.UserResponse)
def create_user(user: s.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)

# Roles
@app.get("/api/roles", response_model=list[s.RoleResponse])
def read_roles(db: Session = Depends(get_db)):
    return crud.get_roles(db)

@app.get("/api/roles/{role_id}", response_model=s.RoleResponse)
def read_role(role_id: int, db: Session = Depends(get_db)):
    role = crud.get_role_by_id(db, role_id)
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")
    return role

@app.post("/api/roles", response_model=s.RoleResponse)
def create_role(role: s.RoleResponse, db: Session = Depends(get_db)):
    return crud.create_role(db, role)

@app.put("/api/roles/{role_id}", response_model=s.RoleResponse)
def update_role(role_id: int, role: s.RoleCreate, db: Session = Depends(get_db)):
    updated_role = crud.update_role(db, role_id, role)
    if not updated_role:
        raise HTTPException(status_code=404, detail="Role not found")
    return updated_role

@app.delete("/api/roles/{role_id}")
def delete_role(role_id: int, db: Session = Depends(get_db)):
    deleted_role = crud.delete_role(db, role_id)
    if not deleted_role:
        raise HTTPException(status_code=404, detail="Role not found")
    return {"message": "Role deleted"}

# Teams
@app.get("/api/teams", response_model=list[s.TeamResponse])
def read_teams(db: Session = Depends(get_db)):
    return crud.get_teams(db)

@app.get("/api/teams/{team_id}", response_model=s.TeamResponse)
def read_team(team_id: int, db: Session = Depends(get_db)):
    team = crud.get_team_by_id(db, team_id)
    if not team:
        raise HTTPException(status_code=404, detail="Team not found")
    return team

@app.post("/api/teams", response_model=s.TeamResponse)
def create_team(team: s.TeamCreate, db: Session = Depends(get_db)):
    return crud.create_team(db, team)

@app.delete("/api/teams/{team_id}")
def delete_team(team_id: int, db: Session = Depends(get_db)):
    deleted_team = crud.delete_team(db, team_id)
    if not deleted_team:
        raise HTTPException(status_code=404, detail="Team not found")
    return {"message": "Team deleted"}

# Projects
@app.get("/api/projects", response_model=list[s.ProjectResponse])
def read_projects(db: Session = Depends(get_db)):
    return crud.get_projects(db)

@app.get("/api/projects/{project_id}", response_model=s.ProjectResponse)
def read_project(project_id: int, db: Session = Depends(get_db)):
    project = crud.get_project_by_id(db, project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project

@app.post("/api/projects", response_model=s.ProjectResponse)
def create_project(project: s.ProjectCreate, db: Session = Depends(get_db)):
    return crud.create_project(db, project)

@app.put("/api/projects/{project_id}", response_model=s.ProjectResponse)
def update_project(project_id: int, project: s.ProjectCreate, db: Session = Depends(get_db)):
    updated_project = crud.update_project(db, project_id, project)
    if not updated_project:
        raise HTTPException(status_code=404, detail="Project not found")
    return updated_project

# Tasks
@app.get("/api/tasks/{task_id}", response_model=s.TaskResponse)
def read_task(task_id: int, db: Session = Depends(get_db)):
    task = crud.get_task_by_id(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.get("/api/tasks/projects/{project_id}", response_model=list[s.TaskResponse])
def read_tasks_by_project(project_id: int, db: Session = Depends(get_db)):
    return crud.get_tasks_by_project(db, project_id)

@app.get("/api/tasks/user/{user_id}", response_model=list[s.TaskResponse])
def read_tasks_by_user(user_id: int, db: Session = Depends(get_db)):
    return crud.get_tasks_by_user(db, user_id)

@app.post("/api/tasks", response_model=s.TaskResponse)
def create_task(task: s.TaskCreate, db: Session = Depends(get_db)):
    return crud.create_task(db, task)

@app.patch("/api/tasks/{task_id}/status")
def update_task_status(task_id: int, status: s.TaskStatus, db: Session = Depends(get_db)):
    updated_task = crud.update_task_status(db, task_id, status)
    if not updated_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated_task

@app.patch("/api/tasks/{task_id}/assign/{user_id}")
def assign_task(task_id: int, user_id: int, db: Session = Depends(get_db)):
    updated_task = crud.assign_task(db, task_id, user_id)
    if not updated_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated_task
