from models.hero import Hero
from models.dice import Dice
from config import hero as hero_config

def test_hero_initialize():
    test_dice = Dice([0])
    test_hero = Hero(test_dice)

    assert test_hero.hp == hero_config.BASE_HP
    assert test_hero.sp == hero_config.BASE_SP
    assert test_hero.dp == 0