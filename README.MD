# Cookie Session Generator

### Description
Application is meant to be used as a session cookie generator (as a ctf utility). Flask/Django session cookie is generated with "isDangerous" library which can took time while debugging for the first time.

### Set-up
Set up new docker container, so that:
```
	git clone https://github.com/BillyGLW/SessionCookieGenerator.git && cd SessionCookieGenerator
```
	Build and run docker container:
```
	docker-compose build .
	docker-compose down && docker-compose up
```

### Usage
Navigate to localhost:1337, then encoode/decode session cookie depending on the needs.

