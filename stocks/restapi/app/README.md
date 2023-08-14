# RESTful API

## How to Run

1. Build the Docker container:
`docker build -t restapi-app .`


2. Run the container:
`docker run -p 5000:5000 restapi-app`


## Rationale

We chose Flask as our framework for building the REST API due to its lightweight nature and ease of use. It allows us to quickly set up API endpoints and handle HTTP requests.

## Challenges Faced

- Implementing error handling for API requests and responses.
- Ensuring proper communication with the Celery tasks and handling asynchronous responses.

## Potential Failure Scenarios

- If the Celery worker crashes or fails to process tasks, the API may not receive timely responses.
- We assume that the reponse if valid, with code 200 will not be empty.

## Improvements for Production

- Instead of using Flask development server, use production WSGI server instead.
- Implement load balancing to handle a large number of requests.
- Set up proper logging and monitoring to identify and address issues in real-time.