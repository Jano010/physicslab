import asyncio
from typing import Any

from physicslab.experiments.exceptions import ExperimentNotFoundError


class ExperimentsRepository:

    DB_LATENCY_SECONDS = 0.2    

    def __init__(self) -> None:
        self.experiments : list[dict[str, Any]] = []

    async def create_experiment(self, experiment: dict[str, Any]) -> dict[str, Any]:
        await asyncio.sleep(self.DB_LATENCY_SECONDS)
        experiment["id"] = len(self.experiments) + 1
        experiment["user_id"] = 1
        self.experiments.append(experiment)
        print(self.experiments)
        return experiment

    async def get_experiments(self, user_id : int) -> list[dict[str, Any]]:
        await asyncio.sleep(self.DB_LATENCY_SECONDS)
        print(self.experiments)
        return [experiment for experiment in self.experiments if experiment["user_id"] == user_id] 

    async def get_experiment_by_id(self, id:int) -> dict[str, Any] | None:
        await asyncio.sleep(self.DB_LATENCY_SECONDS)
        for experiment in self.experiments:
            if experiment["id"] == id:
                return experiment
        return None

    async def update_experiment(self, id:int, experiment_data:dict[str, Any]) -> dict[str, Any]:
        await asyncio.sleep(self.DB_LATENCY_SECONDS)
        experiment = await self.get_experiment_by_id(id)
        if experiment:
            new_experiment = {**experiment, **experiment_data}
            self.experiments.remove(experiment)
            self.experiments.append(new_experiment)
            return new_experiment
        else:
            raise ExperimentNotFoundError(f"Experiment with id {id} not found.")

    async def delete_experiment(self, id:int) -> None:
        await asyncio.sleep(self.DB_LATENCY_SECONDS)
        experiment = await self.get_experiment_by_id(id)
        if experiment:
            self.experiments.remove(experiment)
        else:
            raise ExperimentNotFoundError(f"Experiment with id {id} not found.")