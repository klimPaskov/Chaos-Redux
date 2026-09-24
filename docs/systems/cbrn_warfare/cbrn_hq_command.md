# CBRN Army Headquarters command system

## Purpose

Army Headquarters is the theater command layer for CBRN protection and response. Three HQ-only support sections provide Operations and Intelligence, Protection and Decontamination, and Medical and Biosecurity functions. Five paid commander orders cover protection, decontamination, cordons, medical response, and outbreak containment.

Chemical and biological attacks use native raids. Headquarters orders do not select a weapon, stage an attack, release a payload, create contamination or an outbreak, record casualties or evidence, or change Condemnation.

## Headquarters sections

| Section | Runtime identifier | Standing role |
| --- | --- | --- |
| Operations and Intelligence | `cbrn_hq_operations_section` | Planning, reconnaissance, weather assessment, and command coordination |
| Protection and Decontamination | `cbrn_hq_protective_logistics_section` | Protective issue, corridor opening, sealed-area work, and mobile decontamination |
| Medical and Biosecurity | `cbrn_hq_medical_countermeasure_directorate` | Countermeasures, casualty response, outbreak control, and biological security |

The old Intelligence and Weather Cell, Mobile Decontamination Column, and Biological Security Section identifiers survive only as trigger aliases to their consolidated section. They are not separate subunits, technology cards, CXT grants, or player-menu entries.

All three sections are Army-HQ-only, zero-width support subunits. Their native statistics depend on their real equipment needs, so shortages reduce their performance. Their protection and response effects are also checked against the country’s real CBRN stock and derived readiness state.

## Commander orders

| Order | Required section | Purpose |
| --- | --- | --- |
| Theater Protective Posture | Protection and Decontamination | Sustains issued protection across a threatened command |
| Decontamination Corridor | Protection and Decontamination | Opens and maintains a cleanup route |
| Seal Operational Area | Operations and Intelligence plus Medical and Biosecurity | Restricts access to an exposed operational area |
| Mass Antidote and Casualty Response | Medical and Biosecurity | Commits medical capacity to a chemical emergency |
| Seal Infection Corridor | Medical and Biosecurity | Commits medical and cordon resources to outbreak containment |

Each order checks a deployed Army HQ, the exact consolidated section, relevant threat or response context, no conflicting HQ commitment, Command Power, and a complete real operating package. Activation stores the force band, debits the package once, applies a bounded preparation status, and schedules only the targeted completion, upkeep, and cleanup events required by that order.

Preparation completion rechecks the command, section, and context. Weekly upkeep exists only for the finite active duration. If upkeep fails, the benefit ends and the already scheduled cleanup releases the remaining commitment. No daily, weekly, monthly, or other all-country pulse is used.

The `chemical_operations_commander` trait reduces preparation time by 30 percent for these five protective orders. It is earned from qualifying completed service; starting an order, canceling it, or repeatedly preparing it gives no credit.

## Force bands and derived readiness

The commander’s exact battalion count selects light, standard, or mass operating packages. The thresholds and packages are centralized in `common/script_constants/cbrn_hq_constants.txt`.

Chemical Readiness is a derived status refreshed from issued military masks, filter condition, decontamination capacity, instruments, and training. It changes preparation time but is not a separate resource that the player buys. Equipment debits use real stock, and filter consumption passes through the shared military-mask loss helper.

## Native offensive operations

Cylinder releases, projector barrages, artillery delivery, armored delivery, strategic air delivery, and biological operations are native raid definitions. Each raid owns its weapon, state target, origin requirements, assigned formation, intelligence source, preparation timer, equipment reservation, and success factors.

The retired `cbrn_prepare_chemical_offensive` and `cbrn_combined_overmatch` abilities have no gameplay definition, sprite registration, runtime DDS, cost, status trait, event branch, trigger, or localisation. Native raid preparation is the only offensive preparation path.

A successful native chemical land release may record the headquarters-dependent achievement receipt when the actor country has a qualifying deployed Operations section or all three sections. Installed raid scope does not expose the assigned division’s exact Army-HQ pointer to the actor-country outcome recorder. The receipt therefore proves a qualifying deployed HQ in the actor country, not that the selected raid division belonged to that specific HQ.

Captured biological-facility recovery raids use the consolidated Medical and Biosecurity section through the stable `cbrn_hq_has_biological_security_section` compatibility trigger. The selected division must also contain the Biosecurity Assault Detachment.

## AI behavior

The AI templates use the same three sections and real standing equipment bills as the player. Defensive profiles prioritize protection and medical coverage, contaminated theaters prioritize the protection section, outbreak response prioritizes the medical section, and offensive native raids retain their own exact payload, policy, target, formation, and success gates.

Removed HQ sections and the eighteen obsolete agent-specific chemical tank companies are absent from active AI templates. Light, medium, and heavy armored delivery roles remain the supported chassis variants.

## Assets and wiring

The active section sprites are registered in `interface/chaosx_subuniticons.gfx`. The five commander-order sprites are registered in `interface/chaosx_ability.gfx` and use the matching files under `gfx/interface/abilitylist/`. Technology and doctrine artwork remain registered in their dedicated technology and doctrine GFX files.

The current package manifest and review sheets are under `docs/assets/chaos_warfare_cbrn/icon_package/`. Retired offensive ability icons are listed as removals in that manifest.

## Main files

- `common/units/cbrn_hq_support.txt`
- `common/abilities/cbrn_hq_abilities.txt`
- `common/unit_leader/cbrn_hq_traits.txt`
- `common/script_constants/cbrn_hq_constants.txt`
- `common/scripted_triggers/cbrn_hq_triggers.txt`
- `common/scripted_effects/cbrn_hq_effects.txt`
- `events/cbrn_hq_events.txt`
- `interface/chaosx_ability.gfx`
- `localisation/english/cbrn_hq_l_english.yml`

## Validation limits

Source review proves three active HQ sections, five active commander orders, finite targeted event chains, real stock debits, and removal of the separate offensive-preparation path. MCP event traces cover bounded HQ and protection chains but the full workspace event graph still reports unresolved diagnostics. Exact native reservation behavior on cancellation and the assigned-division-to-HQ association remain outside the documented script interface and require consumer evidence.
