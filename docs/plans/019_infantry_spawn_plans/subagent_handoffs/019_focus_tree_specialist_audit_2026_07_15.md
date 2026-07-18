# Event 19 Focus-Tree Specialist Audit

Date: 2026-07-15  
Role: `chaosx_focus_tree_auditor`  
Mode: read-only specialist audit; this handoff is the only file changed by the auditor

## Verdict

**Final re-audit verdict (2026-07-15): P0: 0. P1: 0. P2: 0.**

The parent remediation resolves all three focus-tree findings recorded by the 2026-07-15 audit. The zombie, ghost, and golem focus graphs retain their structurally sound 35-focus adapted packages, and the fourth idea track, focus-icon shine pairs, and five incomplete focus tooltips now match the package contract. The original findings and baseline evidence are retained below as audit history; the dated **Parent resolution re-audit** section at the end of this handoff is the current live-source status.

The two owner-approved engine limitations are not focus-tree defects and were excluded from severity counts:

- exact transfer of the frozen loyal-formation set remains explicitly fail-closed pending approval of an ownership-transfer fallback;
- the four exact same-battle achievements remain pending approval because their required facts are not atomically exposed.

## Original findings (2026-07-15; resolved by the parent re-audit below)

### P1-FT-01: the fourth simultaneous idea track becomes empty after former-parent resolution

The source-of-truth package contract says that a live derivative carries four simultaneous tracks: government recognition, family command, logistics/doctrine/sustainment, and former-parent/expansion (`docs/specs/019_infantry_spawn_specs/matrices/019_country_package_matrix.md:16`, `:48-52`).

The live implementation establishes those four slots correctly:

- `infantry_spawn_derivative_add_starting_ideas` installs government, logistics, former-parent, and one family burden (`common/scripted_effects/019_infantry_spawn_derivative_package_effects.txt:49-64`);
- `infantry_spawn_derivative_choose_claimant_route`, `...choose_collective_route`, and `...choose_species_route` preserve one mutually exclusive idea in each slot (`:1305-1370`);
- `infantry_spawn_derivative_refresh_logistics_idea_slot` keeps doctrine and sustainment mutually exclusive in the logistics slot (`:1373-1431`).

The fourth slot then disappears. `infantry_spawn_derivative_resolve_former_parent_pressure` removes whichever former-parent route idea is active and installs no expansion-stage successor (`:1451-1456`). `infantry_spawn_derivative_regional_predator` is added only after the late capstone's separate hard gates pass (`:1817-1831`). A derivative can therefore spend the potentially long post-resolution/pre-capstone interval with three active track ideas, not four.

Impact: this is a required package and balance-contract mismatch, not a cosmetic omission. It also makes the documented former-parent/expansion lifecycle discontinuous. Resolution requires either an implemented post-resolution expansion-stage idea in that slot or an explicit owner-approved change to the source-of-truth four-simultaneous-track contract. The auditor did not choose between those designs.

### P2-FT-01: all 45 focus icons lack conventional `_shine` SpriteTypes

Every focus has a unique base sprite, and all 45 referenced DDS files exist and have valid `DDS ` headers at `100x88`. The 45 base definitions occupy `interface/019_infantry_spawn.gfx:200-379`. There are **0/45** matching `GFX_goal_infantry_spawn_derivative_*_shine` SpriteTypes.

Recommended precedent:

- vanilla pairs `GFX_goal_support_communism` in `Hearts of Iron IV/interface/goals.gfx:626` with `GFX_goal_support_communism_shine` in `interface/goals_shine.gfx:2220`;
- Chaos Redux pairs each Event 6 base focus sprite with a same-texture `_shine` SpriteType and `effectFile = "gfx/FX/buttonstate.lua"` in `interface/006_independence_wave.gfx:3-30`.

No new art is needed. The recommended repair is one matching `_shine` SpriteType per existing Event 19 focus sprite, reusing the same DDS and `gfx/FX/buttonstate.lua`.

### P2-FT-02: five focus tooltips omit additive rewards that the focus grants

The focus title, description, and tooltip keys all exist, but these five tooltips do not disclose real additive rewards in their completion effects:

| Focus node | Live reward omitted from tooltip | Script evidence | Localisation evidence |
|---|---:|---|---|
| `infantry_spawn_derivative_make_an_army_of_the_host` | `army_experience_medium` (10 XP) | focus file `:450-452` | localisation `:891` |
| `infantry_spawn_derivative_zombie_number_the_devouring_bands` | `army_experience_small` (5 XP) and `command_power_small` (10 CP) | focus file `:681-685` | localisation `:935` |
| `infantry_spawn_derivative_zombie_teach_the_base_dead_to_muster` | `army_experience_small` (5 XP) | focus file `:703-706` | localisation `:939` |
| `infantry_spawn_derivative_ghost_call_a_second_procession` | `command_power_small` (10 CP) | focus file `:790-794` | localisation `:955` |
| `infantry_spawn_derivative_golem_reconstruct_the_binding_marks` | `army_experience_small` (5 XP) | focus file `:899-903` | localisation `:975` |

The unlock and route-exclusion text is otherwise accurate. The repair is localisation-only: append the omitted reward values to the five existing `_tt` strings.

## Live tree inventory and graph evidence

- Focus-tree identifier: `infantry_spawn_derivative_focus_tree`. This is the `focus_tree` ID and is **not** counted as a focus node.
- Focus nodes: **45/45 unique** `focus = {}` blocks.
- Composition: **30 shared + 5 zombie + 5 ghost + 5 golem**.
- Visibility: **35 zombie, 35 ghost, 35 golem**. All 15 family nodes have a matching family `allow_branch`; the two foreign family modules remain hidden.
- A family country can complete 25 of its 35 visible nodes because hierarchy, doctrine, and family-transformation groups each contain one three-way commitment.
- Prerequisites: 44 blocks, 54 focus references, 0 missing targets, and 0 directed cycles. The only node without a prerequisite is the intended opener, `infantry_spawn_derivative_hold_the_first_ground`.
- Multi-reference prerequisite blocks use HOI4 OR semantics at the five intended merge nodes: `infantry_spawn_derivative_make_an_army_of_the_host`, `...a_method_fit_for_the_host`, and the zombie, ghost, and golem family capstones.
- Mutual exclusions: 15 blocks, 30 directed references, 0 missing targets, and 0 asymmetric references. These form 15 undirected pairs across five three-way commitment groups.
- Layout: 45 unique coordinate pairs; no exact node overlap was found.
- Every node has an icon, `available`, `completion_reward`, `custom_effect_tooltip`, and `ai_will_do` block.

## Route, gate, reward, and identity review

### Hierarchy and doctrine

- Claimant, Collective, and Species hierarchy openers are pairwise hard-exclusive.
- Claimant requires `infantry_spawn_derivative_claimant_uid`; Collective and Species reject the scenario claimant-breakaway wrapper.
- The hierarchy merge accepts the completed final node of any one route using one OR prerequisite block.
- Concentrated Host, Scattered Bands, and Captured Auxiliaries are pairwise hard-exclusive, and the doctrine merge accepts any one outcome.
- In each family module, the claimant-shaped outcome is hard-gated to the claimant route. The other two outcomes remain player-flexible but carry Collective/Species AI preference rather than a hard route gate. That is consistent with the live route map's flexible family-method wording; it is not counted as a defect.

### Capstone

`infantry_spawn_derivative_become_the_regional_predator` is gated by all of the following live proofs:

- one consolidated hierarchy route;
- the matching zombie, ghost, or golem family identity capstone;
- family sustainment unlocked plus at least one paid reinforcement/sustainment action (or authorized base-zombie training);
- former-parent pressure resolved;
- at least one integrated district;
- at least 8 controlled states;
- at least 2 recorded war victories.

The completion effect sets `infantry_spawn_derivative_regional_predator_ambition` and immediately calls `infantry_spawn_derivative_check_regional_predator`; that helper repeats the hard proofs before adding `infantry_spawn_derivative_regional_predator`. Because focus rewards execute before the focus is marked complete, not requiring the just-completed focus inside the helper is correct.

### Reward substance and family identity

- The focus file sets 34 distinct package flags. All 34 are consumed by decisions, AI profiles, scripted gates, or the capstone, or are explicit route-state markers; all 34 are cleared by final cleanup.
- Focus rewards unlock a 25-entry derivative decision/mission category: 22 actionable decisions with AI weights and 3 timed missions.
- Family adaptations are not mere renamed copies: zombie nodes unlock controlled training/band rally and fragmentation handling; ghost nodes unlock manifestation/anchors and decline control; golem nodes unlock binding/foundry/material patterns. Their icons and localisation are also family-distinct.
- The idea file defines 38 unique ideas with 38/38 names and 38/38 descriptions. Before P1-FT-01's lifecycle gap, the four slots are mutually exclusive and route-aware; defeat installs one government failure, one logistics failure, one family failure, and one former-parent failure.
- Starting weaknesses are substantive: Unrecognized Host, Seized Muster Districts, Pursued by Former State, and the matching Fragmented Command / Unstable Manifestation / Broken Pattern burden all apply negative modifiers. Late family and Regional Predator bonuses remain bounded below parent-event escalation systems.

## AI evidence

- All 45 focus nodes have `ai_will_do`.
- Hierarchy weighting prefers claimant authority when a claimant is viable, Collective for zombie/ghost cohesion, and Species for golem autonomy; the relevant alternatives receive avoid factors where appropriate.
- Doctrine weighting prefers concentration for claimant/golem play, scattering for collective/zombie play, and captured auxiliaries for ghosts while discouraging auxiliaries on Species routes.
- Each family transformation's three-way group has route-aware preference modifiers.
- `common/ai_strategy/019_infantry_spawn_derivative_ai_strategy.txt` contains 22 profiles and 51 strategy entries. All 22 have `abort_when_not_enabled = yes`; their family triggers route through the active derivative trigger, so defeat deactivates them.
- The 22 non-mission derivative decisions all have `ai_will_do`; target decisions use bounded neighbor/state filters rather than distant-country scans.

## Localisation and icon coverage

- Focus localisation: 45/45 titles, 45/45 descriptions, and 45/45 tooltips; no duplicate or empty derivative keys were found. P2-FT-02 concerns completeness of five values, not missing keys.
- The English localisation file begins with UTF-8 BOM bytes `EF BB BF`.
- Base focus sprites: 45/45 present and unique.
- Focus DDS files: 45/45 present, valid DDS headers, all `100x88`.
- Visual inspection of `docs/assets/019_infantry_spawn/contact_sheets/event_019_focus_icon_contact_sheet.png` confirms distinct shared, zombie, ghost, and golem icon families rather than a single hue-shifted set.
- Shine sprites: 0/45; see P2-FT-01.

## Defeat cleanup, isolation, and world-end boundary

- `on_capitulation` records derivative defeat and `on_annex` runs final cleanup (`common/on_actions/019_infantry_spawn_derivative_on_actions.txt:9-42`).
- Defeat closes the package and decision category, removes all active track ideas, removes three live missions, and installs four matching remnant ideas (`common/scripted_effects/019_infantry_spawn_derivative_package_effects.txt:1858-1945`).
- Final annex cleanup removes every one of the 38 derivative ideas, clears all 34 focus-created flags, removes the missions, clears derivative route/family variables, clears private ledgers, and removes tracked formations (`:2089-2222`).
- The tree has one load call only, inside derivative setup (`:365-368`). Setup clears `infantry_spawn_participant`; `infantry_spawn_derivative_is_parent_isolated` rejects zombie-parent, Death-parent, cave/golem-parent, `ZZZ`, and `DTH` identities (`common/scripted_triggers/019_infantry_spawn_triggers.txt:718-779`).
- No world-end, super-event, parent-stage, or parent-endgame token is referenced by the focus, derivative idea, derivative effect, derivative trigger, derivative decision, derivative AI, derivative on-action, or Event 19 event surfaces searched for this audit.
- Exactly one Event 19 registry code file exists: `common/scripted_effects/019_infantry_spawn_unit_registry_effects.txt`. The auditor neither opened it for modification nor changed it.

## Bounded caveat: scenario claimant wrapper

SCN-013 General Mutiny uses `infantry_spawn_setup_claimant_breakaway_identity`, which deliberately assigns family ID `none` and loads the shared derivative tree. That wrapper sees the 30 shared nodes, not one of the three 35-node anomalous-family adaptations, and it cannot satisfy the family-transformation capstone gate. This audit does not count that as a defect because the requested 35-node acceptance target is explicitly zombie/ghost/golem, while General Mutiny is a separate Evolution III claimant scenario. If General Mutiny claimant actors are intended to earn Regional Predator, that requires an explicit design decision rather than an assumed family fallback.

## Reference and validation record

Before opening Event 19 source, the auditor fully read `AGENTS.md` and the repo skills `hoi4-focus-trees`, `chaos-redux-events`, and `chaos-redux-subagents`; consulted the required offline wiki pages for data structures, triggers, effects, modifiers, localisation, scopes, on-actions, events, decisions, ideas, AI, national focuses, countries, units, and divisions; and consulted installed vanilla documentation for script concepts/constants, triggers, effects, modifiers, localisation objects/formatters, on-actions, units, and AI strategy. Vanilla focus, idea, on-action, AI-strategy, icon, and localisation precedents were compared, including `baltic_shared.txt`, `generic.txt`, Baltic idea/AI files, and the regular-plus-shine goal pair cited above.

The configured HOI4 MCP focus inspector/render/lint tools were not exposed to this subagent session. That is recorded as a tooling limitation, not a pass or failure. Direct live-source graph analysis was used instead.

Audited focus source SHA-256: `700A7BB456C7C3BF9E915ED19E64B021B56EE665EF16A3E6372E4547B287C8BE`.

## Simplifications, omissions, blockers, and remaining risks

- No gameplay, localisation, asset, spec, workbook, or registry file was edited by this auditor.
- No audit criterion was silently waived.
- P1-FT-01, P2-FT-01, and P2-FT-02 are resolved by the live parent remediation verified on 2026-07-15.
- The loyal-formation transfer and four same-battle achievements remain known owner-approval blocks, not focus-tree findings.
- The claimant-wrapper caveat above remains a design-boundary risk if its intended endgame changes.
- No commit was created: the shared worktree contains extensive concurrent parent changes, and this read-only subagent did not stage or commit them.

## Changed file

- `docs/plans/019_infantry_spawn_plans/subagent_handoffs/019_focus_tree_specialist_audit_2026_07_15.md`

## Parent resolution re-audit — 2026-07-15

**Status: all three original findings are resolved. Final severity count: P0: 0. P1: 0. P2: 0.**

This was a narrow read-only re-audit of the parent's remediation. No gameplay, localisation, asset, specification, workbook, or registry file was edited by the auditor.

### P1-FT-01 resolved: the fourth idea track remains occupied

- `infantry_spawn_derivative_outward_muster` is defined as a distinct idea at `common/ideas/019_infantry_spawn_derivative_ideas.txt:339-346`.
- `infantry_spawn_derivative_resolve_former_parent_pressure` removes the active former-parent route idea and adds `infantry_spawn_derivative_outward_muster` whenever Regional Predator is not already present (`common/scripted_effects/019_infantry_spawn_derivative_package_effects.txt:1451-1462`). This preserves the fourth former-parent/expansion slot across resolution.
- Once the capstone's live hard gates pass, `infantry_spawn_derivative_check_regional_predator` removes Outward Muster and adds `infantry_spawn_derivative_regional_predator` in the same effect block (`:1821-1837`). The slot is replaced rather than stacked or left empty.
- `infantry_spawn_derivative_remove_active_ideas` removes both Outward Muster and Regional Predator (`:1863-1898`). Defeat calls that helper before installing remnant ideas (`:1900-1921`), and final annex cleanup calls the same helper (`:2095-2107`). Neither idea is missing from defeat or final cleanup.
- Outward Muster and Regional Predator each have exactly one idea definition, one English name, and one English description (`localisation/english/019_infrantry_spawn_l_english.yml:791-794`). The full derivative idea inventory is now 39/39 unique definitions with 39/39 names, 39/39 descriptions, and complete final-cleanup coverage.

### P2-FT-01 resolved: all focus icons have matching shine sprites

The live focus tree references 45 focus icons, all 45 unique. `interface/019_infantry_spawn.gfx` contains exactly 45 matching base SpriteTypes and 45 matching `_shine` SpriteTypes. A one-to-one parse found zero missing or duplicate bases, zero missing or duplicate shines, zero base/shine texture mismatches, and zero shine effect mismatches. Every `_shine` SpriteType reuses its base icon's exact texture path and sets `effectFile = "gfx/FX/buttonstate.lua"`.

### P2-FT-02 resolved: all five additive rewards are disclosed exactly

The five `_tt` strings retain their existing unlock and route-exclusion wording and now disclose the exact scripted reward constants:

| Focus node | Live effect | Corrected tooltip disclosure |
|---|---:|---:|
| `infantry_spawn_derivative_make_an_army_of_the_host` | `army_experience_medium` | 10 Army Experience |
| `infantry_spawn_derivative_zombie_number_the_devouring_bands` | `army_experience_small`; `command_power_small` | 5 Army Experience; 10 Command Power |
| `infantry_spawn_derivative_zombie_teach_the_base_dead_to_muster` | `army_experience_small` | 5 Army Experience |
| `infantry_spawn_derivative_ghost_call_a_second_procession` | `command_power_small` | 10 Command Power |
| `infantry_spawn_derivative_golem_reconstruct_the_binding_marks` | `army_experience_small` | 5 Army Experience |

Each corrected tooltip key exists exactly once and displays the same `constant:infantry_spawn_derivative_reward.*` token used by its focus completion effect. The constants resolve to 5/10 at `common/script_constants/019_infantry_spawn_derivative_package_constants.txt:33-36`. The English localisation file retains its UTF-8 BOM.

### Re-audit disposition

- No narrow re-audit simplification, omission, fallback, or unresolved focus-tree finding remains.
- The loyal-formation transfer and same-battle achievement approval blocks remain outside this focus-tree verdict and were not reclassified.
- Only this handoff was changed by the auditor: `docs/plans/019_infantry_spawn_plans/subagent_handoffs/019_focus_tree_specialist_audit_2026_07_15.md`.
- No commit was created.
