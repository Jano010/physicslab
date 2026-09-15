.PHONY: install test cov lint format typecheck run clean

check:
	uv run ruff format --check .
	uv run ruff check .
	uv run mypy .
	uv run pytest

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	rm -rf .pytest_cache
