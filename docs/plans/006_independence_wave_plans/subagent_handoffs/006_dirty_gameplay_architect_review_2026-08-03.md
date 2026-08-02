# Event 006 dirty gameplay tranche - scripted-system architecture audit

Date: 2026-08-03.

Scope: read-only review of the current dirty Event 006 gameplay tranche, with emphasis on `events/006_independence_wave*.txt`, `common/decisions/006_independence_wave*.txt`, `common/decisions/categories/006_independence_wave*.txt`, `common/scripted_effects/006_independence_wave*.txt`, `common/scripted_triggers/006_independence_wave*.txt`, `common/ai_strategy/006_independence_wave*.txt`, Event 006 character and country-leader definitions, ideas, and localisation.

No gameplay file was edited by this subagent. The only file added by this subagent is this handoff.

## References consulted

- `AGENTS.md` and the required Chaos Redux event, decision/mission, and subagent skills.
- `paradox_wiki/Character modding - Hearts of Iron 4 Wiki.md`, especially the static recruitment restriction for `common/characters` entries and the country-history requirement.
- `paradox_wiki/AI modding - Hearts of Iron 4 Wiki.md`, including `equipment_production_factor`, `equipment_production_min_factories`, and `equipment_production_min_factories_archetype` identifiers.
- The offline data structures, triggers, effects, modifiers, localisation, scopes, on-actions, event, decision, idea, and AI wiki snapshots.
- Vanilla `documentation/effects_documentation.md`, `documentation/triggers_documentation.md`, `documentation/script_concept_documentation.md`, `common/script_constants/documentation.md`, and vanilla `common/units/equipment/trains.txt`.

## Findings

### 1. Character recruitment source must stay explicit

The offline Character modding page says static character definitions in `common/characters` need recruitment in `history/countries/TAG*.txt`, and that recruitment cannot take place outside country history. The vanilla effects documentation separately confirms that the runtime `recruit_character` effect is valid in country scope, so a hidden country event is a legal runtime path.

At the latest shared-worktree snapshot, `events/006_independence_wave.txt` still contains the runtime recruitment paths in `chaosx.nr6.10` (lines 167-193) and `chaosx.nr6.350` (lines 210-306). There are 40 `recruit_character` lines in those two hidden events, including route-conditional CHU, ASY, and SOK roles. Their callers validate package-specific `has_character` rosters before publishing package success.

An earlier dirty snapshot contained `history/general/006_independence_wave_character_recruitment.txt` with 35 direct `recruit_character` lines for SCO, WLS, RHI, BAY, AJX, COR, HAW, FSM, FIJ, CHU, ASY, DOX, and SOK. That path is not present in the current worktree, has no current status or history entry, and must not be recreated as a static startup source. If characters are ever moved out of the hidden events, they must be recruited in each owning `history/countries/TAG*.txt` file, with route-conditional roles still added at runtime. Keep one authoritative recruitment source per character to avoid duplicate or order-sensitive ownership.

The affected roster gates include `has_independence_wave_sco_advisor_roster`, `has_independence_wave_wls_advisor_roster`, Pacific HAW/FSM/FIJ leadership triggers, the COR/ARX/ASX Mediterranean roster triggers, the AJX Saar roster trigger, the MNT command roster trigger, and the IW093/IW098 DOX/SOK roster triggers. A missing authoritative recruitment source makes those gates fail closed.

### 2. AI train strategy semantic check

The latest shared-worktree snapshot retains the original train strategy type and identifier on all 24 changed train lines and only replaces file-local `constant:` values with file-scoped `@CR_SC_*` mirrors. The 24 lines are distributed as follows: Brittany 2, Generic 1, IW043/IW058 6, IW093/IW098 2, Mediterranean 3, Pacific 1, Rhineland/Bavaria 2, Rival Bloc 2, Scotland/Wales 3, and Wallonia/Frisia 2.

During an intermediate dirty snapshot, the same family of lines was transiently changed to `equipment_production_min_factories_archetype id = train_equipment`. That form is syntactically documented and `train_equipment` is a vanilla archetype, but it is not behavior-equivalent to either `equipment_production_factor id = train` or `equipment_production_min_factories id = train`: it changes weighted production priority or type-level minimum factories into an archetype-level minimum-factory rule. The latest snapshot no longer carries that conversion, but the final diff should be rechecked before commit so it does not reappear.

### 3. Three new decision categories lack automatic descriptions

The three new category files omit an explicit `desc`, so HOI4 will look for the conventional `<category_key>_desc` localisation key. A scoped localisation scan found these missing keys:

- `common/decisions/categories/006_independence_wave_catalonia_categories.txt` defines `independence_wave_cat_industrial_compact_category`, but `independence_wave_cat_industrial_compact_category_desc` is absent.
- `common/decisions/categories/006_independence_wave_evolution_incident_categories.txt` defines `independence_wave_evolution_incident_category`, but `independence_wave_evolution_incident_category_desc` is absent.
- `common/decisions/categories/006_independence_wave_montenegro_categories.txt` defines `independence_wave_mnt_mountain_compact_category`, but `independence_wave_mnt_mountain_compact_category_desc` is absent.

The existing modified categories retain their conventional description keys, and the repository's duplicate category-definition pattern across `common/decisions` and `common/decisions/categories` is established elsewhere. Add the three missing descriptions or restore an explicit `desc` field before claiming localisation closure.

### 4. Character role removals are structurally plausible but need route validation

The current character edits remove some oligarchism or centrism role combinations from COR/ARX/ASX, AJX, AFX/AGX, and DOX entries. The corresponding route effects promote a remaining role and use `set_country_leader_ideology` for patron or neutral outcomes. Vanilla documentation describes that effect as changing the active leader's ideology, so the role split is structurally valid, but route-specific leadership and date checks were not run in-game. The parent should verify each promotion path still has an active role and that no trigger requires the removed role token directly.

## Scripted-system architecture disposition

### Helper map

- Existing package setup effects in `common/scripted_effects/006_independence_wave_*_package_effects.txt` select a package, invoke `chaosx.nr6.10` or `chaosx.nr6.350`, and publish setup flags only after roster checks.
- Existing package roster triggers in `common/scripted_triggers/006_independence_wave_*_package_triggers.txt` read `has_character` and role/date assertions. Their outputs are boolean acceptance gates; they should remain the single validation surface rather than duplicating character lookup in decisions.
- No new generic helper is warranted by this tranche. Character IDs are static tokens, and dynamic injection through a meta effect would increase surface area without reducing the current package-specific route conditions.

### Constants and tuning table plan

The dirty tranche adds file-scoped `@CR_SC_*` mirrors where fields reject shared script constants. A static check over the Event 006 gameplay surfaces found no duplicate definition within a file, no unresolved same-file use, and no forbidden `<=` or `>=` operators. Keep the authoritative values in `common/script_constants/` and retain file-local mirrors only where the target field rejects `constant:` syntax.

### Event target and cleanup plan

The roster handoff uses country scope, flags, and character state; it does not need a new event target. Existing Event 006 event-target cleanup remains separate from character recruitment and must not be replaced by a broad cleanup helper. If a future implementation introduces a global recruitment target, it must add an explicit clear path; no such target is needed for the current package events.

### Migration plan

1. Preserve one valid recruitment source for every package character, preferably the existing hidden country events for route-conditional roles.
2. If startup recruitment is required for a static role, place it in the owning country history file and remove the duplicate event source only after all roster and role gates have an equivalent path.
3. Re-scan all package roster triggers after any recruitment move, including SCO/WLS/RHI/BAY/AJX, COR/ARX/ASX, HAW/FSM/FIJ, MNT, CHU/ASY, and DOX/SOK.
4. Add the three missing category description keys and re-run the category localisation scan.
5. Re-run a normalized AI diff to confirm every train line still uses its intended original strategy type and identifier.

## Validation performed

- Read-only scoped source inspection of the Event 006 event, decision, scripted-effect, scripted-trigger, AI, character, country-leader, idea, and localisation surfaces.
- Counted 40 current runtime `recruit_character` lines in `events/006_independence_wave.txt` and confirmed the previously observed `history/general/006_independence_wave_character_recruitment.txt` file is absent from the current worktree.
- Normalized the current AI diff and counted 24 train-line pairs across the ten files listed above.
- Checked the three new decision category keys against all localisation files and found the three missing `_desc` keys listed above.
- Ran a scoped forbidden-operator scan; no `<=` or `>=` hits were found.
- No Clausewitz parser, HOI4 launch, live save, or weighted-AI simulation was run because the repository instructions reserve in-game validation for the user.

## Safe-to-commit status

This handoff is safe to commit as documentation. The gameplay tranche itself is not ready for a final completion claim until the parent confirms the recruitment source remains authoritative, the three category descriptions are supplied, the final AI diff has no unintended train-archetype conversion, and the removed character roles are checked against all route promotion gates.

## Limitations and follow-up

The audit did not patch gameplay, did not invoke a Clausewitz parser, and did not run live gameplay or AI simulation. The earlier `history/general` finding is preserved as a stale-state warning because that file is absent now; no fallback recruitment path was introduced. The parent owns any gameplay edits, localisation additions, and final validation.
