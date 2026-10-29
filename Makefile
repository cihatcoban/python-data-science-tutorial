.PHONY: help install install-dev lint format test coverage clean jupyter docker-build docker-run

help:
	@echo "Available commands:"
	@echo "  make install       : Install production dependencies"
	@echo "  make install-dev   : Install development & test dependencies"
	@echo "  make lint          : Run code linter (ruff)"
	@echo "  make format        : Format code automatically (ruff & black)"
	@echo "  make test          : Run unit tests with pytest"
	@echo "  make coverage      : Run tests and generate HTML coverage report"
	@echo "  make clean         : Clean caches and build artifacts"
	@echo "  make jupyter       : Launch Jupyter Lab"
	@echo "  make docker-build  : Build reproducible Docker container"

install:
	pip install -r requirements.txt
	pip install -e .

install-dev:
	pip install -r requirements.txt -r requirements-dev.txt
	pip install -e .

lint:
	ruff check src tests

format:
	ruff format src tests
	black src tests

test:
	pytest tests/ -v

coverage:
	pytest --cov=src/datascience_toolbox --cov-report=term-missing --cov-report=html tests/

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name ".ruff_cache" -exec rm -rf {} +
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	rm -rf htmlcov .coverage build dist

jupyter:
	jupyter lab --ip=0.0.0.0 --port=8888 --no-browser

docker-build:
	docker build -t python-data-science:latest .

docker-run:
	docker run -p 8888:8888 -v $(PWD):/workspace python-data-science:latest
