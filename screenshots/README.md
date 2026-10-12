# Project Output Screenshots

This directory is designated for real screenshots captured from executing the application in your local environment.

## Recommended Screenshots to Include
1. **`01_dataset_inspection.png`**: Terminal view showing data loading, column schema, and data validation.
2. **`02_student_results_table.png`**: Terminal view of the computed student performance table (total marks, average, grade, pass/fail status).
3. **`03_subject_department_analysis.png`**: Terminal view displaying the subject-wise statistical analysis, department-wise summary, and semester comparison.
4. **`04_attendance_and_key_answers.png`**: Terminal view displaying the attendance eligibility report and answers to the 12 key analytical questions.
5. **`05_unit_tests.png`**: Terminal view showing all passing unit tests (`python -m unittest discover -s tests -v`).

## How to Capture and Add Screenshots
1. Open PowerShell or Command Prompt on Windows.
2. Run the main program:
   ```powershell
   python main.py
   ```
3. Use the Windows Snipping Tool (`Win + Shift + S`) to capture the terminal window.
4. Save the captured image files in this `screenshots/` directory.
5. Update markdown links in [Project_Documentation.md](../Project_Documentation.md) or [README.md](../README.md) using markdown image syntax:
   ```markdown
   ![Student Performance Analytics Execution](screenshots/01_dataset_inspection.png)
   ```
