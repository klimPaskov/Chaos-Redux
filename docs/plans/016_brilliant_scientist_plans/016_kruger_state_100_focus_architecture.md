# Event 016 Kruger State: exact 100-focus architecture

Date: 2026-07-16

Status: accepted architecture implemented in the Event 016 focus tranche. All 180 focus-produced contracts have executable consumers; the implementation handoff and consumer ledger record the exact downstream wiring. All 100 focus icon DDS files are present in the runtime asset folder; engine render and parent visual acceptance remain outstanding.

## Fixed implementation contract

The tree ID is `brilliant_scientist_kruger_state_focus_tree`, matching the two existing `load_focus_tree` calls in `common/scripted_effects/016_brilliant_scientist_country_effects.txt`. The tree is allowed only for a country satisfying `brilliant_scientist_is_active_kruger_state = yes`.

The architecture contains exactly 100 manually authored focuses. A campaign sees the common state-building lanes, its one fixed formation-origin opener, and only the project branches supported by Warren Kruger's carried project history. The tree never creates a missing project stage, invents an absent project army, or calls any `brilliant_scientist_spawn_*_project_force` effect. Project focuses unlock or improve physical infrastructure, production decisions, missions, templates, and operational systems. The existing one-time formation dispatcher remains the only source of inherited opening project formations.

The labels below match the final English focus titles. Every focus has its own stable `94x86` icon contract. Visual direction follows its lane: survival, government, laboratory economy, conventional security, cloning, robotics, paleogenetics, xenobiology, quantum transit, temporal operations, exotic energy, biological warfare, diplomacy, integration, world conquest, or singularity.

### Prerequisite notation

- `A + B` means two separate `prerequisite` blocks and therefore AND.
- `{A | B}` means one `prerequisite` block containing both focuses and therefore OR.
- `mutex A/B` is a symmetric `mutually_exclusive` relation.
- A bypass never grants the focus reward. Bypasses are used only for a crisis already resolved through its proper mission or for a route made obsolete by world end.

### Duration constants

The focus file should define same-file cost constants because `cost` is a technical field whose support for `constant:` tokens must not be assumed.

| Token | Days | Focus cost | Use |
| --- | ---: | ---: | --- |
| `D21` | 21 | 3 | Formation emergency work |
| `D35` | 35 | 5 | Tactical unlock or narrow institutional change |
| `D70` | 70 | 10 | Standard branch development |
| `D105` | 105 | 15 | Route or project capstone |
| `D140` | 140 | 20 | Terminal doctrine commitment |

The 21-day value is a technical three-week duration. All balance values used by rewards belong in `common/script_constants/016_brilliant_scientist_focus_constants.txt`; focus blocks should not repeat tuning literals.

### AI weight constants

Rows use the existing values from `brilliant_scientist_country`: `X = 0`, `L = 1`, `S = 5`, `H = 10`, and `P = 20`. A condition after the token is the modifier condition. Invalid project, origin, and terminal routes remain `X`, not merely low-weight.

### Visibility and availability gates

`allow_branch` is reserved for fixed origin facts, inherited project-route visibility, and enabled Evolution IV terminal content. Live resource, facility, debt, war, and crisis checks belong in `available`. Whenever an Event 016 project first reaches the stage that changes one of these branch-visibility predicates, the project-stage effect must call `mark_focus_tree_layout_dirty`.

| Token | Exact gate |
| --- | --- |
| `ACTIVE` | `brilliant_scientist_is_active_kruger_state = yes`, no Event 016 terminal lock, and no shared `world_end` |
| `C/R/E/T` | `brilliant_scientist_formed_by_charter/rebellion`, `brilliant_scientist_formed_as_enclave`, or `brilliant_scientist_formed_by_takeover` |
| `CLN` | `brilliant_scientist_has_cloning_route_seed`; stage gates use `brilliant_scientist_has_cloning_force_history_{prototype,deployment,weaponization}` and the physical `...force_deployment` gate |
| `ROB` | `brilliant_scientist_has_robotics_route_seed`; stage gates use the matching robotics force-history and physical-deployment triggers |
| `PAL` | `brilliant_scientist_has_paleogenetics_route_seed`; stage gates use the matching paleogenetics triggers and retain reserve plus hatchery checks |
| `XEN` | `brilliant_scientist_has_xenobiological_route_seed`; stage gates use the matching xenobiological triggers plus `brilliant_scientist_has_exact_xeno_control_mode` |
| `POR` | `brilliant_scientist_has_teleportation_route_seed`; operational gates use the matching teleportation deployment and weaponization triggers |
| `TMP` | `brilliant_scientist_has_temporal_route_seed`; operational gates use the matching temporal deployment and weaponization triggers, authenticated anchor, synchronization, and debt checks |
| `ALI` | `brilliant_scientist_has_alien_arms_route_seed`; operational gates use the matching alien-arms deployment and weaponization triggers |
| `BIO` | `brilliant_scientist_has_biological_route_seed`; stage gates use the matching biological force-history triggers and exact personal agent flags |
| `ENE` | `brilliant_scientist_has_high_energy_route_seed`; Deployment and Weaponization read `brilliant_scientist_project_stage_entries^4` |
| `RKT` | `brilliant_scientist_has_rocketry_route_seed`; Deployment and Weaponization read `brilliant_scientist_project_stage_entries^3` |
| `MIX` | `brilliant_scientist_has_multiple_sovereign_project_routes = yes`; Synthesis additionally requires Paleogenetics and Xenobiological Synthesis at Deployment or higher |
| `E4` | Evolution IV chronology recorded and the corresponding world-end scenario not disabled |

No focus availability gate reads a focus-only verification receipt. The KRG trigger layer derives every such condition from authoritative Event 016 state: paid Directorate facility and institution flags, physical project-site markers, event targets, project deployment and can-pay triggers, incident ledgers, exact resources, containment technologies, foreign-framework history, war state, temporal synchronization/debt, and former-host facility evidence. Crisis bypasses read the canonical Cloning, Robotics, or Teleportation `*_incident_resolved` flag. Historical focus checks use `has_completed_focus = KRG_*`; the tree does not duplicate them into 100 setter-only `_completed` flags.

## Layout overview

```text
                     001 audit inherited portfolio
              charter / rebellion / enclave / takeover
        staff -------- heartland -------- supply -------- command
                     010 founding audit complete
                                |
      economy ---- government ---- conventional security ---- diplomacy
         |              |                    |                    |
      supply      human/clone/machine    ordinary army       former host
      choice      temporal/xeno/mixed    and intelligence    world posture
         \              |                    |                  /
          \---- eight project-force and strategic lanes ------/
                               |
                  corridors, facilities, integration
                               |
                   098 Evolution IV sovereign science
                         /                       \
          099 Laboratory World       100 Strategic Singularity
```

The actual coordinate canvas runs from `x = 0` through `x = 53` and `y = 0` through `y = 20`. Deep political capstones sit beside the project lane that proves their availability, avoiding long crossing lines through the opening.

## Focus ledger: 001-010, formation and survival

| # | ID and working label | x,y / duration | Prerequisites and mutex | Gate | Concrete reward and hook | AI |
| ---: | --- | --- | --- | --- | --- | --- |
| 001 | `KRG_audit_inherited_portfolio` — Audit the Inherited Portfolio | 24,0 / D35 | none | ACTIVE | Rebuild the runtime package with `brilliant_scientist_rebuild_project_force_runtime_package`, preserve any interrupted-project diagnostic values for the audit surface, and unlock the Kruger State administration category. It never calls the formation spawn dispatcher. | P until complete |
| 002 | `KRG_ratify_the_charter_transfer` — Ratify the Charter Transfer | 18,1 / D21 | 001 | allow C; available ACTIVE | Confirm the charter border and former-host compact, activate the two-year truce-monitor mission, and unlock negotiated rail, archive, and research-access decisions. | P C; X otherwise |
| 003 | `KRG_hold_the_rebellion_perimeter` — Hold the Rebellion Perimeter | 22,1 / D21 | 001 | allow R; available ACTIVE | Activate a named primary-facility defense mission, add fortification and anti-air construction to that actual state, and set the former host as the first military planning target. | P R; X otherwise |
| 004 | `KRG_keep_the_enclave_alive` — Keep the Enclave Alive | 26,1 / D21 | 001 | allow E; available ACTIVE | Activate the corridor-or-patron survival mission, unlock emergency rail/port access negotiations, and register the enclave supply deficit. No factories or divisions appear for free. | P E; X otherwise |
| 005 | `KRG_secure_the_captured_ministries` — Secure the Captured Ministries | 30,1 / D21 | 001 | allow T; available ACTIVE | Start the institutional-consolidation mission, audit captured state-wide domains, remove obsolete host appointments through an event, and preserve takeover as an institutional origin rather than a territorial one. | P T; X otherwise |
| 006 | `KRG_count_the_surviving_staff` — Count the Surviving Staff | 18,2 / D21 | {002 OR 003 OR 004 OR 005} | ACTIVE | Build the finite assistant and scientist roster from actual transferred characters, unlock amnesty/recruitment decisions, and register missing specialist roles. | P while Scientific Exodus is active |
| 007 | `KRG_secure_the_laboratory_heartland` — Secure the Laboratory Heartland | 22,2 / D21 | {002 OR 003 OR 004 OR 005} | ACTIVE; valid primary facility owned and controlled | Repair one facility level or its documented capability in the real primary state, activate the primary-site security mission, and preserve the global facility target. | P if facility damaged; H otherwise |
| 008 | `KRG_repair_the_supply_spine` — Repair the Supply Spine | 26,2 / D21 | {002 OR 003 OR 004 OR 005} | ACTIVE | Unlock a targeted rail, port, or infrastructure repair decision chosen from the capital-to-primary-facility route; provide trains and trucks only through paid recovery missions. | P if out of supply; H otherwise |
| 009 | `KRG_form_the_provisional_command` — Form the Provisional Command | 30,2 / D21 | {002 OR 003 OR 004 OR 005} | ACTIVE | Appoint conventional commanders from surviving officers, unlock force-cap and maintenance readouts, and expose the Fragmented Command lifecycle choice. No new formation is created. | P if at war; H otherwise |
| 010 | `KRG_complete_the_founding_audit` — Complete the Founding Audit | 24,3 / D35 | 006 + 007 + 008 + 009 | ACTIVE | Close the origin emergency once its mission is resolved, refresh formation facts, unlock government, economy, security, diplomacy, and valid project lanes, and fire the state-foundation policy event. | P |

## Focus ledger: 011-030, government and population status

The seven identity capstones `014`, `017`, `021`, `025`, `028`, `029`, and `030` are pairwise mutually exclusive. Their openers are not mutually exclusive because early constitutional debate is not itself a route lock. Completing a capstone sets one route flag, one cosmetic identity, one government package, and one administration-idea swap through an exact country effect.

| # | ID and working label | x,y / duration | Prerequisites and mutex | Gate | Concrete reward and hook | AI |
| ---: | --- | --- | --- | --- | --- | --- |
| 011 | `KRG_define_the_states_purpose` — Define the State's Purpose | 24,4 / D35 | 010 | ACTIVE | Fire the constitutional congress event, expose population shares and project blocs, and open only project-supported identity branches. | P |
| 012 | `KRG_preserve_the_directorate` — Preserve the Directorate | 8,5 / D70 | 011 | ACTIVE | Retain personal Directorate authority, unlock direct appointments and laboratory decrees, and accept higher foreign suspicion in exchange for faster crisis response. | H R/T; S C/E |
| 013 | `KRG_rule_by_demonstration` — Rule by Demonstration | 8,6 / D70 | 012 | ACTIVE; one successful project operation | Unlock public demonstration and coercive-science decisions. Each demonstration consumes a real project output and can increase Exposure or world threat. | H with high Grievance; S otherwise |
| 014 | `KRG_the_sovereign_directorate` — The Sovereign Directorate | 8,7 / D105 | 013; mutex every other identity capstone | ACTIVE | Call a required `brilliant_scientist_form_sovereign_directorate` effect, swap Improvised Laboratory State into a personal-administration successor, and unlock the direct-rule AI plan. | H violent/high Grievance; X after another identity |
| 015 | `KRG_restore_human_government` — Restore Human Government | 13,5 / D70 | 011 | ACTIVE | Establish a civil service and rights commission, unlock human-administration integration decisions, and prohibit clone property and full human replacement. | H C/public history; L extreme route |
| 016 | `KRG_convene_the_scientific_assembly` — Convene the Scientific Assembly | 13,6 / D70 | 015 | ACTIVE | Create an elected scientific assembly through an event, unlock public budget and inspection decisions, and strengthen recognition without granting it automatically. | H low Grievance; S otherwise |
| 017 | `KRG_the_human_scientific_republic` — The Human Scientific Republic | 13,7 / D105 | 016; mutex every other identity capstone | ACTIVE | Call `brilliant_scientist_form_human_scientific_republic`, swap in Civic Laboratory Administration, and unlock commonwealth diplomacy plus rights-respecting integration. | P C with low Grievance; X after another identity |
| 018 | `KRG_hear_the_replicated_petition` — Hear the Replicated Petition | 18,5 / D35 | 011 | allow CLN; available CLN prototype | Fire a clone-personhood event and unlock the legal-status decision family without changing force cap or creating bodies. | H clone route; X absent CLN |
| 019 | `KRG_clones_are_citizens` — Clones Are Citizens | 17,6 / D70 | 018; mutex 020 | CLN deployment | Set the citizen-clone law, unlock settlement and education decisions, and prohibit clone-property production bonuses. | H C/low Grievance; S otherwise |
| 020 | `KRG_clones_are_cohorts` — Clones Are Cohorts | 19,6 / D70 | 018; mutex 019 | CLN deployment | Set the bounded cohort hierarchy, unlock military maturation priorities, and create identity-pressure and revolt counterplay rather than a flat manpower bonus. | H R/extreme; X morally restrictive plan |
| 021 | `KRG_replicated_sovereignty` — Replicated Sovereignty | 18,7 / D105 | {019 OR 020}; mutex every other identity capstone | CLN weaponization; stable growth site | Call `brilliant_scientist_form_replicated_state`, swap in Replication Administration, and unlock population-majority transition only after measured clone population crosses its ledger threshold. | P clone AI with sustainable equipment/medical capacity |
| 022 | `KRG_hear_the_machine_network` — Hear the Machine Network | 24,5 / D35 | 011 | allow ROB; available ROB prototype | Fire the network-standing event, expose active nodes and power burden, and unlock machine-status decisions. | H robotics route; X absent ROB |
| 023 | `KRG_human_machine_partnership` — Human-Machine Partnership | 23,6 / D70 | 022; mutex 024 | ROB deployment | Lock human supervisory keys, unlock mixed administration and repair teams, and retain human citizenship. | H C/charter; S otherwise |
| 024 | `KRG_the_replacement_protocol` — The Replacement Protocol | 25,6 / D70 | 022; mutex 023 | ROB weaponization; adequate power | Unlock staged ministry replacement missions. Each transition requires a functioning node and creates sabotage and network-schism risks. | H takeover/extreme; X severe power deficit |
| 025 | `KRG_machine_ascendancy` — Machine Ascendancy | 24,7 / D105 | {023 OR 024}; mutex every other identity capstone | ROB weaponization; power and assembly complex valid | Call `brilliant_scientist_form_machine_state`, swap in Machine Laboratory Administration, and permit the nonhuman classification only after the machine-majority effect is separately satisfied. | P machine AI with power reserve; X absent/unstable network |
| 026 | `KRG_authenticate_krugers_continuity` — Authenticate Kruger's Continuity | 43,13 / D70 | 011 + 077 | allow TMP; available authenticated anchor and noncritical debt | Compare ledgers, witnesses, and anchor records through an event. It locks no origin conclusion by itself and cannot erase prior temporal uses. | H temporal AI below severe debt; X critical debt |
| 027 | `KRG_settle_the_succession_paradox` — Settle the Succession Paradox | 43,14 / D70 | 026 | TMP deployment; 081 complete or stabilization not required | Unlock a one-time Prime-versus-Council succession event, record the selected authority, and create a persistent scar if contradictory claimants remain. | H after successful stabilization; S otherwise |
| 028 | `KRG_the_temporal_continuum` — The Temporal Continuum | 43,15 / D105 | 027 + 081; mutex every other identity capstone | TMP deployment; authenticated anchor; debt below critical | Call `brilliant_scientist_form_temporal_continuum`, swap in its administration package, and unlock Continuum government decisions without refreshing synchronization or clearing debt. | P stable temporal plan; X critical debt/anchor loss |
| 029 | `KRG_xenobiological_ascendancy` — Xenobiological Ascendancy | 33,14 / D105 | 011 + 071; mutex every other identity capstone | allow XEN; available XEN weaponization and exact control mode | Call `brilliant_scientist_form_xenobiological_ascendancy`; unlock engineered-population transition only after real population/control thresholds, and preserve origin uncertainty unless independent proof exists. | H stable XEN weaponization; X control crisis |
| 030 | `KRG_the_project_synthesis` — The Project Synthesis | 29,15 / D105 | 011 + 065 + 071; mutex every other identity capstone | allow MIX; available PAL deployment + XEN deployment + at least one additional sovereign project route | Call required `brilliant_scientist_can_unlock_synthesis`/`...unlock_synthesis` validation, then `brilliant_scientist_form_project_synthesis`. Paleogenetic and xenobiological ledgers remain separate after political convergence. | P mixed AI with sustainable burdens; X if either biology family is absent |

## Focus ledger: 031-040, laboratory economy and logistics

Focuses `036` through `039` are mutually exclusive supply doctrines. They swap the Experimental Supply Chain liability one-for-one and never stack. `040` is reachable through one OR prerequisite block containing the four doctrines.

| # | ID and working label | x,y / duration | Prerequisites and mutex | Gate | Concrete reward and hook | AI |
| ---: | --- | --- | --- | --- | --- | --- |
| 031 | `KRG_stabilize_the_laboratory_economy` — Stabilize the Laboratory Economy | 2,4 / D35 | 010 | ACTIVE | Unlock the facility-budget ledger, expose reserved factory/capacity burdens, and prohibit new expansion decisions while maintenance is unpaid. | P |
| 032 | `KRG_restore_the_power_grid` — Restore the Power Grid | 0,5 / D70 | 031 | ACTIVE; valid primary state | Add one infrastructure and one state-level power/facility capability through a targeted helper, then unlock paid grid-expansion decisions. | P machine/portal/temporal; H otherwise |
| 033 | `KRG_reconnect_rail_and_port` — Reconnect Rail and Port | 2,5 / D70 | 031 | ACTIVE | Repair or construct the shortest valid capital-to-facility railway segment and unlock a port alternative only for a coastal state. | P E/R; H otherwise |
| 034 | `KRG_document_the_carried_portfolio` — Document the Carried Portfolio | 4,5 / D70 | 031 | ACTIVE | Call `brilliant_scientist_document_inherited_portfolio`, expose exact family stages and maintenance, and unlock project-specific replication/standardization decisions. | P while inherited/fragmented portfolio idea is active |
| 035 | `KRG_reopen_the_prototype_works` — Reopen the Prototype Works | 2,6 / D70 | 032 + 033 + 034 | ACTIVE; capacity and factory burden payable | Repair one actual prototype works or unlock a targeted construction decision, increase usable project capacity through the existing board, and open valid production lanes. | P if any project force history; H otherwise |
| 036 | `KRG_conventional_supply_corps` — Conventional Supply Corps | 0,7 / D70 | 035; mutex 037/038/039 | ACTIVE | Call `brilliant_scientist_establish_conventional_supply`, unlock truck/train depot decisions, and favor ordinary infantry reliability. | P weak/mixed enclave; S advanced routes |
| 037 | `KRG_automated_supply_network` — Automated Supply Network | 2,7 / D70 | 035; mutex 036/038/039 | allow ROB; available ROB deployment and paid power reserve | Call `brilliant_scientist_establish_automated_supply`, unlock node-repair convoys, and tie supply benefits to live power and assembly capacity. | P machine plan; X power deficit |
| 038 | `KRG_portal_supply_network` — Portal Supply Network | 4,7 / D70 | 035; mutex 036/037/039 | allow POR; available POR deployment and two controlled terminals | Call `brilliant_scientist_establish_portal_supply`, unlock terminal-depot linking, and retain energy/fuel and terminal-defense burdens. | P separated sites; X fewer than two terminals |
| 039 | `KRG_biological_supply_network` — Biological Supply Network | 6,7 / D70 | 035; mutex 036/037/038 | allow CLN/PAL/XEN/BIO; available one matching Deployment stage | Call `brilliant_scientist_establish_biological_supply`, unlock medical/feed/reagent logistics appropriate to the exact family, and never merge Paleogenetic feed with Xenobiological reagents. | P clone/biology dominant; X absent family |
| 040 | `KRG_sustainable_project_capacity` — Sustainable Project Capacity | 3,8 / D105 | {036 OR 037 OR 038 OR 039} | ACTIVE; all active-family maintenance paid | Unlock the capped project-force production board, a maintenance audit mission, and expansion brakes that block new force cycles when supply or factory burden is unsafe. No force cap rises. | P before new force production |

## Focus ledger: 041-047, conventional security

`046` and `047` are mutually exclusive command solutions. Machine and clone political routes may later replace the selected command idea with their exact machine-command or clone-officer lifecycle effect, but the ideas never stack.

| # | ID and working label | x,y / duration | Prerequisites and mutex | Gate | Concrete reward and hook | AI |
| ---: | --- | --- | --- | --- | --- | --- |
| 041 | `KRG_restore_the_ordinary_chain_of_command` — Restore the Ordinary Chain of Command | 10,9 / D35 | 010 | ACTIVE | Unlock conventional recruitment, training, and garrison templates using ordinary equipment; expose the live conventional cap without spawning divisions. | P at war; H otherwise |
| 042 | `KRG_recall_the_defector_officers` — Recall the Defector Officers | 8,10 / D70 | 041 | ACTIVE | Recover only officers recorded in the formation ledger, add bounded command experience, and open an amnesty-versus-purge event shaped by origin. | H R/T; S C/E |
| 043 | `KRG_laboratory_engineer_battalions` — Laboratory Engineer Battalions | 10,10 / D70 | 041 | ACTIVE | Unlock engineer support and paid facility-repair missions; add no free battalions or equipment stockpile. | P damaged facilities; H otherwise |
| 044 | `KRG_found_the_counterintelligence_bureau` — Found the Counterintelligence Bureau | 12,10 / D70 | 041 | ACTIVE | Create an intelligence agency only if absent, otherwise grant a relevant upgrade; unlock archive, assistant, terminal, and control-channel counterintelligence operations. | P high Exposure/violent origin; H otherwise |
| 045 | `KRG_shield_the_laboratory_airspace` — Shield the Laboratory Airspace | 10,11 / D70 | 043 + 044 | ACTIVE; controlled primary facility | Add one radar and bounded anti-air construction to a valid facility state and unlock missile/air warning missions. | P enemy air threat; S otherwise |
| 046 | `KRG_a_general_staff_for_the_state` — A General Staff for the State | 9,12 / D105 | 045; mutex 047 | ACTIVE | Call `brilliant_scientist_establish_general_staff_command`, unlock ordinary battle plans and project-support attachments, and favor disciplined combined arms. | P human/conventional AI; S otherwise |
| 047 | `KRG_a_council_of_project_commanders` — A Council of Project Commanders | 11,12 / D105 | 045; mutex 046 | ACTIVE; at least two project-force histories | Call `brilliant_scientist_establish_project_council_command`, unlock multi-family coordination decisions, and add rivalry crises when incompatible burdens are ignored. | P mixed-project AI; X fewer than two families |

## Focus ledger: 048-053, cloning and the replicated army

| # | ID and working label | x,y / duration | Prerequisites and mutex | Gate | Concrete reward and hook | AI |
| ---: | --- | --- | --- | --- | --- | --- |
| 048 | `KRG_audit_the_growth_halls` — Audit the Growth Halls | 15,9 / D35 | 035 | allow CLN; available CLN prototype | Unlock the clone infrastructure category, audit surviving growth sites, and preserve the exact inherited stage. | P clone plan; X absent CLN |
| 049 | `KRG_secure_the_nutrient_chain` — Secure the Nutrient Chain | 14,10 / D70 | 048 | CLN prototype; medical and equipment burden payable | Unlock paid growth-site, medical, food-proxy, and maturation decisions. It does not add manpower directly. | P manpower need with supply; X famine/medical collapse |
| 050 | `KRG_write_the_identity_register` — Write the Identity Register | 16,10 / D70 | 048 | CLN prototype | Create an identity/authentication ledger, unlock infiltrator detection and personhood disputes, and support the citizen route without forcing it. | H all clone plans |
| 051 | `KRG_field_the_clone_cadres` — Field the Clone Cadres | 14,11 / D70 | 049 + 050 | CLN physical Deployment | Call `brilliant_scientist_rebuild_project_force_runtime_package`, unlock the `Replicated Guard Cadre` recruitment decision, and enforce growth-site, equipment, time, and cap checks. | P if under clone cap and supplied; X otherwise |
| 052 | `KRG_stabilize_replication_drift` — Stabilize Replication Drift | 16,11 / D70 | 050 + 044 | CLN deployment | Unlock an identity-crisis mission, assistant mediation, and one-time registry repair. Bypass only if the drift crisis was already resolved. | P active drift; H high clone population |
| 053 | `KRG_the_replicated_host` — The Replicated Host | 15,12 / D105 | 051 + 052 | CLN weaponization; sustainable growth cycle | Call the runtime rebuild, unlock bounded mature-cohort production up to the existing clone cap of 8, and call `brilliant_scientist_establish_clone_officer_corps` only for the Replicated Sovereignty route. | P clone route with equipment/medical surplus; X unsupplied |

## Focus ledger: 054-059, robotics and autonomous command

| # | ID and working label | x,y / duration | Prerequisites and mutex | Gate | Concrete reward and hook | AI |
| ---: | --- | --- | --- | --- | --- | --- |
| 054 | `KRG_wake_the_assembly_lines` — Wake the Assembly Lines | 21,9 / D35 | 035 | allow ROB; available ROB prototype | Unlock the robotics production category, audit surviving assembly sites, and preserve the exact inherited stage. | P robotics plan; X absent ROB |
| 055 | `KRG_secure_the_machine_power_backbone` — Secure the Machine Power Backbone | 20,10 / D70 | 054 | ROB prototype; grid capacity payable | Designate paid machine power nodes and register their fuel/resource burden. Loss of the nodes suppresses production. | P if power deficit can be solved; X otherwise |
| 056 | `KRG_standardize_frame_repair` — Standardize Frame Repair | 22,10 / D70 | 054 | ROB prototype | Unlock frame repair, salvage, and maintenance decisions that consume factories, support equipment, and rare materials. | H damaged frames/assembly; S otherwise |
| 057 | `KRG_write_the_machine_command_protocol` — Write the Machine Command Protocol | 20,11 / D70 | 055 + 056 | ROB physical Deployment | Call the runtime rebuild, unlock `Autonomous Frame Cohort` recruitment, and require an air-gapped human or machine command choice. | P machine route; H other robotics routes |
| 058 | `KRG_air_gap_the_rogue_nodes` — Air-Gap the Rogue Nodes | 22,12 / D70 | 057 + 044 | ROB deployment | Unlock a rogue-node containment mission, physical shutdown decisions, and a controlled recapture path. Bypass only after the network crisis is resolved. | P compromised network; H otherwise |
| 059 | `KRG_an_army_of_machines` — An Army of Machines | 21,13 / D105 | 057 + 058 | ROB weaponization; assembly and power valid | Call the runtime rebuild, unlock bounded frame production up to the existing robotics cap of 8, and call `brilliant_scientist_establish_machine_command` only for Machine Ascendancy. | P machine route with power/material surplus; X unsafe maintenance |

## Focus ledger: 060-065, paleogenetics and restored terrestrial creatures

This lane uses only restored terrestrial organisms, reserves, hatcheries, feed, handlers, transport, and veterinary capacity. It shares no facility, equipment, production counter, failure dispatcher, or countermeasure progress with Xenobiological Synthesis.

| # | ID and working label | x,y / duration | Prerequisites and mutex | Gate | Concrete reward and hook | AI |
| ---: | --- | --- | --- | --- | --- | --- |
| 060 | `KRG_open_the_restoration_ledger` — Open the Restoration Ledger | 27,9 / D35 | 035 | allow PAL; available PAL prototype | Unlock the Paleogenetics category, list actual restored lineages, and preserve the independent project ledger. | P PAL plan; X absent PAL |
| 061 | `KRG_designate_breeding_reserves` — Designate Breeding Reserves | 26,10 / D70 | 060 | PAL prototype; valid low-density controlled state | Unlock a targeted reserve/hatchery designation decision with land, feed, and construction costs; set no state marker before payment and completion. | P suitable land/feed; X no viable state |
| 062 | `KRG_train_handlers_and_veterinarians` — Train Handlers and Veterinarians | 28,10 / D70 | 060 | PAL prototype | Unlock finite handler recruitment and veterinary support missions, using manpower, support equipment, trucks, and time. | P if handler deficit; H otherwise |
| 063 | `KRG_build_the_transport_pens` — Build the Transport Pens | 26,11 / D70 | 061 + 062 | PAL physical Deployment | Call the runtime rebuild, unlock `Paleogenetic Shock Pack` recruitment, and add paid transport-pen and railway loading decisions. | P rough-terrain/transport need; X no reserve/hatchery |
| 064 | `KRG_drill_for_the_great_escape` — Drill for the Great Escape | 28,12 / D70 | 063 | PAL deployment | Unlock escape-response, civilian evacuation, feed-denial, and recapture missions; add anti-air vulnerability and anti-armor counterplay to the public tooltip. | P active escape/ecological risk; H otherwise |
| 065 | `KRG_the_dinosaur_host` — The Dinosaur Host | 27,13 / D105 | 063 + 064 | PAL weaponization; reserve, hatchery, handlers, transport all valid | Call the runtime rebuild and unlock bounded breeding cycles up to the existing Paleogenetics cap of 6. The focus adds no creature formation itself. | P PAL route with feed/logistics surplus; X otherwise |

## Focus ledger: 066-071, xenobiological synthesis and engineered organisms

This lane uses vats, medical fabrication, reagents, power, sealed cells, and one exact control method. It does not consume Paleogenetic reserves or handlers and does not create restored species.

| # | ID and working label | x,y / duration | Prerequisites and mutex | Gate | Concrete reward and hook | AI |
| ---: | --- | --- | --- | --- | --- | --- |
| 066 | `KRG_open_the_designed_organism_dossier` — Open the Designed Organism Dossier | 33,9 / D35 | 035 | allow XEN; available XEN prototype | Unlock the Xenobiological Synthesis category, list actual designs, and preserve the selected-control ledger separately from Paleogenetics. | P XEN plan; X absent XEN |
| 067 | `KRG_build_the_vat_complexes` — Build the Vat Complexes | 32,10 / D70 | 066 | XEN prototype; valid powered medical site | Unlock targeted vat-complex and medical-fabrication construction using reagents, power, factories, and containment capacity. | P fort-break/lab-defense need; X no powered site |
| 068 | `KRG_lock_the_control_channel` — Lock the Control Channel | 34,10 / D70 | 066 | XEN prototype | If no mode exists, fire one exclusive chemical, neural, machine-linked, or researched-control event. If a coherent mode already exists, bypass without changing it. Contradictory modes block the branch. | P before Deployment; X incoherent history |
| 069 | `KRG_seal_the_containment_cells` — Seal the Containment Cells | 32,11 / D70 | 067 + 068 | XEN physical Deployment and exact mode | Call the runtime rebuild, unlock `Xenobiological Assault Organisms` recruitment, and require live vat plus control-center state markers. | P if lab defense/fort-breaking needed; X invalid control |
| 070 | `KRG_red_team_the_autonomous_nest` — Red-Team the Autonomous Nest | 34,12 / D70 | 069 + 044 | XEN deployment | Unlock control-channel countertests, autonomous-nest containment, and handler-amnesty operations specific to the chosen mode. | P active control risk; H otherwise |
| 071 | `KRG_the_engineered_legion` — The Engineered Legion | 33,13 / D105 | 069 + 070 | XEN weaponization; exact control and paid containment valid | Call the runtime rebuild and unlock bounded engineered-organism production up to the existing Xenobiological cap of 6. No Paleogenetic output is granted. | P XEN route with reagent/power surplus; X otherwise |

## Focus ledger: 072-076, quantum transit and portal warfare

| # | ID and working label | x,y / duration | Prerequisites and mutex | Gate | Concrete reward and hook | AI |
| ---: | --- | --- | --- | --- | --- | --- |
| 072 | `KRG_recover_the_transit_logs` — Recover the Transit Logs | 39,9 / D35 | 035 | allow POR; available POR route seed | Unlock the terminal audit category and identify only inherited or rebuilt terminals. Prototype history alone grants no strategic movement. | P separated-site plan; X absent POR |
| 073 | `KRG_harden_the_terminal_rings` — Harden the Terminal Rings | 38,10 / D70 | 072 | POR physical Deployment | Unlock paid fortification, independent shutdown, and dual-key decisions for each named terminal; loss of power closes the link. | P exposed terminals; H otherwise |
| 074 | `KRG_link_the_depot_network` — Link the Depot Network | 40,10 / D70 | 072 + 033 | POR physical Deployment; at least two controlled terminals | Unlock bounded equipment/specialist transit and terminal supply links. It moves existing assets and never creates a unit or stockpile. | P multi-site/enclave; X fewer than two terminals |
| 075 | `KRG_close_the_transit_breach` — Close the Transit Breach | 38,11 / D70 | 073 | POR deployment | Unlock breach-perimeter, calibration-archive destruction, and compromised-terminal closure missions; bypass only after a real breach is resolved. | P breach active; H high Exposure |
| 076 | `KRG_the_strategic_transit_corps` — The Strategic Transit Corps | 39,12 / D105 | 074 + 075 | POR weaponization; terminal network supplied | Call the runtime rebuild and unlock capped raider recruitment up to the live portal cap plus paid strategic insertion missions. | P defended network and distant targets; X exposed terminals |

## Focus ledger: 077-082, temporal operations and the continuity guard

Every operational reward in this lane binds one named semantic target, spends synchronization capacity, adds temporal debt, records the target ID permanently, and may add a scar. No focus refreshes synchronization, removes debt, clears used-target IDs, or recreates a lost anchor.

| # | ID and working label | x,y / duration | Prerequisites and mutex | Gate | Concrete reward and hook | AI |
| ---: | --- | --- | --- | --- | --- | --- |
| 077 | `KRG_authenticate_the_temporal_ledger` — Authenticate the Temporal Ledger | 45,11 / D35 | 035 + 044 | allow TMP; available TMP route seed and evidence | Unlock record-authentication and anchor-discovery missions. Capturing an anchor state is not authentication. | P temporal plan; X absent evidence |
| 078 | `KRG_fortify_the_anchor` — Fortify the Anchor | 44,12 / D70 | 077 | TMP physical Deployment; authenticated owned anchor | Add targeted fortification/anti-air construction to the actual anchor and unlock independent observer teams. | P exposed anchor; H otherwise |
| 079 | `KRG_found_the_synchronization_bureau` — Found the Synchronization Bureau | 46,12 / D70 | 077 | TMP deployment; authenticated records | Expose synchronization capacity, debt, scars, and immutable use records; unlock paid calibration decisions without increasing maximum capacity. | P temporal plan |
| 080 | `KRG_issue_bounded_future_warnings` — Issue Bounded Future Warnings | 44,13 / D70 | 078 + 079 | TMP deployment; `brilliant_scientist_temporal_action_is_ready` for a named crisis | Unlock information-warning operations using the 15-cost/15-debt contract. Each capital, component, leader, or crisis target can be used once. | P genuine capital/component crisis; X routine war |
| 081 | `KRG_accept_the_stabilization_window` — Accept the Stabilization Window | 46,13 / D70 | 079 | `brilliant_scientist_can_begin_temporal_stabilization` or prior completed stabilization | Unlock the 180-day stabilization mission through `brilliant_scientist_begin_temporal_stabilization`. During it, temporal actions are disabled, synchronization is empty, and the facility/anchor is exposed. | P severe debt with defensible window; X immediate collapse risk |
| 082 | `KRG_the_continuity_guard` — The Continuity Guard | 45,14 / D105 | 080 + 081 | TMP weaponization; authenticated anchor; debt below critical | Call the runtime rebuild and unlock the bounded Continuity Guard/recovery operation up to the live temporal cap. Recovery uses the 40-cost/40-debt contract and never duplicates an arbitrary division. | P critical named defense with debt headroom; X routine battles |

## Focus ledger: 083-088, high energy, alien arms, and biological warfare

| # | ID and working label | x,y / duration | Prerequisites and mutex | Gate | Concrete reward and hook | AI |
| ---: | --- | --- | --- | --- | --- | --- |
| 083 | `KRG_build_an_independent_reactor_grid` — Build an Independent Reactor Grid | 51,9 / D70 | 035 | allow ENE; available High Energy at Deployment or higher | Unlock a targeted reactor/power-site program, contamination response, and rare-material procurement. It grants no nuclear stockpile. | P power-hungry portfolio; X absent ENE |
| 084 | `KRG_prepare_strategic_delivery_architecture` — Prepare Strategic Delivery Architecture | 51,10 / D70 | 083 | allow ENE and {RKT OR POR}; available RKT Deployment or POR weaponization | Unlock delivery-network design, hardened command-node sites, and missile/portal counterintelligence. It is a prerequisite surface, not a weapon grant. | P singularity candidate; H long-range need |
| 085 | `KRG_train_the_interface_specialists` — Train the Interface Specialists | 49,11 / D70 | 083 | allow ALI; available alien-arms Deployment and valid interface chamber | Unlock finite specialist training, artifact-interface security, and energy-breach missions. Origin remains unresolved unless the independent evidence contract is met. | P ALI route with material supply; X absent/unauthenticated artifact |
| 086 | `KRG_arm_the_exotic_guard` — Arm the Exotic Guard | 49,12 / D105 | 084 + 085 | ALI weaponization; rare-material production valid | Call the runtime rebuild and unlock exotic guard production up to the live cap. Equipment remains expensive, elite, and unsuitable for attritional garrison duty. | P decisive target/material surplus; X attrition or shortage |
| 087 | `KRG_make_containment_the_first_doctrine` — Make Containment the First Doctrine | 53,11 / D70 | 034 + 044 | allow BIO; available BIO prototype and one exact carried agent | Unlock quarantine, vaccine, safe stockpile seizure, and delivery-authentication decisions through the existing biological lifecycle. | P all BIO plans before offensive use |
| 088 | `KRG_authorize_agents_of_last_resort` — Authorize Agents of Last Resort | 53,12 / D105 | 084 + 087 | BIO weaponization; exact agent and delivery technology; containment operational | Unlock bounded stockpile/raid/fail-deadly decisions through canonical biowarfare APIs. Every use records deaths, contamination, condemnation, retaliation, and threat; no agent or stockpile is fabricated. | L normal AI; H extreme/near-defeat with containment; X moral route |

## Focus ledger: 089-093, diplomacy, intelligence, and the former host

`092` and `093` are mutually exclusive strategic doctrines. They determine whether expansion offers negotiated scientific association or coercive submission. Neither creates subjects instantly.

| # | ID and working label | x,y / duration | Prerequisites and mutex | Gate | Concrete reward and hook | AI |
| ---: | --- | --- | --- | --- | --- | --- |
| 089 | `KRG_a_state_without_friends` — A State Without Friends | 5,9 / D35 | 010 | ACTIVE | Build the actor-specific foreign-interest registry, unlock recognition/patron/containment reactions, and clear invalid foreign targets. | P E/C; H R/T |
| 090 | `KRG_found_the_foreign_intelligence_bureau` — Found the Foreign Intelligence Bureau | 5,10 / D70 | 089 | ACTIVE | Create an agency if absent or add a relevant upgrade if present; unlock bounded archive theft, scientist recruitment, countermeasure, and facility-defense operations. | P high Exposure/enemy majors; H otherwise |
| 091 | `KRG_settle_accounts_with_the_former_host` — Settle Accounts with the Former Host | 3,11 / D70 | 090 | ACTIVE; former-host target valid | Charter: unlock compact, border, archive, and research-access negotiations. Rebellion/enclave: prioritize defense, lost laboratory recovery, settlement, or a justified war. Takeover: unlock resistance and exile-network cleanup. | P R while war/archives unresolved; H C compact; S T |
| 092 | `KRG_open_the_scientific_commonwealth` — Open the Scientific Commonwealth | 4,12 / D105 | 091; mutex 093 | ACTIVE; recognition path and no extreme submission lock | Call `brilliant_scientist_open_international_scientific_center`, unlock voluntary research compacts, recognition, asylum, inspections, and rights guarantees. | P C/human route; L violent high Grievance |
| 093 | `KRG_build_the_submission_network` — Build the Submission Network | 6,12 / D105 | 091; mutex 092 | ACTIVE; military reach and one sustainable project force | Call `brilliant_scientist_open_autonomous_research_network`, unlock ultimatum/protectorate decisions with refusal and coalition responses, and preserve real war/supply costs. | P violent/E4 strong state; X weak enclave |

## Focus ledger: 094-097, expansion, conquest, and integration

| # | ID and working label | x,y / duration | Prerequisites and mutex | Gate | Concrete reward and hook | AI |
| ---: | --- | --- | --- | --- | --- | --- |
| 094 | `KRG_secure_the_laboratory_corridors` — Secure the Laboratory Corridors | 24,16 / D70 | 040 + {046 OR 047} | ACTIVE | Unlock targeted corridor negotiations or limited war goals only for states linking actual facilities, ports, rail hubs, and the capital. No arbitrary regional claims. | P E/multi-site; H otherwise |
| 095 | `KRG_recover_the_stolen_facilities` — Recover the Stolen Facilities | 28,17 / D70 | 091 + 094 | ACTIVE; evidence names a former facility/archive state | Unlock one evidence-backed recovery target at a time, with archive capture and safe dismantlement missions. Invalid/dead targets clean up. | P R/former-host archive; S C unless compact broken |
| 096 | `KRG_integrate_by_project` — Integrate by Project | 26,17 / D105 | 094 + {092 OR 093} + {053 OR 059 OR 065 OR 071 OR 076 OR 082 OR 086 OR 088} | ACTIVE; current occupation has supply and administration capacity | Unlock route-specific integration: civil administration, clone settlement, machine control, reserve administration, control-center rule, portal linkage, or inspected biological cleanup. Cores require time and compliance. | P occupied backlog; X before integration capacity |
| 097 | `KRG_the_continental_laboratory_network` — The Continental Laboratory Network | 26,18 / D105 | 095 + 096 | ACTIVE; overextension mission clear and network supplied | Register a continental network from actual integrated facilities, unlock a global-administration score, and serve as the regional capstone when Evolution IV is disabled. It does not set global threat by itself. | P after integration; X unresolved overextension |

## Focus ledger: 098-100, Evolution IV and terminal commitments

`099` and `100` are mutually exclusive. They commit the state to a strategic doctrine and unlock their respective long systems. Neither focus fires a world end.

| # | ID and working label | x,y / duration | Prerequisites and mutex | Gate | Concrete reward and hook | AI |
| ---: | --- | --- | --- | --- | --- | --- |
| 098 | `KRG_evolution_four_sovereign_science` — Evolution IV: Sovereign Science | 26,19 / D105 | 097 + {014 OR 017 OR 021 OR 025 OR 028 OR 029 OR 030} + {053 OR 059 OR 065 OR 071 OR 076 OR 082 OR 086 OR 088} | allow E4; available ACTIVE and Evolution IV chronology recorded | Unlock world-route decisions, refresh shared Kruger threat only from actual weaponization/aggression/reach, open global scientist/facility targets, and trigger coalition counterplay. | P Evolution IV expansion AI; X disabled E4 |
| 099 | `KRG_commit_to_the_laboratory_world` — Commit to the Laboratory World | 24,20 / D140 | 098; mutex 100 | allow Laboratory World scenario; available `brilliant_scientist_can_commit_to_lab_world = yes` | Call `brilliant_scientist_commit_to_lab_world`, unlock global submission/integration/administration missions, and require verified nonterminal singularity state if arming ever began. The later terminal event still requires chaos, overwhelming control, integration, administration, submission, and no major opposition. | H overwhelming conquest with verified disarmament; X armed/fail-deadly or strong opposition |
| 100 | `KRG_commit_to_the_strategic_singularity` — Commit to the Strategic Singularity | 28,20 / D140 | 098; mutex 099 | allow Singularity scenario; available `brilliant_scientist_can_begin_singularity_theory = yes` | Call `brilliant_scientist_commit_to_singularity`; unlock the six named native component projects, exact component ledger, at least three mixed facilities, two command nodes, two power links, long core/delivery construction, a separate 365-day arming process, disarmament raids, survivable surrender, temporal escape, and doctrine selection. Firing remains in the canonical Fallout request pipeline. | H viable long-war/deterrence AI; L weak state; X missing prerequisites/quick defeat |

## Identity, doctrine, and terminal lock rules

1. Completing any identity capstone sets a permanent `brilliant_scientist_sovereign_identity_locked` receipt before its country effect runs. Every other identity capstone becomes unavailable and gets `ai_will_do = 0`.
2. `019` versus `020`, `023` versus `024`, `036` through `039`, `046` versus `047`, `092` versus `093`, and `099` versus `100` are the only non-capstone hard exclusions. Other tradeoffs use decisions, costs, and crises rather than unnecessarily locking whole lanes.
3. Synthesis is a political convergence, not a project-ledger merger. Paleogenetic and Xenobiological stage, facility, equipment, force-cap, maintenance, accident, AI, and countermeasure state remain distinct.
4. Singularity commitment sets the existing terminal commitment lock. Verified disarmament must call `brilliant_scientist_verify_singularity_nonterminal` before Laboratory World can become available. Singularity firing permanently cancels Laboratory World; Laboratory World firing permanently cancels Singularity.
5. When Evolution IV is disabled, `097` remains a meaningful regional-state ending. Focuses `098` through `100` stay hidden and no disabled chronology flag is fabricated.

## Idea lifecycle plan

The existing country package begins with five formation liabilities. The focus tree only replaces an idea in its existing lifecycle slot; it never adds a parallel focus-only spirit. The implementation should preserve one active idea per row below and must not allow both an old and new state from the same row.

| Lifecycle slot | Formation state | Focus transition | Valid successors | Failure state |
| --- | --- | --- | --- | --- |
| Administration | `brilliant_scientist_improvised_laboratory_state` | identity capstone | civic, replication, machine, temporal/xenobiological/synthesis administration, or required sovereign-directorate administration | `brilliant_scientist_laboratory_feudalism` |
| Portfolio | `brilliant_scientist_inherited_project_portfolio` | 034, then route weaponization only through a later paid project decision | `brilliant_scientist_documented_project_portfolio` or `brilliant_scientist_weaponized_project_portfolio` | `brilliant_scientist_fragmented_portfolio` |
| Command | `brilliant_scientist_fragmented_command` | 046/047, with 053 or 059 route replacement | general staff, project council, clone officers, or machine command | `brilliant_scientist_project_armies_in_rivalry` |
| Supply | `brilliant_scientist_experimental_supply_chain` | 036/037/038/039 | conventional, automated, portal, or biological supply | `brilliant_scientist_prototype_cannibalization` |
| Scientific population | `brilliant_scientist_scientific_exodus` | 092/093 | international scientific center or autonomous research network | `brilliant_scientist_intellectual_isolation` |

Focus 001 resolves the five-visible-spirit conflict without changing balance. Administration, portfolio, and scientific-population ideas move into hidden one-per-slot mechanical mirrors whose modifiers exactly match the canonical ideas. One modifier-free visible summary represents those three slots. Command and supply retain their canonical visible lifecycle ideas. Every focus transition calls the canonical helper, transfers its exact result into the matching hidden slot when needed, and refreshes the summary, leaving exactly three visible lifecycle spirits.

## Decision, mission, event, and helper handoff

### Required Kruger State categories

| Category | Opened by | Core content |
| --- | --- | --- |
| `brilliant_scientist_kruger_state_administration` | 001 | formation audit, staff, heartland, government, idea lifecycle |
| `brilliant_scientist_kruger_state_project_forces` | 035/040 | capped family production, maintenance, physical facilities, family crises |
| `brilliant_scientist_kruger_state_foreign_policy` | 089 | recognition, patrons, former host, intelligence, commonwealth/submission |
| `brilliant_scientist_kruger_state_integration` | 094 | corridors, facility recovery, targeted occupation and integration |
| `brilliant_scientist_kruger_state_temporal_operations` | 077 | authentication, anchors, bounded targets, debt, stabilization, scars |
| `brilliant_scientist_kruger_state_global_program` | 098 | world-route threat refresh, global targets, Laboratory World administration |
| `brilliant_scientist_kruger_state_singularity` | 100 | six components, sites, command/power links, arming, doctrine, disarmament |

### Existing helpers the tree may call

- `brilliant_scientist_rebuild_project_force_runtime_package` after a physical Deployment/Weaponization gate changes.
- Country route effects `brilliant_scientist_form_human_scientific_republic`, `...form_replicated_state`, `...form_machine_state`, `...form_temporal_continuum`, `...form_xenobiological_ascendancy`, and `...form_project_synthesis`.
- One-for-one idea transitions in `016_brilliant_scientist_country_effects.txt`.
- `brilliant_scientist_bind_temporal_target`, `...commit_bounded_temporal_action`, `...begin_temporal_stabilization`, and `...complete_temporal_stabilization` only through a decision/mission that supplies the exact inputs.
- `brilliant_scientist_commit_to_lab_world`, `...commit_to_singularity`, and `...verify_singularity_nonterminal` under their existing triggers.
- Project and force-history triggers named in the gate table. The tree never substitutes a country flag for a missing stage ledger.

### Required narrow helpers or hooks

- `brilliant_scientist_form_sovereign_directorate`, which must use the same route-clearing and one-for-one administration lifecycle as the existing identities.
- `brilliant_scientist_can_unlock_synthesis` and `brilliant_scientist_unlock_synthesis`, requiring separate Paleogenetic and Xenobiological Deployment plus a third carried route, with no ledger merge.
- A focus-layout refresh hook after a project gains or loses a route-seed state.
- Targeted building helpers for the primary facility, anchor, reserve, hatchery, vat complex, control center, terminals, assembly complex, and interface chamber. Every helper validates current ownership/control and a real state target.
- A global-threat refresher that reads actual territorial reach, weaponization, aggressive war/submission, and strategic state. Focus 098 calls the refresher but cannot set threat unconditionally.
- A post-focus event for 100 that exposes component intelligence stages to foreign actors and activates exact component raids. It must not bypass the project board or terminal pipeline.

### Forbidden calls from focus rewards

- `brilliant_scientist_apply_project_force_package_from_history`.
- Every `brilliant_scientist_spawn_*_project_force` effect.
- Direct `create_unit` for a project family.
- Direct grants of missing project stages, missing biological agents, arbitrary cores, arbitrary country targets, synchronization resets, debt removal, or terminal world-end flags.

## AI strategy-plan architecture

Focus-level weights are a safety net. Deterministic route ownership belongs in KRG-specific AI strategy plans modeled on vanilla Italy and Ethiopia plan sequencing. Every plan has `allowed = { brilliant_scientist_is_kruger_sovereign_country = yes }`, an exact enable gate, an abort condition when the route becomes impossible, an ordered `ai_national_focuses` list, and zero factors for incompatible capstones.

| Plan | Enable and preferred focus sequence | Refusal/abort and military behavior |
| --- | --- | --- |
| `KRG_charter_republic_plan` | C, low Grievance, public history: 001-010, 031-040, 015-017, 041-046, 089-092, 094-097 | Preserve truce, seek recognition/resources, use limited projects, break compact only after a verified breach |
| `KRG_rebellion_directorate_plan` | R, high Grievance: 001-010, 041-047, dominant project lane, 012-014, 089-091, 093-098 | Defend facilities/supply first, recover archives, prioritize former host, integrate before another major war |
| `KRG_enclave_survival_plan` | E or tiny KRG: 001-010, 031-040, 041-046, 089-092, 094 | Abort expansion while corridor/patron/supply missions fail; never start Singularity as a weak enclave |
| `KRG_takeover_consolidation_plan` | T: 001-010, 031-040, 041-047, selected identity, 089-091 | Suppress institutional resistance, preserve inherited logistics, no territorial-origin assumptions |
| `KRG_takeover_post_audit_plan` | T after 010: 011-017, 089-092 | Resolve the captured government's identity after the founding audit, favouring direct Directorate authority while keeping a civic route available |
| `KRG_clone_sovereignty_plan` | CLN Deployment, medical/equipment capacity: 048-053 and 018-021 | Stop growth at cap or when medical/equipment burden fails; sustained fronts, not free replacement spam |
| `KRG_machine_ascendancy_plan` | ROB Deployment, power/material surplus: 054-059 and 022-025 | Protect power/assembly, avoid low-power deep offensives, stabilize rogue nodes before expansion |
| `KRG_paleogenetic_plan` | PAL Deployment, feed/land/handlers/transport: 060-065 | Use rough-terrain shock and intimidation; avoid urban, heavy-air, and unsupported operations |
| `KRG_xenobiological_plan` | XEN Deployment, exact control, reagents/power/containment: 066-071 and optionally 029 | Use fort breaking and facility defense; resolve control crisis before production |
| `KRG_project_synthesis_plan` | Paleogenetic and xenobiological Deployment plus a third coherent route: 031-035, 060-071, selected synthesis identity | Preserve separate ledgers while steering a mixed-family state toward the Synthesis capstone |
| `KRG_portal_plan` | POR Deployment, two defensible terminals: 072-076 | Reinforce enclaves and seize facilities; never expose an undefended terminal or create units through transit |
| `KRG_temporal_plan` | TMP Deployment, authenticated anchor, debt below severe: 077-082 and 026-028 | Spend actions only on named strategic crises; stabilize when the weakness window is defensible; never use routine battle retries |
| `KRG_alien_arms_plan` | Exact ALI prerequisites with high-energy delivery: 083-086 | Preserve rare elite equipment and interface security; avoid unsupported attrition |
| `KRG_biological_containment_plan` | Biological Prototype with a settled containment doctrine: 031-035, 041-047 | Establish containment before delivery and keep ordinary security in the loop |
| `KRG_biological_last_resort_plan` | Biological Weaponization, valid delivery, high-energy reach: 083-088 | Reserve biological offense for severe threats and evaluate condemnation or self-contamination |
| `KRG_commonwealth_plan` | 092, recognition opportunity, rights-compatible identity | Offer compacts/asylum/inspection and prefer protectorates or negotiated integration |
| `KRG_submission_plan` | 093, strong army, Evolution IV/global reach | Demand submission before war, target facilities/resources/ports/rails, avoid simultaneous wars beyond supply |
| `KRG_laboratory_world_plan` | 099, overwhelming control, verified nonterminal state | Integrate and administer before terminal readiness; never proceed while armed/fail-deadly |
| `KRG_singularity_plan` | 100, exact theory gate, long-war expectation | Protect all components, expose deterrence stages, fire failsafe only when armed and near capitulation with no surrender/escape override |

## Origin and former-host behavior

| Origin | Opening interaction | Former-host priority | Expansion brake |
| --- | --- | --- | --- |
| Charter | Legal territory, truce, shared archives, recognition dispute | Preserve compact, negotiate access and borders, retaliate only after verified breach | No claims on compact-compliant former host |
| Rebellion | Facility war, damaged supply, defectors, high Grievance | Defend labs, reopen supply, recover archives, then defeat or settle with former host | No second large war before former-host front and integration backlog are stable |
| Enclave | One or two sites, corridor/patron emergency, severe supply | Seek ceasefire, patron, corridor, or portal link; former host remains a threat but not an automatic annex target | No global route while enclave survival mission is unresolved |
| Takeover | Existing national territory and institutions, resistance/exile networks | Old regime is an internal and foreign legitimacy problem, not a territorial actor | Complete institutional consolidation before external conquest |

## Reward-diversity and anti-snowball audit

- Building rewards target actual facilities, rail/port corridors, anchors, reserves, hatcheries, vats, control centers, terminals, power nodes, or interface chambers. No random-state factory spray exists.
- Project capstones unlock bounded production and operations. They never spawn formations or raise the live family caps: clone 8, robotics 8, Paleogenetics 6, Xenobiological 6, portal 4, temporal 3, and alien arms 4. Biological warfare uses the canonical agent and stockpile lifecycle rather than a division cap. The one-time opening conventional package is clamped to 1–8, while the authoritative live conventional ceiling is 12 and later growth remains paid.
- Clone, robot, restored-creature, engineered-organism, portal, temporal, exotic, and biological forces retain distinct equipment, facilities, production burdens, maintenance, operational roles, failures, AI, and counters.
- Conventional infantry, engineers, supply, air defense, and counterintelligence remain mandatory foundations. Project forces cannot replace every garrison and supply task.
- Expansion selects one facility/resource/corridor target at a time. Integration and overextension missions block the next large target until supply, compliance, and administration are adequate.
- Commonwealth and submission are strategic choices. Recognition, subjects, cores, scientists, and facilities are earned through decisions, diplomacy, war, compliance, and time.
- Strategic Singularity is not one focus reward. The focus opens a multi-year, six-component, multi-site race plus a separate arming clock and foreign counterplay.
- Laboratory World requires verified disarmament, overwhelming control, integration, administration, submission, chaos threshold, and defeated major opposition. A completed focus alone cannot end the world.

## Exact count and route-coverage proof

| Lane | Focus numbers | Count |
| --- | --- | ---: |
| Formation and survival | 001-010 | 10 |
| Government and population status | 011-030 | 20 |
| Laboratory economy and logistics | 031-040 | 10 |
| Conventional security | 041-047 | 7 |
| Cloning | 048-053 | 6 |
| Robotics | 054-059 | 6 |
| Paleogenetics | 060-065 | 6 |
| Xenobiological Synthesis | 066-071 | 6 |
| Quantum transit | 072-076 | 5 |
| Temporal operations | 077-082 | 6 |
| High energy, alien arms, biological warfare | 083-088 | 6 |
| Diplomacy and former host | 089-093 | 5 |
| Expansion and integration | 094-097 | 4 |
| Evolution IV and terminal commitments | 098-100 | 3 |
| **Total** | **001-100** | **100** |

Coverage is complete for charter, rebellion, enclave, takeover, direct Directorate, human technocracy, Replicated Sovereignty, Machine Ascendancy, Temporal Continuum, Xenobiological Ascendancy, explicit Project Synthesis, laboratory economy, conventional logistics/security, cloning, robotics, Paleogenetics, Xenobiological Synthesis, portal forces, temporal forces, exotic arms, biological weapons, diplomacy, intelligence, former-host settlement, facility/resource expansion, postwar integration, Laboratory World, and Strategic Singularity.

## Resolved implementation notes and remaining review

1. `brilliant_scientist_kruger_state_focus_tree` now contains exactly 100 manually authored focuses and matches the existing country-effect load calls.
2. Ten KRG decision categories and their route-specific decisions, missions, and events consume the focus mandates. The consumer ledger proves all 180 focus-produced contracts have executable readers.
3. Focus 001 resolves the five-visible-liability presentation conflict through hidden mechanical mirrors and a modifier-free summary. Command and supply remain visible, preserving three lifecycle spirits and the full modifier total.
4. `brilliant_scientist_refresh_kruger_focus_route_layout` owns `mark_focus_tree_layout_dirty` and is called after the sovereign runtime is reconciled.
5. `brilliant_scientist_form_sovereign_directorate`, `brilliant_scientist_can_unlock_synthesis`, and `brilliant_scientist_unlock_synthesis` are implemented in the focus-owned helper layer.
6. Project-stage gates call named operational triggers. The only same-file status-array readers cover High Energy and Rocketry, which have no project-force family helper.
7. Final English focus localisation and 19 route AI strategy plans are present, including the post-audit takeover handoff and the mixed-family Synthesis plan. The interface registers stable normal and shine sprites for every focus, and the 100 registered focus DDS files are present; visual acceptance remains a parent-owned review surface.
8. Source-level layout and reference audits pass. The HOI4 focus inspector could not return a render because its artifact store reported `ARTIFACT_STORAGE_LIMIT`; no engine-render claim is made.

No fallback, placeholder branch, absent-project unlock, free-unit loop, generic repeated ladder, or terminal shortcut is included in this architecture.
