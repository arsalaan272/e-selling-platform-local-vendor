from sqlmodel import create_engine, Session


# creating a file named 'databaseConnectionDetails.db' to store the database connection details
sqlite_file_name = "databaseConnectionDetails.db";
sqlite_url = f"sqlite:///{sqlite_file_name}";

# creating the database engine to handle database connections.
engine = create_engine(sqlite_url, echo=True);

# creating a dependency fn to manage database connection to your routes.
def get_session():
    with Session(engine) as session:
        yield session;