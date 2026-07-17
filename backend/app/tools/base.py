from abc import ABC, abstractmethod


class Tool(ABC):

    name = "base"


    @abstractmethod
    async def execute(self, **kwargs):
        pass
