# Event 019 derivative focus tree — final live-source independent audit

Date: 2026-07-16  
Auditor: `chaosx_focus_tree_auditor` route  
Audited tree: `common/national_focus/019_infantry_spawn_derivative_focus.txt`

## Verdict

**PASS — P0: 0, P1: 0, P2: 0.**

This verdict is based on the final live files, including the route-lock and claimant-identity corrections made during this audit. I did not treat earlier handoffs as proof. The only file written by this audit is this report; no gameplay, localisation, interface, or asset source was edited by the auditor.

The live tree contains 45 unique focuses: 30 shared focuses plus five zombie, five ghost, and five golem focuses. Each family therefore sees 35 focus-scale pieces. A brace-aware graph pass found one root, 45/45 nodes reachable from that root, no missing focus references, no asymmetric mutual exclusions, and no duplicate coordinates. Every focus has an icon, `available`, `completion_reward`, a unique custom reward tooltip, and `ai_will_do`.

## Findings and closure

No open severity finding remains.

Two defects were found against the pre-correction live snapshot and corrected by the parent before this final pass:

1. Six family transformation focuses could cross from collective to species outcomes or vice versa. The final source now gates the complete three-by-three matrix exactly: zombie species/collective/claimant at `common/national_focus/019_infantry_spawn_derivative_focus.txt:672`, `:695`, and `:716`; ghost at `:783`, `:804`, and `:825`; golem at `:892`, `:913`, and `:934`.
2. An existing claimant UID could pass the claimant focus gate after its character ceased to exist, allowing an irrevocable hierarchy focus to complete without installing a route. The final trigger requires aligned claimant ledgers, no invariant failure, and an exact live male army leader with the recorded UID at `common/scripted_triggers/019_infantry_spawn_derivative_package_triggers.txt:35-62`. The transaction repeats the same unit-leader, army-leader, male, and UID proof at `common/scripted_effects/019_infantry_spawn_derivative_package_effects.txt:319-334` and uses it in the claimant preparation transaction at `:6301-6372`.

## Focus graph and route proof

- Tree ownership is restricted to Event 019 derivative countries by the zero base score and derivative-only score modifier at `common/national_focus/019_infantry_spawn_derivative_focus.txt:15-29`.
- The file declares its 30 shared plus 3×5 structure at `:5-12`; the live parse confirms those exact counts.
- Opening survival has a single root at `:35-53`. All later nodes connect to it through valid prerequisites. The three hierarchy entries and their symmetric mutexes are at `:136-273`.
- The hierarchy join is an intentional OR prerequisite at `:442`; the doctrine choice and join are at `:454-530`. The three family modules and their route-locked, symmetric three-way transformations are at `:643-966`.
- Each family capstone accepts any one of that family's mutually exclusive transformation outcomes, so no selected route creates an orphaned capstone: zombie `:729-752`, ghost `:837-861`, and golem `:946-966`.
- The Regional Predator capstone is not granted from a route label. It requires an active package, consolidated hierarchy, completed family transformation, sustainable reinforcement, resolved former-parent pressure, territorial foothold, eight controlled states, and two recorded war wins at `:611-636`.
- There are no `bypass`, `bypass_if_unavailable`, `cancel`, `cancel_if_invalid`, or `continue_if_invalid` keys in the 45 focus blocks. Thus no focus can be silently marked complete without its reward, and normal engine invalidation cancels an in-progress focus when `available` becomes false. This matches the offline National Focus Modding reference at `paradox_wiki/National focus modding - Hearts of Iron 4 Wiki.md:303-322`.

No dead or unreachable node remains. Route mutexes remove only alternatives, and every downstream join uses the correct OR form documented at `paradox_wiki/National focus modding - Hearts of Iron 4 Wiki.md:234-245`.

## Rewards, localisation, and focus art

- All 45 `completion_reward` blocks contain a distinct `custom_effect_tooltip`; the source spans `common/national_focus/019_infantry_spawn_derivative_focus.txt:35-966`. Rewards are not copied placeholders: they select route transactions, swap lifecycle ideas, unlock priced decisions, set doctrine/family state, or grant route-appropriate bounded resources.
- All 45 focus titles, 45 descriptions, and 45 reward tooltip keys are present in `localisation/english/019_infrantry_spawn_l_english.yml:880-1060`. Their visible strings are distinct, and the file has the required UTF-8 BOM.
- Each focus icon has both its exact base sprite and `<icon>_shine` sprite in `interface/019_infantry_spawn.gfx:204-383` and `:657-702`. All 45 referenced DDS files exist under `gfx/interface/goals/019_infantry_spawn/`; the 45 files have 45 distinct SHA-256 hashes and consistent 100×88 dimensions. Base and shine definitions resolve to the same intended focus texture, matching the offline focus-art contract at `paradox_wiki/National focus modding - Hearts of Iron 4 Wiki.md:267-273`.

## Linked ideas, decisions, AI, and expansion

- The derivative idea file defines 42 unique ideas with complete name/description localisation (84/84 keys) and eight valid idea picture sprites/textures. Opening burdens and route swaps are defined at `common/ideas/019_infantry_spawn_derivative_ideas.txt:13-278`; doctrine, sustainment, and outward stages at `:281-376`; defeated remnants at `:379-444`.
- The decision package contains 26 unique decisions/missions with 52/52 name/description keys, 69/69 referenced tooltip/cost keys, and 14/14 valid decision icon sprites/textures. The category is derivative-only at `common/decisions/categories/019_infantry_spawn_derivative_decision_categories.txt:10-24`.
- Every focus has a nonzero `ai_will_do`. Nineteen self-removing dynamic-country AI profiles cover opening survival, the three hierarchy routes, governance policies, and all three families at `common/ai_strategy/019_infantry_spawn_derivative_ai_strategy.txt:9-252`.
- Continuing expansion is bounded and target-safe. The warned submission decision selects only neighbors passing the ordinary-country target contract at `common/decisions/019_infantry_spawn_derivative_decisions.txt:535-585`; the target trigger excludes special, nonhuman, derivative, protected, faction, puppet, oversized, and otherwise invalid actors at `common/scripted_triggers/019_infantry_spawn_derivative_package_triggers.txt:406-423`. Successful warning completion creates a finite annex war goal at `common/scripted_effects/019_infantry_spawn_derivative_package_effects.txt:6896-6931`. Conquest exposes the next ordinary neighbor, so the same mechanism continues through reachable ordinary countries without a global-country target sweep.
- Route tone remains intentional rather than uniform: collective and preservation profiles retain moderate restraint, while species primacy releases aggression once the outward campaign is ready at `common/ai_strategy/019_infantry_spawn_derivative_ai_strategy.txt:55-131`. Claimant profiles emphasize army growth and operational reserves at `:31-53`. This matches `docs/specs/019_infantry_spawn_specs/matrices/019_ai_strategy_matrix.md:88-125`.

## Country identity, relative strength, and parent isolation

- Region is frozen from one of seven valid continents at `common/scripted_effects/019_infantry_spawn_derivative_package_effects.txt:176-209`; base and claimant/collective/species cosmetic identities are selected at `:215-317`.
- The scripted localisation maps all seven region tokens and all 13 identity tokens at `common/scripted_localisation/019_infantry_spawn_scripted_localisation.txt:381-408`. The live matrix has all 91 cosmetic tags, all 1,365 required generic/DEF/ADJ and ideology name keys at `localisation/english/019_infrantry_spawn_l_english.yml:1641-3107`, and all 273 full/medium/small flag files.
- Species commanders and collective councils are family-specific and use all six wired leader names and portraits at `common/scripted_effects/019_infantry_spawn_derivative_package_effects.txt:385-453`. Each sprite is defined and its texture exists.
- Derivatives remain materially weaker than their parent phenomena. Only base zombies can become trainable, and the provider explicitly excludes mutated or weaponized zombie battalions at `common/scripted_effects/019_infantry_spawn_unit_registry_effects.txt:4179-4237`. Ghosts and golems are spawn-only and pay political/command/equipment or factory-gate costs at `:4415-4466` and `:4642-4698`. Every paid formation is also subject to the shared derivative reinforcement cooldown at `common/scripted_effects/019_infantry_spawn_derivative_package_effects.txt:5940-6005`. The late capstone grants a bounded regional spirit, not a parent-event terminal power, at `common/ideas/019_infantry_spawn_derivative_ideas.txt:359-376`.
- Ordinary Event 019 management, claimant, evolution, and Muster Board state is removed whenever derivative runtime is established at `common/scripted_effects/019_infantry_spawn_derivative_package_effects.txt:75-170`. Derivatives are explicitly excluded from ordinary evolution history and counter membership at `common/scripted_triggers/019_infantry_spawn_triggers.txt:44-64`. Global manifestations close into their private ledger and immediately clear ordinary runtime at `common/scripted_effects/019_infantry_spawn_derivative_package_effects.txt:5811-5861`.
- A negative scan of the linked focus, idea, decision, AI, on-action, trigger, and derivative-effect sources found no world-ending flag, terminal route, super-event call, or grant of ordinary evolution/participant state. The only derivative country events are the scoped release/defeat reports at `common/scripted_effects/019_infantry_spawn_derivative_package_effects.txt:744-767` and `:7176-7195`.

## Ghost decline and lifecycle cleanup

- Ghost decline is slow, bounded, and auditable: a 180-day interval with base/anchored/managed fractions, minimum, maximum, and hard cap is centralized in `common/script_constants/019_infantry_spawn_derivative_package_constants.txt:209-222`. Each interval affects only one valid controlled populated non-impassable state, registers the exact `Deaths` reason, uses the shared death effect, and reapplies its cooldown at `common/scripted_effects/019_infantry_spawn_derivative_package_effects.txt:6939-6969`.
- Capitulation records the winner and applies defeat state; annexation routes the losing derivative through provider cleanup and exact tracked-formation proof at `common/on_actions/019_infantry_spawn_derivative_on_actions.txt:70-112`. The ROOT/FROM scopes match the official on-action contract and the vanilla precedent in `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/on_actions/09_aat_on_actions.txt:2411-2420`.
- Defeat closes active missions/ideas and installs only the appropriate remnant package at `common/scripted_effects/019_infantry_spawn_derivative_package_effects.txt:7040-7197`. Exact recorded formations and state/private ledgers are removed only after proof at `:7199-7345`.
- Final cleanup removes all derivative and ordinary runtime ideas/missions, drops the cosmetic tag, clears identity/route/expansion/decline flags and variables, and marks cleanup complete at `:7347-7509`. Annex cleanup retries instead of committing partial cleanup when formation proof fails at `:7511-7540`.

## Tooling limitation

The required HOI4 MCP focus inspect and render calls were attempted against the live tree. Both returned `ARTIFACT_STORAGE_LIMIT` before scanning a file or creating an artifact. This is a renderer-storage limitation, not a source diagnostic; no MCP output was used to replace live-source inspection. The independent graph, localisation, sprite, texture, identity, and lifecycle checks above operated directly on the final repository files.

## Scope integrity

The audit found no simplification, omitted route, missing linked surface, or unresolved blocker. The controlled one-formation combat trials and exact recorded-formation recreate/prove/delete method remain the approved substitutes; this audit did not broaden either mechanism.

Skills used: `chaos-redux-focus-trees`, `chaos-redux-events`, and `chaos-redux-subagents`. No skill was created or changed.
