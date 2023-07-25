from unittest import TestCase, main
from project.student_report_card import StudentReportCard

class TestStudentReportCard(TestCase):
    def setUp(self) -> None:
        self.student_report_card = StudentReportCard("Student", 11)

    def test_initialize_student_report_card(self):
        self.assertEqual("Student", self.student_report_card.student_name)
        self.assertEqual(11, self.student_report_card.school_year)
        self.assertEqual({}, self.student_report_card.grades_by_subject)
    def test_student_name_is_empty_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.student_report_card.student_name = ""

        self.assertEqual("Student Name cannot be an empty string!", str(ve.exception))

    def test_add_first_school_year_successfully(self):
        self.student_report_card.school_year = 1
        self.assertEqual(1, self.student_report_card.school_year)

    def test_add_last_school_year_successfully(self):
        self.student_report_card.school_year = 12
        self.assertEqual(12, self.student_report_card.school_year)

    def test_school_year_is_less_than_one_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.student_report_card.school_year = 0

        self.assertEqual("School Year must be between 1 and 12!", str(ve.exception))

    def test_school_year_is_more_than_twenty_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.student_report_card.school_year = 13

        self.assertEqual("School Year must be between 1 and 12!", str(ve.exception))

    def test_add_grade_to_student_card_not_existing_subject(self):
        self.student_report_card.add_grade("math", 5)
        self.assertEqual([5], self.student_report_card.grades_by_subject["math"])

    def test_add_grade_to_student_card_with_existing_subject(self):
        self.student_report_card.grades_by_subject["math"] = [6]
        self.student_report_card.add_grade("math", 5)
        self.assertEqual([6, 5], self.student_report_card.grades_by_subject["math"])

    def test_average_grade_by_subject_to_student_without_subjects(self):
        result = self.student_report_card.average_grade_by_subject()
        self.assertEqual("", result)

    def test_average_grade_by_subject_to_student_with_subject(self):
        self.student_report_card.grades_by_subject["math"] = [6]
        result = self.student_report_card.average_grade_by_subject()
        self.assertEqual("math: 6.00", result)

    def test_average_grade_by_subject_to_student_with_subjects(self):
        self.student_report_card.grades_by_subject = {"math": [6, 5], "biology": [4.25, 5.20]}
        result = self.student_report_card.average_grade_by_subject()
        self.assertEqual("math: 5.50\nbiology: 4.72", result)

    def test_average_grade_for_none_subjects_to_student_raises(self):
        with self.assertRaises(ZeroDivisionError):
            self.student_report_card.average_grade_for_all_subjects()

    def test_average_grade_for_all_subjects_to_student(self):
        self.student_report_card.grades_by_subject = {"math": [6, 5], "biology": [4.25, 5.20]}
        result = self.student_report_card.average_grade_for_all_subjects()
        self.assertEqual("Average Grade: 5.11", result)

    def test_represent_student_report_card_raises(self):
        with self.assertRaises(ZeroDivisionError):
            self.student_report_card.average_grade_for_all_subjects()

    def test_represent_student_report_card(self):
        self.student_report_card.grades_by_subject = {"math": [6, 5], "biology": [4, 5]}

        expected = "Name: Student\n" \
                "Year: 11\n" \
                "----------\n" \
                "math: 5.50\nbiology: 4.50\n" \
                "----------\n" \
                "Average Grade: 5.00"

        self.assertEqual(expected, str(self.student_report_card))


if __name__ == "__main__":
    main()