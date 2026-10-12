"""Student Performance Analytics - Reusable Analytical Functions.

This module provides data loading, rigorous validation, analytical calculations,
grading policies, and summary reporting using Python standard libraries,
Pandas, and NumPy.
"""

from pathlib import Path
from typing import Any, Dict, List, Union
import numpy as np
import pandas as pd

REQUIRED_COLUMNS: List[str] = [
    "student_id",
    "student_name",
    "department",
    "semester",
    "python_marks",
    "mathematics_marks",
    "statistics_marks",
    "attendance_percentage",
]

NUMERIC_COLUMNS: List[str] = [
    "semester",
    "python_marks",
    "mathematics_marks",
    "statistics_marks",
    "attendance_percentage",
]

SUBJECT_COLUMNS: List[str] = [
    "python_marks",
    "mathematics_marks",
    "statistics_marks",
]

PASSING_MARK_THRESHOLD: float = 35.0
ATTENDANCE_THRESHOLD: float = 75.0


def load_student_data(file_path: Union[str, Path]) -> pd.DataFrame:
    """Load student performance dataset from a CSV file.

    Parameters
    ----------
    file_path : str or Path
        Path to the CSV file.

    Returns
    -------
    pd.DataFrame
        Loaded student data.

    Raises
    ------
    FileNotFoundError
        If the file does not exist at the specified path.
    ValueError
        If the file is empty or cannot be parsed as a valid CSV.
    """
    path_obj = Path(file_path).resolve()
    if not path_obj.exists():
        raise FileNotFoundError(f"Student data file not found at: {path_obj}")

    if path_obj.stat().st_size == 0:
        raise ValueError(f"The student data file is completely empty: {path_obj}")

    try:
        df = pd.read_csv(path_obj)
    except Exception as exc:
        raise ValueError(f"Failed to parse CSV file '{path_obj}': {exc}") from exc

    if df.empty:
        raise ValueError("The loaded DataFrame contains no rows.")

    return df


def validate_student_data(df: pd.DataFrame) -> None:
    """Validate student performance DataFrame for structure, completeness, and values.

    Parameters
    ----------
    df : pd.DataFrame
        Input DataFrame to validate.

    Raises
    ------
    ValueError
        If DataFrame is empty, missing required columns, has duplicates,
        contains nulls/empty strings, or has values outside permitted ranges.
    """
    if df is None or not isinstance(df, pd.DataFrame):
        raise ValueError("Input data must be a valid Pandas DataFrame.")

    if df.empty:
        raise ValueError("Validation failed: The DataFrame is empty.")

    # 1. Required Columns Check
    missing_cols = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    if missing_cols:
        raise ValueError(
            f"Validation failed: Missing required columns: {', '.join(missing_cols)}"
        )

    # 2. Null / Missing Values Check
    null_counts = df[REQUIRED_COLUMNS].isnull().sum()
    cols_with_nulls = null_counts[null_counts > 0]
    if not cols_with_nulls.empty:
        details = ", ".join([f"{col} ({cnt})" for col, cnt in cols_with_nulls.items()])
        raise ValueError(f"Validation failed: Null values detected in: {details}")

    # 3. String columns non-empty check
    for col in ["student_id", "student_name", "department"]:
        empty_strings = df[col].astype(str).str.strip().eq("").sum()
        if empty_strings > 0:
            raise ValueError(
                f"Validation failed: Column '{col}' contains {empty_strings} empty/blank values."
            )

    # 4. Duplicate Student ID Check
    duplicate_ids = df[df["student_id"].duplicated(keep=False)]["student_id"].tolist()
    if duplicate_ids:
        unique_dupes = sorted(list(set(str(x) for x in duplicate_ids)))
        raise ValueError(
            f"Validation failed: Duplicate student IDs found: {', '.join(unique_dupes)}"
        )

    # 5. Numeric conversion & Range Checks
    for col in NUMERIC_COLUMNS:
        non_numeric = pd.to_numeric(df[col], errors="coerce").isna().sum()
        if non_numeric > 0:
            raise ValueError(
                f"Validation failed: Column '{col}' contains non-numeric values."
            )

    # Check semester positive integer
    semesters = pd.to_numeric(df["semester"])
    if (semesters <= 0).any() or (semesters % 1 != 0).any():
        raise ValueError("Validation failed: Semester values must be positive integers.")

    # Check marks in 0-100 range
    for sub in SUBJECT_COLUMNS:
        marks = pd.to_numeric(df[sub])
        if (marks < 0.0).any() or (marks > 100.0).any():
            out_of_bounds = marks[(marks < 0.0) | (marks > 100.0)].tolist()
            raise ValueError(
                f"Validation failed: Marks in '{sub}' must be between 0 and 100. Found: {out_of_bounds}"
            )

    # Check attendance in 0-100 range
    attendance = pd.to_numeric(df["attendance_percentage"])
    if (attendance < 0.0).any() or (attendance > 100.0).any():
        out_of_bounds = attendance[(attendance < 0.0) | (attendance > 100.0)].tolist()
        raise ValueError(
            f"Validation failed: Attendance must be between 0 and 100. Found: {out_of_bounds}"
        )


def assign_grade(average: float) -> str:
    """Assign letter grade based on overall average percentage.

    Policy:
    - 90 - 100: A+
    - 80 - <90: A
    - 70 - <80: B
    - 60 - <70: C
    - 50 - <60: D
    - 35 - <50: E
    - Below 35: F

    Parameters
    ----------
    average : float
        Overall average marks (0.0 to 100.0).

    Returns
    -------
    str
        Assigned letter grade.

    Raises
    ------
    ValueError
        If average is outside 0.0 to 100.0.
    """
    if average < 0.0 or average > 100.0:
        raise ValueError(f"Average mark must be between 0 and 100. Got: {average}")

    if average >= 90.0:
        return "A+"
    elif average >= 80.0:
        return "A"
    elif average >= 70.0:
        return "B"
    elif average >= 60.0:
        return "C"
    elif average >= 50.0:
        return "D"
    elif average >= 35.0:
        return "E"
    else:
        return "F"


def get_pass_fail_status(
    python_marks: float, mathematics_marks: float, statistics_marks: float
) -> str:
    """Determine overall academic pass/fail status.

    A student passes overall only when all three subject marks are at least 35.

    Parameters
    ----------
    python_marks : float
        Marks in Python.
    mathematics_marks : float
        Marks in Mathematics.
    statistics_marks : float
        Marks in Statistics.

    Returns
    -------
    str
        "Pass" if all subjects >= 35.0, else "Fail".
    """
    marks = [python_marks, mathematics_marks, statistics_marks]
    for mark in marks:
        if mark < PASSING_MARK_THRESHOLD:
            return "Fail"
    return "Pass"


def calculate_student_results(df: pd.DataFrame) -> pd.DataFrame:
    """Compute total marks, average, grade, pass/fail status, and attendance flags.

    Does not mutate the original input DataFrame.

    Parameters
    ----------
    df : pd.DataFrame
        Validated student records.

    Returns
    -------
    pd.DataFrame
        Copy of input DataFrame augmented with calculated performance fields.
    """
    validate_student_data(df)
    results = df.copy()

    # Calculate total marks using NumPy summation across subject columns
    subject_matrix = results[SUBJECT_COLUMNS].to_numpy(dtype=float)
    results["total_marks"] = np.sum(subject_matrix, axis=1)

    # Calculate student average
    results["average_marks"] = np.mean(subject_matrix, axis=1)

    # Assign grades using conditional logic
    results["grade"] = [assign_grade(avg) for avg in results["average_marks"]]

    # Determine pass/fail status
    results["pass_fail_status"] = [
        get_pass_fail_status(p, m, s)
        for p, m, s in zip(
            results["python_marks"],
            results["mathematics_marks"],
            results["statistics_marks"],
        )
    ]

    # Attendance eligibility flag (< 75% flagged as True)
    results["low_attendance"] = results["attendance_percentage"] < ATTENDANCE_THRESHOLD

    return results


def calculate_subject_summary(df: pd.DataFrame) -> pd.DataFrame:
    """Calculate statistical summaries for each academic subject.

    Parameters
    ----------
    df : pd.DataFrame
        Student records containing subject marks.

    Returns
    -------
    pd.DataFrame
        Summary table showing class average, std dev, min, max, pass count,
        and pass percentage per subject.
    """
    validate_student_data(df)
    summary_data = []

    subject_labels = {
        "python_marks": "Python",
        "mathematics_marks": "Mathematics",
        "statistics_marks": "Statistics",
    }

    for col, label in subject_labels.items():
        marks_array = df[col].to_numpy(dtype=float)
        avg = float(np.mean(marks_array))
        std = float(np.std(marks_array, ddof=1)) if len(marks_array) > 1 else 0.0
        min_mark = float(np.min(marks_array))
        max_mark = float(np.max(marks_array))
        pass_count = int(np.sum(marks_array >= PASSING_MARK_THRESHOLD))
        pass_pct = float((pass_count / len(marks_array)) * 100.0)

        summary_data.append(
            {
                "subject": label,
                "column_name": col,
                "average_mark": round(avg, 2),
                "std_deviation": round(std, 2),
                "min_mark": round(min_mark, 2),
                "max_mark": round(max_mark, 2),
                "pass_count": pass_count,
                "fail_count": len(marks_array) - pass_count,
                "pass_percentage": round(pass_pct, 2),
            }
        )

    return pd.DataFrame(summary_data)


def get_top_students(df_results: pd.DataFrame, n: int = 5) -> pd.DataFrame:
    """Retrieve top n students sorted descending by average marks.

    Parameters
    ----------
    df_results : pd.DataFrame
        Calculated student results DataFrame.
    n : int, default 5
        Number of top students to return.

    Returns
    -------
    pd.DataFrame
        Top students ranked by average marks.
    """
    if "average_marks" not in df_results.columns:
        raise ValueError("DataFrame must contain 'average_marks' column.")

    sorted_df = df_results.sort_values(
        by=["average_marks", "total_marks"], ascending=[False, False]
    ).reset_index(drop=True)
    return sorted_df.head(n)


def get_highest_students(df_results: pd.DataFrame) -> pd.DataFrame:
    """Retrieve the student or students with the highest average mark (handles ties).

    Parameters
    ----------
    df_results : pd.DataFrame
        Calculated student results DataFrame.

    Returns
    -------
    pd.DataFrame
        All students matching the maximum average marks.
    """
    if "average_marks" not in df_results.columns:
        raise ValueError("DataFrame must contain 'average_marks' column.")

    max_avg = df_results["average_marks"].max()
    return df_results[df_results["average_marks"] == max_avg].reset_index(drop=True)


def get_lowest_students(df_results: pd.DataFrame) -> pd.DataFrame:
    """Retrieve the student or students with the lowest average mark (handles ties).

    Parameters
    ----------
    df_results : pd.DataFrame
        Calculated student results DataFrame.

    Returns
    -------
    pd.DataFrame
        All students matching the minimum average marks.
    """
    if "average_marks" not in df_results.columns:
        raise ValueError("DataFrame must contain 'average_marks' column.")

    min_avg = df_results["average_marks"].min()
    return df_results[df_results["average_marks"] == min_avg].reset_index(drop=True)


def get_class_summary(df_results: pd.DataFrame) -> Dict[str, Any]:
    """Calculate overall class-level performance metrics.

    Parameters
    ----------
    df_results : pd.DataFrame
        Calculated student results DataFrame.

    Returns
    -------
    dict
        Dictionary containing overall class totals, averages, pass rates, and subject comparisons.
    """
    total_students = len(df_results)
    if total_students == 0:
        raise ValueError("Cannot calculate class summary for an empty dataset.")

    passed_count = int((df_results["pass_fail_status"] == "Pass").sum())
    failed_count = int((df_results["pass_fail_status"] == "Fail").sum())
    pass_pct = round((passed_count / total_students) * 100.0, 2)

    class_avg = float(df_results["average_marks"].mean())
    avg_attendance = float(df_results["attendance_percentage"].mean())
    low_attendance_count = int(df_results["low_attendance"].sum())

    # Subject with highest class average
    subj_means = {
        "Python": float(df_results["python_marks"].mean()),
        "Mathematics": float(df_results["mathematics_marks"].mean()),
        "Statistics": float(df_results["statistics_marks"].mean()),
    }
    highest_subj = max(subj_means.items(), key=lambda item: item[1])

    return {
        "total_students": total_students,
        "passed_students": passed_count,
        "failed_students": failed_count,
        "class_pass_percentage": pass_pct,
        "overall_class_average": round(class_avg, 2),
        "overall_class_std": round(float(df_results["average_marks"].std(ddof=1)), 2),
        "overall_class_median": round(float(df_results["average_marks"].median()), 2),
        "average_attendance": round(avg_attendance, 2),
        "low_attendance_count": low_attendance_count,
        "subject_means": {k: round(v, 2) for k, v in subj_means.items()},
        "highest_average_subject": highest_subj[0],
        "highest_average_subject_mark": round(highest_subj[1], 2),
    }


def get_attendance_summary(df_results: pd.DataFrame) -> Dict[str, Any]:
    """Calculate attendance metrics and list students flagged for low attendance.

    Parameters
    ----------
    df_results : pd.DataFrame
        Calculated student results DataFrame.

    Returns
    -------
    dict
        Attendance statistics and DataFrame of flagged students.
    """
    total_students = len(df_results)
    attendance_arr = df_results["attendance_percentage"].to_numpy(dtype=float)

    low_att_df = df_results[df_results["low_attendance"]][
        ["student_id", "student_name", "department", "attendance_percentage", "pass_fail_status"]
    ].reset_index(drop=True)

    return {
        "average_attendance": round(float(np.mean(attendance_arr)), 2),
        "min_attendance": round(float(np.min(attendance_arr)), 2),
        "max_attendance": round(float(np.max(attendance_arr)), 2),
        "low_attendance_count": len(low_att_df),
        "low_attendance_percentage": round((len(low_att_df) / total_students) * 100.0, 2),
        "flagged_students": low_att_df,
    }


def get_department_summary(df_results: pd.DataFrame) -> pd.DataFrame:
    """Generate department-wise performance breakdown.

    Parameters
    ----------
    df_results : pd.DataFrame
        Calculated student results DataFrame.

    Returns
    -------
    pd.DataFrame
        Summary table grouped by department.
    """
    grouped = df_results.groupby("department")
    summary = []

    for dept, group in grouped:
        total = len(group)
        passed = int((group["pass_fail_status"] == "Pass").sum())
        pass_pct = round((passed / total) * 100.0, 2)
        avg_marks = round(float(group["average_marks"].mean()), 2)
        avg_att = round(float(group["attendance_percentage"].mean()), 2)

        summary.append(
            {
                "department": dept,
                "student_count": total,
                "average_marks": avg_marks,
                "pass_count": passed,
                "fail_count": total - passed,
                "pass_percentage": pass_pct,
                "average_attendance": avg_att,
            }
        )

    return pd.DataFrame(summary).sort_values(by="average_marks", ascending=False).reset_index(drop=True)


def get_semester_summary(df_results: pd.DataFrame) -> pd.DataFrame:
    """Generate semester-wise performance breakdown.

    Parameters
    ----------
    df_results : pd.DataFrame
        Calculated student results DataFrame.

    Returns
    -------
    pd.DataFrame
        Summary table grouped by semester.
    """
    grouped = df_results.groupby("semester")
    summary = []

    for sem, group in grouped:
        total = len(group)
        passed = int((group["pass_fail_status"] == "Pass").sum())
        pass_pct = round((passed / total) * 100.0, 2)
        avg_marks = round(float(group["average_marks"].mean()), 2)
        avg_att = round(float(group["attendance_percentage"].mean()), 2)

        summary.append(
            {
                "semester": sem,
                "student_count": total,
                "average_marks": avg_marks,
                "pass_count": passed,
                "fail_count": total - passed,
                "pass_percentage": pass_pct,
                "average_attendance": avg_att,
            }
        )

    return pd.DataFrame(summary).sort_values(by="semester").reset_index(drop=True)
