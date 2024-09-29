# Dynamic argument handling
args = `arg="$(filter-out $@,$(MAKECMDGOALS))" && echo $${arg:-${1}}`

# Load .env file
ifneq (,$(wildcard .env))
include .env
export $(shell grep -v '^#' .env | xargs)
endif

# Example target that uses an environment variable
example:
	echo "The value of MY_VAR is: ${VERSION}"

# LLM commands
codellama:
	ollama run codellama --model llama2 --host 127.0.0.1 --port 11434

llm:
	llm -m orca-mini-3b-gguf2-q4_0 'What is the capital of France?'

chat:
	llm -m llm-gpt4all -c 'What is the capital of France?'

query-llm:
	llm models

########################################################################################################################
# Quality checks
########################################################################################################################
poetry:
	pip install poetry

test:
	PYTHONPATH=. poetry run pytest tests

black:
	poetry run black . --check

ruff:
	poetry run ruff check app tests

format:
	poetry run black .
	poetry run ruff check tests --fix

mypy:
	poetry run mypy app

# Compile requirements
compile:
	pip-compile requirements.in --upgrade

# Pre-installation steps for Docker
pre-docker-install:
	sudo apt update && sudo apt upgrade -y
	sudo apt install -y apt-transport-https ca-certificates curl software-properties-common
	curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
	echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Install Docker
docker-install:
	sudo apt update
	sudo apt install -y docker-ce docker-ce-cli containerd.io

# Build Docker image
build:
	docker build -t do360now/semiconductor:${VERSION} .

# Run Docker container
run:
	docker run --rm --name semiconductor-overview -p 8000:80 do360now/semiconductor:${VERSION}

# Push Docker image to repository
push:
	docker push do360now/semiconductor:${VERSION}

# Install CUDA if the script exists
install-cuda:
	if [ -f ./install-cuda.sh ]; then ./install-cuda.sh; else echo "CUDA install script not found."; ficheck:
	make format
	make mypy


.PHONY: build run push compile

########################################################################################################################
# Local development
########################################################################################################################

add-dependencies:
	poetry add $(shell cat requirements.in)

install-dependencies:
	poetry install

run-local:
	poetry run uvicorn app.main:app --reload --host 127.0.0.1 --port 8080

compile:
	pip-compile requirements.in --upgrade

pre-docker-install:
	sudo apt update
	sudo apt upgrade -y
	sudo apt install apt-transport-https ca-certificates curl software-properties-common
	curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
	echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

docker-install:
	sudo apt update
	sudo apt install docker-ce docker-ce-cli containerd.io -y

build:
	docker build -t do360now/semiconductor:${VERSION} .

run:
	docker run --rm --name semiconductor-overview -p 8000:80 do360now/semiconductor:${VERSION}

push:
	docker push do360now/semiconductor:${VERSION}

install-cuda:
	if [ -f ./install-cuda.sh ]; then ./install-cuda.sh; else echo "CUDA install script not found."; fi
