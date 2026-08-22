"""OpenAI model provider adapter.

Kept isolated so the application architecture is not tied to one vendor.
"""


class OpenAIProvider:
    def __init__(self, client):
        self.client = client

    def generate_structured(self, prompt: str, schema: dict):
        response = self.client.responses.create(
            model="gpt-5-mini",
            input=prompt,
            text={"format": {"type": "json_schema", "schema": schema}},
        )

        return response.output_parsed
