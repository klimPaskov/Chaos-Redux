# Event 20: Black Plague

Event 20 is a playable state-level epidemic, containment, biowarfare, and Rat emergence system. The source-of-truth design package is `docs/specs/020_black_plague_specs/`; this document records the live core contract. Additional narrative content and bespoke 3D models remain later production tranches.

## Natural origin

The natural entry event chooses one eligible mainland state through a weighted ticket pool. It favors population, crowding, underdevelopment, occupation, resistance, troops, refugees, war, ports, railways, and weak protection. Prevention, field hospitals, stability, infrastructure, and response capacity reduce the weight. The chosen state begins Incubating, nearby eligible states begin Threatened, and the system records the historical owner and controller.

## State lifecycle

`black_plague_phase` is the authoritative state phase:

| Value | Phase | Established | Map base |
| ---: | --- | --- | --- |
| 0 | Clear | No | Shared background |
| 1 | Threatened | No | Shared warning |
| 2 | Incubating | Yes | Black |
| 3 | Infected | Yes | Black |
| 4 | Severe Crisis | Yes | Black |
| 5 | Collapsed | Yes | Black |
| 6 | Contained | Yes | Black |
| 7 | Recovery | Yes | Black |
| 8 | Cured | No | Monitored recovery |
| 9 | Rat-Controlled | Yes | Black |

Disease load, mortality pressure, spread pressure, containment, treatment coverage, relapse risk, incoming exposure, Rat Infestation, and untreated time are stored separately. Phase changes do not erase those values. Cleanup lowers the underlying pressures and requires sustained response rather than instantly removing infection. Severe Crisis, Collapsed, and Rat-Controlled states suffer recurring physical devastation.

## Mortality and spread

The seven-day pulse calculates nonlinear mortality once and sends the applied population loss through the shared exact-loss transaction. Its returned value is the sole input to the Event 20 Deaths ledger and Chaos contribution, preventing double counting.

Spread is produced from a frozen source snapshot and resolved through a target ledger, preventing same-pulse cascades. Routes cover land borders, rail and transport, troop presence, occupation and fronts, refugees, war disruption, ports, Evolution II overseas contact, biological delivery, and Rat occupation. Countermeasure progress, containment, quarantine, inspection, and protection reduce exposure without erasing established infection.

## Shared disease UI and response

Event 20 uses `chaosx_disease_containment_category`, the existing disease interface, and the existing contamination mapmode. It does not create a dedicated Black Plague category.

The selected-state response surface provides rat cleaning, sealed food storage, sewer and burrow clearance, flea control, rail-yard and dock purges, demolition of lost blocks, emergency hospitals, quarantine, cordons, treatment, and Doctor Wu's protocol. Visibility and availability depend on the selected state, its phase, control, and response conditions. Actions have material, military, economic, and time costs. National countermeasure progress runs from 0 to 100 and reduces deaths and spread while enabling sustained cleanup.

Authorized established Black Plague states retain a black base in the shared mapmode. Phase, containment, weaponization, and rat control are conveyed by the existing border and tooltip layers while other diseases retain their own colors. State-clipped black fog is not used because the supported scripted-mapmode layers do not provide a verified safe clipping mechanism.

## Evolutions and weaponization

Five logged evolutions have dynamic active and pre-fire Event Details entries:

1. Evolution I strengthens the strain.
2. Evolution II enables physically proven overseas spread.
3. Evolution III creates the Rat Nation from an uncontrolled basin.
4. Evolution IV creates the separate sentient Rat King.
5. Evolution V is the earned terminal route.

Ordinary disease phases are not evolutions.

The weaponization project has six phases, eighteen unique iteration roles, four mutually exclusive approaches, accidents, condemnation, and payload integration with the existing delivery system. Doctor Wu uses one persistent validated host and accelerates response only through the normal selected-state and resource rules.

## Rat countries

The country package uses the reusable Rat Nation tag `RTA` and the separate Rat King tag `RTX`. The Rat Nation chooses one of four origin archetypes from its founding basin and represents additional broods through rat-controlled states, capped force-growth pulses, and internal brood mass rather than extra country tags. The package includes country identity, leaders, flags, ideas, AI, locked zero-manpower division templates, starting forces, decisions, focus trees, plague immunity, and occupation-driven infection.

Rat units do not consume human manpower or normal equipment and cannot be manually deployed. Their current map models intentionally use the registered infantry entity as a temporary engine-safe visual consumer. Bespoke Rat Nation and Rat King unit models and skeletal animations are required in a later 3D production tranche.

## SCN-012 and terminal route

Black Plague Unbound is implemented in the existing triggerable-scenario UI as `SCN-012`. Each intensity directly seeds established outbreaks across multiple eligible continents, forces Evolutions I through IV, creates the Rat Nation, creates the Rat King in a separate Royal Basin, grants a coexistence grace period, initializes AI, forces, disease values, decisions, logs, coronation, and performs one mapmode rebuild. The setup uses a scoped bypass, clears it after the transaction, and is idempotent. It never grants Evolution V, `world_end`, or automatic victory and disqualifies ordinary-progression achievements.

Evolution V remains gated by Chaos above 1000, catastrophic plague deaths, conquest, the completed Rat King route, and 90 percent control of an eligible continent together with its designated capitals and refuge nodes. Only that earned route performs deterministic takeover and the world-end super-event.

## Runtime ownership

Event 20 uses an event-owned seven-day scheduler rather than adding a world-iterating daily, weekly, or monthly on-action. Natural initialization, scenarios, and weekly pulses batch state writes and rebuild the shared mapmode once per transaction.

Primary implementation surfaces include:

- `common/script_constants/020_black_plague_*.txt`
- `common/scripted_triggers/020_black_plague_*.txt`
- `common/scripted_effects/020_black_plague_*.txt`
- `common/decisions/020_black_plague_*.txt`
- `common/national_focus/020_black_plague_*.txt`
- `common/special_projects/projects/020_black_plague_weaponization_projects.txt`
- `events/020_black_death.txt`
- `events/020_black_plague_*.txt`
- `history/countries/RT*.txt`
- `history/units/RT*_1936.txt`
- `interface/020_black_plague_*.gfx`
- `localisation/english/020_black_plague_*_l_english.yml`

## Core-readiness boundary

The scripted core is source-complete for the stabilization tranche. Static audits resolve all Event 20 custom constants, scripted calls, event callers, GFX references, and texture paths. The package includes final runtime icons, country flags and portraits, super-event images, and licensed 44.1 kHz music.

Later content production remains intentionally separate: bespoke rat 3D units and animations, additional scenario variants, more narrative events, deeper country routes and crises, visible achievement presentation, source-frame UI animation packages, a unique Doctor Wu report image, and a dedicated weapon-delivery icon. These omissions do not leave active gameplay references unresolved.

The full audit and deferral record is `docs/plans/020_black_plague_plans/2026-07-29_event20_core_readiness_report.md`.
