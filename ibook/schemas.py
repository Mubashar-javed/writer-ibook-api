import dataclasses
from dataclasses import dataclass


@dataclass
class Pronunciation:
    all: str


@dataclass
class Result:
    definition: str
    part_of_speech: str
    synonyms: list[str]
    type_of: list[str]
    has_types: list[str] | None = None
    derivation: list[str] | None = None
    examples: list[str] | None = None


@dataclass
class Syllables:
    count: int
    list: list[str]


@dataclass
class RapidAPIResponse:
    word: str
    results: list[Result] | None = None
    syllables: Syllables | None = None
    pronunciation: Pronunciation | None = None
    frequency: float = 0.0

    def as_dict(self) -> dict:
        return dataclasses.asdict(self)
