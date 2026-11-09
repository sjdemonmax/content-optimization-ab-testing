"""
Generate synthetic A/B/C/D experimentation dataset for content format optimization.
Simulates realistic EdTech learner behavior across four distinct content modalities:
- Control (A): Long-form Lecture Videos (30-45 mins)
- Variant B: Chunked Micro-learning Videos (3-6 mins)
- Variant C: Micro-learning Videos + In-Video Interactive Mini-Quizzes
- Variant D: Bite-sized Concept Shorts/Reels (60-90s) + Practical Take-home Exam

Calibrated against empirical EdTech benchmarks:
- Long videos: ~18% completion rate, steep drop-off past 6 mins
- Micro videos: ~68% completion rate, higher steady watch ratio
- Micro videos + Mini Quizzes: ~78% completion rate, active recall boosts post-test score (+12 pts)
- Shorts/Reels + Take-home: ~42% completion rate (take-home creates friction), but top scores for submitters
- Mobile vs Desktop platform interaction effects
"""

import csv
import math
import random
from datetime import datetime, timedelta

# Set fixed seed for reproducibility
random.seed(42)

NUM_LEARNERS = 4000
VARIANTS = [
    "control_long_video",
    "variant_micro_video",
    "variant_micro_quiz",
    "variant_shorts_takehome"
]

DEVICES = ["desktop", "mobile", "tablet"]
DEVICE_WEIGHTS = [0.45, 0.45, 0.10]

DOMAINS = ["Data Science & ML", "Full Stack Web", "Cloud Engineering", "Product Management"]
EXPERIENCE_LEVELS = ["beginner", "intermediate", "advanced"]
EXPERIENCE_WEIGHTS = [0.50, 0.35, 0.15]

START_DATE = datetime(2026, 9, 1)

rows = []

for i in range(1, NUM_LEARNERS + 1):
    learner_id = f"LRN-{10000 + i}"
    
    # Stratified variant assignment (1000 learners per arm)
    variant = VARIANTS[(i - 1) % len(VARIANTS)]
    
    device = random.choices(DEVICES, weights=DEVICE_WEIGHTS)[0]
    subject = random.choice(DOMAINS)
    experience = random.choices(EXPERIENCE_LEVELS, weights=EXPERIENCE_WEIGHTS)[0]
    
    # Signup date distributed over 4 weeks
    days_offset = random.randint(0, 28)
    cohort_week = f"2026-W{36 + (days_offset // 7)}"
    
    # Baseline engagement modifiers based on experience and device
    exp_mod = {"beginner": -0.05, "intermediate": 0.05, "advanced": 0.10}[experience]
    
    # Format-specific behavioral simulation
    if variant == "control_long_video":
        # Long videos: ~40 mins planned duration. Desktop users do better than mobile.
        planned_duration_mins = 42.0
        mobile_penalty = -0.15 if device == "mobile" else 0.0
        base_completion_prob = 0.20 + exp_mod + mobile_penalty
        base_completion_prob = max(0.05, min(0.40, base_completion_prob))
        
        is_completed = 1 if random.random() < base_completion_prob else 0
        if is_completed:
            watch_ratio = round(random.uniform(0.85, 1.0), 3)
            time_spent_mins = round(planned_duration_mins * watch_ratio + random.uniform(-2, 5), 1)
        else:
            # Steep drop-off curve: most drop off before 10-15 mins
            watch_ratio = round(random.betavariate(1.2, 3.5), 3)
            watch_ratio = min(0.84, max(0.02, watch_ratio))
            time_spent_mins = round(planned_duration_mins * watch_ratio, 1)
            
        quizzes_attempted = 0
        quiz_score = None
        takehome_submitted = 0
        takehome_score = None
        
        # Post-module assessment score (0-100)
        base_score = 62.0 + (15.0 * watch_ratio) + (10.0 if experience == "advanced" else (5.0 if experience == "intermediate" else 0))
        post_assessment_score = round(max(20.0, min(100.0, base_score + random.gauss(0, 8))), 1) if watch_ratio > 0.3 else round(random.gauss(45, 10), 1)
        
        satisfaction_rating = random.choices([1, 2, 3, 4, 5], weights=[0.15, 0.25, 0.35, 0.20, 0.05])[0]

    elif variant == "variant_micro_video":
        # Micro videos: 5 chunks of 4 mins = 20 mins total. High completion on all devices.
        planned_duration_mins = 20.0
        mobile_boost = 0.05 if device == "mobile" else 0.0
        base_completion_prob = 0.68 + exp_mod + mobile_boost
        base_completion_prob = max(0.45, min(0.88, base_completion_prob))
        
        is_completed = 1 if random.random() < base_completion_prob else 0
        if is_completed:
            watch_ratio = round(random.uniform(0.90, 1.0), 3)
            time_spent_mins = round(planned_duration_mins * watch_ratio + random.uniform(-1, 3), 1)
        else:
            watch_ratio = round(random.betavariate(2.0, 1.5), 3)
            watch_ratio = min(0.89, max(0.10, watch_ratio))
            time_spent_mins = round(planned_duration_mins * watch_ratio, 1)
            
        quizzes_attempted = 0
        quiz_score = None
        takehome_submitted = 0
        takehome_score = None
        
        base_score = 68.0 + (16.0 * watch_ratio) + (8.0 if experience == "advanced" else (4.0 if experience == "intermediate" else 0))
        post_assessment_score = round(max(25.0, min(100.0, base_score + random.gauss(0, 7))), 1) if watch_ratio > 0.3 else round(random.gauss(50, 9), 1)
        
        satisfaction_rating = random.choices([1, 2, 3, 4, 5], weights=[0.05, 0.10, 0.30, 0.40, 0.15])[0]

    elif variant == "variant_micro_quiz":
        # Micro videos + In-video interactive mini-quizzes (Active recall)
        planned_duration_mins = 24.0 # 20 mins video + 4 mins quizzes
        base_completion_prob = 0.77 + exp_mod
        base_completion_prob = max(0.55, min(0.92, base_completion_prob))
        
        is_completed = 1 if random.random() < base_completion_prob else 0
        if is_completed:
            watch_ratio = round(random.uniform(0.92, 1.0), 3)
            time_spent_mins = round(planned_duration_mins * watch_ratio + random.uniform(0, 6), 1)
            quizzes_attempted = random.randint(4, 5)
        else:
            watch_ratio = round(random.betavariate(2.2, 1.3), 3)
            watch_ratio = min(0.89, max(0.15, watch_ratio))
            time_spent_mins = round(planned_duration_mins * watch_ratio, 1)
            quizzes_attempted = random.randint(1, 3) if watch_ratio > 0.25 else 0
            
        if quizzes_attempted > 0:
            q_mean = 78.0 + (8.0 if experience == "advanced" else (4.0 if experience == "intermediate" else 0))
            quiz_score = round(max(30.0, min(100.0, random.gauss(q_mean, 10))), 1)
        else:
            quiz_score = None
            
        takehome_submitted = 0
        takehome_score = None
        
        # Noticeable active recall boost (+10-14 points on post assessment)
        base_score = 76.0 + (18.0 * watch_ratio) + (6.0 if experience == "advanced" else (3.0 if experience == "intermediate" else 0))
        post_assessment_score = round(max(30.0, min(100.0, base_score + random.gauss(0, 6))), 1) if watch_ratio > 0.3 else round(random.gauss(55, 8), 1)
        
        satisfaction_rating = random.choices([1, 2, 3, 4, 5], weights=[0.03, 0.07, 0.20, 0.45, 0.25])[0]

    else: # variant_shorts_takehome
        # Reels / Shorts (6 mins total) + Take-home Applied Assignment (45-60 mins)
        planned_duration_mins = 50.0
        # Mobile users love the shorts but hate doing complex take-home on phone
        mobile_penalty = -0.25 if device == "mobile" else 0.0
        base_completion_prob = 0.44 + exp_mod + mobile_penalty
        base_completion_prob = max(0.15, min(0.65, base_completion_prob))
        
        is_completed = 1 if random.random() < base_completion_prob else 0
        # Watch ratio for shorts is almost always high
        shorts_watch_ratio = round(random.uniform(0.80, 1.0), 3)
        watch_ratio = shorts_watch_ratio
        
        quizzes_attempted = 0
        quiz_score = None
        
        if is_completed:
            takehome_submitted = 1
            th_mean = 84.0 + (6.0 if experience == "advanced" else 0)
            takehome_score = round(max(40.0, min(100.0, random.gauss(th_mean, 8))), 1)
            time_spent_mins = round(6.0 + random.uniform(35, 60), 1)
            # High conceptual mastery for those who actually complete the take-home project
            post_assessment_score = round(max(50.0, min(100.0, 82.0 + random.gauss(0, 7))), 1)
            satisfaction_rating = random.choices([1, 2, 3, 4, 5], weights=[0.05, 0.10, 0.15, 0.35, 0.35])[0]
        else:
            takehome_submitted = 1 if random.random() < 0.20 else 0
            if takehome_submitted:
                takehome_score = round(max(30.0, min(80.0, random.gauss(58, 12))), 1)
                time_spent_mins = round(6.0 + random.uniform(15, 30), 1)
                post_assessment_score = round(random.gauss(64, 10), 1)
            else:
                takehome_score = None
                time_spent_mins = round(6.0 * watch_ratio, 1)
                post_assessment_score = round(random.gauss(54, 9), 1)
            satisfaction_rating = random.choices([1, 2, 3, 4, 5], weights=[0.20, 0.30, 0.30, 0.15, 0.05])[0]

    # Bound post assessment score
    post_assessment_score = max(15.0, min(100.0, post_assessment_score))

    rows.append({
        "learner_id": learner_id,
        "cohort_week": cohort_week,
        "assigned_variant": variant,
        "subject_domain": subject,
        "device_type": device,
        "learner_experience": experience,
        "time_spent_mins": time_spent_mins,
        "video_watch_ratio": watch_ratio,
        "quizzes_attempted": quizzes_attempted,
        "quiz_score": quiz_score if quiz_score is not None else "",
        "takehome_submitted": takehome_submitted,
        "takehome_score": takehome_score if takehome_score is not None else "",
        "module_completed": is_completed,
        "post_assessment_score": post_assessment_score,
        "satisfaction_rating": satisfaction_rating
    })

fieldnames = [
    "learner_id",
    "cohort_week",
    "assigned_variant",
    "subject_domain",
    "device_type",
    "learner_experience",
    "time_spent_mins",
    "video_watch_ratio",
    "quizzes_attempted",
    "quiz_score",
    "takehome_submitted",
    "takehome_score",
    "module_completed",
    "post_assessment_score",
    "satisfaction_rating"
]

output_path = "content_ab_test_experiment.csv"
with open(output_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f"Generated {len(rows)} records in {output_path}")

# Calculate summary stats per variant
stats = {}
for r in rows:
    v = r["assigned_variant"]
    if v not in stats:
        stats[v] = {"count": 0, "completed": 0, "scores": [], "time": [], "ratings": []}
    stats[v]["count"] += 1
    stats[v]["completed"] += r["module_completed"]
    stats[v]["scores"].append(r["post_assessment_score"])
    stats[v]["time"].append(r["time_spent_mins"])
    stats[v]["ratings"].append(r["satisfaction_rating"])

print("\n--- EXPERIMENT SUMMARY BY VARIANT ---")
print(f"{'Variant':<26} | {'Sample':<6} | {'Comp. Rate':<10} | {'Avg Score':<10} | {'Avg Time (m)':<12} | {'Avg CSAT':<8}")
print("-" * 85)
for v, s in stats.items():
    comp_rate = (s["completed"] / s["count"]) * 100
    avg_score = sum(s["scores"]) / len(s["scores"])
    avg_time = sum(s["time"]) / len(s["time"])
    avg_csat = sum(s["ratings"]) / len(s["ratings"])
    print(f"{v:<26} | {s['count']:<6} | {comp_rate:6.1f}%    | {avg_score:6.1f}     | {avg_time:8.1f}     | {avg_csat:5.2f}")
