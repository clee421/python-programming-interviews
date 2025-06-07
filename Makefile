# ───────────── configurable knobs (override via CLI/env) ─────────────
MIN_PYTHON      ?= 3.12
UV_INSTALL_URL  ?= https://astral.sh/uv/install.sh
VENV_DIR        ?= .venv

# Which extras to install from pyproject ― e.g. `make EXTRAS='dev,test' install`
EXTRAS          ?= dev
# Pip flags to pass through (useful for --no-build-isolation, etc.)
EXTRA_PIP_ARGS  ?=

# ───────────── paths detected at *invoke* time ─────────────
UV_BIN := $(shell command -v uv 2>/dev/null || echo "")
PY_BIN := $(shell command -v python3 python 2>/dev/null | head -n1)

# ---- default goal -----------------------------------------------------------
.DEFAULT_GOAL := install          # <— add this

# ───────────── public targets ─────────────
.PHONY: setup venv install test

## setup : ensure python + uv present (idempotent)
setup: check-python install-uv
	@echo "✔ Environment prerequisites satisfied."

## venv  : create or reuse virtual-env driven by uv
venv: setup
	@if [ -d "$(VENV_DIR)" ] && [ -f "$(VENV_DIR)/pyvenv.cfg" ]; then \
		echo "✔ Virtual env exists → $(VENV_DIR)"; \
	else \
		echo "Creating $(VENV_DIR)…"; \
		uv venv "$(VENV_DIR)"; \
	fi

## install : prefer uv.lock, else fall back to a live resolve
install: venv
	@if [ -f uv.lock ]; then \
		echo "🔒 uv.lock found → running 'uv sync'"; \
		GROUP_FLAGS=""; \
		if [ -n "$(EXTRAS)" ]; then \
			for g in $(EXTRAS); do \
				GROUP_FLAGS="$$GROUP_FLAGS --group $$g"; \
			done; \
		fi; \
		uv sync $$GROUP_FLAGS $(EXTRA_PIP_ARGS); \
	else \
		echo "🔓 No lockfile → falling back to 'uv pip install'"; \
		if [ -n "$(EXTRAS)" ]; then \
			EXTRA_STR=".[${EXTRAS}]"; \
		else \
			EXTRA_STR=.; \
		fi; \
		uv pip install -e $$EXTRA_STR $(EXTRA_PIP_ARGS); \
	fi
	@echo "Activating venv and install pre-commit..."
	@source "$(VENV_DIR)/bin/activate" && pre-commit install

## test : simple downstream workflow
test: install
	@echo "Running tests…"
	@$(VENV_DIR)/bin/python -m pytest -q

## clean : blow away venv & build artefacts
clean:
	@rm -rf "$(VENV_DIR)" .pytest_cache dist build
	@echo "🗑  Cleaned virtual env and build artifacts."

# ───────────── helpers ─────────────
.PHONY: check-python install-uv

check-python:
	@python -c 'import os,sys; want=tuple(map(int,"$(MIN_PYTHON)".split("."))); \
have=sys.version_info[:3]; \
import sys as _s; \
(_s.exit(f"❌ Need {want[0]}.{want[1]}+, found {have[0]}.{have[1]}.{have[2]}") \
 if have<want else print(f"✔ Python {have[0]}.{have[1]}.{have[2]} ≥ {want[0]}.{want[1]}"))'

install-uv:
	@if [ -n "$(UV_BIN)" ]; then \
		echo "✔ uv already installed → $(UV_BIN)"; \
	else \
		echo "Installing uv …"; \
		curl -Ls "$(UV_INSTALL_URL)" | sh; \
	fi
