# Disease State Matrix

| State status | Entry conditions | Population effect | Spread role | Available response | Exit conditions | Mapmode |
| --- | --- | --- | --- | --- | --- | --- |
| Clear | no active infection or exposure | none | can receive exposure | prevention only | Threatened after route exposure | neutral |
| Threatened | exposure pressure above warning threshold | none | does not emit ordinary spread | inspections, border control, hospital staging, movement limits | Clear after exposure decays, Incubating after protection fails | amber-brown |
| Incubating | infection established below public threshold | very low initial deaths | weak hidden spread | early quarantine and treatment when detected | Infected after recognition, Contained after exceptional early suppression | dark charcoal to authorized owner |
| Infected | recognized active disease | low to rising deaths | normal outgoing spread | quarantine, hospitals, relief, treatment, cordon, Black Plague rat-control decisions | Severe Crisis, Contained, or Collapsed | black base with infected outline |
| Severe Crisis | high disease load and mortality pressure | high and accelerating deaths | strong outgoing spread | harsh containment, major relief, army cordon, urban rat clearing, evacuation perimeter | Contained after major suppression, Collapsed after capacity failure | black base with severe outline or pattern |
| Collapsed | containment and administration fail | extreme deaths | maximum natural spread | emergency military, destructive rat clearing, and foreign intervention | Severe Crisis or Contained after restored control, Rat-Controlled after emergence or occupation | black base with broken crisis edge |
| Contained | effective spread below threshold | reduced but continuing deaths | little outgoing spread | maintain cordon, trace clusters, rat cleanup, controlled reopening | Recovery after sustained low load, relapse to Infected | black base with blue containment outline |
| Recovery | load declining after containment | low residual deaths | minimal spread | cleanup, rat infestation reduction, rebuilding, monitoring | Cured at zero load and no exposure, relapse when pressure returns | black base with green recovery outline |
| Cured and monitored | cleanup complete | no active disease deaths | protected from weak exposure | optional prevention and rebuilding | Clear after monitoring memory, Incubating after major new exposure | pale green-grey |
| Rat-Controlled | rat country owns or controls active plague state | high to terminal human deaths | reliable infection source and brood growth | human actions unavailable until liberation | remains until liberated, then returns to current disease phase | black base with rat-control accent |

## Disease value interactions

| Value | Low | Medium | High | Extreme |
| --- | --- | --- | --- | --- |
| Disease Load | hidden or local cases | recognized outbreak | severe state-wide infection | collapsed or rat-amplified state |
| Mortality Pressure | isolated deaths | growing weekly loss | mass death | demographic destruction |
| Spread Pressure | local household route | adjacent and transport threat | multi-route regional emission | overseas or rat occupation emission |
| Containment | no organized response | partial measures | sustained effective cordon | overcapacity response with high national burden |
| Treatment Coverage | little access | field treatment | hospitals and mature protocol | near-universal access in reachable population |
| Relapse Risk | stable cleanup | manageable residual clusters | rushed reopening or active exposure | fresh weapon or rat exposure |
| Rat Infestation | isolated evidence | established warehouses and shelters | city-wide infestation and transport spread | organized nests, rat occupation, or emergence basin |

## Mapmode rule

When Black Plague is selected, every established Black Plague state uses a black base fill. Phase, containment, weaponized provenance, and rat control are carried by outlines, patterns, icons, and tooltips. Threatened states keep the shared warning colour until infection is established. Cured states leave the black fill after cleanup.

## Provenance layer

Provenance does not create a separate disease instance.

| Provenance | Meaning | Extra consequence |
| --- | --- | --- |
| Natural outbreak | initial event or ordinary spread | no condemnation |
| Accidental release | lab or stockpile failure | investigation, possible condemnation, facility damage |
| Weaponized deployment | deliberate biological strike | high condemnation, retaliation, attribution system |
| Rat occupation | disease established by rat control | brood growth, rat immunity, human death acceleration |
| Relapse | residual local load returns | lower trust, higher emergency burden, adaptation need |
