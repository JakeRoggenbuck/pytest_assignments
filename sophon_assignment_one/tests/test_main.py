from main import FishType, get_fish_type

def test_get_fish_type():
    cases = (
        ((301, 0, 0), FishType.JeffFish),
        ((200, 15, 4), FishType.Shark),
        ((200, 0, 23423425), FishType.SwordFish),
        ((123, 123, 200), FishType.SophonFish)
    )

    for case in cases:
        assert get_fish_type(*case[0]) == case[1]
