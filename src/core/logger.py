import logging, sys

logger = logging.getLogger()
formatter = logging.Formatter(
	fmt = "%(asctime)s - %(levelname)s - %(message)s")
stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setFormatter(formatter)
logger.setLevel(logging.INFO)
logger.handlers = [stream_handler]
