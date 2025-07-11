from fastapi import FastAPI
from pydantic import BaseModel
from query_generator import generate_sql_query, execute_query

#Initialize FastAPI app
app = FastAPI()

class QueryRequest(BaseModel):
    query:str

@app.post("/generate_sql")
async def generate_sql(request: QueryRequest):
    """Generate SQL query from natural language input."""
    sql_query = generate_sql_query(request.query)
    if not sql_query:
        return {"error": "Failed to generate SQL"}
    return {"sql query": sql_query}

@app.post("/execute_sql/")
async def execute_sql(request: QueryRequest):
    """Execute a given SQL query and return results."""
    sql_query = request.query
    results = execute_query(sql_query)
    if results is None:
        return {"error": "Error executing query"}
    return {"results ": results["results"], "optimization_tips":results["optimization_tips"]}

#Run the FASTAPI app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)