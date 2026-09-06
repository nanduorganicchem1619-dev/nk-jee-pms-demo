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
    [data-testid="stAppDeployButton"] {
        display: none !important;
    }
       [data-testid="stWidgetLabel"] p {
    color: #e2e8f0 !important;
    font-size: 18px !important;
    font-weight: 800 !important;
}

[data-testid="stRadio"] {
    width: 100% !important;
}

[data-testid="stRadio"] [data-testid="stWidgetLabel"] {
    display: none !important;
}
    display: flex !important;
    justify-content: center !important;
    width: 100% !important;
    text-align: center !important;
    margin-bottom: 24px !important;
}
[data-testid="stRadio"] [data-testid="stWidgetLabel"] p {
    width: 100% !important;
    text-align: center !important;
}
[data-testid="stRadio"] div[role="radiogroup"] {
    display: flex !important;
    justify-content: center !important;
    gap: 48px !important;
    width: 100% !important;
    margin-top: 0 !important;
}

        div[role="radiogroup"] label {
        min-width: 260px;
        padding: 16px 24px;
        border: 2px solid #64748b;
        border-radius: 16px;
        background: #111c35;
        justify-content: center;
        cursor: pointer;
        transition: all 0.25s ease;
    }

    div[role="radiogroup"] label:hover {
        border-color: #38bdf8;
        box-shadow: 0 0 24px rgba(56, 189, 248, 0.35);
        transform: translateY(-3px);
    }

    div[role="radiogroup"] label p {
        color: #ffffff !important;
        font-size: 21px !important;
        font-weight: 900 !important;
    }

    div[role="radiogroup"] label:has(input:checked) {
        border-color: #fbbf24;
        background: linear-gradient(135deg, #17345f, #312e81);
        box-shadow: 0 0 24px rgba(251, 191, 36, 0.35);
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
# College GT Percentile and batch rank calculations.
# All 10 dummy students appeared in both tests.
for test_name in ["GT1", "GT2"]:
    total_column = f"{test_name} Total"
    percentile_column = f"{test_name} College GT Percentile"
    rank_column = f"{test_name} Batch Rank"

    students[percentile_column] = (
        students[total_column].rank(method="max", pct=True) * 100
    ).round(1)

    students[rank_column] = (
        students[total_column].rank(method="min", ascending=False).astype(int)
    )

students["Percentile Change"] = (
    students["GT2 College GT Percentile"]
    - students["GT1 College GT Percentile"]
).round(1)

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
"""<style>
@keyframes collegeFade {
0% {
    opacity: 0;
    transform: translateY(-12px);
}
100% {
    opacity: 1;
    transform: translateY(0);
}
}

.nk-college {
    animation: collegeFade 1.2s ease-out both;
}
</style>

<div style="width:100%;margin:0 auto 26px;text-align:center;">
<div class="nk-college" style="color:#7dd3fc;font-size:52px;font-weight:950;letter-spacing:0.04em;text-shadow:0 0 20px rgba(56,189,248,0.55);">VISHRA JUNIOR COLLEGE</div>
<div style="color:white;font-size:25px;font-weight:850;margin-top:7px;">BALAPUR, HYDERABAD</div>
<div style="display:inline-block;margin-top:17px;padding:10px 24px;border-radius:14px;background:#111c35;border:1px solid #a78bfa;color:#c4b5fd;font-size:23px;font-weight:900;">NK JEE - PERFORMANCE MONITORING SYSTEM<br></div>
</div>""",
    unsafe_allow_html=True,
)
st.markdown(
"""<style>
@keyframes purposeFade {
0% {
    opacity: 0;
transform: translateY(6px);}
100% {
    opacity: 1;
    transform: translateY(0);
}
}

.purpose-animate {
animation: purposeFade 0.8s ease-out 0.2s both;}
</style>""",
    unsafe_allow_html=True,
)


st.markdown(
    """
    <style>
    @keyframes targetFade {
        0% {
            opacity: 0;
            transform: scale(0.96);
        }
        100% {
            opacity: 1;
            transform: scale(1);
        }
    }

    .target-animate {
        animation: targetFade 0.8s ease-out 0.3s both;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


st.markdown(
    """
    <div style="
        margin:18px auto 26px;
        padding:20px 28px;
        max-width:900px;
        text-align:center;
        background:linear-gradient(135deg,#111c35,#25205a);
       border:2px solid #fbbf24;
        border-radius:22px;
       box-shadow:0 0 32px rgba(251,191,36,0.38);
    ">
        <div style="
           color:#fde68a;
            font-size:42px;
            font-weight:950;
            letter-spacing:1px;
            text-shadow:0 0 18px rgba(251,191,36,0.75);
        ">
            ✨ SELECT DASHBOARD VIEW ✨
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

selector_left, selector_middle, selector_right = st.columns([1.2, 3, 0.8])
with selector_middle:
    st.markdown(
        '<div style="width:100%;text-align:center;color:#e2e8f0;'
        'font-size:18px;font-weight:800;margin-bottom:24px;">'
        'CHOOSE HOW YOU WANT TO VIEW STUDENT PERFORMANCE'
        '</div>',
        unsafe_allow_html=True,
    )

    dashboard_view = st.radio(
        "Dashboard view",
        ["MARKS VIEW", "PERCENTILE VIEW"],
        format_func=lambda view: {
            "MARKS VIEW": "📊 MARKS VIEW",
            "PERCENTILE VIEW": "📈 PERCENTILE VIEW",
        }[view],
        horizontal=True,
        key="dashboard_view",
        label_visibility="collapsed",
    )
st.markdown(
    '<div style="margin:10px 0 26px;padding:15px 22px;border-radius:16px;'
    'background:#111c35;border:1px solid #818cf8;text-align:center;'
    'color:#e2e8f0;font-size:18px;font-weight:800;">'
    '<b style="color:#38bdf8;">MARKS VIEW</b> shows the student’s score. '
    '<b style="color:#c4b5fd;">PERCENTILE VIEW</b> shows the student’s '
    'position within the college batch.'
    '</div>',
    unsafe_allow_html=True,
)
if dashboard_view == "PERCENTILE VIEW":
    percentile_improved = int((students["Percentile Change"] > 0).sum())
    percentile_declined = int((students["Percentile Change"] < 0).sum())
    percentile_stable = int((students["Percentile Change"] == 0).sum())

    st.markdown("## COLLEGE GT PERCENTILE")

    st.markdown(
        '<div style="margin:14px 0 24px;padding:22px 26px;border-radius:20px;'
        'background:#111c35;border:2px solid #a78bfa;text-align:center;">'
        '<div style="color:#c4b5fd;font-size:23px;font-weight:950;">'
        'COLLEGE GT PERCENTILE FORMULA</div>'
        '<div style="color:white;font-size:22px;font-weight:850;'
        'line-height:1.7;margin-top:12px;">'
        '100 × (Number of appeared students scoring equal to or below '
        'the student) ÷ Total number of students who appeared'
        '</div></div>',
        unsafe_allow_html=True,
    )

    percentile_columns = st.columns(4)

    with percentile_columns[0]:
        show_card(
            "STUDENTS APPEARED",
            total_students,
            "#38bdf8",
            "included in percentile calculation",
        )

    with percentile_columns[1]:
        show_card(
            "PERCENTILE IMPROVED",
            percentile_improved,
            "#22c55e",
            "GT1 to GT2",
        )

    with percentile_columns[2]:
        show_card(
            "PERCENTILE STABLE",
            percentile_stable,
            "#fbbf24",
            "GT1 to GT2",
        )

    with percentile_columns[3]:
        show_card(
            "PERCENTILE DECLINED",
            percentile_declined,
            "#ef4444",
            "GT1 to GT2",
        )

    st.markdown(
        '<div style="margin:24px 0;padding:18px 24px;border-radius:18px;'
        'background:#2b2108;border:1px solid #fbbf24;text-align:center;">'
        '<div style="color:#fde68a;font-size:18px;font-weight:850;">'
        'College GT Percentile is based on the students who appeared '
        'in this test. It is not the official NTA percentile.'
        '</div></div>',
        unsafe_allow_html=True,
    )
    st.markdown("### 📈 GT1 TO GT2 — COLLEGE GT PERCENTILE MOVEMENT")

    gt2_bar_colors = [
        "#22c55e" if change > 0
        else "#ef4444" if change < 0
        else "#fbbf24"
        for change in students["Percentile Change"]
    ]

    percentile_fig = go.Figure()

    percentile_fig.add_trace(
        go.Bar(
            name="GT1 Percentile",
            x=students["Student"],
            y=students["GT1 College GT Percentile"],
            marker_color="#64748b",
            text=students["GT1 College GT Percentile"],
            textposition="outside",
        )
    )

    percentile_fig.add_trace(
        go.Bar(
            name="GT2 Percentile",
                        showlegend=False,
            x=students["Student"],
            y=students["GT2 College GT Percentile"],
            marker_color=gt2_bar_colors,
            text=students["GT2 College GT Percentile"],
            textposition="outside",
        )
    )
    for legend_name, legend_color in [
        ("GT2 Improved", "#22c55e"),
        ("GT2 Stable", "#fbbf24"),
        ("GT2 Declined", "#ef4444"),
    ]:
        percentile_fig.add_trace(
            go.Scatter(
                x=[None],
                y=[None],
                mode="markers",
                marker=dict(
                    symbol="square",
                    size=14,
                    color=legend_color,
                ),
                name=legend_name,
            )
        )
    percentile_fig.add_hline(
        y=90,
        line_color="#38bdf8",
        line_dash="dash",
        annotation_text="90+ PERCENTILE",
        annotation_font_color="#38bdf8",
    )

    percentile_fig.update_layout(
        barmode="group",
        height=520,
                xaxis=dict(
            title=dict(
                text="STUDENTS",
                font=dict(color="#38bdf8", size=18),
            ),
            tickfont=dict(color="#e2e8f0", size=14),
        ),
        yaxis=dict(
            title=dict(
                text="COLLEGE GT PERCENTILE",
                font=dict(color="#38bdf8", size=18),
            ),
            tickfont=dict(color="#e2e8f0", size=14),
            range=[0, 110],
        ),
        paper_bgcolor="#080b12",
        plot_bgcolor="#111c35",
        font_color="#ffffff",
        legend_title_text="",
                legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.10,
            xanchor="center",
            x=0.5,
            font=dict(color="#ffffff", size=16),
            bgcolor="rgba(0,0,0,0)",
        ),
        margin=dict(t=90, b=40, l=40, r=40),
    )

    st.plotly_chart(
        percentile_fig,
        use_container_width=True,
        config={
            "displayModeBar": False,
            "displaylogo": False,
        },
    )
    achievers_90 = students.loc[
        students["GT2 College GT Percentile"] >= 90,
        [
            "Student",
            "GT1 College GT Percentile",
            "GT2 College GT Percentile",
        ],
    ].copy()

    achievers_90 = achievers_90.sort_values(
        "GT2 College GT Percentile",
        ascending=False,
    )

    st.markdown("### 🏆 90+ COLLEGE GT PERCENTILE ACHIEVERS")

    if achievers_90.empty:
        st.info("No student achieved 90+ College GT Percentile in GT2.")
    else:
                achievers_table_html = """
        <style>
        .achievers-table {
            margin-top: 18px;
            margin-bottom: 28px;
        }
        .achievers-table table {
            width: 100%;
            border-collapse: separate;
            border-spacing: 0;
            border: 2px solid #fbbf24;
            border-radius: 12px;
            overflow: hidden;
        }
        .achievers-table th {
            background-color: #fbbf24;
            color: #081426;
            font-size: 18px;
            font-weight: 800;
            padding: 14px;
            text-align: center;
        }
        .achievers-table td {
            background-color: #111c38;
            color: #ffffff;
            font-size: 17px;
            font-weight: 600;
            padding: 14px;
            text-align: center;
            border-top: 1px solid #465a7a;
        }
        .achievers-table tbody tr:nth-child(even) td {
            background-color: #18264a;
        }
        </style>
        <div class="achievers-table">
        """ + achievers_90.to_html(index=False, border=0) + """
        </div>
        """

                st.html(achievers_table_html)
    st.markdown("## 👤 INDIVIDUAL STUDENT PERCENTILE ANALYSIS")

    selector_left, selector_center, selector_right = st.columns([3, 2, 3])

    with selector_center:
        st.markdown(
            "<div style='text-align:center; font-size:26px; "
            "font-weight:800; color:#ffffff; margin-bottom:8px;'>"
            "SELECT A STUDENT</div>",
            unsafe_allow_html=True,
        )

        selected_percentile_student = st.selectbox(
            "SELECT A STUDENT",
            students["Student"].tolist(),
            key="percentile_student_selector",
            label_visibility="collapsed",
        )

    selected_percentile_data = students.loc[
        students["Student"] == selected_percentile_student
    ].iloc[0]

    gt1_percentile = int(selected_percentile_data["GT1 College GT Percentile"])
    gt2_percentile = int(selected_percentile_data["GT2 College GT Percentile"])
    percentile_change = int(selected_percentile_data["Percentile Change"])
    gt1_rank = int(selected_percentile_data["GT1 Batch Rank"])
    gt2_rank = int(selected_percentile_data["GT2 Batch Rank"])
    gt1_marks = int(selected_percentile_data["GT1 Total"])
    gt2_marks = int(selected_percentile_data["GT2 Total"])
    marks_change = gt2_marks - gt1_marks
    gt1_distance_from_target = 180 - gt1_marks
    gt2_distance_from_target = 180 - gt2_marks
    if marks_change > 0:
        marks_movement_color = "#22c55e"
        marks_movement_status = "INCREASED"
    elif marks_change < 0:
        marks_movement_color = "#ef4444"
        marks_movement_status = "DECREASED"
    else:
        marks_movement_color = "#fbbf24"
        marks_movement_status = "UNCHANGED"
    if marks_change > 0:
        marks_change_message = f"Marks increased by {marks_change}."
    elif marks_change < 0:
        marks_change_message = f"Marks decreased by {abs(marks_change)}."
    else:
        marks_change_message = "Marks remained unchanged."

    if gt2_distance_from_target > 0:
            target_distance_message = (
                f"{selected_percentile_student} is currently "
                f"{gt2_distance_from_target} marks short of the 180 target."
            )
    elif gt2_distance_from_target < 0:
        target_distance_message = (
                f"{selected_percentile_student} is currently "
                f"{abs(gt2_distance_from_target)} marks above the 180 target."
            )
    else:
        target_distance_message = (
                f"{selected_percentile_student} has exactly reached "
                "the 180 target."
            )

    marks_target_summary = (
        f"{marks_change_message} {target_distance_message}"
    )
    if percentile_change > 0:
            percentile_status = "IMPROVED"
            status_color = "#22c55e"
            status_icon = "📈"
    elif percentile_change < 0:
            percentile_status = "DECLINED"
            status_color = "#ef4444"
            status_icon = "📉"
    else:
            percentile_status = "STABLE"
            status_color = "#fbbf24"
            status_icon = "➡️"

    if percentile_change > 0:
        percentile_reason = (
            f"{selected_percentile_student}'s "
            f"{marks_change_message.lower()} "
            f"The College GT Percentile increased from {gt1_percentile} "
            f"to {gt2_percentile}. "
            f"{selected_percentile_student}'s position in the batch improved from rank {gt1_rank} "
            f"to rank {gt2_rank}."
        )
    elif percentile_change < 0:
        percentile_reason = (
            f"{selected_percentile_student}'s "
            f"{marks_change_message.lower()} "
            f"The College GT Percentile decreased from {gt1_percentile} "
            f"to {gt2_percentile} because other students improved more. "
            f"{selected_percentile_student}'s position in the batch moved down from rank {gt1_rank} "
            f"to rank {gt2_rank}."
        )
    else:
        percentile_reason = (
            f"{selected_percentile_student}'s "
            f"{marks_change_message.lower()} "
            f"The College GT Percentile remained stable at {gt2_percentile}. "
            f"{selected_percentile_student}'s rank in the batch was {gt1_rank} in GT1 "
            f"and {gt2_rank} in GT2."
        )
    st.markdown(
        """
        <style>
        [data-testid="stMetric"] {
            background: #111c35;
            border: 1px solid #64748b;
            border-radius: 16px;
            padding: 20px;
                        text-align: center;
        }

        [data-testid="stMetricLabel"] p {
        color: #38bdf8 !important;
        font-size: 22px !important;
            font-weight: 850 !important;
        }

        [data-testid="stMetricValue"] {
        color: #fbbf24 !important;
        font-size: 52px !important;
        font-weight: 900 !important;
        }

        [data-testid="stMetricDelta"] {
            color: #cbd5e1 !important;
        }
                [data-testid="stMetricLabel"],
        [data-testid="stMetricDelta"] {
            justify-content: center !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    analysis_col1, analysis_col2, analysis_col3 = st.columns(3)

    with analysis_col1:
        st.metric(
            "GT1 PERCENTILE",
            gt1_percentile,
            f"Batch Rank: {gt1_rank}",
            delta_color="off",
        )

    with analysis_col2:
        st.metric(
            "GT2 PERCENTILE",
            gt2_percentile,
            f"Batch Rank: {gt2_rank}",
            delta_color="off",
        )

    with analysis_col3:
        st.metric(
            f"{status_icon} PERCENTILE STATUS",
            percentile_status,
            f"{percentile_change:+d} percentile",
            delta_color="off",
        )
    st.markdown(
        f"""
        <div style="
            margin: 24px 0 10px;
            padding: 20px 24px;
            background: #111c35;
            border: 1px solid {status_color};
            border-left: 7px solid {status_color};
            border-radius: 16px;
            box-shadow: 0 0 20px {status_color}33;
        ">
            <div style="
                color: {status_color};
                font-size: 21px;
                font-weight: 900;
                margin-bottom: 10px;
            ">
                🔍 PERCENTILE EXPLANATION
            </div>
            <div style="
                color: #ffffff;
                font-size: 19px;
                font-weight: 650;
                line-height: 1.6;
            ">
                {percentile_reason}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        f"## 📊 {selected_percentile_student.upper()} — COLLEGE PERCENTILE MOVEMENT"
    )

    individual_percentile_fig = go.Figure()

    individual_percentile_fig.add_trace(
        go.Scatter(
            x=["GT1", "GT2"],
            y=[gt1_percentile, gt2_percentile],
            mode="lines+markers+text",
            line=dict(color=status_color, width=5),
            marker=dict(
                color=[ "#64748b", status_color ],
                size=18,
                line=dict(color="#ffffff", width=2),
            ),
            text=[gt1_percentile, gt2_percentile],
            textposition="top center",
            textfont=dict(color="#ffffff", size=20),
            hovertemplate="<b>%{x}</b><br>College Percentile: %{y}<extra></extra>",
            showlegend=False,
        )
    )
    individual_percentile_fig.update_layout(
        height=400,
        paper_bgcolor="#080b12",
        plot_bgcolor="#111c35",
        margin=dict(l=60, r=40, t=45, b=55),
        xaxis=dict(
            title="TEST",
            tickfont=dict(color="#ffffff", size=17),
            title_font=dict(color="#38bdf8", size=18),
        ),
        yaxis=dict(
            title="COLLEGE GT PERCENTILE",
            range=[0, 105],
            tickfont=dict(color="#e2e8f0", size=14),
            title_font=dict(color="#38bdf8", size=18),
            gridcolor="#64748b",
        ),
        font=dict(color="#ffffff"),
    )

    st.plotly_chart(
        individual_percentile_fig,
        use_container_width=True,
        config={
            "displayModeBar": False,
            "displaylogo": False,
        },
    )
    st.markdown(
        f"## 🎯 {selected_percentile_student.upper()} — MARKS PROGRESS TOWARDS 180"
    )
    individual_marks_fig = go.Figure()

    individual_marks_fig.add_trace(
        go.Bar(
            x=["GT1", "GT2"],
            y=[gt1_marks, gt2_marks],
            marker_color=["#64748b", marks_movement_color],
            text=[gt1_marks, gt2_marks],
            textposition="outside",
            textfont=dict(color="#ffffff", size=20),
            width=[0.42, 0.42],
            hovertemplate="<b>%{x}</b><br>Total Marks: %{y}<extra></extra>",
            showlegend=False,
        )
    )
    individual_marks_fig.add_hline(
        y=180,
        line_color="#fbbf24",
        line_width=3,
        line_dash="dash",
        annotation_text="180 MARKS TARGET",
        annotation_position="top right",
        annotation_font_color="#fbbf24",
        annotation_font_size=16,
    )

    individual_marks_fig.update_layout(
        height=460,
        paper_bgcolor="#080b12",
        plot_bgcolor="#111c35",
        margin=dict(l=60, r=40, t=45, b=55),
        xaxis=dict(
            title="TEST",
            tickfont=dict(color="#ffffff", size=17),
            title_font=dict(color="#38bdf8", size=18),
        ),
        yaxis=dict(
            title="TOTAL MARKS OUT OF 300",
            range=[0, 210],
            tickfont=dict(color="#e2e8f0", size=14),
            title_font=dict(color="#38bdf8", size=18),
            gridcolor="#64748b",
        ),
        font=dict(color="#ffffff"),
    )

    st.plotly_chart(
        individual_marks_fig,
        use_container_width=True,
        config={
            "displayModeBar": False,
            "displaylogo": False,
        },
    )

    st.markdown(
        f"""
        <div style="
            margin: 14px 0 10px;
            padding: 18px 24px;
            background: #111c35;
            border: 1px solid {marks_movement_color};
            border-left: 7px solid {marks_movement_color};
            border-radius: 15px;
            color: #ffffff;
            font-size: 20px;
            font-weight: 750;
            line-height: 1.5;
            text-align: center;
        ">
            🎯 {marks_target_summary}
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.stop()
if dashboard_view == "MARKS VIEW":
    st.markdown(
        '<div style="margin:18px 0 32px;padding:24px 28px;border-radius:22px;'
        'background:#080b12;border:2px solid #fbbf24;'
        'box-shadow:0 0 30px rgba(251,191,36,0.30);text-align:center;">'
        '<div style="color:#fde68a;font-size:23px;font-weight:900;">'
        'COLLEGE WORKING MARKS TARGET</div>'
        '<div class="target-animate" style="color:#fbbf24;font-size:56px;'
        'font-weight:950;text-shadow:0 0 16px #f59e0b;">180 / 300</div>'
        '<div style="color:#cbd5e1;font-size:16px;margin-top:6px;">'
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
"GT1 — FIRST-TEST<br>AVERAGE",
        f"{gt1_average:.1f}",
        "#94a3b8",
        "Average total of all 10 students",
    )

with comparison_columns[1]:
    show_card(
       "GT2 — LATEST-TEST<br>AVERAGE",
        f"{gt2_average:.1f}",
        "#38bdf8",
        "Average total of all 10 students",
    )

with comparison_columns[2]:
    show_card(
       "BATCH IMPROVED<br>BY",
        f"+{batch_improvement:.1f}",
        "#22c55e",
        "marks from GT1 to GT2",
    )

with comparison_columns[3]:
    show_card(
        "STUDENTS REACHING<br>180",
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
'All 10 students are divided into the three groups shown below.'    '</div>',
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

marks_selector_left, marks_selector_center, marks_selector_right = st.columns([3, 2, 3])

with marks_selector_center:
    st.markdown(
        "<div style='text-align:center; font-size:30px; "
        "font-weight:800; color:#ffffff; margin-bottom:8px;'>"
        "SELECT A STUDENT</div>",
        unsafe_allow_html=True,
    )

    selected_student_name = st.selectbox(
        "SELECT A STUDENT",
        students["Student"].tolist(),
        key="marks_student_selector",
        label_visibility="collapsed",
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
           helped_text = f"{best_subject}<br>+{best_change}"
else:
    helped_text = "No subject increased"

if lowest_change < 0:
           reduced_text = f"{lowest_subject}<br>{lowest_change}"
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

st.markdown("<div style='height:24px;'></div>", unsafe_allow_html=True)
st.markdown("### SUBJECT-WISE MARKS")
st.markdown("<div style='height:32px;'></div>", unsafe_allow_html=True)

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
            helped_text = f"{helped_text}<br>+{highest_change}"
else:
    helped_text = "No subject increased<br>&nbsp;"

if lowest_change < 0:
    reduced_text = " and ".join(lowest_subjects)
    reduced_text = f"{reduced_text}<br>{lowest_change}"
else:
    reduced_text = "No subject decreased<br>&nbsp;"
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

st.markdown("<div style='height:24px;'></div>", unsafe_allow_html=True)
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
    '<div style="color:white;font-size:30px;font-weight:900;margin-top:20px;">'
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

    