# Repo Explorer Handoff

Disposition: implemented within the user's CXT template, dispersion, and manual-grant request. This report records the pre-change source inventory; the implemented 50-template static roster, two Event 014 formations, two Event 039 formations, and ten-battalion Event 016 cohort are documented in `docs/testing/chaosx_test_country.md` and their current scripted-effect files. Its gap and blocker lists are discovery findings, not unresolved current-state claims. Source-level coverage and compatibility audits were performed, but no agent-run live-game validation is claimed.

## Scope read

- Parent task: map real multi-battalion Chaos Redux division-template precedents for the CXT roster repair, including frontline and support coverage, current one-battalion/zero-battalion risks, and owned-state dispersal implications.
- Explicit constraints: read-only exploration; do not edit gameplay, assets, localisation, docs other than this requested handoff, or other agents' work; retain all Chaos Redux units and the three-division test count; report exact gaps and a safe implementation order.
- Files or ids requested: `common/scripted_effects/chaosx_test_country_unit_effects.txt`, CXT package registration helpers, Chaos-only `history/units` OOBs, and actual country/scripted `division_template` effects.
- Skills or docs read: `AGENTS.md`; `.agents/skills/chaos-redux-subagents/SKILL.md`; offline `Data structures`, `Triggers`, `Effects`, `Modifiers`, `Localisation`, `Scopes`, `On actions`, `Event modding`, `Decision modding`, `Idea modding`, `AI modding`, and `Division modding` wiki pages; vanilla `effects_documentation.md` and `triggers_documentation.md` under the installed Hearts of Iron IV `documentation` directory.

## Primary findings

- `common/scripted_effects/chaosx_test_country_unit_effects.txt` currently has 89 `unlock_subunit` calls, 89 `division_template` blocks, and 89 `create_unit` blocks. Its header at lines 4-9 explicitly says one recruitable template per static unit and three divisions from every template.
- Static CXT templates at lines 103-1799 are one combat regiment for ordinary units. Support entries are one anchor plus one support, mostly `chaos_battalion`; armored CBRN delivery entries use `autonomous_robot` as the armor-group anchor.
- Dynamic registration at lines 1814-1974 makes one template per registered frontline token or support token. The support helper only checks that the caller supplied an anchor token at lines 1840-1864; it does not verify the anchor is a valid combat group or that the generated template is nonempty. This is the confirmed zero-battalion/invalid-anchor risk.
- The strongest compact Chaos precedents already group complete families: rats, cave broods, Africa Strange, cannibal frontlines, and zombie variants. They provide a defensible small CXT roster while preserving every unlock and the existing `@CXT_TEST_UNIT_COUNT = 3`.
- All current CXT spawns use `capital_scope`; the vanilla `create_unit` documentation supports `prioritize_location`, `country_score`, and `count`, so the parent can replace capital-only spawning with an owned-state/province allocator while keeping three fully equipped divisions per selected template.

## Relevant files

| Path | Why it matters | Evidence |
| --- | --- | --- |
| `common/scripted_effects/chaosx_test_country_unit_effects.txt` | Current CXT roster, static unlocks, per-unit templates, dynamic registration, and spawn effects. | Lines 4-12 document the one-template/three-division contract; lines 103-1799 are the 89 static one-unit blocks; lines 1814-1865 register tokens; lines 1867-1929 create one template per token; lines 1931-1974 iterate processed arrays. |
| `common/scripted_effects/chaosx_test_country_effects.txt` | CXT setup and extension application order. | `chaosx_test_country_initial_setup` calls the static roster and extension sync; `chaosx_test_country_sync_registered_content_apply` calls the dynamic roster. |
| `docs/testing/chaosx_test_country.md` | CXT dynamic extension contract and support ownership rules. | Dynamic registration examples use token arrays; CBRN HQ/chemical/tank/Livens entries are support consumers and require a combat anchor, not support-only divisions. |
| `common/scripted_effects/002_zombie_outbreak_effects.txt` | Real mixed zombie runtime template. | `Mutated Zombie Muster [TEMPLATE_UID]` at lines 2554-2580 contains eight unarmored variants and three armored variants. `zombies` base is intentionally absent, so add the OOB precedent or keep a separate base-zombie template. |
| `common/scripted_effects/020_black_plague_effects.txt` | Real mixed rat runtime template. | `Rat Brood Muster [TEMPLATE_UID]` at lines 1957-1979 contains five rat combat types and `rat_tunnelers` support. |
| `common/scripted_effects/018_resources_found_cave_effects.txt` | Real mixed cave runtime template. | `Cave Brood Muster [TEMPLATE_UID]` at lines 2595-2615 contains all five cave combat types. |
| `common/scripted_effects/012_africa_effects.txt` | Real mixed Africa Strange runtime template. | `Africa Strange Formation Muster [TEMPLATE_UID]` at lines 2658-2684 contains five combat types and `pan_sappers`, `oracle_recon`, and `disaster_wardens` supports. |
| `common/scripted_effects/014_cannibalism_effects.txt` | Real mixed cannibal runtime template. | `Cannibal Irregular Muster [TEMPLATE_UID]` begins at line 19668 and includes one of each of the nine cannibal frontline tokens. |
| `common/scripted_effects/012_africa_elephant_effects.txt` | Real multi-battalion elephant template. | `Africa Charter Elephant Guard` begins at line 45 and has two `chaosx_elephant` regiments plus `recon` and `engineer` supports. |
| `common/scripted_effects/005_soviet_collapse_effects.txt` | Real multi-battalion coal-golem template. | `Coal Golem Column` begins at line 22199 and has four `coal_golem` regiments plus `engineer`. |
| `common/scripted_effects/010_death_effects.txt` | Real mixed death-host runtime template. | `Hollow Ghost Muster [TEMPLATE_UID]` begins at line 3737 and combines `death_hollow_ghost_host` and `death_last_shore_ghost_host`; `death_weak_ghost_host` remains a separate gap. |
| `common/scripted_effects/039_murder_mystery_event19_effects.txt` | Only real assassin-family runtime template found. | `Assassin Forces Muster [TEMPLATE_UID]` at lines 54-76 has three `assassin_cadre` and `saboteur_cell`; no mixed template covers `shadow_company`, `silent_guard`, `master_assassin`, and `mechanized_assassin`. |
| `common/scripted_effects/016_brilliant_scientist_project_force_effects.txt` | Event 016's actual family-specific multi-battalion templates. | `Quantum Transit Raiders` (6 `portal_raider`), `Replicated Guard Cadre` (10 `clone_infantry`), `Autonomous Robot Cohort` (5 `autonomous_robot`), `Paleogenetic Shock Pack` (5 `paleogenetic_creature`), `Xenobiological Assault Organisms` (6 `xenobiological_assault_organism`), and `Temporal Continuity Guard` (4 `temporal_guard`) are authored in this file. |
| `common/scripted_effects/016_brilliant_scientist_project_force_event19_effects.txt` | Event 016's dynamic provider templates. | The same six families plus `Aryan Clone Formation` have explicit 3-10 battalion runtime bodies; no cross-family template was found. |
| `common/scripted_effects/016_alien_infantry_api_effects.txt` | Shared alien-infantry special-case template. | `D’Rhondan Landing Cohort` is the accepted locked ten-battalion API template; it must not be replaced by a normal CXT recruitable roster entry. |
| `common/scripted_effects/016_alien_infantry_cxt_test_effects.txt` | CXT special alien registration. | Lines 116-131 register Event 016 frontlines; lines 134-165 mark seven ordinary static templates as processed; lines 167-190 intentionally create one locked one-line `CXT Test - Alien Landing Cohort` fallback for `alien_infantry`. |
| `common/scripted_effects/cbrn_doctrine_effects.txt` | CBRN runtime precedent. | `Chaos Warfare Assault Muster [TEMPLATE_UID]` at lines 753-770 has only one `chaos_battalion`, so it is not a multi-battalion grouping precedent. |
| `common/ai_templates/cbrn_regimental_support.txt` | CBRN grouped layout precedent, not a runtime template creator. | AI templates group three CBRN supports around 6 infantry + 3 `chaos_battalion`, or around armor/cavalry lines. Use only as a compatibility guide. |
| `common/units/cbrn_regimental_support.txt` | CBRN support compatibility and collision constraints. | All listed CBRN entries are `group = support`; armored deliveries require armor/mobile anchors; same-support-type fields limit how many offensive-delivery, flame, field-hospital, and related support families can share one template. |
| `common/units/cbrn_hq_support.txt`, `common/units/chemical_tank_support.txt`, `common/units/livens_projector_support.txt` | Remaining static support families. | HQ, chemical tank, and Livens entries are support-only and need a compatible line anchor; chemical/Livens entries share offensive-delivery compatibility constraints. |
| `common/units/020_black_plague_rat_units.txt` | Rat support compatibility. | `rat_tunnelers` at lines 217-227 is `group = support`, matching the mixed rat template. |
| `history/units/020_black_plague_rat_1936.txt` | Actual rat country OOB precedent. | `Rat Brood` (4 `rat_swarm`), `Rat Shock Brood` (3 `rat_swarm` + 3 `rat_brutes` + `rat_tunnelers`), `Rat Burrow Column` (4 `rat_burrowers` + `rat_tunnelers`), `Rat Carrion Guard` (4), and `Rat Dock Stowaways` (4 + `rat_tunnelers`) at lines 8-87. |
| `history/units/DHO_1936.txt` | Actual cave-country OOB precedent. | `Oth-Kesh War-Brood`, `Oth-Kesh Stone Phalanx`, `Oth-Kesh Burrow Column`, `Oth-Kesh Scree Pack`, and `Oth-Kesh Feeding Guard` at lines 14, 31, 48, 65, and 80 use 6-8 same-family cave battalions. |
| `history/units/DTH_1936.txt` | Actual death-country OOB precedent. | `Death Passive Host`, `Death Hollow Host`, and `Death Last Shore Host` at lines 2, 15, and 30 use 4/6/8 same-family ghost battalions. |
| `history/units/ZZZ_1936.txt`, `history/units/ZZZ_weaponized_1936.txt`, `history/units/ZZZ_weaponized_hardened_1936.txt` | Actual zombie-country OOB precedents. | `Brainzz Horde` and the Infected/Rabid/Parasitic/Mutant/Undead/Necrotic/Demonic/Wendigo hordes use 16 same-family zombie battalions; hardened OOBs use the three armored zombie variants. |

## Existing patterns

The current CXT static pattern is intentionally exhaustive but creates one template and one capital-spawn block for every unlocked ID. The static support blocks at lines 283-640, 805, 862-1457, 1495-1535, and 1699-1718 demonstrate the correct nonempty shape: one valid combat anchor plus one support company.

The extension bus is additive and de-duplicates token registration, but it has no family/template grouping metadata. Event 014 registers nine cannibal frontlines at `common/scripted_effects/014_cannibalism_cxt_test_effects.txt:23-40`; Event 016 registers eight Event 016 frontlines at `common/scripted_effects/016_alien_infantry_cxt_test_effects.txt:116-131`; Event 039 registers five assassins plus `saboteur_cell` at `common/scripted_effects/039_murder_mystery_cxt_test_effects.txt:22-35`. A compact redesign must either add an accepted family/group contract to these registrations or route package tokens through explicit grouped CXT builders; blindly retaining the one-token dynamic loop preserves the template explosion.

The CXT static baseline includes 18 CBRN/HQ support IDs, 18 chemical-tank variants, 7 Livens variants, three Africa Strange supports, and `rat_tunnelers`. These are not standalone frontlines. Keep them in grouped, anchored support templates and respect `group = support`, `allowed_battalion_groups`, and `same_support_type` constraints.

## Vanilla or reference precedents

- `paradox_wiki/Division modding - Hearts of Iron 4 Wiki.md:47-72` establishes that `regiments` are combat battalions, `support` is for support companies, support IDs must have `group = support`, and a template needs at least one valid combat regiment to avoid a support-only/empty formation.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md:3278-3308` documents `create_unit`, including `count`, `prioritize_location`, and `country_score`. It supports replacing CXT's `capital_scope` concentration with an owned-state/province scoring strategy, subject to parent verification of the exact scope and selector used.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md:2433-2452` documents `add_units_to_division_template` as a possible post-creation grouping/edit route, but direct explicit `division_template` blocks are clearer for CXT's fixed roster and easier to audit.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/triggers_documentation.md:2621,4905-4945` provides template existence and battalion-in-template checks for post-write validation.
- Chaos Redux's actual country OOB files above are the primary approved precedents. The runtime family builders listed in the table are stronger than the CXT one-unit pattern because they show the project already accepts compact mixed formations with real support slots.

## Likely edit order for the parent

1. Freeze an explicit coverage matrix before editing: every static CXT frontline, every package frontline, every support ID, its family template, its line anchor, and its allowed support slot. Mark `alien_infantry` as the locked API-owned exception and decide separately whether the CXT fallback remains.
2. Keep every `unlock_subunit` and equipment registration, but replace per-token template creation with a small set of explicit family builders modeled on `Rat Brood Muster`, `Cave Brood Muster`, `Africa Strange Formation Muster`, `Cannibal Irregular Muster`, and `Mutated Zombie Muster`.
3. Add the base `zombies` and weak death host to a deliberate family template or retain one small companion template each; do not claim complete family coverage while relying on templates that omit those IDs.
4. Preserve concrete multi-battalion Event 016 sizes and locked ownership: use family-specific six/ten/five/four-battalion patterns where the package or API requires them, and do not merge `alien_infantry` into normal recruitable templates.
5. Decide the assassin gap explicitly. The only existing template covers `assassin_cadre` + `saboteur_cell`; a compact CXT family builder must cover the other four assassin frontlines without inventing a source claim.
6. Replace `capital_scope` creation with a bounded owned-state/province allocator using the documented `create_unit` location/scoring fields. Ensure three units per grouped template are distributed across owned, controlled locations rather than all three in the capital; avoid unbounded world iteration.
7. Build CBRN, chemical-tank, Livens, Africa support, and rat-support groups only after checking each support's allowed battalion groups and `same_support_type`. Never create support-only templates. Validate every generated template has at least one `regiments` entry.
8. If existing saves must be migrated, identify exact legacy CXT template names first and propose a guarded cleanup/version path. Do not use broad template deletion. Take a save backup and record the recoverable rollback path before applying any cleanup.

## Validation checks

- Recount `unlock_subunit`, explicit `division_template`, and `create_unit` blocks in `common/scripted_effects/chaosx_test_country_unit_effects.txt`; the desired template count should be materially below 89 while all expected IDs remain unlocked and covered.
- Parse every new grouped template and assert at least one `regiments` entry, no support ID appears under `regiments`, and no combat ID appears under `support`.
- Cross-check all static IDs in lines 15-100 and all package registrations against the coverage matrix; specifically check `zombies`, `death_weak_ghost_host`, all five assassin frontlines, all Event 016 frontlines including `aryan_clone_infantry`, all CBRN/HQ entries, all 18 chemical-tank variants, all 7 Livens variants, Africa supports, and `rat_tunnelers`.
- Run duplicate-template-name and duplicate-subunit-in-template checks. Confirm dynamic package calls do not re-create names already handled by the grouped pass and that processed arrays or a replacement grouping registry are idempotent across daily sync.
- Use the vanilla template triggers (`has_template`, `has_template_containing_unit`, `division_has_battalion_in_template`) in source-level or game-owner validation to prove coverage and prevent an invalid anchor from generating an empty formation.
- Verify each support's `allowed_battalion_groups` and `same_support_type` against its chosen anchor/template. Armored CBRN delivery must stay on an armor-compatible anchor; no template may stack mutually exclusive offensive-delivery or duplicate support types.
- Audit all generated `create_unit` calls for `count = 3`, full equipment/manpower factors, and a bounded owned-state/province location strategy. Record the expected distribution across at least two owned states when the country owns that many states; document the single-state fallback.
- Re-run the exact source searches after edits and inspect any existing CXT setup cleanup path before declaring migration safe. Live-game validation remains the user's responsibility.

## Risks and blockers

Confirmed blockers:

- No real mixed assassin template covers `shadow_company`, `silent_guard`, `master_assassin`, and `mechanized_assassin`; a design decision or new owner-authored grouped template is required.
- No real runtime multi-template precedent covers the CBRN/HQ, chemical-tank, and Livens support families. The AI template files are compatibility guidance only, not proof that a runtime `division_template` is valid.
- `alien_infantry` is intentionally API-owned and locked in `D’Rhondan Landing Cohort`; changing it to a normal three-division CXT recruitment template would conflict with the Event 016 API contract. The one-line CXT fallback in `016_alien_infantry_cxt_test_effects.txt` needs an explicit parent decision if the user requires every token to have three ordinary CXT divisions.
- The existing support registration contract trusts the caller's anchor. A grouped rewrite must define how anchor compatibility and support-slot collisions are checked before template creation.

Ordinary risks:

- `Mutated Zombie Muster` omits base `zombies`; `Hollow Ghost Muster` omits `death_weak_ghost_host`; the compact set must cover these explicitly.
- The Africa elephant constants describe a one-battalion provider in `common/script_constants/012_africa_elephant_constants.txt`, while `Africa Charter Elephant Guard` has two elephant regiments. Parent should preserve the source template contract rather than silently infer a CXT size.
- Template cleanup on an existing save can destroy or strand units if old names are removed without a guarded migration. Dry-run exact-name inventory and save backup are required.
- `capital_scope` is a confirmed concentration point, but the exact state/province selector and deterministic distribution mechanism still need parent-side source validation before applying a change.

No focus, event, technology, weighted-logic, scripted-GUI, or map surface was in scope for this unit-roster exploration, so no HOI4 focus/event/technology/probability/GUI/map MCP inspection was applicable. Tool exposure or standalone viewer availability was not used as evidence for this task.

## Recommended next action

Adopt a small explicit coverage matrix and make the parent-owned CXT builder emit at least the real family groups for rats, caves, Africa Strange, cannibals, zombies, elephants, coal, and death, then add explicit decisions for assassin, CBRN/chemical/Livens, and Event 016 special ownership. Preserve three divisions per grouped template, validate one-or-more combat lines and support compatibility, and only then replace capital-only spawning with an owned-state distribution pass.

Proposed write process (not performed by this explorer): dry-run a generated coverage/name/count report and legacy-template inventory; parent review the matrix and accepted exceptions; apply the gameplay change in one bounded pass; post-validate counts, coverage, anchors, support constraints, idempotence, and owned-state placement; retain a save/source backup and exact-name recovery path for any migration cleanup. The only file written by this explorer is this handoff report.
