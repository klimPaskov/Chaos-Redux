# Event 016 Brilliant Scientist Evolutions

## Purpose

Event 016 has exactly four logged evolutions. Appointment, laboratory construction, project approval, Directorate growth, and ordinary confrontation remain baseline progression. World Collapse is a terminal eligibility state and does not create a fifth evolution.

The shared Event Log identity is Event `16`, evolution type `16`, stages `1` through `4`. Each evolution records the current host as actor. Once the Kruger State exists, sovereign-science records use that country as the actor.

## Runtime sequence

1. Before Event 016 fires, the random-event preparation path evaluates the current Chaos state and stores the strongest enabled evolved opening.
2. The opening still selects a valid host and presents the real appointment choices. Evolution state is committed only after a country accepts Doctor Warren Kruger.
3. An active host schedules a private evolution check through the Event 016 scheduler. The system does not use a daily, weekly, monthly, or whole-world polling action.
4. Every stage has a base MTTH of 90 days. Mandate, Dependence, Exposure, project maturity, war, active crises, and temporal stabilization modify the interval. Scheduled checks are clamped between 30 and 180 days.
5. A pulse may deliver at most one enabled and valid stage. The delivery event commits its state, updates Kruger's portrait, records the Event Log row, applies the selected policy, and schedules the next check.
6. Evolution IV ends ordinary evolution scheduling and resolves through a supervised regional compact or the sovereignty deadline.

## Evolution stages

| Stage | Player-facing identity | Normal Chaos band | Main change |
| --- | --- | --- | --- |
| I | National Scientific Ascendancy | Gathering Storm | Kruger becomes a national institution. The host chooses open methods, a strategic laboratory, an industrial timetable, or a university confederation. |
| II | The International Scientific Contest | Rising Chaos | Foreign powers begin direct recruitment, theft, sabotage, protection, and assassination operations. The host selects the security authority responsible for Kruger. |
| III | Forbidden and Autonomous Science | Chaos Tier | Impossible projects gain autonomy and weaponization pressure. The host chooses safe public science, secret projects, or negotiated limits. |
| IV | Sovereign Science | Totalen Chaos | Hosted science must receive a final constitutional settlement. A sovereign Kruger State gains access to its conquest and terminal routes. |

The evolution incidents are `chaosx.nr16.21` through `chaosx.nr16.24`. Their report images are registered as `GFX_report_event_016_brilliant_scientist_evolution_1` through `GFX_report_event_016_brilliant_scientist_evolution_4`.

Each evolution report retains the host archetype selected at appointment or transfer. The same clause that describes the university, industrial, militarized, threatened, colonial, refugee, or default institutional environment now appears in all four evolution openings, so the escalation reads as a continuation of the host's actual political setting rather than a generic global incident. The evolution AI uses that retained archetype as a bounded preference: universities and refugee networks favor open or supervised settlements, industrial and colonial hosts favor production or chartered authority, and militarized or threatened hosts favor security and containment. These modifiers only weight existing options; they do not add a fifth evolution, a new flag family, or a separate meter.

## Evolved openings

An evolved opening strengthens the initial appointment package without bypassing the player's decision or creating a second Kruger.

- Evolution I can seed a conventional Theory project and brings institutional competition into the opening.
- Evolution II can seed a conventional Prototype and begins with greater foreign attention and security pressure.
- Evolution III can seed an impossible Prototype and opens the early safe-science or dangerous-project conflict.
- Evolution IV can seed a Deployment-stage project and accelerates the route toward a supervised compact or sovereignty deadline.

The evolved opening is recorded after appointment so the selected country remains the correct actor. Disabled stages are skipped while the strongest valid lower opening remains available.

## Disabled-evolution safety

Every stage has an explicit disabled disposition. A disabled stage does not set its recorded flag, cannot grant its gated content, and does not block baseline Directorate play.

- Disabling Evolution I preserves appointment, laboratories, and the ordinary project system.
- Disabling Evolution II removes the international escalation layer while domestic security and ordinary diplomacy remain usable.
- Disabling Evolution III forces a safe-science resolution and prevents forbidden autonomy from becoming a rebellion prerequisite.
- Disabling Evolution IV prevents the world-conquest and Strategic Singularity routes. A formed Kruger State can remain a powerful regional country.

The scheduler stops once every stage is recorded or safely disposed.

## Policy and AI behavior

The four incidents use route-aware AI weights rather than one repeated preference.

- Public and distributed institutions favor open methods and shared oversight.
- Secret or militarized Directorates favor strategic laboratories, military protection, and dangerous projects.
- High Grievance and Independent Capacity increase resistance to containment.
- Strong replication and low Dependence favor negotiated limits and supervised compacts.
- A Kruger State follows its recorded project portfolio and political route when selecting sovereign policy.

Costs and consequences use the Directorate's real resources, facilities, production burden, stability, war support, exposure, and time commitments. Evolution choices do not create a separate political-power store.

## Portrait progression

Stages 0 through II use the corresponding registered leader and advisor portrait pairs. Evolution III selects a visible strange-science route. Evolution IV resolves the severe identity from the completed project portfolio.

The severe routes are clone, machine, temporal, xenobiological, alien-revealed, and synthesis. Alien-revealed requires independent provenance evidence. A transformed body alone does not prove that the original Kruger was extraterrestrial.

Each runtime portrait change updates the same persistent character token. It does not create another advisor, scientist, actor, or leader.

## Implementation surfaces

- Constants and shared identity: `common/script_constants/016_brilliant_scientist_constants.txt`
- Evolution runtime constants: `common/script_constants/016_brilliant_scientist_evolution_constants.txt`
- Dynamic timing: `common/mtth/016_brilliant_scientist_mtth.txt`
- Gates and disabled-stage safety: `common/scripted_triggers/016_brilliant_scientist_evolution_triggers.txt`
- Scheduling, state delivery, portrait routing, and policy effects: `common/scripted_effects/016_brilliant_scientist_evolution_effects.txt`
- Evolution incidents: `events/016_brilliant_scientist_evolutions.txt`
- Sovereignty deadline mission: `common/decisions/016_brilliant_scientist_evolution_missions.txt`
- Player-facing text: `localisation/english/016_brilliant_scientist_evolutions_l_english.yml`
- Portrait and report sprites: `interface/016_brilliant_scientist.gfx`
- Canonical design: `docs/specs/016_brilliant_scientist_specs/specs/016_brilliant_scientist_spec_part_4_evolutions_and_event_chain.md`

## Visual assets

Each evolution incident has a dedicated `210x176` report-event DDS under `gfx/event_pictures/016_brilliant_scientist/`. Kruger's stage portraits use full `156x210` textures under `gfx/leaders/KRG/` and separate native `65x67` advisor dossier textures under `gfx/interface/ideas/016_brilliant_scientist/`.

Severe animated portraits require real frame-by-frame source animation, a static fallback, a frame sheet, and state-specific runtime selection. Transform-only motion is not accepted.

## Open validation

Static audits have verified the four-stage identity, scheduler references, incident IDs, localisation, and asset registrations. Live pacing, visual transitions, the Evolution IV deadline, and disabled-stage campaign behavior remain user-owned in-game validation surfaces.
