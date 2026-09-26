# IW-040/KUB founding-route source arithmetic

**Disposition:** implemented as a source-level route witness; AI selection, resource availability, and engine deadline behavior remain unresolved.

## Purpose and method

This parent-owned audit checks whether the accepted KUB focus and government systems contain at least one deterministic source path to the founding mission's two 60-point ledger thresholds before its 600-day timeout. It calculates each of the eight KUB group branch/government combinations from current constants and scripted effects. This is arithmetic over source; it is not a runtime, AI-probability, or campaign-scenario test.

## Sources

- KUB ledger starting values and bounds: `common/script_constants/006_independence_wave_constants_registry.txt:6335-6352`.
- Existing five-unit focuses: `common/national_focus/006_independence_wave_focus.txt:138-160` for capital administration, `:193-240` for inventory, and `:244-285` for first oath. All three require only the full framework after their displayed prerequisite, and inventory/oath are separate sibling nodes without mutual exclusion.
- KUB callback deltas: `common/scripted_effects/006_independence_wave_kuban_package_effects.txt:328-359`.
- KUB group deltas and gates: `common/national_focus/006_independence_wave_focus.txt:5038-5198` and `common/scripted_triggers/006_independence_wave_kuban_package_triggers.txt:45-52`.
- Government-route ledger deltas: `common/scripted_effects/006_independence_wave_kuban_package_effects.txt:224-321`.
- Government-choice availability and decision timers: `common/scripted_triggers/006_independence_wave_kuban_package_triggers.txt:27-43` and `common/decisions/006_independence_wave_frontier_decisions.txt:930-1110`.
- Founding mission condition and timeout: `common/decisions/006_independence_wave_frontier_decisions.txt:619-660`; `founding_crisis = 600` is in the KUB duration constant block.

## Constructive pre-resolution sequence

Starting values are Civic Concord 34 and Mounted Readiness 41. The existing capital-administration focus invokes the guarded KUB provisional-assembly callback for +15 Civic Concord and +5 Mounted Readiness. Inventory the State invokes the guarded community callback for +15/+10. Bind the First Oath invokes the guarded border-guard callback for +5/+15. These existing direct focuses require the full framework and do not mutually exclude each other.

After these three focuses, the ledgers are 69/71. The KUB group root and register step add +5 Civic Concord and +5 Mounted Readiness, reaching 74/76. Its hearing branch then yields 84/71; its mounted-service branch yields 69/86. The matching docket cannot be used yet because the two paid companion projects remain behind successful founding resolution; the docket is not needed for founding stability.

The government route effect deltas applied at successful decision expiry are constitutional +15/+5, agrarian +15/+10, socialist +5/+15, and emergency -5/+20. Applying each to each branch gives:

| KUB branch | Constitutional | Agrarian | Socialist | Emergency |
| --- | --- | --- | --- | --- |
| Petition hearing, 84/71 before government | 99/76 | 99/81 | 89/86 | 79/91 |
| Mounted service roll, 69/86 before government | 84/91 | 84/96 | 74/100 | 64/100 |

All eight arithmetic results meet the 60/60 requirement after the government choice. Values use the existing 0-100 clamp; the two 100 results are capped.

The sequential focus path takes 32 units: the capital focus, inventory, and first-oath focuses use 5 each, and the KUB root/register/selected-branch path uses 5/5/7. At seven nominal days per unit, that is 224 days. The four government projects last 75, 180, 75, and 120 days; if the selected project is started after the focus path, the longest combined sequence is 224 + 180 = 404 days, below the 600-day mission timeout. The mission stays active and unresolved until a government is installed, so the separate government-choice gate remains open during that sequence.

## Preconditions and limits

This route witness assumes the exact IW-040 setup and full Event 006 focus framework are active, state 234 remains owned and controlled as the capital, and the selected government's existing cost trigger is satisfied. The costs remain substantial: light administration requires command power, manpower, and a civilian factory reservation; agrarian government requires the diplomatic-standard convoy/train payment; emergency government requires 10,000 manpower, 35 Army XP, 1,000 infantry equipment, and 200 support equipment. No initial-stockpile or resource-acquisition fixture was available here, so affordability of every government route is not proven.

This calculation does not show that KUB's AI selects the focus branch and matching government, avoids a late government choice, or keeps state/capital control. The probability auditor's typed fixture could not bind route, decision, mission, ledger, and resource state; the 15-scenario probe in `006_event6_iw040_kuban_decision_ai_probability_audit_2026-09-26.md` is explicitly invalid fixture evidence. No numeric weights changed, and no engine or live session test was performed. Imported shared-focus layout remains blocked as MCP evidence under the user's selected design.
