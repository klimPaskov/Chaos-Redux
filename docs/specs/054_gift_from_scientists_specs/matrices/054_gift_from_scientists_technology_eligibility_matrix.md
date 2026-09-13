# Event 54 Technology Eligibility Matrix

This matrix is a design and review contract. The implementation inventory must be generated from the current installed technology graph and current Chaos Redux owners.

## Candidate class matrix

| Candidate class | Baseline | Evolution I | Evolution II | Evolution III | Default profile | Main review question |
| --- | --- | --- | --- | --- | --- | --- |
| Conventional industry technology | Eligible when safe | Eligible when safe | Eligible when safe | Eligible when safe | Direct jump or prerequisites required | Does the node conflict with the recipient's industry branch? |
| Conventional electronics and engineering | Eligible when safe | Eligible when safe | Eligible when safe | Eligible when safe | Direct jump | Does the node rely on a hidden project or DLC replacement? |
| Conventional infantry and support technology | Eligible when safe | Eligible when safe | Eligible when safe | Eligible when safe | Direct jump | Does direct grant unlock a self-contained equipment or modifier? |
| Conventional artillery and armor technology | Eligible when safe | Eligible when safe | Eligible when safe | Eligible when safe | Direct jump | Are equipment lines and module unlocks valid without earlier nodes? |
| Conventional air technology | Eligible when safe | Eligible when safe | Eligible when safe | Eligible when safe | Direct jump or prerequisites required | Does the node depend on a DLC designer or exclusive airframe branch? |
| Conventional naval technology | Eligible when safe | Eligible when safe | Eligible when safe | Eligible when safe | Direct jump or prerequisites required | Are module, hull, and branch dependencies safe? |
| Conventional rocketry and nuclear research | Eligible when safe | Eligible when safe | Eligible when safe | Eligible when safe | Direct jump or prerequisites required | Does the node grant normal research only, without completing a special project? |
| Land doctrine | Excluded | Excluded | Excluded | Excluded | Excluded | Event 27 owns sudden doctrine progress |
| Naval doctrine | Excluded | Excluded | Excluded | Excluded | Excluded | Event 27 owns sudden doctrine progress |
| Air doctrine | Excluded | Excluded | Excluded | Excluded | Excluded | Event 27 owns sudden doctrine progress |
| Chaos Warfare doctrine or mastery | Excluded | Excluded | Excluded | Excluded | Excluded | Direct grant would bypass institutional and payload rules |
| Special project progress or reward marker | Excluded | Excluded | Eligible only when the owner registers a separate final technology | Eligible only when the owner registers a separate final technology | Excluded | Would the grant simulate project completion? |
| Hidden setup, test, compatibility, or deprecated technology | Excluded | Excluded | Excluded | Excluded | Excluded | Is the node player-meaningful technology? |
| Country-exclusive technology | Excluded | Excluded | Eligible only through explicit owner registration | Eligible only through explicit owner registration | Owner callback required | Can the node function outside its country package? |
| Event 16 registered technology | Excluded | Excluded | Eligible when registered and safe | Eligible when registered and safe | Owner-defined | Does Event 16 remain unfired and fully available? |
| Event 25 registered technology | Excluded | Excluded | Eligible when registered and safe | Eligible when registered and safe | Owner-defined | Does the expedition and wreck reward remain untouched? |
| CBRN registered technology | Excluded | Excluded | Eligible when registered and safe | Eligible when registered and safe | Owner-defined | Does the grant avoid free payloads, facilities, readiness, and doctrine? |
| Future event-owned registered technology | Excluded | Excluded | Eligible when registered and safe | Eligible when registered and safe | Owner-defined | Is every owner lifecycle boundary explicit? |

## Recipient state matrix

| Recipient state | Expected result |
| --- | --- |
| Existing independent human country with ordinary research | Included |
| Existing independent AI country with ordinary research | Included |
| Subject with ordinary research | Included |
| Capitulated country that still researches | Included |
| Government in exile with ordinary research | Included |
| Completed civil-war country creation | Included |
| Special Chaos country with ordinary research | Included unless owner opts out |
| Actual nonhuman country with ordinary research | Included unless owner opts out |
| Reserved, observer, dummy, or system tag | Excluded |
| Country inside protected creation or replacement transaction | Excluded for current firing |
| Dead or invalid country scope | Excluded |
| Country with no safe missing candidates | Included as a recipient with zero grants, then reported only if human |

## Branch safety matrix

| Branch condition | Candidate treatment |
| --- | --- |
| Recipient has concentrated industry | Dispersed branch candidates are removed |
| Recipient has dispersed industry | Concentrated branch candidates are removed |
| Recipient has flexible production | Streamlined branch candidates are removed |
| Recipient has streamlined production | Flexible branch candidates are removed |
| Recipient has neither branch and one side is granted | Opposing side is removed before next draw |
| Candidate belongs to a newly discovered exclusive family | Add explicit family before eligibility is approved |
| Registered candidate declares owner incompatibility group | Apply the same immediate recheck after grant |
| Grant package supplies a branch node | Treat package node as researched before next draw |

## Safety profile matrix

| Profile | Missing prerequisites allowed | Extra grant state allowed | Owner callback | Typical use |
| --- | --- | --- | --- | --- |
| Direct jump | Yes | No | No | Self-contained conventional technology |
| Prerequisites required | No | No | No | Node whose safe operation needs an intact chain |
| Grant package | As owner defines | Only the minimum declared package | Optional | Technology with bounded required setup |
| Owner callback required | As owner defines | Narrow compatibility state only | Yes | Registered custom technology |
| Excluded | No grant | None | None | Unsafe, hidden, project-only, doctrine, or lifecycle marker |

## Owner registration review

Every registered candidate must pass all rows below.

| Review item | Pass condition |
| --- | --- |
| Stable identity | One candidate maps to one live technology token |
| Player meaning | The technology has a real player-facing effect |
| Owner | One event or system is responsible for safety |
| Recipient rule | The owner can determine safe recipients without global guesses |
| Exclusivity | Every incompatible family is named |
| Prerequisites | The direct-jump, required, or package rule is explicit |
| Lifecycle | The owner event, project, and reward remain unchanged |
| Callback | Any callback is narrow, idempotent, and recipient-only |
| DLC | Missing DLC removes the candidate safely |
| AI | An AI recipient can use or safely ignore the technology |
| Report name | The recipient report can show the real localized technology name |
| Duplicate protection | Aliases and package nodes cannot appear again in the same firing |
| Normal owner route | A later normal owner firing has a defined duplicate-reward response |
| Testing | Baseline, direct grant, later owner firing, save and reload, and cluster co-occurrence are covered |

## Initial owner decisions

The following decisions must be made during implementation after inspecting the actual owner packages.

| Owner | Required decision |
| --- | --- |
| Event 16 Brilliant Scientist | Identify individual Kruger technologies that work without Kruger or the laboratory |
| Event 25 Alien Technology in Antarctica | Identify rewards that work without the expedition, wreck, or race state |
| Chemical warfare system | Separate ordinary research nodes from program, payload, facility, and doctrine state |
| Biological warfare system | Separate ordinary research nodes from outbreak, payload, facility, and protection state |
| Unusual weapon owners | Decide whether possession alone is safe or whether the technology must stay route-exclusive |
| Future technology owners | Add an explicit Event 54 registration decision to the owner specification |

## Inventory maintenance

The final implementation inventory should record candidate state by technology token and graph revision. A change to a technology's prerequisites, exclusivity, effects, DLC conditions, owner, or hidden role invalidates its prior approval until the relevant review is rerun.

The inventory must not classify a technology from its display name alone. It should follow the actual graph node and owner references.
