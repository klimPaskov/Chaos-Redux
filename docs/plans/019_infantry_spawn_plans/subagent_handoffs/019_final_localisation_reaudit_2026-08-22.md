# Event 019 Final Localisation Reaudit — 2026-08-22

## Outcome

The final bounded audit is complete. Event 019 remains a Minor Repeatable, decisions-only feature with no runtime scripted GUI. I patched the two missing standardization-requisition keys, removed live and archival player-text references to the former Muster Board, clarified staged settlement and standardization wording, replaced implementation-facing provider language, and made derivative family sustainment display only the active family's exact two-resource cost.

No gameplay source was changed. No commit was created.

## Changed files

- `localisation/english/019_infrantry_spawn_l_english.yml`
- `common/scripted_localisation/019_infantry_spawn_scripted_localisation.txt`
- `docs/plans/019_infantry_spawn_plans/subagent_handoffs/019_final_localisation_reaudit_2026-08-22.md`

## Changed identifiers

### Missing decision coverage added

- `infantry_spawn_advance_standardization_requisition`
- `infantry_spawn_advance_standardization_requisition_desc`

The existing `infantry_spawn_advance_standardization_requisition_tt` was retained and rewritten only to remove a semicolon and make the final conversion gate easier to read.

### Stale UI wording removed

- `chaosx.nr19.2.b.tt`
- `chaosx.nr19.2.c.tt`
- `infantry_spawn_achievement_combat_trial_country_available_tt`
- `infantry_spawn_muster_gui_title`
- `infantry_spawn_muster_gui_animations_tt`
- `infantry_spawn_muster_gui_close_tt`
- `infantry_spawn_muster_gui_lot_standardize_tt`

The live opening and achievement tooltips now refer to the sealed Formation Ledger. The unused archival `_muster_gui_` keys retain their identifiers for compatibility, but their values no longer claim that a Muster Board exists.

### Exact tranche and provider prose repaired

- `infantry_spawn_settle_selected_lot_obligations_tt`
- `infantry_spawn_requisition_tranche_cost_tooltip`
- `infantry_spawn_open_standardization_cycle_tt`
- `infantry_spawn_advance_standardization_requisition_tt`
- `infantry_spawn_selected_lot_exact_obligation_cost_tooltip`
- `infantry_spawn_family_sustainment_cost_profile_ledger_backed`
- `infantry_spawn_family_request_cost_profile_mutated_zombie`
- `infantry_spawn_family_request_cost_profile_elephant`
- `infantry_spawn_family_request_cost_profile_africa_strange_force`
- `infantry_spawn_family_request_cost_profile_greater_ghost`
- `infantry_spawn_family_request_cost_profile_cave_brood`
- `infantry_spawn_family_request_cost_profile_rat_brood`
- `infantry_spawn_family_request_cost_profile_chaos_assault_battalion`
- `infantry_spawn_family_request_cost_profile_cannibal_irregular`
- `infantry_spawn_family_request_cost_profile_ledger_backed`

The revised tranche text says that one action charges only the displayed entries, never more than four, keeps every unpaid class pinned, archives an unaccounted lot only after both debt and manpower reach zero, and refunds every paid standardization tranche if roster proof fails.

### Project-host prose repaired

- `brilliant_scientist_event19_clone_host_desc`
- `brilliant_scientist_event19_aryan_clone_host_desc`
- `brilliant_scientist_event19_paleogenetic_host_desc`
- `brilliant_scientist_event19_xenobiological_host_desc`
- `brilliant_scientist_event19_portal_host_desc`
- `brilliant_scientist_event19_temporal_host_desc`

The descriptions now present sealed project receipts and independent muster commands in-world. They no longer mention a “provider-owned” receipt or an “Event 016 parent identity.” The Aryan clone text preserves the established Mengele connection without implementation terminology.

### Dynamic localisation added

- `GetInfantrySpawnDerivativeFamilySustainmentCost`
- `GetInfantrySpawnDerivativeFamilySustainmentBlockedCost`
- `infantry_spawn_derivative_pay_family_sustainment_cost`
- `infantry_spawn_derivative_pay_family_sustainment_cost_blocked`
- `infantry_spawn_derivative_pay_family_sustainment_cost_tooltip`
- `infantry_spawn_derivative_family_sustainment_cost_zombie_blocked`
- `infantry_spawn_derivative_family_sustainment_cost_ghost_blocked`
- `infantry_spawn_derivative_family_sustainment_cost_golem_blocked`

Before the patch, the derivative sustainment decision displayed six icons covering zombie, ghost, and golem schedules together even though only one family branch could be charged. It now selects the active derivative family and shows exactly its two icon-first resources. The selector uses the existing `infantry_spawn_derivative_is_zombie`, `infantry_spawn_derivative_is_ghost`, and `infantry_spawn_derivative_is_golem` country-scoped triggers, with the existing ledger-backed text as a defensive fallback.

## Audit inventories

### Missing keys

- Before patch: `infantry_spawn_advance_standardization_requisition` and `infantry_spawn_advance_standardization_requisition_desc` were missing.
- After patch: none among all 85 Event 019 depth-one decisions and missions, all 45 derivative focuses, all 26 derivative decisions and missions, all referenced event/focus/decision tooltips, all 51 custom-cost base/blocked/tooltip contracts, all 57 provider presentation keys, or all 11 visible achievement name/description pairs.

### Duplicate keys

- Duplicate keys within `019_infrantry_spawn_l_english.yml`: none.
- Event 019 key collisions elsewhere under `localisation/english`: none.

### Scripted localisation issues

- Fixed: the derivative sustainment cost was static across three mutually exclusive families and misleadingly displayed six resource icons.
- `019_infantry_spawn_scripted_localisation.txt` now has 19 unique `defined_text` names, 219 unique localisation references, no unresolved non-GFX localisation reference, balanced braces, and no direct `§` or `£` characters.
- The exact settlement and requisition recursion retains temporary, unscoped display cursors, aligned icon/amount arrays, explicit terminal rows, and one icon-first row per charged class. No broken `ROOT.` or other scoped temporary-variable use was found.
- The claimant selectors cover all 20 profiles and all four male name variants per profile, with their established fallbacks intact.

### Dynamic text opportunities

- Implemented: active-family derivative sustainment selection.
- Implemented: missing standardization decision title and description.
- Existing dynamic text retained: exact settlement rows, requisition tranche rows, provider presentation tokens, claimant identities, derivative region/identity tokens, and SCN-013 type/intensity selectors.
- No further in-scope dynamic-text gap remains.

### Cross-surface mismatch notes

- Fixed: opening event and achievement availability text referred to a nonexistent Muster Board while the accepted runtime is decision categories plus the Formation Ledger.
- Fixed: project-host descriptions exposed provider and parent-event implementation language.
- Fixed: derivative sustainment displayed costs for inactive families.
- The ordinary and claimant categories share `infantry_spawn_ordinary_management_category_is_relevant`. The inspected trigger excludes completed takeover, achievement-marked revolt, derivative/scenario actors, and keeps the surface open only while lots, obligations, claimants, deferred actions, transactions, operations, or cooldowns remain. Evolution III and IV flags alone do not prevent peaceful high-evolution closeout.
- SCN-013 has four localized types and four localized intensities, with matching name and tooltip selectors: conventional flood, arsenal lottery, general mutiny, anomalous rising; contained, widespread, cascading, and world muster.
- All 11 Event 019 achievements are visible definitions and have `_NAME` and `_DESC` strings in `chaosx_achievements_l_english.yml` plus resolved requirement tooltips in the Event 019 localisation surface.
- The derivative focus tree has 45 focus nodes with complete title/description coverage. The derivative decisions file has 26 player actions/missions with complete title/description coverage.
- The 20 claimant profiles expose 80 region-appropriate male names. No female claimant identity or pronoun was found.
- Event and scenario prose consistently describes formations, armies, barracks, columns, or massed hosts. `GetInfantrySpawnScenarioActorArmyScene` retains the formation-first visual selector contract. No portrait-centric wording was introduced.

### Provider and texticon evidence

- Provider IDs: `501–514`, `518`, `520–523`, exactly 19 providers.
- Presentation contract: name, request cost, and sustainment cost for each provider, exactly 57 keys; all resolve, including nested references.
- Custom equipment texticons: exactly 20 Event 019 custom `_text_icon` keys beyond the three standard equipment keys; every referenced GFX sprite is registered.
- Provider 523 template contains all nine cannibal combat bodies: `cannibal_scavenger_warband`, `cannibal_feast_guard`, `cannibal_feast_cohort`, `cannibal_bone_guard`, `cannibal_bone_riders`, `cannibal_island_reavers`, `cannibal_siege_eaters`, `cannibal_march_predation_column`, and `cannibal_network_cadre`.
- Provider 523 obligations remain exact at 7,350 manpower, 990 infantry equipment, and 35 motorized equipment.

### Cost and tooltip evidence

- All 51 Event 019 `custom_cost_text` keys have a base, `_blocked`, and `_tooltip` value.
- No static Event 019 cost value now displays more than four icons. Ordinary request modes display exactly four icon-first resources. Dynamic settlement and standardization are source-capped at four positive classes per tranche. The derivative sustainment repair reduces its visible schedule from six mixed-family icons to two active-family icons.
- All 111 Event 019 decision/mission tooltip references resolve. Every actionable decision has a useful effect tooltip; timed mission completion is described by its title/description and owning start-action tooltip. Requirement tooltips used by the 26 derivative decisions resolve, and blocked custom costs present the actual resource amounts rather than prose labels.
- No misleading refund claim was found: the standardization failure path applies exact refunds from the paid token/amount arrays before clearing the requisition.

### Encoding concerns

- `019_infrantry_spawn_l_english.yml` begins with UTF-8 BOM bytes `EF BB BF` after patching.
- No encoding concern remains in the authorized files.

### Prose-quality issue list and before/after summary

- Vagueness: “Formation Ledger obligations only” became a direct statement of whether stockpiles are charged now and when each obligation appears.
- Bloat: overloaded semicolon sentences in tranche tooltips were split into short, complete statements without losing payment, pinning, archive, conversion, or refund rules.
- Obvious explanation: archival UI animation text no longer repeats the nonexistent Muster Board title; it describes only the decorative state the key would control if consumed.
- Repetition: repeated “provider-owned” and “parent identity” formulas across project hosts became concise project-receipt language while retaining host distinctions.
- Overcomplication: “provider-owned class … is exposed as the next tranche” became “unpaid equipment class … appears in a later tranche.”
- Style-rule repair: all player-facing Event 019 values are free of semicolons and em dashes, and no value contains `Muster Board`, provider implementation language, update-history wording, prompt fragments, or tuning-history claims.

### Sourced quotation preservation

No sourced or attributed quotation appears on the inspected Event 019 event, decision, focus, scenario, achievement, claimant, provider, or project-host localisation surfaces. No quotation was altered.

## MCP and source validation

- Event lint: `EVENT_INSPECTED_PARTIAL`, no blocker. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6f9fc976bee73c09d940fed8594d4e4ede8da5d76fa6fabdba809cef5a292f5a/fbc2bcb9ce56b35b5208f529727aee986cc8caa3dd2bc15c13076abf75c096a9/event-lint-e8ab707dc24e.json`.
- Event options render: `EVENT_RENDERED_PARTIAL`, no blocker. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1068684fa2f471e7a153cf19226c0093108551a392d1b8e4ac44c00fe7207304/47d9894e63f3c47d44926647f04d0a11a90cd2addd7fb0fcc412e39fa58762d2/event-options-e8ab707dc24e-manifest.json`.
- Focus inspect: `FOCUS_INSPECTED`, 45 focuses, 45 resolved titles, no blocking diagnostic. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/07a6e7feb655aafda9abf69b4311d49d61e6e95135a4ccd883cba8bf99dbd217/6031533b1a708a07dd05a5e10d7fbce74ecfadeaeb78a39415af02b50c963fe8/focus-inspect.4e131bc10da84224.json`.
- Focus render: `FOCUS_RENDERED`, validation passed, no blocker. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/12241b0bf8dce416753a76b4ea279bcb61f8da0fc278a63df8d33d1af46efffc/e86b89ea39af62e573a63df2dbeaf276d257cd6ca04a4cc42aadeb64f97889a3/infantry_spawn_derivative_focus_tree.focus.json`.
- The two Event MCP calls deferred workspace-wide helper and lifecycle projection because of workspace size. Their direct source-linked evidence completed, but this limitation is not equivalent to a fully passing workspace-wide event validation.
- The installed HOI4 MCP exposes no decision-specific inspection or rendering route. Decision validation therefore used current source, localisation references, exact-cost contracts, and the required offline/vanilla decision documentation; this is an exact tooling limitation rather than MCP-equivalent evidence.
- No GUI MCP route was run because Event 019 has no runtime scripted GUI. The former Muster Board is archival and must not be treated as an active surface.

## Unresolved wording decisions, simplifications, and fallbacks

- Unresolved wording decisions: none.
- Simplifications or omitted requested surfaces: none.
- Gameplay changes: none.
- Asset substitutions or UI fallbacks: none.
- Live in-game validation was not run; repository rules reserve that consumer check for the user.

## Skills and references used

- `chaos-redux-events`
- `chaos-redux-decisions-missions`
- `chaos-redux-focus-trees`
- `chaos-redux-event-assets`
- `chaos-redux-subagents`
- Offline Paradox wiki pages for Localisation, Event modding, Decision modding, National focus modding, Data structures, Triggers, Effects, Modifiers, Scopes, On actions, Idea modding, and AI modding
- Installed vanilla script, trigger, effect, and decision/localisation precedents
