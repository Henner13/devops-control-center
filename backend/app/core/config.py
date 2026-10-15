from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str

    db_host: str
    db_port: int

    db_user: str
    db_password: str
    db_name: str

    class Config:
        env_file = ".env"

    @property
    def database_url(self):
        return (
            f"postgresql+psycopg2://"
            f"{self.db_user}:"
            f"{self.db_password}@"
            f"{self.db_host}:"
            f"{self.db_port}/"
            f"{self.db_name}"
        )


settings = Settings()
