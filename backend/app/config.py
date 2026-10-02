from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    groq_api_key: str

    groq_model: str = "openai/gpt-oss-20b"

    tavily_api_key: str

    use_mock_llm: bool = True

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()