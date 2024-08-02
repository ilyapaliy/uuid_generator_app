from fastapi import Header, HTTPException, status
from typing import Annotated
from schemas import XFlag


def verify_x_flag(X_Flag: Annotated[XFlag | None, Header()] = None):
	if X_Flag == XFlag.green or XFlag.red or None:
		return(X_Flag)
	else:
		raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Invalid header X-Flag")
