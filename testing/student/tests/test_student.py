from unittest import TestCase, main

from project.student import Student


class TestStudent(TestCase):
    def setUp(self) -> None:
        self.student1 = Student("Name1")  # without courses
        self.student2 = Student("Name2", {"course_name": ["note"]})  # with courses

    def test_initializing(self):
        self.assertEqual("Name1", self.student1.name)
        self.assertEqual({}, self.student1.courses)
        self.assertEqual({"course_name": ["note"]}, self.student2.courses)

    def test_add_notes_to_existing_course(self):
        result = self.student2.enroll("course_name", ["note2"])
        self.assertEqual("note2", self.student2.courses["course_name"][1])
        self.assertEqual("Course already added. Notes have been updated.", result)

    def test_add_notes_to_non_existing_course_without_third_parameter(self):
        result = self.student1.enroll("non_exit_course", ["note2"])
        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual("note2", self.student1.courses["non_exit_course"][0])

    def test_add_notes_to_non_existing_course_with_third_parameter(self):
        result = self.student1.enroll("non_exit_course", ["note2"], "Y")
        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual("note2", self.student1.courses["non_exit_course"][0])


    def test_add_new_course_without_adding_notes(self):
        result = self.student1.enroll("non_exit_course", ["note2"], "third_parameter")
        self.assertEqual("Course has been added.", result)
        self.assertEqual(0, len(self.student1.courses["non_exit_course"]))

    def test_add_notes_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student1.add_notes("some_course", "note")
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_add_notes_successfully(self):
        result = self.student2.add_notes("course_name", "new_note")
        self.assertEqual("new_note", self.student2.courses["course_name"][1])
        self.assertEqual("Notes have been updated", result)

    def test_leave_course_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student1.leave_course("some_course")
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))

    def test_leave_course_successfully(self):
        result = self.student2.leave_course("course_name")
        self.assertEqual("Course has been removed", result)
        self.assertEqual(0, len(self.student2.courses))
if __name__ == "__main__":
    main()
