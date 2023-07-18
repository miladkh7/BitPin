# BitPin
this is technical task for BitPin
Blog App Api

**Some additional feature and improvments add in my free time 
but the technical task tagged by version 1.0.0**

## Technologies
* Django
* Django Rest Framework
* docker and docker compose 


## Project Technical Description
* use DRF token base login 


## Installation
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

### Registration 
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
### Login
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
### Logout
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
only support technical Task

### [1.1.0] 2023-07-18 milad_khaleghi@Live.com
Some additional Feature and improvements added to project in my free time as hobby.

#### Added
- User Api (Registration-login-logout)
- permissions check 
- swagger documents for api


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


### Deployment
 - [ ] git hub ci/cd