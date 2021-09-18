import main

def test_get_fish_type():
    assert main.get_fish_type(301, 25, 25) == main.FishType.JeffFish
    assert main.get_fish_type(300,19,4) == main.FishType.Shark
    assert main.get_fish_type(300,0,25) == main.FishType.SwordFish
    assert main.get_fish_type(300,25,2) == main.FishType.SophonFish