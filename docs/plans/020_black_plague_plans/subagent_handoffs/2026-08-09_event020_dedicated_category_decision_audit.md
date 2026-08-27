# Event 020 dedicated Black Plague response-category decision audit

Date: 2026-08-09

Status: source audit complete; no gameplay patch made.

Scope: `common/decisions/categories/020_black_plague_response_categories.txt`, `common/decisions/020_black_plague_response_decisions.txt`, `common/decisions/020_black_plague_shared_response_decisions.txt`, `common/scripted_triggers/020_black_plague_response_triggers.txt`, `common/scripted_triggers/020_black_plague_shared_response_triggers.txt`, `common/scripted_localisation/020_black_plague_response_scripted_localisation.txt`, `localisation/english/020_black_plague_response_l_english.yml`, `interface/020_black_plague_response.gfx`, and Event 020 documentation.

## Disposition


No source patch was necessary. The in-scope files already contain parent/other-agent edits, so I preserved those edits and wrote only this handoff.

## Findings by severity

### Blockers

None found in the source split, category lifecycle, cost/effect wiring, or standard category-picture registration.

### High

None found. The dedicated category is visible independently of the selected disease, preserves the shared category, and does not introduce a scripted GUI or an instant-cure shortcut.

### Medium

The required probability route is unavailable for these Event 020 decision files. `hoi4.probability_inspect` with adapter `decision_ai_will_do` returned `PROBABILITY_SURFACE_EMPTY` and the exact message `No weighted blocks matched this request` for both `common/decisions/020_black_plague_response_decisions.txt` and `common/decisions/020_black_plague_shared_response_decisions.txt`. This is an MCP adapter/source-discovery blocker, not a source conclusion; the same adapter did inspect the comparison Rat decision file.

The generic GUI route is not a faithful named-window route for a vanilla decision category. `hoi4.gui_inspect` for `windowName=decision_category` and scenario `black_plague_response_category` returned a complete graph but reported `GUI_WINDOW_MISSING` and `GUI_SCRIPTED_CONTEXT_INVALID` (48) among global diagnostics, with unrelated workspace-index collisions and truncation warnings. `hoi4.gui_render` still emitted the standard-category artifact, but returned `validation.passed=false` with no checks and an `MCP_RESPONSE_TRUNCATED` diagnostic. This does not justify a scripted-GUI addition; the requested surface is the standard decision UI.

### Low


## Category lifecycle notes

`common/decisions/categories/020_black_plague_response_categories.txt:8-14` defines `black_plague_response_category` with `visible = { black_plague_strategic_response_category_is_visible = yes }`, `visible_when_empty = yes`, `icon = GFX_decision_category_contamination_defense`, `picture = GFX_decision_cat_picture_black_plague_response`, and priority `101`. The category visibility trigger delegates to `black_plague_country_can_direct_response` and therefore remains independent of the selected disease.

`common/decisions/categories/biowarfare_disease_containment_categories.txt:3-15` continues to define `chaosx_disease_containment_category` at priority `100` with the existing disease-board/technology visibility and scripted header. No metadata was removed or redirected.


## Ownership and decision notes


The shared containment surface retains quarantine, emergency hospitals, rat cleanup, food/sewer/flea/transport control, demolition, cordons, treatment distribution, anti-rat operations, and terminal Royal Node/Crown/seal launchers and missions. These entries remain state-targeted or state-resolving and continue to use selected-state/control/phase triggers.

## Mission quality notes

| Surface and owner | Category/target | Requirement and duration | Success/failure/cleanup | Duplicate risk |
| --- | --- | --- | --- | --- |
| `black_plague_shared_emergency_countermeasure_drive` (national response owner) | `black_plague_response_category`; country-level mission | `activation` requires the strategic category, at least one controlled severe state, and no active/failed flag; selectable; `90` days from `constant:black_plague_shared_duration.emergency_countermeasure_drive` | Selection pays support equipment, motorized equipment, and fuel, sets the active flag, and calls `black_plague_add_countermeasure_progress` with `18`; timeout sets failed, adds stability loss and exposure to active states, and fires `chaosx.nr20.56`; cancellation occurs when no severe state remains | Active/failed flags prevent a second mission; the producer clamps to the shared 0–100 threshold |
| `black_plague_shared_strike_the_crown` plus `black_plague_shared_strike_the_crown_mission` (shared containment owner) | `chaosx_disease_containment_category`; state-targeted launcher plus native country mission | Launcher is a zero-day state operation; native mission lasts `constant:black_plague_shared_duration.strike_the_crown` (`180` days) | Launcher stores the state marker and activates the mission; daily success, cancellation on target/control/world-end loss, and timeout each call one resolver | State marker and country active flag gate a single mission; resolver clears operation state |
| `black_plague_shared_seal_royal_burrows` plus `black_plague_shared_seal_royal_burrows_mission` (shared containment owner) | `chaosx_disease_containment_category`; state-targeted launcher plus native mission | Launcher is zero-day; native mission lasts `constant:black_plague_shared_duration.seal_royal_burrows` (`180` days); mission `available = { always = no }` makes it deadline-driven | Target/control/world-end cancellation resolves without the sealing result; timeout calls the existing seal resolver | Active state/country flags and resolver cleanup prevent duplicate sealing |
| `black_plague_shared_last_response_hold_mission` and `black_plague_shared_last_response_refuge_mission` (shared containment owner) | `chaosx_disease_containment_category`; hidden country missions with state-derived success predicates | Activated only by their matching start flags; each uses `constant:black_plague_last_response.mission_days` | `available` predicates resolve success; invalid target cancels; timeout uses the existing hold/refuge timeout resolvers | Matching active flags and cleanup effects prevent stale mission duplication |

The ordinary selected-state entries use `days_remove` constants, project/lane ownership records, explicit completion and cancellation effects, and state control/phase predicates. No duplicate mission ID or unbounded selectable mission was found in the audited files.

## Cost and requirement clarity

`black_plague_produce_medical_reserve` checks factory capacity, manpower, support equipment, motorized equipment, fuel, response capacity, and reserve room through `black_plague_can_pay_medical_reserve_batch`; `black_plague_begin_medical_reserve_batch` pays the same constants, and completion clamps reserve to maximum capacity.

`black_plague_establish_countermeasure_program` checks state eligibility, field-hospital/emergency-hospital access, medical reserve entry threshold, factories, manpower, support equipment, trains, and fuel through `black_plague_can_pay_countermeasure_program`; its begin/finish helpers register the selected state and maintain country response capacity.



Country knowledge/cooperation/hoarding/theft/recovery actions use the shared country-material trigger and per-action flags/cooldowns. The emergency drive's localized cost matches its effect (`120` support equipment, `60` motorized equipment, `1200` fuel, `2` civilian factories, `90` days); its `18` progress gain is partial and routed through the shared producer.

## AI validity and route-lock notes


`black_plague_country_can_direct_response` excludes missing countries, non-host/special rat contexts, terminal takeover completion, and world-end. `black_plague_response_state_is_selected_or_ai_target` keeps human targeting on the selected state while allowing AI to evaluate eligible controlled states. Foreign alliance/inspection actions require a non-self faction partner, and theft requires an intelligence agency plus a foreign active programme.

The mandatory probability comparison remains unresolved only because the Event 020 source returned `PROBABILITY_SURFACE_EMPTY`; no AI target or route-lock defect was found by source inspection.

## Localisation, tooltip, and picture notes

The dedicated category localisation in `localisation/english/020_black_plague_response_l_english.yml` reports country/world deaths, cure status, 0–100 cure progress, Medical Reserve, Response Capacity, and international coordination, and explicitly directs state quarantine/hospital/rat/cordon/treatment work to the shared board. Status keys cover complete, active research, mobilisation, waiting findings, and not-started states.

A read-only reference scan found `77` distinct decision localisation references in `020_black_plague_response_decisions.txt` and `145` in `020_black_plague_shared_response_decisions.txt`; all resolve to keys in the Event 020 English localisation file. Custom cost and effect tooltips are present for the audited decision families.

`interface/020_black_plague_response.gfx:2` registers `GFX_decision_cat_picture_black_plague_response` against `gfx/interface/decisions/020_black_plague/decision_cat_picture_black_plague_response.dds`. The asset manifest and QA handoff record an opaque `114x101` DDS, exact `46184`-byte file length, and zero-pixel DDS round-trip difference; the scene is plague doctors/protected medical workers tending a patient with no text or simulated interface. The category uses this sprite through the standard decision UI and adds no scripted GUI.

## Cleanup and exploit-risk notes

`black_plague_add_countermeasure_progress` initializes progress once, clamps it to `constant:black_plague_response_threshold.countermeasure_completion` (`100`), sets milestone flags, unlocks completion at the threshold, clears the active programme at completion, marks findings available, and recomputes response capacity. The emergency drive's `18` gain therefore cannot bypass the 0–100 lifecycle or create an instant cure.


## Evidence and validation

- Offline Paradox wiki decision documentation confirms category `picture`/`visible_when_empty`, targeted `target_root_trigger`/`target_trigger`, custom-cost debit requirements, and mission `activation`/`available`/`selectable_mission`/`days_mission_timeout` semantics.
- Vanilla category precedent inspected: `common/decisions/categories/AUS_decision_categories.txt` uses standard category metadata with `picture` and `visible_when_empty`.
- Static brace-aware category/child scan found the dedicated and shared ownership lists above with no duplicate child IDs.
- Static localisation-reference scan found no missing decision `name`, `desc`, `custom_cost_text`, or `custom_effect_tooltip` keys in the Event 020 English file.
- `hoi4.gui_inspect` artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0a43b23b565a6c94008bcc9dd7e8285c6b85780c304c2e63ad87349080d21bc3/8eb32abbe7375d516df32e49cdd45ce7f830b9ab70bf570bae72dca604d4ba00/gui-inspect.a1cb5eb222e74238.json`.
- `hoi4.gui_render` artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0c9ce7cca50d9c395bf6b3c5f563d970009b0e65b7f7595c80838b039a80c306/c9bb6c3e66a0b7d0b606813a4ce0ab7aeb1ae05c07934d20aa201fa959c9cace/decision_category-full.svg`.
- Probability adapter listing succeeded, but Event 020 decision inspection returned `PROBABILITY_SURFACE_EMPTY` as described above. The comparison Rat source did produce an artifact, confirming the blocker is specific to this source/adapter parse route rather than a blanket server outage: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1fb3a8e842430f4360dd88f544a525c81b1ff87b9f4fdb22315019f073bf1b4e/403bc28efc76dd5b26e0b9956146eb47c97378614591a07dcca69fa0cae77829/probability-inspect-ef74839ba803.json`.

## Changed files, remaining work, and blockers

Changed by this subagent: only `docs/plans/020_black_plague_plans/subagent_handoffs/2026-08-09_event020_dedicated_category_decision_audit.md`.

No gameplay, category, trigger, localisation, or GFX patch was applied because no clearly blocking source defect was found and the requested correction is already present in the working tree.

Parent review should retain the dedicated/shared category split and the standard category picture, and should carry the exact probability-adapter blocker into the final report. If a later MCP adapter revision exposes Event 020 decision weights, rerun `decision_ai_will_do` inspection and comparison with the same candidate set; source review already records the AI blocks and route locks.

Live in-game category rendering and gameplay balance remain user-owned validation. This audit did not launch Hearts of Iron IV.
