# User-Management-API

## About the project

It is a simple project which manages data and I am using this project as an exercise to practice my web development skills.

* Server:
    * Flask

## Endpoints

### GET
* `/` - health check
* `/v1/users` - details of users
* `/v1/users/<request-id>` - users with the specific id

### POST
* `/v1/users` - create a new user with proper attributes

### DELETE
* `/v1/users/<request-id>` - deleting user details and providing error with proper HTTP response code

### PUT
* `/v1/users/<id>` - updating user details without changing any other attributes

