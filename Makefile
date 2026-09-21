.PHONY: install test cov lint format typecheck run clean

run:
	uv run fastapi dev src/physicslab/main.py

check:
	uv run ruff format --check .
	uv run ruff check .
	uv run mypy .
	uv run pytest

test:
	uv run pytest

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	rm -rf .pytest_cache
