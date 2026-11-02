from fastapi import FastAPI, Query, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.core.config import get_settings
from app.models.puzzle import Puzzle
from app.services.slicer import slice_image

import logging
import time

settings = get_settings()
app = FastAPI()

settings.pieces_dir.mkdir(parents=True, exist_ok=True)
app.mount("/pieces", StaticFiles(directory=settings.pieces_dir), name="pieces")


# ---------------------------------------------------------
# CORS
# ---------------------------------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,   # e.g. ["http://localhost:5173"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------------------------------------------------
# Logging middleware
# ---------------------------------------------------------
logger = logging.getLogger("showboxd")

@app.middleware("http")
async def log_requests(request: Request, call_next):
    start = time.time()
    response = await call_next(request)
    duration = round((time.time() - start) * 1000, 2)

    logger.info(
        f"{request.method} {request.url.path} "
        f"status={response.status_code} duration={duration}ms"
    )

    return response


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.get("/puzzle", response_model=Puzzle)
def get_puzzle(
        rows: int = Query(gt=0, le=settings.max_grid_size),
        columns: int = Query(gt=0, le=settings.max_grid_size),
):
    out_dir = settings.pieces_dir / f"{rows}x{columns}"
    return slice_image(
        image_path=settings.image_path,
        rows=rows,
        columns=columns,
        out_dir=out_dir,
        url_prefix=f"/pieces/{rows}x{columns}",
    )
