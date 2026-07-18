# Event 19 Derivative Focus Tree Independent Specialist Audit

Date: 2026-07-16

Role: `chaosx_focus_tree_auditor`

## Scope and independence

This audit independently reviewed the current Event 19 derivative focus tree and the linked ideas, decisions, AI strategies, localisation, sprites, dynamic-country setup, family providers, expansion rules, defeat lifecycle, and parent-isolation seams. It did not use earlier audit conclusions as evidence.

The primary tree under review was `common/national_focus/019_infantry_spawn_derivative_focus.txt`. Linked runtime review included the Event 19 derivative package effects and triggers, derivative decisions and category, derivative ideas, derivative AI strategies, derivative on-actions, scenario setup effects, the consolidated Event 19 family provider registry, script constants, English localisation, and `interface/019_infantry_spawn.gfx`.

Required project guidance used:

- `hoi4-focus-trees`
- `chaos-redux-events`
- `chaos-redux-subagents`
- `hoi4-decisions-missions`
- `chaos-redux-event-assets`

The required offline Paradox wiki pages were consulted, including National focus modding, Decision modding, Idea modding, AI modding, Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, and Event modding. Vanilla official effect, trigger, script-concept, AI strategy, and decision documentation was consulted. Vanilla focus layout, explicit `load_focus_tree`, and AI strategy precedents were also inspected.

## Specialist verdict

The current source satisfies the audited derivative focus and linked-package requirements. No outstanding focus or linked package defect remains in the reviewed source.

The only evidence limitation is visual tooling. Both the focus inspector and focus renderer were blocked before scanning by `ARTIFACT_STORAGE_LIMIT`. Static source inspection supports a coherent graph and collision-free authored coordinates, but connector crossings and rendered behavior at different resolutions were not independently proven by the MCP tools.

This is a specialist focus-package verdict only. It is not an overall Event 19 completion claim.

## Content scale and route coverage

The tree contains 45 unique focuses:

- 30 shared focuses
- 5 zombie focuses
- 5 ghost focuses
- 5 golem focuses

The shared layer contains the requested opening, hierarchy, sustainment, military method, bounded expansion, and regional-predator content. Each nonhuman derivative sees the 30 shared focuses and its 5-focus family overlay, giving 35 visible focus-scale pieces. A normal nonhuman route can complete 25 focuses because the three hierarchy roots, three military doctrines, and three family transformations are mutually exclusive choices.

| Derivative identity | Visible focus content | Normally completable | Adapted content and identity proof |
| --- | ---: | ---: | --- |
| Claimant breakaway | 30 shared | 22 | Claimant continuity, guard rally, governance, sustainment, integration, and submission decisions supplement the shared claimant route |
| Zombie derivative | 35 | 25 | Base-zombie training, zombie rally, hunger discipline, barracks recovery, and zombie-specific integration |
| Ghost derivative | 35 | 25 | Spawn-only processions, anchor decisions, managed slow decline, spectral sustainment, and ghost-specific integration |
| Golem derivative | 35 | 25 | Spawn-only binding, coal and factory gates, foundry integration, pattern choices, and golem-specific sustainment |

The claimant package therefore meets the specification through 30 shared focus-scale pieces plus adapted decisions. Zombie, ghost, and golem packages meet it directly through 35 visible focus-scale pieces each.

## Graph, locks, and layout

Static graph checks found:

- 45 unique focus IDs and 45 unique focus icons
- one graph root, `infantry_spawn_derivative_hold_the_first_ground`
- 54 prerequisite connectors
- every prerequisite reference resolves to a focus in the tree
- every prerequisite connector moves downward to a later row
- no asymmetric mutual exclusion
- no duplicate coordinate pair
- coordinate bounds of `x = -6..44` and `y = 0..16`
- minimum same-row spacing of 3 columns
- all 45 focuses have `available`, `completion_reward`, and `ai_will_do`
- all 15 family focuses have a family-specific `allow_branch`

The three hierarchy roots are mutually exclusive and their descendants require the selected root. Claimant-only breakaways cannot enter the collective or species roots. The three military doctrine roots are mutually exclusive. `infantry_spawn_derivative_a_method_fit_for_the_host` correctly uses one prerequisite block containing all three doctrine focuses, which is an OR gate. Each family has one opener, three mutually exclusive identity outcomes, and one capstone using an OR prerequisite over those outcomes.

The source uses authored absolute positions. None of the 45 nodes uses `relative_position_id`. Static inspection found no duplicate coordinates, same-row crowding, backward connector, or disconnected focus. Coordinates were not mechanically converted without render evidence. Because MCP rendering was unavailable, connector crossings and resolution-specific visual continuity remain unavailable evidence rather than a source finding.

## Dynamic-country availability

All reviewed dynamic derivative creation routes converge on the same identity initializer before gameplay begins:

- natural claimant release calls `infantry_spawn_setup_claimant_breakaway_identity`
- natural family release calls `chaos_unit_family_provider_[PROVIDER]_event19_setup_derivative`
- scenario claimant takeover calls `infantry_spawn_setup_claimant_breakaway_identity`
- scenario anomalous rising calls `chaos_unit_family_provider_[PROVIDER]_event19_setup_derivative`
- provider 501 dispatches to `infantry_spawn_setup_zombie_derivative_identity`
- provider 502 dispatches to `infantry_spawn_setup_ghost_derivative_identity`
- provider 503 dispatches to `infantry_spawn_setup_golem_derivative_identity`

Each path reaches `infantry_spawn_setup_derivative_identity_common`, which establishes derivative identity and ideas and loads `infantry_spawn_derivative_focus_tree` with `keep_completed = no`. Family and claimant identity are established before the load, so one-shot `allow_branch` evaluation sees the intended derivative identity.

The focus tree itself has no fixed-tag dependency. Its country score and focus availability use dynamic derivative classifiers and package flags, so dynamically created derivatives receive the same package regardless of their temporary dynamic tag.

## Family differentiation

### Zombie

Provider 501 registers as `trainable_and_spawnable`, but exposes only the base `zombies` battalion. Its generated template contains four base-zombie battalions and starts locked with recruiting disabled.

`infantry_spawn_derivative_authorize_base_zombie_training_decision` requires zombie identity, the focus unlock, army experience, infantry equipment, manpower, and aligned ledgers. The authorization effect adds only family 501 to `infantry_spawn_trainable_family_ids` and enables recruiting only for the exact generated `Unbidden Muster [TEMPLATE_UID]` base-zombie template. No mutated or weaponized zombie token is registered or unlocked by the derivative package.

### Ghost

Provider 502 registers as `spawn_only`, exposes only `death_weak_ghost_host`, keeps its generated template locked, and reports that it cannot train. Reinforcement uses a paid manifestation action.

Slow decline is centralized in `infantry_spawn_derivative_apply_ghost_decline`. It runs only for an active ghost derivative after a 180-day cooldown and affects one eligible controlled state. The configured population fractions are 0.25 percent at base, 0.20 percent when anchored, and 0.15 percent when managed, with a 0.50 percent cap and a hard cap of 5,000 deaths. The effect makes one call to `chaos_meter_register_state_civilian_deaths_percent` with the Event 19 ghost-decline reason. The derivative pulse has one call site for this decline effect.

### Golem

Provider 503 registers as `spawn_only`, exposes the coal-golem battalion and `coal_golem_equipment_1`, keeps its generated template locked, and reports that it cannot train. Binding requires political power, command power, available civilian-factory capacity, coal-golem equipment, an eligible state, and aligned ledgers. The focus and decision package connects coal recovery, binding marks, workshops, foundries, material agreements, and foundry-district integration.

These are distinct reinforcement economies and state pressures, not localisation-only variations.

## Rewards, ideas, and AI

Focus durations are tuned in one file-scoped table at 3, 5, and 7 weeks. Rewards are mostly small political power, command power, army experience, war support, equipment, route transitions, and operation unlocks. The tree does not create free factories, annex countries, or issue global war goals.

The derivative idea file defines 42 ideas with complete title and description localisation. Four opening tracks are maintained:

1. diplomatic and command legitimacy
2. seized-district logistics
3. family or claimant burden
4. former-parent pressure

Route and doctrine effects replace ideas within those tracks instead of stacking permanent bonuses. Defeat swaps them into remnant penalties and final cleanup removes the derivative idea set. The 24 distinct modifier keys used by the ideas were checked against official modifier documentation or direct vanilla building-production precedents.

The AI file defines 22 dynamically enabled profiles. Every profile uses `abort_when_not_enabled = yes`. The nine strategy types used are documented vanilla strategy types. Route weighting distinguishes claimant concentration, collective resilience, species specialization, zombie quantity and training, ghost preservation and manifestation, and golem material and foundry priorities.

## Expansion and the weaker-than-parent rule

Expansion is aggressive after the survival and military sequence, but bounded:

- submission targets must be adjacent
- the derivative cannot start a new submission while already at war
- target size is limited to 1 through 12 controlled states
- special Chaos countries, actual nonhuman countries, other Event 19 derivatives, subjects, faction partners, capitulated countries, nonaggression partners, and already targeted countries are excluded
- submission uses a 21-day warning and a 90-day cooldown
- the regional-predator payoff requires a consolidated hierarchy, completed family or claimant transformation, sustainable reinforcement, resolved former-parent pressure, a regional foothold, 8 controlled states, and 2 recorded war victories

The package remains weaker than its source actors. It starts with material stability, political, consumer-goods, supply, organization, movement, or production burdens. It uses base zombies, weak ghost hosts, or a small coal-golem template rather than parent escalation units. Focus rewards are modest, expansion is regional, and no parent technology tree, focus tree, mutation system, Death economy, golem progression, or endgame package is copied.

## Defeat cleanup and focus closure

`on_capitulation` records derivative defeat and calls `infantry_spawn_derivative_handle_defeat`. `on_annex` guarantees defeat recording, then starts proof-gated final cleanup. Defeat closes the decision package, cancels derivative missions, cancels state and submission transactions, removes active route ideas, and applies remnant ideas. Final cleanup deletes or proves absent the tracked formations and templates before removing the remaining derivative package.

All focus branches close correctly at defeat. Shared focus availability gates require `infantry_spawn_derivative_package_is_active` either directly or through a narrow helper trigger. Family focuses use `infantry_spawn_derivative_is_zombie`, `infantry_spawn_derivative_is_ghost`, or `infantry_spawn_derivative_is_golem`, and each of those family triggers delegates to `infantry_spawn_derivative_package_is_active`. That active-package trigger rejects defeated and capitulated actors. The offline focus documentation also confirms that `cancel_if_invalid` defaults to true and `available_if_capitulated` defaults to false.

A transient cleanup omission was found during the audit. Final cleanup initially did not clear these actor-lifetime values:

- `infantry_spawn_derivative_release_report_dispatched`
- `infantry_spawn_derivative_defeat_report_dispatched`
- `infantry_spawn_derivative_release_mode`
- `infantry_spawn_derivative_release_nonce`

The active exact-transfer transaction owner applied the narrow cleanup fix in their owned file during this audit. Current source clears all four values. A current set comparison found 75 derivative-prefixed country flags set and all 75 cleared, plus 27 derivative-prefixed variables mutated and all 27 cleared. Both package-owned derivative arrays, `infantry_spawn_derivative_diplomacy_target_countries` and `infantry_spawn_derivative_owned_marker_states`, are also cleared. This audit did not duplicate or claim ownership of the transaction-owner edit.

## Parent isolation and terminal-route check

The common derivative initializer clears `infantry_spawn_participant`, parent evolution flags, management surfaces, and `infantry_spawn_country_stage`. Provider callbacks reuse only the registered unit tokens. They do not call Zombie Outbreak, Death, or Kuznetsk Mining Board country setup.

The derivative reinforcement transaction explicitly excludes ordinary evolution history. Its temporary stage tokens are private generation metadata, not parent progression. The natural-release transaction snapshots and restores global Event 19 progression counters and checks that they did not change.

No parent-stage setter, parent-participant setter, super-event call, parent focus-tree load, or terminal `world_end` setter was found in the reviewed derivative focus and linked package surface. `infantry_spawn_derivative_become_the_regional_predator` is the terminal focus and remains a regional payoff only.

## Localisation and asset seams

Current linked-content checks found:

- 45 focus titles, 45 focus descriptions, and 45 focus effect tooltips present
- 42 idea titles and descriptions present
- 26 decision or mission titles and descriptions present
- 114 unique linked tooltip or cost localisation references, all present
- 112 unique linked focus, focus-shine, decision, category, and idea sprite requests, all defined with existing texture files
- 45 distinct focus DDS files, all `100x88`
- no duplicate SHA-256 group among the 45 focus DDS files
- 45 processed focus PNGs and 45 split source PNGs present

## Tool evidence

Attempts to use `hoi4.focus_inspect` and `hoi4.focus_render` both returned `ARTIFACT_STORAGE_LIMIT` before any file was scanned. They returned no diagnostics, validation data, or render artifact. No MCP lint or layout claim is therefore included.

Static checks were used only as source evidence. MCP unavailability is recorded as unavailable evidence and not as an implementation failure.

## Files changed by this specialist

- `docs/plans/019_infantry_spawn_plans/subagent_handoffs/019_focus_tree_independent_specialist_audit_2026_07_16.md`

No gameplay, localisation, sprite, or asset file was edited by this specialist.

## Simplifications, omissions, and remaining risks

- No content simplification or fallback was introduced.
- No outstanding focus or linked derivative-package defect was found in current source.
- Visual connector crossings, node intersections, and multiple-resolution rendering remain unverified because the focus MCP tools were blocked before scanning.
- The tree intentionally retains its authored absolute coordinates. No relative-position rewrite was made without render evidence.
- This report does not claim overall Event 19 completion.

## Skill maintenance

Skills used: `hoi4-focus-trees`, `chaos-redux-events`, `chaos-redux-subagents`, `hoi4-decisions-missions`, and `chaos-redux-event-assets`.

No reusable workflow gap requiring a skill creation or skill update was identified in this bounded audit.
