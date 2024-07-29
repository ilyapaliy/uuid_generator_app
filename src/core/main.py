from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import routs

app = FastAPI(
	title="Get UUID",
	docs_url="/api/docs",
	openapi_url="/api/openapi.json",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:8000",
        "http://0.0.0.0:80",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(routs.router)

if __name__ == "__main__":
    uvicorn.run(
    	app="main:app",
    	host="127.0.0.1",
    	port=8000,
    	reload=True,
    	reload_excludes="*.log"
    )
