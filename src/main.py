from fastapi import FastAPI, Depends, Header, HTTPException, status
import uuid
import uvicorn
from typing import Optional, Annotated
from logger import logger
import producer

app = FastAPI(
	title="Get UUID",
	docs_url="/api/docs",
	openapi_url="/api/openapi.json",
)

def verify_x_flag(X_Flag: Annotated[str, Header()]):
	if X_Flag == "green" or X_Flag == "red":
		return(X_Flag)
	else:
		raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Invalid header X-Flag")
	return(X_Flag)

@app.get("/generate-uuid")
def get_uuid(x_flag: Annotated[str, Depends(verify_x_flag)]):
	random_uuid = str(uuid.uuid4())
	message = f"UUID: {random_uuid} - X-Flag: {x_flag}"
	if x_flag == "green":
		logger.info(message)
	if x_flag == "red":
		producer.send_message(message)

	return {"uuid": random_uuid}

if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True)
