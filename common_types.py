from typing import Protocol
from enum import Enum, auto

class Mechanics(Enum):
    WATER = auto()
    PLANT = auto()
    HARVEST = auto()
    GRID = auto()
    NEXTDAY = auto()

class CropEnum(Protocol):
    key: object
    val: str

class WateringCans(Protocol):
    def __init__(self, r: int, c: int) -> None:
        ...
        
    def use_can(self, plants: list[list[Crop | None]], idx: tuple[int, int]):
        ...

class BasicWateringCan:
    def __init__(self, r: int, c: int) -> None:
        self._row = r
        self._col = c

    def use_can(self, plants: list[list[Crop | None]], idx: tuple[int, int]):
        crop = plants[idx[0]][idx[1]]
        if crop is not None:
           crop.water_plant()

class Crop(Protocol):
    def __str__(self) -> str:
        ...
    
    @property
    def cost(self) -> int:
        ...
    
    @property
    def harvest_val(self) -> int:
        ...

    def water_plant(self):
        ...
    
    def can_harvest(self) -> bool:
        ...
    
    def progress(self):
        ...

class Turnip:
    def __init__(self) -> None:
        self._cost: int = 300
        self._growth_time: int = 2
        self._harvest_val: int = 500
        self._watered: bool = False

    def __str__(self) -> str:
        if self._growth_time > 0:
            return "t"
        else:
            return "T"
    
    @property
    def cost(self) -> int:
        return self._cost
    
    @property
    def harvest_val(self) -> int:
        return self._harvest_val
    
    def can_harvest(self) -> bool:
        if self._growth_time <= 0:
            return True
        else:
            return False
    
    def water_plant(self):
        self._watered = True
    
    def progress(self):
        if self._watered:
            self._growth_time -= 1
            self._watered = False

class Sunflower:
    def __init__(self) -> None:
        self._cost: int = 25
        self._growth_time: int = 1
        self._harvest_val: int = 50
        self._watered: bool = False

    def __str__(self) -> str:
        if self._growth_time > 0:
            return "s"
        else:
            return "S"
    
    @property
    def cost(self) -> int:
        return self._cost
    
    @property
    def harvest_val(self) -> int:
        return self._harvest_val
    
    def can_harvest(self) -> bool:
        if self._growth_time <= 0:
            return True
        else:
            return False
    
    def water_plant(self):
        self._watered = True
    
    def progress(self):
        if self._watered:
            self._watered = False
            self._growth_time -= 1

class Marygold:
    def __init__(self) -> None:
        self._cost: int = 50
        self._growth_time: int = 2
        self._harvest_val: int = 150
        self._watered: bool = False

    def __str__(self) -> str:
        if self._growth_time > 0:
            return "m"
        else:
            return "M"
    
    @property
    def cost(self) -> int:
        return self._cost
    
    @property
    def harvest_val(self) -> int:
        return self._harvest_val
    
    def can_harvest(self) -> bool:
        if self._growth_time <= 0:
            return True
        else:
            return False
    
    def water_plant(self):
        self._watered = True
    
    def progress(self):
        if self._watered:
            self._watered = False
            self._growth_time -= 1
    
class Scenario(Protocol):
    @property
    def crops_dict(self) -> dict[str, type[Crop]]:
        ...
    
    @property
    def initial_money(self) -> int:
        ...
    
    @property
    def grid_size(self) -> tuple[int, int]:
        ...

    def str_to_class(self, crop: str) -> type[Crop]:
        ...

class AnimalCrossing:
    def __init__(self) -> None:
        self._class_dict: dict[str, type[Crop]] = {"turnip": Turnip}
        self._initial_pesos: int = 1000
        self._grid_size: tuple[int, int] = (5, 5)
    
    @property
    def crops_dict(self) -> dict[str, type[Crop]]:
        return self._class_dict
    
    @property
    def initial_money(self) -> int:
        return self._initial_pesos
    
    @property
    def grid_size(self) -> tuple[int, int]:
        return self._grid_size
    
    def str_to_class(self, crop: str) -> type[Crop]:
        return self._class_dict[crop]

class PlantsVSZombies:
    def __init__(self) -> None:
        self._class_dict: dict[str, type[Crop]] = {"sunflower": Sunflower, "marygold": Marygold}
        self._initial_pesos: int = 100
        self._grid_size: tuple[int, int] = (6, 9)
    
    @property
    def crops_dict(self) -> dict[str, type[Crop]]:
        return self._class_dict
    
    @property
    def initial_money(self) -> int:
        return self._initial_pesos
    
    @property
    def grid_size(self) -> tuple[int, int]:
        return self._grid_size
    
    def str_to_class(self, crop: str) -> type[Crop]:
        return self._class_dict[crop]

class SteelCan:
    def __init__(self, r: int, c: int) -> None:
        self._row = r
        self._col = c

    def use_can(self, plants: list[list[Crop | None]], idx: tuple[int, int]):
        def in_range(r: int, c: int) -> bool:
            if 0 <= r < self._row and 0 <= c < self._col:
                return True
            else:
                return False
        
        adder: set[int] = {-1, 0, 1}
        for r in adder:
            for c in adder:
                if in_range(idx[0] + r, idx[1] + c):
                    crop = plants[idx[0] + r][idx[1] + c]
                    if crop:
                        crop.water_plant()

class WaterBucket:
    def __init__(self, r: int, c: int) -> None:
        self._row = r
        self._col = c

    def use_can(self, plants: list[list[Crop | None]], idx: tuple[int, int]):
        def in_range(r: int, c: int) -> bool:
            if 0 <= r < self._row and 0 <= c < self._col:
                return True
            else:
                return False
        directions = {(-1, 0), (1, 0), (0, -1), (0, 1)}

        current: list[tuple[int, int]] = [idx]
        visited: set[tuple[int, int]] = {idx}

        while current:
            curr_idx = current.pop()
            
            pp = plants[curr_idx[0]][curr_idx[1]]
            if pp:
                pp.water_plant()
            
            for r, c in directions:
                if in_range(curr_idx[0] + r, curr_idx[1] + c) and (curr_idx[0] + r, curr_idx[1] + c) not in visited:
                    curr_plant = plants[curr_idx[0] + r][curr_idx[1] + c]
                    if curr_plant:
                        current.append((curr_idx[0] + r, curr_idx[1] + c))
                        visited.add((curr_idx[0] + r, curr_idx[1] + c))
                    
class KuyukiCan:
    def __init__(self, r: int, c: int) -> None:
        self._row = r
        self._col = c
    
    def use_can(self, plants: list[list[Crop | None]], idx: tuple[int, int]): 
        def in_range(r: int, c: int) -> bool: 
            if 0 <= r < self._row and 0 <= c < self._col: 
                return True 
            else: 
                return False 
        for r in range(self._row): 
            for c in range(self._col): 
                if abs(idx[0] - r) + abs(idx[1] - c) <= 4 and in_range(r, c): 
                    curr_crop = plants[r][c] 
                    if curr_crop: 
                        curr_crop.water_plant()
                    



class StardewValley:
    def __init__(self) -> None:
        self._class_dict: dict[str, type[Crop]] = {"parsnip": Parsnip, "ancientfruit": AncientFruit, "sweetgemberry": SweetGemBerry}
        self._initial_pesos: int = 400
        self._grid_size: tuple[int, int] = (9, 9)
    
    @property
    def crops_dict(self) -> dict[str, type[Crop]]:
        return self._class_dict
    
    @property
    def initial_money(self) -> int:
        return self._initial_pesos
    
    @property
    def grid_size(self) -> tuple[int, int]:
        return self._grid_size
    
    def str_to_class(self, crop: str) -> type[Crop]:
        return self._class_dict[crop]


class Parsnip:
    def __init__(self) -> None:
        self._cost: int = 100
        self._growth_time: int = 1
        self._harvest_val: int = 200
        self._watered: bool = False

    def __str__(self) -> str:
        if self._growth_time > 0:
            return "p"
        else:
            return "P"
    
    @property
    def cost(self) -> int:
        return self._cost
    
    @property
    def harvest_val(self) -> int:
        return self._harvest_val
    
    def can_harvest(self) -> bool:
        if self._growth_time <= 0:
            return True
        else:
            return False
    
    def water_plant(self):
        self._watered = True
    
    def progress(self):
        if self._watered:
            self._watered = False
            self._growth_time -= 1

class SweetGemBerry:
    def __init__(self) -> None:
        self._cost: int = 300
        self._growth_time: int = 3
        self._harvest_val: int = 1000
        self._watered: bool = False
        self._was_watered: bool = False

    def __str__(self) -> str:
        if self._growth_time > 0:
            return "g"
        else:
            return "G"
    
    @property
    def cost(self) -> int:
        return self._cost
    
    @property
    def harvest_val(self) -> int:
        return self._harvest_val
    
    def can_harvest(self) -> bool:
        if self._growth_time <= 0:
            return True
        else:
            return False
    
    def water_plant(self):
        self._watered = True
    
    def progress(self):
        if self._watered:
            self._was_watered = True
            self._watered = False
            if self._was_watered:
                self._growth_time -= 1  
        else:
            self._was_watered = False


class AncientFruit:
    def __init__(self) -> None:
        self._cost: int = 1000
        self._growth_time: int = 14
        self._harvest_val: int = 6700
        self._watered: bool = False
        self._streak: int = 0

    def __str__(self) -> str:
        if self._growth_time > 0:
            return "a"
        else:
            return "A"
    
    @property
    def cost(self) -> int:
        return self._cost
    
    @property
    def harvest_val(self) -> int:
        return self._harvest_val
    
    def can_harvest(self) -> bool:
        if self._growth_time <= 0:
            return True
        else:
            return False
    
    def water_plant(self):
        self._watered = True
    
    def progress(self):
        if self._watered:
            self._streak += 1
            self._watered = False
            self._growth_time -= self._streak  
        else:
            self._streak = 0

