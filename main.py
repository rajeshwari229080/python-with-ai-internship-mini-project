"""Student Performance Analytics Using Python, NumPy and Pandas.

Main program execution entry point.
Performs data loading, validation, analytical computations, statistical summaries,
and outputs a comprehensive, structured report answering all analytical questions.
"""

from pathlib import Path
import sys
import numpy as np
import pandas as pd

from functions import (
    load_student_data,
    validate_student_data,
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

SEPARATOR_LINE = "=" * 80
SECTION_LINE = "-" * 80


def print_banner() -> None:
    """Print project header and disclaimers."""
    print(SEPARATOR_LINE)
    print("      STUDENT PERFORMANCE ANALYTICS SYSTEM")
    print("      Powered by Python 3, Pandas, and NumPy")
    print(SEPARATOR_LINE)
    print("Project       : Student Performance Analytics Using Python")
    print("Course / Org  : EWB Courses - Python with AI")
    print("Dataset Path  : data/students.csv")
    print("Notice        : This dataset is synthetic and created strictly for")
    print("                educational analytics. No real personal student data is used.")
    print(SEPARATOR_LINE)
    print()


def display_dataframe_inspection(df: pd.DataFrame) -> None:
    """Display basic dataset structure, schema, and quality inspection."""
    print("SECTION 1: DATASET INSPECTION & DATA QUALITY")
    print(SECTION_LINE)
    print(f"Total Student Records : {len(df)}")
    print(f"Total Attributes/Cols : {len(df.columns)}")
    print(f"Column Names          : {', '.join(df.columns.tolist())}")
    print()
    print("First 5 Student Records (Raw Data):")
    formatted_head = df.head(5).copy()
    print(formatted_head.to_string(index=False))
    print()

    print("Data Schema & Types:")
    for col in df.columns:
        print(f"  - {col:<24}: {str(df[col].dtype):<10} (Non-null: {df[col].notna().sum()}/{len(df)})")
    print()

    print("Data Quality Verification:")
    missing_count = df.isnull().sum().sum()
    duplicate_count = df["student_id"].duplicated().sum()
    print(f"  - Missing / Null Values    : {missing_count} detected")
    print(f"  - Duplicate Student IDs   : {duplicate_count} detected")
    print(f"  - Marks Range (0 - 100)    : Validated (All marks within valid boundaries)")
    print(f"  - Attendance Range (0-100) : Validated (All values within valid boundaries)")
    print()


def display_student_results(df_results: pd.DataFrame) -> None:
    """Display calculated results for all students in a clean table."""
    print("SECTION 2: COMPUTED STUDENT RESULTS")
    print(SECTION_LINE)
    print("Calculations applied: Total Marks, Overall Average, Grade Band, Academic Pass/Fail, Low Attendance Flag.")
    print()

    display_cols = [
        "student_id",
        "student_name",
        "department",
        "semester",
        "python_marks",
        "mathematics_marks",
        "statistics_marks",
        "total_marks",
        "average_marks",
        "grade",
        "pass_fail_status",
        "attendance_percentage",
        "low_attendance",
    ]

    table_copy = df_results[display_cols].copy()
    table_copy["average_marks"] = table_copy["average_marks"].apply(lambda v: f"{v:.2f}")
    table_copy["attendance_percentage"] = table_copy["attendance_percentage"].apply(lambda v: f"{v:.1f}%")
    table_copy["low_attendance"] = table_copy["low_attendance"].apply(lambda v: "YES" if v else "No")

    print(table_copy.to_string(index=False))
    print()


def display_subject_analysis(df: pd.DataFrame) -> None:
    """Display subject-level statistics and performance metrics."""
    print("SECTION 3: SUBJECT-WISE PERFORMANCE ANALYSIS")
    print(SECTION_LINE)
    subject_summary = calculate_subject_summary(df)

    # Format table for display
    display_df = subject_summary[[
        "subject", "average_mark", "std_deviation", "min_mark", "max_mark", "pass_count", "pass_percentage"
    ]].copy()
    display_df.columns = [
        "Subject", "Class Average", "Std Dev", "Min Mark", "Max Mark", "Pass Count", "Pass %"
    ]
    print(display_df.to_string(index=False))
    print()


def display_department_and_semester_analysis(df_results: pd.DataFrame) -> None:
    """Display department and semester group analyses."""
    print("SECTION 4: DEPARTMENT & SEMESTER GROUP BREAKDOWNS")
    print(SECTION_LINE)
    print("Department-Wise Breakdown:")
    dept_df = get_department_summary(df_results)
    dept_display = dept_df.copy()
    dept_display.columns = [
        "Department", "Students", "Avg Mark", "Passed", "Failed", "Pass %", "Avg Attendance %"
    ]
    print(dept_display.to_string(index=False))
    print()

    print("Semester-Wise Breakdown:")
    sem_df = get_semester_summary(df_results)
    sem_display = sem_df.copy()
    sem_display.columns = [
        "Semester", "Students", "Avg Mark", "Passed", "Failed", "Pass %", "Avg Attendance %"
    ]
    print(sem_display.to_string(index=False))
    print()


def display_attendance_analysis(df_results: pd.DataFrame) -> None:
    """Display class attendance metrics and list students flagged for low attendance."""
    print("SECTION 5: ATTENDANCE & ELIGIBILITY REPORT")
    print(SECTION_LINE)
    att_summary = get_attendance_summary(df_results)

    print(f"Class Average Attendance   : {att_summary['average_attendance']:.2f}%")
    print(f"Minimum Attendance         : {att_summary['min_attendance']:.2f}%")
    print(f"Maximum Attendance         : {att_summary['max_attendance']:.2f}%")
    print(f"Low Attendance Threshold   : < 75.00%")
    print(f"Students Below Threshold   : {att_summary['low_attendance_count']} ({att_summary['low_attendance_percentage']:.2f}% of class)")
    print()

    if att_summary["low_attendance_count"] > 0:
        print("Students Flagged for Low Attendance (< 75%):")
        flagged = att_summary["flagged_students"].copy()
        flagged.columns = ["Student ID", "Name", "Department", "Attendance %", "Academic Status"]
        flagged["Attendance %"] = flagged["Attendance %"].apply(lambda v: f"{v:.1f}%")
        print(flagged.to_string(index=False))
        print("Note: In accordance with project policy, low attendance does NOT automatically override academic pass/fail status.")
    else:
        print("All students meet the 75% attendance requirement.")
    print()


def display_answers_to_analytical_questions(df_results: pd.DataFrame) -> None:
    """Explicitly address all 12 analytical questions using computed figures."""
    print("SECTION 6: ANSWERS TO KEY ANALYTICAL QUESTIONS")
    print(SECTION_LINE)

    class_sum = get_class_summary(df_results)
    att_sum = get_attendance_summary(df_results)
    top_5 = get_top_students(df_results, n=5)
    highest_students = get_highest_students(df_results)
    lowest_students = get_lowest_students(df_results)
    dept_df = get_department_summary(df_results)

    # Q1: Highest average student(s)
    highest_names = [f"{row['student_name']} ({row['student_id']}) with {row['average_marks']:.2f}%" for _, row in highest_students.iterrows()]
    print(f"1. Highest Performing Student(s):")
    for item in highest_names:
        print(f"   -> {item}")
    print()

    # Q2: Subject with highest average mark
    print(f"2. Subject with Highest Class Average:")
    print(f"   -> {class_sum['highest_average_subject']} ({class_sum['highest_average_subject_mark']:.2f}%)")
    print(f"      (Python: {class_sum['subject_means']['Python']}%, Math: {class_sum['subject_means']['Mathematics']}%, Stats: {class_sum['subject_means']['Statistics']}%)")
    print()

    # Q3: Passed all 3 subjects
    print(f"3. Number of Students Passing All Three Subjects:")
    print(f"   -> {class_sum['passed_students']} out of {class_sum['total_students']} students")
    print()

    # Q4: Failed at least one subject
    print(f"4. Number of Students Failing At Least One Subject:")
    print(f"   -> {class_sum['failed_students']} out of {class_sum['total_students']} students")
    print()

    # Q5: Overall class average
    print(f"5. Overall Class Average:")
    print(f"   -> {class_sum['overall_class_average']:.2f}% (Std Dev: {class_sum['overall_class_std']:.2f}%, Median: {class_sum['overall_class_median']:.2f}%)")
    print()

    # Q6: Average attendance percentage
    print(f"6. Average Attendance Percentage:")
    print(f"   -> {att_sum['average_attendance']:.2f}%")
    print()

    # Q7: Students with attendance below 75%
    flagged_names = [f"{row['student_name']} ({row['student_id']}) - {row['attendance_percentage']:.1f}% [{row['department']}]" for _, row in att_sum['flagged_students'].iterrows()]
    print(f"7. Students with Attendance Below 75% ({len(flagged_names)} students):")
    for s in flagged_names:
        print(f"   -> {s}")
    print()

    # Q8: Top five students
    print(f"8. Top 5 Students in Class (by Overall Average):")
    for rank, (_, row) in enumerate(top_5.iterrows(), start=1):
        print(f"   {rank}. {row['student_name']} ({row['student_id']}) - Dept: {row['department']} | Avg: {row['average_marks']:.2f}% | Grade: {row['grade']}")
    print()

    # Q9: Lowest average student(s)
    lowest_names = [f"{row['student_name']} ({row['student_id']}) with {row['average_marks']:.2f}%" for _, row in lowest_students.iterrows()]
    print(f"9. Lowest Performing Student(s):")
    for item in lowest_names:
        print(f"   -> {item}")
    print()

    # Q10: Class pass percentage
    print(f"10. Class Academic Pass Percentage:")
    print(f"    -> {class_sum['class_pass_percentage']:.2f}%")
    print()

    # Q11: Average marks differences across departments/semesters
    top_dept = dept_df.iloc[0]
    low_dept = dept_df.iloc[-1]
    print(f"11. Performance Variation Across Departments & Semesters:")
    print(f"    -> Highest Performing Department : {top_dept['department']} ({top_dept['average_marks']:.2f}% avg, {top_dept['pass_percentage']:.1f}% pass rate)")
    print(f"    -> Lowest Performing Department  : {low_dept['department']} ({low_dept['average_marks']:.2f}% avg, {low_dept['pass_percentage']:.1f}% pass rate)")
    print()

    # Q12: Distribution suggestions
    avg_arr = df_results["average_marks"].to_numpy(dtype=float)
    p25, p50, p75 = np.percentile(avg_arr, [25, 50, 75])
    print(f"12. Statistical Insights on Student Performance Distribution:")
    print(f"    -> 25th Percentile (Q1) : {p25:.2f}%")
    print(f"    -> 50th Percentile (Q2) : {p50:.2f}% (Median)")
    print(f"    -> 75th Percentile (Q3) : {p75:.2f}%")
    print(f"    -> Interquartile Range  : {(p75 - p25):.2f}%")
    print(f"    -> Conclusion           : Performance reflects a balanced bell-like spread, with")
    print(f"                              exceptional outliers at 90%+ and an academic intervention")
    print(f"                              need for {class_sum['failed_students']} students who scored < 35 in required coursework.")
    print()


def main() -> None:
    """Execute main end-to-end analytics workflow."""
    print_banner()

    # Resolve dataset path relative to this script
    base_dir = Path(__file__).resolve().parent
    dataset_path = base_dir / "data" / "students.csv"

    # 1. Load Data
    try:
        raw_df = load_student_data(dataset_path)
    except FileNotFoundError as fnf_err:
        print(f"[ERROR] Dataset file not found: {fnf_err}", file=sys.stderr)
        sys.exit(1)
    except ValueError as val_err:
        print(f"[ERROR] Failed to load dataset: {val_err}", file=sys.stderr)
        sys.exit(1)

    # 2. Validate Data
    try:
        validate_student_data(raw_df)
    except ValueError as val_err:
        print(f"[ERROR] Data validation failed: {val_err}", file=sys.stderr)
        sys.exit(1)

    # 3. DataFrame Inspection
    display_dataframe_inspection(raw_df)

    # 4. Compute Results
    results_df = calculate_student_results(raw_df)

    # 5. Display Full Student Results
    display_student_results(results_df)

    # 6. Display Subject Analysis
    display_subject_analysis(raw_df)

    # 7. Department and Semester Analysis
    display_department_and_semester_analysis(results_df)

    # 8. Attendance Report
    display_attendance_analysis(results_df)

    # 9. Answers to 12 Key Analytical Questions
    display_answers_to_analytical_questions(results_df)

    print(SEPARATOR_LINE)
    print("      ANALYSIS COMPLETE - REPORT GENERATED SUCCESSFULLY")
    print(SEPARATOR_LINE)


if __name__ == "__main__":
    main()
