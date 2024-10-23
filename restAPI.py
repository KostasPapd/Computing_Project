# https://www.pythonanywhere.com/user/Kostas1/

from fastapi import FastAPI, HTTPException
from supabase import create_client, Client
import os

# Initialize FastAPI
app = FastAPI()

# Supabase URL and API Key (get these from your Supabase project)
SUPABASE_URL = os.getenv("SUPABASE_URL", "pvvduzraadbgtljdkmyg.supabase.co")
SUPABASE_API_KEY = os.getenv("SUPABASE_API_KEY", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InB2dmR1enJhYWRiZ3RsamRrbXlnIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTYxMTE5ODAsImV4cCI6MjAzMTY4Nzk4MH0.oIuwg-IgTGgKW_O90niT1tI8oWaRxtZpZt2Cj-mz4KI")

# Create a Supabase client
supabase: Client = create_client(SUPABASE_URL, SUPABASE_API_KEY)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Supabase API"}

# Define a route to get data from a Supabase table
@app.get("/get-data/{table_name}")
def get_data(table_name: str):
    try:
        # Query the table to get data
        response = supabase.table(table_name).select("*").execute()
        if response.status_code != 200:
            raise HTTPException(status_code=400, detail="Error fetching data")
        return {"data": response.data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Example: Fetch a specific item by ID
@app.get("/get-item/{table_name}/{item_id}")
def get_item(table_name: str, item_id: int):
    try:
        response = supabase.table(table_name).select("*").eq("id", item_id).execute()
        if response.status_code != 200:
            raise HTTPException(status_code=400, detail="Error fetching item")
        return {"item": response.data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))