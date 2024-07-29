from fastapi import APIRouter, Depends
import uuid
from logger import logger
import producer
from schemas import XFlag
from dependencies import verify_x_flag


router = APIRouter(
    prefix="/generate-uuid"
)


@router.get("/")
def get_uuid(x_flag: XFlag = Depends(verify_x_flag)):
	random_uuid = str(uuid.uuid4())
	message = f"UUID: {random_uuid} - X-Flag: {x_flag}"
	if x_flag == XFlag.green:
		logger.info(message)
	if x_flag == XFlag.red:
		producer.send_message(message)

	return {"uuid": random_uuid}
