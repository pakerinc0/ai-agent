from pydantic import BaseModel
from typing import Any, Optional



# Сообщение от пользователя

class Message(BaseModel):
    message: str



# Анализ сообщения

class Analysis(BaseModel):
    type: str
    intent: str
    confidence: float



# План выполнения

class Plan(BaseModel):
    action: str
    tool: Optional[str] = None



# Результат инструмента

class ToolResult(BaseModel):
    success: bool
    data: Optional[Any] = None
    error: Optional[str] = None



# Общий результат агента

class Result(BaseModel):
    success: bool
    data: Optional[Any] = None
    error: Optional[str] = None



# Ответ агента

class AgentResponse(BaseModel):

    agent: str

    version: str

    input: str

    analysis: Analysis

    plan: Plan

    result: Result

    time: str
