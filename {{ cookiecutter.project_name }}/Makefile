.PHONY: install lint format test build deploy ship_it start mcp_inspector clean

install:
	uv sync

lint:
	uv run mypy --strict {{ cookiecutter.project_slug }}/
	uv run ruff check --fix {{ cookiecutter.project_slug }}/

format:
	uv run ruff format {{ cookiecutter.project_slug }}/

test:
	uv run pytest {{ cookiecutter.project_slug }} \
		--doctest-modules \
		--junitxml=reports/test-results-$(shell cat .python-version).xml

build: clean
	uv run build

deploy: install build

ship_it: build
	git push

start:
	uv run {{ cookiecutter.project_slug }}/main.py

mcp_inspector:
	npx @modelcontextprotocol/inspector uv --directory ${PWD} run {{ cookiecutter.project_slug }}/main.py

clean:
	rm -rf dist/ build/ reports/ *.egg-info/ *cache