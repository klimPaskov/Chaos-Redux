# Equipment from Heavens: Evolutions and Integrations

## Evolution model

Event 42 has one global evolution track with three stages. Each stage becomes eligible at its Chaos threshold, then advances through the normal evolution pacing system. A starting mean time near ninety days is appropriate, with bounded adjustments from current Chaos, recent Event 42 firings, world war intensity, and whether the event has already demonstrated the prior stage.

Evolution activation changes future manifests. It gives no equipment by itself and adds no Chaos by itself.

When an evolution is active before Event 42 first fires, the first delivery immediately uses the active stage. The event does not require a weaker baseline firing before an evolved opening.

Each stage receives one evolution log entry with a global actorless context. The title direction should describe the changing nature of the skyfall, not a hidden scripting threshold.

## Evolution I: Everything Falls

- Chaos requirement: 200+

The equipment pool becomes much broader and more advanced. The sky begins treating every existing conventional military family as equally plausible cargo.

### Pool expansion

Evolution I adds or makes common:

- mechanized vehicles
- amphibious tanks and amphibious equipment
- tank destroyers
- self-propelled artillery when a safe complete variant exists
- self-propelled anti-air when a safe complete variant exists
- specialized support vehicles
- advanced rocket artillery
- additional fighter and bomber roles
- transport aircraft when safely grantable
- higher-tier trains and logistics equipment
- foreign designer variants
- mixed equipment lineages from several countries

The event remains indifferent to strategic relevance. Landlocked recipients can receive amphibious equipment. Countries with weak fuel access can receive enormous armored fleets. Countries with no meaningful air force can receive thousands of aircraft.

### Technology level

The recipient's research position becomes a weaker constraint on selection.

Suggested technology mix:

- 20 percent recognizable peer equipment
- 45 percent one or two meaningful generations ahead
- 25 percent highest safe conventional tier for the family
- 10 percent unusual foreign or specialized variants

This distribution is a starting point for probability review. Every selected item remains an existing conventional family or a complete conventional variant.

### Manifest scale

Evolution I increases the average family count and shifts magnitude toward Colossal and Impossible. It can also raise the value share assigned to specialized families. The event should not hide the evolution inside the same small baseline composition.

### New report themes

Reports can describe equipment that local officers recognize only from foreign journals, vehicles built for terrain the recipient does not possess, amphibious parks hundreds of kilometers from the sea, and aircraft without familiar controls or markings.

## Evolution II: Arsenal of the Future

- Chaos requirement: 400+

The sky begins delivering the highest existing conventional equipment tiers and can create a sudden nuclear power.

### Highest-tier conventional pool

Every safe late-game conventional family becomes eligible regardless of recipient research or current date. The manifest can contain the best complete tanks, mechanized vehicles, aircraft, artillery, anti-tank, anti-air, rockets, trains, and support systems present in the installed game and mod.

Evolution II is not a research preview. The quantity remains enough to decide wars. A recipient can receive tens of thousands of late-game vehicles or aircraft.

### Nuclear cache roll

Evolution II adds a nuclear slot after the conventional manifest is valid.

Suggested starting chance by current Chaos:

| Current Chaos | Nuclear cache chance |
| --- | ---: |
| 400 to 599 | 25 percent |
| 600 to 799 | 35 percent |
| 800 to 999 | 45 percent |
| 1000+ | 55 percent |

The probability should be capped and audited. Package magnitude can adjust quantity but should not make the nuclear result guaranteed.

Suggested nuclear quantities:

- standard cache: 25 to 75 weapons
- Colossal cache: 75 to 150 weapons
- Impossible cache: 150 to 250 weapons

These quantities are intentionally substantial. They can turn a previously irrelevant country into a nuclear actor.

### Physical nuclear ownership

The recipient receives nuclear weapons through the existing nuclear stockpile system. It does not receive nuclear research, bomb production, nuclear facilities, special projects, research bonuses, or a permanent source of replacements.

Implementation must prove that a country with physical weapons but without nuclear research can actually launch them through the current engine and mod rules. If ordinary launch access is blocked by production technology, Event 42 needs a narrow launch-only compatibility contract.

That contract must permit use of the received stockpile while preserving these limits:

- no nuclear weapon production
- no nuclear research completion
- no research-tree reveal beyond normal behavior
- no free facility
- no thermonuclear access
- no missile technology
- no bypass of ordinary delivery-platform, target, air, war, or range conditions except where the existing nuclear system already permits it
- no persistence after the country has no Event 42 nuclear stockpile unless the normal game later grants access

A launch-only contract can reuse a validated Event 23 physical-stockpile route when that event is implemented. If no safe route exists, Evolution II is incomplete. Granting an unusable number is not an acceptable fallback.

### Nuclear use consequences

Possession alone does not create Condemnation. Actual use enters the existing nuclear-use, fallout, Deaths, Air Cleanliness, world tension, Condemnation, and Chaos pipelines. Event 42 must not duplicate those consequences.

A delivery to a country with no prior nuclear capability can create one event-owned proliferation milestone in the Chaos impact map because the dangerous capability has materially entered the world. Later use still follows shared sources.

### Report themes

Reports should become severe and controlled. The recipient discovers sealed weapon cores, handling equipment, coded custody instructions, or a guarded storage site whose doors were never built locally. Final text should avoid jokes and avoid claiming a sender.

## Evolution III: Chaos Arsenal

- Chaos requirement: 600+

The sky can deliver existing special Chaos Redux equipment whose source event has not occurred for the recipient or may not have occurred anywhere.

This stage never invents a new equipment family. It uses an explicit allowlist built from repository evidence.

## Special-equipment inclusion roll

Evolution III adds a special slot after the conventional and nuclear manifest is validated.

Suggested starting distribution:

- 40 percent no special family
- 40 percent one special family
- 15 percent two distinct special families
- 5 percent three distinct special families

The pool contains only families marked safe for the current repository revision. If fewer safe families exist than the roll requires, reduce the number of distinct special families without duplicating one token. The conventional package remains full size.

The absence of a safe special family is an implementation blocker for the stage's intended identity. It is not permission to invent generic alien guns, zombie rifles, or placeholder equipment.

## Special-equipment registry contract

Every candidate family needs one registry row with:

- source event or owner system
- exact concrete equipment token
- physical stockpile grant proof
- equipment-unit meaning
- matching battalion, support unit, raid, air mission, or other consumer
- independent-use status
- production-access status
- minimum compatibility receipt when needed
- AI fielding and use rules
- quantity basis
- source-event isolation checks
- cleanup behavior
- current repository evidence
- final status: allowed, conditional, or excluded

The full working matrix is in `research/042_equipment_from_heavens_special_equipment_audit_matrix.md`.

## Compatibility receipts

A compatibility receipt is the smallest Event 42-owned permission needed to consume a physical stockpile. It is not a copy of the source event.

A fielding receipt may:

- expose one existing inactive battalion to the recipient
- create one editable stockpile-consuming template
- allow the AI to field that template
- reveal the correct equipment icon and unit text
- register bounded sustainment and cleanup behavior

A payload receipt may:

- expose one existing captured-payload use action
- require an actual payload in stockpile
- use the ordinary target, range, war, fuel, command, delivery-platform, and consequence rules
- consume the physical payload once

A compatibility receipt must not:

- mark the source event as fired
- unlock a source evolution
- create a source country
- set a source world-threat flag
- grant source projects or project stages
- grant source facilities
- grant source production rights
- grant source focus trees or decisions beyond the minimum captured-equipment action
- grant source technologies except a hidden non-production access token that has no broader effect
- show source super-events
- unlock source terminal routes
- register the recipient as the source event's host
- create a permanent replacement pipeline

When the owner API cannot separate fielding from production or source lifecycle, exclude the equipment family.

## Provisional repository findings

### Clone equipment

The current repository defines `clone_equipment_1` as a provider-neutral physical cohort. Captured, transferred, or lend-leased clone equipment gives reserve manpower to its current holder even without manufacturing access. This makes the token a strong first candidate.

The existing `clone_grant_infantry_access` effect also enables manufacture, so Event 42 should not call it unchanged. The implementation needs either a fielding-only clone receipt or a deliberate choice to let the skyfall function only as a reserve-manpower stockpile. A fielding-only receipt is preferred because Evolution III promises usable special military equipment.

Special quantity should follow cohort meaning rather than conventional rifle counts. A package can contain hundreds or thousands of clone cohorts, which is already enormous.

### Event 16 project-force equipment

Existing tokens include:

- `teleportation_equipment_1`
- `autonomous_robot_equipment_1`
- `paleogenetic_creature_equipment_1`
- `xenobiological_assault_organism_equipment_1`
- `alien_laser_weapon_equipment_1`
- `temporal_guard_equipment_1`

The equipment can be placed in stockpile, but the matching battalions are inactive and normal production is tied to project, facility, Kruger, or contact conditions. These families remain conditional until a fielding-only receipt is proven for each one.

The receipt must not set Kruger project stages, facility flags, contact-source counts, or operational technology flags. Alien contact and Event 16 ownership must remain unchanged.

### Coal golems

`coal_golem_equipment_1` is a real stockpile token. Its matching `coal_golem` battalion is inactive, and production belongs to the Kuznetsk Mining Board or validated Event 19 derivatives.

Event 42 can use this family only after a fielding-only receipt creates a bounded template without granting KMB identity, derivative status, coal-golem production, or Event 19 provider registration.

### Black Plague payloads

`plague_bomb_1` is a real physical payload. The current Black Plague delivery contract also requires Event 020 system activation, project or technology access, weaponization-complete flags, delivery readiness, support equipment, command power, fuel, a valid hostile target, and cooldown logic.

Raw stockpile ownership is therefore insufficient. The token stays excluded from the first allowlist unless the Black Plague owner exposes a provider-neutral captured-payload route that preserves ordinary delivery and consequence rules without starting Event 020.

### Other biological and zombie payloads

Existing stockpile tokens include anthrax, tularemia, smallpox, and zombie-disease bombs. Their safe use depends on the shared biological-warfare and delivery systems. They remain conditional until the owner systems provide a captured-payload contract.

### Chemical special bombs and payloads

Existing chemical bombs, cylinders, shells, air payloads, and agent lots are physical stockpile items. Their battlefield use belongs to the shared CBRN command, payload, raid, support-unit, and Condemnation systems.

Event 42 must not initialize the entire CBRN system merely to make one package usable. A candidate is allowed only when a narrow captured-payload path can consume it through the established consequence pipeline.

### African strange formations

The Event 012 repository package defines eight strange-formation equipment families and matching inactive battalions. Production depends on a global package-readiness gate and owner systems.

These tokens remain conditional. A safe Event 42 receipt must open only the matching field consumer and cannot set the global Event 012 package-ready state, launch Africa Is One, create Event 012 countries, or unlock Event 012 routes.

## Special quantity basis

Special equipment units have different meanings. Their quantities should be calculated from their real consumer rather than copied from rifle bands.

Use these roles:

- battalion equipment: enough for 10 to 40 full battalion-equivalents in Enormous packages, 40 to 100 in Colossal packages, and 100 to 250 in Impossible packages
- clone cohorts: 250 to 1,000 in Enormous packages, 1,000 to 2,500 in Colossal packages, and 2,500 to 5,000 in Impossible packages, subject to reserve-manpower balance review
- strategic payloads: 10 to 30 in Enormous packages, 30 to 80 in Colossal packages, and 80 to 200 in Impossible packages
- support attachments: enough for 25 to 75 divisions in Enormous packages, 75 to 200 in Colossal packages, and 200 to 500 in Impossible packages

The implementation should translate battalion-equivalents through the actual equipment need of the verified unit. Every result remains rounded and visible in the manifest.

## Cross-event isolation

Receiving special equipment must leave the source event in the same lifecycle state it had before the delivery.

The implementation must snapshot and compare at least:

- source fired count
- source event weight and cap
- source evolution flags and log records
- source country and host markers
- source world-threat flags
- source focus and decision unlock flags
- source special-project state
- source facility state
- source super-event visibility
- source terminal-route eligibility

A permitted owner-neutral callback can register the minimum fielding receipt. It must be documented as an Event 42 compatibility consumer, not as evidence that the source event fired.

## Source event later firing

If the source event fires after Event 42 has distributed its equipment, the source event remains authoritative for its own project, countries, evolutions, production, and world consequences.

The source event should detect the recipient's captured-equipment receipt and merge access cleanly. It must not duplicate templates, remove legitimate stockpile, or misclassify the earlier recipient as a source host.

When source and Event 42 access conflict, source-event ownership wins. Event 42 retains only the fact that the earlier stockpile came from a skyfall.

## Chaos impact map

Event 42 is beneficial, but its physical impossibility and proliferation effects make the world less predictable.

| Milestone or outcome | Why Chaos changes | Direction | Starting magnitude | Dynamic factors | Repeat guard | Shared-source overlap | Reversal or containment counterpart |
| --- | --- | --- | ---: | --- | --- | --- | --- |
| First successful public skyfall | A material arsenal has appeared without a sender or delivery route | Increase | +2 | None | Once globally for Event 42 | Does not duplicate military buildup because the cause is the anomaly | No direct refund because the manifestation cannot be undone |
| First nuclear cache delivered to a country with no prior bombs or production access | A new nuclear actor exists through an impossible proliferation route | Increase | +10 | May fall to +5 if the recipient already had launch access but no stockpile | Once globally | Nuclear use later follows the shared nuclear ladder | Later disarmament can use a future shared disarmament source, not an automatic Event 42 refund |
| First verified Chaos Arsenal family delivered and made fieldable outside its owner event | An event-owned capability has escaped its original system | Increase | +5 | +10 when the family is a strategic mass-casualty payload | Once globally across Evolution III | Actual CBRN, nuclear, deaths, contamination, war, and conquest effects use their shared sources | Destroying a quarantined captured payload can lower Chaos only through an owner-approved dismantlement path |
| Evolution I, II, or III activation | The event gains future capability but no material outcome has happened | No change | 0 | None | Not applicable | Not applicable | Not applicable |
| Ordinary repeat delivery | The event is already known and repeatability alone should not farm Chaos | No direct change | 0 | None | Every ordinary repeat | Military buildup remains handled by shared systems | Not applicable |
| Nuclear, chemical, biological, or special weapon use | The delivered weapon produces a concrete consequence | Shared systems | Shared values | Existing target, deaths, contamination, repeat-use, and condemnation factors | Existing shared guards | Event 42 adds nothing for the same consequence | Existing containment and cleanup systems |

Direct Event 42 Chaos contribution should remain bounded. The first manifestation, first nuclear proliferation, and first fieldable Chaos Arsenal escape are the meaningful authored milestones. The event must not add Chaos for every crate, landing report, family, or repeat firing.

## Cluster integration

Equipment from Heavens belongs to Various Anomalies as a Low member. The cluster assignment follows the accepted design even though the current export has no numeric cluster ID or member list.

The event can be selected normally at Chaos level 1. Cluster eligibility remains independent and follows the final Various Anomalies cluster unlock and participation rules.

When Event 42 is the selected root of a cluster firing, it creates one delivery. When it joins as an optional member, it also creates one delivery. It cannot fire twice inside the same cluster transaction.

The cluster counts as one pacing event. Event 42 still records its own actor, history, fired count, repeatable cap reduction, and effects. Landing reports do not add pacing.

If no eligible recipient exists during a cluster transaction, the member is skipped with a clear invalid-recipient reason. The cluster does not substitute a special country.

## Evolution enable and disable behavior

Every evolution is independently governed by the normal event evolution controls.

A disabled Evolution I keeps future deliveries on the baseline pool even if higher Chaos is reached. Evolution II cannot silently bypass a disabled Evolution I unless the shared evolution framework explicitly supports independent stage activation and the event's log and pool state remain coherent. The preferred model is ordered progression.

A disabled Evolution II prevents nuclear caches and highest-tier future arsenals. A disabled Evolution III prevents all Chaos-equipment slots and compatibility receipts.

Disabling an evolution after equipment was already granted does not delete stockpile, templates, receipts, or history. It affects future manifestations only.
