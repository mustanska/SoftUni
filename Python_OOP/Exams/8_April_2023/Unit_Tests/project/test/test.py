from unittest import TestCase, main
from project.tennis_player import TennisPlayer

class TestTennisPlayer(TestCase):
    def setUp(self) -> None:
        self.tennis_player = TennisPlayer("Name", 18, 10)

    def test_initialize_tennis_player(self):
        self.assertEqual("Name", self.tennis_player.name)
        self.assertEqual(18, self.tennis_player.age)
        self.assertEqual(10, self.tennis_player.points)
        self.assertEqual([], self.tennis_player.wins)

    def test_set_name_to_tennis_player_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.tennis_player.name = "Na"

        self.assertEqual("Name should be more than 2 symbols!", str(ve.exception))

    def test_set_age_to_tennis_player_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.tennis_player.age = 17

        self.assertEqual("Players must be at least 18 years of age!", str(ve.exception))

    def test_add_new_win(self):
        self.tennis_player.add_new_win("Tournament")
        self.assertEqual(["Tournament"], self.tennis_player.wins)

        result = self.tennis_player.add_new_win("Tournament")
        self.assertEqual(["Tournament"], self.tennis_player.wins)
        self.assertEqual("Tournament has been already added to the list of wins!", result)

    def test_less_than(self):
        other = TennisPlayer("Other", 20, 9)
        result = self.tennis_player < other
        self.assertEqual("Name is a better player than Other", result)

        other.points = 11
        result = self.tennis_player < other
        self.assertEqual("Other is a top seeded player and he/she is better than Name", result)

    def test_string_represent_tennis_player(self):
        expected = "Tennis Player: Name\n" \
               "Age: 18\n" \
               f"Points: 10.0\n" \
               f"Tournaments won: "
        self.assertEqual(expected, str(self.tennis_player))

        self.tennis_player.add_new_win("Tournament1")
        expected = "Tennis Player: Name\n" \
                   "Age: 18\n" \
                   f"Points: 10.0\n" \
                   f"Tournaments won: Tournament1"
        self.assertEqual(expected, str(self.tennis_player))

        self.tennis_player.add_new_win("Tournament2")
        expected = "Tennis Player: Name\n" \
                   "Age: 18\n" \
                   f"Points: 10.0\n" \
                   f"Tournaments won: Tournament1, Tournament2"
        self.assertEqual(expected, str(self.tennis_player))

if __name__ == "__main__":
    main()
    