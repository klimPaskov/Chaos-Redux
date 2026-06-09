# Event006 Formation Ledger Decision/Mission Audit

Subagent role: `chaosx_decision_mission_auditor`  
Scope: current Event006 Independence Wave Formation Ledger after Free Port, Protected Mandate, Oil Protectorate, Canal Authority, and Municipal Authority package additions.

## Required References Consulted

- Offline wiki: `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md`, `Triggers - Hearts of Iron 4 Wiki.md`, `Effect - Hearts of Iron 4 Wiki.md`, `Localisation - Hearts of Iron 4 Wiki.md`, `Modifiers - Hearts of Iron 4 Wiki.md`, `Scopes - Hearts of Iron 4 Wiki.md`, `Data structures - Hearts of Iron 4 Wiki.md`, `AI modding - Hearts of Iron 4 Wiki.md`.
- Vanilla docs/examples: `~/projects/Hearts of Iron IV/common/decisions/_documentation.md`, `~/projects/Hearts of Iron IV/documentation/effects_documentation.md`, `triggers_documentation.md`, `modifiers_documentation.md`, vanilla `common/decisions/AFG.txt`.
- Repo skills: `hoi4-decisions-missions`, `chaos-redux-events`.

## Findings

### 1. Medium: Municipal event-log selected detail body omits municipal types

Refs:
- `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt:3988` through `4013`
- `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt:4015` through `4028`
- Positive title/list refs exist at `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt:711` through `713`, `791` through `793`, `2639` through `2656`, and `2730` through `2732`
- Localisation exists at `localisation/english/chaosx_gui_l_english.yml:289` through `312`

Why it matters:
The municipal formation/package types are mapped in the list, history, event-detail title, and selected-detail title paths, but the selected-detail body routing omits `municipal_authority_formation_type` and `municipal_charter_package_type`. Selecting a municipal log row can therefore fall through to the wrong generic body or no matching Event006 formation/package detail body even though the name is localised.

Small local fix:
Add `constant:independence_wave_event_log.municipal_authority_formation_type` to the formation-body `OR` after the canal authority line, and add `constant:independence_wave_event_log.municipal_charter_package_type` to the package-body `OR` after the canal register line.

### 2. Medium: Municipal integration mission uses the Free Port duration constant

Refs:
- `common/decisions/006_independence_wave_decisions.txt:21`
- `common/decisions/006_independence_wave_decisions.txt:24`
- `common/decisions/006_independence_wave_decisions.txt:1469`
- `common/script_constants/006_independence_wave_constants.txt:706` through `709`

Why it matters:
`independence_wave_integrate_municipal_authority` uses `days_mission_timeout = @independence_wave_free_port_integration_days`. There is no municipal-specific `@independence_wave_municipal_authority_integration_days`, so municipal mission tuning is silently tied to Free Port tuning. That is not a runtime break today because both are plausible short integration missions, but it violates the central tuning pattern used by the surrounding package missions.

Small local fix:
Add `@independence_wave_municipal_authority_integration_days = 95` or `100` near the other Formation Ledger day constants and use it at line 1469. If the parent wants municipal authority to match Free Port exactly, add a comment-free named alias anyway so future tuning does not couple unrelated packages.

### 3. Medium-Low: Non-proclamation package steps expose raw scripted trigger gates

Refs:
- Free Port: `common/decisions/006_independence_wave_decisions.txt:1188` through `1214`
- Canal: `common/decisions/006_independence_wave_decisions.txt:1288` through `1315`
- Municipal: `common/decisions/006_independence_wave_decisions.txt:1389` through `1416`
- Protected Mandate: `common/decisions/006_independence_wave_decisions.txt:1490` through `1517`
- Oil Protectorate: `common/decisions/006_independence_wave_decisions.txt:1591` through `1618`
- Scripted triggers exist at `common/scripted_triggers/006_independence_wave_triggers.txt:1324` through `1509`
- Proclamation decisions use custom requirement tooltips, e.g. `common/decisions/006_independence_wave_decisions.txt:1334` through `1338`, `1435` through `1439`, `1637` through `1641`

Why it matters:
The opener/intermediate decisions use direct `can_independence_wave_* = yes` gates in `available`. If blocked, the player is likely to see raw trigger structure or trigger names instead of readable requirements. This is most visible for the recent municipal, canal, oil, and protectorate packages because their proclamation steps already have proper custom tooltips but their preceding steps do not.

Small local fix:
Wrap each opener/intermediate `available` gate in `custom_trigger_tooltip` and add short `_requirements_tt` keys. The text should name the concrete requirement: controlled canal state, opened register, controlled inland city state, opened municipal charter, controlled oil field, audited concessions, audited protectorate treaties, or reviewed guarantees.

### 4. Low-Medium: Oil Protectorates also receive the generic protectorate AI overlay

Refs:
- Generic protectorate overlay: `common/ai_strategy/006_independence_wave.txt:465` through `499`
- Oil overlay: `common/ai_strategy/006_independence_wave.txt:537` through `566`
- Oil package trigger keeps `independence_wave_package_type = protectorate_package` at `common/scripted_triggers/006_independence_wave_triggers.txt:1465` through `1469`

Why it matters:
`independence_wave_protectorate_mandate_restraint` enables for any country whose `independence_wave_package_type` is `protectorate_package`, not only the generic `independence_wave_package_protectorate_mandate`. Oil Protectorates therefore stack the generic protectorate restraint/defense overlay with their oil-specific fuel-security overlay. That may be acceptable if intended as a broad family baseline, but the strategy name and separate oil strategy suggest an accidental double layer.

Small local fix:
Either remove the package-type fallback from lines 473 through 477, or add `NOT = { has_country_flag = independence_wave_package_oil_protectorate }` if the generic overlay should remain limited to non-oil protected mandates. If the stacking is intended, rename or comment the strategy in a parent patch so future audits do not treat it as accidental.

## Areas With No Blocking Issue Found

- Decision and mission syntax: brace balance is clean for the audited Event006 decision, trigger, effect, constants, and AI files.
- Unsupported comparison operators: no matches found in the audited Event006 decision/trigger/effect/constants/AI files.
- Localisation key coverage: every decision id in `common/decisions/006_independence_wave_decisions.txt` has a matching name and `_desc` in the audited English localisation set; referenced tooltip-like keys also resolve.
- Localisation encoding: both `localisation/english/006_independence_wave_l_english.yml` and `localisation/english/chaosx_gui_l_english.yml` start with UTF-8 BOM.
- Recent package effect/log wiring: Canal, Municipal, Protected Mandate, and Oil package actions call their package or formation log helpers; the missing municipal selected-detail body routing above is the only concrete event-log integration issue found in this bounded pass.
- Mission lifecycle pattern: the recent integration missions use the established non-selectable failure-on-`available`, success-on-timeout pattern and have failure/success tooltips. The Canal and Oil failure triggers include subject status, lost control, and dangerous patron leverage; Municipal includes subject status and lost inland-city control as documented.
- AI weights on recent decisions: the recent package decisions have `ai_will_do` blocks on clickable steps and AI strategy overlays for municipal, canal, oil, and protectorate packages. The only balance concern found is the oil/generic protectorate overlay stacking noted above.

## Validation Commands Run

- `sed -n`/`nl -ba` reads of all required offline wiki, vanilla docs/examples, skills, and audited Event006 files.
- `rg -n "municipal|canal|oil_|free_port|protectorate|protected_mandate|formation_ledger|record_events_log|event_log" ...`
- `python3` brace-balance check over `common/decisions/006_independence_wave_decisions.txt`, `common/scripted_triggers/006_independence_wave_triggers.txt`, `common/scripted_effects/006_independence_wave_effects.txt`, `common/script_constants/006_independence_wave_constants.txt`, and `common/ai_strategy/006_independence_wave.txt` returned `brace_balance=0 min_balance=0` for all.
- `python3` decision localisation coverage check returned `decision_ids 130` and `missing decision loc entries 0`.
- `python3` tooltip-like localisation coverage check returned `missing tooltip-ish loc 0`.
- Raw unsupported comparison-operator scan found no matches in the audited Event006 decision/trigger/effect/constants/AI files.
- `xxd -p -l 3 localisation/english/006_independence_wave_l_english.yml` and `xxd -p -l 3 localisation/english/chaosx_gui_l_english.yml` both returned `efbbbf`.
- `git status --short` was inspected before writing this handoff; the worktree already had many unrelated Event005/Event006 changes and untracked Event006 files.

## Files Changed By This Subagent

- Added this handoff only: `docs/plans/006_independence_wave_plans/subagent_handoffs/2026_06_04_083702_decision_mission_audit.md`
