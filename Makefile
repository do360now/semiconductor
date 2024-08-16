.PHONY: build run push compile

compile:
	pip-compile requirements.in --upgrade

uvicorn:
	uvicorn app:app --reload --host 127.0.0.1 --port 8080

build:
	docker build -t do360now/semiconductor:0.3.3 .

run:
	docker run --rm --name semiconductor-overview -p 80:80 do360now/semiconductor:0.3.3

push:
	docker push do360now/semiconductor:0.3.3


