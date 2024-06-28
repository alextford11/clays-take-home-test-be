# clays-take-home-test-be

## Getting started

1. Install requirements: `make install`
2. Setup postgres database: `make start-dev-docker` (to stop close database use `make stop-dev-docker`)
3. Run migrations: `python manage.py migrate`
4. Start the django app: `make run`

## Testing

1. Install requirements: `make install`
2. Setup postgres database: `make start-test-docker` (to stop close database use `make stop-test-docker`)
3. Run tests: `make test`
