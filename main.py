from model import GrassModel
from controller import GrassController
from view import GrassView
from common_types import *
from argparse import ArgumentParser

def args():
    parser = ArgumentParser("Scenario and Can", description="choose whick scenario and can to use")
    
    scenarios = parser.add_argument_group("Scenario")
    scenarios.add_argument("--mode", choices=["ac", "pvz", "sdv"], required=True)

    watering_cans = parser.add_argument_group("Watering Cans")
    watering_cans.add_argument("--water", choices=["basic", "steel", "koyuki", "bucket"], required=True)

    arg = parser.parse_args()
    arg_to_scenario: dict[str, type[Scenario]] = {"ac": AnimalCrossing, "pvz": PlantsVSZombies, "sdv": StardewValley}
    arg_to_can: dict[str, type[WateringCans]] = {"basic": BasicWateringCan, "steel": SteelCan, "koyuki": KuyukiCan, "bucket": WaterBucket}

    return arg_to_scenario[arg.mode], arg_to_can[arg.water]

if __name__ == "__main__":
    arg = args()
    model = GrassModel(arg[0](), arg[1])
    view = GrassView()
    controller = GrassController(model, view)
    controller.run()