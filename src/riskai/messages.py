from dataclasses import dataclass


@dataclass
class Observation:
    troops: list[int]
    ownership: list[int]
    cards: list[int]
    current_decision: int
    player_id: int
    turn_number: int


@dataclass
class Response:
    current_decision: int
    response: object


@dataclass
class InvalidResponseError:
    err_id: int
    custom_str: str = ""


errors = ["Error when placing territory"]
# the valid responses


@dataclass
class TroopPlacement:
    territory_id: int
