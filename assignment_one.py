from enum import Enum


class FishType(Enum):
    GoldFish = 0
    SwordFish = 1
    Shark = 2
    SophonFish = 3
    JeffFish = 4


def get_fish_type(scale_count: int, fin_count: int, head_count: int):
    if scale_count > 300:
        # JeffFish is the only fish with 300+ scales
        return FishType.JeffFish

    if fin_count < 20:
        if head_count == 4:
            return FishType.Shark

    if fin_count == None:
        return FishType.SwordFish

    if head_count % 2 == 0:
        return FishType.SophonFish
