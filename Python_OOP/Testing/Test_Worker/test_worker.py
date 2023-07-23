import unittest

from Testing.Test_Worker.worker import Worker


class WorkerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.worker = Worker("Test", 1000, 50)

    def test_initialize_worker(self):
        self.assertEqual("Test", self.worker.name)
        self.assertEqual(1000, self.worker.salary)
        self.assertEqual(50, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_work_raises(self):
        self.worker.energy = 0

        with self.assertRaises(Exception) as ex:
            self.worker.work()

        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_work(self):
        self.assertEqual(50, self.worker.energy)
        self.assertEqual(0, self.worker.money)

        self.worker.work()
        self.assertEqual(50 - 1, self.worker.energy)
        self.assertEqual(1000, self.worker.money)

        self.worker.work()
        self.assertEqual(50 - 2, self.worker.energy)
        self.assertEqual(2000, self.worker.money)

    def test_rest(self):
        self.assertEqual(50, self.worker.energy)

        self.worker.rest()

        self.assertEqual(50 + 1, self.worker.energy)

    def test_get_info(self):
        result = self.worker.get_info()
        self.assertEqual('Test has saved 0 money.', result)

        self.worker.work()
        result = self.worker.get_info()
        self.assertEqual('Test has saved 1000 money.', result)


if __name__ == "__main__":
    unittest.main()
