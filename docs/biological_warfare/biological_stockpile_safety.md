# Biological Stockpile Safety

## Purpose

Biological payload production creates a domestic storage problem before it
creates a delivery option. The stockpile-safety subsystem binds one exact state
as the national arsenal, reads the four live payload inventories, exposes a
player-facing risk band, and resolves ordinary accidents through the shared
ordinary-pathogen lifecycle.

The arsenal decision is management only. It cannot target another country or
release an agent. Anthrax, Plague, Tularemia, and Smallpox deployment remains in
the native biological raid routes.

## Exact arsenal designation

Completion of an agent special project records its exact facility state through
`facility_state_effects` when that context exists. The first verified project
facility becomes the national arsenal. If a project was completed by script,
the engine may provide no facility state, so the country must use
`bio_designate_national_biological_arsenal` on an exact owned, controlled state
with a `biowarfare_facility`.

The persistent country pointer is
`bio_stockpile_safety_arsenal_state`. The state records the matching country in
`bio_stockpile_safety_arsenal_actor`. Validation never scans for a replacement,
chooses a random state, or reconstructs a completed project location.

## Risk calculation

`bio_stockpile_safety_refresh_risk_band` reads:

- live `num_equipment@` values for all four payload models;
- danger weights calibrated against each agent's native raid reservation;
- the national Biosecurity meter;
- Pathogen Handling Protocols, Sealed Containment Laboratories, and Fail-Safe
  Containment Facilities;
- exact facility level, damaged level, and operational level;
- exact-state strategic bombing, sabotage, and recent handling records.

The accepted matrix defines the bands:

| Band | Primary condition | Ordinary accident expectation |
|---|---|---|
| Controlled | Biosecurity 70 or higher, stock below the high threshold, no damage or sabotage | negligible |
| Strained | Biosecurity 40 to 69, high stock, handling strain, or limited facility damage | rare and usually contained |
| Dangerous | Biosecurity 20 to 39 with a large stock, a disabled facility, or recent bombing | meaningful local outbreak risk |
| Critical | Biosecurity below 20, extreme stock, war damage, or confirmed sabotage | major domestic outbreak and public exposure possible |

The 0-100 risk score is a readable summary. Band assignment still evaluates the
explicit matrix conditions and does not reduce them to score cutoffs.

## Targeted monitor

There is no all-country daily, weekly, or monthly pulse. A delayed hidden event
is scheduled only for a country with a verified arsenal pointer. Every thirty
days it reads the current equipment and facility values, updates the visible
risk idea, and performs the band-specific ordinary-accident roll. A due-day
record makes delayed events from an old designation inert after relocation.
If the exact state is temporarily uncontrolled or its facility is disabled, the
same country-specific monitor remains armed but performs no roll. It resumes on
that exact pointer after control and an operational facility return; it never
searches for another state.

The current HOI4 documentation exposes the live stockpile value but no custom
on-action for completion of each equipment unit. The targeted monitor therefore
samples the authoritative live inventory at its scheduled boundary. It does not
estimate output, infer a production line, or iterate over countries without an
active verified program.

## Accident resolution

When an accident occurs:

1. The agent is weighted by its exact current payload count, excluding only an
   agent still under its own two-year accident cooldown.
2. Severity is selected from Contained Incident, Laboratory Contamination,
   Local Outbreak, Major Domestic Outbreak, or International Exposure.
3. A severity-scaled amount of the exact matching payload equipment is removed
   once from the national stockpile.
4. The exact designated state records the agent, severity, date, and stock loss.
5. A contained incident creates no outbreak seed.
6. Every non-contained incident enters `bio_lifecycle_dispatch_seed` with route
   `laboratory_accident`, source `accident`, result `accident`, and exact domestic
   actor and victim scopes.
7. Incubation, detection, contamination, medical saturation, deaths, evidence,
   confirmed-accident attribution, Condemnation, spread, and cleanup remain
   owned by the shared biological lifecycle.

Only one unresolved accident notification may exist for a country. The monitor
keeps its targeted cadence while a notification is pending but cannot overwrite
that incident's agent, severity, evidence, or stock-loss record.

Fail-Safe Containment Facilities prevent ordinary stockpile accidents. They do
not prevent sabotage, bombing, captured-facility release, or doomsday release.
Doctrine can make a seeded episode more potent and may reduce Condemnation only;
it does not erase stock loss, evidence, attribution, deaths, contamination,
medical saturation, or accident history.

## AI behavior

AI countries prefer a core state with an operational facility and stronger
infrastructure. They avoid an active outbreak state and strongly prioritize a
new designation when the current pointer is invalid. The engine has no verified
exact state-scope frontline predicate, so no unrelated building or regional
proxy is used for frontline distance.

## Assets and wiring

| Gameplay id | Sprite | Runtime DDS |
|---|---|---|
| `bio_stockpile_risk_controlled` | `GFX_idea_bio_stockpile_risk_controlled` | `gfx/interface/ideas/cbrn/idea_bio_stockpile_risk_controlled.dds` |
| `bio_stockpile_risk_strained` | `GFX_idea_bio_stockpile_risk_strained` | `gfx/interface/ideas/cbrn/idea_bio_stockpile_risk_strained.dds` |
| `bio_stockpile_risk_dangerous` | `GFX_idea_bio_stockpile_risk_dangerous` | `gfx/interface/ideas/cbrn/idea_bio_stockpile_risk_dangerous.dds` |
| `bio_stockpile_risk_critical` | `GFX_idea_bio_stockpile_risk_critical` | `gfx/interface/ideas/cbrn/idea_bio_stockpile_risk_critical.dds` |
| `bio_designate_national_biological_arsenal` | `GFX_decision_bio_designate_national_biological_arsenal` | `gfx/interface/decisions/biowarfare/bio_designate_national_biological_arsenal.dds` |

All sprites are registered in `interface/biological_warfare.gfx`. Source PNGs,
processed PNGs, contact sheet, DDS validation, hashes, and prompts live under
`docs/assets/chaos_warfare_system/stage_7_biological_warfare/stockpile_risk_ideas/`.
The existing native raid icons under `gfx/interface/military_raids/` are
unchanged.

## Future plans and required continuations

Captured-facility secure, destroy, evidence-preservation, and accidental-release
handling must be completed with exact capture context and verified Biological
Security Assault Detachment participation. Doomsday release, remaining
countermeasures and treatment, designer risk traits, package scenarios, and the
Stage 7 specialist audits remain required before biological warfare or the full
CBRN goal can be called complete.
