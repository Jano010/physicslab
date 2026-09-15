"""Smoke test: check to see if the environment is working and the test package is working"""

import sys


def test_python_version() -> None:
    """Check that the Python version is 3.14 or higher"""
    assert sys.version_info >= (3, 14), "Python version must be 3.14 or higher"


def test_import_package() -> None:
    """Check that the package can be imported"""
    import physicslab  # noqa: F401


def test_pytest_detect_failures() -> None:
    """Check that the assertion failures are detected by pytest"""
    import pytest

    with pytest.raises(AssertionError):
        assert False  # noqa: PLR0133


async def test_asyncio() -> None:
    """Check that asyncio is working"""

    import asyncio

    async def async_func() -> int:
        await asyncio.sleep(0.1)
        return 42

    result = await async_func()
    assert result == 42
