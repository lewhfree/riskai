from dataclasses import dataclass


@dataclass
class Observation:
    troops: list[int]
    ownership: list[int]
    cards: list[int]
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


@dataclass
class Attack:
    do_attack: bool
    from_territory_id: int = -1
    to_territory_id: int = -1
    troops: int = -1
