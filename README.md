# User-Management-API

## About the project

It is a simple project which manages data and I am using this project as an exercise to practice my web development skills.

* Server:
    * Flask

## Deployment

This application is deployed on [Heroku](https://www.heroku.com/). You can access the application using the following link: <https://user-manager.herokuapp.com/>

## Project Management

The project management of this application was done using Trello boards with the use of a kanban workflow. Tasks related to the endpoints (GET, POST, DELETE and PUT) were added as cards and moved through different stages of the kanban board (to-do, doing, code-review, and done)

## Endpoints

### GET
* `/` - health check and provide the welcome message
* `/v1/users` - details of all users and can also identify the user with the help of query strings. For eg: v1/users?team=red
* `/v1/users/<request-id>` - output of all users with the specific id

### POST
* `/v1/users` - create a new user with proper attributes like age, name and team in a string format

### DELETE
* `/v1/users/<request-id>` - deleting user details with ID provided and providing error with proper HTTP response code of 404

### PUT
* `/v1/users/<id>` - updating ID of specific user details without changing any other attributes. Attributes allowed to update are age, name and team