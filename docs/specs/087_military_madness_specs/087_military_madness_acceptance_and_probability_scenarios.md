# Military Madness: Acceptance and Probability Scenarios

These are design acceptance cases and required future evidence. They are not records of completed engine tests. No HOI4 MCP probability, event, or GUI audit was executed in this chat.

## User requirement coverage

| Requirement | Canonical design location | Required evidence |
|---|---|---|
| Minor Repeatable, Chaos level 1, Military Preparation Low | Part 1 | Catalog and runtime classification agree |
| Every valid country independently affected | Parts 1 and 2 | Complete recipient trace and separate draws |
| Exactly 365 days | Parts 1 and 4 | Days-based activation and expiry evidence |
| 1, 3, 6, and 10 rolls | Parts 1 and 2 | Exact counts at every stage |
| Broad minimums 1, 1, 2, and 3 | Parts 1 and 2 | Quota trace, including duplicates |
| Chaos thresholds 200, 400, and 600 | Part 1 | Boundary and disabled-stage cases |
| No evolution after III | Part 1 | No further stage, registry row, or hidden terminal grant |
| Modifier and magnitude both randomized | Parts 2 and 3 | Complete entry pool and per-entry magnitude trace |
| Standard modifiers remain available | Part 2 | Combined-pool membership at each stage |
| Duplicate categories and same-stat stacking | Parts 2 and 4 | Within-package and cross-package cases |
| No archetypes or national balancing | Parts 1 and 2 | Equal canonical entry weights, no usefulness filters |
| Expanded terrain, weather, mission, and unit coverage | Parts 2 and 3 | Full discovery and disposition report |
| Vanilla, DLC, country, and Chaos Redux support | Part 2 and research notes | Provider coverage, scope, rollback, and safety proof |
| Only technically unusable candidates excluded | Part 2 | Every exclusion has an exact technical basis |
| Old and new packages expire separately | Part 4 | Staggered and same-time expiry cases |

## Probability evidence contract

The runtime candidate pool must be complete for the relevant country and content configuration before a normalized probability is described as exact.

Audit the guaranteed broad draws separately from the remaining union draws. Audit magnitude selection separately from modifier selection. Candidate aliases, duplicate provider exports, and the same entry appearing in several stage definitions must not multiply its weight.

Use the required read-only HOI4 MCP workflow: inspect, evaluate named scenarios, sweep boundaries, and compare the same scenarios across revisions. Simulations are supplementary and must declare seeds and uncertain inputs.

The existing repeat-weight and cluster selection systems are separate from the package lottery. A package's equal internal weights do not imply that Event 087 has an equal chance of being selected from the global event pool.

A score in an AI strategy or willingness system is not a click probability. This design adds no strategic acknowledgement branch.

## Named probability cases

| ID | Case | Acceptance condition |
|---|---|---|
| P01 | Baseline with complete broad pool | One broad entry and one legal independent magnitude |
| P02 | Evolution I | Three rolls, at least one broad |
| P03 | Evolution II | Six rolls, at least two broad |
| P04 | Evolution III | Ten rolls, at least three broad |
| P05 | All free slots also draw broad entries | Accepted without rejection or substitution |
| P06 | Every slot draws the same canonical entry | Accepted, all magnitudes and records retained |
| P07 | Broad entry appears in several source lists | One union entry, no accidental extra weight |
| P08 | Two provider names alias the same effect | Canonical deduplication prevents double weight |
| P09 | Broad and unit-specific effects share a calculation family | Both remain distinct only when their actual scope differs |
| P10 | Two otherwise identical countries have very different armed forces | Same eligible pool and weights when technical capabilities match |
| P11 | Landlocked country with zero ships | Eligible naval effects remain present |
| P12 | Peacetime country with zero deployed forces | Combat entries remain present |
| P13 | Missing optional system | Only entries requiring that actual unavailable capability are absent |
| P14 | Country-origin effect exported nationally | Origin tag alone does not restrict a valid national statistic |
| P15 | Current effect is saturated or strategically useless | No reroll or extra compensation |
| P16 | Minimum and maximum magnitude endpoints | Both endpoints reachable with correct signs and units |
| P17 | Provider has a flat capacity statistic | No percentage conversion without semantic evidence |
| P18 | Boolean-only candidate | Type conflict recorded, no meaningless large numeric magnitude |
| P19 | Empty mandatory broad pool | Occurrence fails validation before distribution |
| P20 | Same game state and synchronized occurrence | Identical peer results without cosmetic RNG influence |
| P21 | Repeated source generation | Stable catalog ordering and identity with matching inputs |
| P22 | Before/after addition of compatible entries | Distribution changes only as documented by the expanded complete pool |
| P23 | Global event-selection integration | Existing weight recovery, caps, and cluster cadence remain separate |
| P24 | Independent-timer multiplayer setting | Each legitimate worldwide occurrence applies once, never once per report |

## Stage and lifecycle cases

| ID | Setup | Expected behavior |
|---|---|---|
| L01 | Chaos 199, 200, 399, 400, 599, 600 | Stages 0, I, I, II, II, III |
| L02 | Chaos 1000 or higher | Still at most Evolution III |
| L03 | Evolution III disabled at 650, Evolution II enabled | New package uses Evolution II |
| L04 | Evolution I disabled, Evolution II enabled at 450 | Evolution II can open directly |
| L05 | All evolutions disabled | Baseline package |
| L06 | Chaos rises after distribution begins | All recipients retain the frozen occurrence stage |
| L07 | Chaos falls while an older high-stage package is active | Old package unchanged, next firing reevaluates current Chaos |
| L08 | Two firings at day 0 and day 100 | Expiries at days 365 and 465 |
| L09 | Two distinct firings on the same day | Two distinct packages with matching expiry timestamps |
| L10 | Same delivery callback repeated | No additional package |
| L11 | Same expiry callback repeated | No additional removal |
| L12 | Open, close, postpone, or repeat a report | No reward, magnitude, or timer change |
| L13 | Save immediately before or after expiry | No redraw, extension, residue, or double cleanup |
| L14 | Event disabled while packages remain | No new random firing, normal cleanup continues |
| L15 | Country changes ideology, leader, or cosmetic tag | Same country lifetime preserves packages |
| L16 | Country becomes a subject or gains independence | Packages preserved |
| L17 | Valid country remains in exile | Timer continues, compatible effects remain national |
| L18 | Annexation and later release of the same tag | No inheritance or resurrection of the old lifetime's package |
| L19 | Civil war copies national ideas | Event-owned records and effects are not duplicated to the new country |
| L20 | New country appears after distribution | Receives no retroactive package |
| L21 | Country vanishes before queued delivery | No award to an invalid recipient |
| L22 | Catalog entry reorders after update | Saved identity keeps its original meaning |
| L23 | An old binding disappears | Explicit supported migration or disclosed unsupported save transition |
| L24 | Old nine-month entrenchment idea exists | No invented random package or guessed renewed duration |

## Safety and composition cases

| ID | Case | Required result |
|---|---|---|
| S01 | Two additive positive modifiers affect one statistic | Raw sum is correct, no accidental multiplication |
| S02 | Two reductions exceed the valid technical range | Raw records retained, applied result remains valid |
| S03 | One saturated reduction expires | Rebuild from surviving raw contributions |
| S04 | External reduction appears after the package | Supported composition remains within its certified domain |
| S05 | External reduction disappears | Event contribution stays beneficial and correctly recomputed |
| S06 | Dynamic modifiers evaluate in a different order | No circular drift, sign reversal, or stale self-subtraction |
| S07 | Save/load changes carrier application order | Same valid result as before saving |
| S08 | High positive stacking approaches numeric limits | Explicit technical bound, no overflow and no silent data loss |
| S09 | Percentage-points statistic | Display and engine unit agree |
| S10 | Penalty reduction | Reduces the penalty without inventing an unrelated universal bonus |
| S11 | Organization capacity changes | Verified native current-value behavior, no repeated healing exploit |
| S12 | Recruitment capacity falls at expiry | Native over-cap handling, no event-owned deletion |
| S13 | Experience gain bonus expires | Earned experience remains |
| S14 | Active country has many overlapping ten-roll packages | All records survive and remain inspectable |
| S15 | Unknown provider lacks a value type or safe bound | Binding remains visibly unverified, not assigned a generic percentage |
| S16 | Engine-valid but currently ineffective modifier | Remains an eligible unhelpful result |

## Interface, integrity, and achievement cases

| ID | Case | Acceptance condition |
|---|---|---|
| U01 | One baseline roll | Exact magnitude and expiry readable |
| U02 | Ten rolls with long labels and duplicates | All rows reachable, no clipping or missing pages |
| U03 | Numerous overlapping packages | Expiry-ordered navigation, no backend truncation |
| U04 | Next expiry removes only some contributions | UI matches surviving effects |
| U05 | Saturated statistic | Raw request and applied amount clearly distinguished |
| U06 | Last package expires with ledger open | Active view refreshes and does not retain a false bonus |
| U07 | Foreign country selected | No unauthorized access to another country's private ledger |
| U08 | Supported resolutions, UI scales, hover and selected states | Mandatory matching MCP renders and click-region inspection |
| U09 | Shared Event Details | Premise and progression only, no result dump |
| U10 | Worldwide natural occurrence | One history record and one Chaos impulse |
| U11 | Cluster delivery | No duplicate member firing or double Chaos accounting |
| U12 | Force or debug path | No farmable Chaos or achievement progress |
| U13 | A1 capital moved after opening | Frozen target remains authoritative |
| U14 | A1 ally captures the capital | Does not satisfy recipient direct hostile seizure |
| U15 | A2 states ceded, released, or de-cored | Frozen recovery requirement is not reduced |
| U16 | A2 loses a required state during the hold | Hold restarts within the original deadline |
| U17 | A3 another package arrives during the unassisted hold | Attempt interrupted, reward is still applied normally |
| U18 | A3 diplomatic transfer substitutes for conquest | Does not create qualifying gains |
| U19 | Achievement earned during an invalid country lifetime | Rejected |
| U20 | Four reports, spirit, and three achievement triplets | Fourteen exact runtime textures with complete source-to-consumer evidence |

## Performance and evidence limits

Test logical scale with a large supported country roster, the complete generated pool, repeated same-day occurrences, and numerous active packages. A finite stress fixture is evidence of that tested load, not permission for a hidden gameplay cap.

Distribution may visit all recipients once when the event fires. Expiry, country cleanup, UI refresh, and achievement observations must be bounded to the relevant active records. This package grants no permission for a new recurring whole-world scan.

Runtime acceptance requires the installed game's documentation, real modifier bindings, complete source traces, the required MCP outputs, and the user's eventual live-game evidence. Static document checks cannot certify these surfaces.
