# Event 012 Gods doctrine consequences, 2026-09-26

Disposition: **implemented** for the authorized doctrine consequence matrix. The full Gods of Africa goal remains active; this handoff does not claim whole-feature completion.

## Acceptance basis

The active user goal explicitly requires the Event 012 overlay doctrines to reshape demands, protection, retaliation, and settlement. The goal authorizes those four gameplay surfaces; the exact amounts and thresholds below are the parent's concrete tuning within that scope. The existing doctrine identifiers, protection payment, bounded participant registry, and punishment safety gates remain in use.

## Implemented effects

| Doctrine | Source behavior |
| --- | --- |
| Reciprocal Covenant | Demand amounts use the existing 90% scale. Protection cooldown is 30 days shorter and lowers Wrath by 4. Punishment intent drops by one tier, with Pressure as the floor. Favored standing needs two fulfilled demands or one recorded support action. |
| Sovereign Exaction | Demand amounts use the existing 120% scale. Protection lowers Wrath by 1. A host-marked offender raises punishment intent by one tier when it is below Ultimatum; the first-failure ceiling and host Strength ceiling still apply, and catastrophe still requires the existing extreme gate. Favored standing needs four fulfilled demands or two recorded support actions. |
| Strategic Ambiguity | Frozen demand deadlines gain 30 days without changing quoted amounts. Enemy intelligence rises from 5 to 10 in each shared category behind the La Résistance, Security capability, both-agency, active-war, and eligible-enemy gates. Direct stability and war-support losses are halved; a host-marked offender also receives the existing sanctions memory. Respected standing tolerates up to two failures and two refusals, subject to the existing offender, treaty, Wrath, and defiance exclusions. |

The hidden support history is the existing `gods_of_africa_aid_count`; it records participant voluntary aid and host leniency or protection actions. No additional public value, protection cost type, random pool, or AI weight was introduced.

## Files changed

- `common/script_constants/012_africa_gods_constants.txt` centralizes doctrine tuning and alternate Strategic Ambiguity punishment losses.
- `common/scripted_effects/012_africa_gods_effects.txt` applies doctrine behavior to frozen deadlines, punishment intent, protected intelligence, protection cooldown, and Wrath relief.
- `common/scripted_triggers/012_africa_gods_triggers.txt` applies doctrine-specific hidden settlement thresholds.
- `common/scripted_localisation/012_africa_gods_scripted_localisation.txt` selects the current protection-intelligence amount from the host doctrine for reports and focus text.
- `localisation/english/012_africa_gods_l_english.yml` explains the doctrine effects in decision, focus, protection, and report text.
- `docs/specs/012_africa_specs/specs/012_africa_spec_part_3_focus_tree_architecture.md` records the accepted consequence matrix and tuning basis.
- `docs/events/012_africa/gods_of_africa.md` describes the current behavior and limits.

## Evidence and limits

`hoi4.focus_inspect` returned `FOCUS_INSPECTED` with validation passed, no blockers, and 20 nonblocking diagnostics for `africa_continental_focus_tree` in workspace `mod_chaos_redux_ea3b2d67c2c0`; its artifact is `focus-inspect.6a69f0d0e1099f4f.json`. The focus source itself was not changed.

`hoi4.event_inspect` returned `EVENT_INSPECTED_PARTIAL` for `.605` and `.608`; each query used focused analysis, returned one diagnostic and no top-level blocker, and deferred workspace-wide helper and lifecycle projections. `hoi4.event_render` returned `EVENT_RENDERED_PARTIAL` for `.605`, with the same focused-analysis limitation. These results confirm the report surfaces but do not validate the scripted-effect helpers or runtime outcomes.

The accepted `.611`–`.613` response art and `.614` protection art mappings resolve to the existing response and protection sprites. Both DDS files have valid DDS headers and the expected 210×176 dimensions. This confirms wiring and dimensions only; image-content, game-scale, and live playback approval remain open.

The edited English localisation retained UTF-8 BOM encoding and had no duplicate keys. Protection text uses the host's selected doctrine to report the active interval, Wrath relief, and intelligence amount; Strategic Ambiguity reports 10 points, while the other doctrines report the 5-point base. The doctrine tranche did not edit the authoritative workbook or its CSV exports; the Event 070 row remains unassigned in the already updated workbook.

The `.610` success report, the protection effect tooltip, and the Security focus description all resolve the current 5/10 intelligence amount through `GetGodsOfAfricaProtectionIntelAmount`. The `.610` cooldown effect text now includes both the Reciprocal Covenant and Continental Reserve reductions.

## Parent follow-up to completion-audit findings

The completion auditor's initial source crosswalk found stale protection feedback before commit `e2a14dfc7`. That commit resolves the report amount and cooldown findings: `.610` uses the doctrine-aware scripted localization, the effect and Security focus descriptions report the active 5/10 intelligence amount, and the cooldown text includes both reductions. This closes the text mismatch at source; it does not prove the custom localization renders correctly in the live game.

No AI score or probability source changed in this tranche. The named-scenario probability evidence and same-scenario comparison remain under audit because the existing adapter reports incomplete candidate pools. The Event 012 focused event inspection remains partial, runtime and live-save behavior remains unverified by the agent, and broader Part 8 route promises remain unresolved outside the accepted overlay scope.
