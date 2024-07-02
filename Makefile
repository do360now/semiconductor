connect_mongo:
	mongod --dbpath /path/to/your/mongodb/data

setup-docker-compose:
	sudo curl -L "https://github.com/docker/compose/releases/download/v2.10.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
	sudo chmod +x /usr/local/bin/docker-compose

build:
	docker-compose build

up:
	docker-compose up --build


deploy: build up

# git remote add origin https://github.com/do360now/semiconductor.git

git remote add origin git@github.com:do360now/semiconductor.git

git remote set-url origin git@github.com:do360now/semiconductor.git


docker_build:
	docker build -t do360now/semiconductor:0.0.2 .

docker_run:
	docker run --rm --name semiconductor-overview -p 80:80 do360now/semiconductor:0.0.2

docker_push:
	docker push do360now/semiconductor:0.0.2


