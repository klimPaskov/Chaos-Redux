# Battlefield Biological Scripted-System Audit Handoff

Date: 2026-07-18

Status: bounded audit complete; no gameplay correction was unambiguously necessary. This handoff does not claim Stage 7 or the overall Chaos Warfare goal complete.

## Files inspected

Stage 7 battlefield tranche:

- `common/script_constants/biological_battlefield_constants.txt`
- `common/scripted_triggers/biological_battlefield_triggers.txt`
- `common/scripted_effects/biological_battlefield_effects.txt`
- `common/raids/biological_battlefield_raids.txt`
- `common/scripted_triggers/cbrn_hq_triggers.txt`
- `common/raids/categories/chaosx_raid_categories.txt`
- `interface/chaosx_raids.gfx`

Read-only continuity and precedent surfaces:

- `common/raids/biological_raids.txt` (prohibited from editing)
- `common/scripted_effects/biological_lifecycle_effects.txt` (prohibited from editing)
- `common/units/equipment/bioweapons.txt`
- the current biological strategic raid and headquarters scripted surfaces
- `2026-07-18_stage_7_battlefield_dissemination_validation.md`
- `2026-07-14_stage_7_biological_lifecycle.md`
- the required offline Paradox wiki core pages and Interface Modding page
- vanilla `common/raids/_documentation.md`, `land_infiltration_custom.txt`, `land_infiltration_raids.txt`, and state-target raid precedents
- vanilla raid, trigger, effect, script-constant, and script-concept documentation

## Files changed

Only this handoff file was added. No gameplay file was changed. In particular, the prohibited biological raid and lifecycle files, DDS files, localisation, specs, and unrelated dirty-worktree files were left untouched.

## Findings and evidence

### Native raid contract

The tranche contains four native land raid types: Anthrax, Plague, Tularemia, and Smallpox. Deployment is not a decision click. Each type uses the native `var:target_state`, a supply-node starting point, a land arrow, one of the allowed infantry/motorized/mechanized unit requirement alternatives, native `essential_equipment`, and all four native result callbacks.

The installed raid documentation supports the used state-target grammar, native actor/victim/target variables, starting-point building filters, repeated unit requirements, essential-equipment reservation, success factors, and failure/limited-success/success/critical-success callbacks. The current vanilla raid files provide matching state-target and land-raid precedents.

The native reservations and private scripted mirrors agree:

| Agent | Native essential equipment | Reservation | Shared mirror | Command cost |
| --- | --- | ---: | ---: | ---: |
| Anthrax | `anthrax_bomb_equipment` | 50 | 50 | 10 |
| Plague | `plague_bomb_equipment` | 25 | 25 | 12 |
| Tularemia | `tularemia_bomb_equipment` | 25 | 25 | 10 |
| Smallpox | `smallpox_bomb_equipment` | 10 | 10 | 15 |

The trigger-side stockpile checks use the corresponding `_1` equipment variants defined in `common/units/equipment/bioweapons.txt`. Native equipment remains the authoritative reservation and debit; the scripted values only mirror the immutable payload identity when entering the shared lifecycle.

### Scope and target correctness

The player and native-result paths consistently use the selected state. The resolver saves `actor_country`, `victim_country`, and `target_state` as regular event targets before validation and uses those targets through the result chain. Regular targets are appropriate here because they persist through the current effect chain and fired effects, then clear automatically; no global event target or periodic cleanup is introduced.

The target gate requires a passable lifecycle-eligible state controlled by the enemy, a supply node or at least three enemy divisions, and an adjacent eligible actor-controlled state containing an actor division. War, faction, subject, and controller checks are repeated in the native result context.

The apparently suspicious AI expression
`ROOT = { is_subject_of = PREV }` is valid in context: inside `var:target_state -> OWNER -> ROOT`, `PREV` is the target state's owner country. It correctly rejects an AI target owned by a country that is the actor's overlord. No scope patch is justified.

### Authorization and AI

Combined Overmatch is checked as a live, valid, correctly coded army-leader posture. Headquarters fielding requires a matching payload reserve; the active posture can remain valid after a native raid consumes payload. This is the supported theater-authorization boundary because the engine exposes no exact HQ-to-selected-state binding or native launch callback.

Player availability and AI targeting reuse the same readiness, policy, project, payload, Overmatch, war, front, and target gates. AI additionally rejects friendly/faction/subject-related targets and applies the route, retaliation, first-use, treaty, outbreak, sanction, defensive-profile, and desperation weights. No fallback target, inferred launch state, proxy callback, estimator, periodic scan, or weaponized-zombie route is present.

The vanilla raid documentation describes `enemy_units` as province-target-only, while a current vanilla state-target raid precedent still contains that factor. Because the installed game contains both signals, this is not an unambiguous parser defect and it was deliberately left unchanged in this bounded audit.

### Outcome and lifecycle continuity

Native failure takes the no-release branch: the complete native reservation is treated as lost, exact-state attempt evidence and the eligible biological Condemnation source are recorded, and completed-use history is not created. Limited success, success, and critical success map to the existing ordinary lifecycle dispatcher as partial, success, and catastrophic `battlefield_dissemination` seeds. Dispatch failure is recorded without fabricating a release.

The successful primary release may create one bounded adjacent friendly `connected_spread` seed. It does not perform an alternate-state search, second payload debit, deliberate-use record, or periodic retry. Event-target cleanup remains automatic for the regular chain targets.

Doctrine increases potency/harm and bounded blowback, and refunds only Command Power capped to the native command cost. Payload, evidence, attribution, physical consequences, history, and public-harm floors are not refunded or reduced. Only Condemnation receives the doctrine multiplier.

The existing Anthrax, Plague, Tularemia, Smallpox, and biological-category military-raid icons are reused in `interface/chaosx_raids.gfx`; no existing DDS was overwritten.

## Existing helper map

No new helper is proposed. The current private helper split is sufficient:

| Helper | Scope and inputs | Output/side effects | Main call sites |
| --- | --- | --- | --- |
| `bio_battlefield_country_can_operate` | Country; war, technology, readiness, policy, project, Overmatch, authority | Boolean gate | Native raid availability/launch and AI path |
| `bio_battlefield_target_from_is_valid` | Actor country with native `FROM` and `var:target_state` | Boolean exact-front gate | Target display, availability, launch, AI |
| `bio_battlefield_native_context_is_valid` | Raid instance after regular event targets are saved | Boolean resolution gate | Battlefield resolver |
| `bio_battlefield_set_payload_internal` | Raid instance; immutable agent code | Private payload/CP mirror only; no debit | Resolver and rejected-reservation record |
| `bio_battlefield_dispatch_primary_release_internal` | Raid instance; native outcome and selected state | Ordinary lifecycle seed | Resolver release branch |
| `bio_battlefield_attempt_friendly_blowback_internal` | Raid instance; selected state and actor | At most one exact adjacent spread seed | Resolver after successful dispatch |
| `bio_resolve_battlefield_dissemination` | Raid instance; native agent/outcome variables | Failure records or shared lifecycle dispatch | All four native result callbacks |

All helpers remain subsystem-private and are not added to shared dynamic registries.

## Constants, cleanup, and migration plan

- Shared constants centralize agent reservations, reservation floors, potency, command costs/refunds, target thresholds, blowback, AI weights, outcome codes, and history increments.
- Native raid parser fields retain file-local `@` values where the installed native parser surface does not accept shared constants. The reservation, Command Power, and AI minimum-success values are mirrored and documented above.
- Only regular event targets are used: `bio_battlefield_actor`, `bio_battlefield_victim`, `bio_battlefield_target_state`, the seed targets, and the optional friendly state. They clear with the effect chain; no global target cleanup helper is required.
- The four native callbacks migrate into the one private resolver, which maps releasing outcomes into the existing ordinary biological dispatcher. No legacy dispatcher or strategic biological raid file was edited.

## Validation and unsupported analysis

Read-only validation included source inspection against the installed raid documentation and vanilla precedents, cross-file reservation and equipment-name comparison, call-site tracing for all four native outcomes, scope tracing for `ROOT`/`PREV`/event targets, and inspection of AI/front/lifecycle/doctrine/cleanup branches.

Read-only `hoi4-agent-tools` event, GUI, and map inspection calls were attempted, but each stalled without an artifact and was terminated. Therefore no MCP render or GUI/map artifact is claimed as validation; source and installed documentation remain the evidence for this handoff. No in-game run or parser log is claimed.

## Remaining engine limits and risks

- The engine does not expose an exact HQ-to-state binding or native raid launch callback. Combined Overmatch therefore proves theater authorization, while the native selected state and assigned formation remain delivery context.
- Script cannot independently query the native essential-equipment debit after the raid callback. The native engine remains authoritative; the lifecycle adapter uses an agent-specific proof mirror only after native result entry.
- The installed documentation's province-only description for `enemy_units` conflicts with a current vanilla state-target precedent. It was retained because the evidence is mixed, not because its state behavior was independently proven.
- Final package scenarios, live native UI rendering, and the remaining Stage 7 systems remain outside this audit and unresolved.

## Parent disposition

The main implementation pass resolved the mixed `enemy_units` evidence in favor of the installed documentation. The province-only modifier and its two file-local constants were removed from all four state-target raid success formulas. Exact `divisions_in_state` target eligibility and AI weighting remain. No province estimator, inferred target province, or substitute success modifier was added.
