# Holy Realm Buddhahood Focus Tree Audit And Patch Handoff

## Patch Summary

Changed files:

- `common/national_focus/003_holy_realm.txt`
- `docs/plans/003_holy_realm_buddhahood_plans/holy_realm_focus_tree_completion_plan.md`
- `docs/plans/003_holy_realm_buddhahood_plans/subagent_handoffs/2026-06-11_focus_tree_audit_patch.md`

Changed focus ids:

- No focus id behavior was directly changed.
- `THR_focus` tree-level filter priority placement was fixed.

Route behavior before and after:

- Before: `search_filter_prios` was inside `focus_tree = { ... }` at `common/national_focus/003_holy_realm.txt:33`, despite the offline National focus wiki and vanilla `generic.txt` showing this block as root-level.
- After: `search_filter_prios` is root-level at `common/national_focus/003_holy_realm.txt:20`, before `focus_tree = { ... }`. This only fixes filter priority parsing/placement and does not redesign routes.

Localisation keys and icon ids changed:

- None.

## Route Coverage Table

| Required route | Implemented route or focus branch | Status | Notes |
| --- | --- | --- | --- |
| Opening survival trunk | `THR_mountain_refuge`, `THR_shelter_border_villages`, `THR_guard_high_passes`, `THR_bodhisattva_accepts_seal` | Partial | Survival exists, but the spec's named opening anchors like `Open the Mandala Chamber`, `The Bodhisattva's Vow`, `World Sends Questions`, and survey setup are merged into older route nodes. |
| Teaching mission path | `THR_convene_mountain_assembly` unlocks teaching decisions; `THR_hold_dharma_teaching` exists in decisions | Shallow/decision-only | Spec requires a visible teaching focus path with mission-slot, foreign teaching, crisis teaching, and `Many Lamps, One Flame` gates. Current tree has no dedicated teaching branch. |
| Meditation and Dhyana path | Concentration decisions exist: `THR_begin_concentration_sequence`, `THR_hold_intention`, `THR_hold_energy`, `THR_hold_mind`, `THR_hold_investigation` | Missing as focus route | The decision fallback exists, but no focus branch represents First-Fourth Dhyana, meditation charge cap, or `The Unshaken Seat` preparation path. |
| Governance route family | `THR_rewrite_civil_register`, `THR_mandala_bureau`, `THR_arhat_examinations`, `THR_arhats_take_office` | Not matching spec | Current route is Arhat bureaucracy, not the required Council of Abbots / Protector Regent / Pilgrim Assembly family with identity and route tradeoffs. |
| Industry and sanctuary logistics | `THR_refuge_foundries`, `THR_count_mountain_roads`, `THR_monastic_labor_vows`, `THR_shelters_under_stone` | Partial | Map construction exists but is mostly broad `every_owned_state` rewards rather than named sanctuary logistics, clinics, granaries, roads, storehouses, and compact supply support. |
| Guardian military | `THR_guard_high_passes`, `THR_vow_keeper_regiments`, `THR_quiet_mobilization`, `THR_mountain_artillery_mandalas` | Partial | Defensive military content exists, including Vow-Keeper mountaineers, but lacks the spec's visible temple guard / pilgrimage escort / wrathful protection / anti-chaos guardian route. |
| Sangha Compact diplomacy | `THR_lamps_remain_lit`, `THR_permit_foreign_pilgrimage`, `THR_letters_to_war_tired`, `THR_mandala_of_nations` | Partial/renamed | `Mandala of Nations` may be an equivalent, but the spec requires Sangha Compact membership rules, cohesion, anti-puppet clauses, shared relief decisions, failure/exit behavior, and AI. |
| Expansion/liberation | `THR_complete_himalayan_mandala` through `THR_world_is_a_border` | Implemented but mismatched | Expansion exists and has claims/war goals/cores/decisions, but much of it is ordinary annexation/register expansion rather than pilgrimage corridors, liberation, protectorates, and anti-chaos intervention. |
| Anti-chaos powers | Buddha power decisions exist in `holy_realm_buddha_powers_category` | Missing as focus branch | The powers are implemented as decisions, but the focus branch for upgrades/gates (`One Becomes Many`, `Path Through Walls`, `Lotus Bridge`, etc.) is absent. |
| Buddhahood and Final Silence | `THR_buddha_mandate` as `The Unshaken Seat`; `THR_throne_without_body` through `THR_final_silence` | Partial | Final Silence route is substantial and decision-gated, but the required visible sequence around Awakened One, Show the Powers, Witnesses Gather, Extinction of Defilements, and Empty Seat is not represented as focuses. |
| Hidden Schism branch | False Buddha debate/suppression decisions exist | Missing as focus branch | Spec says hidden schism branch should appear if triggered. Current focus tree has no hidden Schism focus family. |

## Missing Or Simplified Content

- Teaching and meditation are implemented primarily as decision systems, not focus route families. Evidence: focus tree only has `THR_convene_mountain_assembly` as teaching unlock while decisions contain the detailed concentration and Buddhahood actions.
- Governance is an older Arhat administration route, not the three-way governance family required by the spec.
- Anti-chaos powers are decision-only; no focus upgrades or branch pacing exist.
- Sangha Compact is likely represented by `Mandala of Nations`, but the naming, membership rules, shared compact mechanics, anti-puppet clauses, and witness-to-final-wheel support are not aligned with the spec.
- Hidden Schism exists as decisions/events, but not as a hidden focus branch.
- Expansion content is deep but tonally mismatched: several focuses grant ordinary annexation war goals and broad regional claims instead of primarily liberation, safe-passage, protectorate, or chaos-occupation intervention.

## Icon Coverage Table

| Area | Current icon coverage | Status | Notes |
| --- | --- | --- | --- |
| Custom Holy Realm focus icons | `GFX_goal_THR_refuge`, `GFX_goal_THR_bodhisattva`, `GFX_goal_THR_arhat`, `GFX_goal_THR_buddha`, `GFX_goal_THR_mercy`, `GFX_goal_THR_pacification`, `GFX_goal_THR_final` in `interface/003_holy_realm.gfx` | Present but limited | Core older-route icons exist. No dedicated teaching, Dhyana, Sangha Compact, or anti-chaos power focus-icon family. |
| Generic/vanilla icons | Most support nodes use generic icons such as `GFX_focus_generic_*`, `GFX_goal_generic_*`, China/RAJ icons, and `GFX_sp_thermo_nuclear_bomb` | Functional but repetitive | Likely loads, but repeated generic visual language weakens route identity. |
| Focus filter icons/localisation | Current filters are `FOCUS_FILTER_THR_PEACE`, `FOCUS_FILTER_THR_FINAL_SILENCE_PRESSURE`, `FOCUS_FILTER_THR_MANDALA_INTEGRATION` | Partial | Spec asks for `FOCUS_FILTER_HOLY_REALM_BODHI`, `TEACHING`, `MEDITATION`, `SANCTUARY`, `COMPACT`, `ANTI_CHAOS`, `NIRVANA`, and `HIDDEN`. |

## Localisation And Reward Mismatches

- All current focus ids have title and description localisation in `localisation/english/003_the_holy_realm_l_english.yml`; only the tree id `THR_focus_desc` is absent from the mechanical key check.
- `THR_buddha_mandate` is localized as `The Unshaken Seat`, matching `docs/holy_realm_buddhahood_progression.md:35`, but the focus itself only fires event `chaosx.nr3.30`; the actual Buddhahood conditions live in the decision/event layer.
- `THR_mandala_of_nations` localisation describes a coalition of refusal and witnessed peace, but the spec asks for a Sangha Compact route with stricter membership/cohesion/failure mechanics.
- Several expansion focus names and descriptions use register/mandala/world-border language while rewards grant ordinary annexation war goals and claims, which conflicts with the spec's liberation/sanctuary framing.

## AI Behavior Gaps

- The focus file has route-aware `ai_will_do` for Final Silence and expansion paths, and `common/ai_strategy/003_holy_realm.txt` has broad strategies for refuge defense, Mandala consolidation, expansion, peacekeeping, coercive route, and final doctrine.
- There is no focus-route AI for the required teaching route, meditation/Dhyana route, or three-way governance route because those focus branches do not exist.
- AI does not visibly evaluate Dhyana Depth, Defilements, compact status, or teaching success for focus route selection as required by the spec.

## High-Priority Fixes First

1. Implement visible teaching and meditation focus branches tied to existing decision variables and gates.
2. Add the three governance routes and make them affect later route availability/rewards.
3. Decide whether `Mandala of Nations` is the Sangha Compact equivalent; if yes, rename/spec-align docs and mechanics, otherwise add the compact branch.
4. Add anti-chaos power focus upgrades using the existing Buddha power decisions as call sites.
5. Reframe expansion/liberation so ordinary conquest is clearly corrupted/high-chaos and the main branch supports pilgrimage corridors, liberation, and protectorates.
6. Add hidden Schism focus visibility only when False Buddha Schism flags are active.
7. Add the spec focus filters and icon family once the branch set exists.

## Validation

Meaningful validation run:

- Compared `search_filter_prios` placement against the offline National focus wiki and vanilla `common/national_focus/generic.txt`; root-level placement is the supported pattern.
- Counted current `THR_` focus ids: 73 focus ids, but route coverage remains incomplete against the required Buddhahood route family list.
- Checked focus localisation coverage for current `THR_` focus ids: all focus titles/descriptions are present; only `THR_focus_desc` is absent.
- Checked `localisation/english/003_the_holy_realm_l_english.yml` encoding: UTF-8 with BOM.

Skipped meaningful validation:

- Did not run the game or parser logs; this subagent was bounded to static repo audit and small local focus-tree fixes.
- Did not test decision runtime behavior for Buddhahood powers or Final Silence; those systems are outside the focus-tree patch scope.

## Remaining Route Risks

- The current tree should not be considered complete for the active Buddhahood goal. It has enough total focuses, but route families required by the spec are missing, merged into older mechanics, or decision-only.
- The patch did not alter branch design, rewards, AI, localisation tone, or icon coverage beyond the filter-priority placement fix.
- Completion plan path: `docs/plans/003_holy_realm_buddhahood_plans/holy_realm_focus_tree_completion_plan.md`.
