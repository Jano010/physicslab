
from typing import Annotated

from fastapi import Depends

from physicslab.experiments.repository import ExperimentsRepository


def get_experiments_repository() -> ExperimentsRepository:
    return ExperimentsRepository()

ExperimentsRepositoryDep = Annotated[ExperimentsRepository, Depends(get_experiments_repository)]

