# Event 016 - Brilliant Scientist

## Implementation status

Event 016 is default-enabled as a minor fire-once incident after the core package audits. The dispatcher resolves one weighted valid host, the player can appoint Doctor Warren Kruger publicly or secretly or forward his unrecruited application once, and AI always appoints him. Both appointment routes create the same fixed character, grant his non-dismissable national-advisor role with exactly `+100%` research speed, add him as a level-five scientist in all six special-project fields, initialize the Directorate state, preserve the chosen host for the event log, and prevent a second opening reward.

The architecture and identifier maps are frozen in the accepted handoffs under `docs/plans/016_brilliant_scientist_plans/`. Directorate, project portfolio, foreign-operation, containment, territory-planner, Kruger State focus, terminal, achievement, aftermath, presentation, shared wiring, Event 019 provider interoperability, localisation, workbook alignment, and mapped audit tranches form the core runtime package. Deferred report/news and flavor content, Event016-specific 3D models, and live consumer validation remain open. This document does not claim the whole event is content-complete.

The accepted design source is `docs/plans/016_brilliant_scientist_plans/016_source_of_truth_map.md` and the ten-part specification under `docs/specs/016_brilliant_scientist_specs/`. The current runtime and resume pointer is `docs/plans/016_brilliant_scientist_plans/016_core_runtime_handoff_map.md`.

The dedicated runtime-facing evolution guide is `docs/events/016_brilliant_scientist/evolutions.md`.

## Event identity

- Event ID: `16`.
- Entry root: `chaosx.nr16.1`.
- Type: minor fire-once.
- Cluster: none.
- Named character: Doctor Warren Kruger.
- Opening anchor: exactly `+100%` research speed.
- Evolutions: four.
- Project families: fifteen.
- Conditional country: Kruger State.
- Terminal scenarios: Laboratory World and Strategic Singularity.
- Achievements: exactly seventeen.
- Super-event packages: exactly six.

Shared reservations are world-end scenario 11 for Laboratory World and world-end scenario 12 for Strategic Singularity. The exact visible mapping is:

| Visible ID | Role |
| ---: | --- |
| 90 | International recognition |
| 91 | Kruger State formation |
| 92 | Global Kruger threat |
| 93 | Laboratory World |
| 94 | Strategic Singularity |
| 95 | Qualifying defeat aftermath |

Live Event 015 wiring occupies visible IDs 85 through 89. Event 020 separately declares world-end ID 10 and visible IDs 85 through 87 in its own constants. Its visible overlap with Event 015 is external to Event 016.

## Implemented opening lifecycle

The random-event dispatcher selects and preserves an eligible host before dispatch so the event log records the correct actor. Eligibility rejects countries that do not exist, are subjects, have too little viable core territory, are in civil war, have already handled the opening, or already own Kruger. The weighted pool responds to research capacity, industrial scale, facilities, government, war pressure, and relevant Chaos Redux history without iterating over every country on a recurring on action.

The selected country sees the minor report event `chaosx.nr16.2`. A player may appoint Kruger publicly, place him in a secret military programme, or forward his still-unrecruited application to one prevalidated weighted recipient. AI has zero weight for referral and always selects one of the two appointment routes. A recipient sees `chaosx.nr16.3` and cannot forward him again.

Appointment is an atomic transaction around the single token `KRG_warren_kruger`. It creates that token once, changes nationality once, adds one advisor role and one scientist role, assigns level five in nuclear, naval, aeronautics, land warfare, biowarfare, and chemical warfare, records the posture and host, initializes the causal state, resolves the global fire-once gate, and rebinds the event-log actor. The advisor cannot be fired, so the `+100%` reward cannot be dismissed and reacquired. Later transfers must reject an active-project scientist and remove the existing roles before nationality and role ownership move.

The public and secret options differ in Directorate posture and AI preference, not research power. The opening reveals no alien or temporal origin and fires no major news event or super-event. The host focus tree remains intact.

## Directorate state

The player sees Mandate, Dependence, Exposure, and Project Capacity. Independent Capacity and Grievance remain hidden causal state, but visible incidents must communicate their consequences. Directorate actions cover laboratories, staff, governance, replication, security, resources, foreign contacts, confrontation, and recovery.

No all-country daily, weekly, or monthly polling action is planned. Use bounded hooks, selected targets, missions, or self-scheduled events.

## Project portfolio

The fifteen project families are computation, electronics and guidance, advanced materials, rocketry and propulsion, atomic and high energy, biomedical acceleration, teleportation, cloning, robotics and AI, paleogenetics, xenobiological synthesis, biological weapons, alien arms, temporal mechanics, and strategic singularity.

Paleogenetics reconstructs extinct terrestrial organisms. It uses reserves, hatcheries, transport pens, handler schools, feed, land, transport, and veterinary capacity. Its deployed roles include reconnaissance, rough-terrain transport, intimidation, and dinosaur or megafauna shock. Its failures and counters concern escape, breeding, habitat, handlers, transport, air attack, anti-armor defense, and reserve capture.

Xenobiological synthesis designs new organisms from modular anatomy and artificial tissue. It uses growth vats, medical fabrication, control centers, reagents, power, sealed containment, and a selected control method. Its roles include laboratory defense, tunneling, fortification breaking, sensing, adaptive support, and specialist assault. Its failures and counters concern mutation, control loss, unauthorized reproduction, nests, growth laboratories, command isolation, and the selected control channel.

The two families converge only through explicit Synthesis.

## Temporal mechanics

Every meaningful temporal action consumes synchronization capacity and adds temporal debt. It targets a named crisis, project component, leader, or bounded unit package and records use so the same loss cannot be restored repeatedly. Severe actions may leave persistent timeline scars.

Temporal debt does not passively disappear. Stabilization reduces debt while disabling temporal actions, occupying the relevant facility, and exposing a weakness window. Opponents require evidence before authenticating records, discovering anchors, capturing ledgers, or disabling linked recovery actions.

## Origin conclusions

A campaign may lock one of four conclusions:

- extraterrestrial provenance
- temporal displacement
- manufactured continuity
- unresolved origin

Public proof requires the relevant independent evidence. A clone, machine, temporal, xenobiological, or synthesis transformation does not prove that the original Kruger was extraterrestrial.

## Host resolution and Kruger State

Host outcomes include negotiated limits, public settlement, a controlled compact, unrestricted hosted science, safe removal, defection, confinement, military seizure, peaceful charter, partial enclave, violent rebellion, and rare host takeover.

Takeover is institutional capture. It requires extreme Dependence, compromised Control, several warning incidents, control across several independent national domains, and at least one state-wide control domain. It is never enabled because a territorial split is invalid or inconvenient.

When a viable Kruger State forms, its territory, economy, forces, technology, politics, focus access, AI, and countermeasures derive from recorded project and host history. Its planned focus tree contains 85 to 115 manually authored focuses.

## Terminal commitments

Laboratory World is the conquest, submission, integration, and global-administration ending. It requires overwhelming world control, defeated or submitted opposition, a functioning global facility network, and the shared chaos threshold.

Strategic Singularity is a vulnerable multi-year component race and denied-victory ending. It can mature before world conquest. When validly fired, it raises chaos above the shared threshold and enters the canonical Fallout pipeline.

Automatic fail-deadly or deliberate global-use doctrine blocks Laboratory World while the device is armed. Laboratory World consolidation requires verified disarmament and nonterminal control. Singularity firing prevents Laboratory World permanently. Laboratory World firing cancels singularity construction, arming, and activation.

## Presentation inventory

Six super-event packages are planned for recognition, formation, global threat, Laboratory World, Strategic Singularity, and qualifying defeat. Recognition and defeat are conditional at runtime but remain full production packages.

Text and audio are complete for all six packages. Six role-distinct Event 016-owned WAVs exist at IDs 90 through 95, and six generated super-event DDS files plus seven generated report-event DDS files are present. Shared image, title, quotation, button, description, sound, volume-setting, trigger, and aftermath wiring is complete. Live playback acceptance remains user-owned.

Six severe Kruger portrait animation packages exist for clone, machine, temporal, xenobiological, alien-revealed, and synthesis outcomes. Every package contains separate source frames, a static fallback, frame sheet, DDS, preview, contact sheet, manifest, and GFX handoff. Transform-only animation is not used.

Stage 0 is complete from the exact `portrait_generic_biowarfare_europe_male_01` base. The runtime leader or scientist DDS and `65x67` advisor DDS are registered as `GFX_portrait_KRG_doctor_warren_kruger_stage_0` and `GFX_idea_doctor_warren_kruger_stage_0`, and the character definition consumes both. All fourteen later-stage leader or scientist portraits and matching advisor cards are present under stable Stage I through IV sprite names. The advisor family uses `.agents/skills/chaos-redux-event-assets/tools/create_advisor_icon.py`: each complete portrait is resized to a native `65x67` intermediate, uniformly transformed without warping, and covered once by the untouched canonical `advisor_template.png`. Standard cards use `33x46`, clone cards use `36x50`, and temporal cards use `39x54`; all use `-6` degrees and center `24 31.5`. A dedicated `210x176` opening report composition derived from the same approved identity is registered as `GFX_report_event_016_brilliant_scientist_appointment` and used by `chaosx.nr16.2` and `.3`. Stage I through IV route portraits, six severe frame sheets, static fallbacks, and state routing are wired. The copied base is explicitly authorized for internal mod use, while external redistribution rights remain unresolved.

Exactly seventeen achievements require completed, grey, and not-eligible icons, for 51 final DDS files.

## Icon and sprite plan

Stage-0 and later portrait sprites, static fallbacks, and severe animation frame sheets are registered or documented in `interface/016_brilliant_scientist.gfx`. The runtime package exists, but final state selection and parent-owned validation remain separate from asset production.

| Family | Planned path | Planned registration |
| --- | --- | --- |
| Kruger portraits | `gfx/leaders/KRG/` and Event 016 source folders | `interface/016_brilliant_scientist.gfx` and character portrait blocks |
| Directorate background, frames, meters, cards, warnings | `gfx/interface/016_brilliant_scientist/` | `interface/016_brilliant_scientist.gfx` and `.gui` |
| Ideas and advisor icons | `gfx/interface/ideas/016_brilliant_scientist/` | `interface/016_brilliant_scientist.gfx` |
| Focus icons | `gfx/interface/goals/016_brilliant_scientist/` | `interface/016_brilliant_scientist.gfx` |
| Decision and category icons | `gfx/interface/016_brilliant_scientist/decisions/` | `interface/016_brilliant_scientist.gfx` |
| Project and technology icons | `gfx/interface/016_brilliant_scientist/projects/` and `gfx/interface/technologies/016_brilliant_scientist/` | `interface/016_brilliant_scientist.gfx` |
| Unit and equipment icons | Event 016 unit and equipment interface folders | `interface/016_brilliant_scientist.gfx` and verified equipment surfaces |
| Report and news images | `gfx/event_pictures/016_brilliant_scientist/` | `interface/016_brilliant_scientist.gfx` |
| Super-event images | `gfx/super_events/016_brilliant_scientist/` | `interface/chaosx_super_events.gfx` after shared ID reservation |
| Achievement icons | `gfx/achievements/016_brilliant_scientist_<slug>.dds` and two state variants | Existing Chaos Redux achievement registry and localisation |
| Kruger State flags | `gfx/flags/`, `gfx/flags/medium/`, `gfx/flags/small/` | Country and cosmetic-tag definitions |

The achievement slugs are `borrowed_century`, `every_door`, `public_method`, `the_one_who_left`, `clean_break`, `approve_everything`, `the_former_host`, `combined_arms_redefined`, `clever_girl`, `the_machine_continues`, `population_one`, `yesterday_sent_help`, `not_from_here`, `no_second_sun`, `the_last_calculation`, `the_world_is_the_laboratory`, and `ordinary_people_won`.

## Integration points

Implementation must align Event 016 with the random-event dispatcher, event log, four evolution rows, Event Details, special projects, characters, decisions, scripted GUI, world threat, world-end registry, Fallout, Deaths, Condemnation, Chaos, achievements, super-event audio settings, documentation, and the event catalog workbook.

Biological-weapon work must reuse the existing biowarfare, contamination, Deaths, and Condemnation systems where their semantics match. It must not create parallel anthrax, plague, smallpox, or equivalent systems.

## Current blockers

- Event 016 is default-enabled for ordinary fire-once selection; live scenario validation remains user-owned.
- The report, super-event, portrait, animation, icon, flag, achievement, and Directorate UI packages are registered and have static consumer checks. Live presentation acceptance remains user-owned.
- No Event016-specific 3D unit or building model package is accepted. The seven route-specific unit consumers remain a production and runtime-wiring backlog.
- Broader news, defeat/remnant, and country-specific flavor content remains queued after the core runtime milestone, and no dedicated Kruger triggerable scenario is required by the accepted design.

## Future plans

Continue from the core-runtime handoff with live scenario validation and future content tranches. Keep broader flavor, news, defeat or remnant, and Event016-specific 3D production queued behind that core boundary. Preserve the completed opening transaction, accepted architecture, staged identity packages, accepted visual tranches, and Event 016-owned WAVs.

Another improvement-loop pass is appropriate only after the accepted addendum is implemented and new evidence shows a distinct shallow or disconnected mechanic.
