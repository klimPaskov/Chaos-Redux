# Private custom-family Deployment payoff audit

Date: 2026-09-08.
Disposition: source audit implemented; all payoff proposals unresolved pending parent acceptance.
Ownership: this handoff only; no gameplay, AI, technology, GUI, focus, or asset edits.

## Requirement and current finding

The parent requested meaningful Deployment payoffs for the seven custom private families within the accepted final completion contract.
Full neutral operational technology at authentic native Prototype must remain unchanged, including manufacture, templates and ordinary runtime access.
Paid Deployment must add a tangible capability rather than repeat that grant or make existing public access conditional on a private receipt.
No new family, category, GUI, technology, global scheduler, unit-spawn loop, or Kruger Directorate state is authorized by this audit.
The parent's subsequent addition of the seven existing Deployment modifiers is baseline parity, not closure of the physical-capability gap.

`brilliant_scientist_mengele_grant_custom_stage_package` in `common/scripted_effects/016_mengele_project_stage_effects.txt` currently calls `chaosx_grant_custom_operational_technology` at Deployment for each family.
The native bridge already makes that same full grant after authentic private Prototype recording.
Consequently, after a successful native Prototype, the repeated grant itself adds no new operational entitlement.
The private Deployment receipt remains useful as a Weaponization predecessor but is not, by itself, a tangible Deployment payoff.

Do not solve this by delaying neutral access, granting Weaponization early, writing `brilliant_scientist_project_stage_entries`, setting Kruger facility/history flags, or declaring an existing capability newly unlocked.

## Family-by-family source map and proposed implementation

Every proposed private consumer uses `brilliant_scientist_mengele_project_stage_provider_is_valid`, the exact `mengele_event016_<family>_deployment_completed` receipt, and the corresponding neutral operational entitlement.
It must also revalidate any selected owned-and-controlled physical state at settlement.
None of the following consumers exists as a private adapter yet.
New private state receipts and narrow payment/output helper extractions require parent acceptance; names below describe proposed contracts, not installed IDs.

### Teleportation: physical transit logistics

Source: `016_brilliant_scientist_project_effects.txt` marks both primary and secondary facilities `brilliant_scientist_quantum_transit_terminal` and sets `brilliant_scientist_quantum_transit_network_ready` at Kruger Deployment.
`brilliant_scientist_has_teleportation_force_deployment` additionally checks Kruger stage history, so these flags are not a neutral API.
Existing action precedents are `brilliant_scientist_krg_construct_transit_terminal`, `brilliant_scientist_krg_link_terminal_supply_network`, and `brilliant_scientist_krg_fabricate_portal_transit_batch` in the portal/temporal decision file.
The batch output kernel is 180 `teleportation_equipment_1`, from `brilliant_scientist_krg_output.portal_equipment_batch`; the completion helper also writes a KRG batch count and therefore must not be called unchanged.

Proposal: Deployment commissions an actual two-site private transit route, with a player-selected origin and destination from existing controlled industrial/supply states.
Its immediate physical payoff should be the inspected terminal/supply construction component, while its ongoing consumer is an additional paid transit-equipment fabrication option.
Extract only the construction/output portion, preserve the existing public Portal raid and ordinary production gates, and use private endpoint receipts instead of `brilliant_scientist_quantum_transit_network_ready`.
Do not claim a flag alone improves supply; the implementation must name and deliver the actual building/railway output after a map inspection and slot validation.
The exact route construction quantity remains an acceptance and map-validation decision, not an approved substitute.

### Cloning: reserve replenishment rather than another template

Source: Kruger Deployment records a growth site; Kruger Weaponization calls `clone_select_kruger_refinement`.
Private Weaponization already owns the Mengele refinement path, so moving that reward to Deployment would merely shift the duplicate-reward problem.
`clone_system_effects.txt` defines neutral template access and stockpile-derived manpower, with `clone_system.weekly_manpower_per_equipment = 10`.
Important defect in the reusable precedent: `brilliant_scientist_krg_complete_clone_growth_cycle` currently outputs 400 `infantry_equipment_0` and 40 `support_equipment_1`, not clone equipment, and then writes KRG growth/identity-crisis state.
It cannot honestly be reused as a clone-production payoff without changing its output contract.

Proposal: Deployment establishes a private growth-site consumer permitting a bounded, explicitly paid clone-equipment production cycle, feeding the existing physical reserve-manpower system.
The installed concrete output ID is `clone_equipment_1` in `common/units/equipment/clone_equipment.txt`, with the `clone_equipment` archetype; do not reuse the old infantry/support kit or create divisions.
Its ordinary factory recipe uses one steel and two rubber with build cost 12; these are reserve/production references, not permission to deduct strategic resources as stockpiled equipment.
The extra production must preserve ordinary factory manufacture from Prototype and must have its own paid receipt and finite cooldown/limit.
Quantity and recipe require acceptance because the inspected KRG cycle does not supply a valid clone-equipment amount.
This is an explicit source gap, not approval to invent an amount or substitute seven generic army kits.

Parent source correction, 2026-09-08: the private program already has `germany_mengele_produce_clone_equipment` in `common/scripted_effects/germany_mengele_effects.txt`.
It checks `germany_mengele_cloning_project_completed`, counts controlled states containing `biowarfare_facility`, and adds actual `clone_equipment_1` at `constant:germany_mengele_cloning_project.clone_equipment_per_facility_per_week`, currently one, before refreshing reserve manpower.
Call sites include project completion, `common/on_actions/germany_mengele_clone_on_actions.txt`, and additional program effects; the full eligibility and timing audit is delegated to `016_private_clone_existing_production_review_2026-09-08.md` in this handoff directory.
The proposal above remains unresolved and must be evaluated against that existing consumer before accepting another private production subsystem.
This source finding does not authorize changing its output rate, inventing Deployment history, or treating a weekly-named constant as proof that every caller runs only weekly.

### Robotics: assembly capacity and paid frame manufacture

Source: Kruger Deployment establishes `brilliant_scientist_robotics_assembly_complex`; `brilliant_scientist_krg_run_bounded_robot_assembly` requires the KRG power-node/operational gates.
`brilliant_scientist_krg_complete_robot_assembly_cycle` outputs 125 `autonomous_robot_equipment_1` and writes KRG cycle/burden state.
`brilliant_scientist_krg_standardize_frame_repair` awards army experience, not actual damaged-frame recovery; it must not be advertised as a salvage system.

Proposal: commission a private assembly site in a real industrial state and expose the extra paid 125-frame batch as a capacity-limited supplemental production channel.
Its tangible distinction from cloning is machine manufacture consuming the inspected support/truck/fuel inputs rather than reserve manpower growth.
Extract the stockpile output only and retain ordinary military-factory production unchanged.
A physical assembly-capacity award at Deployment is preferable to an unlock whose only result is permission to pay again, but the actual building increment and slot handling require acceptance.

### Paleogenetics: reserve-to-transport production chain

Source: Kruger Deployment establishes distinct `brilliant_scientist_paleogenetic_reserve` and `brilliant_scientist_paleogenetic_hatchery` sites.
`brilliant_scientist_krg_run_bounded_paleogenetic_breeding_cycle` requires veterinary support plus an owned transport pen and outputs 275 `paleogenetic_creature_equipment_1` plus 75 `support_equipment_1`.
The relevant existing actions also include `brilliant_scientist_krg_designate_paleogenetic_reserve`, `brilliant_scientist_krg_construct_paleogenetic_hatchery`, and `brilliant_scientist_krg_construct_paleogenetic_transport_pen`.

Proposal: private Deployment commissions a real reserve/hatchery pair, then permits the existing paid breeding-output recipe only while both sites and the transport requirement remain controlled.
Keep creature equipment as stockpile output, not spawned formations.
The two-state physical dependency makes this different from the single-site robot assembly channel.
Do not write the KRG veterinary, recruitment, breeding-cycle or crisis flags; private wrappers need their own bounded operational receipts.
Loss of a site suspends supplemental production without revoking learned technology or deleting existing equipment.

### Xenobiological synthesis: control choice and medical fabrication

Source: Kruger Deployment establishes vat/control-center sites; its Weaponization grants formations and a selected control technology.
`brilliant_scientist_krg_choose_xenobiological_control_mode` fires `chaosx.brilliant_scientist_krg.30`, which is a KRG action and must not simply be fired for a private owner.
The neutral API already exposes `chaosx_grant_custom_technology_upgrade` with `xeno_chemical_control`, `xeno_neural_control`, `xeno_machine_control`, and `xeno_researched_control`, including exclusivity reconciliation.
`brilliant_scientist_krg_establish_xenobiological_medical_fabrication` physically adds one `fuel_silo` and writes KRG medical-fabrication and shared control-center flags.
Its label does not establish a separate medical-equipment production capability.

Proposal: Deployment offers a deliberate choice among the existing neutral control refinements, conditioned on the matching real prerequisites and exact private Deployment receipt, without changing base operational access or granting the separate Weaponization upgrade.
This is a family-specific management payoff rather than a generic modifier ladder.
Use existing decision presentation, not an unreviewed KRG popup or new technology.
If parent prefers physical fabrication instead, extract the actual building output and state its real fuel-storage benefit; do not describe a fuel silo as manufactured medical supplies.
Choice timing, prerequisites, replacement rights and whether the stage payment includes the first refinement require acceptance.

### Alien arms: expedition support, not duplicate contact access

Source: Kruger Deployment establishes `brilliant_scientist_alien_interface_chamber`.
Neutral operational Alien Infantry already supports contact/landing access, so merely re-enabling contact at private Deployment is not a payoff.
The existing `dhrondan_envoy_craft_has_operational_work` private branch reads old completed-project flags for alien arms/materials/computation plus `rocket_engines` and `atomic_research`.
`dhrondan_send_mengele_to_dhronda` already exists, and the expedition costs 50 Political Power and 500 fuel through `dhrondan_contact` constants.
The supplemental production kernel `brilliant_scientist_krg_complete_alien_laser_batch` outputs 100 `alien_laser_weapon_equipment_1` but also writes a KRG batch count.

Proposal: Deployment commissions a private interface-production site and adds a paid, limited 100-laser batch consumer to support the existing 2,000-laser landing economy and expedition preparation.
Reconcile envoy-craft readiness with authentic private alien/materials/computation progression through an additive provider-specific branch, retaining actual rocket/atomic/native-craft requirements.
That readiness repair is compatibility work, not by itself a reward if the legacy branch already grants access.
Do not grant the envoy craft, complete the expedition, spawn a landing, grant a pact, or bypass the existing landing reservation by stage callback.
The parent must decide the immediate site benefit versus supplemental paid production; no free army kit is proposed.

### Temporal: one bounded defensive intervention

Source: Kruger registers/authenticates the temporal anchor at Prototype, not Deployment.
Kruger Deployment itself adds only its stage modifier.
`brilliant_scientist_krg_issue_bounded_future_warning` targets a live threatened state; its commit helper adds one `bunker` and one `anti_air_building`, binds a persistent rescue target, incurs synchronization/debt, and starts a survival mission.
This is not a neutral helper: it also writes KRG attempt, mission, target and achievement state.

Proposal: private Deployment commissions a physically anchored one-use warning intervention with the same concrete bunker/anti-air defensive result in a currently controlled threatened state.
Extract the physical effect and strict target validation, but do not call the KRG warning/temporal-ledger helper unchanged.
The private stage payment may purchase this single intervention; no equipment or units need be spawned.
Anchor, one-use target receipt, delayed-loss cancellation and any genuine temporal liability must be explicitly designed and accepted before implementation.
Without accepted private synchronization/debt semantics, call this proposal unresolved rather than pretending that a fortification-only extract implements the complete KRG temporal system.

## Extraction and transaction contract

Do not expose KRG focus-locked categories to private countries wholesale.
A reviewed implementation may add narrow adapters in the existing `mengele_clone_army_category` or reuse an already neutral action consumer, preserving all current KRG/public callers.
Separate three layers: provider-specific eligibility; provider-neutral physical payment/output kernel; provider-specific receipt/history/incident settlement.
The physical kernel takes explicit country/state/equipment/amount inputs and returns a success result; it must not discover a provider by reading Kruger selectors.
Temporary selectors are cleared and caller values preserved as with the native grant extraction.

The existing KRG project-batch recipe is 150 support equipment, 50 trucks, 1,000 fuel and 1,000 manpower, with a 90-day heavy timer, 30-day re-enable delay and native factory reservation.
It is a source reference, not automatically the accepted recipe for all private families.
Blindly copying that recipe across all families would reproduce generic content and may consume manpower nonsensically for robotic production.
Use existing shared duration/payment constants where they genuinely match the accepted recipe; put changed private recipe tuning in a coherent shared constant table only after acceptance.
The finite cycle maxima in `brilliant_scientist_krg_capacity` are source-owned KRG tuning, not permission to write its counters.

For an immediate Deployment physical output, set the private completion receipt only after actual success; if the chosen target becomes invalid, do not charge and award an empty facility flag.
For supplemental timed production, reserve the displayed inputs once, store exact owner/family/target/amounts, refund or settle once, and let the native decision own factory occupancy.
No generic scheduler is needed.
Do not reverse native learned technology on site loss or provider departure.
No proposal changes native project payment, public operational strength or separate Weaponization outcomes.

## Validation and remaining acceptance

Required implementation scenarios: Prototype-only owner retains full native manufacture; paid Deployment adds the specific physical/choice consumer; repeated stage callbacks cannot award it twice; Kruger and private programs coexist without selector/history contamination; captured/invalid sites cannot produce delayed rewards; exact-price starts work; cancellation releases only its own receipt; production never creates a free division; existing native contact, raid and expedition reservations remain independent.
Xeno choice additionally needs all four prerequisite/exclusivity cases and a preexisting neutral control grant.
Cloning needs stockpile-derived manpower before/after consuming the produced clone equipment.
Temporal needs an explicit accepted private liability contract and target-loss test, not only a construction check.

The events, decisions/missions and subagents skills informed provider separation, native timer ownership and proposal/acceptance distinctions.
Offline Decision modding and Scopes references and installed vanilla `documentation/effects_documentation.md` were consulted for state construction and explicit scope behavior, alongside the existing repository action precedents.
Installed vanilla `common/decisions/_documentation.md` was read completely; its country/target scope and daily-versus-frame gate distinctions govern the proposed state adapters.
`common/decisions/aat_mio_decisions.txt` supplied an additional native scoped-decision precedent.
This audit did not change weights or choose AI balance targets.
Parent implementation requires the applicable probability baseline/comparison, decision/localisation audit and map inspection before site/railway design is finalized.

Event inspection returned `EVENT_INSPECTED_PARTIAL`, focused analysis with zero expanded helpers and deferred lifecycle passes.
Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1835a7bb307994bfa261208366f1578a442e1d9dd820abd7700214e8c803fc69/16fee41b9b7b5bd56fd0ee764f6dfad35291837f17a1be36839d12703fb28373/event-scan-4bccb6ec7fe1.json`.
It does not validate the proposed private consumers, map effects or full helper lifecycle.
No map topology, new GUI, technology layout, or focus route was designed or edited in this audit.
All seven physical payoff contracts remain proposals; baseline Deployment modifier parity does not close them.

Source snapshot SHA-256: private stage effects `a6408c5269ed09b3b8b9ebc01c09b5551eae396290fd5b622c088d52be147e83`; Kruger project effects `8b670bb2a868aee0ba1275cc72d87161bab222d47d2c10a88adb478f51d7d5d7`; KRG physical/action effects `ef9de1e07f710e284a6a1b7c2cbd1202f535c2b46b137f07e5fb947714d802e8`.
