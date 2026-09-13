# Event 062 implementation surface map

## Status of this map

The paths below follow current Chaos Redux conventions from the supplied skills. They are provisional until the implementation agent inspects the actual repository. Existing local files and patterns take priority when they provide the same ownership cleanly.

## Event-owned source files

| Surface | Provisional path | Ownership |
| --- | --- | --- |
| event chain | `events/062_allies_backstab.txt` | entry, role events, delayed transaction events, settlement reports |
| script constants | `common/script_constants/062_allies_backstab_constants.txt` | faction budgets, size bands, grace, cooldowns, cohesion, costs, durations, AI factors |
| scripted triggers | `common/scripted_triggers/062_allies_backstab_triggers.txt` | valid faction leader, valid member, political unit, target eligibility, side legality, mission conditions, cleanup |
| scripted effects | `common/scripted_effects/062_allies_backstab_effects.txt` | snapshot, scoring, selection, transaction phases, side assignment, settlement, cleanup |
| decisions | `common/decisions/062_allies_backstab_decisions.txt` | role actions and missions |
| category | `common/decisions/categories/062_allies_backstab_categories.txt` | event-owned crisis category |
| ideas | `common/ideas/062_allies_backstab_ideas.txt` | staged victim, loyalist, and liaison states when ideas are the chosen local precedent |
| opinion modifiers | `common/opinion_modifiers/062_allies_backstab_opinion_modifiers.txt` | betrayal, defection, guarantee, mediation, settlement, violation memories |
| AI strategy | `common/ai_strategy/062_allies_backstab_ai_strategy.txt` | temporary role-aware strategy where ordinary decision weights are insufficient |
| active processing | `common/on_actions/062_allies_backstab_on_actions.txt` | sparse active-generation processing only when the repository pattern requires it |
| event assets registry | `interface/062_allies_backstab.gfx` | event picture, category picture, decision, mission, idea, achievement, and super-event sprites as applicable |
| event localisation | `localisation/english/062_allies_backstab_l_english.yml` | event, decision, mission, idea, opinion, achievement, and tooltips |
| scripted localisation | `common/scripted_localisation/062_allies_backstab_scripted_localisation.txt` | role, cohesion, target, faction, capital, terms, and generation summaries |
| event documentation | `docs/events/062_allies_backstab/` | implemented mechanic, assets, tuning, interactions, and validation evidence |

## Shared surfaces

The implementation should update the current local equivalents of these shared systems.

| Shared system | Required Event 62 change |
| --- | --- |
| event category initialization | register `62` as Minor Repeatable |
| event chaos-level registry | register Chaos level `1` |
| default enabled-event allowlist | enable Event 62 after the rework is complete |
| event name selectors | resolve `Allies Backstab` in event log and debug views |
| Event Details catalog | add premise, Chaos level, type, current status, and three Evolutions |
| event history logger | one global row per Event 62 firing, no duplicate row per faction transaction |
| evolution logger | register Evolution I, II, and III with correct actor rules |
| Wars cluster | add Event 62 as a High member without replacing any other membership |
| cluster availability | call the Event 62 valid-target gate and return a clear skip reason |
| Chaos Meter faction-change hook | classify Event 62 forced exits so they do not receive the ordinary negative leave source |
| Chaos History | add distinct structural fracture and settlement-violation reasons only if retained after overlap audit |
| super-event framework | add one conditional Evolution III slot and audio ID if the strict threshold is met |
| achievement registry | add four Event 62 achievements to the single Chaos Redux file |
| catalog workbook | update the authoritative XLSX and run the exporter |

## Entry and event chain

The exact subevent IDs should be chosen after repository inspection. The logical chain needs these roles:

1. `chaosx.nr62.1` entry and global resolver
2. global summary for uninvolved human players
3. faction-leader role event
4. expelled-government role event
5. retained-member role event
6. pending-member stance event for Evolution II and III
7. selected sponsor or mediator event
8. delayed war launch and revalidation
9. mission success, partial success, and failure reports where a visible event is useful
10. settlement offer and acceptance events
11. outcome and cleanup reports
12. Evolution III global super-event trigger

Hidden runtime events should not create player-facing popup spam.

## Script constant groups

The implementation should centralize at least these groups:

- event identity and Evolution IDs
- faction-count budgets by eligible pool and Evolution
- political-unit victim count bands
- full-fracture and global mutation caps
- ordinary join grace, successor-faction grace, victim protection, and faction cooldown
- cohesion base values, thresholds, gains, losses, and caps
- side-viability floors
- strength-ratio bands
- decision cost floors, scaling steps, and caps
- mission duration floors, scaling, and caps
- AI factor multipliers
- settlement thresholds
- outside sponsor cap
- Chaos source values and anti-repeat rules
- super-event threshold values

No tuning number should be copied across several event, decision, trigger, and localisation files.

## Event-owned APIs

The event should expose owner-specific helpers with clear contracts. Working names below describe behavior and are not mandatory identifiers.

### Read-only triggers

- valid global Event 62 target exists
- country is a valid faction transaction anchor
- country is a valid victim political-unit leader
- country is in a given Event 62 generation
- country is a loyalist, victim, pending member, neutral withdrawal, or sponsor
- side assignment is legal
- political unit can move safely
- event-linked war exists
- mission objective is satisfied
- settlement terms are legal
- generation can clean up

### Mutating effects

- collect valid faction anchors
- snapshot one faction
- build political units
- calculate faction pressure
- calculate member vulnerability
- select victims without replacement
- assign initial roles
- reconcile subject bundles
- expel one political unit with a receipt
- prepare withdrawal access
- schedule and revalidate war launch
- attach participants to a legal conflict
- initialize side cohesion
- open and close role decisions
- evaluate member stance
- create or dissolve victim liaison
- calculate settlement willingness
- submit a settlement offer
- resolve outcome
- clean one generation

## Shared helper review

Before adding any neutral helper, inspect `chaosx_dynamic_effects` and local shared APIs.

Event 62 selection, transaction, side assignment, and lifecycle logic remains event-owned. A new helper belongs in the shared dynamic registry only when its contract is neutral and already needed by unrelated systems.

Potential owner API calls include:

- subject independence request
- Random Civil War request
- Chaos History registration
- Event Logs registration
- settings-aware super-event sound
- stockpile debit helpers
- event-cluster member result

Do not copy an owner API into Event 62.

## Active processing

The event must not add an unbounded whole-world daily, weekly, or monthly scan.

Preferred model:

- one-shot world scan only when Event 62 fires to collect valid faction leaders
- global array of active faction transaction anchors
- country or leader scoped periodic processing over that array
- event-driven updates for capital loss, mission resolution, defection, peace, and country destruction
- immediate removal from the active array during cleanup

If the current repository has a generic sparse registry or pulse system, Event 62 should register with it.

## Decision implementation

The event uses one category with role-based visibility. It does not introduce a dedicated scripted GUI.

Required features:

- selected-target pattern for multi-victim, member, or sponsor actions
- three to five visible actions per phase, six maximum
- one to three active missions
- goal-style auto-completion
- dynamic costs with correct texticons
- custom trigger tooltips for dynamic capitals, routes, faction names, and side leaders
- AI access that does not depend on human target selection
- cleanup on annexation, faction change, war end, settlement, and role change

## Event log and Event Details

The implementation should preserve the distinction between history and catalog views.

Event history:

- one row per global firing
- date, event ID, event name, affected faction count, expelled country count, split count, linked war count
- no fake actor when several factions are involved

Evolution history:

- Evolution I can remain global
- Evolution II can use the first split's faction leader as actor
- Evolution III can remain global

Event Details:

- premise and public event identity
- Chaos level 1
- Minor Repeatable type
- Wars cluster and High role
- three Evolution previews
- latest generation summary when available
- no target-score or hidden side-choice formula

## Asset consumers

Provisional runtime groups:

- report event picture at the current event-picture consumer size
- static decision category picture at the verified category-picture size
- decision icons at the current decision icon size
- mission icons at the current mission icon size
- idea icons at the current idea or national-spirit size
- achievement triplets in `gfx/achievements/`
- conditional super-event image at the current super-event size

The asset worker must inspect exact vanilla and Chaos Redux consumers before production.

## Catalog update

The workbook row should contain player-facing wording consistent with final localisation:

- ID `62`
- Event name `Allies Backstab`
- expanded premise
- Evolution I `Alliance Purges`
- Evolution II `Internal Bloc Wars`
- Evolution III `The Alliances Collapse`
- Type `Minor Repeatable`
- Chaos level `1`
- Cluster `Wars`
- Member severity `High`
- implementation status chosen from the repository's accepted workflow

Never edit the three CSV exports directly.

## Mandatory evidence before completion

- offline wiki and vanilla documentation review
- vanilla and Chaos Redux faction, war, decision, event, and asset precedents
- `hoi4.event_inspect` before implementation
- event render and compare after implementation
- baseline probability audit
- owner implementation and balance pass
- `hoi4.probability_compare` with the same named scenarios
- decision and mission audit
- localisation audit
- conditional super-event research and wiring audit
- event completion audit
- workbook export proof
- acceptance scenario report
- explicit simplification and blocker section
