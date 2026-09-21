
from fastapi import APIRouter, FastAPI, Request
from fastapi.responses import JSONResponse

from physicslab.experiments.dependencies import ExperimentsRepositoryDep
from physicslab.experiments.exceptions import (
    ExperimentAlreadyExistsError,
    ExperimentError,
    ExperimentForbiddenError,
    ExperimentNotFoundError,
)
from physicslab.experiments.schemas import (
    ExperimentCreate,
    ExperimentRead,
    experiment_read_dummy,
)

router = APIRouter(prefix="/experiments", tags=["experiments"])

DUMMY_USER_ID = 1

@router.post("")
async def create_experiment(
    repository: ExperimentsRepositoryDep, 
    experiment: ExperimentCreate
    ) -> ExperimentRead:
    experiment_data = experiment.model_dump()
    new_experiment = await repository.create_experiment(experiment_data)
    return ExperimentRead(**new_experiment)

@router.get("")
async def get_experiments(repository: ExperimentsRepositoryDep) -> list[ExperimentRead]:
    object_list = await repository.get_experiments(DUMMY_USER_ID)
    return [ExperimentRead(**o) for o in object_list]

@router.get("/{id}")
async def get_experiment(repository: ExperimentsRepositoryDep, id: int) -> ExperimentRead:
    experiment_data = await repository.get_experiment_by_id(id)

    if not experiment_data:
        raise ExperimentNotFoundError()

    experiment = ExperimentRead(**experiment_data)

    if experiment.user_id != DUMMY_USER_ID:
        raise ExperimentForbiddenError()

    return experiment 

@router.patch("/{id}")
async def update_experiment(
    repository: ExperimentsRepositoryDep, 
    id: int, 
    experiment: ExperimentCreate
    ) -> ExperimentRead:
    new_experiment = await repository.update_experiment(id, experiment.model_dump()) 
    return ExperimentRead(**new_experiment) 

@router.delete("/{id}")
async def delete_experiment(
    repository: ExperimentsRepositoryDep, 
    id: int
    ) -> JSONResponse:
    await repository.delete_experiment(id)
    return JSONResponse(
        status_code=200,
        content={"operation:" "Success"}
    )

def register_experiments_exception_handlers(app: FastAPI) -> None:

    @app.exception_handler(ExperimentError)
    async def experiment_error_handler(
        request : Request, 
        exc: ExperimentError
        ) -> JSONResponse:
        return JSONResponse(
            status_code=exc.status_code,
            content={"detail": "Something went wrong with the experiment."},
        )

    @app.exception_handler(ExperimentAlreadyExistsError)
    async def experiment_already_exists_error_handler(
        request : Request, 
        exc: ExperimentAlreadyExistsError
        ) -> JSONResponse:  
        return JSONResponse(
            status_code=exc.status_code,
            content={"detail": "The experiment already exists."},
        )

    @app.exception_handler(ExperimentForbiddenError)
    async def experiment_forbidden_error_handler(
        request : Request, 
        exc: ExperimentForbiddenError
        ) -> JSONResponse:
        return JSONResponse(
            status_code=exc.status_code,
            content={"detail": "You do not have permission to access this experiment."},
        )

    @app.exception_handler(ExperimentNotFoundError)
    async def experiment_not_found_error_handler(
        request : Request, 
        exc: ExperimentNotFoundError
        ) -> JSONResponse:
        return JSONResponse(
            status_code=exc.status_code,
            content={"detail": "The experiment was not found."},
        )
