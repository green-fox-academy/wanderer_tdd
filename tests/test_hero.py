from models.hero import Hero

def test_hero_initialize():
    test_hero = Hero()
    assert test_hero.hp == 10
