from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict

from contextlib import asynccontextmanager
from temporalio.client import Client
from workflowdomain.userflows.user_registration_worker import RegisterUserWorkflow
import asyncio


#Create a lifespan event for the app

@asynccontextmanager
async def lifespan(app: FastAPI):
    client = await Client.connect("localhost:7233")
    print(f"lifespan mods")
    app.temporal_client = client
    yield


#Mod the app with the new lifespan
app = FastAPI(lifespan=lifespan)
#app = FastAPI()


# Mock user database
users_db: Dict[int, Dict] = {}
next_user_id = 1

# Request model for registration
class UserRegistration(BaseModel):
    username: str
    useremail: str
    usermobile: str


async def workflow_userregistration():
    result= await app.temporal_client.execute_workflow(
        RegisterUserWorkflow.run, "user-reg-reg", id="user-registration-workflow", task_queue="user_registration_queue"
    )

    print(f"Result: {result}")

# API Endpoint for user registration
@app.post("/register", response_model=int)
def register_user(user: UserRegistration):
    global next_user_id
    users_db[next_user_id] = {
        "username": user.username,
        "useremail": user.useremail,
        "usermobile": user.usermobile,
        "activationstatus": 0  # Initially not activated
    }
    user_id = next_user_id
    next_user_id += 1
    print("user register workflow trigger")
    asyncio.run(workflow_userregistration())
    return user_id

# API Endpoint for activating a user
@app.post("/activate/{userid}", response_model=int)
def activate_user(userid: int):
    user = users_db.get(userid)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    user["activationstatus"] = 1  # Activate the user
    return 1  # Return activation status as 1 (activated)

