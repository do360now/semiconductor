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
