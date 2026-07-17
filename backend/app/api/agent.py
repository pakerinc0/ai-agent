from fastapi import APIRouter

from app.core.agent import Agent
from app.models.schemas import Message


router = APIRouter(
    prefix="/agent",
    tags=["Agent"]
)


agent = Agent()



@router.post("/chat")
async def chat(data: Message):

    result = await agent.process(
        data.message
    )

    return result
