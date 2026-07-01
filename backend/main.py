from fastapi import FastAPI;
from fastapi.middleware.cors import CORSMiddleware;
from dotenv import load_dotenv;
from sqlmodel import SQLModel, Session;
from contextlib import asynccontextmanager;
from database import engine, get_session;
from models import User;
import os;


# defining the connection to the database before the app=FastAPI instance.

# the lifespan fn. runs the moment the server starts up.
@asynccontextmanager    
async def lifespan(app: FastAPI):
    # here is the code to create models (table) in the databaseconnectionDetails.db file.
    SQLModel.metadata.create_all(engine);
    yield; # this is where the app runs, and when the app shuts down, the code after this line will run.

app = FastAPI(title="E-Commerce", lifespan=lifespan);

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["GET,POST,DELETE,PUT"],
    allow_headers=["*"],
);

load_dotenv();

@app.get("/")
def root():
    return {"message": "Welcome to the E-Commerce API!"}; 

@app.post("/users/")
def create_user(user: User, session: Session = Depends(get_session())):
    session.add(user);
    session.commit();
    session.refersh(user);
    return {"message":"User created successfully!"};
