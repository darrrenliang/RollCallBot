import config
import uvicorn
from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
# from line.urls import line_app
from routers.line.message_event import line_bot_api
from view import view

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# View
app.include_router(view)

# LINE Bot
# app.include_router(line_app)


if __name__ == "__main__":
    # Local WSGI: Uvicorn
    ip = config.IP
    port = int(config.PORT)
    uvicorn.run(
        "main:app",
        host=ip,
        port=port,
        workers=4,
        log_level="info",
        access_log=True,
        use_colors=True,
        reload=True,
    )