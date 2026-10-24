# Mistresses: interfaces, information, and the screening experience

## A face, a reason for concern, and a decision

The screening window should let the player understand one person's situation without losing the wider condition of the response.
The selected portrait is the visual centre.
A short description establishes the person's household, work, and relevant relationships.
Evidence then explains why the country is considering action, how that information was obtained, and which questions remain unresolved.
The three principal choices are investigate, spare, and purge.

The window needs a real case browser because the player repeatedly selects people, compares saved evidence, tracks an investigation, and returns to previous decisions.
An ordinary list of decisions or a decorative category picture cannot make those tasks clear.
Use a dedicated event-owned native scripted GUI with a compact ordinary decision-category entry.
The response category is ineligible for an additional static or animated category picture because its attached values and custom interaction already perform that role.

All new interface terms and component names in this chapter are working design labels, not final localisation.
The final writer supplies labels from the directions below.
The design must not ship planning terminology, raw identifiers, or sample text as game copy.

## The two public values

Public Confidence and Investigative Reach are the only persistent event-owned public numbers across the screening window, decisions, focus tooltips, event popups, and shared information surfaces.
Both range from zero to 100.
A newly affected host starts at Confidence 65 and Reach 10, with any exceptional starting state explained by the owning core chapter.

| Public value | What it communicates | Meaningful launch states | Useful response |
| --- | --- | --- | --- |
| Public Confidence | Willingness to cooperate with the country's response | Below 25, witness withdrawal makes reliable collection harder. At 50, ordinary cooperation is dependable. At 75, protection and restitution institutions have a strong public basis | Protect people, correct proven wrongs, avoid unjustified coercion, and fulfil visible commitments |
| Investigative Reach | Staffed, connected capacity to pursue cases and operate services | At 25, a second investigation slot opens. At 50, a third slot and a larger active caseload open. At 75, coordination supports advanced institutional routes | Complete service circuits, preserve access, establish independent connections, and use the relevant focus route |

Each meter has a stable icon, a distinct colour family, readable numerical text, and a non-colour threshold marker.
Confidence uses a human cooperation motif, while Reach uses a connected field-service motif.
Neither icon implies that the country knows the true infiltration level.
Tooltips name the largest recent visible causes of change and the immediate consequence of the current band.
They do not expose hidden component weights.

The selected case can also show a date, a finite investigation deadline, an evidence count, and a finite objective checklist.
Existing engine resources can appear in a price.
Those facts do not become additional national progress meters.
There is no guilt percentage, corruption percentage, network-strength gauge, alien population percentage, capture-readiness bar, or Mother-readiness gauge.
Changing tab or opening a tooltip must not evade this information budget.

## Layout and navigation

Use a dark, restrained HOI4 window with clear native typography, a calm photograph area, and readable evidence grouping.
The design should avoid piles of decorative paper, stamped warnings, secrecy motifs, and bureaucratic theatre.
The person's ordinary life and the observed anomalies provide the atmosphere.
Portrait frames remain neutral before and after investigation so colour treatment cannot reveal truth.

The initial layout target is a 1,120 by 700 logical-pixel window at 1920 by 1080 and UI scale one.
A compact target around 1,020 by 620 supports 1366 by 768 at scale one.
These are composition targets for native reference mapping, not an unverified claim about engine scaling.
At 2560 by 1440, review scale one and scale 1.25 where that setting is supported by the inspected consumer.
Text must remain readable without shrinking a failed layout to fit.

| Region | Content | Interaction and limits |
| --- | --- | --- |
| Header | Current host, Public Confidence, Investigative Reach, close control | Value tooltips and close navigation. No hidden-world telemetry |
| Case browser | Ten rows per desktop page or five in compact presentation, each with identity, place, dated public status, and unread-result marker | Select a case, move between pages, and apply simple public filters |
| Selected person | A 156 by 210 portrait consumer or a documented native adaptation, fictional alias, adult life description, relevant household or role | Portrait enlargement for inspection if supported, without changing the underlying image |
| Evidence area | Short observations grouped by source and date, with explicit dependence and integrity concerns | Read details, follow a known source relationship, and inspect the method that produced an item |
| Action area | Investigate, spare, and purge with current prices and requirement states | Three principal gameplay actions. A method-selection substate replaces this area when needed |
| Context strip | Current case investigation or the most relevant operational mission link | One immediate objective and access to the ordinary mission category |

The desktop and compact layouts preserve the same hierarchy.
The compact version uses native scrolling for evidence and fewer visible case rows.
It does not hide a cost, turn purge into an unlabeled icon, or remove the provenance explanation.
The selected portrait remains recognisable at its actual rendered size.
Source photographs retain their intended crop and aspect rather than being stretched to fill a panel.

Default ordering uses public urgency, then oldest unresolved admission, with stable case identity as the tie-break.
Filters may use location, active or closed status, unused methods, unread results, and publicly established source concerns.
They cannot filter for actual aliens, real coordinators, hidden compromised investigations, or unrevealed replacement candidates.
A sort by the actor's private computed guilt estimate is also excluded.

Changing pages has no gameplay effect.
The page reads only its bounded visible rows and the selected record, rather than rebuilding all 1,250 images.
Closing or reopening the window retains the selected case if that record still exists.
If it has closed or transferred, show its new status in place and offer deliberate navigation to the next case.
Do not move another portrait under an existing action button during a click sequence.

## A large pool without a large screen

The case browser supports the complete portrait pool and a long campaign archive without loading a thousand simultaneous controls.
Native dynamic lists, a stable page cursor, and bounded row projections present the active subset.
The portrait assignment and long-campaign reuse rules are specified in `119_mistresses_spec_part_3_screening.md`.
The pool contains at least 1,000 distinct adult identities, with a target of 1,250 and at least 80 percent rights-cleared internet photographs.
The asset chapter owns sourcing and final acceptance.

Each row binds to a permanent case identity, not a mutable list index.
Removing a row cannot transfer its costs, selected state, result marker, or action target to the next row.
If evidence arrives for a case on another page, increment its unread marker and the ordinary notification state without selecting it automatically.
Sorting can change after the player deliberately changes the sort or selects a new case.
A selected card remains anchored while its information updates.

The archive preserves the date, image assignment, evidence visible at the time, actions taken, actual paid costs, later findings, and unresolved uncertainty.
It distinguishes a decision from an established outcome.
A spared case is not labelled human merely because the government released it.
A purged case is not labelled alien merely because the government ordered removal.
The archive shows a later proven wrongful death or verified infiltrator only when the acting country acquired that evidence.
It never replaces an old record with the truth of a newer fictional person who later reuses the photograph.
If new conduct reopens an old case whose image is reserved by another active person, its archive remains readable while the actionable portrait card waits for the reservation.
Show the administrative waiting state without implying guilt or changing either identity.
Urgent protection and source work remain reachable through their named operational targets, while individual action controls remain unavailable until admission.
No wait begins a charge, investigation timer, or new evidence roll.

## Evidence and action states

An evidence card normally contains one to three short lines, with a two to four-line tooltip for provenance and uncertainty.
Use a repeated source-group icon and a concise relationship explanation when several reports share an origin.
When independence is unproven, the presentation must preserve that uncertainty.
An audit result can alter the known relationship between items without rewriting what the earlier report said.

The method picker shows the available question, price, duration band, and source family.
It distinguishes an unused method from one already exhausted and distinguishes an independent packet from another view of the same packet.
Opening the picker cannot select a method, spend resources, or generate a result.
At most three relevant method choices appear simultaneously.
The ordinary principal actions return after the player chooses or cancels a method.

| State | What the player sees | Required interaction behaviour |
| --- | --- | --- |
| First admission | One ordinary adult identity, its referral context, incomplete evidence, and the two country values | No alien label or future-evolution preview on the case card |
| Investigation available | An unused question, a coherent price, a free staff slot, and current access | The same quote and requirements govern selection and payment |
| Investigation active | The chosen method, paid receipt summary, due date, and collection status | Repeated clicks cannot start another copy or redraw evidence |
| Funds or equipment unavailable | The normal control in a visibly disabled state, with the deficient resource identified | No debit, no reservation, no cooldown, and no invisible active hitbox |
| Staff capacity unavailable | Current occupied slots and the case's valid alternatives | A reasoned disabled investigation control, while spare remains usable |
| Coercive handling occupied | The existing five-day handling reservation and its return date | Disable a further purge without charging or starting a cooldown, while investigation and nonlethal work retain their normal availability |
| Source integrity concern | The affected report and its relationship to other evidence | Offer the appropriate audit or replacement path without displaying hidden truth |
| Method exhausted | The recorded result and method history | No repeat roll disguised as refreshing or another laboratory label |
| Purge confirmation | The exact person, current authority, complete price, and irreversible consequence | Harmless cancellation first, with click-time revalidation and a separate active confirmation target |
| Authority lost or target gone | The case's actual changed status and any resulting cancellation | Preserve the old record, disable stale action, and resolve reservations through the transaction owner |
| Empty active list | A concise explanation of the current caseload and access to operational work or archive | No fabricated candidate or free reward |
| Crowded list | Stable rows, complete prices, and usable pagination | No clipping, overlapping hitboxes, or truth-based prioritisation |
| Unveiling transaction in progress | The last coherent case projection with temporary action unavailability | Publish the resulting state once the ordered transaction completes |
| Aftermath | Surviving unresolved cases, restitution obligations, and archived findings | Retire obsolete coercive actions and retain the records needed for recovery |

An unavailable button needs a genuinely disabled appearance as well as a disabled click predicate.
If the native consumer cannot express that reliably on one control, use a verified mutually exclusive active and locked composition with the same painted bounds.
Hidden panels cannot intercept clicks.
Decorative overlays must be click-through where the native element supports that behaviour.
The implementation must compare the painted control face, text bounds, and effective hit region in its actual parent window.

## Current information while paused

The screening window stays current while the game is paused.
Costs, affordability, authority, case status, deadlines, source relationships, and the two public values update from live read-only getters or a synchronously published projection after the responsible transaction.
There is no manual refresh button and no requirement to unpause before a changed resource reserve becomes visible.

Presentation refresh cannot perform investigation, advance a network operation, assign new truth, reroll a source packet, admit another person, or scan the whole world.
It reads the published case set and current bounded selection.
A multi-step mutation publishes its coherent result after completion so the player never sees a half-charged action alongside a supposedly available slot.
External changes such as state capture, coalition changes, a paid decision, or an inherited host authority must invalidate the affected projection through their existing lifecycle hooks.

A stale purge confirmation remains safely cancellable.
An old positive reply cannot acquire authority over a replacement case or a different country incarnation.
The confirmation's immutable identity survives selection changes until the prompt closes.
The transaction chapter owns those receipts and their cleanup.

## Information arrives through evidence

The ordinary crisis begins with observations about relationships, recruitment, discipline, introductions, and obstructed inquiry.
No country begins with verified knowledge of the alien identity.
An institution can recognise that a report is unreliable without knowing who manipulated it.
A country can know that a person has unusual access without knowing whether she is an infiltrator.
The evidence UI must preserve these distinctions.

When a country obtains decisive public proof, it may name the confirmed alien fact in the relevant case and local report.
Other countries receive only what is actually shared or publicly observable.
The Unveiling makes overt revolts, transformed hostile forces, and their territory visible through the normal world state.
It does not retroactively reveal every unresolved prewar case or print the full hidden population ledger.
Mother's public strategic objectives follow `119_mistresses_spec_part_8_mother_aftermath.md` without exposing the sustained-success calculation that selected her emergence.
Her actual relay set appears as at most five named or regionally identified objectives, with the required disabled count derived from that saved set.
Each identified site shows its current public control or operation status and any known temporary disablement expiry.
Relay operation previews show the preparation and access conditions the actor actually knows, with qualified risk where an enemy response remains unobserved.
They cannot expose an unseen counter-operation through an exact probability or a special unavailable state.
The final action preview shows 50 Command Power, the capacity-scaled support-equipment amount, the 30-day emergency duration, and the continuing lair and relay requirements.
These are finite campaign objectives and an actual price, not another permanent command-strength meter.

No true state may leak through portrait tint, file naming visible to the player, tooltip length, missing-cost branches, availability differences, source-only metadata, filter membership, default sorting, animation, notification frequency, or a faster UI refresh.
A source being compromised can change observable evidence according to the saved model.
It cannot silently add a special visual mark that exposes the private integrity flag.
Shared Deaths and actual population accounting remain truthful after a lethal action.
Their post-action changes may permit inference, but the screening preview cannot disclose whether its unresolved target would debit the human or alien ledger.

## Shared information surfaces

The event-owned window supplies its data to the shared event system without taking ownership of that framework.
The parent implementation agent retains Event Logs, Event Details, Settings, the super-event framework, and shared registries.
The UI worker owns only the bounded Mistresses window and its event-owned presentation bindings.

| Surface | Information and writing direction | Boundary |
| --- | --- | --- |
| Ordinary event popup | Household and military observations from the affected country's viewpoint, with incomplete explanations | Do not reveal the hidden species or mechanically list every modifier |
| Case description | A short fictional adult life context, current household or work connection, and the publicly known reason for attention | No protected-trait inference and no borrowed real-person allegation |
| Evidence text | Concrete observation, date, source relationship, collection limits, and changed understanding | Preserve the distinction between report and established fact |
| Decision and mission text | What the country is doing, where it must act, what it spends, and what completion means | Describe actual requirements without raw triggers or hidden scores |
| Outcome report | Visible effects on the person, household, institution, or route, with appropriate uncertainty | Death and suffering use severity rather than cheap humour |
| Event Details and catalogue description | The current premise and the situation experienced by affected countries | No rewards, penalties, raw effects, private thresholds, or achievement route instructions |
| History and evolution views | Genuine recorded milestones with the proper actor, date, and evolution identity | Ordinary screening progress is not logged as an evolution |
| World-end public row | The approved Mother branch's premise and current public availability context | Independent persistent toggle through the shared registry, no private success formula |

Repeated case actions should not flood the global event history.
The case archive holds individual decisions.
The shared history records meaningful national or international milestones such as the first verified public discovery, a completed institutional breakthrough, The Unveiling, and the Mother campaign outcomes defined by their owning chapters.
An evolution catalogue entry is a preview, while a recorded evolution row has an actual date and actor where appropriate.
Neither can be populated with invented history metadata.

## Bounded implementation handoff

The proposed native window identifier is `mistresses_screening_window`, with the scripted-GUI owner `mistresses_screening_gui`.
The opening navigation decision is `mistresses_open_screening` in `mistresses_response`.
The event-owned layout paths are `interface/119_mistresses_screening.gui`, `interface/119_mistresses_screening.gfx`, `common/scripted_guis/119_mistresses_scripted_guis.txt`, and `localisation/english/119_mistresses_gui_l_english.yml`.
The decision owner retains costs and gameplay in `common/decisions/119_mistresses_decisions.txt` and `common/decisions/categories/119_mistresses_categories.txt`.

Before implementation, create the intended normal and compact reference compositions through the approved asset workflow and record the parent's selection within the authorised design.
Map their portrait, list, value, evidence, and action regions to native controls.
Keep labels, meters, lists, prices, and hitboxes functional rather than painting them into a background.
`119_mistresses_spec_part_11_assets_audio.md` owns portrait and panel production, while `119_mistresses_execution_map.md` owns specialist routing and future MCP evidence requirements.

The visual review must include normal and compact layouts, the method picker, active investigation, each disabled reason, confirmation, empty and full pages, first and last rows, long real labels, multiple source groups, and both minimum and maximum public values.
Review state changes while paused, an open window during a completed payment, a closed window reopened after capture, and a confirmation that becomes stale.
The matched evidence records its source revision, scenario, resolution, UI scale, selected person, costs, state flags, and effective click regions.
Unavailable rendering limits the visual claim and does not permit a claim of native game verification.

The decision owner separately verifies action integrity.
A well-aligned button cannot prove a correct debit, finite method use, AI parity, or cleanup.
The parent reviews the window and the transaction evidence together.

## Source notes

The layout, reference-before-implementation, native control, paused refresh, content budget, and visual review rules come from the fully read `.claude/skills/chaos-redux-scripted-gui/SKILL.md`.
The dedicated-window ownership boundary follows `subagents/chaosx-event-ui-worker.md` and `.claude/skills/chaos-redux-subagents/SKILL.md`, Event UI worker gate.
The category presentation choice and action integrity apply `.claude/skills/chaos-redux-decisions-missions/references/formables-and-category-presentation.md`.
Text directions apply `.claude/skills/chaos-redux-event-planning/references/player-facing-text-direction.md`.
Shared Event Details and history boundaries follow `.claude/skills/chaos-redux-events/references/event-text-formatting-and-details.md` and `references/event-log-evolutions-and-clusters.md`.
