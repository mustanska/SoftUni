from unittest import TestCase, main
from project.team import Team

class TestTeam(TestCase):
    def setUp(self) -> None:
        self.team = Team("Name")

    def test_initialize_team(self):
        self.assertEqual("Name", self.team.name)
        self.assertEqual({}, self.team.members)

    def test_set_name_with_value_contains_different_symbols_not_only_letters_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.team.name = "Best Team"

        self.assertEqual("Team Name can contain only letters!", str(ve.exception))

    def test_add_and_remove_member_to_team(self):
        result = self.team.add_member()
        self.assertEqual("Successfully added: ", result)
        self.assertEqual(0, len(self.team))

        result = self.team.add_member(member1=15)
        self.assertEqual("Successfully added: member1", result)
        self.assertEqual({"member1": 15}, self.team.members)
        self.assertEqual(1, len(self.team))

        result = self.team.add_member(member1=20, member2=20, member3=25)
        self.assertEqual("Successfully added: member2, member3", result)
        self.assertEqual({"member1": 15, "member2": 20, "member3": 25}, self.team.members)
        self.assertEqual(3, len(self.team))

        result = self.team.remove_member("member2")
        self.assertEqual("Member member2 removed", result)
        self.assertEqual({"member1": 15, "member3": 25}, self.team.members)
        self.assertEqual(2, len(self.team))

        result = self.team.remove_member("member4")
        self.assertEqual("Member with name member4 does not exist", result)
        self.assertEqual({"member1": 15, "member3": 25}, self.team.members)
        self.assertEqual(2, len(self.team))

    def test_greater_than(self):
        other = Team("Other")
        result = self.team > other
        self.assertEqual(False, result)

        other.add_member(other_member1=20)
        result = self.team > other
        self.assertEqual(False, result)

        self.team.add_member(member1=15, member2=25)
        result = self.team > other
        self.assertEqual(True, result)

    def test_add(self):
        other = Team("Other")
        new_team = self.team + other
        self.assertEqual("NameOther", new_team.name)
        self.assertEqual({}, new_team.members)

        self.team.add_member(member=15)
        other.add_member(other_member=20)
        new_team = self.team + other
        self.assertEqual("NameOther", new_team.name)
        self.assertEqual({"member": 15, "other_member": 20}, new_team.members)

    def test_string_represent_team(self):
        self.assertEqual("Team name: Name", str(self.team))

        self.team.add_member(member1=15, member2=20, member3=20)
        expected = "Team name: Name\nMember: member2 - 20-years old\nMember: member3 - 20-years old\nMember: member1 - 15-years old"
        self.assertEqual(expected, str(self.team))


if __name__ == "__main__":
    main()