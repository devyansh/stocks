# Celery Tasks

## How to Run

1. Build the Docker container:
`docker build -t celery-worker .`


2. Run the container:
`docker run celery-worker`


## Rationale

We chose Celery to manage the asynchronous tasks in the application. It provides a robust way to handle background tasks and offload heavy computations from the main application.

## Challenges Faced

- Configuring Celery to work with a message broker (Redis in our case).
- Ensuring that Celery tasks are properly registered and executed.

## Potential Failure Scenarios

- Message broker (Redis) downtime can affect task processing and communication.

## Improvements for Production

- Deploy multiple Celery workers to handle high task loads.
- Set up monitoring to detect any task failures and automatically retry failed tasks.
