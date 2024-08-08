.PHONY: build run push

build:
	docker build -t do360now/semiconductor:0.1.2 .

run:
	docker run --rm --name semiconductor-overview -p 80:80 do360now/semiconductor:0.1.2

push:
	docker push do360now/semiconductor:0.1.2
