# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build and document a REST API using the FastAPI framework in Python, including defining routes, handling request data, and returning JSON responses.

## 📝 Tasks

### 🛠️ Set Up a FastAPI Application

#### Description
Install FastAPI and create a basic application with at least two routes that return JSON responses.

#### Requirements
Completed program should:

- Install `fastapi` and `uvicorn` using pip
- Create a `main.py` file that initializes a FastAPI app instance
- Define a `GET /` route that returns a welcome message as JSON
- Define a `GET /items` route that returns a hardcoded list of items
- Run the app locally with `uvicorn` and verify responses in the browser or with `curl`


### 🛠️ Add a Resource Endpoint with Path and Query Parameters

#### Description
Extend the API with a resource endpoint that uses a path parameter to retrieve a single item and a query parameter to filter results.

#### Requirements
Completed program should:

- Define a `GET /items/{item_id}` route that returns a single item by its ID
- Return a `404` error response if the item ID does not exist
- Define a `GET /items` route that accepts an optional `search` query parameter to filter items by name
- Return appropriate JSON responses for all cases


### 🛠️ Handle POST Requests with a Request Body

#### Description
Add a `POST` endpoint that accepts a JSON request body to create a new item and adds it to the in-memory list.

#### Requirements
Completed program should:

- Define a Pydantic model (e.g., `Item`) with at least `id` and `name` fields
- Define a `POST /items` route that accepts an `Item` body and appends it to the items list
- Return the created item as the response with a `201` status code
- Validate that required fields are present (FastAPI/Pydantic handles this automatically)
