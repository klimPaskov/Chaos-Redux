# Completion Audit Checklist

Status markers used in the reconciliation below: `[x]` means exact current source or bounded audit evidence exists; `[~]` means a bounded source tranche exists but final, engine-bound, or user-owned evidence remains; `[!]` means fail-closed or blocked; `[ ]` means queued or not evidenced. An unchecked legacy item is not a completion claim.

## Current reconciliation disposition

| Surface | Status | Evidence boundary |
| --- | --- | --- |
| Native selected-state Chemical air raid | `[~]` source-audited | Native reservation, selected-state preservation, shared dispatch, and failed-attempt accounting are source-proven; live consumer validation remains user-owned. |
| Continuous ordinary-air contamination | `[!]` fail-closed | No verified current-version eligible-activity hook exists; no estimator or fallback is permitted. |
| Ground Chemical exact-state operation | `[!]` fail-closed | Exact Army Headquarters weather/terrain receipt remains unavailable. |
| Nerve suppression | `[!]` fail-closed | Exact state/weather/terrain and target-loss clearance remain unavailable. |
| Hardened Mobile Plant | `[!]` blocked | No exact bombing or facility-capture equipment-loss transaction is exposed. |
| Native decision-category presentation | `[x]` accepted | Native categories are accepted; no new all-purpose scripted GUI is required. |
| Window-only animation concepts | `rejected` for the current surface | No accepted custom-window consumer exists for the readiness seal, contamination border, or operation-preparation concepts. |
| Exact live production shares and long-run AI pacing | `user-owned`/unresolved | Current source provides bounded relative strategy weights, not exact live percentage receipts. |
| Historically sourced unique national MIO identities | `[!]` unresolved | Current MIO visibility and AI differentiation do not prove those identities. |

The checklist remains open. The dispositions below do not promote an item merely because a source file exists; each completion claim still requires the exact evidence named in the item.

## Doctrine

- [ ] adoption no longer grants excessive global combat bonuses
- [ ] four milestones have functional unlocks
- [ ] four tracks match the accepted spec
- [ ] mastery pacing depends on equipped participation
- [ ] doctrine-only technologies are correctly gated
- [ ] officer corps spirits are bounded and mutually exclusive where intended

## Army Headquarters

- [ ] exact 1.19 schema and vanilla precedent documented
- [ ] all planned HQ companies implemented or explicitly dispositioned
- [ ] company-gated abilities use order scope and current unit-modifier pattern
- [ ] command-power costs scale correctly
- [ ] essential equipment blocks effects when missing
- [ ] AI creates HQs and uses abilities

## Regimental support and units

- [ ] masks, recon, pioneer, projector, ammunition, armored delivery, medical, epidemiology, biosecurity, and suppression roles covered
- [ ] no agent-by-agent duplicate unit family remains active without reason
- [ ] Chaos Assault Battalion has coherent stats and equipment
- [ ] no chemical tank support is parachute-capable without verified reason
- [ ] legacy units migrate safely or remain hidden compatibility content

## Equipment and technology

- [ ] gas-mask equipment is producible
- [ ] decontamination and instrument equipment is implemented
- [ ] equipment enums updated
- [ ] payload and shell or air operation consumption works
- [ ] tabun has a complete or precursor-only role
- [ ] all techs have AI, icons, localisation, and dependencies

## Chemical operations

- [ ] all delivery calls use shared exposure
- [ ] artillery consumes shell lots
- [ ] armored delivery consumes payload
- [ ] air raids reliably contaminate selected states
- [ ] continuous air mission behavior is verified or blocked, not silently approximated
- [ ] first-use shock is defender adaptation, not a global attacker buff
- [ ] weather and protection affect outcomes
- [ ] friendly blowback works

## Biological operations

- [ ] incubation and detection work
- [ ] agent profiles differ
- [ ] spread uses targeted approved hooks
- [ ] quarantine, hospitals, antibiotics, vaccination, and border closure work
- [ ] stockpile accidents scale with safety and stock
- [ ] facilities create capture and evidence risk
- [ ] zombie systems remain separate

## Gas masks and civil defence

- [ ] country starting reserves follow profiles
- [ ] military coverage uses actual equipment
- [ ] civilian distribution consumes crates based on population
- [ ] filters and damaged masks need replacement
- [ ] emergency distribution has wastage
- [ ] masks reduce every chemical death pipeline
- [ ] occupied-population protection choices work

## Suppression and occupation

- [ ] nerve suppression is targeted and temporary
- [ ] payload and advanced protection required
- [ ] deaths, contamination, trauma, evidence, and Condemnation apply
- [ ] no genocide infrastructure is unlocked by doctrine
- [ ] later liberation can discover responsibility

## Shared consequences

- [ ] deaths use the shared tracker
- [ ] population never becomes invalid
- [ ] continuing deaths do not duplicate
- [ ] Air Cleanliness updates by contamination class
- [ ] attribution moves from hidden to confirmed without double charge
- [ ] confirmed use has a Condemnation floor
- [ ] sanctions affect practical support and imports
- [ ] retaliation and treaty context work

## AI

- [ ] AI protects before attacking
- [ ] AI has research, production, template, HQ, operation, containment, and sanction behavior
- [ ] country program profiles differ
- [ ] invalid targets and suicidal use are blocked
- [ ] minors can use defensive content

## UI and localisation

- [ ] readiness, stockpiles, protection, operations, contamination, and response are readable
- [ ] irrelevant decisions hide
- [ ] all dynamic requirements have custom tooltips
- [ ] no hidden mechanics are exposed through final text
- [ ] localisation matches repository style and encoding

## Achievement conformance

- [x] Quarantine Without Collapse uses exact current and needed truck/train `get_supply_vehicles_temp` receipts, requires 80% of each needed class, writes `cbrn_achievement_outbreak_supply_ready_history` only during catastrophic-outbreak recovery, and requires that receipt in its completion trigger.
- [x] Starting-country eligibility is written once after accepted startup profiles through `cbrn_achievement_start_country_eligible`, `cbrn_achievement_starting_major_power`, and `cbrn_achievement_starting_civil_defence_profile`; the common eligibility trigger requires the start-country receipt, and A Mask for Every Door requires the civil-defence receipt.
- [x] A Poisoned Victory requires current Condemnation at or above the accepted high threshold rather than only a historical peak.
- [!] No Wind Is Friendly remains fail-closed because exact selected-state forecast/friendly-exposure receipts require the unavailable ground Chemical weather/terrain hook; its required writers are `cbrn_achievement_forecast_failure_history`, `cbrn_achievement_friendly_exposure_history`, `cbrn_achievement_operation_recovered_history`, and `cbrn_achievement_no_wind_clean_after_failure_history`.
- [!] The Antidote Arrived remains fail-closed because its response receipts are written only by `cbrn_achievement_record_nerve_response`, whose only caller is the exact nerve-suppression state transaction, and Sarin/Soman suppression lacks exact condition/target-loss receipts.
- [!] Unbroken Supply Corridor remains fail-closed because no exact assigned-Army supply-ratio or major-offensive-objective receipt exists; `cbrn_achievement_corridor_operational_history`, `cbrn_achievement_corridor_supply_objective_history`, `cbrn_achievement_corridor_state_count`, and `cbrn_achievement_corridor_supply_days` have no current writers.
- [!] Air Is Still Breathable is unresolved because its accepted prompt requires any major or regional power with enemy Chemical use, while no accepted CBRN regional-power definition or gate exists. The Event 006-specific `is_independence_wave_regional_power` predicate must not be reused, and the startup major-power receipt is not itself an accepted regional definition.
- [ ] The remaining named achievements require final reachability, localisation, icon, anti-exploit, and package scenario audit evidence.

Generic achievement registry `possible = { always = yes }` is presentation-only; happened predicates enforce the startup and campaign receipts. No proxy receipt, estimator, neutral receipt, or fallback is accepted for the fail-closed achievements.

## Assets

- [ ] every visible icon in the asset prompt has source, PNG, DDS, manifest, and GFX handoff
- [ ] animated assets have real source frames and static fallbacks
- [ ] no placeholder art remains
- [ ] asset types are not resized substitutes for one another

## Documentation

- [ ] accepted specs promoted to source-of-truth folder
- [ ] old docs marked superseded or updated
- [ ] mechanics guide matches implementation
- [ ] relevant event docs and catalog rows match actual changed events
- [ ] all plans have a disposition

## Validation

- [ ] ten balance scenarios recorded at weak, normal, and high-chaos conditions
- [ ] AI scenarios recorded for seven major country profiles and three minor profiles
- [ ] exact air-operation hook result documented
- [ ] no broad unapproved global pulse added
- [ ] completion auditor finds no missing accepted requirement

## Simplification report

Completion report must explicitly list every omitted, merged, unsupported, placeholder, or weaker substitute. If none exist, it must state that and provide file and audit evidence.
