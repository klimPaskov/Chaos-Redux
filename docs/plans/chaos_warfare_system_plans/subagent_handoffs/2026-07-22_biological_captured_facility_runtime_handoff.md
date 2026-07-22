# Captured Biological Facility Runtime Handoff

Date: 2026-07-22

## Status

Implemented directly by the parent after the bounded scripted-system subagent was closed without returning files. The runtime is integrated with two native land raids; there is no decision-based biological deployment path.

## Changed files

- `common/script_constants/biological_facility_capture_constants.txt`
- `common/scripted_triggers/biological_facility_capture_triggers.txt`
- `common/scripted_triggers/biological_lifecycle_triggers.txt`
- `common/scripted_effects/biological_facility_capture_effects.txt`
- `common/scripted_effects/biological_stockpile_safety_effects.txt`
- `common/on_actions/biological_facility_capture_on_actions.txt`
- `events/biological_facility_capture_events.txt`
- `common/raids/biological_facility_recovery_raids.txt`
- `common/raids/categories/chaosx_raid_categories.txt`
- `common/scripted_effects/biological_lifecycle_effects.txt`
- `localisation/english/biological_facility_recovery_raids_l_english.yml`
- `docs/systems/captured_biological_facility_recovery.md`

Raid icons and their source package were committed separately in `faebc4b5a`.

## Runtime identifiers

- Category: `biological_facility_recovery_raids`
- Raids: `bio_facility_secure_preserve_raid`, `bio_facility_destroy_safely_raid`
- Exact unresolved state: `bio_captured_facility_unsecured`
- Exact controller pointer: `bio_captured_facility_controller`
- Exact original custodian pointer: existing `bio_stockpile_safety_arsenal_actor`
- Agent ledgers: `bio_captured_facility_anthrax`, `bio_captured_facility_plague`, `bio_captured_facility_tularemia`, `bio_captured_facility_smallpox`
- Total ledger: `bio_captured_facility_total`
- Targeted due ledger: `bio_captured_facility_hazard_due_day`, `bio_captured_facility_hazard_event_scheduled`
- Event namespace: `cbrn_bio_facility`

## Exact scope assumptions

- `on_state_control_changed`: ROOT is the new controller, FROM is the old controller, and FROM.FROM is the exact changed state. The callback evaluates only FROM.FROM.
- The existing `bio_stockpile_safety_arsenal_complex` marker and `bio_stockpile_safety_arsenal_actor` pointer prove the one designated national arsenal.
- HOI4 equipment stock is national, not state-scoped. First hostile capture therefore removes all currently unallocated four-agent payload equipment from the recorded custodian once and stores those counts on the exact captured state. Negative removal deliberately omits a producer filter so mixed domestic, captured, and licensed payload stock cannot survive the aggregate debit. Equipment already reserved by a native raid is absent from `num_equipment` and is not double-counted.
- A third-party control change updates the exact controller pointer and preserves the payload and due ledgers. Original-custodian recapture restores exactly the remaining state-ledger payload.
- Explicit manual arsenal relocation preserves the captured state's original-custodian pointer. On recapture, the old designation is rebound only when no replacement exists; an active replacement designation is never cleared by resolving or retaking the captured site.
- If the exact original custodian no longer exists when a release occurs, the ordinary outbreak still resolves in the exact state with the exact current controller as victim, but actor proof remains missing. No surviving-country attribution proxy is substituted.
- Native raid outcome helpers accept only `var:actor_country` and `var:target_state` from the raid instance and reject stale context without selecting another state.

## Lifecycle and consequence integration

- Accidental release route: `bio_lifecycle_route.captured_facility_release`
- Source: `bio_lifecycle_source.captured_facility`
- Result: `bio_lifecycle_result.accident`
- Payload debit proof records the exact released state-ledger amount once.
- Captured-facility lifecycle validation requires the exact current-controller victim proof, current controller match, positive required and consumed values, supplied debit proof, and consumed amount bounded by the required amount. Original-custodian actor proof remains optional only when that recorded country no longer exists.
- Force detection is queued for activation because the containment breach is observed.
- No deliberate-use proof or use-history record is supplied.
- Lifecycle attribution now treats `accident`, `captured_facility`, and `field_test` sources as accident-class, preventing evidence from relabeling those records as deliberate attacks.
- Program evidence uses source `biological`, context `experiment_site`, discovered visibility, and major severity against the recorded original custodian. Raw evidence is never doctrine-reduced. Terminal doctrine multiplies only the Condemnation base by its existing 0.80 factor.
- Existing genocide state-control discovery remains authoritative for atrocity and cover-up sites; this runtime does not duplicate it.

## Raid-layer behavior

- Both raids hard-require one selected division with `cbrn_biosecurity_assault_detachment`.
- The selected division's character-scoped unit leader receives a fail-closed -10 success weight when `cbrn_hq_has_biological_security_section = no`; the exact assigned section also provides the intended +0.25 success modifier. Because the native `unit_requirements` block accepts only battalion/equipment filters, an invalid formation can remain visible to a player but cannot succeed. AI rejects it through the native minimum-success threshold. No national-HQ proxy is used.
- State hazard at or above 100 payload units applies a -0.15 success modifier.
- Secure/preserve: 21 days, 25 Command Power, 80 masks, 50 decontamination, 40 instruments, 60 support, 30 trucks.
- Destroy safely: 14 days, 20 Command Power, 80 masks, 70 decontamination, 30 instruments, 70 support, 30 trucks.
- Failure releases 15 percent of one weighted available agent, minimum one.
- Unresolved due event releases 10 percent of one weighted available agent, minimum one, then rearms only the same exact state after 30 days if payload remains.
- Limited secure transfers 40 percent of each agent; limited destroy debits 50 percent of each agent. These nominal shares may round to zero for a one-unit agent stock and never use the minimum-one release rule.
- Full secure transfers all surviving payload. Full destroy debits all surviving payload and removes one `biowarfare_facility` level.

## Validation performed

- Verified the installed raid documentation for state targets, repeated unit requirements being OR, essential equipment, raid-instance variables, land-raid unit effects, and character/state custom success modifiers.
- Used exactly one BSA unit-requirement block per raid.
- Verified all eight raid outcome helper references resolve to private scripted effects.
- Verified aggregate capture debit omits the producer filter required to remove mixed-producer stock, while all positive restoration/transfers retain the receiving country as producer.
- Verified the minimum-one rule is called only by accidental-release accounting and not by limited secure/destroy fractions.
- Verified the assigned-HQ requirement is sampled from the selected formation's character scope and cannot be satisfied by an unrelated national headquarters.
- Verified brace balance across constants, triggers, effects, on-actions, events, raid definitions, and category definitions.
- Verified no unsupported comparison operators, unary negative variable tokens, periodic world pulses, random-state selectors, decision activation, or placeholder sprites occur in the captured-facility file set.
- Verified the localisation file retains the required UTF-8 BOM.
- Verified the existing `gfx/interface/military_raids` assets were neither deleted nor modified by this tranche.

## Remaining validation risk

The current-version raid documentation permits arbitrary state target triggers but does not include a vanilla example of a land raid aimed at an enemy-owned state already controlled by the actor. The implementation uses that documented arbitrary state-target surface and has no fallback. This must remain an explicit package scenario check; if the engine suppresses such targets, the behavior is unsupported until a native raid hook is found, and it must not be replaced by a decision.

The current-version raid `unit_requirements` schema accepts battalion and equipment filters but no selected-unit character trigger. The exact assigned-headquarters requirement is enforced through a fail-closed character-scoped success factor in native unit selection. The selection UI cannot remove the invalid formation itself; this engine presentation limit is disclosed and has no decision, country-wide HQ check, or inferred assignment fallback.
