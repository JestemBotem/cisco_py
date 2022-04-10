import pydantic
from pydantic import BaseModel, ValidationError
from starlette.endpoints import HTTPEndpoint
from starlette.requests import Request
from starlette.responses import JSONResponse, Response

from external_content import ContentService


class PingPayload(BaseModel):
    url: pydantic.HttpUrl


class PingEndpoint(HTTPEndpoint):
    async def post(self, req: Request) -> Response:
        """
        requestBody:
            content:
                application/json:
                    schema:
                        type: object
                        properties:
                            url:
                                type: string
        responses:
            200:
                description: Payload of given site
                content:
                    application/json:
                        schema:
                            type: object
                            properties:
                                payload:
                                    type: string
            400:
                description: Invalid param error
        """
        payload = await req.json()

        try:
            ping_payload = PingPayload(**payload)
        except ValidationError as e:
            return Response(e.json(), status_code=400, media_type="application/json")

        cs = ContentService()
        content = cs.get_content(ping_payload.url)

        return JSONResponse({"payload": content.content})


class InfoEndpoint(HTTPEndpoint):
    async def get(self, req: Request) -> Response:
        """
        responses:
            200:
                description: Static content
        """
        return JSONResponse({"receiver": "Cisco is the best!"})
