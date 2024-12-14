from celery import Celery
import torch

from src.inference.brain_tumors_classification.service import (
    BrainTumorClassificationService,
)

from src.config import Config

torch.set_num_threads(1)

celery_app = None

brain_tumor_service = None


# @celery_app.task
def predict_brain_tumors_task(image_bytes: bytes):
    """
    Celery task for predicting brain tumor type.

    Args:
        instance_url (str): The DICOM file instance URL.

    Returns:
        dict: Prediction result with class and probability.
    """
    raise NotImplementedError("This function is not implemented yet.")