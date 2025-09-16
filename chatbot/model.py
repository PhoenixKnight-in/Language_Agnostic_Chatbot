from datetime import datetime
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field, GetJsonSchemaHandler
from pydantic.json_schema import JsonSchemaValue
from bson import ObjectId

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __get_pydantic_json_schema__(
        cls, core_schema, handler: GetJsonSchemaHandler
    ) -> JsonSchemaValue:
        json_schema = handler(core_schema)
        json_schema.update(type="string")
        return json_schema


# Request Models
class ChatMessage(BaseModel):
    message: str
    language: Optional[str] = "auto"
    session_id: Optional[str] = None
    user_id: Optional[str] = None

class FeedbackRequest(BaseModel):
    session_id: str
    message_id: str
    rating: int = Field(..., ge=1, le=5)
    comment: Optional[str] = None

class FAQRequest(BaseModel):
    question: str
    answer: str
    category: str
    keywords: List[str]
    languages: Dict[str, Dict[str, str]]

# Response Models
class ChatResponse(BaseModel):
    response: str
    confidence: float
    detected_language: str
    session_id: str
    message_id: str
    fallback_to_human: bool = False
    suggested_questions: List[str] = []
    category: Optional[str] = None

class LanguageDetectionResponse(BaseModel):
    detected_language: str
    confidence: float
    supported: bool

# Database Models
class FAQ(BaseModel):
    id: Optional[PyObjectId] = Field(default_factory=PyObjectId, alias="_id")
    question: str
    answer: str
    keywords: List[str]
    category: str
    languages: Dict[str, Dict[str, str]]  # {"hi": {"question": "...", "answer": "..."}}
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
    is_active: bool = True
    priority: int = 1
    
    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

class ConversationLog(BaseModel):
    id: Optional[PyObjectId] = Field(default_factory=PyObjectId, alias="_id")
    session_id: str
    message_id: str
    user_id: Optional[str] = None
    user_message: str
    bot_response: str
    detected_language: str
    confidence: float
    category: Optional[str] = None
    timestamp: datetime = Field(default_factory=datetime.now)
    fallback_triggered: bool = False
    response_time_ms: int = 0
    
    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

class Feedback(BaseModel):
    id: Optional[PyObjectId] = Field(default_factory=PyObjectId, alias="_id")
    session_id: str
    message_id: str
    user_id: Optional[str] = None
    rating: int
    comment: Optional[str] = None
    timestamp: datetime = Field(default_factory=datetime.now)
    
    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

class User(BaseModel):
    id: Optional[PyObjectId] = Field(default_factory=PyObjectId, alias="_id")
    user_id: str = Field(..., unique=True)
    name: Optional[str] = None
    email: Optional[str] = None
    preferred_language: str = "en"
    created_at: datetime = Field(default_factory=datetime.now)
    last_active: datetime = Field(default_factory=datetime.now)
    total_conversations: int = 0
    
    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

# Analytics Models
class ConversationStats(BaseModel):
    total_conversations: int
    total_users: int
    languages_used: Dict[str, int]
    categories_queried: Dict[str, int]
    average_confidence: float
    fallback_rate: float
    response_time_avg: float

class DailyStats(BaseModel):
    date: str
    conversations: int
    unique_users: int
    avg_confidence: float
    fallback_count: int
    top_categories: List[Dict[str, Any]]