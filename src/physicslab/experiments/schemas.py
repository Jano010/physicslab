from enum import StrEnum

from pydantic import BaseModel, ConfigDict, Field


class ExperimentStatus(StrEnum):
    ACTIVE = "active"
    INACTIVE = "inactive"

class BaseExperiment(BaseModel):
   name : str = Field(max_length=100, min_length=1)
   description : str | None = Field(default=None, max_length=500)
   status : ExperimentStatus 

class ExperimentCreate(BaseExperiment):
    model_config = ConfigDict(extra="forbid")
    pass

class ExperimentRead(BaseExperiment):
   id : int
   user_id : int

class ExperimentUpdate(BaseExperiment):
    model_config = ConfigDict(extra="forbid")
    pass

experiment_read_dummy = ExperimentRead(
    id=1,
    name="Test Experiment",
    description="This is a test experiment.",
    status=ExperimentStatus.ACTIVE,
    user_id=1
    )