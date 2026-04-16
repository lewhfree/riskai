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
    
# the valid responses

@dataclass
class TroopPlacement:
    territory_id:int
