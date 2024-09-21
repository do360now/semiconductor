.PHONY: build run push compile

compile:
	pip-compile requirements.in --upgrade

uvicorn:
	uvicorn app.main:app --reload --host 127.0.0.1 --port 8080

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
	docker build -t do360now/semiconductor:1.2.0 .

run:
	docker run --rm --name semiconductor-overview -p 8000:80 do360now/semiconductor:1.2.0

push:
	docker push do360now/semiconductor:1.2.0


