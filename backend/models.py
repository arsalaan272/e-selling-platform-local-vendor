# in this file we are defining the schema of the database aka table with its columns.

from sqlmodel import SQLModel, Field;


# table=True tells SQLModel this should be a real database table
class User(SQLModel, table=True):

    #id: int | None = Field(...) This means the id must be an integer, or it can be None (which is Python's version of null). We allow it to be None initially because before a user is saved, they don't have an ID—the database generates the primary key for them upon saving.
    id: int | None = Field(default=None, primary_key=True);
    name: str = Field(..., max_length=100);
    #... literally means "This field is absolutely required.
    mobile: int = Field(..., unique=True, index=True, min_length=10, max_length=10);
    email: str = Field(..., unique=True, index=True, max_length=70);


# 'Field' acts as the bridge to pass those extra configurations down to the database. Think of it exactly like passing an options object in Mongoose, where you might write { type: String, unique: true, index: true }.

# 'index=True' This creates an index (a lookup table) in the database for this specific column. Because you will likely need to search for users by their mobile number frequently (like during a login process), this makes those searches lightning-fast.
