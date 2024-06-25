.PHONY: install
install:
	pip install -r requirements.txt

.PHONY: run
run:
	python manage.py runserver

.PHONY: test
test:
	python manage.py test

.PHONY: start-dev-docker
start-dev-docker:
	docker compose -f docker/docker-compose.dev.yaml up -d

.PHONY: stop-dev-docker
stop-dev-docker:
	docker compose -f docker/docker-compose.dev.yaml down

.PHONY: start-test-docker
start-test-docker:
	docker compose -f docker/docker-compose.test.yaml up -d

.PHONY: stop-test-docker
stop-test-docker:
	docker compose -f docker/docker-compose.test.yaml down
