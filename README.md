# Assignment

Basic HTTP application with docker

## Installation

Use docker compose to setup application

> cd docker/
> docker-compose up

## Server

Server will run on port 8000

## Examples

### Info endpoint

Request:
```
curl --location --request GET 'http://localhost:8000/info' \
--header 'Content-Type: application/json' \
--data-raw '{
    "url": "https://example.com"
}'
```

Response:
```
{"receiver":"Cisco is the best!"}
```

### Ping endpoint

Request:
```
curl --location --request POST 'http://localhost:8000/ping' \
--header 'Content-Type: application/json' \
--data-raw '{
    "url": "https://example.com"
}'
```

Response:
```
{"payload":"<!doctype html>\n<html>\n<head>\n    <title>Example Domain</title> ... </html>\n"}
```

---

Request invalid domain:
```
curl --location --request POST 'http://localhost:8000/ping' \
--header 'Content-Type: application/json' \
--data-raw '{
    "url": "https://example123.com"
}'
```

Response:
```
{"payload":null}
```


## Schema

Request
```
curl --location --request GET 'http://localhost:8000/schema' \
--header 'Content-Type: application/json' \
--data-raw '{
    "url": "https://example.com"
}'
```

Response
```
info:
  title: Example API
  version: '1.0'
openapi: 3.0.0
paths:
  /info:
    get:
      responses:
        200:
          description: Static content
  /ping:
    post:
      requestBody:
        content:
          application/json:
            schema:
              properties:
                url:
                  type: string
              type: object
      responses:
        200:
          content:
            application/json:
              schema:
                properties:
                  payload:
                    type: string
                type: object
          description: Payload of given site
        400:
          description: Invalid param error
```
