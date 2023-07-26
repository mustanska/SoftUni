from unittest import TestCase, main
from project.movie import Movie

class TestMovie(TestCase):
    def setUp(self) -> None:
        self.movie = Movie("Stars", 1997, 9.9)
        self.other_movie = Movie("Test", 2010, 7.3)

    def test_initialize_movie_instance(self):
        self.assertEqual("Stars", self.movie.name)
        self.assertEqual(1997, self.movie.year)
        self.assertEqual(9.9, self.movie.rating)
        self.assertEqual([], self.movie.actors)

    def test_set_name_to_movie_with_empty_value_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.movie.name = ""

        self.assertEqual("Name cannot be an empty string!", str(ve.exception))

    def test_set_name_to_movie(self):
        self.movie.name = "New"
        self.assertEqual("New", self.movie.name)

    def test_set_year_to_movie_before_1887_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.movie.year = 1886

        self.assertEqual("Year is not valid!", str(ve.exception))

    def test_set_year_to_movie(self):
        self.movie.year = 1887
        self.assertEqual(1887, self.movie.year)

    def test_add_actor_to_movie_if_name_does_not_exist(self):
        self.movie.add_actor("Hilary Duff")
        self.assertEqual(["Hilary Duff"], self.movie.actors)

    def test_add_actor_to_movie_if_name_exist(self):
        self.movie.actors = ["Hilary Duff"]
        result = self.movie.add_actor("Hilary Duff")
        self.assertEqual("Hilary Duff is already added in the list of actors!", result)

    def test_existing_movie_is_better_than_other(self):
        result = self.movie > self.other_movie
        self.assertEqual('"Stars" is better than "Test"', result)

    def test_existing_movie_is_equal_than_other(self):
        self.movie.rating = 7.3
        result = self.movie > self.other_movie
        self.assertEqual('"Test" is better than "Stars"', result)

    def test_other_movie_is_better_than_existing(self):
        self.other_movie.rating = 10
        result = self.movie > self.other_movie
        self.assertEqual('"Test" is better than "Stars"', result)

    def test_represent_movie_without_actors(self):
        expected = "Name: Stars\n" \
               "Year of Release: 1997\n" \
               "Rating: 9.90\n" \
               "Cast: "

        self.assertEqual(expected, str(self.movie))

    def test_represent_movie_with_actors(self):
        self.movie.actors = ["Hilary Duff", "Brad Pitt"]
        expected = "Name: Stars\n" \
               "Year of Release: 1997\n" \
               "Rating: 9.90\n" \
               "Cast: Hilary Duff, Brad Pitt"

        self.assertEqual(expected, str(self.movie))

if __name__ == "__main__":
    main()