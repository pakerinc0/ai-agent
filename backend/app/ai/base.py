from abc import ABC, abstractmethod


class AIProvider(ABC):
    """
    Базовый интерфейс любой AI модели.
    """

    @abstractmethod
    async def generate(self, prompt: str) -> str:
        pass
