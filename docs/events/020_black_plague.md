# Event 20: Black Plague

Event 20 is a state-level epidemic, containment, biowarfare, and rat-emergence crisis. The source-of-truth design package is `docs/specs/020_black_plague_specs/`; this document records the live implementation contract and the files that realize it.

## Natural origin

The natural entry event selects one eligible mainland state. It does not select a continent and does not apply a continent-wide modifier.

Each eligible state receives a dynamic origin weight derived from its civilian population and vulnerability. The model favors large populations while increasing risk for rural and crowded settlement classes, weak infrastructure and industry, occupation or resistance, troops, refugees, ports and transport hubs, war, weak national stability, and missing prevention or hospital protection. Advanced prevention and field-hospital technology reduce the weight. A capped ticket array performs the final weighted selection.

The chosen state begins in Incubating. Two to four nearby eligible states begin in Threatened. The original owner and controller are recorded separately so later occupation changes do not rewrite the historical origin.

## State lifecycle

`black_plague_phase` is the single state-phase variable:

| Value | Phase | Established infection | Map base |
| ---: | --- | --- | --- |
| 0 | Clear | No | Shared background |
| 1 | Threatened | No | Amber-brown |
| 2 | Incubating | Yes | Black |
| 3 | Infected | Yes | Black |
| 4 | Severe Crisis | Yes | Black |
| 5 | Collapsed | Yes | Black |
| 6 | Contained | Yes | Black |
| 7 | Recovery | Yes | Black |
| 8 | Cured | No | Pale green-grey while monitored |
| 9 | Rat-Controlled | Yes | Black |

State values are independently stored from 0 to 100: disease load, mortality pressure, spread pressure, containment, treatment coverage, relapse risk, incoming exposure, and Rat Infestation. Phase changes do not instantly delete these values. Containment and treatment must suppress load and spread over time; Recovery must hold before Cured is available; Cured retains finite monitoring memory. Rat-Controlled is an occupation condition, not an ordinary disease evolution.

The active phase applies one scaled dynamic state modifier. Severe Crisis, Collapsed, and Rat-Controlled states also receive recurring physical devastation at centrally tuned intervals. Untreated time accumulates while an established state lacks meaningful containment, treatment, and national countermeasure progress, and it intensifies mortality and destruction until response begins to hold.

## Mortality and shared Deaths

Mortality is calculated once per seven-day state pulse before the phase transition for that pulse. The weekly rate combines:

- a phase baseline;
- a nonlinear load × mortality-pressure term;
- an elapsed untreated-time term;
- Evolution I, accidental-release, or weaponized provenance factors when applicable;
- reductions from state containment, treatment coverage, and national countermeasure progress.

The requested number of people is passed to `apply_exact_state_civilian_population_loss`. Its returned applied amount is the only value reused for the Event 20 death ledger and the Chaos meter. The shared low-level population transaction reconciles any recruitable-manpower credit actually observed on the state's owner or distinct controller after the engine mutation. The Deaths target country remains ledger attribution only and does not choose the engine recipient of that credit. Death reason `18` is reserved for Black Plague, at the normal shared conversion of one Chaos per million recorded deaths. Event 20 never applies a second population loss or a direct Chaos increment.

Nonterminal progression preserves the centrally configured minimum surviving population. The earned terminal route may explicitly lower that floor to zero.

### Part 1 mortality calibration

The core curve was simulated with the real weekly pulse order against a one-million-person representative state and a midpoint incubation window. The accepted Part 1 constants produce these plague-attributed cumulative losses before natural population growth:

| Profile | Day 91 | Day 182 | Day 364 |
| --- | ---: | ---: | ---: |
| Exceptional current flags | 0.54% | 0.67% | 0.93% |
| Strong current flags | 1.89% | 2.11% | 2.36% |
| Weak response | 3.14% | 18.19% | 43.99% |
| Neglect and collapse | 5.12% | 29.10% | 64.91% |
| Evolution I with neglect | 8.08% | 42.51% | 81.52% |
| Rat control | 18.68% | 35.92% | 62.40% |

Weak response, neglect, Evolution I, and Rat-Controlled trajectories fit their 90-, 180-, and 365-day design bands. Exceptional and strong annual outcomes remain intentionally provisional because the live core does not yet write national countermeasure progress or cleanup completion. Their final calibration must use the implemented progress ramp and decision timing; raising Contained and Recovery mortality before those writers exist would make successful containment itself disproportionately lethal.

## Spread model

Spread is produced from a start-of-pulse snapshot and resolved through a target ledger, preventing same-pulse cascades. Each target receives one aggregate exposure amount and one deterministic dominant route/provenance tuple.

Supported physical routes are:

- adjacent land borders;
- verified same-controller railway connections;
- troop presence and movement pressure;
- occupation and frontline disruption;
- refugee pressure;
- local port adjacency;
- Evolution II overseas port contact proven by reciprocal current ship presence in the source and target ports;
- biological strikes;
- Rat Nation occupation.

Border closure, quarantine, port inspection, transport restriction, prevention capacity, target containment, and national countermeasure progress reduce exposure. They do not remove an established infection. Overseas spread does not use continent, faction, docking-access, or diplomatic-access proxies.

## Event-owned scheduler

The runtime uses hidden Event 20 callbacks and an event-owned seven-day scheduler. It does not add a world-iterating daily, weekly, or monthly on-action. The pulse rebuilds the tracked-state snapshot, updates each tracked state, produces spread from the frozen source set, resolves each target once, and schedules the next pulse while the crisis remains active.

Natural initialization, later scenario initialization, and other batch setup paths refresh the contamination mapmode once after all state writes. Each weekly pulse also batches all phase, value, and provenance writes into one refresh. Ordinary display cleanup remains covered by the mapmode's daily update.

## Shared disease and mapmode integration

Event 20 uses `chaosx_disease_containment_category`, the existing contamination mapmode, and the shared mapmode button. It never defines a dedicated Black Plague decision category.

Every established Black Plague state that the mapmode player is authorized to know is pure black in the contamination mapmode. Owners and controllers can see their own Incubating states and exact outbreak values. Foreign states remain hidden until public recognition, after which their tooltip exposes phase, qualitative containment and Rat Infestation bands, and public provenance without leaking internal values. Recurrent Threatened and Incubating phases clear stale public recognition until the outbreak is recognized again. A single colored border expresses the highest-priority visible status: Rat-Controlled, currently weaponized infection with public attribution, then phase. Other disease states retain the shared green disease color. Disease selection controls the shared crisis-board action set, while the latest acceptance rule keeps authorized established Black Plague states black in the contamination mapmode regardless of the selected disease tab.

The engine provides only two flat scripted-mapmode layers and one colored border. It has no supported state-clipped texture or mapmode-visibility trigger for particles. Black fog clipped to infected state borders is therefore blocked by the engine surface. A centroid particle is not used because it would cross state borders and remain visible outside the selected mapmode.

## Central tuning and implementation files

- Identity, phase, origin, timing, growth, mortality, spread, modifier, and devastation constants: `common/script_constants/020_black_plague_constants.txt`
- Phase, target, route, and capability predicates: `common/scripted_triggers/020_black_plague_triggers.txt`
- Origin, lifecycle, mortality, scheduler, and initialization effects: `common/scripted_effects/020_black_plague_effects.txt`
- Snapshot and route-specific spread effects: `common/scripted_effects/020_black_plague_spread_effects.txt`
- State modifier: `common/dynamic_modifiers/020_black_plague_dynamic_modifiers.txt`
- Root and state callbacks: `events/020_black_death.txt`
- Shared disease detection: `common/scripted_triggers/cbw_triggers.txt`
- Shared mapmode rendering and tuning: `common/map_modes/chaosx_state_map_modes.txt` and `common/script_constants/state_map_modes_constants.txt`
- Shared mapmode tooltip: `common/scripted_localisation/chaosx_scripted_localisation_map_modes.txt` and `localisation/english/chaosx_map_modes_l_english.yml`
- Shared Deaths and Chaos integration: `common/script_constants/chaos_meter_constants.txt`, `common/scripted_effects/chaos_meter_effects.txt`, and their localisation and system documentation

## Visual asset registry

The live state modifier references the registered `GFX_idea_black_death` sprite. The final Event 20 asset audit must explicitly accept that sprite as final or replace the reference and registry together; it is not silently treated as a generic substitute.

The complete Event 20 package requires final, wired assets for:

- the shared crisis-board disease selector and Black Plague state card;
- every Black Plague-specific response decision and mission;
- Rat Infestation, containment, countermeasure, provenance, and rat-control status marks;
- five evolution entries and their pre-fire variants;
- twelve distinct Rat Nation identities and the separate Rat King identity;
- Rat Nation and Rat King focus trees, ideas, decisions, units, and royal mechanics;
- coronation, terminal takeover, and global-defeat super events;
- fourteen achievements with locked, available, and completed states;
- source-frame animation packages, contact sheets, previews, static fallbacks, manifests, and `.gfx`/`.gui` handoffs;
- licensed 44.1 kHz super-event music with recorded license and source evidence.

Final asset paths and sprite names will be recorded in the Event 20 asset manifest before gameplay references are committed.

## Remaining implementation tranches

The shared crisis board, selected-state decision system, national countermeasure program, Doctor Wu bridge, six-phase weaponization project, evolutions, Rat Nation pool, Rat King package, triggerable scenario, earned terminal route, super events, achievements, final visual/audio assets, event logs, catalog, workbook alignment, and completion audits remain separate required tranches. They must follow the source pack and may not be substituted with generic decisions, copied flags, ordinary plague projects, instant cures, or fallback trees.

## Future extensions

After the accepted Event 20 package is complete, safe extensions include more route-specific diplomatic reactions, regional historical response variants, additional nonterminal aftermath events, and richer shared-disease comparisons. Any extension should reuse the phase/value model and physical spread proofs rather than introduce a second plague state system.
