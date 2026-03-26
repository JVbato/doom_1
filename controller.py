from model import GrassModel
from view import GrassView
from common_types import *

class GrassController:
    def __init__(self, model: GrassModel, view: GrassView) -> None:
        self._model = model
        self._view = view
    
    def run(self) -> None:
        model = self._model
        view = self._view

        while True:
            print("=====")
            print()
            view.print_day(model.day)
            view.print_pesos(model.pesos)
            view.print_grid(model.grid)
            
            while True:
                print()
                action = view.choose_action()
                match action:
                    case action.PLANT:
                        view.print_plants(model.str_crops)
                        chosen_crop = view.choose_plant()
                        if model.is_crop(chosen_crop):
                            index = view.ask_idx()
                            if model.in_range(*index) and not model.already_planted(*index) and model.have_money(chosen_crop):
                                model.plant(chosen_crop, index)
                                view.print_success()
                            else:
                                view.print_failed()
                        else:
                            view.print_failed()
                    
                    case action.WATER:
                        index = view.ask_idx()
                        if model.in_range(*index):
                            model.water(index)
                            view.print_success()
                        else:
                            view.print_failed()
                    
                    case action.HARVEST:
                        if model.harvest():
                            view.print_success()
                        else:
                            view.print_failed()
                    
                    case action.GRID:
                        view.print_grid(model.grid)
                    
                    case action.NEXTDAY:
                        print("Day Ended.", end="\n\n")
                        model.next_day()
                        break
                                




                


            