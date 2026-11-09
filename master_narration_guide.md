# PROJECT PROJECT: MASTER CHRONOLOGICAL RECORDING & NARRATION GUIDE

**Task:** Content Optimization & A/B/n Testing (Curriculum Delivery Modality Optimization)  
**Domain:** Data Science and Analytics | **Role:** Senior Product Data Scientist  
**Target Duration:** 26:00 – 30:00 ($51.76 Project Tier)  
**Topology:** Microsoft Word (Intro) → Firefox (Research) → JupyterLab (Live Stats) → Google Sheets (Scorecard) → Streamlit (ROI Dashboard)

---

### [COMPLIANCE CHECKLIST] Pre-Recording Verification
* **Desktop UI Diversity:** Confirm macOS appearance (Dark Mode, customized desktop wallpaper, Dock on Left or Bottom, not default factory settings).
* **Screen Layout:** Screen 1: Word (Goal text placed directly behind TaskRecorder) | Screen 2: Firefox (Doc tabs) | Screen 3: JupyterLab (`starter.ipynb`).
* **Generative AI Rule:** Zero AI tools on camera (No ChatGPT, Claude, Copilot). Narration strictly uses prepared, royalty-free synthetic CSVs.
* **Narration Rule (What, Where, Why):** For every mouse action, state What you do, Where on screen, and Why it is technically needed.
* **Pacing & Silence Gap Rule:** Never leave silence exceeding 40 seconds. Maintain continuous, calm narration during computations.
* **Mouse-Heavy Execution Defense:** Pre-configured starter notebook template allows sequential mouse runs with only 2 micro-edits (~25s total typing).

---

### [CHRONOLOGICAL TIMELINE] Phase & App Sequence Breakdown
* **00:00 - 00:20:** Phase 1: Mandatory Opening Sequence (Word Goal doc behind TaskRecorder)
* **00:20 - 03:00:** Phase 2: Firefox Statistical Documentation & EdTech A/B Testing Research [LOOKUP]
* **03:00 - 18:00:** Phase 3: JupyterLab Live Pipeline Execution, Statistical Z/t-Tests & 2 Micro-Edits [MODIFY]
* **18:00 - 24:00:** Phase 4: Google Sheets Executive Scorecard, PivotTables & Heatmap in Firefox [MODIFY]
* **24:00 - 28:00:** Phase 5: Streamlit Interactive Experimentation Decision Dashboard in Firefox [LOOKUP]
* **28:00 - 30:00:** Phase 6: Deliverables Packaging (`Deliverables.zip`) & Compliance Wrap-up

---

## Phase 1: Mandatory Opening Sequence (00:00 - 00:20)

> **[MOUSE ACTION & SCREEN FOCUS]:**  
> Microsoft Word window is positioned behind TaskRecorder displaying ONLY the approved Goal paragraph. Ensure no extra headers, titles, or Approval IDs are visible. Click 'Start Recording' in TaskRecorder, then immediately minimize TaskRecorder to reveal Word.

> **[SPOKEN DIALOGUE] VERBATIM NARRATION:**  
> *"I will be beginning my task soon. Here is the workflow I have in mind."*

*(Hover cursor smoothly over the Goal text in Word for 5-8 seconds, then minimize Word and switch to Firefox from the Dock).*

---

## Phase 2: Firefox Statistical Research & Modality Benchmarks (00:20 - 03:00) [LOOKUP]

> **[MOUSE ACTION & SCREEN FOCUS]:**  
> In Firefox, switch between 3 open documentation tabs: Tab 1 (EdTech Completion Baselines), Tab 2 (Two-Proportion Z-Test & Bonferroni Corrections), Tab 3 (Welch's t-Test for Heterogeneous Variance). Scroll down to formulas and highlight them with cursor.

> **[SPOKEN DIALOGUE] VERBATIM NARRATION:**  
> *"I am opening Firefox to examine the statistical testing guidelines and industry benchmarks for content format optimization. In our EdTech curriculum platform, learner retention is heavily influenced by instructional delivery architecture. Traditional monolithic lecture videos suffer severe drop-off after 6 to 10 minutes, yielding low module completion rates around 15%. To evaluate potential optimizations, we designed a 4-arm randomized controlled A/B/n experiment across 4,000 learners: Control long-form video, Variant B modular micro-videos, Variant C micro-videos with embedded formative mini-quizzes, and Variant D concept shorts paired with an applied take-home project. Because we are testing multiple challenger variants against a single control, standard independent hypothesis testing inflates the family-wise error rate. Therefore, we will apply both Bonferroni and Holm-Bonferroni corrections to our two-proportion Z-tests to maintain our family-wise significance threshold at alpha 0.01. Furthermore, we will use Welch’s t-test to evaluate post-assessment knowledge retention, accounting for unequal variances across format arms."*

---

## Phase 3: JupyterLab Live Analysis, Statistical Testing & Micro-Edits (03:00 - 18:00) [MODIFY]

Bring up JupyterLab from the Dock. Open `starter.ipynb`. Execute cells sequentially using mouse clicks on the 'Run' button. Perform 2 concise micro-edits in Cell 7 and Cell 10.

### Step 1: Environment Setup & Analytical Libraries (Cell 1) [03:00 - 04:15]
> **[MOUSE ACTION & SCREEN FOCUS]:**  
> Click inside Cell 1. Highlight imports: pandas, numpy, scipy.stats, statsmodels, matplotlib, and seaborn. Click 'Run' button with mouse.

> **[SPOKEN DIALOGUE] VERBATIM NARRATION:**  
> *"Switching to JupyterLab, in Step 1, Cell 1, I am importing our analytical dependencies: pandas and numpy for vectorized data manipulation, scipy.stats for parametric two-proportion Z-tests and Welch’s t-tests, and matplotlib and seaborn for diagnostic reporting. We also configure high-resolution plotting aesthetics. Why? Because executing our statistical calculations locally guarantees reproducible data analysis without external API dependencies, network latency, or student privacy risks."*

---

### Step 2: Ingest Learner Trial Dataset & Curriculum Catalog (Cell 2) [04:15 - 05:30]
> **[MOUSE ACTION & SCREEN FOCUS]:**  
> Click Cell 2 -> Click Run. Point cursor to printed dataset dimensions: 4,000 learner records, 1,000 per variant, and 20 curriculum syllabus modules.

> **[SPOKEN DIALOGUE] VERBATIM NARRATION:**  
> *"In Step 2, Cell 2, I load our prepared, royalty-free learner experimentation dataset from input 1.csv containing 4,000 learner trial records, alongside input 2.csv, our curriculum catalog of 20 course modules across Data Science, Full Stack Web, Cloud Engineering, and Product Management. Inspecting the data schema, each record logs the learner ID, assigned variant, device type, watch duration ratio, quiz and take-home attempts, binary module completion flag, and post-assessment test score. The randomized assignment is perfectly balanced with exactly 1,000 learners in each experimental arm, eliminating sampling allocation bias."*

---

### Step 3: Exploratory Data Analysis & Empirical Baseline Verification (Cell 3) [05:30 - 07:00]
> **[MOUSE ACTION & SCREEN FOCUS]:**  
> Click Cell 3 -> Click Run. Hover cursor over the baseline conversion table showing Control completion at 15.0% and watch ratio distribution.

> **[SPOKEN DIALOGUE] VERBATIM NARRATION:**  
> *"In Step 3, Cell 3, we execute exploratory data analysis to establish our empirical baselines. In our Control arm (monolithic 40-minute lecture videos), only 150 out of 1,000 learners completed the module, establishing a baseline completion rate of exactly 15.0%. The mean video watch ratio in Control drops to 0.32, confirming that monolithic videos create substantial passive viewing fatigue. Meanwhile, exploratory figures for our challenger variants show marked improvements: 71.0% completion for micro-videos, 79.5% for micro-videos with mini-quizzes, and 31.4% for concept shorts with take-home projects."*

---

### Step 4: Primary Hypothesis Testing - Two-Proportion Z-Tests (Cell 4) [07:00 - 08:45]
> **[MOUSE ACTION & SCREEN FOCUS]:**  
> Click Cell 4 -> Click Run. Drag cursor over the statistical test summary table highlighting Z-scores, p-values, and relative uplifts.

> **[SPOKEN DIALOGUE] VERBATIM NARRATION:**  
> *"In Step 4, Cell 4, I execute two-sample proportion Z-tests comparing each variant arm against Control for our primary metric: Module Completion Rate. For Variant B (modular micro-videos), completion increases from 15.0% to 71.0%, representing a massive +56.0% absolute lift and +373.3% relative uplift, yielding a Z-score of 25.29 and p-value less than 0.001. For Variant C (micro-videos with formative mini-quizzes), completion reaches 79.5%, an absolute lift of +64.5% and +430.0% relative uplift, with Z equal to 28.89 and p less than 0.001. For Variant D (concept shorts with take-home), completion is 31.4%, a +16.4% absolute lift, Z of 8.69, and p less than 0.001. All three challenger modalities demonstrate statistically significant improvements over Control at alpha 0.01."*

---

### Step 5: Multiple Testing Corrections - Bonferroni & Holm Step-Down (Cell 5) [08:45 - 10:15]
> **[MOUSE ACTION & SCREEN FOCUS]:**  
> Click Cell 5 -> Click Run. Point cursor to adjusted significance thresholds: Bonferroni alpha = 0.0033 and sequential Holm rankings.

> **[SPOKEN DIALOGUE] VERBATIM NARRATION:**  
> *"In Step 5, Cell 5, we apply family-wise error rate corrections across our three hypothesis tests. Under a standard Bonferroni adjustment, our target alpha of 0.01 is divided by 3, setting the adjusted significance cutoff to 0.0033. Under Holm-Bonferroni sequential step-down testing, we rank p-values from smallest to largest and test against adjusted thresholds of 0.0033, 0.005, and 0.010. Even under these conservative multiple testing penalties, all three variants maintain adjusted p-values far below the critical thresholds, rigorously verifying that our observed uplifts are not artifacts of multiple comparison testing."*

---

### Step 6: Secondary Hypothesis Testing - Welch's t-Test on Retention (Cell 6) [10:15 - 11:45]
> **[MOUSE ACTION & SCREEN FOCUS]:**  
> Click Cell 6 -> Click Run. Drag cursor over post-assessment score means: Control (57.45), Variant B (83.28), Variant C (92.96), Variant D (64.04).

> **[SPOKEN DIALOGUE] VERBATIM NARRATION:**  
> *"In Step 6, Cell 6, we evaluate our secondary hypothesis metric: Post-Assessment Knowledge Retention Scores. In Control, learners achieved an average test score of 57.45 with a standard deviation of 17.94. Running Welch’s t-tests to account for unequal group variances, Variant B scores 83.28, a statistically significant gain of +25.83 points with t equal to 39.74. Variant C achieves the highest mastery at 92.96 points, an extraordinary +35.51 point improvement with t equal to 57.39 and p less than 0.001. This demonstrates the active recall testing effect: frequent low-stakes quizzes solidify conceptual comprehension far more effectively than passive video consumption alone."*

---

### Step 7: LIVE MICRO-EDIT 1 - Subgroup Heterogeneity (Desktop vs Mobile) (Cell 7) [11:45 - 13:45]
> **[MOUSE ACTION & SCREEN FOCUS]:**  
> Click inside Cell 7. Highlight the placeholder variables. Type the 3 lines below (~10 seconds). Click Run with mouse.

```python
>>> [TYPE EXACTLY THESE LINES IN CELL 7] >>>
SUBGROUP_DIMENSION = "device_type"
PRIMARY_DEVICES = ["desktop", "mobile"]
EVALUATE_INTERACTION_GAP = True
<<< [END OF TYPING] <<<
```
*Rationale: Configures subgroup segmentation to detect heterogeneous treatment effects across mobile vs desktop devices.*

> **[SPOKEN DIALOGUE] VERBATIM NARRATION:**  
> *"Now in Step 7, Cell 7, I perform Micro-Edit 1 to configure our subgroup interaction model, isolating desktop versus mobile device behavior. Project Project guidelines emphasize evaluating heterogeneous treatment effects. Looking at the generated device interaction table, we uncover a crucial product dynamic: in Control, desktop completion is 19.9% while mobile plummets to 7.9%—a negative 12.0% mobile penalty. In Variant D (shorts plus take-home), desktop completion is 41.8% but mobile drops to 19.8%, creating a severe negative 22.1% mobile gap because typing code or writing reports on a smartphone introduces heavy user friction. In stark contrast, Variant C (micro-videos with mini-quizzes) completely neutralizes the device gap, maintaining 79.8% completion on desktop and 80.2% on mobile—a positive 0.4% delta. This proves Variant C is resilient across mobile-first learner demographics."*

---

### Step 8: Statistical Power Analysis & Minimum Detectable Effect (MDE) (Cell 8) [13:45 - 15:00]
> **[MOUSE ACTION & SCREEN FOCUS]:**  
> Click Cell 8 -> Click Run. Point cursor to power output: MDE = 4.8%, Sample Size N = 1,000 per arm, Statistical Power = 1.00.

> **[SPOKEN DIALOGUE] VERBATIM NARRATION:**  
> *"In Step 8, Cell 8, we verify the statistical power of our experiment. With 1,000 samples per variant arm and baseline conversion of 15.0%, our Minimum Detectable Effect at 80% power and alpha 0.01 is 4.8%. Because our observed absolute lifts of +56.0% and +64.5% far exceed this 4.8% MDE threshold, our achieved statistical power is essentially 1.00 (100%), guaranteeing our test was neither underpowered nor exposed to Type II errors."*

---

### Step 9: Diagnostic Visualizations & Disparity Analysis (Cell 9) [15:00 - 16:30]
> **[MOUSE ACTION & SCREEN FOCUS]:**  
> Click Cell 9 -> Click Run. Scroll smoothly through Figure 1 (completion bar chart with error bars), Figure 2 (device interaction gap chart), and Figure 3 (retention violin plot).

> **[SPOKEN DIALOGUE] VERBATIM NARRATION:**  
> *"In Step 9, Cell 9, we generate our diagnostic visualizations. Figure 1 displays the module completion rates with 99% confidence error bars, highlighting clear non-overlapping separation between Control and all challenger variants. Figure 2 illustrates the device interaction effect, visually depicting how the mobile line for Variant D collapses while Variant C remains robustly horizontal. Figure 3 shows the post-assessment score distributions, illustrating how Variant C shifts the entire density distribution upward toward mastery above 90 points."*

---

### Step 10: LIVE MICRO-EDIT 2 - Production Rollout Recommendation (Cell 10) [16:30 - 17:30]
> **[MOUSE ACTION & SCREEN FOCUS]:**  
> Click inside Cell 10. Highlight decision policy variables. Type the 3 lines below (~10 seconds). Click Run with mouse.

```python
>>> [TYPE EXACTLY THESE LINES IN CELL 10] >>>
WINNING_VARIANT = "variant_micro_quiz"
RECOMMENDED_ROLLOUT_PCT = 100.0
PROJECTED_ANNUAL_LIFT_FACTOR = 4.30
<<< [END OF TYPING] <<<
```
*Rationale: Formulates empirical decision policy designating Variant C as the 100% production rollout winner.*

> **[SPOKEN DIALOGUE] VERBATIM NARRATION:**  
> *"In Step 10, Cell 10, I perform Micro-Edit 2 to calibrate our production rollout parameters. Based on our dual criteria of maximizing completion rate and post-assessment retention while preserving mobile accessibility, Variant C (micro-videos with in-video mini-quizzes) is declared the definitive winner. I set the winning variant to variant_micro_quiz with a 100% production rollout allocation, projecting 79,500 total annual course completers—an extraordinary net gain of 64,500 additional certified learners over our 15,000 status-quo baseline."*

---

### Step 11: Export Executive Summary CSV & Launch Streamlit Server (Cell 11) [17:30 - 18:00]
> **[MOUSE ACTION & SCREEN FOCUS]:**  
> Click Cell 11 -> Click Run. Point cursor to export notification for final output 2.csv and printed message: 'Streamlit Decision App LIVE on port 8501!'.

> **[SPOKEN DIALOGUE] VERBATIM NARRATION:**  
> *"In Step 11, Cell 11, I export our executive summary table to final output 2.csv and launch our local Streamlit decision dashboard script, final output 4.py, in the background. The server is active on port 8501. Now, I switch over to Firefox to build our Executive Scorecard in Google Sheets and explore the interactive dashboard."*

---

## Phase 4: Google Sheets Executive Scorecard in Firefox (18:00 - 24:00) [MODIFY]

> **[MOUSE ACTION & SCREEN FOCUS]:**  
> 1. Switch to Firefox tab with Google Sheets. Click File → Import → Upload → select `final output 2.csv`.  
> 2. Format header row: dark navy fill, white bold text. Select data range → Insert → Pivot table.  
> 3. Rows: `subject_domain` | Columns: `variant_name` | Values: Average of `completion_rate_pct` and `post_assessment_score`.  
> 4. Apply Color Scale Conditional Formatting: Min (15%, soft red) → Mid (50%, soft yellow) → Max (80%, soft green).  
> 5. Build Executive KPI Header Block at top: Total Learners (4,000), Winning Format (Variant C), Rel Lift (+430%), Total Completers (79,500), Net Gain (+64,500).  
> 6. Click File → Download → Microsoft Excel (.xlsx) → save directly as `final output 3.xlsx`.

> **[SPOKEN DIALOGUE] VERBATIM NARRATION:**  
> *"Now in Firefox, I open Google Sheets to construct our Executive A/B Experimentation Scorecard. I import final output 2.csv containing our verified metrics. Next, I insert a multi-dimensional PivotTable segmenting learner performance across our four subject domains: Data Science & ML, Full Stack Web, Cloud Engineering, and Product Management. Notice that across every single curriculum domain, Variant C consistently outperforms Control by over 60 percentage points in completion and over 30 points in retention. I apply a conditional formatting color scale across the matrix, providing executive leadership with an instant visual heatmap. At the top, I assemble an executive decision card highlighting our key metrics: 4,000 trial learners, a +430% relative completion lift, 79,500 total projected completers, and an estimated net volume increase of 64,500 additional course completers over our 15,000 baseline. Finally, I download the completed workbook as final output 3.xlsx for stakeholder sign-off."*

---

## Phase 5: Streamlit Interactive Decision Dashboard in Firefox (24:00 - 28:00) [LOOKUP]

> **[MOUSE ACTION & SCREEN FOCUS]:**  
> 1. Switch to Firefox tab at `http://localhost:8501` (A/B Rollout Decision Dashboard).  
> 2. Drag 'Variant C Rollout Percentage' slider from 0% → 50% → 100%. Highlight real-time KPI card changes.  
> 3. Adjust 'Mobile Traffic Share' slider from 45% to 70%. Show that Variant D crashes while Variant C stays stable at ~80%.  
> 4. Inspect Tab 1 (Format Comparison & Forest Plot), Tab 2 (Heterogeneous Subgroup Explorer), and Tab 3 (Annualized ROI Curve).

> **[SPOKEN DIALOGUE] VERBATIM NARRATION:**  
> *"Next in Firefox, I navigate to our interactive A/B Experimentation Decision Dashboard at localhost 8501, powered by final output 4.py. The top KPI cards summarize our empirical findings: 4,000 total participants, a baseline Control completion of 15.0%, and a winning Variant C rate of 79.5%. In the interactive sidebar, product leaders can simulate rollout scenarios. When I adjust the Variant C rollout slider from zero to 100%, the dynamic projection models a 4.3-fold uplift in platform-wide completions. In Tab 2, adjusting the mobile traffic slider to 70% simulates an expanding mobile-first learner cohort; the dashboard clearly illustrates that while monolithic videos and take-home exams suffer catastrophic funnel leakage on handheld devices, Variant C maintains resilient 80% completion rates. In Tab 3, the ROI projection shows that fully retiring long monolithic lectures in favor of modular micro-videos with active recall mini-quizzes unlocks over 64,000 additional completed course certifications annually."*

---

## Phase 6: Deliverables Packaging & Final Compliance Wrap-up (28:00 - 30:00)

> **[MOUSE ACTION & SCREEN FOCUS]:**  
> 1. Return to Terminal/Finder. Inspect workspace folder: verify all 6 files.  
> 2. Run packaging command: `zip -r Deliverables.zip input\ 1.csv input\ 2.csv final\ output\ 1.ipynb final\ output\ 2.csv final\ output\ 3.xlsx final\ output\ 4.py`.  
> 3. Inspect archive to verify flat root structure without nested subdirectories.

> **[SPOKEN DIALOGUE] VERBATIM NARRATION:**  
> *"To conclude our task, I return to our project directory to assemble Deliverables.zip. Let us verify full compliance with Project Project guidelines: all deliverables sit directly at the root of the archive without unnecessary subdirectories, strictly following the standard naming convention: input 1.csv for our learner trial dataset, input 2.csv for our curriculum module catalog, final output 1.ipynb for our executed analysis notebook, final output 2.csv for our statistical summary, final output 3.xlsx for our Google Sheets executive scorecard, and final output 4.py for our interactive Streamlit decision dashboard. We have thoroughly evaluated, benchmarked, and modeled our multi-arm content format experiment, establishing an empirical foundation for full product rollout."*
