.PHONY: build run push

build:
	docker build -t do360now/semiconductor:0.1.1 .

run:
	docker run --rm --name semiconductor-overview -p 8000:8000 do360now/semiconductor:0.1.1

push:
	docker push do360now/semiconductor:0.1.1
