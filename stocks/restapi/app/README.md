# RESTful API

## How to Run

1. Build the Docker container:
`docker build -t restapi-app .`


2. Run the container:
`docker run -p 5000:5000 restapi-app`

To run without docker:
`python -m flask --app __init__ run`


## Rationale

We chose Flask as our framework for building the REST API due to its lightweight nature and ease of use. It allows us to quickly set up API endpoints and handle HTTP requests.

## Challenges Faced

- Implementing error handling for API requests and responses.
- Ensuring proper communication with the Celery tasks and handling asynchronous responses.
- Celery versioning, using verison greater than 4 would lead to unexpected error. 
ValueError: not enough values to unpack (expected 3, got 0)


## Potential Failure Scenarios

- If the Celery worker crashes or fails to process tasks, the API may not receive timely responses.
- We assume that the reponse if valid, with code 200 will not be empty.

## Improvements for Production

- Instead of using Flask development server, use production WSGI server instead.
- Instead of using a loop tp go through all dates, we can use Celery's built in function to dispatch multiple tasks concurrently. Doing this will save the computation load and increase performance.
- Implement load balancing to handle a large number of requests.
- Set up proper logging and monitoring to identify and address issues in real-time.
