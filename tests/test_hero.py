from models.hero import Hero
from config import hero as hero_config

def test_hero_initialize():
    test_hero = Hero()
    assert test_hero.hp == hero_config.BASE_HP
