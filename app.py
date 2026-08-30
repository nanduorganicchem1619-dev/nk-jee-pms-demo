import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(
    page_title="NK JEE PMS",
    page_icon="🎯",
    layout="wide",
)

st.markdown(
    """
    <style>
    .stApp {
        background:
            radial-gradient(circle at 15% 8%, rgba(37, 99, 235, 0.28), transparent 30%),
            radial-gradient(circle at 85% 18%, rgba(124, 58, 237, 0.24), transparent 28%),
            linear-gradient(135deg, #061326 0%, #0b1730 48%, #10112b 100%);
        color: #f8fafc;
    }

    [data-testid="stHeader"] {
        background: transparent;
    }

    .block-container {
        max-width: 1500px;
        padding-top: 3rem;
        padding-bottom: 5rem;
    }

    h1 {
        font-size: 4.3rem !important;
        font-weight: 950 !important;
        letter-spacing: 0.03em;
        background: linear-gradient(90deg, #38bdf8, #818cf8, #c084fc);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    h2 {
        color: #f8fafc !important;
        font-size: 2.4rem !important;
        margin-top: 2.4rem !important;
    }

    h3 {
        color: #f8fafc !important;
        font-size: 2rem !important;
        border-left: 8px solid #fbbf24;
        padding: 16px 22px;
        border-radius: 12px;
        background: rgba(15, 23, 42, 0.78);
    }
        div.stButton > button {
        width: 100%;
        min-height: 64px;
        border-radius: 16px;
        border: 2px solid #fbbf24;
        background: linear-gradient(135deg, #10213f, #1e1b4b);
        color: #ffffff !important;
        font-size: 20px !important;
        font-weight: 900 !important;
        letter-spacing: 0.02em;
        box-shadow: 0 0 20px rgba(251, 191, 36, 0.22);
    }

    div.stButton > button p {
        color: #ffffff !important;
        font-size: 20px !important;
        font-weight: 900 !important;
    }

    div.stButton > button:hover {
        border-color: #fde68a;
        background: linear-gradient(135deg, #17345f, #312e81);
        box-shadow: 0 0 32px rgba(251, 191, 36, 0.55);
        transform: translateY(-2px);
    }

    div.stButton > button:hover p {
        color: #fef3c7 !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

students = pd.DataFrame(
    [
        ["Ananya", 45, 50, 40, 50, 55, 45],
        ["Rahul", 55, 42, 48, 52, 46, 52],
        ["Meghana", 58, 61, 54, 64, 66, 58],
        ["Arjun", 62, 58, 57, 68, 63, 61],
        ["Sanjana", 48, 52, 44, 54, 57, 49],
        ["Karthik", 51, 47, 50, 48, 44, 46],
        ["Divya", 60, 56, 59, 62, 60, 63],
        ["Vikram", 42, 46, 38, 47, 50, 41],
        ["Priya", 57, 63, 52, 54, 60, 49],
        ["Aditya", 49, 44, 43, 53, 48, 46],
    ],
    columns=[
        "Student",
        "GT1 Physics",
        "GT1 Chemistry",
        "GT1 Maths",
        "GT2 Physics",
        "GT2 Chemistry",
        "GT2 Maths",
    ],
)

students["GT1 Total"] = students[
    ["GT1 Physics", "GT1 Chemistry", "GT1 Maths"]
].sum(axis=1)

students["GT2 Total"] = students[
    ["GT2 Physics", "GT2 Chemistry", "GT2 Maths"]
].sum(axis=1)

students["Change"] = students["GT2 Total"] - students["GT1 Total"]
students["Distance from 180"] = 180 - students["GT2 Total"]

total_students = len(students)
gt1_average = students["GT1 Total"].mean()
gt2_average = students["GT2 Total"].mean()
batch_improvement = gt2_average - gt1_average

gt1_reached_180 = int((students["GT1 Total"] >= 180).sum())
gt2_reached_180 = int((students["GT2 Total"] >= 180).sum())

moving_closer = int(
    ((students["Change"] > 0) & (students["GT2 Total"] < 180)).sum()
)
moving_away = int((students["Change"] < 0).sum())

need_attention = int(
    ((students["GT2 Total"] < 150) | (students["Change"] < 0)).sum()
)


def show_card(title, value, colour, note=""):
    st.markdown(
        f'<div style="min-height:170px;padding:24px 18px;border-radius:22px;'
        f'background:#111c35;border:1px solid {colour};border-top:6px solid {colour};'
        f'box-shadow:0 0 24px {colour}33;text-align:center;">'
        f'<div style="color:{colour};font-size:19px;font-weight:900;">{title}</div>'
        f'<div style="color:white;font-size:50px;font-weight:950;margin-top:10px;">{value}</div>'
        f'<div style="color:#cbd5e1;font-size:16px;margin-top:6px;">{note}</div>'
        f'</div>',
        unsafe_allow_html=True,
    )


st.markdown(
    '<div style="width:100%;margin:0 auto 26px;text-align:center;">'
    '<div style="color:#7dd3fc;font-size:52px;font-weight:950;'
    'letter-spacing:0.04em;text-shadow:0 0 20px rgba(56,189,248,0.55);">'
    'VISHRA JUNIOR COLLEGE</div>'
    '<div style="color:white;font-size:25px;font-weight:850;'
    'margin-top:7px;">BALAPUR, HYDERABAD</div>'
    '<div style="display:inline-block;margin-top:17px;padding:10px 24px;'
    'border-radius:14px;background:#111c35;border:1px solid #a78bfa;'
    'color:#c4b5fd;font-size:23px;font-weight:900;">'
    'NK JEE - PERFORMANCE MONITORING SYSTEM<br><span style="font-size:18px;color:white;">DEMO</span></div></div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div style="margin:10px 0 28px;padding:22px 28px;border-radius:20px;'
    'background:#111c35;border:1px solid #38bdf8;text-align:center;'
    'box-shadow:0 0 22px rgba(56,189,248,0.16);">'
    '<div style="color:#7dd3fc;font-size:27px;font-weight:950;margin-bottom:14px;">PURPOSE OF THIS SYSTEM</div>'
    '<div style="color:white;font-size:19px;line-height:1.9;">'
    '1. See where the batch and each student stand after every test.<br>'
    '2. Identify who needs attention and how many marks each student needs to reach 180.<br>'
    '3. Help teachers guide students to improve their scores and strengthen their chances of NIT admission.'
    '</div></div>',
    unsafe_allow_html=True,
)
st.subheader('V1: "WHERE IS MY STUDENT?"')

st.markdown(
    '<div style="margin:20px 0 34px;padding:24px 30px;border-radius:22px;'
    'background:#080b12;border:2px solid #fbbf24;'
    'box-shadow:0 0 30px rgba(251,191,36,0.30);text-align:center;">'
    '<div style="color:white;font-size:24px;font-weight:850;">OUR TARGET FOR EVERY STUDENT</div>'
    '<div style="color:#fbbf24;font-size:54px;font-weight:950;'
    'text-shadow:0 0 16px #f59e0b;">180 / 300</div>'
    '<div style="color:#fde68a;font-size:21px;font-weight:800;">'
            'OUR COLLEGE WORKING TARGET</div>'
    '<div style="color:#cbd5e1;font-size:16px;margin-top:7px;">'
    'Our planning target — not an official cutoff or seat guarantee.</div>'
    '</div>',
    unsafe_allow_html=True,
)

st.markdown("## 1. GT1 TO GT2 — WHAT CHANGED?")

st.markdown(
    '<div style="margin:10px 0 22px;padding:16px 22px;border-radius:16px;'
    'background:#111c35;border:1px solid #38bdf8;text-align:center;">'
    '<span style="color:#94a3b8;font-size:22px;font-weight:900;">GT1 — FIRST TEST</span>'
    '<span style="color:#fbbf24;font-size:30px;font-weight:950;margin:0 24px;">→</span>'
    '<span style="color:#38bdf8;font-size:22px;font-weight:900;">GT2 — LATEST TEST</span>'
    '</div>',
    unsafe_allow_html=True,
)

comparison_columns = st.columns(4)

with comparison_columns[0]:
    show_card(
        "GT1 — FIRST-TEST AVERAGE",
        f"{gt1_average:.1f}",
        "#94a3b8",
        "Average total of all 10 students",
    )

with comparison_columns[1]:
    show_card(
        "GT2 — LATEST-TEST AVERAGE",
        f"{gt2_average:.1f}",
        "#38bdf8",
        "Average total of all 10 students",
    )

with comparison_columns[2]:
    show_card(
        "BATCH IMPROVED BY",
        f"+{batch_improvement:.1f}",
        "#22c55e",
        "marks from GT1 to GT2",
    )

with comparison_columns[3]:
    show_card(
        "STUDENTS REACHING 180",
        f"{gt1_reached_180} → {gt2_reached_180}",
        "#fbbf24",
        "GT1 → GT2",
    )

st.markdown(
    f'<div style="margin:20px 0;padding:18px 24px;border-radius:18px;'
    f'background:#123524;border:1px solid #22c55e;text-align:center;">'
    f'<span style="color:#dcfce7;font-size:22px;font-weight:850;">'
    f'The batch average increased from {gt1_average:.1f} to {gt2_average:.1f}. '
    f'That is an improvement of {batch_improvement:.1f} marks.</span>'
    f'</div>',
    unsafe_allow_html=True,
)

st.markdown("## 2. AFTER GT2 — WHERE IS THE BATCH?")

st.markdown(
    '<div style="margin:10px 0 22px;padding:15px 22px;border-radius:16px;'
    'background:#111c35;border:1px solid #64748b;text-align:center;'
    'color:#e2e8f0;font-size:18px;">'
    'The three student groups below add up to all 10 students.'
    '</div>',
    unsafe_allow_html=True,
)

position_columns = st.columns(4)

with position_columns[0]:
    show_card(
        "TOTAL STUDENTS",
        total_students,
        "#38bdf8",
        "entire demo batch",
    )

with position_columns[1]:
    show_card(
        "REACHED 180",
        gt2_reached_180,
        "#22c55e",
        "target reached in GT2",
    )

with position_columns[2]:
    show_card(
        "IMPROVED, BELOW 180",
        moving_closer,
        "#06b6d4",
        "score increased in GT2",
    )

with position_columns[3]:
    show_card(
        "SCORE DECREASED",
        moving_away,
        "#ef4444",
        "score fell in GT2",
    )

st.markdown(
    f'<div style="margin:22px 0;padding:18px 24px;border-radius:18px;'
    f'background:#33210a;border:1px solid #f59e0b;'
    f'box-shadow:0 0 20px rgba(245,158,11,0.15);">'
    f'<span style="color:#fbbf24;font-size:24px;font-weight:900;">'
    f'⚠ {need_attention} STUDENTS NEED OUR ATTENTION</span>'
        '<div style="color:#fde68a;font-size:16px;margin-top:6px;"><b>Karthik:</b> GT1 148 &rarr; GT2 138 &mdash; decreased by 10<br><b>Priya:</b> GT1 172 &rarr; GT2 163 &mdash; decreased by 9<br><b>Vikram:</b> GT1 126 &rarr; GT2 138 &mdash; improved by 12, but still below 150<br><b>Aditya:</b> GT1 136 &rarr; GT2 147 &mdash; improved by 11, but still below 150.</div>',
    unsafe_allow_html=True,
)

st.markdown("## 3. EACH STUDENT — GT1 AND GT2")

st.markdown(
    '<div style="margin:10px 0 20px;padding:15px 22px;border-radius:16px;'
    'background:#111c35;border:1px solid #64748b;text-align:center;'
    'color:#e2e8f0;font-size:18px;">'
    '<b style="color:#94a3b8;">GREY = GT1 FIRST TEST</b>'
    '<span style="margin:0 16px;">•</span>'
    '<b style="color:#06b6d4;">CYAN = IMPROVED IN GT2</b>'
    '<span style="margin:0 16px;">•</span>'
    '<b style="color:#22c55e;">GREEN = REACHED 180</b>'
    '<span style="margin:0 16px;">•</span>'
    '<b style="color:#ef4444;">RED = SCORE DECREASED</b>'
    '</div>',
    unsafe_allow_html=True,
)

gt2_colours = []

for _, student in students.iterrows():
    if student["GT2 Total"] >= 180:
        gt2_colours.append("#22c55e")
    elif student["Change"] > 0:
        gt2_colours.append("#06b6d4")
    else:
        gt2_colours.append("#ef4444")

movement_chart = go.Figure()

movement_chart.add_trace(
    go.Bar(
        name="GT1 — First Test",
        x=students["Student"],
        y=students["GT1 Total"],
        texttemplate="<b>GT1</b><br>%{y}",
        textposition="inside",
        marker_color="#64748b",
        hovertemplate="<b>%{x}</b><br>GT1 first test: %{y}<extra></extra>",
    )
)

movement_chart.add_trace(
    go.Bar(
        name="GT2 — Latest Test",
        x=students["Student"],
        y=students["GT2 Total"],
        texttemplate="<b>GT2</b><br>%{y}",
        textposition="inside",
        marker_color=gt2_colours,
        hovertemplate="<b>%{x}</b><br>GT2 latest test: %{y}<extra></extra>",
    )
)

movement_chart.add_hline(
    y=180,
    layer="below",
    line_width=5,
    line_dash="dash",
    line_color="#fbbf24",
    annotation_text="OUR TARGET: 180",
    annotation_position="top left",
    annotation_font=dict(color="#fbbf24", size=22),
)

movement_chart.update_layout(
    height=620,
    barmode="group",
    showlegend=False,
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(8,15,32,0.88)",
    font=dict(color="#f8fafc", size=18),
    margin=dict(l=30, r=30, t=40, b=30),
    xaxis=dict(
        title="Student",
        tickfont=dict(size=16),
        gridcolor="rgba(255,255,255,0.05)",
    ),
    yaxis=dict(
        title="Total Marks out of 300",
        range=[0, 215],
        tickfont=dict(size=16),
        gridcolor="rgba(255,255,255,0.10)",
    ),
)

st.plotly_chart(
    movement_chart,
    use_container_width=True,
    config={"displayModeBar": False},
)

st.markdown("## 4. FIND ONE STUDENT")

st.markdown(
    '<div style="margin:10px 0 18px;padding:15px 22px;border-radius:16px;'
    'background:#111c35;border:1px solid #38bdf8;'
    'color:#e2e8f0;font-size:18px;">'
    'Select a student to see the first-test score, latest-test score, '
    'distance from 180 and subject-wise change.'
    '</div>',
    unsafe_allow_html=True,
)

selected_student_name = st.selectbox(
    "SELECT STUDENT",
    students["Student"].tolist(),
)

selected_student = students[
    students["Student"] == selected_student_name
].iloc[0]

student_gt1_total = int(selected_student["GT1 Total"])
student_gt2_total = int(selected_student["GT2 Total"])
student_change = int(selected_student["Change"])

if student_gt2_total >= 180:
    distance_text = f"Reached by +{student_gt2_total - 180}"
    distance_colour = "#22c55e"
else:
    distance_text = f"{180 - student_gt2_total} marks"
    distance_colour = "#fbbf24"

physics_change = int(
    selected_student["GT2 Physics"] - selected_student["GT1 Physics"]
)
chemistry_change = int(
    selected_student["GT2 Chemistry"] - selected_student["GT1 Chemistry"]
)
maths_change = int(
    selected_student["GT2 Maths"] - selected_student["GT1 Maths"]
)

subject_changes = {
    "Physics": physics_change,
    "Chemistry": chemistry_change,
    "Maths": maths_change,
}

best_subject = max(subject_changes, key=subject_changes.get)
best_change = subject_changes[best_subject]

lowest_subject = min(subject_changes, key=subject_changes.get)
lowest_change = subject_changes[lowest_subject]

if best_change > 0:
    helped_text = f"{best_subject} +{best_change}"
else:
    helped_text = "No subject increased"

if lowest_change < 0:
    reduced_text = f"{lowest_subject} {lowest_change}"
else:
    reduced_text = "No subject decreased"

st.markdown(
    f'<div style="margin:18px 0;padding:20px 26px;border-radius:18px;'
    f'background:#080b12;border:1px solid #818cf8;text-align:center;">'
    f'<span style="color:#a5b4fc;font-size:30px;font-weight:950;">'
    f'{selected_student_name}</span>'
    f'</div>',
    unsafe_allow_html=True,
)

student_columns_1 = st.columns(4)

with student_columns_1[0]:
    show_card(
        "GT1 — FIRST TEST",
        student_gt1_total,
        "#94a3b8",
        "total out of 300",
    )

with student_columns_1[1]:
    show_card(
        "GT2 — LATEST TEST",
        student_gt2_total,
        "#38bdf8",
        "total out of 300",
    )

with student_columns_1[2]:
    change_colour = "#22c55e" if student_change >= 0 else "#ef4444"
    change_sign = "+" if student_change > 0 else ""
    show_card(
        "CHANGE",
        f"{change_sign}{student_change}",
        change_colour,
        "GT1 to GT2",
    )

with student_columns_1[3]:
    show_card(
        "DISTANCE FROM 180",
        distance_text,
        distance_colour,
        "marks needed to reach 180",
    )
physics_sign = "+" if physics_change > 0 else ""
chemistry_sign = "+" if chemistry_change > 0 else ""
maths_sign = "+" if maths_change > 0 else ""
total_sign = "+" if student_change > 0 else ""

physics_colour = "#22c55e" if physics_change > 0 else (
    "#ef4444" if physics_change < 0 else "#94a3b8"
)

chemistry_colour = "#22c55e" if chemistry_change > 0 else (
    "#ef4444" if chemistry_change < 0 else "#94a3b8"
)

maths_colour = "#22c55e" if maths_change > 0 else (
    "#ef4444" if maths_change < 0 else "#94a3b8"
)

st.markdown("### SUBJECT-WISE MARKS")

subject_columns = st.columns(3)

with subject_columns[0]:
    show_card(
        "PHYSICS",
        f'{int(selected_student["GT1 Physics"])} → {int(selected_student["GT2 Physics"])}',
        physics_colour,
        f"GT1 → GT2 | Change: {physics_sign}{physics_change}",
    )

with subject_columns[1]:
    show_card(
        "CHEMISTRY",
        f'{int(selected_student["GT1 Chemistry"])} → {int(selected_student["GT2 Chemistry"])}',
        chemistry_colour,
        f"GT1 → GT2 | Change: {chemistry_sign}{chemistry_change}",
    )

with subject_columns[2]:
    show_card(
        "MATHS",
        f'{int(selected_student["GT1 Maths"])} → {int(selected_student["GT2 Maths"])}',
        maths_colour,
        f"GT1 → GT2 | Change: {maths_sign}{maths_change}",
    )

st.markdown(
    f'<div style="margin:20px 0;padding:18px 24px;border-radius:18px;'
    f'background:#111c35;border:1px solid #818cf8;text-align:center;'
    f'color:white;font-size:23px;font-weight:900;">'
    f'Physics {physics_sign}{physics_change} &nbsp; + &nbsp; '
    f'Chemistry {chemistry_sign}{chemistry_change} &nbsp; + &nbsp; '
    f'Maths {maths_sign}{maths_change} &nbsp; = &nbsp; '
    f'Total change {total_sign}{student_change}'
    f'</div>',
    unsafe_allow_html=True,
)
highest_change = max(subject_changes.values())
highest_subjects = [
    subject
    for subject, change in subject_changes.items()
    if change == highest_change
]

lowest_change = min(subject_changes.values())
lowest_subjects = [
    subject
    for subject, change in subject_changes.items()
    if change == lowest_change
]

if highest_change > 0:
        if len(highest_subjects) == 3:
            helped_text = f"ALL 3 SUBJECTS +{highest_change}"
        else:
            helped_text = " and ".join(highest_subjects)
            helped_text = f"{helped_text} +{highest_change}"
else:
    helped_text = "No subject increased"

if lowest_change < 0:
    reduced_text = " and ".join(lowest_subjects)
    reduced_text = f"{reduced_text} {lowest_change}"
else:
    reduced_text = "No subject decreased"
student_columns_2 = st.columns(2)

with student_columns_2[0]:
    helped_colour = "#06b6d4" if best_change > 0 else "#94a3b8"
    show_card(
        "SUBJECT THAT HELPED MOST",
        helped_text,
        helped_colour,
        "largest increase from GT1 to GT2",
    )

with student_columns_2[1]:
    reduced_colour = "#ef4444" if lowest_change < 0 else "#22c55e"
    show_card(
        "SUBJECT THAT REDUCED THE SCORE",
        reduced_text,
        reduced_colour,
        "decrease from GT1 to GT2",
    )

st.markdown(
    '<div style="width:100%;margin:44px auto 34px;padding:42px 30px;'
    'border-radius:24px;background:#03050a;border:2px solid #38bdf8;'
    'box-shadow:0 0 35px rgba(56,189,248,0.30);text-align:center;">'
    '<div style="color:#7dd3fc;font-size:34px;font-weight:950;'
    'text-shadow:0 0 18px rgba(56,189,248,0.75);">'
    'WE KNOW WHO NEEDS HELP.</div>'
    '<div style="color:white;font-size:30px;font-weight:900;margin-top:12px;">'
    'THE NEXT CHALLENGE IS HOW TO HELP EACH STUDENT DIFFERENTLY.'
    '</div></div>',
    unsafe_allow_html=True,
)

st.markdown("## 5. SAME SCORE. SAME GAP. DIFFERENT STUDENTS.")

st.markdown(
    '<div style="margin:10px 0 22px;padding:16px 22px;border-radius:16px;'
    'background:#111c35;border:1px solid #fbbf24;text-align:center;">'
    '<span style="color:white;font-size:22px;font-weight:900;">'
    'Ananya and Rahul both scored 150. Both need 30 more marks to reach 180.'
    '</span></div>',
    unsafe_allow_html=True,
)

comparison_students = st.columns(2)

with comparison_students[0]:
    st.markdown(
        '<div style="min-height:310px;padding:28px;border-radius:24px;'
        'background:#111c35;border:2px solid #a78bfa;'
        'box-shadow:0 0 26px rgba(167,139,250,0.20);">'
        '<div style="color:#c4b5fd;font-size:31px;font-weight:950;'
        'text-align:center;">ANANYA</div>'
        '<div style="color:white;font-size:46px;font-weight:950;'
        'text-align:center;margin:8px 0;">150 / 300</div>'
        '<div style="color:#fbbf24;font-size:23px;font-weight:900;'
        'text-align:center;">30 MARKS FROM 180</div>'
        '<hr style="border-color:#334155;margin:20px 0;">'
        '<div style="color:#e2e8f0;font-size:20px;line-height:1.8;">'
        '<b>Physics:</b> 45 → 50 &nbsp; '
        '<span style="color:#22d3ee;">(+5)</span><br>'
        '<b>Chemistry:</b> 50 → 55 &nbsp; '
        '<span style="color:#22d3ee;">(+5)</span><br>'
        '<b>Maths:</b> 40 → 45 &nbsp; '
        '<span style="color:#22d3ee;">(+5)</span>'
        '</div></div>',
        unsafe_allow_html=True,
    )

with comparison_students[1]:
    st.markdown(
        '<div style="min-height:310px;padding:28px;border-radius:24px;'
        'background:#111c35;border:2px solid #38bdf8;'
        'box-shadow:0 0 26px rgba(56,189,248,0.20);">'
        '<div style="color:#7dd3fc;font-size:31px;font-weight:950;'
        'text-align:center;">RAHUL</div>'
        '<div style="color:white;font-size:46px;font-weight:950;'
        'text-align:center;margin:8px 0;">150 / 300</div>'
        '<div style="color:#fbbf24;font-size:23px;font-weight:900;'
        'text-align:center;">30 MARKS FROM 180</div>'
        '<hr style="border-color:#334155;margin:20px 0;">'
        '<div style="color:#e2e8f0;font-size:20px;line-height:1.8;">'
        '<b>Physics:</b> 55 → 52 &nbsp; '
        '<span style="color:#f87171;">(-3)</span><br>'
        '<b>Chemistry:</b> 42 → 46 &nbsp; '
        '<span style="color:#22d3ee;">(+4)</span><br>'
        '<b>Maths:</b> 48 → 52 &nbsp; '
        '<span style="color:#22d3ee;">(+4)</span>'
        '</div></div>',
        unsafe_allow_html=True,
    )

st.markdown(
    '<div style="width:100%;margin:34px auto 24px;padding:20px 24px;'
    'border-radius:20px;background:#111c35;border:1px solid #818cf8;'
    'text-align:center;">'
    '<div style="color:white;font-size:34px;font-weight:950;">'
    'FOR EXAMPLE, SOME POSSIBLE +30 ROUTES ARE:'
    '</div></div>',
    unsafe_allow_html=True,
)

example_routes = [
    ("EXAMPLE 1", "P +10 | C +10 | M +10", "#38bdf8"),
    ("EXAMPLE 2", "P +10 | C +15 | M +5", "#a78bfa"),
    ("EXAMPLE 3", "P +15 | C +5 | M +10", "#f59e0b"),
    ("EXAMPLE 4", "P +5 | C +15 | M +10", "#22d3ee"),
    ("EXAMPLE 5", "P +20 | C +5 | M +5", "#fb7185"),
    ("EXAMPLE 6", "P +5 | C +10 | M +15", "#34d399"),
    ("EXAMPLE 7", "P +5 | C +5 | M +20", "#c084fc"),
]

first_route_row = st.columns(4)

for route_column, route in zip(first_route_row, example_routes[:4]):
    title, route_text, colour = route

    with route_column:
        st.markdown(
            f'<div style="min-height:155px;padding:22px 14px;'
            f'border-radius:20px;background:#111c35;'
            f'border:1px solid {colour};border-top:5px solid {colour};'
            f'box-shadow:0 0 18px {colour}33;text-align:center;">'
            f'<div style="color:{colour};font-size:18px;font-weight:900;">'
            f'{title}</div>'
            f'<div style="color:white;font-size:24px;font-weight:900;'
            f'margin-top:18px;">{route_text}</div>'
            f'<div style="color:#cbd5e1;font-size:15px;margin-top:10px;">'
            f'Total = +30</div></div>',
            unsafe_allow_html=True,
        )

second_route_row = st.columns(3)

for route_column, route in zip(second_route_row, example_routes[4:]):
    title, route_text, colour = route

    with route_column:
        st.markdown(
            f'<div style="min-height:155px;padding:22px 14px;'
            f'border-radius:20px;background:#111c35;'
            f'border:1px solid {colour};border-top:5px solid {colour};'
            f'box-shadow:0 0 18px {colour}33;text-align:center;">'
            f'<div style="color:{colour};font-size:18px;font-weight:900;">'
            f'{title}</div>'
            f'<div style="color:white;font-size:24px;font-weight:900;'
            f'margin-top:18px;">{route_text}</div>'
            f'<div style="color:#cbd5e1;font-size:15px;margin-top:10px;">'
            f'Total = +30</div></div>',
            unsafe_allow_html=True,
        )

st.markdown(
    '<div style="width:100%;margin:22px auto;padding:17px 24px;'
    'border-radius:18px;background:#111c35;border:1px solid #64748b;'
    'text-align:center;">'
    '<span style="color:#e2e8f0;font-size:18px;font-weight:800;">'
    'These are only examples. Many other mathematical combinations are possible.'
    '</span></div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div style="width:100%;margin:34px auto 24px;padding:28px 26px;'
    'border-radius:22px;background:#2b2108;border:2px solid #fbbf24;'
    'box-shadow:0 0 28px rgba(251,191,36,0.25);text-align:center;">'
    '<div style="color:#fbbf24;font-size:31px;font-weight:950;">'
    'WHICH ROUTE IS BEST FOR ANANYA?</div>'
    '<div style="color:#fbbf24;font-size:31px;font-weight:950;margin-top:8px;">'
    'WHICH ROUTE IS BEST FOR RAHUL?</div>'
    '<div style="color:white;font-size:26px;font-weight:900;margin-top:20px;">'
    'BEST ROUTE IN V1: NOT DECIDED</div>'
    '<div style="color:#fde68a;font-size:18px;margin-top:10px;">'
    'V1 shows the gap and example routes. It does not have enough evidence '
    'to choose the best route for each student.</div>'
    '</div>',
    unsafe_allow_html=True,
)

st.markdown("## HOW WILL V2 DECIDE THE BEST ROUTE?")

st.markdown(
    '<div style="width:100%;margin:10px auto 22px;padding:18px 24px;'
    'border-radius:18px;background:#111c35;border:1px solid #38bdf8;'
    'text-align:center;">'
    '<div style="color:white;font-size:23px;font-weight:900;">'
    'V2 WILL USE MARKS AND ANSWER-PAPER DETAILS AND THE ADVICE OF THE CONCERNED '
    'PHYSICS, CHEMISTRY AND MATHS TEACHERS.</div>'
    '</div>',
    unsafe_allow_html=True,
)

v2_factor_columns = st.columns(3)

with v2_factor_columns[0]:
    st.markdown(
        '<div style="min-height:330px;padding:26px;border-radius:22px;'
        'background:#111c35;border:1px solid #38bdf8;">'
        '<div style="color:#38bdf8;font-size:23px;font-weight:950;'
        'text-align:center;">STUDENT MARKS</div>'
        '<div style="color:#e2e8f0;font-size:18px;line-height:2;margin-top:18px;">'
        '• Present subject marks<br>'
        '• Subject changes from one test to the next<br>'
        '• Scores from earlier tests<br>'
        '• How regularly the student performs<br>'
        '• Highest marks scored earlier'
        '</div></div>',
        unsafe_allow_html=True,
    )

with v2_factor_columns[1]:
    st.markdown(
        '<div style="min-height:330px;padding:26px;border-radius:22px;'
        'background:#111c35;border:1px solid #a78bfa;">'
        '<div style="color:#c4b5fd;font-size:23px;font-weight:950;'
        'text-align:center;">ANSWER-PAPER DETAILS</div>'
        '<div style="color:#e2e8f0;font-size:18px;line-height:2;margin-top:18px;">'
        '• Questions attempted<br>'
        '• Correct and incorrect answers<br>'
        '• Percentage of correct answers<br>'
        '• Marks lost for wrong answers<br>'
        '• Time used for each subject'
        '</div></div>',
        unsafe_allow_html=True,
    )

with v2_factor_columns[2]:
    st.markdown(
        '<div style="min-height:330px;padding:26px;border-radius:22px;'
        'background:#111c35;border:1px solid #f59e0b;">'
        '<div style="color:#fbbf24;font-size:23px;font-weight:950;'
        'text-align:center;">TEACHER AND STUDENT INPUT</div>'
        '<div style="color:#e2e8f0;font-size:18px;line-height:2;margin-top:18px;">'
        '• Topics the student finds difficult<br>'
        '• Marks teachers believe the student can gain<br>'
        '• Time available for study<br>'
        '• Student confidence in each subject<br>'
        '• Advice from the subject teachers'
        '</div></div>',
        unsafe_allow_html=True,
    )

st.markdown(
    '<div style="width:100%;margin:44px auto 20px;padding:48px 30px;'
    'border-radius:24px;background:#03050a;border:2px solid #fbbf24;'
    'box-shadow:0 0 42px rgba(251,191,36,0.32);text-align:center;">'
    '<div style="color:#fde68a;font-size:36px;font-weight:950;'
    'text-shadow:0 0 20px rgba(251,191,36,0.85);">'
    'THE ANSWER IS NOT IN THE GAP.</div>'
    '<div style="color:white;font-size:38px;font-weight:950;margin-top:14px;'
    'text-shadow:0 0 18px rgba(255,255,255,0.45);">'
    'THE ANSWER IS IN THE STUDENT.</div>'
    '</div>',
    unsafe_allow_html=True,
)

    