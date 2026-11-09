# Content Delivery Modality Optimisation — A/B/n Experiment

> **Role**: Senior Product Data Scientist · EdTech Learning Platform

## The Problem

Content teams at learning platforms routinely invest in producing new formats — micro-videos, interactive quizzes, short-form reels — without rigorous evidence of which modality actually drives learner outcomes. Decisions are often made on gut instinct, production cost, or anecdote. The result: expensive content investments in formats that may not outperform the status quo, and no principled framework for future rollout decisions.

Worse, aggregate completion rates mask a critical hidden variable: device type. A format that performs brilliantly on desktop may collapse on mobile — and in mobile-first learner demographics, that gap can sink an otherwise promising rollout.

## The Solution

This project executes a **rigorous 4-arm randomised controlled A/B/n experiment** across 4,000 learners to identify which content delivery modality maximises both completion rates and knowledge retention — with full statistical discipline and device-stratified analysis.

### Experimental Arms

| Arm | Modality |
|---|---|
| **Control** | Long-form 40-minute video |
| **Variant B** | Modular micro-videos |
| **Variant C** | Micro-videos + in-video mini quizzes |
| **Variant D** | Concept shorts + applied take-home assignment |

### Analytical Approach

1. **Completion Rate Testing** — Two-sample proportion Z-tests with **Bonferroni-Holm multiple comparison corrections** to control family-wise error rate across all pairwise variant comparisons.
2. **Knowledge Retention Testing** — Welch's t-tests for retention score differences, robust to unequal variance across arms.
3. **Heterogeneous Treatment Effects** — Subgroup interaction analysis decomposing outcomes by **mobile vs. desktop device type**, revealing format-specific friction for mobile-first learners.
4. **Executive Scorecard** — Multi-dimensional PivotTables in Google Sheets with uplift calculations and conditional formatting for stakeholder communication.
5. **Rollout Sensitivity Modelling** — Interactive Streamlit dashboard enabling product and business stakeholders to evaluate rollout trade-offs across confidence intervals and threshold scenarios.

### Tech Stack

- **Statistics**: SciPy (Z-tests, Welch's t-tests, Bonferroni-Holm corrections) · Statsmodels
- **Analysis**: Python · Pandas · NumPy · Matplotlib · Seaborn
- **Scorecard**: Google Sheets Executive A/B Scorecard (PivotTables, conditional formatting)
- **Dashboard**: Streamlit (rollout slider, mobile/desktop sensitivity, CI visualisation)
- **Notebook**: JupyterLab (fully executed, all cells run)

## Measurable Business Impact

| Metric | Result |
|---|---|
| Experiment scale | **4,000 learners** across 4 content format arms |
| Statistical corrections applied | Bonferroni-Holm (controls false discovery across multiple comparisons) |
| Device interaction uncovered | Statistically significant mobile vs. desktop differential across variants |
| Key finding — Variant C | Micro-videos + mini quizzes achieved **~80% completion on both desktop and mobile** — neutralising the device gap entirely |
| Key finding — Variant D | Concept shorts + take-home showed severe mobile penalty (~22 percentage point drop vs. desktop) |
| Rollout recommendation | **Variant C** — highest completion, highest retention, device-resilient, production-ready |
| Business value | Evidence-based content investment framework replacing anecdotal decision-making; prevents costly rollout of mobile-hostile formats |

The subgroup interaction finding — that only Variant C is resilient across mobile-first demographics — represents a decision that could not have been made from aggregate completion rates alone, and would have cost significant learner engagement if Variant D had been selected on headline numbers.

## Repository Contents

| File | Description |
|---|---|
| `starter.ipynb` | Starter notebook template |
| `final output 1.ipynb` | Fully executed analysis notebook (Z-tests, Welch's t-tests, Bonferroni-Holm, device interaction) |
| `final output 2.csv` | Executive A/B experimentation summary (sample sizes, completion rates, p-values, uplifts, retention) |
| `final output 3.xlsx` | Executive A/B Scorecard (Google Sheets export with PivotTables) |
| `final output 4.py` | Interactive Streamlit rollout decision dashboard |
| `input 1.csv` | Learner trial dataset (4,000 records across 4 arms) |
| `input 2.csv` | Course curriculum syllabus catalog (20 modules) |
| `analyze_ab_test.py` | Statistical analysis pipeline script |
| `generate_content_ab_data.py` | Synthetic dataset generation script |
| `generate_modules_catalog.py` | Module catalog generation script |
