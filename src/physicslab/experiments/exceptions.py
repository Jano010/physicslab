
class ExperimentError(Exception):
    """Base class for exceptions in this module."""
    status_code: int = 500
    pass

class ExperimentAlreadyExistsError(ExperimentError):
    """Exception raised when an experiment already exists."""
    status_code: int = 400
    pass

class ExperimentForbiddenError(ExperimentError):
    """Exception raised when an experiment is forbidden."""
    status_code: int = 403
    pass

class ExperimentNotFoundError(ExperimentError):
    """Exception raised when an experiment is not found."""
    status_code: int = 404
    pass