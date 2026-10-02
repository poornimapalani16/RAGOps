from langchain_groq import ChatGroq

from app.config import settings
from app.services.mock_llm import mock_llm


class LLMService:

    def __init__(self):

        self.use_mock = settings.use_mock_llm

        if not self.use_mock:

            self.groq = ChatGroq(
                model=settings.groq_model,
                api_key=settings.groq_api_key,
                temperature=0,
                max_tokens=400,
                reasoning_effort="low",
            )


    def invoke(self, prompt: str):

        if self.use_mock:

            return mock_llm.invoke(prompt)

        return self.groq.invoke(prompt)


    def invoke_json(self, prompt: str):

        if self.use_mock:

            return mock_llm.invoke(prompt)

        json_llm = self.groq.bind(
            response_format={
                "type": "json_object"
            }
        )

        return json_llm.invoke(prompt)


llm = LLMService()