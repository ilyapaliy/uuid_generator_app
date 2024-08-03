from fastapi import APIRouter, Depends, Request
import uuid
from schemas import XFlag, UUIDResponse, AMQPMessage
from dependencies import verify_x_flag
import logging


logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/generate-uuid"
)


@router.get("/", response_model=UUIDResponse)
async def get_uuid(request: Request, x_flag: XFlag = Depends(verify_x_flag)):
	random_uuid = uuid.uuid4()

	if x_flag == XFlag.green:
		logger.info(AMQPMessage(uuid=random_uuid, xflag=x_flag).to_log_message())
	if x_flag == XFlag.red:
		message = AMQPMessage(uuid=random_uuid, xflag=x_flag)
		await request.app.pika_producer.send_message(message)

	return UUIDResponse(uuid=random_uuid)
