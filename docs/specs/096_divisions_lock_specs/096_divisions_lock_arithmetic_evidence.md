# Event 096 arithmetic evidence

## Result and evidence class

No arithmetic contradiction was found in the checked formulas. The capacity examples, force examples, batch bounds, review budgets, review delays, growth-hold boundaries, release and relock equality edges, AI score examples, and AI action delays all match the current specification when evaluated exactly. The reference script completed 94 arithmetic checks.

This document is **arithmetic evidence only**. It checks the written design with a deterministic reference script. It does not report HOI4 execution, native probability output, or engine validation. No native probability route or HOI4 tool name was exposed in `ALL_TOOLS` during this review. No event was run in game, and no random selection or native `ai_will_do` pool was evaluated.

The checked sources were Parts 2, 3, 4, and 5, plus Part 8 validation. The strict release rule in Part 1 and the day-floor bookkeeping in Part 7 were also read where needed to check equality and timing language. The complete reference script appears in the appendix and is also kept at `docs/plans/096_divisions_lock_plans/096_arithmetic_check.py`. Run it with:

```text
python docs/plans/096_divisions_lock_plans/096_arithmetic_check.py
```

The script uses exact rational arithmetic for the specified decimal constants and counts each check. Passing checks mean the equations agree with the examples. They do not prove that installed game inputs have the intended meaning or that an engine implementation follows the equations. The appendix is reference arithmetic code, not game implementation.

## Force and capacity checks

The force equation

```text
F = N + sum((w_b - 1) * n_b)
```

is algebraically equal to summing `weight * count` over each final type profile. A merge that preserves the battalion and support multiset therefore preserves F. Removing an actual support attachment changes F because the multiset changed.

| Structure | Exact force result |
| --- | ---: |
| Nine foot battalions and three basic support attachments | 12 |
| Eighteen foot battalions and three basic support attachments | 21 |
| Six medium armor, four motorized, and three basic support attachments | 23 |
| Twenty-four autonomous robot battalions and three basic support attachments | 75 |
| Four formations with six ordinary battalions each | 24 |
| One formation with twenty-four ordinary battalions | 24 |

The hypothetical capacity table was recalculated from `A_raw = 10 + 5P + 2T + 3C + 5M`. Evolution IV then applies `max(10, 0.55 * A_raw)` and rounds down to a quarter point. The unrounded Evolution IV column below is shown to make the floor operation visible.

| Fixture | Exact A_raw | Evolution IV before quarter flooring and floor | Final base A | Final Evolution IV A |
| --- | ---: | ---: | ---: | ---: |
| Small state | 16.50 | 9.075, so the ten point minimum applies | 16.50 | 10.00 |
| Minor | 55 | 30.25 | 55.00 | 30.25 |
| Regional industrial power | 244 | 134.20, floors to 134.00 | 244.00 | 134.00 |
| Large industrial power | 1040 | 572.00 | 1040.00 | 572.00 |
| Former power after major losses | 101 | 55.55, floors to 55.50 | 101.00 | 55.50 |
| Expanded late-campaign power | 1980 | 1089.00 | 1980.00 | 1089.00 |

These values match Part 2. The displayed examples also respect the quarter-point representation. For instance, `floor(4 * 134.20) / 4 = 134.00`, and `floor(4 * 55.55) / 4 = 55.50`.

## Severe batch bound

Part 3 currently defines the severe bound as:

```text
k = min(10, max(2, ceil(0.10 * e * N_owned)))
```

The arithmetic checks reproduce all three written examples:

| Raw excess e | N_owned | Unclamped ceiling | Formula result k |
| ---: | ---: | ---: | ---: |
| 0.75 | 20 | 2 | 2 |
| 0.75 | 100 | 8 | 8 |
| 1.00 | 400 | 40 | 10 |

The severe eligibility test is inclusive at `e = 0.75`. At that threshold, `N_owned = 2` still produces a formula bound of 2. The formula returns 2 whenever `e * N_owned` is at most 20. It returns 3 once that product exceeds 20. At a product of exactly 90 it returns 9, and above 90 the ceiling reaches the ten-unit cap. Part 3 further clamps the displayed request to the eligible pool and makes the action unavailable below two eligible formations. Those pool rules can reduce or disable the formula result.

The formula uses raw e, while the AI score uses capped `E = min(e, 2)`. For a twenty-division army, the batch bound is 4 at `e = 2` and 6 at `e = 3`, even though the AI score formulas have already saturated at `e = 2`. The two uses of excess are internally consistent.

## Release, relock, and review arithmetic

The held-state release test is inclusive on both boundaries:

```text
day >= earliest_release_day and F <= A
```

Thus a country at `F = A` can release exactly when the seven-day floor is reached. It cannot release one day earlier, or at the floor while any positive excess remains. This is distinct from evolved reacquisition, which is checked only during a post-release review.

| Rule | Equality edge | Result |
| --- | --- | --- |
| Held release at `F = A` and `day = earliest_release_day` | Equality satisfies both inclusive tests | Release is permitted |
| Evolution II force gate at `F = 1.25A` | First condition is strict `F > 1.25A` | No relock, even if the watch-baseline condition passes |
| Evolution II watch gate at `F = 1.15F_watch` | Second condition is inclusive `F >= 1.15F_watch` | This condition passes when the separate strict force gate also passes |
| Evolution III at `F = 1.15A` | Strict `F > 1.15A` | No relock |
| Evolution IV at `F = 1.05A` | Strict `F > 1.05A` | No relock |

Exact examples confirm the edges. With `A = 100`, Evolution II does not reacquire at `F = 125`, but does pass its force gate at `F = 125.25`. With `A = 90`, `F_watch = 100`, and `F = 115`, both Evolution II conditions pass because `115 > 112.5` and `115 = 1.15 * 100`. Evolution III at `A = 100` does not reacquire at 115 and does at 115.25. Evolution IV at `A = 100` does not reacquire at 105 and does at 105.25.

Part 4 now states the budget equations explicitly. The reference script checks these definitions:

| Regime | Budget interpretation | Checked peak excess examples |
| --- | --- | --- |
| II | 1 review | Always 1 |
| III | `3 + 1` when peak e is at least 1 | 3 below 1, 4 from 1 onward |
| IV | `4 + min(2, floor(peak e))` | 4 below 1, 5 from 1 to below 2, 6 from 2 onward |

These equations agree with the stated three-to-four and four-to-six ranges. The credit update is also non-additive: with two reviews already spent, a new target of four and one old remaining credit gives `max(1, 4 - 2) = 2` remaining, rather than adding a new grant on top of the old credit.

For each new watch, the checked delay uses `ceil(clamp(base / (1 + min(peak e, 2)), lower, upper))` days. Because each clamp endpoint is already an integer, clamping the ceiling to the same endpoints produces the same values.

| Peak e used for delay | Evolution II | Evolution III | Evolution IV |
| ---: | ---: | ---: | ---: |
| 0 | 30 days | 24 days | 15 days |
| 0.5 | 20 days | 16 days | 10 days |
| 1 | 15 days | 12 days | 8 days |
| 2 or more | 10 days | 8 days | 5 days |

For example, an Evolution III watch opened on day 100 with peak `e = 1` is due on day 112. Ordinary daily refreshes do not move that due day. A newly opened watch receives a new full delay. A later active regime may bring an existing appointment forward using its original start day, but the specification does not permit it to become due before the next game day.

## AI score and action-delay checks

In the peaceful, permissive posture pool, the formulas are `Hold = 40`, `Single = 20 + 40E`, and `Batch = 10 + 50E`, where `E = min(e, 2)`. The batch candidate is available only at severe excess and with its required safe pool. A hard veto `T`, `G`, or `O` bypasses the score pool and selects sticky retain.

| Raw e | Capped E | Hold score | Single score | Batch score | `d_AI` after successful oversized action |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 0 | 0 | 40 | 20 formula value | Unavailable | 10 days by formula, but no removal action is valid while compliant |
| 0.5 | 0.5 | 40 | 40 | Unavailable | 7 days |
| 0.75 | 0.75 | 40 | 50 | 47.5 | 6 days |
| 1 | 1 | 40 | 60 | 60 | 5 days |
| 1.5 | 1.5 | 40 | 80 | 85 | 4 days |
| 2 | 2 | 40 | 100 | 110 | 4 days |
| 3 | 2 | 40 | 100 | 110 | 3 days |

The `e = 0` row evaluates the written score expression only. It is not a valid removal posture because the country is not oversized. At `e = 0.5`, Hold and Single tie at 40. At `e = 1`, Single and Batch tie at 60. At `e >= 2`, scores saturate at 100 and 110, while the raw-e batch bound can still grow until it reaches its ten-unit cap.

The action interval is `d_AI = clamp(ceil(10 / (1 + e)), 2, 10)` days. It is recalculated from refreshed post-action excess only after a successful bounded action that leaves the country oversized. An unchanged clock tick does not reroll a sticky retain posture. A failed or empty attempt returns to sticky retain until a specified material change.

Part 5 treats a ten-percent change in force **or** allowance from its own stored posture baseline as a material change. Either value can trigger review independently. For a positive force baseline of 100, 109.99 is below the trigger and 110 meets it. For an allowance baseline of 200, a decrease to 180 meets the trigger even if force is unchanged. The comparison uses each value stored at the last posture choice, not a baseline rewritten after each poll. The zero-force baseline remains the explicit transition special case in Part 5.

## Growth-hold estimator checks

The updated Part 5 defines `G` with a linear endpoint estimator. It requires eight consecutive complete daily observations over seven elapsed days under the same actor, grant, and regime. With `delta_A = A_now - A_seven_days_ago`, `G` is true only while `F_now > A_now`, `delta_A > 0`, and:

```text
7 * (F_now - A_now) <= 30 * delta_A
```

The inequality is inclusive. For `A_now = 100`, `A_seven_days_ago = 93`, and `F_now = 130`, the gap is 30 and `delta_A` is 7. Both sides equal 210, so G is true. At `F_now = 129.75`, the gap is 29.75 and the inequality still passes. At `F_now = 130.25`, the gap is 30.25, the left side is 211.75, and G is false.

The script also checks that G is false for a compliant country, only seven observations, an incomplete or missing daily observation, zero or falling capacity growth, an endpoint that does not match the current observation, and a changed actor, grant, or regime. After a reset, seven new observations are insufficient. Eight consecutive complete observations under the new identity can restore a valid window if the growth inequality also passes. No missing observation is interpolated.

## Validation boundary

The checks support the expected results for validation fixtures M01, C09, E06, E07, E08, A01, A02, A03, A05, and A06. The fixtures still require their separate native evidence. This report does not prove the battalion counter boundary, timed-floor behavior, score-to-probability mapping, random selection, exact demobilization, MTTH distribution, lock behavior, persistence, or live game outcomes.

## Appendix: complete reference arithmetic script

The following fenced script is the exact reference arithmetic program run for this report. It is not HOI4 script and does not implement Event 096.

```python
from fractions import Fraction
from math import ceil


CHECK_COUNT = 0


def check(condition, description):
    global CHECK_COUNT
    CHECK_COUNT += 1
    if not condition:
        raise AssertionError(description)


def q(value):
    return Fraction(str(value))


def quarter_floor(value):
    scaled = value * 4
    return Fraction(scaled.numerator // scaled.denominator, 4)


def allowance(p, t, c, m, multiplier):
    raw = 10 + 5 * p + 2 * t + 3 * c + 5 * m
    final = quarter_floor(max(Fraction(10), multiplier * raw))
    return raw, final


def force(profile_counts):
    total = sum(profile_counts.values())
    premium = sum((weight - 1) * count for weight, count in profile_counts.items())
    return total + premium


def batch_bound(e, n_owned):
    if e < q("0.75"):
        return None
    raw = e * n_owned / 10
    return min(10, max(2, ceil(raw)))


def review_budget(stage, peak_e):
    if stage in {"base", "I"}:
        return 0
    if stage == "II":
        return 1
    if stage == "III":
        return 3 + int(peak_e >= 1)
    if stage == "IV":
        return 4 + min(2, peak_e.numerator // peak_e.denominator)
    return 0


def watch_delay(stage, peak_e):
    capped = min(peak_e, Fraction(2))
    numerators = {"II": 30, "III": 24, "IV": 15}
    lower = {"II": 10, "III": 8, "IV": 5}
    upper = {"II": 30, "III": 24, "IV": 15}
    days = ceil(Fraction(numerators[stage], 1) / (1 + capped))
    return min(upper[stage], max(lower[stage], days))


def ai_scores(e, eligible=100, veto=False):
    if veto:
        return {"hold": 40, "single": None, "batch": None}
    capped = min(e, Fraction(2))
    single = 20 + 40 * capped if eligible >= 1 else None
    batch = 10 + 50 * capped if e >= q("0.75") and eligible >= 2 else None
    return {"hold": 40, "single": single, "batch": batch}


def ai_delay(e):
    days = ceil(Fraction(10, 1) / (1 + e))
    return min(10, max(2, days))


def material_change(current, baseline):
    if baseline == 0:
        return current != 0
    return 10 * abs(current - baseline) >= baseline


def can_release(day, earliest_day, force_value, allowance_value):
    return day >= earliest_day and force_value <= allowance_value


def valid_growth_history(samples, actor, grant, regime, current_day, current_allowance):
    if len(samples) != 8:
        return False
    if not all(sample["complete"] for sample in samples):
        return False
    days = [sample["day"] for sample in samples]
    if days != list(range(days[0], days[0] + 8)) or days[-1] != current_day:
        return False
    if any(sample["actor"] != actor for sample in samples):
        return False
    if any(sample["grant"] != grant for sample in samples):
        return False
    if any(sample["regime"] != regime for sample in samples):
        return False
    return samples[-1]["allowance"] == current_allowance


def growth_hold(force_now, allowance_now, samples, actor, grant, regime, current_day):
    if force_now <= allowance_now:
        return False
    if not valid_growth_history(samples, actor, grant, regime, current_day, allowance_now):
        return False
    delta_allowance = allowance_now - samples[0]["allowance"]
    return delta_allowance > 0 and 7 * (force_now - allowance_now) <= 30 * delta_allowance


def make_growth_history(allowances, actor="AAA", grant=1, regime="IV", start_day=0):
    return [
        {
            "day": start_day + offset,
            "allowance": allowance,
            "complete": True,
            "actor": actor,
            "grant": grant,
            "regime": regime,
        }
        for offset, allowance in enumerate(allowances)
    ]


def threshold_tests():
    check(q(100) <= q(100), "held release equality")
    check(not (q(125) > q("1.25") * q(100)), "Evolution II strict lower threshold")
    check(q("125.25") > q("1.25") * q(100), "Evolution II above lower threshold")
    check(not (q(115) > q("1.15") * q(100)), "Evolution III strict threshold equality")
    check(q("115.25") > q("1.15") * q(100), "Evolution III above threshold")
    check(not (q(105) > q("1.05") * q(100)), "Evolution IV strict threshold equality")
    check(q("105.25") > q("1.05") * q(100), "Evolution IV above threshold")
    check(q(115) > q("1.25") * q(90), "Evolution II force condition")
    check(q(115) >= q("1.15") * q(100), "Evolution II baseline equality")
    check(q(125) >= q("1.15") * q(100), "Evolution II baseline above equality")
    check(not material_change(q("109.99"), q(100)), "force baseline below ten percent")
    check(material_change(q(110), q(100)), "force baseline ten percent increase")
    check(not material_change(q("180.5"), q(200)), "allowance baseline below ten percent")
    check(material_change(q(180), q(200)), "allowance baseline ten percent decrease")


def main():
    stage_iv = q("0.55")
    capacity_fixtures = {
        "Small state": (q("0.3"), q(1), q(1), q(0)),
        "Minor": (q(3), q(4), q(4), q(2)),
        "Regional": (q(15), q(12), q(20), q(15)),
        "Large industrial": (q(80), q(45), q(80), q(60)),
        "Former power": (q(5), q(6), q(8), q(6)),
        "Expanded late": (q(130), q(60), q(150), q(150)),
    }
    expected_base = [q("16.50"), q("55.00"), q("244.00"), q("1040.00"), q("101.00"), q("1980.00")]
    expected_iv = [q("10.00"), q("30.25"), q("134.00"), q("572.00"), q("55.50"), q("1089.00")]
    print("Capacity table exact arithmetic")
    for (name, inputs), base_expected, iv_expected in zip(capacity_fixtures.items(), expected_base, expected_iv):
        raw, base = allowance(*inputs, Fraction(1))
        _, iv = allowance(*inputs, stage_iv)
        check(base == base_expected, f"{name} base allowance")
        check(iv == iv_expected, f"{name} Evolution IV allowance")
        print(f"{name}: A_raw={raw}, Base={base}, EIV={iv}")

    print("Weighted force and merge invariance")
    ordinary = q(1)
    support = q(1)
    motorized = q("1.25")
    medium = q("2.5")
    robot = q(3)
    check(force({ordinary: 12}) == 12, "ordinary and support total 12")
    check(force({ordinary: 21}) == 21, "ordinary and support total 21")
    check(force({medium: 6, motorized: 4, support: 3}) == 23, "mixed armor and motorized total")
    check(force({robot: 24, support: 3}) == 75, "robot and support total")
    check(force({ordinary: 6}) * 4 == force({ordinary: 24}), "merge invariance")
    check(force({q("2.5"): 1}) == q("2.5"), "one final profile weight")
    print("9+3=12, 18+3=21, 6 medium+4 motorized+3 support=23")
    print("24 robots+3 support=75, four six-battalion formations equal one twenty-four-battalion formation")

    print("Severe batch bounds")
    batch_examples = [(q("0.75"), 20, 2), (q("0.75"), 100, 8), (q(1), 400, 10)]
    for e, n, expected in batch_examples:
        actual = batch_bound(e, n)
        check(actual == expected, f"batch example e={e}, N_owned={n}")
        print(f"e={e}, N_owned={n}, k={actual}")
    check(batch_bound(q("0.7499"), 100) is None, "severe gate below 0.75")
    check(batch_bound(q("0.75"), 2) == 2, "severe gate inclusive at 0.75")
    check(batch_bound(q(1), 20) == 2, "batch lower range includes e times N equal 20")
    check(batch_bound(q("1.0001"), 20) == 3, "batch rises above e times N equal 20")
    check(batch_bound(q(1), 90) == 9, "batch below cap at e times N equal 90")
    check(batch_bound(q("1.0001"), 90) == 10, "batch reaches cap above e times N equal 90")
    check(batch_bound(q(2), 20) == 4, "raw e batch bound at e two")
    check(batch_bound(q(3), 20) == 6, "raw e batch bound above capped score range")
    print("Threshold checks: severe gate is inclusive at 0.75, lower bound is 2, k rises above e*N_owned=20, cap begins above 90")
    print("Raw e changes k after E has saturated, for example N=20 gives k=4 at e=2 and k=6 at e=3")

    print("Review budgets and anchored delays")
    budget_points = [q(0), q("0.99"), q(1), q("1.99"), q(2), q(3)]
    for e in budget_points:
        print(f"peak e={e}: B_III={review_budget('III', e)}, B_IV={review_budget('IV', e)}")
    check(review_budget("base", q(2)) == 0, "base review budget")
    check(review_budget("I", q(2)) == 0, "Evolution I review budget")
    check(review_budget("II", q(2)) == 1, "Evolution II review budget")
    check([review_budget("III", e) for e in budget_points] == [3, 3, 4, 4, 4, 4], "Evolution III budget formula")
    check([review_budget("IV", e) for e in budget_points] == [4, 4, 5, 5, 6, 6], "Evolution IV budget formula")
    for e in [q(0), q("0.5"), q(1), q(2), q(3)]:
        print(f"peak e={e}: II={watch_delay('II', e)}d, III={watch_delay('III', e)}d, IV={watch_delay('IV', e)}d")
    check(watch_delay("II", q("0.5")) == 20, "Evolution II delay at e 0.5")
    check(watch_delay("III", q("0.5")) == 16, "Evolution III delay at e 0.5")
    check(watch_delay("IV", q("0.5")) == 10, "Evolution IV delay at e 0.5")
    check(watch_delay("II", q(1)) == 15, "Evolution II delay at e 1")
    check(watch_delay("III", q(1)) == 12, "Evolution III delay at e 1")
    check(watch_delay("IV", q(1)) == 8, "Evolution IV delay at e 1")
    check(watch_delay("II", q(2)) == 10, "Evolution II delay at capped e 2")
    check(watch_delay("III", q(2)) == 8, "Evolution III delay at capped e 2")
    check(watch_delay("IV", q(2)) == 5, "Evolution IV delay at capped e 2")
    print("Watch starting day 100 with e=1 in III remains due on day 112 through ordinary daily refreshes")

    print("Strict release and relock edges")
    threshold_tests()
    check(not can_release(6, 7, q(100), q(100)), "no release before floor")
    check(can_release(7, 7, q(100), q(100)), "release at floor and force equality")
    check(not can_release(7, 7, q("100.25"), q(100)), "no release with positive excess")
    check(not (q(100) > q(100)), "release equality is not excess")
    print("Held release requires day>=m and F<=A, with equality accepted at both boundaries")
    print("Relock thresholds exclude equality at 1.25A, 1.15A, and 1.05A")
    print("Evolution II accepts equality at 1.15 F_watch when its separate strict F>1.25A condition also passes")
    print("F or A independently reaches the material-change trigger at an absolute 10 percent from its own stored baseline")

    print("AI growth-hold estimator")
    exact_history = make_growth_history([q(93 + i) for i in range(8)])
    check(growth_hold(q(130), q(100), exact_history, "AAA", 1, "IV", 7), "G equality boundary qualifies")
    check(growth_hold(q("129.75"), q(100), exact_history, "AAA", 1, "IV", 7), "G below closure boundary qualifies")
    check(not growth_hold(q("130.25"), q(100), exact_history, "AAA", 1, "IV", 7), "G above closure boundary fails")
    check(not growth_hold(q(100), q(100), exact_history, "AAA", 1, "IV", 7), "G false when no longer oversized")
    missing_history = exact_history[:7]
    check(not growth_hold(q(130), q(100), missing_history, "AAA", 1, "IV", 7), "G false with only seven observations")
    incomplete_history = [dict(sample) for sample in exact_history]
    incomplete_history[3]["complete"] = False
    check(not growth_hold(q(130), q(100), incomplete_history, "AAA", 1, "IV", 7), "G false with an incomplete observation")
    missing_day_history = [dict(sample) for sample in exact_history]
    missing_day_history[4]["day"] += 1
    check(not growth_hold(q(130), q(100), missing_day_history, "AAA", 1, "IV", 7), "G false across a missing daily sample")
    zero_growth = make_growth_history([q(100)] * 8)
    check(not growth_hold(q(130), q(100), zero_growth, "AAA", 1, "IV", 7), "G false with zero capacity growth")
    falling_capacity = make_growth_history([q(101 - i) for i in range(8)])
    check(not growth_hold(q(130), q(94), falling_capacity, "AAA", 1, "IV", 7), "G false with falling capacity")
    changed_actor = [dict(sample) for sample in exact_history]
    changed_actor[0]["actor"] = "BBB"
    check(not growth_hold(q(130), q(100), changed_actor, "AAA", 1, "IV", 7), "G history resets on succession or actor change")
    changed_grant = [dict(sample) for sample in exact_history]
    changed_grant[0]["grant"] = 2
    check(not growth_hold(q(130), q(100), changed_grant, "AAA", 1, "IV", 7), "G history resets on new grant")
    changed_regime = [dict(sample) for sample in exact_history]
    changed_regime[0]["regime"] = "III"
    check(not growth_hold(q(130), q(100), changed_regime, "AAA", 1, "IV", 7), "G history resets on regime change")
    fresh_after_reset = make_growth_history([q(93 + i) for i in range(8)], grant=2, start_day=20)
    check(not growth_hold(q(130), q(100), fresh_after_reset[:7], "AAA", 2, "IV", 26), "G stays false until eight new-grant observations")
    check(growth_hold(q(130), q(100), fresh_after_reset, "AAA", 2, "IV", 27), "G may resume after a complete new-grant window")
    check(not growth_hold(q(130), q(99), exact_history, "AAA", 1, "IV", 7), "G requires current capacity to match latest observation")
    check(not growth_hold(q(130), q(100), exact_history, "AAA", 1, "IV", 8), "G requires current day to match latest observation")
    print("Eight complete daily observations and seven elapsed days are required under one actor, grant, and regime")
    print("With delta_A=7 and gap=30, 7*gap=30*delta_A=210, so equality qualifies")
    print("Missing, incomplete, nonconsecutive, zero-growth, falling-growth, nonoversized, and reset-history cases return false")

    print("AI relative score and next-review delay arithmetic")
    score_points = [q(0), q("0.5"), q("0.75"), q(1), q("1.5"), q(2), q(3)]
    expected_scores = [
        (40, 20, None),
        (40, 40, None),
        (40, 50, 47.5),
        (40, 60, 60),
        (40, 80, 85),
        (40, 100, 110),
        (40, 100, 110),
    ]
    expected_delays = [10, 7, 6, 5, 4, 4, 3]
    for e, expected, expected_delay in zip(score_points, expected_scores, expected_delays):
        scores = ai_scores(e)
        row = (scores["hold"], scores["single"], scores["batch"])
        check(row == expected, f"AI score row at e={e}")
        delay = ai_delay(e)
        check(delay == expected_delay, f"AI delay at e={e}")
        extra = " formula only, removal unavailable while compliant" if e == 0 else ""
        print(f"e={e}, scores={row}, d_AI={delay}d{extra}")
    check(ai_scores(q(1), veto=True) == {"hold": 40, "single": None, "batch": None}, "hard veto bypasses score pool")
    check(ai_delay(q(4)) == 2, "AI delay lower clamp at e 4")
    check(ai_delay(q(6)) == 2, "AI delay lower clamp at e 6")
    print("T, G, or O veto leaves sticky retain without a removal pool. Scores are relative weights, not probabilities")

    print(f"All {CHECK_COUNT} arithmetic checks passed")


if __name__ == "__main__":
    main()
```
