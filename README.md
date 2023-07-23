# Bitpin Blog
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)  [![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)

[![Build and Push Docker Image to Docker Hub](https://github.com/miladkh7/BitPin/actions/workflows/deploy.yml/badge.svg)](https://github.com/miladkh7/BitPin/actions/workflows/deploy.yml)

this is technical task for BitPin
Blog App Api

**:exclamation:Some additional feature and improvments add in my free time 
but the technical task tagged by version 1.0.0**


## Table of contents
* Project technical Info
  * [Technologies](#Technologies)
  * [Project Technical Description](#Project-Technical-Description)
* [Installation](#Installation)
* [EndPoints](#End-Points)
* [Usage](#Usage)
  * [User](#User)
    * [Registration](#Registration)
    * [Login](#Login)
    * [Logout](#Logout)
  * [Blog](#Blog)
    * [Authentication](#Authentication)
  * [Change Log](#Change-Log)
  * [ToDo](#ToDo)
___

## Technologies
* [![Django][Django]][Django-url]
* [![Django Rest Framework][Django-Rest-Framework]][Django-Rest-Framework-url]
* [![Docker][Docker]][Docker-Compose-url]
* [![Docker Compose][Docker-Compose]][Docker-Compose-url]
* [![GitHub Actions][GitHub-Actions]][GitHub-Actions-url]
* [![Docker Hub][Docker-Hub]][Docker-Hub-url]


## Project Technical Description
* use DRF token base login 


## Installation
Install Docker on your machine by following the official Docker installation guide. 
Pull the Docker image from Docker Hub or clone project
### Docker hub
Open a terminal or command prompt.
Pull the Docker image from Docker Hub by running the following command:
`docker pull miladkh4/bitpin:tagname`  
for example for latest last version use this command  
`docker pull miladkh4/bitpin:latest`

### Manual
* clone the repository from github by this command  
 `git clone https://github.com/miladkh7/BitPin.git `
* change `sample.env` to `.env ` and set environments variables
* run by docker with this command `docker-compose up`


## EndPoints
the document of APIs is available in swagger ui at this endpoints
- `appDomain:appPort/schema` in open api3 format
- `appDomain:appPort/schema/swagger-ui/` in swagger view
- `appDomain:appPort/schema/redoc/` in doc view
  
## Usage
### User
#### Registration 
send POST Request to `appDomain:appPort\auth\users\`
with value
>    **email:** `yourEmail`  
    **username:** `yourUserName`  
    **Password:** `yourPassword`  

and get Response `HTTP 201 Created`
for example use this curl command

```
curl -X POST http://127.0.0.1:8000/auth/users/ \
    -H 'Content-Type: application/json' \
    -d '{
    "password": "example123456",
    "username": "userTest",
    "email":"example@example.com"
}'
```
#### Login
for get token login we shod send POST Request to this end point `appDomain:appPort\auth\token\login`
with value
  
>    **username:** yourUserName  
    **Password:** yourPassword  

and get Response with `HTTP 200 OK` and get auth_token

    {
    "auth_token": "6cdfc34a6e2141f77fbc5fdf745de37837e3ab68"
    }
for example use this curl command
```
curl -X POST http://127.0.0.1:8000/auth/token/login \
    -H 'Content-Type: application/json' \
    -d '{
    "password": "123456",
    "username": "milad"
}'
```
#### Logout
for logout send post request to `appDomain:appPort\auth\token\login`
with  `Authorization` in request header and ` Token [auth_token]` for its value

for example use this curl command
```
curl -X POST http://127.0.0.1:8000/auth/token/logout \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Token 6cdfc34a6e2141f77fbc5fdf745de37837e3ab68'
```

### Blog
#### Authentication
set `Authorization` in request header with value ` Token [auth_token]`
for example for post use this curl command
```
curl -X POST http://127.0.0.1:8000/blog/article/ \
    -H 'Authorization: Token 6cdfc34a6e2141f77fbc5fdf745de37837e3ab68' \
    -H 'Content-Type: application/json' \
    -d '{
    "title": "New Book",
    "content": "new book contnet"
}'
```
## Change Log  
### [1.0.0] 2023-07-08 milad_khaleghi@Live.com
:sparkles: Only support technical Task

### [1.1.0] 2023-07-18 milad_khaleghi@Live.com
:sparkles: Some additional Feature and improvements added to project my free time as hobby.

#### Added
- :sparkles: User Api (Registration-login-logout)
- :lock: Permissions check 
- :sparkles:: Swagger documents for API
- :books: Add some tests for blog

#### Changed
- :key: Use Token for authentication
  
### [1.2.0] 2023-07-23 milad_khaleghi@Live.com
:sparkles: Some additional Feature and improvements added to project in my free time as hobby.

#### Added
- :books: Add GitHub Action for build and push images to Docker Hub

## ToDo
### User app
 - [x] create custom user
 - [x] create profile 
 - [x] custom user model admin page
 - [x] login api(token base)
 - [x] permission
 - [x] add open api schema
 - [ ] separate develop setting
 - [ ] document
 - [ ] Update profile Apis
 - [ ] define reviewer permission
 - [ ] use only field to improve performance

### Blog App
 - [x] add unit test for create, update , get , delete test with checking permission

### Deployment
 - [x] git hub ci/cd




<!-- assets -->
[Django]:https://img.shields.io/badge/-Django-092E20?style=for-the-badge&logo=django&logoColor=white
[Django-Rest-Framework]:https://img.shields.io/badge/-Django%20Rest%20Framework-FF1709?style=for-the-badge&logo=django&logoColor=white
[Docker]:https://img.shields.io/badge/-Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white
[Docker-Compose]:https://img.shields.io/badge/-Docker%20Compose-2496ED?style=for-the-badge&logo=docker&logoColor=white
[GitHub-Actions]:https://img.shields.io/badge/-GitHub%20Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white
[Docker-Hub]:https://img.shields.io/badge/-Docker%20Hub-2496ED?style=for-the-badge&logo=docker&logoColor=white

[Django-url]:https://.djangoproject.com/
[Django-Rest-Framework-url]:https://www.django-rest-framework.org/
[Docker-url]:https://www.docker.com
[Docker-Compose-url]:https://docs.docker.com/compose/
[GitHub-Actions-url]:https://github.com/features/actions
[Docker-Hub-url]:https://hub.docker.com/