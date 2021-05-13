from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import HTTPException
from fastapi import File
from typing import List
from typing import Any
from eda.ws.ctrls import VisualizationCtrl


router = APIRouter()


@router.post("/upload", response_model=List[str])
async def upload(file: UploadFile = File(...)) -> Any:
    if file.content_type != "text/csv":
        raise HTTPException(status_code=400, detail="Incorrect file type!")

    viz_ctrl = VisualizationCtrl(file.file)
    err, files = viz_ctrl.process_file()

    if err:
        raise HTTPException(status_code=400, detail=err)

    return files
