from sqlalchemy import Column, Integer, String, Enum, ForeignKey, DateTime, Text
from database import Base
from datetime import datetime

class User(Base):
    __tablename__ = "User"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(45), nullable=False)
    email = Column(String(45), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    roleId = Column(Integer, ForeignKey("Role.id"), nullable=False)
    status = Column(Enum("ACTIVE", "BANNED"), default="ACTIVE")
    createdAt = Column(DateTime, default=datetime.now())

class Role(Base):
    __tablename__ = "Role"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(45), unique=True, nullable=False)

class Team(Base):
    __tablename__ = "Team"
    id = Column(Integer, primary_key=True, index=True)
    createdAt = Column(DateTime, default=datetime.now())

class Project(Base):
    __tablename__ = "Project"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)
    description = Column(Text)
    ownerId = Column(Integer, ForeignKey("User.id"), nullable=False)
    teamId = Column(Integer, ForeignKey("Team.id"), nullable=False)
    createdAt = Column(DateTime, default=datetime.now())

class Task(Base):
    __tablename__ = "Task"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    description = Column(Text)
    assignedTo = Column(Integer, ForeignKey("User.id"))
    projectId = Column(Integer, ForeignKey("Project.id"), nullable=False)
    status = Column(Enum("PENDING", "IN_PROGRESS", "COMPLETED", "ON_HOLD", "CANCELLED"), default="PENDING")
    priority = Column(Enum("LOW", "MEDIUM", "HIGH"), default="MEDIUM")
    dueDate = Column(DateTime)
    createdAt = Column(DateTime, default=datetime.now())
