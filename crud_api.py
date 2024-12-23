from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict

# Define a Pydantic model for a simple user
class User(BaseModel):
    username: str
    email: str
    age: int

# Initialize FastAPI app
app = FastAPI()

# In-memory storage for users
users: Dict[str, User] = {}

@app.get("/users/{username}", response_model=User)
def get_user(username: str):
    """Retrieve a user by their username."""
    user = users.get(username)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.post("/users", response_model=User)
def create_user(user: User):
    """Create a new user."""
    if user.username in users:
        raise HTTPException(status_code=400, detail="Username already exists")
    users[user.username] = user
    return user

@app.put("/users/{username}", response_model=User)
def update_user(username: str, updated_user: User):
    """Update an existing user."""
    if username not in users:
        raise HTTPException(status_code=404, detail="User not found")
    users[username] = updated_user
    return updated_user

@app.delete("/users/{username}")
def delete_user(username: str):
    """Delete a user by their username."""
    if username not in users:
        raise HTTPException(status_code=404, detail="User not found")
    del users[username]
    return {"detail": "User deleted successfully"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
