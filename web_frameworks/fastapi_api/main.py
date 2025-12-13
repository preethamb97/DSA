"""
FastAPI REST API - Modern Python async web framework
Complete CRUD API with JWT Authentication and async/await
"""

from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
from typing import List, Optional
import jwt
from datetime import datetime, timedelta
from passlib.context import CryptContext
import asyncio

app = FastAPI(title="Todo API", version="1.0.0")
security = HTTPBearer()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Configuration
SECRET_KEY = "your-secret-key-here"  # Use environment variable in production
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# In-memory storage (use database in production)
users_db = {}
todos_db = {}
todo_id_counter = 0


# Pydantic models
class UserRegister(BaseModel):
    username: str
    password: str


class UserLogin(BaseModel):
    username: str
    password: str


class TodoCreate(BaseModel):
    title: str
    description: Optional[str] = ""


class TodoUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None


class Todo(BaseModel):
    id: int
    title: str
    description: str
    completed: bool
    user: str
    created_at: str


# Helper functions
def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify password against hash"""
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    """Hash password"""
    return pwd_context.hash(password)


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    """Create JWT token"""
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """Dependency to get current authenticated user"""
    token = credentials.credentials
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid authentication credentials"
            )
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token has expired"
        )
    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
        )
    return username


# Routes
@app.post("/api/register", status_code=status.HTTP_201_CREATED)
async def register(user: UserRegister):
    """User registration"""
    if user.username in users_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already registered"
        )
    
    users_db[user.username] = {
        "password": get_password_hash(user.password),
        "created_at": datetime.utcnow().isoformat()
    }
    
    return {"message": "User registered successfully"}


@app.post("/api/login")
async def login(user: UserLogin):
    """User login - returns JWT token"""
    db_user = users_db.get(user.username)
    
    if not db_user or not verify_password(user.password, db_user["password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password"
        )
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    
    return {"access_token": access_token, "token_type": "bearer"}


@app.get("/api/todos", response_model=List[Todo])
async def get_todos(current_user: str = Depends(get_current_user)):
    """Get all todos for current user"""
    user_todos = [
        Todo(**todo) for todo in todos_db.values() 
        if todo["user"] == current_user
    ]
    return user_todos


@app.post("/api/todos", response_model=Todo, status_code=status.HTTP_201_CREATED)
async def create_todo(
    todo: TodoCreate,
    current_user: str = Depends(get_current_user)
):
    """Create a new todo"""
    global todo_id_counter
    
    todo_id_counter += 1
    new_todo = {
        "id": todo_id_counter,
        "title": todo.title,
        "description": todo.description,
        "completed": False,
        "user": current_user,
        "created_at": datetime.utcnow().isoformat()
    }
    
    todos_db[todo_id_counter] = new_todo
    return Todo(**new_todo)


@app.get("/api/todos/{todo_id}", response_model=Todo)
async def get_todo(
    todo_id: int,
    current_user: str = Depends(get_current_user)
):
    """Get a specific todo"""
    todo = todos_db.get(todo_id)
    
    if not todo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Todo not found"
        )
    
    if todo["user"] != current_user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not enough permissions"
        )
    
    return Todo(**todo)


@app.put("/api/todos/{todo_id}", response_model=Todo)
async def update_todo(
    todo_id: int,
    todo_update: TodoUpdate,
    current_user: str = Depends(get_current_user)
):
    """Update a todo"""
    todo = todos_db.get(todo_id)
    
    if not todo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Todo not found"
        )
    
    if todo["user"] != current_user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not enough permissions"
        )
    
    if todo_update.title is not None:
        todo["title"] = todo_update.title
    if todo_update.description is not None:
        todo["description"] = todo_update.description
    if todo_update.completed is not None:
        todo["completed"] = todo_update.completed
    
    return Todo(**todo)


@app.delete("/api/todos/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(
    todo_id: int,
    current_user: str = Depends(get_current_user)
):
    """Delete a todo"""
    todo = todos_db.get(todo_id)
    
    if not todo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Todo not found"
        )
    
    if todo["user"] != current_user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not enough permissions"
        )
    
    del todos_db[todo_id]
    return None


@app.get("/api/health")
async def health():
    """Health check endpoint"""
    return {"status": "healthy", "timestamp": datetime.utcnow().isoformat()}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

