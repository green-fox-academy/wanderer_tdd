from models.dice import Dice

def test_dice_initialize():
    test_dice = Dice([0])
    assert test_dice.roll() == 0