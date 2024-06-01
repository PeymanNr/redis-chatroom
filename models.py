from dataclasses import dataclass


@dataclass
class User:
    id: str
    username: str


@dataclass
class Channel:
    id: str
    name: str

