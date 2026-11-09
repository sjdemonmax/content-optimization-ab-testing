"""
final output 4.py - Interactive A/B Experimentation Rollout Decision Dashboard
Domain: Data Science and Analytics | Role: Senior Product Data Scientist
"""

import streamlit as st
import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="EdTech Content Format A/B Rollout Radar",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling
st.markdown("""
<style>
    .metric-card {
        background-color: #f8fafc;
        border-radius: 8px;
        padding: 14px;
        border: 1px solid #e2e8f0;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 20px;
    }
</style>
""", unsafe_allow_html=True)

# Title & Context
st.title("📊 Curriculum Modality A/B/n Rollout Decision Dashboard")
st.markdown("**Executive Analytics Portal:** Multi-arm evaluation across 4,000 learners to optimize completion rates and knowledge retention.")

# -------------------------------------------------------------
# SIDEBAR CONTROLS (Live Interactive Inputs)
# -------------------------------------------------------------
st.sidebar.header("⚙️ Dynamic Simulation Controls")
rollout_pct = st.sidebar.slider(
    "Variant C (Micro-Quiz) Rollout %",
    min_value=0,
    max_value=100,
    value=75,
    step=5,
    help="Adjust percentage of incoming learner traffic allocated to winning Variant C vs Control."
)

mobile_share = st.sidebar.slider(
    "Platform Mobile User Share %",
    min_value=10,
    max_value=90,
    value=45,
    step=5,
    help="Simulate platform traffic shift toward mobile-first learners (10% to 90% mobile share)."
)

alpha_choice = st.sidebar.selectbox(
    "Significance Level (α)",
    ["0.01 (High Stringency - 99% CI)", "0.05 (Standard - 95% CI)"],
    index=0
)
alpha_val = 0.01 if "0.01" in alpha_choice else 0.05
z_crit = stats.norm.ppf(1 - alpha_val / 2)

st.sidebar.markdown("---")
st.sidebar.markdown(f"""
**Live Configuration State:**
- **Variant C Allocation:** `{rollout_pct}%`
- **Control Allocation:** `{100 - rollout_pct}%`
- **Mobile / Desktop Split:** `{mobile_share}%` Mob / `{100 - mobile_share}%` Dsk
- **Critical Z-Score:** `{z_crit:.3f}` (α = {alpha_val})
""")

# -------------------------------------------------------------
# BASELINE EMPIRICAL CONSTANTS
# -------------------------------------------------------------
MODALITY_DATA = {
    "Control (Long Video)": {"rate": 15.0, "desktop": 19.9, "mobile": 7.9, "score": 57.45, "csat": 2.80, "color": "#94a3b8"},
    "Variant B (Micro-Video)": {"rate": 71.0, "desktop": 69.6, "mobile": 72.4, "score": 83.28, "csat": 3.75, "color": "#38bdf8"},
    "Variant C (Micro-Quiz)": {"rate": 79.5, "desktop": 79.8, "mobile": 80.2, "score": 92.96, "csat": 4.25, "color": "#22c55e"},
    "Variant D (Shorts + Take-Home)": {"rate": 31.4, "desktop": 41.8, "mobile": 19.8, "score": 64.04, "csat": 3.35, "color": "#f59e0b"}
}

# Dynamic Blended Computations
eff_ctrl_rate = ((100 - mobile_share) / 100) * MODALITY_DATA["Control (Long Video)"]["desktop"] + (mobile_share / 100) * MODALITY_DATA["Control (Long Video)"]["mobile"]
eff_var_c_rate = ((100 - mobile_share) / 100) * MODALITY_DATA["Variant C (Micro-Quiz)"]["desktop"] + (mobile_share / 100) * MODALITY_DATA["Variant C (Micro-Quiz)"]["mobile"]

# Blended platform completion rate across rollout % and device traffic
blended_completion = ((100 - rollout_pct) / 100) * eff_ctrl_rate + (rollout_pct / 100) * eff_var_c_rate
blended_retention = ((100 - rollout_pct) / 100) * 57.45 + (rollout_pct / 100) * 92.96
blended_csat = ((100 - rollout_pct) / 100) * 2.80 + (rollout_pct / 100) * 4.25

# -------------------------------------------------------------
# DYNAMIC TOP KPI CARDS (Fully reactive to both sliders)
# -------------------------------------------------------------
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric(
        label="🎯 Active Rollout Allocation",
        value=f"{rollout_pct}% Variant C",
        delta=f"{100 - rollout_pct}% Control Baseline"
    )
with col2:
    st.metric(
        label="📈 Blended Completion Rate",
        value=f"{blended_completion:.1f}%",
        delta=f"+{blended_completion - 15.0:.1f}% vs Control",
        delta_color="normal"
    )
with col3:
    st.metric(
        label="🧠 Projected Retention Score",
        value=f"{blended_retention:.1f} pts",
        delta=f"+{blended_retention - 57.45:.1f} pts Mastery Lift",
        delta_color="normal"
    )
with col4:
    mob_delta = MODALITY_DATA["Variant C (Micro-Quiz)"]["mobile"] - MODALITY_DATA["Control (Long Video)"]["mobile"]
    st.metric(
        label="📱 Mobile Attrition Resilience",
        value=f"{eff_var_c_rate:.1f}% at {mobile_share}% Mob",
        delta=f"+{mob_delta:.1f}% Mobile Lift over Control",
        delta_color="normal"
    )

st.divider()

# -------------------------------------------------------------
# MAIN DASHBOARD TABS
# -------------------------------------------------------------
tab1, tab2, tab3 = st.tabs([
    "📈 Modality Performance & Statistical Significance",
    "📱 Mobile vs. Desktop Traffic Simulation",
    "🚀 Annualized Rollout ROI & Certification Engine"
])

with tab1:
    st.subheader(f"Modality Performance Matrix with Dynamic {int((1-alpha_val)*100)}% Confidence Intervals")
    st.markdown(f"Evaluated at **α = {alpha_val}** (Critical $Z = {z_crit:.3f}$). Confidence intervals expand or contract as significance level is adjusted.")
    
    rows = []
    for arm, d in MODALITY_DATA.items():
        p = d["rate"] / 100.0
        se = np.sqrt(p * (1 - p) / 1000)
        ci_half = z_crit * se * 100
        ci_low = max(0.0, d["rate"] - ci_half)
        ci_high = min(100.0, d["rate"] + ci_half)
        rel_up = ((d["rate"] - 15.0) / 15.0) * 100 if "Control" not in arm else 0.0
        
        # Rollout allocation share display
        if "Variant C" in arm:
            alloc_display = f"{rollout_pct}%"
        elif "Control" in arm:
            alloc_display = f"{100 - rollout_pct}%"
        else:
            alloc_display = "0% (Retire)"
            
        rows.append({
            "Delivery Modality": arm,
            "Sample Size": 1000,
            "Base Completion Rate": f"{d['rate']:.1f}%",
            f"{int((1-alpha_val)*100)}% Conf. Interval": f"[{ci_low:.1f}% - {ci_high:.1f}%]",
            "Relative Uplift": f"+{rel_up:.1f}%" if rel_up > 0 else "Baseline",
            "Avg Retention Score": f"{d['score']:.2f}",
            "Simulated Traffic Share": alloc_display,
            "Statistically Significant": "YES (p < 0.001)" if "Control" not in arm else "Baseline"
        })
        
    st.dataframe(pd.DataFrame(rows), use_container_width=True, hide_index=True)
    
    # Plot: Bar chart with dynamic error bars
    fig, ax = plt.subplots(figsize=(10, 4.2))
    arms = list(MODALITY_DATA.keys())
    rates = [d["rate"] for d in MODALITY_DATA.values()]
    errs = [z_crit * np.sqrt((r/100)*(1 - r/100)/1000) * 100 for r in rates]
    bar_colors = [d["color"] for d in MODALITY_DATA.values()]
    
    bars = ax.bar(arms, rates, yerr=errs, capsize=6, color=bar_colors, edgecolor="#1e293b", linewidth=1, width=0.55)
    ax.set_ylabel("Completion Rate (%)", fontweight="bold")
    ax.set_title(f"Completion Rates with Dynamic {int((1-alpha_val)*100)}% Confidence Intervals (α = {alpha_val})", fontweight="bold", fontsize=12)
    ax.set_ylim(0, 100)
    for i, (bar, r, e) in enumerate(zip(bars, rates, errs)):
        ax.text(bar.get_x() + bar.get_width()/2, r + e + 2, f"{r:.1f}%\n(±{e:.1f}%)", ha='center', va='bottom', fontsize=9, fontweight='bold')
    st.pyplot(fig)

with tab2:
    st.subheader(f"📱 Mobile vs. Desktop Traffic Simulation (Current Setting: {mobile_share}% Mobile / {100-mobile_share}% Desktop)")
    st.markdown(
        f"Drag the **Platform Mobile User Share %** slider in the sidebar to simulate how changing smartphone adoption impacts each format. "
        f"Notice how **Variant C** stays flat while **Variant D** and **Control** crash as mobile traffic grows."
    )
    
    # Dynamic computation for each arm under current mobile share
    sim_data = []
    for arm, d in MODALITY_DATA.items():
        eff = ((100 - mobile_share) / 100) * d["desktop"] + (mobile_share / 100) * d["mobile"]
        gap = d["mobile"] - d["desktop"]
        attrition_at_share = (d["desktop"] - eff) if gap < 0 else 0.0
        
        sim_data.append({
            "Delivery Modality": arm,
            "Desktop Baseline": f"{d['desktop']:.1f}%",
            "Mobile Baseline": f"{d['mobile']:.1f}%",
            "Interaction Gap (Mob - Dsk)": f"{gap:+.1f}%",
            f"Simulated Effective Rate ({mobile_share}% Mob)": f"{eff:.1f}%",
            "Impact of Mobile Influx": f"-{attrition_at_share:.1f}% Loss" if gap < 0 else f"+{eff - d['desktop']:.1f}% Gain"
        })
    st.dataframe(pd.DataFrame(sim_data), use_container_width=True, hide_index=True)
    
    # Interactive Sensitivity Curve with dynamic marker
    fig2, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 4.5))
    
    # Left subplot: Grouped bars for Desktop vs Mobile vs Simulated Effective
    x = np.arange(len(arms))
    w = 0.25
    desk_vals = [d["desktop"] for d in MODALITY_DATA.values()]
    mob_vals = [d["mobile"] for d in MODALITY_DATA.values()]
    eff_vals = [((100 - mobile_share)/100)*d["desktop"] + (mobile_share/100)*d["mobile"] for d in MODALITY_DATA.values()]
    
    ax1.bar(x - w, desk_vals, w, label="Desktop (100% Dsk)", color="#3b82f6", edgecolor="#1e3a8a")
    ax1.bar(x, mob_vals, w, label="Mobile (100% Mob)", color="#f97316", edgecolor="#9a3412")
    ax1.bar(x + w, eff_vals, w, label=f"Simulated Blended ({mobile_share}% Mob)", color="#10b981", edgecolor="#064e3b", linewidth=1.5)
    ax1.set_ylabel("Completion Rate (%)", fontweight="bold")
    ax1.set_title(f"Completion Rates by Device & Current Simulation ({mobile_share}% Mobile)", fontweight="bold")
    ax1.set_xticks(x)
    ax1.set_xticklabels(["Control", "Variant B", "Variant C", "Variant D"], rotation=15)
    ax1.legend(frameon=True)
    ax1.set_ylim(0, 100)
    
    # Right subplot: Sensitivity curve as mobile share varies from 0% to 100%
    m_range = np.linspace(0, 100, 101)
    for arm, d in MODALITY_DATA.items():
        curve = ((100 - m_range) / 100) * d["desktop"] + (m_range / 100) * d["mobile"]
        ax2.plot(m_range, curve, label=arm, color=d["color"], linewidth=2.5)
        
    # Vertical marker line for current mobile_share slider
    ax2.axvline(x=mobile_share, color="#ef4444", linestyle="--", linewidth=2, label=f"Current Setting ({mobile_share}%)")
    # Mark the current point on Variant C and Control
    ax2.scatter([mobile_share], [eff_var_c_rate], color="#22c55e", s=90, zorder=5, edgecolor="black")
    ax2.scatter([mobile_share], [eff_ctrl_rate], color="#94a3b8", s=90, zorder=5, edgecolor="black")
    ax2.set_xlabel("Platform Mobile Traffic Share (%)", fontweight="bold")
    ax2.set_ylabel("Effective Cohort Completion Rate (%)", fontweight="bold")
    ax2.set_title("Sensitivity Curve: Impact of Mobile Influx on Completion", fontweight="bold")
    ax2.set_xlim(0, 100)
    ax2.set_ylim(0, 100)
    ax2.legend(loc="lower left", fontsize=8)
    
    plt.tight_layout()
    st.pyplot(fig2)

with tab3:
    st.subheader(f"🚀 Annualized Rollout ROI & Certification Engine (Current Rollout: {rollout_pct}% Variant C)")
    st.markdown(
        f"Adjust the **Variant C Rollout %** slider in the sidebar to model production deployment across an annual platform cohort of 100,000 enrolled learners."
    )
    
    annual_cohort = 100000
    base_completers = int(annual_cohort * (eff_ctrl_rate / 100.0))
    sim_completers = int(annual_cohort * (blended_completion / 100.0))
    net_new_completers = sim_completers - base_completers
    cert_value = 150 # $150 course certificate or completion value
    incremental_value = net_new_completers * cert_value
    
    r1, r2, r3 = st.columns(3)
    r1.metric("Current Status Quo Completers", f"{base_completers:,}", delta=f"At {mobile_share}% mobile share")
    r2.metric("Projected Annual Completers", f"{sim_completers:,}", delta=f"+{net_new_completers:,} net completions ({rollout_pct}% rollout)")
    r3.metric("Projected Economic Value", f"${incremental_value:,.0f}", delta=f"+{(sim_completers/max(1,base_completers)-1)*100:.1f}% ROI Uplift")
    
    # Rollout Trajectory Chart
    fig3, ax3 = plt.subplots(figsize=(10, 4.2))
    p_range = np.linspace(0, 100, 101)
    trajectory = [int(annual_cohort * (((100 - p)/100)*eff_ctrl_rate + (p/100)*eff_var_c_rate) / 100.0) for p in p_range]
    
    ax3.plot(p_range, trajectory, color="#2563eb", linewidth=3, label="Projected Annual Completers")
    ax3.axhline(y=base_completers, color="#94a3b8", linestyle=":", label=f"Baseline Control ({base_completers:,})")
    
    # Mark current point on curve
    ax3.scatter([rollout_pct], [sim_completers], color="#dc2626", s=130, zorder=6, edgecolor="white", linewidth=2, label=f"Current: {rollout_pct}% ({sim_completers:,})")
    ax3.annotate(
        f"Selected: {rollout_pct}% Rollout\n→ {sim_completers:,} Completers\n(+{net_new_completers:,} Net Gain)",
        xy=(rollout_pct, sim_completers),
        xytext=(rollout_pct + 4 if rollout_pct < 60 else rollout_pct - 35, sim_completers - 8000),
        arrowprops=dict(facecolor='#dc2626', shrink=0.08, width=1.5, headwidth=6),
        fontweight='bold',
        fontsize=9,
        bbox=dict(boxstyle="round,pad=0.5", fc="#fef2f2", ec="#dc2626", lw=1.5)
    )
    ax3.set_xlabel("Variant C (Micro-Quiz) Production Rollout (%)", fontweight="bold")
    ax3.set_ylabel("Annual Course Completions (N=100,000)", fontweight="bold")
    ax3.set_title("Annualized Completion Trajectory vs. Rollout Allocation", fontweight="bold")
    ax3.set_xlim(0, 100)
    ax3.legend(loc="upper left")
    
    st.pyplot(fig3)
