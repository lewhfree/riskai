import riskai.players.player_class as player_class
import riskai.messages as m
from riskai.utils import inputs
from riskai.decisions import Stages


class User(player_class.PlayerTemplate):
    def decision(
        self, observation: m.Observation, phase: Stages
    ) -> m.Response:
        print(observation)
        match phase:
            # =================================================================
            # =================================================================
            case Stages.TREATY:
                level = input(
                    "Which Treaty level (LEVEL1, LEVEL2, LEVEL3, WAR, NONE)? "
                )
                level = m.TreatyLevels[level]
                person = inputs.int_input("Which person to attack? ")
                response = m.Response(
                    Stages.TREATY, m.Treaty(level=level, person=person)
                )
                return response
            # =================================================================
            # =================================================================
            case Stages.CARDS:
                print("cards")
                pass
            # =================================================================
            # =================================================================
            case Stages.REINFORCE | Stages.INITIAL_PLACEMENT:
                territory_num = inputs.int_input("Where to place a troop? ")
                response = m.Response(
                    Stages.REINFORCE,
                    m.TroopPlacement(territory_id=territory_num),
                )
                return response
            # =================================================================
            # =================================================================
            case Stages.ATTACK_DECLARATION:
                shouldAttack = inputs.bool_input("Attack (True/False)? ")
                if not shouldAttack:
                    return m.Response(
                        Stages.ATTACK_DECLARATION, m.Attack(do_attack=False)
                    )
                from_territory = inputs.int_input("Origin territory id? ")
                target_territory = inputs.int_input("Target territory id? ")
                troops = inputs.int_input("How many troops? ")

                response = m.Response(
                    Stages.ATTACK_DECLARATION,
                    m.Attack(
                        do_attack=True,
                        from_territory_id=from_territory,
                        to_territory_id=target_territory,
                        troops=troops,
                    ),
                )
                return response
            # =================================================================
            # =================================================================
            case Stages.RETREAT:
                shouldRetreat = inputs.bool_input("Retreat (True/False)? ")
                return m.Response(
                    Stages.RETREAT, m.Retreat(retreat=shouldRetreat)
                )
            # =================================================================
            # =================================================================
            case Stages.FORTIFY:
                fortifyq = inputs.bool_input(
                    "Should fortify stage (True/False)? "
                )
                if not fortifyq:
                    return m.Response(
                        Stages.FORTIFY, m.Fortify(do_reinforce=False)
                    )
                origin = inputs.int_input("Origin territory id? ")
                target = inputs.int_input("Target territory ID? ")
                troops = inputs.int_input("troop count? ")

                response = m.Response(
                    Stages.FORTIFY, m.Fortify(True, origin, target, troops)
                )
                return response
            # =================================================================
            # =================================================================
            case _:
                exit("not implemented")
        return m.Response(-1, None)
