from unittest import TestCase, main

from project.mammal import Mammal


class TestMammal(TestCase):

    def setUp(self) -> None:
        self.mammal = Mammal("some name", "some type", "some sound")

    def test_correct_initializing(self):
        self.assertEqual("some name", self.mammal.name)
        self.assertEqual("some type", self.mammal.type)
        self.assertEqual("some sound", self.mammal.sound)

    def test_if_make_sound_returns_correct_message(self):
        self.assertEqual("some name makes some sound", self.mammal.make_sound())

    def test_if_get_kingdom_returns_correct_message(self):
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_if_info_returns_correct_message(self):
        self.assertEqual("some name is of type some type", self.mammal.info())

if __name__ == '__main__':
    main()
