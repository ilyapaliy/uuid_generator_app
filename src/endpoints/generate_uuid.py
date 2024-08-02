from fastapi import APIRouter, Depends, Request
import uuid
from schemas import XFlag
from dependencies import verify_x_flag
import logging

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/generate-uuid"
)


@router.get("/")
async def get_uuid(request: Request, x_flag: XFlag = Depends(verify_x_flag)):
	random_uuid = str(uuid.uuid4())
	message = f"UUID: {random_uuid} - X-Flag: {x_flag}"
	if x_flag == XFlag.green:
		logger.info(message)
	if x_flag == XFlag.red:
		await request.app.pika_producer.send_message(message)

	return {"uuid": random_uuid}
