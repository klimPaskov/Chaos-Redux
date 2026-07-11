# Event 010 Death Tranche Completion Audit

**Date:** 2026-07-11
**Audit roles:** `chaosx_event_completion_auditor`, `chaosx_decision_mission_auditor`
**Mode:** audit with small, local Event 010 corrections
**Source plan:** `docs/plans/010_death_plans/2026_07_11_death_improvement_loop_addendum.md`
**Implementation handoff reviewed:** `docs/plans/010_death_plans/subagent_handoffs/2026_07_11_death_backend_tranche_handoff.md`

## Verdict

**PASS WITH AUDIT CORRECTIONS.** The current Death backend tranche satisfies the accepted addendum for spatial ordinary spread, maritime evidence, and irreversible post-defeat custodianship after the corrections listed below. No remaining blocker was found inside the bounded audit surface.

The ordinary spatial routes retain ordered short/wide/maximum selection and do not fall back to a global target. Maritime evidence has bounded, one-time evidence sources and the intended first-dismissal/second-report reopening lifecycle. Custodianship requires survey, then outpost, then one permanent policy; its capacity ledgers survive reconsumption and control transfer, and none of the policies restores erased population, factories, resources, or state category. The pre-confirmation decision surface no longer names Death or the Living Compact.

## Audit Surface

Gameplay and localisation files audited:

- `common/script_constants/010_death_constants.txt`
- `common/scripted_triggers/010_death_triggers.txt`
- `common/scripted_effects/010_death_effects.txt`
- `common/dynamic_modifiers/010_death_state_modifiers.txt`
- `common/decisions/010_death_decisions.txt`
- `common/decisions/categories/010_death_categories.txt`
- `events/010_death.txt`
- `common/on_actions/010_death_on_actions.txt`
- `common/scripted_localisation/010_death_scripted_localisation.txt`
- `localisation/english/010_death_l_english.yml`

Required reference work completed before the audit:

- Offline wiki: Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, and AI modding.
- Official documentation: `documentation/effects_documentation.md`, `documentation/triggers_documentation.md`, `documentation/script_concept_documentation.md`, and `common/script_constants/documentation.md` in the vanilla game directory.
- Vanilla precedents: state-targeted decisions; the dynamic `days` variable used with `add_dynamic_modifier` in `common/resistance_activity/resistance_activity.txt`; and the nested state/PREV `distance_to` pattern in `common/ai_strategy/SPR.txt`.

## Acceptance Evidence

### 1. Ordinary spatial spread

**Pass.**

- `death_spatial_route` centralizes the three route bands at 750, 1500, and 2500.
- `death_is_within_short_ordinary_route`, `death_is_within_wide_ordinary_route`, and `death_is_within_maximum_ordinary_route` evaluate candidate states against an active DTH wasteland with `distance_to = { target = PREV ... }`. Official trigger documentation supports `distance_to` in state scope, and vanilla's SPR AI strategy uses the same nested candidate/PREV structure.
- Standard mainland reveal, war-bypass reveal, and coastal jump select tier one, then tier two, then tier three. Their success variables prevent a later tier from running after an earlier success.
- The standard and war-bypass paths require a spatial candidate before spending their route opportunity. A failed coastal jump starts its cooldown but does not reduce spread pressure.
- Coastal Watch remains absolute for ordinary jumps unless No Ferry Returns or world end allows the documented exception. Network interception still requires a spatially valid destination.
- The continent-based world-end foothold triggers and `death_create_world_end_footholds` contain no changed lines in this tranche diff; ordinary routing did not replace or narrow that separate system.

### 2. Maritime evidence and spoiler control

**Pass after corrections.**

- First and second reports award exactly +2 and +3 through separate one-time country ledgers.
- A second report clears a first-report dismissal (`death_ignored_missing_island_report` or `death_maritime_case_closed_under_weather`) before adding evidence. A dismissal after the second report remains closed because no later report clears it.
- Telegraph, survey, and confirmed coastal warning evidence are one-time. The coastal warning snapshots owner and controller before state transfer; the country evidence ledger deduplicates a shared owner/controller.
- Quiet quarantine remains repeatable as protection but grants its +1 evidence only on the first use through `death_maritime_quiet_quarantine_evidence_recorded`.
- Filing under weather removes exactly 3 confidence, preserves any remainder, and closes the quiet investigation. It can occur once before the scheduled second-report reopening and once after that reopening, but cannot be repeated without a reopened file.
- The missing-island category now closes for both dismissal flags. Scripted category title/description and Keep the Port Lit tooltip use unknown-safe text until the country has confirmed the case or Death is publicly revealed.
- The Black Atlas remains independently gated behind both its open flag and public reveal, so the early containment category does not expose it.

### 3. Irreversible custodianship

**Pass after corrections.**

- Survey targets require a recaptured, unsurveyed wasteland. Outpost targets require that survey and no existing outpost. Policy targets require Death's defeat, both completed projects, and no previously selected policy.
- Survey and outpost each award exactly 1 custodial capacity once per state. Their capacity-claim flags are deliberately not cleared by reconsumption or control transfer.
- Reconsumption clears the active survey, outpost, selected policy, and policy modifiers while retaining the anti-duplication ledgers. A later recapture therefore requires rebuilding the progression but cannot recreate already-claimed capacity.
- Memorial Stewardship keeps its state ledger and grants its national +3% stability/up-to-2 mourning-debt benefit only once per country. This prevents repeated national reward farming across many dead states while leaving the permanent state policy available per eligible state.
- Transit Custodianship's underlying policy is permanent, but active maintenance is timed. The maintenance effect now revalidates the current controller, underlying policy, lapse state, and country cost before charging or restoring the timed modifier.
- A control transfer refreshes the permanent policy from state flags and removes active transit maintenance, requiring the new controller to fund upkeep.
- The recaptured wasteland modifier and custodial policy modifiers combine to keep local factories and resources fully erased. No custodial effect changes population, restores buildings/resources, removes the wasteland category, or grants productive recovery.

### 4. Decision and AI behavior

**Pass after corrections.**

- Survey and outpost decision visibility, root targeting, target validation, availability, and completion effects now share the same progression-specific scripted triggers.
- State-target scope follows the vanilla pattern: `state_target = any_controlled_state`, `FROM` is the selected state, and `ROOT` is the acting country.
- Sealed Exclusion is favored for exposed/coastal states; Transit Custodianship is favored only where a naval base or supply node gives the corridor a strategic purpose; Memorial Stewardship is favored for secure interior states.
- Positive mourning debt gives Memorial Stewardship an additional centralized AI multiplier instead of a hard eligibility gate.
- Transit upkeep is highly weighted only after the timed maintenance modifier has lapsed. All decision costs, duration text, capacity gains, and the one-time Memorial national reward match the script constants and effects.

### 5. Integration and compatibility

**Pass.**

- Event 010's first and second report events call the corresponding evidence helpers.
- The existing state-control on-action routes consumed states through `death_on_state_control_changed`, which reapplies active or recaptured wasteland state and refreshes custodial policy behavior.
- `add_dynamic_modifier` accepts a variable in `days`; the transit helper assigns the shared script constant to a temporary duration variable before passing it, matching official documentation and a vanilla implementation.
- New dynamic modifiers have matching English localisation, and the decision/scripted-localisation references resolve to unique localisation keys. The English file retains UTF-8 BOM encoding.

## Corrections Applied During Audit

### `common/script_constants/010_death_constants.txt`

- Added `death_decision_tuning.ai_custodial_mourning_pressure_factor`.
- Added `death_decision_tuning.ai_custodial_mourning_debt_threshold`.

### `common/scripted_triggers/010_death_triggers.txt`

- Closed the missing-island decision category while either report-dismissal flag is active.

### `common/decisions/010_death_decisions.txt`

- Replaced broad recaptured-wasteland survey/outpost target checks with progression-specific candidate and target triggers.
- Added the centralized mourning-debt AI multiplier to Memorial Stewardship.

### `common/scripted_effects/010_death_effects.txt`

- Made the scheduled second report reopen a file dismissed after the first report.
- Made quiet-quarantine evidence one-time while retaining repeatable protection.
- Limited the Memorial national reward to once per country while retaining the state policy ledger.
- Added internal target/controller/lapse revalidation to transit maintenance.

### `common/scripted_localisation/010_death_scripted_localisation.txt`

- Added contextual selectors for the containment-category title and Keep the Port Lit tooltip.
- Added unknown, confirmed, and aftermath routing for the containment description.

### `localisation/english/010_death_l_english.yml`

- Aligned report, evidence, closure/reopening, capacity, survey/outpost, policy, and upkeep wording with the implemented values and irreversible lifecycle.
- Added unknown-safe category and port-watch text and confirmed/aftermath variants.
- Documented the once-per-country Memorial national reward in the player-facing tooltip.

## Validation Notes

- All audited script files have balanced top-level structure, and the new top-level identifiers are unique within their respective files.
- All 508 Event 010 English localisation keys are unique; every new decision and selector key checked by this audit resolves.
- The world-end foothold symbols appear zero times among the changed lines of the trigger/effect diff.
- The dynamic modifier and decision cost/value comparisons were checked against their shared constants and player-facing text.

No live-engine execution was part of this subagent audit. Scope and dynamic-duration conclusions are grounded in current official documentation and matching vanilla precedents.

## Simplifications, Omissions, and Blockers

No fallback or simplification was used in the audited tranche, and no in-scope blocker remains.

Focus-tree work, Living Compact expansion, Black Atlas expansion, later Death route mechanics, assets, and spreadsheet alignment were explicitly outside this bounded backend audit. They are not substitutes for, or claimed as part of, this verdict. No commit was created by this subagent.
