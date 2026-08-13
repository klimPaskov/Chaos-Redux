# Event 019 derivative focus-tree specialist re-audit

**Date:** 2026-07-16  
**Role:** focus-tree specialist re-audit  
**Mode:** audit-only; this specialist made no gameplay, localisation, asset, workbook, or specification edits  
**Audited package:** the live, stabilized Event 019 derivative focus package and its directly coupled ideas, decisions, AI, cleanup, isolation, art, localisation, and registry boundaries

## Verdict

The stabilized derivative focus package is clean.

- **P0:** 0
- **P1:** 0
- **P2:** 0
- No simplification or fallback was accepted for this focus-package scope.
- This verdict does not clear the two external approval blockers recorded below and does not claim that all of Event 019 is complete.

## Live re-audit remediation verified

The final snapshot includes and passes re-audit for four corrections made while this audit was active:

1. `Ghost: Thin the Hunger for Life` now discloses its Stability reward.
2. Both player-facing former-parent resolution paths now disclose the `Outward Muster` idea they grant.
3. The three unintended, consumerless focus markers and their redundant cleanup sites were removed:
   - `infantry_spawn_derivative_captured_workshops_open`
   - `infantry_spawn_derivative_doctrine_choice_open`
   - `infantry_spawn_derivative_military_method_complete`
4. The claimant-wrapper Regional Predator boundary was closed with `infantry_spawn_derivative_has_regional_territorial_foothold`, including matching focus availability, runtime validation, and player-facing localisation.

The final focus source sets 31 derivative focus flags. Every one has a live consumer and a final-cleanup clear. None of the three removed markers remains anywhere in the focus or package-effect source.

## Focus graph, visibility, and route reachability

The balanced-block graph audit found:

- 45 unique focus nodes: 30 shared, five zombie, five ghost, and five golem.
- 35 visible nodes for each zombie, ghost, and golem derivative; the family-none claimant wrapper sees the intended 30 shared nodes.
- One root: `infantry_spawn_derivative_hold_the_first_ground`.
- 44 prerequisite blocks containing 54 valid focus references.
- Five multi-reference OR merges: the shared hierarchy merge, shared doctrine merge, and one family capstone merge for each of zombie, ghost, and golem.
- Zero missing references, zero directed cycles, and zero raw coordinate collisions.
- 15 mutual-exclusion blocks containing 30 references, forming five symmetric three-way commitment groups. There are no asymmetric mutex references.
- Every focus has an icon, an `available` block, a completion reward, a custom effect tooltip, and `ai_will_do`.

The route commits, downstream availability checks, and OR merges agree. A zombie, ghost, or golem actor can complete 25 of its 35 visible nodes after choosing one hierarchy route, one doctrine, and one family transformation. Each family capstone remains reachable from either permitted non-claimant transformation as well as the claimant-shaped transformation when that route is selected.

## Claimant-wrapper adapted equivalents

The family-none claimant wrapper is no longer stranded at the shared Regional Predator capstone:

- `infantry_spawn_derivative_family_transformation_is_complete` accepts the claimant continuity decision plus consolidated claimant command as the family-transformation equivalent.
- `infantry_spawn_derivative_sustainable_reinforcement_is_established` accepts claimant reinforcement activity, including an established sustainment district.
- `infantry_spawn_derivative_has_regional_territorial_foothold` accepts either one integrated family district or, specifically for `infantry_spawn_claimant_breakaway`, one established sustainment district.
- Both `infantry_spawn_derivative_become_the_regional_predator` availability and `infantry_spawn_derivative_check_regional_predator` use that same territorial-foothold trigger.
- The Regional Predator tooltip explicitly tells the player that an established claimant sustainment district is the adapted alternative to an integrated family district.

The claimant wrapper therefore has an adapted equivalent at every family-shaped capstone gate without being given a species-specific district-integration operation.

## Rewards, tooltips, and family distinctness

- All 45 focuses have dedicated title, description, and tooltip localisation keys, with no missing or duplicate key in that set.
- Reward tooltips disclose the material effects checked in this audit. The live corrections above close the Stability and `Outward Muster` disclosure gaps found during the initial pass.
- Reward values and AI weights use the existing Event 019 constants rather than new focus-local magic values.
- Zombie content centers on scavenged equipment, band counting and training, hunger discipline, and base-dead consolidation.
- Ghost content centers on anchors, additional manifestations, binding to place, thinning dependence on life, and a pale dominion.
- Golem content centers on recovered coal, binding marks, captured foundries, shared living patterns, and a march of living stone.
- The family packages use distinct effects, decisions, idea progression, writing, and authored art rather than renamed copies of one shared reward package.

## Four idea tracks and lifecycle

The idea source defines 42 unique ideas, all with localized names and descriptions.

- Package setup installs exactly four opening burdens: government/recognition, logistics, former-parent pressure, and the claimant or family command burden.
- Route helpers replace the government and family-command tracks with claimant, collective, species, zombie, ghost, or golem identities as appropriate.
- The logistics helper removes every candidate in that slot before installing exactly one doctrine/sustainment state. Taking sustainment before or after doctrine neither stacks duplicate logistics ideas nor leaves the slot vacant.
- Resolving former-parent pressure replaces its burden with `Outward Muster`; Regional Predator replaces `Outward Muster` in the same track.
- Defeat removes the 35 possible active-package ideas, then installs four remnant tracks: hunted, scattered, encircled, and the claimant/zombie/ghost/golem-specific remnant.
- Proof-gated final cleanup removes the seven possible defeat ideas as well as the complete active set, covering all 42 definitions.

No fourth-track gap, stacking gap, defeat gap, or annex-cleanup gap remains.

## Decisions, missions, reinforcement, expansion, and AI

- The derivative decision file contains 26 entries: 23 actionable decisions and three timed missions.
- Every actionable decision has visibility, availability, a completion effect, and `ai_will_do`.
- All three timed missions have activation, availability, cancellation trigger/effect, and timeout effect flows.
- The decision category is derivative-scoped, remains visible when empty, and is load-safe with `allowed = { always = yes }`.
- All 45 focuses have route- or state-aware `ai_will_do` logic.
- The AI strategy file contains 22 profiles and 51 strategy entries; every profile has `abort_when_not_enabled = yes`.
- Family reinforcement and sustainment decisions feed the shared sustainable-reinforcement trigger. Family district operations feed the territorial ledger, while the claimant wrapper uses its sustainment-district equivalent.
- War victories are recorded through the derivative capitulation path. The recurring derivative pulse rechecks Regional Predator ambition without a global daily or monthly country scan.

## Icons, shine sprites, and localisation

- The focus source references 45 unique dedicated focus icons.
- `interface/019_infantry_spawn.gfx` contains exactly one matching base sprite and one matching `_shine` sprite for every focus icon.
- Every shine uses the same authored texture as its base sprite and `gfx/FX/buttonstate.lua`.
- All 45 referenced DDS files exist, have a valid DDS header, and are 100 x 88 pixels.
- The Event 019 focus contact sheet was visually inspected. Shared art is individually authored, while the zombie, ghost, and golem modules remain immediately distinguishable through subject, silhouette, and palette.
- `localisation/english/019_infrantry_spawn_l_english.yml` remains UTF-8 with BOM (`EF BB BF`).

## Defeat, annex cleanup, and isolation

- Defeat closes the active package and decision surfaces, cancels integration/submission state, removes all three missions, removes active ideas, and installs the four-track remnant package.
- Annex cleanup remains exact-set and proof-gated behind derivative formation/template removal. Only after proof does it remove all ideas and missions and clear focus flags, route/family variables, state markers, ledgers, and category state; a failed proof keeps the retry path alive.
- The derivative package is gated by both derivative identity and parent-isolation triggers.
- Setup scrubs parent Event 019 runtime state before activating the derivative package.
- No audited derivative focus, idea, decision, AI, on-action, effect, or trigger path advances the parent Event 019 evolution chain, parent news/super-event flow, or a world-end branch.
- The derivative recurring loop is a delayed country event that stops after defeat; it is not a whole-world daily, weekly, or monthly scan.

## Registry invariant

The exact repository invariant is satisfied:

- The sole Event 019-dedicated registry code file is `common/scripted_effects/019_infantry_spawn_unit_registry_effects.txt`.
- Event 019 registry constants remain in the existing Event 019 script-constant files.
- Event 019 registry triggers remain in `common/scripted_triggers/019_infantry_spawn_triggers.txt`.
- Provider registrations remain in their parent on-actions, each once:
  - provider 501 in `common/on_actions/002_zombie_outbreak_on_actions.txt`
  - provider 502 in `common/on_actions/010_death_on_actions.txt`
  - provider 503 in `common/on_actions/005_soviet_collapse_on_actions.txt`
- No second Event 019 registry code file exists.

## External approval blockers, not focus defects

These remain blocked on an exact engine contract or explicit fallback approval and are not counted against the focus-package verdict:

1. Exact ownership transfer of the recorded loyal formations during natural derivative release. A recreate/delete substitute has not been approved.
2. Four exact same-battle achievement contracts. The available script surface does not yet prove the required battle/division identity atomically, and a controlled-trial substitute has not been approved.

## Final source snapshot

The principal audited files had these SHA-256 hashes after the live corrections:

| Surface | SHA-256 |
| --- | --- |
| `common/national_focus/019_infantry_spawn_derivative_focus.txt` | `5891F641B66B2C23F33C52C6727294F2C8F88F259034D5A3A445517A35A0A04C` |
| `common/ideas/019_infantry_spawn_derivative_ideas.txt` | `82E0B7AD00EA9A7E1281DA92E694D5E20EF9BCD4A1D9EB32CA4A25CB7ED180BF` |
| `common/scripted_effects/019_infantry_spawn_derivative_package_effects.txt` | `4A8F3698C79E8667C065ED588F3D5409F308039ECD9552CA38A732A1EC9B2D75` |
| `common/scripted_triggers/019_infantry_spawn_derivative_package_triggers.txt` | `FEFFA864E1198273C93605138AE9DE8519C58ADC3767CD63DC9163056F1B5214` |
| `common/decisions/019_infantry_spawn_derivative_decisions.txt` | `644566ADF9DAADB672C61518495F8BD85749611BF3AC38E2BF7875E1FAC92058` |
| `common/ai_strategy/019_infantry_spawn_derivative_ai_strategy.txt` | `46D73696FD88CF7DCF01C8CB1BB746054A67BB1195C7C8EA3DD8D75F5EA14943` |
| `interface/019_infantry_spawn.gfx` | `C75168AB4496D8FD6103245915628DAB218E3392BE78EFCCDEA5B043BA060DDE` |
| `localisation/english/019_infrantry_spawn_l_english.yml` | `0A3ABCD47618134083909163FFD8B2133ECC17401C3F6658088E18B49D023E49` |
| `common/scripted_effects/019_infantry_spawn_unit_registry_effects.txt` | `AEB58CFC5DA2B7AF6C2058D6370B613DD9B3919AF591530C7E4966CEE791BD72` |

## References used

The audit consulted the required offline wiki snapshot pages for data structures, triggers, effects, modifiers, localisation, scopes, on-actions, events, decisions, ideas, and AI, plus the national-focus, AI-focus, graphical-asset, achievement, country-creation, and division-modding pages.

It also consulted the corresponding official vanilla documentation under `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation`, including focus, idea, event, effect, trigger, and script-constant documentation, and compared the package with vanilla national-focus, AI-strategy, idea, decision, and mutual-exclusion precedents. The installed HOI4 MCP domain tools were not exposed in this specialist session, so this was a read-only source/contract audit rather than an MCP render pass.

## Handoff and changed files

This specialist created only this handoff:

- `docs/plans/019_infantry_spawn_plans/subagent_handoffs/019_focus_tree_specialist_reaudit_2026_07_16.md`

No files were staged or committed.

Skills used: `chaos-redux-subagents`, `chaos-redux-focus-trees`, and `chaos-redux-events`. No skill was created or updated.
