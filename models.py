from dataclasses import dataclass
from datetime import datetime


@dataclass
class User:
    id: str
    username: str


@dataclass
class Channel:
    id: str
    name: str


@dataclass
class Stream:
    id: str
    channel_id: str
    message: str
    timestamp: datetime

