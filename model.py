from common_types import Crop, WateringCans, Scenario

class GrassModel:
    def __init__(self, scenario: Scenario, watering_can: type[WateringCans]) -> None:
        self._pesos = scenario.initial_money
        self._row, self._col = scenario.grid_size
        self._day = 1
        self._grid: list[list[None | Crop]] = [[None for _ in range(self._col)] for _ in range(self._row)]
        self._watering_can = watering_can(*scenario.grid_size)
        self._scenario = scenario
    
    @property
    def day(self) -> int: 
        return self._day
    
    @property
    def grid(self) -> list[list[None | Crop]]:
        return self._grid
    
    @property
    def pesos(self) -> int:
        return self._pesos

    @property
    def str_crops(self) -> list[str]:
        return [x for x in self._scenario.crops_dict.keys()]
    
    def next_day(self) -> None:
        self._day += 1
        for row in self._grid:
            for cell in row:
                if cell is not None:
                    cell.progress()
        
    
    def in_range(self, r: int, c: int) -> bool:
        if 0 <= r < self._row and 0 <= c < self._col:
            return True
        else:
            return False
    
    def is_crop(self, crop: str) -> bool:
        if crop in self._scenario.crops_dict.keys():
            return True
        else:
            return False

    def have_money(self, crop: str) -> bool:
        crop_class = self._scenario.str_to_class(crop)()
        if self.pesos >= crop_class.cost:
            return True
        else:
            return False
    
    def already_planted(self, r: int, c: int) -> bool:
        if self._grid[r][c] is not None:
            return True
        else:
            return False
        
    def plant(self, crop: str, idx: tuple[int, int]) -> None:
        crop_class = self._scenario.str_to_class(crop)()
        self._grid[idx[0]][idx[1]] = crop_class
        self._pesos -= crop_class.cost
    
    def water(self, idx: tuple[int, int]) -> None:
        self._watering_can.use_can(self._grid, idx)

    def harvest(self) -> bool:
        has_harvested: bool = False
        for r in range(self._row):
            for c in range(self._col):
                curr_crop = self._grid[r][c]
                if curr_crop is not None and curr_crop.can_harvest():
                    self._pesos += curr_crop.harvest_val
                    self._grid[r][c] = None
                    has_harvested = True
                else:
                    continue
        return True if has_harvested else False

    




    

    