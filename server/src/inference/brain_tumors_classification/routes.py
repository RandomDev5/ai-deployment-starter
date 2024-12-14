from fastapi import APIRouter, File, UploadFile
from celery.result import AsyncResult

from src.inference.brain_tumors_classification.service import (
    BrainTumorClassificationService,
)
from src.inference.celery_jobs import celery_app, predict_brain_tumors_task

brain_tumors_classification_router = APIRouter()

brain_tumor_service = None


@brain_tumors_classification_router.post(
    "",
    summary="Predict brain tumor type",
    description="Predict the type of brain tumor from an image",
)
async def predict(file: UploadFile = File(...)):
    """
    Submit a brain tumor prediction task.

    Args:
        inferenceSchema (InferenceSchema): Schema containing the instance URL of the DICOM image.

    Returns:
        dict: Contains the task ID of the submitted Celery task.
    """
    raise NotImplementedError("This function is not implemented yet.")


# Part 2: This is the advanced deployment mechanism
@brain_tumors_classification_router.post(
    "/background",
    summary="Submit a brain tumor prediction task",
    description="Submit an image for brain tumor prediction",
)
async def submit_prediction(file: UploadFile = File(...)):
    """
    Submit a brain tumor prediction task.

    Args:
        inferenceSchema (InferenceSchema): Schema containing the instance URL of the DICOM image.

    Returns:
        dict: Contains the task ID of the submitted Celery task.
    """
    raise NotImplementedError("This function is not implemented yet.")

# Part 2, the whole block will be written in the live session
@brain_tumors_classification_router.get(
    "/results/{task_id}",
    summary="Check task status",
    description="Query the status and result of a prediction task",
)
async def get_task_status(task_id: str):
    """
    Returns the status of the background task.
    """
    raise NotImplementedError("This function is not implemented yet.")