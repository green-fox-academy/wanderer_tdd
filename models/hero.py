from config import hero as hero_config

class Hero:
    
    def __init__(self, dice):
        self.dice = dice
        self.hp = hero_config.BASE_HP + 3 * dice.roll()
        self.sp = hero_config.BASE_SP + dice.roll()
        self.dp = 2 * dice.roll()
