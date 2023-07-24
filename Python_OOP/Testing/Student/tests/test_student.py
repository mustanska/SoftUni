from unittest import TestCase, main

from project.student import Student


class TestStudent(TestCase):
    def setUp(self) -> None:
        self.student_without_courses = Student("Ivan")
        self.student_with_courses = Student("Maria", {"OOP": ["inheritance"]})

    def test_initialize_student(self):
        self.assertEqual("Ivan", self.student_without_courses.name)
        self.assertEqual({}, self.student_without_courses.courses)
        self.assertEqual({"OOP": ["inheritance"]}, self.student_with_courses.courses)

    def test_enroll_course_existed_in_courses(self):
        result = self.student_with_courses.enroll("OOP", ["encapsulate"])
        self.assertEqual(["inheritance", "encapsulate"], self.student_with_courses.courses["OOP"])
        self.assertEqual("Course already added. Notes have been updated.", result)

    def test_enroll_add_course_notes_in_not_existed_course_with_y_param(self):
        result = self.student_with_courses.enroll("DataBase", ["MySQL"], "Y")
        expected = {"OOP": ["inheritance"], "DataBase": ["MySQL"]}
        self.assertEqual(expected, self.student_with_courses.courses)
        self.assertEqual("Course and course notes have been added.", result)

    def test_enroll_add_course_notes_in_not_existed_course_with_empty_param(self):
        result = self.student_with_courses.enroll("DataBase", ["MySQL"], "")
        expected = {"OOP": ["inheritance"], "DataBase": ["MySQL"]}
        self.assertEqual(expected, self.student_with_courses.courses)
        self.assertEqual("Course and course notes have been added.", result)


    def test_enroll_add_not_existed_course_without_notes(self):
        result = self.student_without_courses.enroll("DataBase", ["MySQL"], "n")
        self.assertEqual({"DataBase": []}, self.student_without_courses.courses)
        self.assertEqual("Course has been added.", result)

    def test_add_notes_to_not_existed_course_raises(self):
        with self.assertRaises(Exception) as ex:
            self.student_without_courses.add_notes("OOP", "encapsulate")

        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_add_notes_to_existed_course(self):
        result = self.student_with_courses.add_notes("OOP", "encapsulate")
        self.assertEqual({"OOP": ["inheritance", "encapsulate"]}, self.student_with_courses.courses)
        self.assertEqual("Notes have been updated", result)

    def test_leave_not_existed_course_raises(self):
        with self.assertRaises(Exception) as ex:
            self.student_without_courses.leave_course("OOP")

        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))

    def test_leave_existed_course(self):
        result = self.student_with_courses.leave_course("OOP")
        self.assertEqual({}, self.student_with_courses.courses)
        self.assertEqual("Course has been removed", result)

if __name__ == "__main__":
    main()