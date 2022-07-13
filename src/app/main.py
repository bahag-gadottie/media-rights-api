from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

#from app.core.config import settings
#from app.db import database
#from app.utils.dependencies import verify_token

from app.routes import pic_rights, ping



app = FastAPI()
#app.state.database = database


# Set all CORS enabled origins
# if settings.BACKEND_CORS_ORIGINS:
#     app.add_middleware(
#         CORSMiddleware,
#         allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
#         allow_credentials=True,
#         allow_methods=["*"],
#         allow_headers=["*"],
#         )


# @app.on_event("startup")
# async def startup() -> None:
#     database_ = app.state.database
#     if not database_.is_connected:
#         await database_.connect()
#
#
# @app.on_event("shutdown")
# async def shutdown() -> None:
#     database_ = app.state.database
#     if database_.is_connected:
#         await database_.disconnect()


app.include_router(
    pic_rights.router,
    tags=["Generate copyrights request documents"]
)

app.include_router(ping.router)
