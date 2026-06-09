# Event005 Soviet Collapse Focus Tree Current Audit and Bounded Patch

Timestamp: 2026-06-04 20:03:05 UTC
Role: `chaosx_focus_tree_auditor`

## Scope

Audited current-state focus trees in:

- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt`

Also inspected directly related helper/idea/decision surfaces:

- `common/scripted_effects/005_soviet_collapse_effects.txt`
- `common/ideas/005_soviet_collapse_ideas.txt`
- `common/decisions/005_soviet_collapse_decisions.txt`
- `localisation/english/005_soviet_collapse_l_english.yml`

No `gfx/flags` or flag sprite files were touched or inspected.

## References Used

- Repo skills: `hoi4-focus-trees`, `chaos-redux-events`, `chaos-redux-subagents`, `chaos-redux-improvement-loop`.
- Repo instructions: `AGENTS.md`.
- Offline wiki: National focus modding, Data structures, Triggers, Effect, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding.
- Vanilla docs: `effects_documentation.md`, `triggers_documentation.md`, `script_concept_documentation.md`, `common/decisions/_documentation.md`, `common/ai_strategy/_documentation.md`.
- Vanilla precedent: `~/projects/Hearts of Iron IV/common/national_focus/generic.txt`.

## Files Changed

- `common/national_focus/005_soviet_collapse_republics.txt`
  - `ukr_soviet_collapse_seal_the_grain_ledgers`: normalized the over-indented `completion_reward` block.

No gameplay behavior was intentionally changed by this patch.

## Current Counts

- Focus trees parsed: 41.
- Focus blocks parsed: 1,698.
- File split:
  - Republics: 9 trees / 501 focuses.
  - Custom splinters: 25 trees / 1,005 focuses.
  - Factory successors: 3 trees / 128 focuses.
  - Ancient restorations: 4 trees / 64 focuses.
- Missing `search_filters`: 0.
- Missing `ai_will_do`: 0.
- Missing prerequisite targets: 0.
- Mutual-exclusion asymmetry: 0.
- Direct focus reward `add_ideas`, `remove_ideas`, `swap_ideas`, `add_timed_idea`: 0.

## Finding 1: Duplicate-Idea and Idea-Spam Surface

I did not find direct focus rewards that add/swap/modify the same idea multiple times. The user's reported symptom is not currently in the focus files as literal repeated `add_ideas` inside a focus.

The current visible-spam problem is helper stacking and repeated helper families:

- `soviet_collapse_apply_focus_depot_and_supply_control`: 138 focus calls.
- `soviet_collapse_apply_focus_military_consolidation`: 131 focus calls.
- `soviet_collapse_apply_focus_legal_recognition`: 108 focus calls.
- `soviet_collapse_apply_focus_republican_compact_plan`: 95 focus calls.
- `soviet_collapse_apply_focus_foreign_channel`: 65 focus calls.
- `soviet_collapse_apply_focus_security_supply_plan`: 64 focus calls.
- `soviet_collapse_apply_focus_high_chaos_identity`: 57 focus calls.
- `soviet_collapse_apply_focus_league_preparation`: 51 focus calls.
- `soviet_collapse_apply_focus_chaos_assault_plan`: 47 focus calls.
- `soviet_collapse_apply_focus_foreign_recognition_plan`: 43 focus calls.

High-confidence focus reward stacks that can produce cluttered helper tooltip/recovery/helper-chain output:

- `kaz_soviet_collapse_the_southern_republics_do_not_kneel` (`005_soviet_collapse_republics.txt:11071`): `soviet_collapse_apply_focus_league_security_plan`, `soviet_collapse_apply_focus_high_chaos_identity`, `soviet_collapse_apply_focus_chaos_assault_plan`.
- `internal_soviet_collapse_tuvan_steppe_compact` (`005_soviet_collapse_republics.txt:4450`): `soviet_collapse_apply_focus_republican_compact_plan`, `soviet_collapse_apply_focus_high_chaos_identity`.
- `internal_soviet_collapse_no_return_to_oblast_rule` (`005_soviet_collapse_republics.txt:4620`): `soviet_collapse_apply_focus_republican_compact_plan`, `soviet_collapse_apply_focus_high_chaos_identity`.
- `soviet_collapse_the_republic_endures` (`005_soviet_collapse_republics.txt:3109`): `soviet_collapse_apply_focus_chaos_legitimacy_plan`, `soviet_collapse_apply_focus_military_consolidation`.
- `blr_soviet_collapse_national_council_of_minsk` (`005_soviet_collapse_republics.txt:8993`): `soviet_collapse_apply_focus_legal_recognition`, `soviet_collapse_apply_focus_republican_compact_plan`.
- `blr_soviet_collapse_foreign_corridor_administration` (`005_soviet_collapse_republics.txt:9091`): `soviet_collapse_apply_focus_foreign_channel`, `soviet_collapse_apply_focus_foreign_recognition_plan`.
- `FTH_stores` (`005_soviet_collapse_custom_splinters.txt:77`): `soviet_collapse_apply_focus_chaos_supply_plan`, `soviet_collapse_apply_focus_security_supply_plan`.
- `FTH_legitimacy` (`005_soviet_collapse_custom_splinters.txt:101`): `soviet_collapse_apply_focus_chaos_legitimacy_plan`, `soviet_collapse_apply_focus_civil_military_authority_plan`.
- `BSC_stores` (`005_soviet_collapse_custom_splinters.txt:4427`): `soviet_collapse_apply_focus_chaos_supply_plan`, `soviet_collapse_apply_focus_security_supply_plan`.
- `NLC_stores` (`005_soviet_collapse_custom_splinters.txt:24434`): `soviet_collapse_apply_focus_chaos_supply_plan`, `soviet_collapse_apply_focus_security_supply_plan`.

Related helper evidence:

- `soviet_collapse_setup_breakaway_country` adds `soviet_collapse_republican_startup_disorder`, but that is release setup, not a focus reward.
- `soviet_collapse_add_republic_focus_recovery_progress` can mitigate or remove `soviet_collapse_republican_startup_disorder`/`soviet_collapse_republican_startup_disorder_mitigated`; it does not add a new visible focus idea.
- `soviet_collapse_update_dsc_dead_army_idea` removes `dsc_grave_regiment_rivalries` and `dsc_dead_soldiers_congress`, then adds `dsc_dead_army_politics` only if missing. This is guarded against duplicate addition.
- `soviet_collapse_clear_republic_staged_ideas` and `soviet_collapse_clear_focus_starting_tension_ideas` are large hidden cleanup helpers. They reduce legacy/staged idea clutter, but their size makes helper-chain audit noisy.

Parent work needed: collapse repeated helper stacks into route-specific payloads with one visible tooltip each, and reserve repeated generic helper calls for genuinely shared baseline work.

## Finding 2: Worst 10 Trees for Missing Branch Depth

These are current-state design gaps, not safe one-line patches.

1. `OGB_soviet_collapse_focus_tree`: 23 focuses. It has restoration flavor and expansion hooks, but political/industry/military/diplomacy branches are too compressed for a successor state.
2. `KZR_soviet_collapse_ancient_focus_tree`: 16 focuses. Ancient-restoration identity is mostly charter/claim/endgame without enough political, industrial, diplomacy, and postwar systems.
3. `SOG_soviet_collapse_ancient_focus_tree`: 16 focuses. Same shallow restoration pattern; needs city-law, trade, legitimacy, and conquest loops.
4. `KHW_soviet_collapse_ancient_focus_tree`: 16 focuses. Water/oasis premise needs a real canal/irrigation/pass-control mechanic, not only a compact route.
5. `ALN_soviet_collapse_ancient_focus_tree`: 16 focuses. Mountain/pass identity needs pass control, raiding, recognition, and aggressive high-chaos payoffs.
6. `TSC_soviet_collapse_focus_tree`: 18 focuses. High-chaos anomaly actor has some expansion hooks but not a full political/industry/expansion route set.
7. `RMC_soviet_collapse_focus_tree`: 18 focuses. Red martyr concept needs distinct mobilization, doctrine, industrial, and conquest loops.
8. `ICD_soviet_collapse_focus_tree`: 18 focuses. Iron Commissariat identity is too compact for the requested overpowered chaos-country standard.
9. `NRF_soviet_collapse_focus_tree`: 18 focuses. Strong theme, weak branch depth; needs a naval mission/fleet-raising loop.
10. `soviet_collapse_breakaway_focus_tree`: 36 focuses, 0 annexation focuses, 0 expansion packages, 0 decision-like unlocks, and heavy generic helper use.

Near misses that still need parent work: `PRA_soviet_collapse_focus_tree` (22 focuses), `soviet_collapse_baltic_focus_tree`, `soviet_collapse_moldova_focus_tree`, and 47-focus custom splinter templates with 0 expansion packages.

## Finding 3: Worst Layout and Pathline Issues

No missing prerequisite targets or mutual-exclusion asymmetry were found. The current layout risk is coordinate collapse and repeated same-row branch stacks, which cause unreadable pathlines and make mutual-exclusion rows hard to read.

Worst current layout issues:

1. `soviet_collapse_breakaway_focus_tree`: 7 duplicate-coordinate groups. Examples: `(14,0)` has `soviet_collapse_assemble_emergency_government`, `soviet_collapse_old_underground_branch`, `soviet_collapse_rail_hub_or_mountain_pass`; `(2,0)` has four military/survival focuses.
2. `BSC_soviet_collapse_focus_tree`: 13 duplicate-coordinate groups. Examples: `(12,0)` has `BSC_birth`, `BSC_supply`, `BSC_anti_puppet_caravan_clause`, `BSC_endgame`; `(8,0)` has five focuses including `BSC_first_guard`, `BSC_legitimacy`, and `BSC_settlement`.
3. `TNC_soviet_collapse_focus_tree`: 13 duplicate-coordinate groups, same template-collapse pattern as BSC.
4. `ALA_soviet_collapse_focus_tree`: 12 duplicate-coordinate groups, same template-collapse pattern.
5. `CFR_soviet_collapse_focus_tree`: 10 duplicate-coordinate groups. The root ladder collapses at `(17,0)` and several strategy/governance branches share rows.
6. `OGB_soviet_collapse_focus_tree`: 6 duplicate-coordinate groups. The compact tree stacks restoration, trade, guard, and Volga question lanes on repeated coordinates.
7. `MFR_soviet_collapse_focus_tree`: 16 duplicate-coordinate groups. The arsenal tree has the worst current coordinate collapse by count.
8. Ancient restorations KZR/SOG/KHW/ALN: no duplicate coordinates, but repeated convergence geometry around road/workshop/guard/envoy/league/old-border focuses likely creates pathline crossings.
9. Ukraine and Belarus: no duplicate-coordinate groups after recent parent work, but several route hubs still stack helper-heavy focuses close together and should be visually checked.
10. 47-focus custom splinter family: several trees no longer duplicate coordinates, but template branch identities still repeat and should be re-laid after mechanical redesign.

## Bounded Patch Rationale

Only one safe patch was made:

- `ukr_soviet_collapse_seal_the_grain_ledgers`: corrected indentation for the `completion_reward` block and its `add_equipment_to_stockpile` reward line.

I did not attempt to fix coordinate-collapse trees because those require parent-owned layout redesign and visual review. I did not rewrite helper stacks because that would be a broad scripted-effect design pass, not a focus-auditor safe patch.

## Validation

Ran/read-only checks:

- Parsed all four focus files: 41 trees / 1,698 focuses.
- Brace balance for all four focus files: ended at 0.
- Direct focus-level idea actions: 0 `add_ideas`, 0 `remove_ideas`, 0 `swap_ideas`, 0 `add_timed_idea`.
- Missing focus filters: 0.
- Missing `ai_will_do`: 0.
- Missing prerequisite targets: 0.
- Mutual-exclusion asymmetry: 0.

Validation to run after this handoff:

- `git diff --check -- common/national_focus/005_soviet_collapse_republics.txt docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_06_04_200305_event005_focus_tree_current_audit_bounded_patch.md`
- `rg -n "<=|>=" common/national_focus/005_soviet_collapse_republics.txt common/national_focus/005_soviet_collapse_custom_splinters.txt common/national_focus/005_soviet_collapse_factory_successors.txt common/national_focus/005_soviet_collapse_ancient_restorations.txt`

## Remaining Parent Work

- Redesign the worst compact trees rather than extending them with generated filler: OGB, ancient restorations, TSC/RMC/ICD/NRF, and generic breakaway.
- Re-lay coordinate-collapsed trees: MFR, BSC, TNC, ALA, CFR, OGB, and generic breakaway.
- Consolidate repeated helper stacks into route-specific helpers with one visible tooltip.
- Give chaos countries aggressive/overpowered expansion systems: claims, wargoals, forced border pressure, puppet demands, raids, neighbor wars, or objective-pressure loops.
- Add route-aware AI to high-impact route focuses, especially in Kazakhstan, republics with simple baseline AI, and small high-chaos successor trees.

No commit was made, per instruction.
