# FORM-05: Mediterranean Island League

## Overview

FORM-05 is a charter-driven league transformation for the Event 006 Corsican,
Sardinian, and Sicilian packages. `COR`, `ARX`, or `ASX` may carry the charter
when it is a living, sovereign regional power with its exact island anchor and
a working naval base. Future Event 006 countries assigned to the same
Mediterranean Island League family may join as compatible island governments.

`MIX` is a cosmetic identity. The carrier keeps its gameplay tag, history,
focus tree, characters, armed forces, territory, cores, and capital. Consenting
governments remain sovereign and receive league membership flags and the
ratified charter idea. Formation never annexes a country, transfers a state,
creates a subject, grants a core, or replaces vanilla `COR`.

## Charter sequence

Before a country can carry the charter, its package route must authorize a
FORM-05 delegation and complete the 300-day Prepare the Maritime Congress
project. That project pays the full strategic package and records the exact
country-specific carrier mandate; it does not start or bypass the shared
charter transaction.

1. A qualified `COR`, `ARX`, or `ASX` carrier petitions for the maritime
   congress. The opening conference lasts 75 days and pays light
   administrative and standard diplomatic commitments.
2. The carrier opens a 540-day charter mission with Shipping Guarantees at 25,
   Common Defense at 20, and Customs Union at 15.
3. The opening effect walks only the reconciled Event 006 active-country
   registry. Connected countries assigned to FORM-05 receive a sovereign
   invitation. Each government spends 35 days and a light diplomatic
   commitment to authorize or withhold its own delegation.
4. The carrier completes three mutually exclusive projects:

   - Chart the Convoy Guarantees: 55 days and a standard diplomatic commitment.
     Shipping and Customs each gain 25.
   - Ratify the Common Defense Protocol: 75 days and a standard security
     commitment. Defense gains 25 and Shipping gains 20.
   - Conclude the Customs Convention: 55 days and standard administrative and
     diplomatic commitments. Customs and Defense each gain 25.

5. Once all three values are at least 50 and a second live government has
   consented, a 55-day capital conference chooses either a rotating island
   congress or a permanent secretariat at the carrier capital. The settlement
   completes the remaining five Customs points.
6. Shipping, Defense, and Customs must each reach 70. The carrier must still
   have a connected, consenting core partner and a valid capital settlement.
   A final 75-day ratification pays a strategic and light administrative
   commitment before applying `MIX`.
7. Missing the 540-day deadline reduces every public value by 10 and applies
   Charter Breakdown. A global 180-day recovery window prevents another island
   government from immediately bypassing the failed congress.
8. Proclamation establishes the `MIX` identity but does not complete regional
   integration. It opens a separate 720-day First Maritime Board mission and
   requires at least one other living, autonomous, diplomatically connected
   founding member for every project and for final ratification.
9. The carrier completes a common shipping board, a linked coastal-warning
   chain, and a customs clearinghouse. These costed projects raise Shipping,
   Defense, and Customs from the charter threshold toward 95. The opening board
   must also choose whether convoy administration or coastal warning receives
   first priority; the favored value gains five while a competing value loses
   five.
10. A 55-day ratification may begin only after all three projects are complete,
    every public value is at least 95, and a live sovereign member remains
    connected. Only this action sets the shared first-stage and required-initial-
    integration completion flags used by Event 006 achievements.
11. Missing the first-board deadline removes the three project certificates,
    reduces every public value by 15, and replaces the ratified charter idea
    with Charter Breakdown. A costed 75-day reconvening restores the lost 15
    points in each ledger and reopens the mission; the projects must be
    performed again before ratification.

## Costs and resource behavior

The system uses the Event 006 shared cost packages. It never creates a
political-power store and never grants free divisions or equipment.

| Action | Duration | Material commitment |
| --- | ---: | --- |
| Opening congress | 75 days | Light administration plus standard diplomacy and civilian industry |
| Delegation response | 35 days | Light diplomacy |
| Shipping article | 55 days | Standard diplomacy and civilian industry |
| Defense article | 75 days | Standard security and civilian industry |
| Customs article | 55 days | Light administration plus standard diplomacy and civilian industry |
| Capital settlement | 55 days | Light administration and civilian industry |
| Final proclamation | 75 days | Strategic cost, light administration, and one civilian factory |
| Reopening after failure | 75 days | Strategic cost and one civilian factory |
| Common shipping board | 75 days | Standard diplomacy, ten convoys, and one civilian factory |
| Coastal-warning chain | 75 days | Standard security and one civilian factory |
| Customs clearinghouse | 55 days | Light administration, standard diplomacy, ten convoys, and one civilian factory |
| First-board ratification | 55 days | Light administration and one civilian factory |
| Reconvene the first board | 75 days | Strategic cost, ten convoys, and one civilian factory |

The underlying cost helpers spend command power, manpower, convoys, army
experience, infantry equipment, support equipment, stability, and war support
as appropriate. FORM-05 explicitly requires convoy capacity, so the generic
landlocked train substitution cannot satisfy a charter action. Project
cancellation does not refund resources already committed.

The complete successful carrier path lasts 390 project-days, leaving 150 days
inside the charter deadline for resource recovery and political delay. Across
those projects the carrier commits 120 Command Power, 15,000 manpower, 40
convoys, 20 Army Experience, 500 infantry equipment, 100 support equipment, 10
percent Stability, and 5 percent War Support. Every carrier project assigns one
civilian factory temporarily and projects run sequentially. Corsica, Sardinia,
and Sicily each begin with one civilian factory, while the shared port/island
economic program adds a dockyard; the one-factory assignment therefore keeps
the route reachable without erasing its entire productive capacity for free.
This burden is substantial for an island state but
does not demand the manpower reserve that a 25,000-man standard-administration
path would impose on Corsica.

The mandatory post-formation path adds 260 project-days inside its 720-day
deadline. Failure recovery is deliberately expensive and cannot be used as a
free progress loop: the failed project certificates are cleared, public values
fall, and the reconvening action pays the full strategic package before the
three projects can be attempted again.

## AI behavior

AI carriers prioritize the charter and its naval-defense articles when their
former hosts pose a severe threat. Invited AI governments normally authorize a
delegation and become more willing when the carrier faces host pressure. Severe
domestic instability blocks acceptance. Patron-client governments and unstable
governments are more likely to withhold their mandate. Constitutional carriers
prefer a rotating congress, while traditional and emergency-military carriers
prefer a permanent secretariat.

## Identity and lifecycle

- `independence_wave_form05_provisional_maritime_charter` applies during the
  active 540-day congress.
- `independence_wave_form05_ratified_island_union` applies to the carrier and
  every connected consenting sovereign member after proclamation.
- `independence_wave_form05_charter_breakdown` applies after a missed deadline
  and remains until a qualified carrier reopens the congress.
- Event IDs `chaosx.nr6.28` through `chaosx.nr6.34` cover the opening congress,
  capital settlement, proclamation, charter breakdown, first-board priority,
  first-stage ratification, and first-board failure.

FORM-05 is registered in the shared regional-formable readiness registry, but
the generic formation transaction is intentionally closed for this family.
Its sovereign charter is the sole formation path; this prevents the generic
integration adapter from annexing members or bypassing the consent ledger.

## Asset and runtime-readiness contract

FORM-05 has no mutable asset switch. Its visible gameplay surface requires
`has_independence_wave_form05_runtime_readiness`, which proves the selected
Mediterranean Island League family, its exact readiness-family value, the
territory, X-tag, flag, identity, integration, and sovereign-member policy
attestations, and the package-owned `independence_wave_form05_readiness_attested`
flag. Before proclamation, MIX must be unused. After proclamation, access is
limited to the exact MIX carrier and its recorded autonomous members while a
live diplomatic connection to that carrier remains.

The reviewed sprites are registered in `interface/006_independence_wave_small_assets.gfx` under the FORM-05 source block; the deleted FORM-05 parser file is historical provenance only.

Decision sprites and expected texture paths:

| Sprite | Texture |
| --- | --- |
| `GFX_decision_independence_wave_form05_charter` | `gfx/interface/decisions/006_independence_wave/mediterranean/decision_independence_wave_form05_charter.dds` |
| `GFX_decision_independence_wave_form05_delegation` | `gfx/interface/decisions/006_independence_wave/mediterranean/decision_independence_wave_form05_delegation.dds` |
| `GFX_decision_independence_wave_form05_shipping` | `gfx/interface/decisions/006_independence_wave/mediterranean/decision_independence_wave_form05_shipping.dds` |
| `GFX_decision_independence_wave_form05_defense` | `gfx/interface/decisions/006_independence_wave/mediterranean/decision_independence_wave_form05_defense.dds` |
| `GFX_decision_independence_wave_form05_customs` | `gfx/interface/decisions/006_independence_wave/mediterranean/decision_independence_wave_form05_customs.dds` |
| `GFX_decision_independence_wave_form05_capital` | `gfx/interface/decisions/006_independence_wave/mediterranean/decision_independence_wave_form05_capital.dds` |
| `GFX_decision_independence_wave_form05_proclamation` | `gfx/interface/decisions/006_independence_wave/mediterranean/decision_independence_wave_form05_proclamation.dds` |
| `GFX_idea_independence_wave_form05_provisional_charter` | `gfx/interface/ideas/006_independence_wave/mediterranean/idea_independence_wave_form05_provisional_charter.dds` |
| `GFX_idea_independence_wave_form05_ratified_union` | `gfx/interface/ideas/006_independence_wave/mediterranean/idea_independence_wave_form05_ratified_union.dds` |
| `GFX_idea_independence_wave_form05_charter_breakdown` | `gfx/interface/ideas/006_independence_wave/mediterranean/idea_independence_wave_form05_charter_breakdown.dds` |
| `GFX_independence_wave_formable_form_05` | `gfx/interface/006_independence_wave/emblems/independence_wave_formable_form_05.dds` |
| `GFX_report_event_independence_wave_form05_charter_congress` | `gfx/event_pictures/006_independence_wave/mediterranean/report_event_independence_wave_form05_charter_congress.dds` |

Flag textures cover the base, democratic, communist, fascist, and neutral
filenames for each of `ARX`, `ASX`, and `MIX` in these folders:

- `gfx/flags/` at 82 by 52 pixels
- `gfx/flags/medium/` at 41 by 26 pixels
- `gfx/flags/small/` at 10 by 7 pixels

All 45 flag files are TGA files using the exact identity names above. The
ARX, ASX, and MIX families each use one civic design across all five ideology
filenames, so ideology changes cannot silently substitute an unreviewed flag.
COR retains its complete vanilla flag family and receives no duplicate flag.
The runtime gate is derived from the audited package registry and cannot be
enabled by a global flag or console-set asset marker.

## Future plans and suggestions

- Add a post-formation accession vote for later compatible island packages.
- Add an explicit sovereign withdrawal process with a notice period and shared
  shipping-liability settlement.
- Connect member naval exercises and customs disputes to broader Event 006
  league diplomacy after the current automatic-pool tranche is fully audited.
- Add a maritime-crisis congress that can temporarily shift the rotating seat
  without changing any country's capital.
