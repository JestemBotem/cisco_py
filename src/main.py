import uvicorn
from fastapi import FastAPI
from starlette.routing import Route
from starlette.schemas import SchemaGenerator

import handlers


def get_schema() -> SchemaGenerator:
    schemas = SchemaGenerator(
        {"openapi": "3.0.0", "info": {"title": "Example API", "version": "1.0"}}
    )

    return schemas


def get_app() -> FastAPI:
    schemas = get_schema()

    routes = [
        Route("/info", handlers.InfoEndpoint),
        Route("/ping", handlers.PingEndpoint),
        Route("/schema", schemas.OpenAPIResponse, include_in_schema=False),
    ]

    app = FastAPI(routes=routes)
    return app


def main():
    app = get_app()

    uvicorn.run(app, host='0.0.0.0', port=8000)


if __name__ == "__main__":
    main()
