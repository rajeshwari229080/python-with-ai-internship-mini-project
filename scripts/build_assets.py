"""
Asset generation script for Student Performance Analytics Project.
Generates light-themed visual assets for README.md and LinkedIn Post showcase (image.png).
Author: Rajeshwari | EWB Courses - Python with AI
"""

import os
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# Ensure target directories exist
ROOT_DIR = Path(__file__).resolve().parent.parent
ASSETS_DIR = ROOT_DIR / "assets"
ASSETS_DIR.mkdir(parents=True, exist_ok=True)

FONT_FAMILY = "Segoe UI"


# -------------------------------------------------------------------------
# 1. README BANNER (assets/banner_light.png)
# -------------------------------------------------------------------------
def generate_readme_banner():
    width_px, height_px = 1200, 380
    fig = plt.figure(figsize=(12, 3.8), dpi=100)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, width_px)
    ax.set_ylim(0, height_px)
    ax.axis('off')

    # Background canvas: Soft light gradient aesthetic
    bg = patches.Rectangle((0, 0), width_px, height_px, facecolor='#F8FAFC', edgecolor='none')
    ax.add_patch(bg)

    # Accent decorative glow/pill in top-left
    glow1 = patches.Circle((100, 360), 220, facecolor='#EEF2FF', edgecolor='none', alpha=0.7)
    glow2 = patches.Circle((1100, 80), 200, facecolor='#F0FDF4', edgecolor='none', alpha=0.6)
    ax.add_patch(glow1)
    ax.add_patch(glow2)

    # Border frame
    frame = patches.FancyBboxPatch((16, 16), width_px - 32, height_px - 32,
                                  boxstyle="round,pad=0.2,rounding_size=18",
                                  facecolor='#FFFFFF', edgecolor='#E2E8F0', linewidth=1.5)
    ax.add_patch(frame)

    # Top Category Pill
    tag_bg = patches.FancyBboxPatch((55, 305), 335, 28,
                                    boxstyle="round,pad=0.2,rounding_size=14",
                                    facecolor='#EEF2FF', edgecolor='#C7D2FE', linewidth=1)
    ax.add_patch(tag_bg)
    ax.text(68, 319, "EWB COURSES • PYTHON WITH AI INTERNSHIP",
            fontsize=9.5, fontweight='bold', color='#4338CA',
            va='center', fontfamily=FONT_FAMILY)

    # Main Title
    ax.text(55, 260, "Student Performance Analytics",
            fontsize=26, fontweight='bold', color='#0F172A',
            va='center', fontfamily=FONT_FAMILY)

    # Subtitle
    ax.text(55, 218, "Automated Academic Performance Evaluation, Statistical Insights & Reporting System",
            fontsize=13, color='#475569',
            va='center', fontfamily=FONT_FAMILY)

    # Key Bullet Highlights
    bullets = [
        "Pure-function architecture with Pandas & NumPy",
        "7-Tier academic grading & strict multi-subject pass rule",
        "Automated 18-suite unittest verification (100% pass rate)"
    ]
    for i, b in enumerate(bullets):
        # Draw small green badge dot
        ax.plot(62, 172 - (i * 24), marker='o', color='#059669', markersize=5)
        ax.text(76, 172 - (i * 24), b, fontsize=11, color='#334155', va='center', fontfamily=FONT_FAMILY)

    # Badge chips at the bottom left
    badges = [
        ("Python 3.11+", "#3776AB", "#EFF6FF"),
        ("Pandas 2.0+", "#150458", "#F5F3FF"),
        ("NumPy 1.24+", "#013243", "#ECFEFF"),
        ("18 Tests Pass", "#059669", "#ECFDF5"),
        ("MIT License", "#4F46E5", "#EEF2FF")
    ]
    bx = 55
    for text, border_c, bg_c in badges:
        bw = len(text) * 8.2 + 22
        chip = patches.FancyBboxPatch((bx, 38), bw, 26,
                                      boxstyle="round,pad=0.2,rounding_size=13",
                                      facecolor=bg_c, edgecolor=border_c, linewidth=1)
        ax.add_patch(chip)
        ax.text(bx + bw / 2, 51, text, fontsize=9.5, fontweight='bold',
                color=border_c, ha='center', va='center', fontfamily=FONT_FAMILY)
        bx += bw + 12

    # Right-side metric cards (Stacked Mini Bento Grid)
    cards = [
        ("84.00%", "Class Pass Rate", "21 Passed / 4 Failed", "#059669", "#ECFDF5", "#A7F3D0"),
        ("65.35%", "Overall Class Avg", "Std Dev: 18.98%", "#4F46E5", "#EEF2FF", "#C7D2FE"),
        ("93.67%", "Top Score (Rank 1)", "Aarav Sharma (S101)", "#D97706", "#FFFBEB", "#FDE68A")
    ]
    cx = 880
    cy = 250
    for val, title, sub, text_c, bg_c, bord_c in cards:
        card_box = patches.FancyBboxPatch((cx, cy), 260, 72,
                                          boxstyle="round,pad=0.2,rounding_size=12",
                                          facecolor=bg_c, edgecolor=bord_c, linewidth=1.2)
        ax.add_patch(card_box)
        ax.text(cx + 18, cy + 48, val, fontsize=17, fontweight='bold', color=text_c, fontfamily=FONT_FAMILY)
        ax.text(cx + 18, cy + 30, title, fontsize=10.5, fontweight='bold', color='#1E293B', fontfamily=FONT_FAMILY)
        ax.text(cx + 18, cy + 14, sub, fontsize=9, color='#64748B', fontfamily=FONT_FAMILY)
        cy -= 86

    out_path = ASSETS_DIR / "banner_light.png"
    plt.savefig(out_path, dpi=100, bbox_inches='tight', pad_inches=0.05, facecolor='#F8FAFC')
    plt.close()
    print(f"Created: {out_path}")



# -------------------------------------------------------------------------
# 2. ARCHITECTURE DIAGRAM (assets/architecture_light.png)
# -------------------------------------------------------------------------
def generate_architecture_diagram():
    width_px, height_px = 1100, 380
    fig = plt.figure(figsize=(11, 3.8), dpi=100)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, width_px)
    ax.set_ylim(0, height_px)
    ax.axis('off')

    # Canvas
    ax.add_patch(patches.Rectangle((0, 0), width_px, height_px, facecolor='#F8FAFC', edgecolor='none'))

    # Container Card
    container = patches.FancyBboxPatch((20, 18), width_px - 40, height_px - 36,
                                       boxstyle="round,pad=0.2,rounding_size=16",
                                       facecolor='#FFFFFF', edgecolor='#E2E8F0', linewidth=1.5)
    ax.add_patch(container)

    # Title section
    ax.text(50, 335, "SYSTEM ARCHITECTURE & PROCESSING PIPELINE",
            fontsize=11, fontweight='bold', color='#4F46E5', fontfamily=FONT_FAMILY)
    ax.text(50, 308, "Data Ingestion, Computation, Verification, and Reporting Pipeline",
            fontsize=17, fontweight='bold', color='#0F172A', fontfamily=FONT_FAMILY)

    # 4 Pipeline Stages
    stages = [
        ("1. Data Ingestion", "data/students.csv",
         ["• Schema validation", "• Null value scan", "• Duplicate ID guard", "• Boundary check"],
         "#3B82F6", "#EFF6FF", "#BFDBFE"),
        ("2. Calculation Core", "functions.py",
         ["• Vector totals & avg", "• 7-Tier grade map", "• Academic pass/fail", "• Attendance isolation"],
         "#6366F1", "#EEF2FF", "#C7D2FE"),
        ("3. Aggregation Engine", "Pandas & NumPy",
         ["• Subject metrics", "• Department cohorts", "• Semester contrasts", "• Quartiles Q1-Q3"],
         "#059669", "#ECFDF5", "#A7F3D0"),
        ("4. Reporting & QA", "main.py & tests/",
         ["• Terminal CLI report", "• 12 Analytical insights", "• Top/bottom rankings", "• 18 unittests (OK)"],
         "#D97706", "#FFFBEB", "#FDE68A")
    ]

    sx = 50
    sw = 215
    sh = 180
    sy = 85

    for i, (title, file_ref, bullets, col, bg_col, bdr_col) in enumerate(stages):
        box = patches.FancyBboxPatch((sx, sy), sw, sh,
                                     boxstyle="round,pad=0.2,rounding_size=12",
                                     facecolor=bg_col, edgecolor=bdr_col, linewidth=1.5)
        ax.add_patch(box)

        # Stage header
        ax.text(sx + 14, sy + sh - 24, title, fontsize=12, fontweight='bold', color=col, fontfamily=FONT_FAMILY)
        ax.text(sx + 14, sy + sh - 42, file_ref, fontsize=9.5, fontweight='bold', color='#475569', fontfamily=FONT_FAMILY)

        # Separator line
        ax.plot([sx + 14, sx + sw - 14], [sy + sh - 52, sy + sh - 52], color=bdr_col, lw=1)

        # Bullets
        by = sy + sh - 72
        for b in bullets:
            ax.text(sx + 14, by, b, fontsize=9.5, color='#334155', fontfamily=FONT_FAMILY)
            by -= 24

        # Connecting arrow
        if i < len(stages) - 1:
            ax.annotate("", xy=(sx + sw + 35, sy + sh/2), xytext=(sx + sw + 5, sy + sh/2),
                        arrowprops=dict(arrowstyle="->,head_width=0.4,head_length=0.6",
                                        lw=2, color='#94A3B8'))

        sx += sw + 45

    # Bottom footer note
    ax.text(width_px / 2, 42, "Pure Functional Design: Source DataFrames remain immutable during analysis",
            fontsize=10, color='#64748B', ha='center', fontfamily=FONT_FAMILY)

    out_path = ASSETS_DIR / "architecture_light.png"
    plt.savefig(out_path, dpi=100, bbox_inches='tight', pad_inches=0.05, facecolor='#F8FAFC')
    plt.close()
    print(f"Created: {out_path}")


# -------------------------------------------------------------------------
# 3. ANALYTICS OVERVIEW DASHBOARD (assets/analytics_overview.png)
# -------------------------------------------------------------------------
def generate_analytics_overview():
    width_px, height_px = 1100, 520
    fig = plt.figure(figsize=(11, 5.2), dpi=100)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, width_px)
    ax.set_ylim(0, height_px)
    ax.axis('off')

    # Canvas
    ax.add_patch(patches.Rectangle((0, 0), width_px, height_px, facecolor='#F8FAFC', edgecolor='none'))

    # Container Card
    container = patches.FancyBboxPatch((20, 18), width_px - 40, height_px - 36,
                                       boxstyle="round,pad=0.2,rounding_size=16",
                                       facecolor='#FFFFFF', edgecolor='#E2E8F0', linewidth=1.5)
    ax.add_patch(container)

    # Title section
    ax.text(50, 475, "ACADEMIC ANALYTICS DASHBOARD",
            fontsize=11, fontweight='bold', color='#4F46E5', fontfamily=FONT_FAMILY)
    ax.text(50, 448, "Cohort Performance, Departmental Variations & Statistical Indicators",
            fontsize=17, fontweight='bold', color='#0F172A', fontfamily=FONT_FAMILY)

    # 4 Metric Cards Across
    metric_cards = [
        ("84.00%", "Class Pass Rate", "21 Passed / 4 Failed", "#059669", "#ECFDF5", "#A7F3D0"),
        ("65.35%", "Cohort Average", "Std Dev: 18.98% | Med: 65%", "#4F46E5", "#EEF2FF", "#C7D2FE"),
        ("79.00%", "Attendance Average", "6 Flagged (<75% threshold)", "#0284C7", "#F0F9FF", "#BAE6FD"),
        ("67.56%", "Highest Subject Avg", "Statistics (Python: 64.9%, Math: 63.6%)", "#D97706", "#FFFBEB", "#FDE68A")
    ]

    mc_w = 232
    mc_x = 50
    for val, label, sub, col, bg_col, bdr_col in metric_cards:
        box = patches.FancyBboxPatch((mc_x, 345), mc_w, 80,
                                     boxstyle="round,pad=0.2,rounding_size=10",
                                     facecolor=bg_col, edgecolor=bdr_col, linewidth=1.2)
        ax.add_patch(box)
        ax.text(mc_x + 14, 398, val, fontsize=17, fontweight='bold', color=col, fontfamily=FONT_FAMILY)
        ax.text(mc_x + 14, 378, label, fontsize=11, fontweight='bold', color='#1E293B', fontfamily=FONT_FAMILY)
        ax.text(mc_x + 14, 358, sub, fontsize=8.8, color='#64748B', fontfamily=FONT_FAMILY)
        mc_x += mc_w + 24

    # Two side-by-side analytical panels
    # Left Panel: Subject-wise Comparison
    lp = patches.FancyBboxPatch((50, 50), 475, 270,
                                boxstyle="round,pad=0.2,rounding_size=12",
                                facecolor='#F8FAFC', edgecolor='#E2E8F0', linewidth=1)
    ax.add_patch(lp)
    ax.text(70, 290, "Subject Performance Breakdown", fontsize=13, fontweight='bold', color='#0F172A', fontfamily=FONT_FAMILY)

    subjects = [
        ("Statistics", 67.56, 19.17, "24 / 25 Passed (96%)", "#10B981"),
        ("Python", 64.88, 21.05, "22 / 25 Passed (88%)", "#3B82F6"),
        ("Mathematics", 63.60, 19.67, "22 / 25 Passed (88%)", "#6366F1")
    ]

    sy = 240
    for subj, avg, std, pass_str, bar_col in subjects:
        ax.text(70, sy, subj, fontsize=11.5, fontweight='bold', color='#1E293B', fontfamily=FONT_FAMILY)
        ax.text(200, sy, f"{avg:.2f}% (σ = {std:.2f})", fontsize=10.5, color='#475569', fontfamily=FONT_FAMILY)
        ax.text(370, sy, pass_str, fontsize=9.5, color='#059669', fontfamily=FONT_FAMILY)

        # Progress bar
        bar_bg = patches.FancyBboxPatch((70, sy - 18), 430, 8, boxstyle="round,pad=0.1,rounding_size=4",
                                       facecolor='#E2E8F0', edgecolor='none')
        ax.add_patch(bar_bg)
        bar_fill = patches.FancyBboxPatch((70, sy - 18), 430 * (avg / 100), 8, boxstyle="round,pad=0.1,rounding_size=4",
                                         facecolor=bar_col, edgecolor='none')
        ax.add_patch(bar_fill)
        sy -= 55

    ax.text(70, 70, "• Statistics demonstrated the highest average and highest pass rate.",
            fontsize=9.5, color='#64748B', fontfamily=FONT_FAMILY)

    # Right Panel: Department Cohort Comparison
    rp = patches.FancyBboxPatch((555, 50), 495, 270,
                                boxstyle="round,pad=0.2,rounding_size=12",
                                facecolor='#F8FAFC', edgecolor='#E2E8F0', linewidth=1)
    ax.add_patch(rp)
    ax.text(575, 290, "Departmental Performance & Attendance", fontsize=13, fontweight='bold', color='#0F172A', fontfamily=FONT_FAMILY)

    depts = [
        ("Computer Science", "7 Students", "72.05%", "85.71%", "81.07%", "#3B82F6"),
        ("Information Tech.", "6 Students", "71.22%", "83.33%", "82.42%", "#10B981"),
        ("Data Science", "6 Students", "62.56%", "83.33%", "80.17%", "#F59E0B"),
        ("Electronics", "6 Students", "54.44%", "83.33%", "72.00%", "#EF4444")
    ]

    dy = 245
    # Table header
    ax.text(575, dy, "Department", fontsize=10, fontweight='bold', color='#64748B', fontfamily=FONT_FAMILY)
    ax.text(730, dy, "Students", fontsize=10, fontweight='bold', color='#64748B', fontfamily=FONT_FAMILY)
    ax.text(810, dy, "Average", fontsize=10, fontweight='bold', color='#64748B', fontfamily=FONT_FAMILY)
    ax.text(890, dy, "Pass Rate", fontsize=10, fontweight='bold', color='#64748B', fontfamily=FONT_FAMILY)
    ax.text(975, dy, "Attendance", fontsize=10, fontweight='bold', color='#64748B', fontfamily=FONT_FAMILY)

    dy -= 28
    for dname, cnt, avg_str, pass_str, att_str, dot_col in depts:
        ax.plot(580, dy + 4, marker='o', color=dot_col, markersize=6)
        ax.text(595, dy, dname, fontsize=10.5, fontweight='bold', color='#1E293B', fontfamily=FONT_FAMILY)
        ax.text(730, dy, cnt, fontsize=10, color='#475569', fontfamily=FONT_FAMILY)
        ax.text(810, dy, avg_str, fontsize=10.5, fontweight='bold', color='#4F46E5', fontfamily=FONT_FAMILY)
        ax.text(890, dy, pass_str, fontsize=10, color='#059669', fontfamily=FONT_FAMILY)
        ax.text(975, dy, att_str, fontsize=10, color='#334155', fontfamily=FONT_FAMILY)
        dy -= 34

    ax.text(575, 70, "• CS scored the highest average (72.05%), Electronics had lowest (54.44%).",
            fontsize=9.5, color='#64748B', fontfamily=FONT_FAMILY)

    out_path = ASSETS_DIR / "analytics_overview.png"
    plt.savefig(out_path, dpi=100, bbox_inches='tight', pad_inches=0.05, facecolor='#F8FAFC')
    plt.close()
    print(f"Created: {out_path}")


# -------------------------------------------------------------------------
# 4. GRADING RUBRIC CARD (assets/grading_rubric_light.png)
# -------------------------------------------------------------------------
def generate_grading_rubric():
    width_px, height_px = 1000, 480
    fig = plt.figure(figsize=(10, 4.8), dpi=100)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, width_px)
    ax.set_ylim(0, height_px)
    ax.axis('off')

    # Canvas
    ax.add_patch(patches.Rectangle((0, 0), width_px, height_px, facecolor='#F8FAFC', edgecolor='none'))

    # Container Card
    container = patches.FancyBboxPatch((20, 18), width_px - 40, height_px - 36,
                                       boxstyle="round,pad=0.2,rounding_size=16",
                                       facecolor='#FFFFFF', edgecolor='#E2E8F0', linewidth=1.5)
    ax.add_patch(container)

    # Title section
    ax.text(50, 435, "ACADEMIC POLICY & EVALUATION STANDARDS",
            fontsize=11, fontweight='bold', color='#4F46E5', fontfamily=FONT_FAMILY)
    ax.text(50, 408, "7-Tier Educational Grade Bands & Decision Rubric",
            fontsize=17, fontweight='bold', color='#0F172A', fontfamily=FONT_FAMILY)

    # Table Headers
    cols = [50, 180, 410, 750]
    headers = ["Grade Band", "Percentage Range", "Academic Standing", "Subject Criterion"]

    # Header bar
    h_bar = patches.FancyBboxPatch((40, 360), 920, 30, boxstyle="round,pad=0.1,rounding_size=6",
                                   facecolor='#F1F5F9', edgecolor='none')
    ax.add_patch(h_bar)
    for c, h in zip(cols, headers):
        ax.text(c, 372, h, fontsize=10.5, fontweight='bold', color='#334155', fontfamily=FONT_FAMILY)

    # Grade Rows
    rows = [
        ("A+", "90.0% – 100.0%", "Outstanding Mastery / Honors", "Pass (All >= 35)", "#059669", "#ECFDF5", "#A7F3D0"),
        ("A",  "80.0% – <90.0%",  "Excellent Performance",        "Pass (All >= 35)", "#0D9488", "#F0FDFA", "#99F6E4"),
        ("B",  "70.0% – <80.0%",  "Very Good Understanding",      "Pass (All >= 35)", "#0284C7", "#F0F9FF", "#BAE6FD"),
        ("C",  "60.0% – <70.0%",  "Good / Above Average",         "Pass (All >= 35)", "#2563EB", "#EFF6FF", "#BFDBFE"),
        ("D",  "50.0% – <60.0%",  "Satisfactory Performance",     "Pass (All >= 35)", "#D97706", "#FFFBEB", "#FDE68A"),
        ("E",  "35.0% – <50.0%",  "Marginal Pass (Threshold)",    "Pass (All >= 35)", "#EA580C", "#FFF7ED", "#FED7AA"),
        ("F",  "Below 35.0%",     "Unsatisfactory / Academic Fail", "Fail (<35 in any)", "#DC2626", "#FEF2F2", "#FECACA")
    ]

    gy = 328
    for grade, rng, standing, criterion, col, bg_col, bdr_col in rows:
        # Grade Badge
        gb = patches.FancyBboxPatch((cols[0], gy - 5), 52, 24, boxstyle="round,pad=0.2,rounding_size=6",
                                    facecolor=bg_col, edgecolor=bdr_col, linewidth=1)
        ax.add_patch(gb)
        ax.text(cols[0] + 26, gy + 7, grade, fontsize=11, fontweight='bold', color=col,
                ha='center', va='center', fontfamily=FONT_FAMILY)

        ax.text(cols[1], gy + 7, rng, fontsize=10.5, color='#1E293B', va='center', fontfamily=FONT_FAMILY)
        ax.text(cols[2], gy + 7, standing, fontsize=10.5, color='#475569', va='center', fontfamily=FONT_FAMILY)

        c_col = '#059669' if 'Pass' in criterion else '#DC2626'
        ax.text(cols[3], gy + 7, criterion, fontsize=10.5, fontweight='bold', color=c_col, va='center', fontfamily=FONT_FAMILY)

        # Thin divider
        ax.plot([40, 960], [gy - 12, gy - 12], color='#F1F5F9', lw=1)
        gy -= 38

    # Important rule note at bottom
    note_box = patches.FancyBboxPatch((40, 36), 920, 34, boxstyle="round,pad=0.2,rounding_size=8",
                                      facecolor='#F8FAFC', edgecolor='#CBD5E1', linewidth=1)
    ax.add_patch(note_box)
    ax.text(500, 53, "Crucial Policy: A student passes only if score >= 35 in Python, Math & Stats. Attendance < 75% is flagged separately without mark deduction.",
            fontsize=9.2, color='#475569', ha='center', va='center', fontfamily=FONT_FAMILY)

    out_path = ASSETS_DIR / "grading_rubric_light.png"
    plt.savefig(out_path, dpi=100, bbox_inches='tight', pad_inches=0.05, facecolor='#F8FAFC')
    plt.close()
    print(f"Created: {out_path}")


# -------------------------------------------------------------------------
# 5. TOP PERFORMERS LEADERBOARD (assets/top_performers_light.png)
# -------------------------------------------------------------------------
def generate_top_performers():
    width_px, height_px = 1000, 440
    fig = plt.figure(figsize=(10, 4.4), dpi=100)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, width_px)
    ax.set_ylim(0, height_px)
    ax.axis('off')

    # Canvas
    ax.add_patch(patches.Rectangle((0, 0), width_px, height_px, facecolor='#F8FAFC', edgecolor='none'))

    # Container Card
    container = patches.FancyBboxPatch((20, 18), width_px - 40, height_px - 36,
                                       boxstyle="round,pad=0.2,rounding_size=16",
                                       facecolor='#FFFFFF', edgecolor='#E2E8F0', linewidth=1.5)
    ax.add_patch(container)

    # Title section
    ax.text(50, 395, "ACADEMIC EXCELLENCE & HONOR ROLL",
            fontsize=11, fontweight='bold', color='#4F46E5', fontfamily=FONT_FAMILY)
    ax.text(50, 368, "Top 5 Academic Performers (Overall Average Ranking)",
            fontsize=17, fontweight='bold', color='#0F172A', fontfamily=FONT_FAMILY)

    # Top 5 Data from verified dataset
    top_5 = [
        ("Rank #1", "S101", "Aarav Sharma", "Computer Science", 4, "93.67%", "A+", "92.5%", "#D97706", "#FFFBEB", "#FDE68A"),
        ("Rank #2", "S102", "Diya Patel", "Information Technology", 4, "90.33%", "A+", "88.0%", "#64748B", "#F1F5F9", "#CBD5E1"),
        ("Rank #3", "S122", "Simran Kaur", "Data Science", 6, "90.00%", "A+", "89.0%", "#B45309", "#FEF3C7", "#FDE68A"),
        ("Rank #4", "S104", "Ananya Iyer", "Computer Science", 4, "88.00%", "A", "94.0%", "#475569", "#F8FAFC", "#E2E8F0"),
        ("Rank #5", "S124", "Meera Menon", "Information Technology", 4, "86.00%", "A", "96.0%", "#475569", "#F8FAFC", "#E2E8F0"),
    ]

    cols = [50, 160, 240, 480, 680, 780, 880]
    headers = ["Rank", "ID", "Student Name", "Department", "Semester", "Average", "Grade"]

    # Header bar
    h_bar = patches.FancyBboxPatch((40, 320), 920, 30, boxstyle="round,pad=0.1,rounding_size=6",
                                   facecolor='#F1F5F9', edgecolor='none')
    ax.add_patch(h_bar)
    for c, h in zip(cols, headers):
        ax.text(c, 332, h, fontsize=10.5, fontweight='bold', color='#334155', fontfamily=FONT_FAMILY)

    py = 285
    for rank, sid, name, dept, sem, avg, grade, att, r_col, r_bg, r_bdr in top_5:
        # Rank Pill
        rp = patches.FancyBboxPatch((cols[0], py - 5), 82, 24, boxstyle="round,pad=0.2,rounding_size=8",
                                    facecolor=r_bg, edgecolor=r_bdr, linewidth=1)
        ax.add_patch(rp)
        ax.text(cols[0] + 41, py + 7, rank, fontsize=10.5, fontweight='bold', color=r_col,
                ha='center', va='center', fontfamily=FONT_FAMILY)

        ax.text(cols[1], py + 7, sid, fontsize=10.5, color='#64748B', va='center', fontfamily=FONT_FAMILY)
        ax.text(cols[2], py + 7, name, fontsize=11, fontweight='bold', color='#0F172A', va='center', fontfamily=FONT_FAMILY)
        ax.text(cols[3], py + 7, dept, fontsize=10.5, color='#334155', va='center', fontfamily=FONT_FAMILY)
        ax.text(cols[4], py + 7, f"Sem {sem}", fontsize=10.5, color='#64748B', va='center', fontfamily=FONT_FAMILY)
        ax.text(cols[5], py + 7, avg, fontsize=11.5, fontweight='bold', color='#4F46E5', va='center', fontfamily=FONT_FAMILY)

        # Grade Pill
        gp = patches.FancyBboxPatch((cols[6], py - 5), 44, 24, boxstyle="round,pad=0.2,rounding_size=6",
                                    facecolor='#ECFDF5', edgecolor='#A7F3D0', linewidth=1)
        ax.add_patch(gp)
        ax.text(cols[6] + 22, py + 7, grade, fontsize=10.5, fontweight='bold', color='#059669',
                ha='center', va='center', fontfamily=FONT_FAMILY)

        # Divider
        ax.plot([40, 960], [py - 12, py - 12], color='#F1F5F9', lw=1)
        py -= 42

    # Bottom note
    ax.text(500, 36, "Tie Handling: If students share identical averages, rankings preserve relative order without skipping positions.",
            fontsize=9.5, color='#64748B', ha='center', fontfamily=FONT_FAMILY)

    out_path = ASSETS_DIR / "top_performers_light.png"
    plt.savefig(out_path, dpi=100, bbox_inches='tight', pad_inches=0.05, facecolor='#F8FAFC')
    plt.close()
    print(f"Created: {out_path}")


# -------------------------------------------------------------------------
# 6. LINKEDIN POST SHOWCASE IMAGE (image.png & assets/linkedin_showcase.png)
# -------------------------------------------------------------------------
def generate_linkedin_image():
    width_px, height_px = 1200, 675  # Standard 16:9 / LinkedIn landscape image
    fig = plt.figure(figsize=(12, 6.75), dpi=100)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, width_px)
    ax.set_ylim(0, height_px)
    ax.axis('off')

    # Canvas
    ax.add_patch(patches.Rectangle((0, 0), width_px, height_px, facecolor='#F8FAFC', edgecolor='none'))

    # Soft glowing background aesthetic
    g1 = patches.Circle((150, 600), 280, facecolor='#EEF2FF', edgecolor='none', alpha=0.6)
    g2 = patches.Circle((1050, 120), 260, facecolor='#ECFDF5', edgecolor='none', alpha=0.6)
    ax.add_patch(g1)
    ax.add_patch(g2)

    # Master Frame
    frame = patches.FancyBboxPatch((24, 20), width_px - 48, height_px - 40,
                                   boxstyle="round,pad=0.2,rounding_size=20",
                                   facecolor='#FFFFFF', edgecolor='#E2E8F0', linewidth=1.8)
    ax.add_patch(frame)

    # Top Brand / Course Pill
    course_pill = patches.FancyBboxPatch((60, 595), 360, 30,
                                         boxstyle="round,pad=0.2,rounding_size=15",
                                         facecolor='#EEF2FF', edgecolor='#C7D2FE', linewidth=1)
    ax.add_patch(course_pill)
    ax.text(76, 610, "EWB COURSES • PYTHON WITH AI INTERNSHIP",
            fontsize=10, fontweight='bold', color='#4338CA', va='center', fontfamily=FONT_FAMILY)

    # Status Pill on Top Right
    status_pill = patches.FancyBboxPatch((960, 595), 180, 30,
                                         boxstyle="round,pad=0.2,rounding_size=15",
                                         facecolor='#ECFDF5', edgecolor='#A7F3D0', linewidth=1)
    ax.add_patch(status_pill)
    ax.text(1050, 610, "18/18 Tests Passed (100%)",
            fontsize=9.5, fontweight='bold', color='#059669', ha='center', va='center', fontfamily=FONT_FAMILY)

    # Main Project Title
    ax.text(60, 545, "Student Performance Analytics System",
            fontsize=26, fontweight='bold', color='#0F172A', fontfamily=FONT_FAMILY)

    # Subtitle / Impact Statement
    ax.text(60, 508, "Automated End-to-End Academic Evaluation, Statistical Profiling & Cohort Reporting in Python",
            fontsize=13, color='#475569', fontfamily=FONT_FAMILY)

    # 4 Core KPI Bento Cards (Horizontal)
    kpis = [
        ("84.00%", "Academic Pass Rate", "21 Passed / 4 Failed", "#059669", "#ECFDF5", "#A7F3D0"),
        ("65.35%", "Class Overall Avg", "Std Dev: 18.98% | Med: 65%", "#4F46E5", "#EEF2FF", "#C7D2FE"),
        ("79.00%", "Attendance Avg", "6 Students < 75% Flagged", "#0284C7", "#F0F9FF", "#BAE6FD"),
        ("93.67%", "Top Score (Rank #1)", "Aarav Sharma (S101)", "#D97706", "#FFFBEB", "#FDE68A")
    ]

    kx = 60
    kw = 252
    for val, label, note, col, bg_col, bdr_col in kpis:
        kbox = patches.FancyBboxPatch((kx, 395), kw, 85,
                                     boxstyle="round,pad=0.2,rounding_size=12",
                                     facecolor=bg_col, edgecolor=bdr_col, linewidth=1.2)
        ax.add_patch(kbox)
        ax.text(kx + 16, 452, val, fontsize=18, fontweight='bold', color=col, fontfamily=FONT_FAMILY)
        ax.text(kx + 16, 430, label, fontsize=11, fontweight='bold', color='#1E293B', fontfamily=FONT_FAMILY)
        ax.text(kx + 16, 410, note, fontsize=9.2, color='#64748B', fontfamily=FONT_FAMILY)
        kx += kw + 24

    # Bottom Middle 3 Feature Columns
    col_w = 338
    # Column 1: Pipeline & Architecture
    c1 = patches.FancyBboxPatch((60, 115), col_w, 255,
                               boxstyle="round,pad=0.2,rounding_size=12",
                               facecolor='#F8FAFC', edgecolor='#E2E8F0', linewidth=1)
    ax.add_patch(c1)
    ax.plot(82, 335, marker='s', color='#4F46E5', markersize=6)
    ax.text(94, 335, "Data Pipeline Architecture", fontsize=12.5, fontweight='bold', color='#0F172A', va='center', fontfamily=FONT_FAMILY)
    p_steps = [
        ("CSV Ingestion & Validation", "data/students.csv schema, duplicate IDs"),
        ("Pure Function Computation", "totals, averages, letter grades"),
        ("Multi-Subject Pass Rule", "must score >= 35 in all 3 subjects"),
        ("Attendance Segregation", "attendance < 75% isolated from marks"),
        ("12 Key Analytical Answers", "department & semester breakdowns")
    ]
    py = 295
    for title, desc in p_steps:
        ax.plot(84, py + 8, marker='o', color='#6366F1', markersize=4)
        ax.text(94, py + 8, title, fontsize=10, fontweight='bold', color='#334155', fontfamily=FONT_FAMILY)
        ax.text(94, py - 6, desc, fontsize=8.5, color='#64748B', fontfamily=FONT_FAMILY)
        py -= 34

    # Column 2: Statistical Insights
    c2 = patches.FancyBboxPatch((430, 115), col_w, 255,
                               boxstyle="round,pad=0.2,rounding_size=12",
                               facecolor='#F8FAFC', edgecolor='#E2E8F0', linewidth=1)
    ax.add_patch(c2)
    ax.plot(452, 335, marker='s', color='#059669', markersize=6)
    ax.text(464, 335, "Analytical & Statistical Findings", fontsize=12.5, fontweight='bold', color='#0F172A', va='center', fontfamily=FONT_FAMILY)
    stats_data = [
        ("Highest Subject Average", "Statistics (67.56% avg, 96% pass)"),
        ("Highest Performing Dept", "Computer Science (72.05% avg)"),
        ("Lowest Performing Dept", "Electronics (54.44% avg)"),
        ("Semester Contrast", "Sem 4 (67.14%) vs Sem 6 (63.06%)"),
        ("Distribution Quartiles", "Q1: 55%, Median: 65%, Q3: 82%")
    ]
    sy = 295
    for title, desc in stats_data:
        ax.plot(454, sy + 8, marker='o', color='#10B981', markersize=4)
        ax.text(464, sy + 8, title, fontsize=10, fontweight='bold', color='#334155', fontfamily=FONT_FAMILY)
        ax.text(464, sy - 6, desc, fontsize=8.5, color='#64748B', fontfamily=FONT_FAMILY)
        sy -= 34

    # Column 3: Honor Roll / Top Performers
    c3 = patches.FancyBboxPatch((802, 115), col_w, 255,
                               boxstyle="round,pad=0.2,rounding_size=12",
                               facecolor='#F8FAFC', edgecolor='#E2E8F0', linewidth=1)
    ax.add_patch(c3)
    ax.plot(824, 335, marker='s', color='#D97706', markersize=6)
    ax.text(836, 335, "Academic Leaderboard (Top 5)", fontsize=12.5, fontweight='bold', color='#0F172A', va='center', fontfamily=FONT_FAMILY)
    top_records = [
        ("1. Aarav Sharma (S101)", "CS", "93.67%", "A+"),
        ("2. Diya Patel (S102)", "IT", "90.33%", "A+"),
        ("3. Simran Kaur (S122)", "DS", "90.00%", "A+"),
        ("4. Ananya Iyer (S104)", "CS", "88.00%", "A"),
        ("5. Meera Menon (S124)", "IT", "86.00%", "A")
    ]
    ty = 295
    for name, dept, avg, gr in top_records:
        ax.text(822, ty + 6, name, fontsize=10, fontweight='bold', color='#0F172A', fontfamily=FONT_FAMILY)
        ax.text(822, ty - 8, f"{dept} • {avg}", fontsize=9, color='#4F46E5', fontfamily=FONT_FAMILY)
        # Grade tag
        gt = patches.FancyBboxPatch((1075, ty - 6), 38, 20, boxstyle="round,pad=0.1,rounding_size=4",
                                   facecolor='#ECFDF5', edgecolor='#A7F3D0', linewidth=1)
        ax.add_patch(gt)
        ax.text(1094, ty + 4, gr, fontsize=9, fontweight='bold', color='#059669', ha='center', va='center', fontfamily=FONT_FAMILY)
        ty -= 34

    # Bottom Footer: Tech Stack Chips & Author Credit
    ax.text(60, 52, "Tech Stack:", fontsize=10.5, fontweight='bold', color='#64748B', fontfamily=FONT_FAMILY)
    techs = ["Python 3.11+", "Pandas 2.0+", "NumPy 1.24+", "unittest (18 Tests)", "Pure Functions", "CSV Pipeline"]
    tx = 150
    for t in techs:
        tw = len(t) * 7.5 + 16
        tchip = patches.FancyBboxPatch((tx, 40), tw, 24, boxstyle="round,pad=0.2,rounding_size=12",
                                      facecolor='#F1F5F9', edgecolor='#CBD5E1', linewidth=1)
        ax.add_patch(tchip)
        ax.text(tx + tw / 2, 52, t, fontsize=9, fontweight='bold', color='#334155', ha='center', va='center', fontfamily=FONT_FAMILY)
        tx += tw + 10

    # Right side author credit
    ax.text(1140, 52, "Built by Rajeshwari | EWB Courses",
            fontsize=11, fontweight='bold', color='#4F46E5', ha='right', fontfamily=FONT_FAMILY)

    # Save to root image.png and assets/linkedin_showcase.png
    out_root = ROOT_DIR / "image.png"
    out_assets = ASSETS_DIR / "linkedin_showcase.png"
    out_screenshots = ROOT_DIR / "screenshots" / "image.png"

    plt.savefig(out_root, dpi=100, bbox_inches='tight', pad_inches=0.05, facecolor='#F8FAFC')
    plt.savefig(out_assets, dpi=100, bbox_inches='tight', pad_inches=0.05, facecolor='#F8FAFC')
    plt.savefig(out_screenshots, dpi=100, bbox_inches='tight', pad_inches=0.05, facecolor='#F8FAFC')
    plt.close()
    print(f"Created: {out_root}")
    print(f"Created: {out_assets}")
    print(f"Created: {out_screenshots}")


if __name__ == "__main__":
    print("Generating light-theme visual assets...")
    generate_readme_banner()
    generate_architecture_diagram()
    generate_analytics_overview()
    generate_grading_rubric()
    generate_top_performers()
    generate_linkedin_image()
    print("All assets generated successfully!")
