# Probability and validation matrix

## Evidence classes

No HOI4 MCP audit or live game was run here. The accompanying Python model checks proposed mathematical and bookkeeping invariants with arbitrary-precision Python arithmetic. It does not inspect Clausewitz, simulate the native event dispatcher, validate installed effects, or prove native floating-point precision.

The future probability auditor must inspect the actual source first through `hoi4.probability_inspect`. It must use the appropriate evaluate, sweep, simulate, compare, sequence, and render routes only when supported by the exposed schema and the question. Complete pools and current scenario state are required for normalization. A score is not a probability, and a source-only calculation cannot replace an unavailable native analysis route.

## Weighted surfaces

| Surface | Required scenarios | Acceptance |
| --- | --- | --- |
| Country selection | AI major, human minor, human major, multiple humans on one country, subject, capitulated live tag, empty carrier | Eligible union deduplicated, uniform country draw, no excluded shell |
| First extra category | 199/200, 399/400, 599/600, 799/800 Chaos, every evolution enable mask | Exact threshold and independent-toggle behavior |
| Family normalization | All families present, only reserves, no valid characters, no population, no compatible national values | Missing families removed, no dummy outcomes or concealed probability assumption |
| Human subpool | Population and all rosters, population only, rosters only, one-person roster, multi-role unique person | Correct conditional weights, no DLC list flooding or double identity |
| IV count and repeated draws | Desired two/three/four, one available category, aliases, intersecting rosters, population/manpower conflict | Without replacement, no quarter-loss, actual reduced count reported |
| Whole-count rounding | Zero, one, odd/even small quantities, many odd rows | Unbiased intended rule, fixed committed draw, no last-object immunity |
| Response AI | War/peace, low PP/CP, no spare factory, no useful recipient, active program, funded/local household options | Only legal useful choices, opportunity costs reflected, no hidden subsidy |
| Shared repeat selection | Actual timer, recovery, cap halving, cluster dispatch and duplicate callback | Existing shared behavior preserved, no invented second cadence |

The simple full-pool first-extra population reference probability is 7.5% at III under the proposed weights. If only population remains in the people subfamily, its conditional share changes. If other families are absent, it changes again. These cases must be audited explicitly rather than presenting the 7.5% reference as a universal chance.

## Required implementation checks

| Test family | Required evidence |
| --- | --- |
| Equipment | Native before/after inventory across domestic, captured, obsolete, DLC, mod, variant/origin rows and issued units |
| Stock ownership | Lend-lease stages, production completion, fielded assignment, free convoy/train aliases, native reservations |
| National values | Positive, zero, negative, capped, fractional, and native precision cases |
| Research | Mixed active projects, no active progress, completed research untouched, special-project independence |
| Population | Many states, odd counts, zero states, large `_k` totals, non-cores, owner/controller split, no Deaths increment |
| Population/manpower | Native side effects measured, no two half-debits, active-force personnel preserved |
| Cohorts | Same person counted physically and in a reception/displacement ledger only once |
| Characters | Assigned/unassigned, current role classification, multi-role identity, unavailable/future person, secret operative |
| Unique owners | Wu/ Kruger present or absent, current continuity form, projects and succession, no death/terminal shortcut |
| Receipts | Duplicate root, duplicate report, duplicate owner callback, same incident after replenishment, genuinely new incident |
| Save and multiplayer | Target, categories, odd draws, identities, claims, response dates, owner state survive authoritative save/load and multiplayer replay |
| Recovery | Exact quote/payment, program start/end/cancel, occupied-factory release, no re-trigger reward, annexation/continuation |
| Connections | Matching Abundance success versus failed card, Devil deficit cap, consumed restoration identity, no generic event replay |
| Achievements | All positives plus near-miss, test-mode, tag-switch, restored-person, missing-proof and expiry negatives |
| Presentation | Actual consumer renders, public/secret labels, correct actor, no extra evolution rows, one cinematic slot with no collision |
| Localization/assets | All dynamic keys, native formatting, complete DDS triplets, actual licenses and sources, no speculative final quotation |

## Stop conditions

A missing named category, unproved equipment family, unsafe character removal, duplicated population, lost receipt, or incorrect enabled-state gate blocks a full completion claim. Tool unavailability must be reported as such. Do not bypass it by replacing the intended event with a simpler behavior or by attaching a Python success report to an untested native implementation.
