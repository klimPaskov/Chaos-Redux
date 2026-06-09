# Event005 Parent Focus and Release Analysis

## Scope

Reviewed current Event005 Soviet Collapse focus and release surfaces while the focus audit subagent runs.

Focus files checked:

- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt`

Supporting files touched or reviewed:

- `common/scripted_effects/005_soviet_collapse_effects.txt`
- `common/scripted_triggers/005_soviet_collapse_triggers.txt`
- `common/script_constants/005_soviet_collapse_constants.txt`
- `common/script_constants/chaosx_triggerable_scenarios_constants.txt`
- `common/scripted_effects/chaosx_triggerable_scenarios_effects.txt`
- `events/005_soviet_collapse.txt`

## Current Findings

Direct focus blocks no longer contain `add_ideas`. The visible idea spam is produced by shared reward helpers and old staged idea spirits, not literal direct `add_ideas` lines in the focus files.

The heaviest repeated generic helpers are still concentrated in:

- Ukraine: repeated military, foreign, socialist, depot, legal, league, and high-chaos helpers.
- Kazakhstan: repeated depot, military, league, socialist, legal, and high-chaos helpers.
- Belarus: repeated depot, legal, military, security, foreign, rail, league, and high-chaos helpers.
- Moldova, internal releases, Baltic shared, Caucasus shared, and Central Asia shared: repeated generic helper families instead of distinct route identities.
- Custom splinters: many tags share the same identity helper sequence, especially `first_guard`, `stores`, `legitimacy`, `rival`, `doctrine`, `economy`, `foreign`, `inner_faction`, `special_arm`, `supply`, `civil_rule`, `propaganda`, `settlement`, `industry_plan`, and `hidden_doctrine`.

The generic helper pattern explains why many trees feel shallow even when the focus count is high. Several route families use different focus names but still converge on the same variable bumps, infantry equipment, support equipment, or generic factory/rail helpers.

Current helper-frequency audit across the four Event005 focus files found these worst repeated reward paths:

- `soviet_collapse_apply_focus_depot_and_supply_control`: 137 focus calls
- `soviet_collapse_apply_focus_military_consolidation`: 134 focus calls
- `soviet_collapse_apply_focus_legal_recognition`: 117 focus calls
- `soviet_collapse_apply_focus_republican_compact_plan`: 82 focus calls
- `soviet_collapse_apply_focus_foreign_channel`: 62 focus calls
- `soviet_collapse_apply_focus_security_supply_plan`: 58 focus calls
- `soviet_collapse_apply_focus_high_chaos_identity`: 55 focus calls
- `soviet_collapse_apply_focus_league_preparation`: 53 focus calls

This is the main remaining depth problem: even without direct idea spam, too many focus names still collapse into the same mechanical buckets.

Layout audit found dense focus coordinates and likely pathline issues in:

- Ukraine: many close pairs and broad mutually exclusive political forks.
- Belarus: recent patches improved some visible prerequisites, but dense sections remain.
- DHC, KHC, FEV, SZA, UWD, MRC, IUL, BAC, ARD, NLC: many one-tile-neighbor focus clusters that can produce compressed pathlines.
- Ancient restorations: compact, mostly readable, but endgame and expansion choices sit very close in multiple mini-trees.

Mutual exclusions are frequent. Ukraine has a large five-route exclusivity cluster plus smaller follow-up exclusivity pairs. Several shared route trees also rely on exclusivity clusters. These need manual layout review because mutually exclusive symbols can cross or sit on intervening focuses if the path is centered too tightly.

## Patches Made From This Analysis

The consolidated republic idea updater was changed to stop adding staged idea tiers and keep focus progress in variables/UI instead.

`has_soviet_collapse_republic_staged_idea` now also detects the older broad route/support idea names so the cleanup helper removes legacy staged idea clutter even in saves that only have those older spirits.

Special high-chaos successors can now enter the progressive release pool at chaos tier 3, while tier 4/5 and chaos triggerable scenarios still force the full high-chaos package.

Triggerable scenario force scaling was increased through constants. The existing formula still scales from controlled states, factories, military factories, and existing divisions, but high and maximum intensity now produce much larger initial armies for strong republics.

Terminal all-possible release passes were raised through constants so overlapping cores and chained releases have more chances to exhaust the full pool.

The triggerable-scenario disabled flag is now checked by the shared active and aftermath triggers. This keeps Soviet Collapse decision surfaces from staying open after a standalone scenario has launched and suppressed the fire-once event.

The foreign patron selected-target trigger now accepts the selected target's own flag directly, instead of relying only on a `FROM` comparison. This makes expanded intervention menus more reliable for dynamic breakaways such as Tajikistan when the engine evaluates the target scope directly.

Focus recovery progress now calls the consolidated republic idea updater. Any focus that uses the shared recovery helper also clears legacy staged republic idea clutter through the central cleanup path, instead of leaving old route/support spirits visible until a later decision happens to refresh the country.

High-chaos identity focuses now call the neighbor expansion and breakaway conflict planners when the country is a high-chaos successor. This makes the identity focus itself create claims/cores, AI aggression, and neighbor war goals or wars instead of only granting local manpower and equipment.

At chaos tier 5, Union Unmade forces the full special-successor spawn package before the terminal all-possible release loops. Lower terminal collapse still uses the normal high-chaos spawn gates.

The focus audit subagent completed a bounded layout pass. It reported no direct focus-file `add_ideas` or `add_timed_idea`, fixed detected same-row mutually-exclusive midpoint collisions in Ukraine and Belarus, and wrote `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_05_31_183450_event005_focus_idea_layout_audit_handoff.md`.

A follow-up focus layout auditor pass wrote `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_05_31_event005_soviet_collapse_focus_layout_audit_patch_handoff.md` and fixed additional Belarus prerequisite/layout violations in `common/national_focus/005_soviet_collapse_republics.txt`. After reviewing that handoff, the parent reduced the visible Ukraine and Belarus route-lock mutual-exclusion meshes from complete graphs to adjacent reciprocal pairs. The route locks still mechanically block every other route through the existing hidden `available` checks, but the focus UI no longer has to draw every route head to every other route head.

The high-chaos focus helper layer now has a shared identity payload, `soviet_collapse_apply_high_chaos_focus_identity_payload`. It is called from the high-chaos identity, legitimacy, assault, supply, and league helpers. The payload is keyed by successor identity flags instead of major-country tag checks:

- civilian factory successors get off-map and state civilian industry plus construction AI pressure
- military factory and Ural worker successors get arms factories, equipment, mobile columns, and arms-factory AI pressure
- Pale Railway Authority successors get the railway construction spirit if missing, trains, railways, infrastructure, supply nodes, and rail/supply AI pressure
- Dead Soldiers Congress successors get the recruitable-population spirit if missing, manpower, assault columns, cores/claims, and neighbor war logic
- naval, Arctic, and northern revenant successors get naval XP, convoys, dockyards, ports, coastal defenses, and naval construction AI pressure
- other high-chaos successors get assault columns, expansion claims, and neighbor expansion logic

CFR and MFR setup now marks their specific factory identity with `soviet_collapse_civilian_factory_successor` and `soviet_collapse_military_factory_successor`, so the shared payload does not need to hardcode those identities by tag.

The runtime high-chaos spawn gate now also accepts chaos tier 3. This matches the event doc/spec claim that special high-chaos successors can start entering the progressive pool at Chaos Tier, while tier 4, tier 5, terminal collapse, and the chaos triggerable scenario still provide the broad force-all path. The dynamic follow-on backlog also treats tier 3 as an emergency cadence tier, so niche ordinary releases and internal releasables are checked more aggressively once the chaos meter reaches Chaos Tier.

The latest focus audit/patch subagent wrote `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_05_31_event005_focus_tree_reward_layout_patch_handoff.md`. It cleared four local vertical path-line blockers in Ukraine and Belarus and strengthened a bounded reward sample for `CFR_rails_first`, `MFR_factory_guard_columns`, `DSC_call_the_dead_soldiers_congress`, `ARD_ice_watch_boards`, and `NLC_ice_road_customs`. It did not touch localisation, icons, or flags.

The follow-up focus audit/patch subagent wrote `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_05_31_191924_event005_focus_reward_layout_audit_patch_handoff.md`. It moved `blr_soviet_collapse_timetable_state` out of a Belarus mutual-exclusion row, added a dockyard/convoy/infrastructure payoff to `ARD_murmansk_port_records`, and added resilience, liaison, infrastructure, radar, and AA payoff to `NLC_polar_neutrality_statute`. It confirmed no direct focus-file `add_ideas`, missing focus icons, missing rewards, missing AI weights, missing filters, or remaining parser-detected same-row layout blockers in the four scoped focus files. It did not touch flags.

The parent patched the shared high-chaos and release helper layer after that handoff:

- `soviet_collapse_release_active_dynamic_follow_on_backlog` now treats chaos tier 3 as an emergency backlog cadence tier, so niche and internal republic follow-on releases are checked faster once the crisis reaches Chaos Tier.
- `soviet_collapse_apply_focus_rail_authority_reward` now gives trains and builds infrastructure/rail across owned controlled core states, with a supply-node payoff and Pale Railway Authority construction AI pressure, instead of being only a single random-state rail reward.
- `soviet_collapse_apply_high_chaos_focus_identity_payload` no longer re-adds the PRA or DSC setup ideas from focus completions; those identities are granted at setup, while focus payloads now push trains/rail/supply, assault columns, cores, claims, and neighbor-war behavior.
- The custom chaos assault helper now scales additional units from controlled states, civilian factories, military factories, existing divisions, and high chaos tier multipliers. This keeps stronger chaos countries spawning and focus-rewarding with much larger forces instead of flat token divisions.
- The malformed but brace-balanced unit-template and meta-unit helper blocks around emergency reserves, League unit deployments, custom chaos assault columns, and high-chaos successor spawning were normalized enough for focused validation.

That handoff confirms this is still not a complete focus-tree finish pass:

- Ukraine, Belarus, and Kazakhstan still need parent-level route-quality review against the spec.
- Many 47-focus custom splinters still have generic helper-only rewards.
- `OGB_soviet_collapse_focus_tree` remains compact at 23 focuses.
- The four ancient restoration trees remain shallow at 16 focuses each.
- Repeated focus icons remain common in `FEV`, `SZA`, `UWD`, `IUL`, and `CFR`.
- AI weights exist, but many route choices remain flat and not route-aware enough.

## Required Follow-Up

The full focus rework is still incomplete.

The next focus implementation tranche should:

- Replace repeated generic helper use with route-specific scripted helpers for Ukraine, Belarus, Kazakhstan, the shared regional republic trees, and the highest-impact chaos countries.
- Make each large tree visibly split into political, industry/logistics, military, diplomacy, expansion, and mechanic branches.
- Make chaos trees intentionally overpowered and identity-driven: construction/factory states should build heavily, dead or military congress states should core/attack neighbors, railway states should build railways and supply hubs, naval directorates should focus on dockyards, ships, ports, and naval aggression.
- Remove or justify every mutual exclusion. If the choice does not alter route access, country identity, expansion logic, decisions, or endgame, it should not be exclusive.
- Reposition dense focus clusters so pathlines do not cross through mutually exclusive focuses or unrelated center focuses.
- Audit filters after reward changes. Industry filters should require real building, production, construction, or resource rewards.
- Connect focus payoffs to decisions and crisis mechanics instead of only variables, equipment, or small buildings.

## Validation Run

- `git diff --check -- common/scripted_triggers/005_soviet_collapse_triggers.txt common/script_constants/chaosx_triggerable_scenarios_constants.txt common/scripted_effects/005_soviet_collapse_effects.txt`
- brace depth check on touched script files
- `rg -n "<=|>="` on touched script files
- `git diff --name-only -- gfx/flags`
- brace depth check on the four scoped Event005 focus files, Event005 decisions, and triggerable scenario effects
- direct focus-file `add_ideas`, `swap_ideas`, and `add_timed_idea` search across the four scoped Event005 focus files
- `git diff --check -- common/scripted_effects/005_soviet_collapse_effects.txt common/scripted_triggers/005_soviet_collapse_triggers.txt docs/plans/005_soviet_collapse_plans/2026_05_31_parent_focus_release_analysis.md common/national_focus/005_soviet_collapse_republics.txt common/national_focus/005_soviet_collapse_custom_splinters.txt common/national_focus/005_soviet_collapse_factory_successors.txt common/national_focus/005_soviet_collapse_ancient_restorations.txt`

All checks passed at the time of this note, and `gfx/flags` remained untouched.
