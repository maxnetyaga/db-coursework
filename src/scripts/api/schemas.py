from pydantic import BaseModel
from typing import Optional
import datetime

# User Schemas
class _UserBase(BaseModel):
    username: str
    email: str
    roleId: int

class UserCreate(_UserBase):
    password: str

class UserResponse(_UserBase):
    id: int

# Role Schemas
class _RoleBase(BaseModel):
    name: str
    description: Optional[str] = None

class RoleCreate(_RoleBase):
    pass

class RoleResponse(_RoleBase):
    id: int

# Team Schemas
class _TeamBase(BaseModel):
    pass

class TeamCreate(_TeamBase):
    pass

class TeamResponse(_TeamBase):
    id: int
    createdAt: datetime.datetime

# Project Schemas
class _ProjectBase(BaseModel):
    name: str
    description: Optional[str] = None
    ownerId: int
    teamId: int

class ProjectCreate(_ProjectBase):
    pass

class ProjectResponse(_ProjectBase):
    id: int

# Task Schemas
class _TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    status: str
    projectId: int
    assignedTo: Optional[int] = None

class TaskCreate(_TaskBase):
    pass

class TaskResponse(_TaskBase):
    id: int

class TaskStatus(_TaskBase):
    status: str
