from pydantic import BaseModel
from typing import Optional, Dict, Any


class Message(BaseModel):

    message: str



class Analysis(BaseModel):

    type: str

    intent: str

    confidence: float



class Plan(BaseModel):

    action: str

    tool: Optional[str] = None



class ToolResult(BaseModel):

    success: bool

    data: Optional[Dict[str, Any]] = None

    error: Optional[str] = None



class AgentResponse(BaseModel):

    agent: str

    version: str

    input: str

    analysis: Analysis

    plan: Plan

    result: Optional[ToolResult] = None

    time: str
