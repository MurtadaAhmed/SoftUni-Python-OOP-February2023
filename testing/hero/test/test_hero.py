from unittest import TestCase, main

from project.hero import Hero


class TestHero(TestCase):
    def setUp(self) -> None:
        self.hero = Hero("Hero", 1, 100, 100)
        self.enemy = Hero("Enemy", 1, 50, 50)

    def test_correct_initialization(self):
        self.assertEqual("Hero", self.hero.username)
        self.assertEqual("Enemy", self.enemy.username)
        self.assertEqual(1, self.hero.level)
        self.assertEqual(1, self.enemy.level)
        self.assertEqual(100, self.hero.health)
        self.assertEqual(50, self.enemy.health)
        self.assertEqual(100, self.hero.damage)
        self.assertEqual(50, self.enemy.damage)

    def test_battle_with_oneself_raises_value_error(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_hero_zero_health_raises_value_error(self):
        self.hero.health = 0
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))


    def test_battle_enemy_zero_health_raises_value_error(self):
        self.enemy.health = 0
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy)
        self.assertEqual(f"You cannot fight Enemy. He needs to rest", str(ex.exception))


    def test_health_damage_take_when_result_is_draw(self):
        self.hero.health = self.enemy.health
        self.hero.damage = self.enemy.damage
        result = self.hero.battle(self.enemy)

        self.assertEqual(0, self.hero.health)
        self.assertEqual(0, self.enemy.health)
        self.assertEqual("Draw", result)

    def test_battle_win(self):
        result = self.hero.battle(self.enemy)
        self.assertEqual(2, self.hero.level)
        self.assertEqual(55, self.hero.health)
        self.assertEqual(105, self.hero.damage)
        self.assertEqual("You win", result)

    def test_battle_lose(self):
        self.hero, self.enemy = self.enemy, self.hero

        result = self.hero.battle(self.enemy)

        self.assertEqual(2, self.enemy.level)
        self.assertEqual(55, self.enemy.health)
        self.assertEqual(105, self.enemy.damage)
        self.assertEqual("You lose", result)


    def test_str_method(self):
        self.assertEqual(f"Hero Hero: 1 lvl\n"+
               f"Health: 100\n"+
               f"Damage: 100\n", str(self.hero))


if __name__ == "__main__":
    main()
