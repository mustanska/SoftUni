from unittest import TestCase, main

from project.mammal import Mammal


class TestMammal(TestCase):
    def setUp(self) -> None:
        self.mammal = Mammal("Kitty", "cat", "meow")

    def test_initialize_mammal(self):
        self.assertEqual("Kitty", self.mammal.name)
        self.assertEqual("cat", self.mammal.type)
        self.assertEqual("meow", self.mammal.sound)
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test_make_sound_mammal(self):
        result = self.mammal.make_sound()

        self.assertEqual("Kitty makes meow", result)

    def test_get_kingdom(self):
        result = self.mammal.get_kingdom()

        self.assertEqual("animals", result)

    def test_info(self):
        result = self.mammal.info()

        self.assertEqual("Kitty is of type cat", result)

        
if __name__ == "__main__":
    main()