# Event 085 — Ten Plagues of Egypt

**Major · Chaos level 3 · Natural Disasters / Severe only · root `chaosx.nr85.1`**

This package is the rework design for Event 085.
The legacy implementation is `events/085_xp.txt`, and the event catalog row still describes the old XP event; the rework is not implemented.
Implementation working evidence belongs under `docs/plans/085_ten_plagues_of_egypt_plans/`.

## Authority

| Source | Status |
| --- | --- |
| [Original brief](085_ten_plagues_of_egypt_original_brief.md) | Explicit user decisions, preserved verbatim. Its closing task paragraph was the planning instruction, not an implementation instruction |
| Manual scenario identity `SCN-032` / raw `32` | Reserved by the user's 7 October 2026 allocation instruction in the [shared identifier registry](../shared_identifier_registry.md); identity only |
| Boils care calendar and Doctor Wu link (Part 5, A23) | Accepted by the parent in the 8 October 2026 planning improvement pass |
| Design changes listed in the revision log | Accepted under the 10 October 2026 spec audit, within the user's planning-package brief |
| Other numeric tuning (calendar, mortality budgets, hazard formula, mourning bands, Chaos map, achievement thresholds) | Proposed design that fills gaps in the brief; tune during implementation and record acceptance in the plans folder |
| [Open questions](#open-questions) | Unresolved |

## Reading order

| Part | Document |
| --- | --- |
| 01 | [The Global Crisis](085_ten_plagues_of_egypt_spec_part_01_the_global_crisis.md) |
| 02 | [Divine Wrath and Government Choices](085_ten_plagues_of_egypt_spec_part_02_divine_wrath_and_government_choices.md) |
| 03 | [Water into Blood and Frogs](085_ten_plagues_of_egypt_spec_part_03_blood_and_frogs.md) |
| 04 | [Lice, Gnats, and Flies](085_ten_plagues_of_egypt_spec_part_04_lice_gnats_and_flies.md) |
| 05 | [Pestilence of Livestock and Boils](085_ten_plagues_of_egypt_spec_part_05_livestock_and_boils.md) |
| 06 | [Hail and Fire, Then Locusts](085_ten_plagues_of_egypt_spec_part_06_hail_fire_and_locusts.md) |
| 07 | [Darkness and the Final Preparation](085_ten_plagues_of_egypt_spec_part_07_darkness_and_passover.md) |
| 08 | [Death of the Firstborn](085_ten_plagues_of_egypt_spec_part_08_the_tenth_plague_and_population.md) |
| 09 | [Evolutions and the Plagues Without End](085_ten_plagues_of_egypt_spec_part_09_evolutions_and_the_plagues_without_end.md) |
| 10 | [The Exodus and International Relief](085_ten_plagues_of_egypt_spec_part_10_the_exodus_and_international_relief.md) |
| 11 | [Mourning and Reconstruction](085_ten_plagues_of_egypt_spec_part_11_mourning_and_reconstruction.md) |
| 12 | [Triggerable Scenario: The Ten Plagues (SCN-032)](085_ten_plagues_of_egypt_spec_part_12_the_triggerable_scenario.md) |
| 13 | [Shared Systems and the Chaos Impact Map](085_ten_plagues_of_egypt_spec_part_13_shared_systems_and_chaos.md) |
| 14 | [Decisions, Costs, and Urgent Objectives](085_ten_plagues_of_egypt_spec_part_14_decisions_and_missions.md) |
| 15 | [AI, Balance, and Acceptance](085_ten_plagues_of_egypt_spec_part_15_ai_balance_and_acceptance.md) |
| 16 | [Visual Presentation and Assets](085_ten_plagues_of_egypt_spec_part_16_visual_presentation_and_assets.md) |
| 17 | [Super-Event Milestones](085_ten_plagues_of_egypt_spec_part_17_super_event_directions.md) |
| 18 | [Achievements](085_ten_plagues_of_egypt_spec_part_18_achievements.md) |

[Narrative source notes](085_ten_plagues_of_egypt_narrative_source_notes.md) separate the Exodus source material from the game's worldwide adaptation.

## Prompts

| Assignment | File |
| --- | --- |
| Complete implementation | [Coding prompt](085_ten_plagues_of_egypt_coding_prompt.md) |
| Compact goal | [Goal prompt](085_ten_plagues_of_egypt_goal_prompt.md) |
| Decisions and missions | [Decision and mission prompt](085_ten_plagues_of_egypt_decision_mission_prompt.md) |
| Visual assets | [Asset prompt](085_ten_plagues_of_egypt_asset_prompt.md) |
| Super-event text, audio and pictures | [Super-event prompt](085_ten_plagues_of_egypt_super_event_prompt.md) |
| Achievements and icon triplets | [Achievement prompt](085_ten_plagues_of_egypt_achievement_prompt.md) |

## Canonical homes

Each rule lives in one part; other parts link to it.

| Rule | Home |
| --- | --- |
| Calendar, participation, fire-once and cluster pacing | Part 1 |
| Divine Wrath values, conduct table, severity multiplier | Part 2 |
| Passover status and coverage | Part 7 |
| Firstborn share and tenth-plague formula | Part 8 |
| Global Wrath, recurrence and world-end gates | Part 9 |
| Owner boundaries (Deaths, Famine, Migration, disease, Natural Disasters) and the Chaos impact map | Part 13 |
| Category budget, cost model, action families, credit limits | Part 14 |
| Mortality budgets, modifier ceilings, AI anchors, acceptance cases | Part 15 |
| Asset inventory | Part 16 |

## Implementation gates

These are required contracts that the implementation must find or build with the owning system; none may be replaced with a flat national effect.

- A non-weapon outbreak entry with the biological outbreak owner for the disease consequences of Lice, Flies and Boils (Part 13).
- A composite Hail and Fire call through `call_natural_disaster` that shares one mortality budget (Part 6).
- A global Darkness presentation that is not ordinary night (Part 7).

The fifty acceptance cases in Part 15 are future checks, not executed tests.
The asset inventory in Part 16 is a production target; no art exists.

## Open questions

These proposals touch an explicit user decision or need the user's choice; they are not applied.

1. **Bounded renewal without world-end branches (Part 9).**
The brief separates Evolution III recurrence from the world-end branch but does not say what Evolution III does when world-end branches are disabled.
Proposal: Evolution III may authorize exactly one renewed sequence when global Wrath is extreme, and never unlimited cycles.
2. **Boils without a disease adapter (Part 5).**
The brief requires Boils to use the existing disease infrastructure.
If the biological outbreak owner cannot accept a non-weapon syndrome, a narrower alternative is a Boils-owned state mortality pulse through the exact population helper with its own Deaths reason.
That alternative would override the brief's instruction, so it needs the user's approval before use.

## Revision log

### 2026-10-10 spec audit

Basis: 10 Oct 2026 spec audit under the user's planning-package brief.

- Replaced per-person firstborn cohorts and Passover coverage records with state-level records, a Passover status and a remaining firstborn share per state (Parts 7, 8, 10, 15, 18).
  This removes the Migration metadata extension that blocked implementation and keeps the no-regeneration and protection rules; a 10% population-growth rule stops last-hour transfers into prepared states.
- Replaced the unsupported local working-capacity reservation and returnable vehicles with a timed local output penalty and consumed equipment, and consolidated sixteen action families into fourteen (Part 14).
  Storm evacuation is Migration's existing action, emergency Passover is a Passover variant, Military Stand-Down is a national attack-for-recovery trade, and Flies has one objective instead of two.
- Earlier work now pays off concretely: completed water, frog, infestation and care work halves later costs in the same state, and broken services make Passover only partial (Parts 4, 5, 7, 14).
- Simplified the Wrath conduct table, tied violent suppression to recorded Condemnation incidents, simplified global-Wrath succession to population-weighted averaging, and gave the mourning directions concrete effects (Parts 2, 9, 11).
- Foreign relief now pays the material cost of a recipient's active objective, and Exodus pressure is a Migration incident request from collapsed high-Wrath states (Part 10).
- Aligned owner contracts with current systems: Famine's food-shock adapter, Migration's named actions, the biological outbreak owner, and a world-threat source for the endless branch (Parts 9, 10, 13).
- Added concrete AI weight anchors and representative balance cases (Part 15), and restated achievement trackers for the state-level records (Part 18); the asset inventory falls to 91 outputs with fourteen decision icons (Part 16).
- Removed duplication and stale process content: the achievement prompt no longer copies Part 18, and the prompts drop the absent companion report, `.agents` paths and runtime-specific spawning syntax.
  Completion rules now match the repository policy for unavailable tools and specialists.
- Deleted `package_manifest.json`, a hash inventory with no remaining consumer.
