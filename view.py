from common_types import Crop, Mechanics

class GrassView:
    def print_day(self, day: int) -> None:
        print(f"Day {day}")
    
    def print_pesos(self, pesos: int) -> None:
        print(f"Pesos: {pesos}")
    
    def print_grid(self, grid: list[list[None | Crop]]):
        for row in grid:
            print("".join(["." if cell is None else cell.__str__() for cell in row]))
        print()

    def choose_action(self) -> Mechanics:
        while True:
            print("Action: ")
            str_to_mech: dict[str, Mechanics] = {"p": Mechanics.PLANT, "w": Mechanics.WATER, "h": Mechanics.HARVEST, "g": Mechanics.GRID, "n": Mechanics.NEXTDAY}
            move = input("- ").lower()
            if move not in str_to_mech.keys():
                self.print_failed()
                print()
                continue
            else:
                return str_to_mech[move]
    
    def choose_plant(self) -> str:
        return input("- ").strip().lower()
    
    def print_plants(self, available_plants: list[str]):
        print("Crops: ", end="")
        print(*available_plants, sep=", ")

    def ask_idx(self) -> tuple[int, int]:
        print("Location (i j): ")
        index = tuple(input("- ").strip().split(" ")[0:2])
        if len(index) < 2:
            return -1, -1
        r, c = tuple(int(num) for num in index)
        return r, c
    
    def print_failed(self) -> None:
        print("Failed.")
    
    def print_success(self) -> None:
        print("Success!")

    
            