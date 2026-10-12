"""Unit tests for Student Performance Analytics functions.

Uses Python standard library unittest to verify calculation accuracy,
grading policy boundaries, pass/fail rules, and input data validation.
"""

import unittest
from pathlib import Path
import pandas as pd
import numpy as np

from functions import (
    load_student_data,
    validate_student_data,
    assign_grade,
    get_pass_fail_status,
    calculate_student_results,
    calculate_subject_summary,
    get_top_students,
    get_highest_students,
    get_lowest_students,
    get_class_summary,
    get_attendance_summary,
    get_department_summary,
    get_semester_summary,
    REQUIRED_COLUMNS,
)


class TestStudentAnalyticsFunctions(unittest.TestCase):
    """Test suite for functions.py analytical functions and validations."""

    def setUp(self):
        """Set up small, controlled sample DataFrames for testing."""
        self.valid_data = pd.DataFrame(
            {
                "student_id": ["T101", "T102", "T103", "T104"],
                "student_name": ["Alice", "Bob", "Charlie", "David"],
                "department": ["Computer Science", "Computer Science", "Information Technology", "Electronics"],
                "semester": [4, 4, 6, 6],
                "python_marks": [90.0, 75.0, 30.0, 40.0],
                "mathematics_marks": [85.0, 65.0, 40.0, 34.0],
                "statistics_marks": [95.0, 70.0, 50.0, 36.0],
                "attendance_percentage": [92.0, 74.0, 80.0, 65.0],
            }
        )

    # -------------------------------------------------------------
    # 1. Grade Assignment Tests (Boundaries & Edge Cases)
    # -------------------------------------------------------------
    def test_assign_grade_boundaries(self):
        """Test grade assignment at every boundary."""
        self.assertEqual(assign_grade(100.0), "A+")
        self.assertEqual(assign_grade(90.0), "A+")
        self.assertEqual(assign_grade(89.9), "A")
        self.assertEqual(assign_grade(80.0), "A")
        self.assertEqual(assign_grade(79.9), "B")
        self.assertEqual(assign_grade(70.0), "B")
        self.assertEqual(assign_grade(69.9), "C")
        self.assertEqual(assign_grade(60.0), "C")
        self.assertEqual(assign_grade(59.9), "D")
        self.assertEqual(assign_grade(50.0), "D")
        self.assertEqual(assign_grade(49.9), "E")
        self.assertEqual(assign_grade(35.0), "E")
        self.assertEqual(assign_grade(34.9), "F")
        self.assertEqual(assign_grade(0.0), "F")

    def test_assign_grade_invalid_raises(self):
        """Test that invalid average marks raise ValueError."""
        with self.assertRaises(ValueError):
            assign_grade(-1.0)
        with self.assertRaises(ValueError):
            assign_grade(100.1)

    # -------------------------------------------------------------
    # 2. Pass / Fail Policy Tests
    # -------------------------------------------------------------
    def test_get_pass_fail_status(self):
        """Test pass/fail evaluation: must score >= 35 in all subjects to pass."""
        # All passed
        self.assertEqual(get_pass_fail_status(35.0, 35.0, 35.0), "Pass")
        self.assertEqual(get_pass_fail_status(90.0, 85.0, 78.0), "Pass")

        # Failing exactly one subject
        self.assertEqual(get_pass_fail_status(34.9, 80.0, 90.0), "Fail")
        self.assertEqual(get_pass_fail_status(80.0, 34.0, 90.0), "Fail")
        self.assertEqual(get_pass_fail_status(80.0, 90.0, 20.0), "Fail")

        # Failing multiple subjects
        self.assertEqual(get_pass_fail_status(25.0, 30.0, 15.0), "Fail")

    # -------------------------------------------------------------
    # 3. Student Calculations Tests
    # -------------------------------------------------------------
    def test_calculate_student_results(self):
        """Test total marks, average, grade, pass/fail, and attendance flag."""
        results = calculate_student_results(self.valid_data)

        # Alice: 90 + 85 + 95 = 270, avg = 90.0, grade = A+, Pass, low_att = False (92%)
        alice = results[results["student_id"] == "T101"].iloc[0]
        self.assertAlmostEqual(alice["total_marks"], 270.0)
        self.assertAlmostEqual(alice["average_marks"], 90.0)
        self.assertEqual(alice["grade"], "A+")
        self.assertEqual(alice["pass_fail_status"], "Pass")
        self.assertFalse(alice["low_attendance"])

        # Bob: 75 + 65 + 70 = 210, avg = 70.0, grade = B, Pass, low_att = True (74% < 75%)
        bob = results[results["student_id"] == "T102"].iloc[0]
        self.assertAlmostEqual(bob["total_marks"], 210.0)
        self.assertAlmostEqual(bob["average_marks"], 70.0)
        self.assertEqual(bob["grade"], "B")
        self.assertEqual(bob["pass_fail_status"], "Pass")
        self.assertTrue(bob["low_attendance"])

        # Charlie: 30 in python -> Fail overall despite passing math and stats
        charlie = results[results["student_id"] == "T103"].iloc[0]
        self.assertEqual(charlie["pass_fail_status"], "Fail")

        # David: 34 in math -> Fail overall, low attendance (65%)
        david = results[results["student_id"] == "T104"].iloc[0]
        self.assertEqual(david["pass_fail_status"], "Fail")
        self.assertTrue(david["low_attendance"])

    # -------------------------------------------------------------
    # 4. Subject Summary & Statistical Operations
    # -------------------------------------------------------------
    def test_calculate_subject_summary(self):
        """Test subject level statistics (mean, min, max, pass counts)."""
        summary = calculate_subject_summary(self.valid_data)
        self.assertEqual(len(summary), 3)

        # Python marks: [90, 75, 30, 40] -> Mean = 235 / 4 = 58.75
        py_row = summary[summary["subject"] == "Python"].iloc[0]
        self.assertAlmostEqual(py_row["average_mark"], 58.75)
        self.assertAlmostEqual(py_row["min_mark"], 30.0)
        self.assertAlmostEqual(py_row["max_mark"], 90.0)
        self.assertEqual(py_row["pass_count"], 3)  # 90, 75, 40 >= 35
        self.assertEqual(py_row["fail_count"], 1)  # 30 < 35
        self.assertAlmostEqual(py_row["pass_percentage"], 75.0)

    # -------------------------------------------------------------
    # 5. Top & Lowest Student Identification & Ties
    # -------------------------------------------------------------
    def test_top_and_lowest_students_with_ties(self):
        """Test identification of top and lowest students including ties."""
        tied_data = pd.DataFrame(
            {
                "student_id": ["S1", "S2", "S3"],
                "student_name": ["Top1", "Top2", "Low1"],
                "department": ["CS", "CS", "IT"],
                "semester": [4, 4, 4],
                "python_marks": [90.0, 90.0, 40.0],
                "mathematics_marks": [90.0, 90.0, 40.0],
                "statistics_marks": [90.0, 90.0, 40.0],
                "attendance_percentage": [80.0, 85.0, 70.0],
            }
        )
        results = calculate_student_results(tied_data)

        # Both S1 and S2 should be returned for highest
        highest = get_highest_students(results)
        self.assertEqual(len(highest), 2)
        self.assertListEqual(sorted(highest["student_id"].tolist()), ["S1", "S2"])

        # S3 lowest
        lowest = get_lowest_students(results)
        self.assertEqual(len(lowest), 1)
        self.assertEqual(lowest.iloc[0]["student_id"], "S3")

        # Top students list
        top_list = get_top_students(results, n=2)
        self.assertEqual(len(top_list), 2)

    # -------------------------------------------------------------
    # 6. Class Summary & Pass Percentage
    # -------------------------------------------------------------
    def test_get_class_summary(self):
        """Test class level summary metrics."""
        results = calculate_student_results(self.valid_data)
        summary = get_class_summary(results)

        # 4 students: Alice (Pass), Bob (Pass), Charlie (Fail), David (Fail)
        self.assertEqual(summary["total_students"], 4)
        self.assertEqual(summary["passed_students"], 2)
        self.assertEqual(summary["failed_students"], 2)
        self.assertAlmostEqual(summary["class_pass_percentage"], 50.0)
        # Class average: mean of [90, 70, 40, 36.6667] = 236.6667 / 4 = 59.17
        self.assertAlmostEqual(summary["overall_class_average"], 59.17, places=1)
        # Low attendance count: Bob (74%) and David (65%) = 2
        self.assertEqual(summary["low_attendance_count"], 2)

    # -------------------------------------------------------------
    # 7. Attendance Summary Tests
    # -------------------------------------------------------------
    def test_get_attendance_summary(self):
        """Test attendance summary and low attendance identification."""
        results = calculate_student_results(self.valid_data)
        att_summary = get_attendance_summary(results)

        # Attendances: 92, 74, 80, 65 -> Mean = 311 / 4 = 77.75
        self.assertAlmostEqual(att_summary["average_attendance"], 77.75)
        self.assertAlmostEqual(att_summary["min_attendance"], 65.0)
        self.assertAlmostEqual(att_summary["max_attendance"], 92.0)
        self.assertEqual(att_summary["low_attendance_count"], 2)
        self.assertAlmostEqual(att_summary["low_attendance_percentage"], 50.0)
        self.assertEqual(len(att_summary["flagged_students"]), 2)

    # -------------------------------------------------------------
    # 8. Department & Semester Summaries
    # -------------------------------------------------------------
    def test_department_and_semester_summary(self):
        """Test department and semester groupings."""
        results = calculate_student_results(self.valid_data)
        dept_sum = get_department_summary(results)
        self.assertIn("department", dept_sum.columns)
        self.assertEqual(len(dept_sum), 3)  # CS, IT, Electronics

        sem_sum = get_semester_summary(results)
        self.assertIn("semester", sem_sum.columns)
        self.assertEqual(len(sem_sum), 2)  # Semester 4 and 6

    # -------------------------------------------------------------
    # 9. Validation Error Handling
    # -------------------------------------------------------------
    def test_validation_empty_dataframe(self):
        """Test validation fails for empty DataFrame."""
        with self.assertRaises(ValueError):
            validate_student_data(pd.DataFrame())

    def test_validation_missing_columns(self):
        """Test validation fails when required column is missing."""
        incomplete = self.valid_data.drop(columns=["attendance_percentage"])
        with self.assertRaises(ValueError) as ctx:
            validate_student_data(incomplete)
        self.assertIn("attendance_percentage", str(ctx.exception))

    def test_validation_duplicate_ids(self):
        """Test validation fails when student_id is duplicated."""
        dupe_df = self.valid_data.copy()
        dupe_df.loc[1, "student_id"] = "T101"  # Same as row 0
        with self.assertRaises(ValueError) as ctx:
            validate_student_data(dupe_df)
        self.assertIn("Duplicate student IDs", str(ctx.exception))

    def test_validation_null_values(self):
        """Test validation fails when null values are present."""
        null_df = self.valid_data.copy()
        null_df.loc[0, "python_marks"] = np.nan
        with self.assertRaises(ValueError) as ctx:
            validate_student_data(null_df)
        self.assertIn("Null values detected", str(ctx.exception))

    def test_validation_empty_strings(self):
        """Test validation fails on blank student names or IDs."""
        blank_df = self.valid_data.copy()
        blank_df.loc[0, "student_name"] = "   "
        with self.assertRaises(ValueError) as ctx:
            validate_student_data(blank_df)
        self.assertIn("empty/blank values", str(ctx.exception))

    def test_validation_out_of_bounds_marks(self):
        """Test validation fails on marks < 0 or > 100."""
        neg_df = self.valid_data.copy()
        neg_df.loc[0, "python_marks"] = -5.0
        with self.assertRaises(ValueError) as ctx:
            validate_student_data(neg_df)
        self.assertIn("Marks in 'python_marks' must be between 0 and 100", str(ctx.exception))

        high_df = self.valid_data.copy()
        high_df.loc[0, "mathematics_marks"] = 105.0
        with self.assertRaises(ValueError) as ctx:
            validate_student_data(high_df)
        self.assertIn("Marks in 'mathematics_marks' must be between 0 and 100", str(ctx.exception))

    def test_validation_out_of_bounds_attendance(self):
        """Test validation fails on attendance < 0 or > 100."""
        att_df = self.valid_data.copy()
        att_df.loc[0, "attendance_percentage"] = 105.0
        with self.assertRaises(ValueError) as ctx:
            validate_student_data(att_df)
        self.assertIn("Attendance must be between 0 and 100", str(ctx.exception))

    def test_validation_invalid_semester(self):
        """Test validation fails on non-positive or non-integer semester."""
        sem_df = self.valid_data.copy()
        sem_df.loc[0, "semester"] = -2
        with self.assertRaises(ValueError) as ctx:
            validate_student_data(sem_df)
        self.assertIn("Semester values must be positive integers", str(ctx.exception))

    def test_load_student_data_file_not_found(self):
        """Test load_student_data raises FileNotFoundError for missing path."""
        with self.assertRaises(FileNotFoundError):
            load_student_data(Path("non_existent_directory/file.csv"))


if __name__ == "__main__":
    unittest.main()
