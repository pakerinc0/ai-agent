import os


class Config:


    AI_ENABLED = os.getenv(
        "AI_ENABLED",
        "false"
    ).lower() == "true"



    MODEL = os.getenv(
        "MODEL",
        "qwen3:8b"
    )



    LMSTUDIO_URL = os.getenv(
        "LMSTUDIO_URL",
        "http://127.0.0.1:1234/v1"
    )



    OLLAMA_URL = os.getenv(
        "OLLAMA_URL",
        "http://127.0.0.1:11434"
    )



    PROJECT_PATH = os.getenv(
        "PROJECT_PATH",
        "."
    )
