from unittest import TestCase, main

from project.hero import Hero


class TestHero(TestCase):
    def setUp(self) -> None:
        self.hero = Hero("Hero", 1, 50.0, 20.5)
        self.enemy = Hero("Enemy", 1, 100.0, 20.0)

    def test_initialize_hero(self):
        self.assertEqual("Hero", self.hero.username)
        self.assertEqual(1, self.hero.level)
        self.assertEqual(50.0, self.hero.health)
        self.assertEqual(20.5, self.hero.damage)

    def test_battle_the_same_hero_and_enemy_raises(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)

        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_hero_health_is_equal_or_less_than_zero_raises(self):
        self.hero.health = 0

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ve.exception))

        self.hero.health = -1

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ve.exception))

    def test_battle_enemy_health_is_equal_or_less_than_zero_raises(self):
        self.enemy.health = 0

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)

        self.assertEqual("You cannot fight Enemy. He needs to rest", str(ve.exception))

        self.enemy.health = -1

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)

        self.assertEqual("You cannot fight Enemy. He needs to rest", str(ve.exception))

    def test_battle_result_draw_between_hero_and_enemy(self):
        self.hero.damage = 100
        self.enemy.damage = 50
        result = self.hero.battle(self.enemy)
        self.assertEqual("Draw", result)

    def test_battle_result_hero_is_winner_and_enemy_is_loser(self):
        self.hero.damage = 100
        result = self.hero.battle(self.enemy)
        self.assertEqual(2, self.hero.level)
        self.assertEqual(35, self.hero.health)
        self.assertEqual(105, self.hero.damage)
        self.assertEqual("You win", result)

    def test_battle_result_enemy_is_winner_and_hero_is_loser(self):
        result = self.hero.battle(self.enemy)
        self.assertEqual(2, self.enemy.level)
        self.assertEqual(84.5, self.enemy.health)
        self.assertEqual(25, self.enemy.damage)
        self.assertEqual("You lose", result)

    def test_str_represent_class_hero_instance(self):
        expected = "Hero Hero: 1 lvl\n" \
                "Health: 50.0\n" \
                f"Damage: 20.5\n"
        self.assertEqual(expected, str(self.hero))

if __name__ == "__main__":
    main()