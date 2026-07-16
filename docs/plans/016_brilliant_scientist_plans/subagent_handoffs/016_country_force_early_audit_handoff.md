# Event 016 Kruger State country and force early audit handoff

## Status and boundary

This is an early, read-only country-package audit. It is **not** a completion claim for Event 016, the Kruger State, its focus tree, its decisions, or its visual package.

The audit snapshot was taken on 2026-07-16 after the formation and project-force repairs then present in the shared worktree. The auditor changed no gameplay, localisation, asset, spreadsheet, or source-specification file. This handoff is the auditor's only file change.

Audit scope:

- fixed-tag Kruger State formation from charter, rebellion, and enclave territory plans;
- institutional takeover of the existing host;
- Warren Kruger identity and transfer invariants;
- carried project history, facilities, capacity, and force reconstruction;
- conventional opening-force scaling;
- bounded project-force templates and runtime revocation;
- the live 100-focus tranche, AI-plan references, localisation coverage, and asset wiring;
- country-package documentation and acceptance scenarios.

Primary design sources were Part 3, Part 5, the acceptance criteria and matrices under `docs/specs/016_brilliant_scientist_specs/`, plus `subagent_handoffs/016_project_reuse_identifier_map.md`. The required offline wiki pages, official vanilla documentation, and vanilla precedents were consulted before source review. No Paradox wiki web page was used.

## Executive disposition

The **core formation transaction is statically acceptable** after the current repairs. The fixed-tag route fails closed if its exact frozen territory plan is no longer valid; institutional takeover remains a separately proven route and is not a fallback. The sole Warren Kruger character is transferred without duplication, success is recorded only after the mutation path finishes, and takeover does not manufacture a second tag or grant a conventional opening army.

The **seven division-producing project-family packages are statically acceptable at the runtime-control layer** after the current cap, designer-bypass, and stale-reconstruction repairs. Their opening formations require exact carried history, an operational project state, and the matching physical site. The battalions remain inactive globally, their templates are locked, recruiting is controlled per template, and the live division ceilings match the reserved table for those seven families.

The **country package as a whole is not ready for acceptance**. Its current blockers are:

1. Thirty-six focus gate flags are tested but have no producer. The critical prototype-works gate blocks every downstream project lane.
2. Three hundred and one focus-set flags have no present `has_country_flag` consumer in `common/` or `events/`; advertised decision, mission, crisis, and integration unlocks therefore remain contracts rather than working systems.
3. The ongoing force-growth and maintenance systems required by Part 5 are not implemented. The biological family also lacks its bounded stockpile/delivery lifecycle.
4. The binding meaning of the reserved conventional ceiling `12` and biological ceiling `4` is not represented by a current bounded runtime system and must be reconciled explicitly.
5. The conventional opening formula has a sound bounded skeleton, but several Part 5 distinctions and the five required balance bands have not been demonstrated.
6. The country visual package is incomplete: all KRG flag triplets, all 100 focus textures, and all five starting-spirit icons are still pending.
7. Event/system documentation still describes the country and force tranche as future work and does not match the live implementation.

## Formation invariant audit

| Invariant | Live finding | Disposition |
| --- | --- | --- |
| Exactly one Warren Kruger | `KRG_warren_kruger` has one character definition in `common/characters/016_brilliant_scientist_characters.txt`. Formation changes nationality and roles; it does not create a replacement character. | Pass |
| Fixed tag is unique | `KRG` is registered once in Chaos Redux. No `KRG` tag collision was found in vanilla or the three approved workshop reference mods. | Pass |
| Territory mutation follows exact revalidation | `brilliant_scientist_form_kruger_state_from_verified_plan` calls `brilliant_scientist_revalidate_formation_territory_plan` before its first core, ownership, control, or capital mutation and then requires `brilliant_scientist_formation_territory_plan_can_be_committed`. The revalidator rescans the frozen marks and does not select replacements. | Pass |
| No takeover fallback | Institutional takeover uses `brilliant_scientist_institutional_capture_is_proven`; the territorial planner explicitly excludes takeover. An invalid charter/rebellion/enclave plan does not transform the host. | Pass |
| Takeover retains one country | `brilliant_scientist_transform_host_into_kruger_state` retains the current tag/map, applies the KRG cosmetic identity, and loads the KRG focus tree. | Pass |
| Commit only after successful mutation | Both formation effects initialize `brilliant_scientist_formation_committed` to zero and set it to one only at the end of the successful branch. | Pass |
| No conventional takeover windfall | The conventional helper creates the template but skips manpower, stockpile, fuel, and units when `brilliant_scientist_formed_by_takeover = yes`. | Pass |
| Fully occupied takeover recovery | The initial project-force dispatcher requires an owned and controlled state. `on_state_control_changed` now retries only for the active KRG carrier with no package receipt after it first owns and controls a state. The same dispatcher repeats its carrier, state, transaction, and persistent-receipt checks. | Static pass; retain scenario test |

### Carried portfolio and facility causality

The fixed-tag transaction snapshots all fifteen exact family stages plus suspended, damaged, dismantled, published, stolen, and interrupted-project facts before the former host is reconciled. It carries `brilliant_scientist_formation_carried_project_capacity_gross` and reconstructs outputs from the carried ledger rather than granting a generic technology package.

Physical capabilities are rebuilt only from sites actually inside transferred territory. The old host reconciliation subtracts only paid physical capacity that no longer remains with that host. Durable Directorate modifiers are re-applied from exact receipts rather than inferred from broad route state.

Paleogenetics and xenobiological synthesis remain separate through their histories, site gates, battalions, equipment, technologies, caps, and control requirements. No implicit merger was found.

### Lifecycle note

The fixed-tag route saves `brilliant_scientist_kruger_state_former_host_persistent` as a global target. A clear exists in the world-end transient-target cleanup, but nonterminal disappearance or invalidation of the former host has not yet been demonstrated. Treat target validation/cleanup as a scenario-level lifecycle check, not as a currently proven leak.

## Project-force audit

### Accepted runtime controls

- Every materialization helper requires the short-lived dispatcher transaction, the matching persistent family receipt to be absent, exact carried family history, and a live operational state. Suspended, damaged, or dismantled entries do not authorize output.
- Deployment/weaponization forces require their matching physical network, growth site, assembly complex, reserve/hatchery pair, vat/control-center pair, interface chamber, or authenticated temporal anchor.
- The dispatcher is one-time and idempotent. It sets the global package receipt after bounded family materialization. The state-control recovery hook calls the same guarded dispatcher; it does not create an alternate spawning path.
- All seven bespoke battalions remain `active = no`. There is no `enable_subunits` grant. The country receives locked templates, per-template recruiting permission, and `set_division_template_cap` ceilings.
- Runtime clear revokes recruiting and sets the matching template cap to zero before removing reconstructed force technologies and ideas. Existing formations survive; new recruitment stops.
- Runtime rebuild derives technologies, ideas, control mode, recruiting permission, and ceilings from current operational history. Old-host reconciliation performs an unconditional rebuild after collapse/physical validation.
- Force technologies modify only their matching `kruger_*` battalion. No bonus leaks into vanilla infantry, marine, or other generic battalions.
- Biological history grants only exact biological capability/technology state. It does not create a generic formation or free agent stockpile.

Vanilla precedent supports the mechanism: vanilla defines inactive battalions such as `militia`, creates locked templates containing them, and uses variable-backed `set_division_template_cap` in the MEN, MAN, and JAP levy systems. The effect is also present in the official effect documentation.

### Live caps and opening quantities

| Family | Live ceiling | Prototype opening | Deployment opening | Weaponization opening | Physical/runtime gate |
| --- | ---: | ---: | ---: | ---: | --- |
| Teleportation | 4 | none | 1 | 2 | Operational transit network |
| Cloning | 8 | 1 demonstration, recruiting disabled | 3 | 6 | Operational growth site |
| Robotics | 8 | 1 demonstration, recruiting disabled | 2 | 4 | Operational assembly complex |
| Paleogenetics | 6 | 1 demonstration, recruiting disabled | 2 | 3 | Operational reserve and hatchery |
| Xenobiological synthesis | 6 | 1 demonstration, recruiting disabled | 2 | 3 | Operational vat, control center, and exact control mode |
| Exotic/alien arms | 4 | none | 1 | 2 | Operational interface chamber |
| Temporal | 3 | none | 1 | 1 | Operational authenticated anchor |

All listed opening quantities are below their live ceilings. No later unguarded formation loop was found.

### Downstream project-force blockers

Part 5 requires concrete reinforcement and maintenance systems. The locked templates and equipment production costs are a useful foundation, but they do not yet supply the full gameplay contracts:

- clone growth must consume equipment, medical capacity, food, and time;
- robotics must consume materials, energy, and military production;
- paleogenetic and xenobiological forces need separate food, handler, medical, land/containment, escape, and replacement lifecycles;
- portal forces need terminal access and power;
- temporal forces need synchronization capacity and temporal-debt consequences;
- exotic forces need rare materials and specialized production;
- biological capability needs a bounded stockpile/delivery lifecycle with exact agent identity, containment, replenishment, seizure, use, condemnation, and cleanup;
- AI must understand affordability, reserve requirements, crisis state, and family ceilings for every added decision or mission.

These are downstream KRG decision-system blockers. They must not be replaced by repeatable free-unit effects or generic stockpile grants.

### Reserved-cap reconciliation

The identifier handoff reserves conventional `12` and biological `4` in addition to the seven ceilings above. The live country package currently has:

- a conventional **opening** clamp of `1..8`, with ordinary later recruitment and no explicit interpretation of the reserved `12`; and
- no biological formation, which is causally correct for the current capability-only grant but leaves the meaning of the reserved biological `4` undefined.

Before the decision-system tranche, the parent must promote an explicit interpretation into the source-of-truth design: opening ceiling, concurrent active-operation ceiling, stockpile ceiling, delivery-team ceiling, or another concrete bounded object. No fallback interpretation should be implemented without that disposition.

## Conventional opening-package audit

The current formula is centralized and bounded:

- route bases: charter `1`, rebellion `3`, enclave `1`, takeover `0`;
- increments: former-host army above `30` and `80`, secret Directorate, two guard-strength bands, military office, internal-security section, hardened primary laboratory, facility network above `3`, KRG military industry above `3`, capital population above one million, and former-host war state;
- final opening clamp: `1..8` outside takeover;
- per-division resource ledger: `1,200` manpower, `700` rifles, conditional `100` support equipment, conditional `20` motorized, and `750` fuel;
- six-infantry Laboratory Guard template with engineer/recon support added only when the relevant technology exists;
- opening unit factors and exact granted resources are written to country variables for later audit.

Remaining design/balance gaps:

1. `brilliant_scientist_assigned_guard_strength` is an aggregate strength proxy, not a literal count of assigned laboratory guards as named in Part 5. The spec or implementation should state which is authoritative.
2. Rebellion obtains more resources because its base creates more formations, but there is no separately identified captured-equipment component. If the higher per-division package is intended to represent captured stock, that interpretation should be explicit in the design and localisation.
3. Charter, rebellion/enclave, and takeover liability ideas provide differentiated administration/exodus pressure, but the relative legitimacy and supply outcomes have not been scenario-balanced against the force grants.
4. Starting research slots are a flat minimum of three. Part 5 requires research slots and special-project capacity to scale with facilities rather than giving a one-state enclave the same setup as a major network.
5. No evidence yet demonstrates the required weak enclave, prepared rebellion, armed laboratory network, sovereign arsenal, and catastrophic split bands against their former hosts.

## Focus-tree early audit

### Structurally present

- `common/national_focus/016_brilliant_scientist_kruger_state_focus.txt` contains exactly 100 unique KRG focus IDs.
- Every focus has coordinates; there are no coordinate collisions in the current snapshot.
- All previously identified same-row/backward prerequisite layout anomalies were repaired in both source and architecture.
- Every focus has title, description, and effect-tooltip localisation in `localisation/english/016_brilliant_scientist_focus_l_english.yml`.
- The interface file registers 200 normal/shine sprite IDs backed by 100 intended texture paths.
- Fifteen AI strategy plans are present, and their referenced focus IDs exist.
- The tree does not directly fabricate project stages or use an unbounded free-unit loop.

### Blocking reachability defects

Static producer/consumer comparison across `common/` and `events/` finds 36 `brilliant_scientist_focus_*` flags that are tested but never set:

`biological_containment_operational`, `biological_delivery_verified`, `clone_drift_crisis_resolved`, `clone_growth_burden_payable`, `continental_network_supplied`, `extreme_submission_lock`, `growth_site_verified`, `integration_administration_verified`, `integration_supply_verified`, `integration_target_verified`, `interface_chamber_verified`, `machine_grid_capacity_payable`, `machine_power_and_assembly_verified`, `machine_power_reserve_paid`, `machine_power_reserve_verified`, `maintenance_audit_clear`, `military_reach_verified`, `overextension_mission_clear`, `paleogenetic_reserve_and_hatchery_verified`, `paleogenetic_support_network_verified`, `powered_medical_site_verified`, `prototype_works_burden_verified`, `rare_material_production_verified`, `recognition_path_verified`, `recovery_target_evidence_verified`, `reserve_candidate_verified`, `rogue_node_crisis_resolved`, `successful_project_operation_recorded`, `sustainable_growth_cycle_verified`, `temporal_evidence_verified`, `terminal_network_supplied`, `transit_breach_resolved`, `two_controlled_terminals_verified`, `vat_and_control_center_verified`, `warning_operation_ready`, and `xenobiological_containment_paid`.

Thirty-two focus definitions directly reference at least one missing producer. The most severe is `KRG_reopen_the_prototype_works`, which positively requires `brilliant_scientist_focus_prototype_works_burden_verified`; that blocks every downstream project lane. Sustainable capacity, most family capstones, integration, recovery, commonwealth/submission, and continental-network conclusions also depend on unproduced evidence.

The intended repair is to replace synthetic focus-only proof flags with derived predicates over canonical Event 016 project, facility, resource, incident, and mission state, or to add a real producer owned by the corresponding decision/mission lifecycle. Simply setting every proof flag from an earlier focus would erase the causal burdens.

### Blocking consumer defects

The same static scan finds 306 unique focus-set country flags but only five with a present `has_country_flag` consumer; 301 are currently setter-only. This includes many flags advertising concrete unlocks such as:

- bounded clone, robotics, paleogenetic, xenobiological, portal, temporal, exotic, and biological production/operations;
- maintenance audits, power nodes, growth sites, vat construction, reserve/hatchery designation, terminal links, temporal calibration, and rare-material procurement;
- clone drift, rogue-node, transit-breach, contamination, escape, rivalry, and identity crises;
- recovery targets, former-host settlement, recognition reactions, scientific compacts, submission ultimatums, protectorates, and integration administration.

Some setter-only flags may be intentional historical receipts, but the live tranche lacks the promised decision/mission/event consumers and an authoritative producer/consumer ledger. They cannot be counted as implemented unlocks until that ledger classifies each as consumed, historical-only, queued, or rejected.

### Inspector limitation

The official focus inspector was attempted twice and failed with `ARTIFACT_STORAGE_LIMIT`. Static ID, coordinate, localisation, GFX-reference, AI-reference, and flag-ledger checks were used instead. The focus inspector/render must be rerun after the gate and consumer tranche; this audit does not substitute for that review.

## Asset and visual audit

Current landed Event 016 visual work includes fourteen leader portrait DDS files and six severe-route animation sheet DDS files. The following country assets are still pending production and final root-owned wiring/verification:

- KRG base plus six cosmetic-route flag identities in large, medium, and small sizes: 21 TGA files total;
- 100 focus DDS textures. All 100 registered paths in `interface/016_brilliant_scientist_kruger_state_focus.gfx` are currently missing;
- five starting-spirit icons for Improvised Laboratory State, Inherited Project Portfolio, Fragmented Command, Experimental Supply Chain, and Scientific Exodus.

Only the Warren Kruger stage-0 idea/portrait DDS is present in `gfx/interface/ideas/016_brilliant_scientist/`; the five starting liabilities do not yet have their required final icon package.

Project unit/equipment/technology definitions also rely on generic vanilla picture references in several places. Under the repository's no-fallback rule, those references require explicit approval as final art or replacement by bespoke wired assets. No unapproved generic visual should be silently presented as a completed Event 016 asset.

## Documentation alignment

The following documentation surfaces do not yet describe the live country/force implementation and should be reconciled after the next implementation tranche:

- `docs/events/016_brilliant_scientist.md` still describes focus/flag/icon work as absent or queued;
- `docs/systems/016_brilliant_scientist_projects.md` still places force, focus, and AI work in a later phase;
- there is no current dedicated country/force system document covering the live formation transaction, conventional formula, project-force caps, runtime revocation, recovery hook, and downstream maintenance contracts;
- the focus architecture and implementation handoff must be refreshed after the 36 missing gates and 301 setter-only flags are classified.

The editable event workbook was not changed by this audit. Any later workbook update must be made in `docs/spreadsheets/chaos_redux_events_catalog.xlsx` and followed by `.tools/export_event_catalog_csv.py`; the exported CSV files are not source material.

## Required acceptance scenarios

These are meaningful scenario checks for the next country/decision audit. They are not claimed as executed here.

1. **Peaceful charter, weak host:** exact marked states transfer; host survives; KRG receives the low conventional band; no project unit appears without matching carried stage and site.
2. **Prepared rebellion:** host-army, guard, office, hardening, population, facility, industry, and war inputs produce the expected bounded conventional count and exact resource ledger; the former-host war begins as designed.
3. **Weak enclave:** the smallest valid territory opens with a survivable but genuinely weak package and no flat three-slot/facility-capacity overgrant beyond the approved scale.
4. **Armed network / sovereign arsenal / catastrophic split:** multiple Deployment or Weaponization families remain within per-family caps and do not automatically overpower the former host; liability and containment pressure scale with the opening.
5. **Institutional takeover:** the existing army and stockpiles remain; no conventional manpower, equipment, fuel, or unit grant occurs; no duplicate KRG tag or character appears.
6. **Fully occupied takeover:** formation commits without spawning; the first later state-control recovery binds the carrier and applies the exact one-time package; a second state-control change creates nothing.
7. **Idempotency:** direct repeated calls to the dispatcher and individual family helpers cannot duplicate formations, templates, stockpiles, or receipts.
8. **Damaged history:** suspended, damaged, and dismantled stages retain history but grant no runtime recruiting, technology, idea, or new formation until exact repair/resume.
9. **Physical loss and recovery:** losing a required site revokes recruiting/caps/bonuses without deleting surviving formations; restoring the exact site reconstructs only the authorized runtime package and never rematerializes the opening force.
10. **Paleogenetic/xenobiological separation:** each family functions, fails, and recovers independently; no shared gate, equipment, control mode, or cap merges them before explicit Synthesis.
11. **Biological bounded lifecycle:** after implementation, exact agents cannot be duplicated, free-stockpiled, or retained after seizure/dismantlement; delivery, containment, and consequence ledgers remain causal.
12. **Focus reachability:** charter, rebellion, enclave, and takeover starts can reach their intended openings; every positive burden gate has a reachable canonical producer; every advertised unlock has a live consumer; mutually exclusive conclusions remain exclusive.
13. **Asset completeness:** every KRG/cosmetic flag, starting spirit, and focus icon resolves to a final file at every required size/state with no undeclared fallback.

## Recommended implementation order

1. Finish the focus derived-predicate repair and publish the exact producer/consumer ledger.
2. Implement the KRG decisions/missions that own project growth, maintenance, biological stockpile/delivery, crises, recovery, and integration.
3. Reconcile conventional `12` and biological `4` into explicit bounded runtime objects and update the binding spec/identifier handoff.
4. Scale research slots and special-project capacity from retained facilities and validate the five opening-force bands against former-host strength.
5. Land and wire all country assets, then run the final read-only asset audit.
6. Refresh country/project docs and any event-catalog facts from the implemented wording.
7. Rerun the official focus inspector/render and the country, decision/mission, localisation, asset, and event-completion audit routes before any completion claim.

## Skills used

- `chaos-redux-subagents` for audit ownership, evidence boundaries, and handoff structure;
- `chaos-redux-events` for Event 016 integration and completion expectations;
- `hoi4-focus-trees` for the 100-focus structural, localisation, AI, reachability, and asset audit.

No skill was created or modified by this audit.
