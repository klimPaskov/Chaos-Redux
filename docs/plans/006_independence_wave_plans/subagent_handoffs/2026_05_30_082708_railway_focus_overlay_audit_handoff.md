# Event 006 Railway Focus Overlay Audit Handoff

Timestamp: 2026-05-30 08:27:08 UTC

## Scope

Audited only the Event 006 Independence Wave railway package focus overlay in `common/national_focus/006_independence_wave_focus.txt`, plus direct decision, scripted effect, scripted trigger, localisation, docs, and vanilla icon references needed to verify the two new focus blocks.

No flags or flag assets were touched. No Event 005 files were edited.

## Files Changed

- `common/national_focus/006_independence_wave_focus.txt`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/2026_05_30_082708_railway_focus_overlay_audit_handoff.md`

Inspected but not edited:

- `common/decisions/006_independence_wave_decisions.txt`
- `common/scripted_effects/006_independence_wave_effects.txt`
- `common/scripted_triggers/006_independence_wave_triggers.txt`
- `localisation/english/006_independence_wave_l_english.yml`
- `docs/events/006_independence_wave.md`
- vanilla `interface/goals.gfx`
- vanilla `interface/goals_shine.gfx`

## Changed Focus IDs

| Focus id | Change |
| --- | --- |
| `independence_wave_junction_committee_manifest` | Added bypass when `independence_wave_junction_committee_assembled` is already set, and corrected AI modifier from nonexistent country flag `independence_wave_focus_industry_support` to existing flag `independence_wave_focus_repaired_rail_yard`. |
| `independence_wave_bridge_guard_mandate` | Added bypass when `independence_wave_bridge_guard_secured` is already set. |

## Route Coverage Table

| Route surface | Implemented behavior | Audit result |
| --- | --- | --- |
| Railway package gate | Both focuses require `is_independence_wave_railway_package = yes` in `available`. | Present. Non-railway releases see the nodes as unavailable rather than hidden, matching the nearby package-overlay pattern in this file. |
| Prerequisite chain | `junction_committee_manifest` requires `repair_the_rail_yard`; `bridge_guard_mandate` requires `junction_committee_manifest`. | Present. Shape is a linear AND-safe chain with one prerequisite per focus. |
| Decision proof continuity | First focus runs `independence_wave_assemble_junction_committee_effect`, second focus runs `independence_wave_secure_bridge_guard_effect`. | Present. Added bypasses so prior decision completion does not duplicate the same proof reward. |
| Decision unlock messaging | First focus shows `unlock_decision_tooltip = independence_wave_secure_bridge_guard`; second shows `unlock_decision_tooltip = independence_wave_proclaim_timetable_authority`. | Present. Decisions exist in `common/decisions/006_independence_wave_decisions.txt`. |
| Event 005 separation | New focus blocks use Event 006 ids/effects and vanilla icons only. | Passed scoped scan for `005`, `PRA`, `soviet`, `Soviet`, and `GFX_focus_PRA` inside the two focus blocks. |

## Missing Or Simplified Content

- No missing content found inside this narrow overlay slice.
- The railway overlay is still a compact two-focus proof chain, not a full railway route family. This is already documented as future work in `docs/events/006_independence_wave.md` and was outside this audit scope.
- The route gate uses `available` rather than `allow_branch`, so non-railway countries can see unavailable package nodes. This matches adjacent Event 006 package-overlay focuses and was not changed.

## Icon Coverage Table

| Focus id | Icon id | Source check | Result |
| --- | --- | --- | --- |
| `independence_wave_junction_committee_manifest` | `GFX_focus_generic_railroad` | Vanilla `interface/goals.gfx:3868`; shine in `interface/goals_shine.gfx:26272`. | Valid vanilla icon, no Event 005 asset dependency. |
| `independence_wave_bridge_guard_mandate` | `GFX_goal_generic_construct_infrastructure` | Vanilla `interface/goals.gfx:506`; shine in `interface/goals_shine.gfx:4906`. | Valid vanilla icon, no Event 005 asset dependency. |

## Localisation And Reward Mismatch List

| Surface | Finding |
| --- | --- |
| Focus names/descs | `independence_wave_junction_committee_manifest`, `_desc`, `independence_wave_bridge_guard_mandate`, and `_desc` exist in `localisation/english/006_independence_wave_l_english.yml:100-103`. |
| Reward text fit | Focus descriptions match the rewards: the first assembles a junction committee and opens bridge-guard work; the second secures bridge guards and opens Timetable Authority proclamation. |
| Decision loc | `independence_wave_secure_bridge_guard` and `independence_wave_proclaim_timetable_authority` localisation exists in `localisation/english/006_independence_wave_l_english.yml:179-183`. |
| Localisation encoding | File begins with BOM bytes `efbbbf`. No `:0` keys found in the scoped scan. |

## AI Behavior Gaps

- Fixed a local AI bug in `independence_wave_junction_committee_manifest`: the weight checked `has_country_flag = independence_wave_focus_industry_support`, but `independence_wave_focus_industry_support` is a scripted effect, not a flag. It now checks the flag set by the prerequisite focus: `independence_wave_focus_repaired_rail_yard`.
- No broader AI strategy changes were made. Full route-aware AI strategy for future railway route families remains outside this narrow overlay audit.

## High-Priority Fixes Applied

1. Added proof-state bypasses to avoid duplicate rewards when the corresponding Formation Ledger decision already set the proof flag before the focus was completed.
2. Corrected the local AI flag reference in `independence_wave_junction_committee_manifest`.

## Route Behavior Before And After

Before:

- Railway releases could complete `independence_wave_junction_committee_manifest` or `independence_wave_bridge_guard_mandate` even if the matching decision had already set `independence_wave_junction_committee_assembled` or `independence_wave_bridge_guard_secured`, duplicating variable, equipment, command power, and construction rewards.
- `independence_wave_junction_committee_manifest` had an AI modifier that checked a scripted effect name as a country flag, so that modifier could not work as intended.

After:

- `independence_wave_junction_committee_manifest` bypasses if `independence_wave_junction_committee_assembled` already exists.
- `independence_wave_bridge_guard_mandate` bypasses if `independence_wave_bridge_guard_secured` already exists.
- The junction committee AI modifier now keys off `independence_wave_focus_repaired_rail_yard`, the flag set by the prerequisite focus.

## Localisation Keys And Icon IDs Changed

- Localisation keys changed: none.
- Icon IDs changed: none.

## Validation Run

- Required offline Paradox wiki pages consulted before inspecting Chaos files: Data structures, Triggers, Effect, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, and National focus modding.
- Vanilla references consulted: `documentation/effects_documentation.md`, `documentation/triggers_documentation.md`, `documentation/modifiers_documentation.md`, `documentation/script_concept_documentation.md`, `common/decisions/_documentation.md`, vanilla focus examples, vanilla decision examples, vanilla focus icon `.gfx` files.
- Brace balance on `common/national_focus/006_independence_wave_focus.txt`: `open=418 close=418 delta=0`.
- Unsupported operator scan on `common/national_focus/006_independence_wave_focus.txt`: no `<=` or `>=` matches.
- Localisation `:0` scan on `localisation/english/006_independence_wave_l_english.yml`: no matches.
- Localisation BOM check on `localisation/english/006_independence_wave_l_english.yml`: `efbbbf`.
- New focus-block Event 005/PRA scan: no `005`, `PRA`, `soviet`, `Soviet`, or `GFX_focus_PRA` matches inside the two focus blocks.
- Icon reference check: both focus icons and shine sprites found in vanilla `goals.gfx` and `goals_shine.gfx`.
- Decision and effect reference check: `independence_wave_secure_bridge_guard`, `independence_wave_proclaim_timetable_authority`, `independence_wave_assemble_junction_committee_effect`, and `independence_wave_secure_bridge_guard_effect` exist in Event 006 files.

## Skipped Validation

- Did not run a full HOI4 game load or live focus-tree UI test. This environment does not provide an in-game validation harness.
- Did not audit or patch the broader Event 006 focus tree, railway package route design, Event 006 decision category balance, assets, flags, scripted GUI, or Event 005 separation beyond the two new focus blocks and direct references named in the prompt.

## Remaining Route Risks

- The railway package overlay is intentionally still shallow: two focuses and existing Formation Ledger decisions. It does not yet provide a full railway country route family.
- The overlay uses `available` route gates rather than `allow_branch`; this is consistent with adjacent package overlays but means unavailable railway nodes can appear to non-railway Event 006 releases.
- Some existing nearby package-overlay indentation and broader focus-tree structure are uneven, but this audit did not perform unrelated formatting cleanup.

## Plan Handoff

No broader improvement plan was written. The remaining route-depth work is already outside this narrow package-overlay slice and should be handled by the parent Event 006 implementation plan if accepted.
