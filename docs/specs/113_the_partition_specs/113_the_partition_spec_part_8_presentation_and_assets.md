# 113 The Partition: Presentation and assets

The presentation should make a complicated territorial agreement readable at a glance.
The player needs to know whose country is threatened, which states are in dispute, what each neighbor wants, and how long the current offer remains open.
The tone is diplomatic menace, with restrained irony directed at the claimants' paperwork and incompatible promises.
Civilian suffering and a threatened country's existence are treated seriously.

## The event-owned dossier

One dedicated window, working identifier `chaosx_partition_dossier`, is justified by the competing state allocations and multiple concurrent targets.
Its proposed owners are `interface/113_the_partition.gui` and `common/scripted_guis/113_the_partition_gui.txt`.
The event's decision category opens it through one dossier entry point.
These identifiers are proposed event-owned names, not verified current registrations.

The accepted root is one independent window in the current player's country context, centered within the verified usable game area.
It has an explicit visible close control and opens only through the dossier entry or an explicit event-owned navigation action.
Closing preserves only the selected crisis and state as navigation preferences.
Reopening revalidates that selection and falls back to the first still-relevant registered crisis if the previous record has retired.
Opening, closing, scrolling, and changing the selected row never sign an agreement or spend a resource.
The implementation chooses the supported native parent attachment and dirty-refresh mechanism from the exact installed precedent before writing the root binding.

The dossier presents Event 113's own data and actions.
The shared event log, event-details framework, settings, and super-event window keep their existing owners.
Their integration is limited to the new event's data, artwork, and links.

### Information hierarchy

| Region | Main content | Interaction and purpose |
| --- | --- | --- |
| Header | Selected target, current role, phase, absolute deadline | Switch the selected active crisis without changing any commitment |
| Target rail | This wave's targets and older observed wars, with short phase or result labels | Select a target, recognize which crises still need attention |
| Proposal area | State list, current owner, proposed recipient, disputed and awarded states | Select a state, inspect its concrete value, and focus it on the native map |
| Selected-state or agreement detail | Relevant retained-population and retained-industry changes, strategic access warning, exact treaty promises | Compare the material effect of the selected offer and review all terms |
| Cohesion strip | One custom measure, its band, and its most important current cause | Explain what kind of negotiation can change coalition behavior |
| Action footer | Current role's valid primary choices and exact costs | Perform at most six primary actions with immediate current-state checks |

The default summary shows Coalition Cohesion and at most two supporting factual values.
The default supporting values are population retained and physical industry retained.
If a critical access issue matters more, a clear qualitative warning replaces the least useful number.
Ports, resources, supply hubs, and individual state statistics appear in selected-state detail rather than a permanent row of telemetry.

### Native controls and the campaign map

Country and state rows use native interactive elements and actual campaign identities.
Selecting a state can focus the camera and highlight only the current registered proposal states.
The native map remains the geographic authority.
Decorative artwork never contains the actionable award state, selected recipient, signature, button, or deadline.

The recipient selector offers only claimants with a feasible current interest and allowed share.
A disputed state shows both interested countries and the proposed recipient distinctly.
Awarded states show the actual current owner and award date.
An invalid state remains visible as invalid until the proposal is consciously revised, so it does not silently disappear from the player's understanding.

Territorial ratification, changed material commitments, and enforcement first open an in-window complete review of one exact version.
That review gives the full state and treaty changes first, then costs and the relevant irreversible consequence.
Its final approval opens one native confirmation popup bound to the reviewed immutable action identity.
The popup identifies the target, action, version, aggregate sacrifice, and completed review, with cancel as the first safe choice at the native 13-day timeout.
An extinction confirmation explicitly identifies the loss of every owned state and the verified native player result.
The original crisis deadline continues while a confirmation is open.
Any stale actor, version, eligibility, recipient, quote, or material state fact cancels the pending approval before debit.
Changing the target rail cancels an unfinished review and requires deliberate review of the newly selected crisis.
An old confirmation cannot authorize a newly selected crisis or revised state list.
Each actor may have only one outstanding affirmative native confirmation across all Partition crises.
Starting another consequential confirmation is unavailable without cost until the first is cancelled, expires, becomes invalid or is consumed.
That release never extends either crisis's deadline.

### Proposed layout budget

The reference composition should be created before implementation and adapted to the actual inspected native GUI precedent.
A wide composition around 1,120 by 670 logical pixels uses a narrow target rail, a broad proposal area, and one detail column.
A compact composition around 900 by 530 logical pixels uses the same hierarchy with detail replacing part of the proposal area when selected.
The compact mode preserves readable labels and scrolls the list rather than shrinking every control.
Its selected-state detail is a replacement pane with a visible return-to-list control, while the target rail and action footer remain available.
It never retains a compressed permanent third data column.
The initial layout rule selects compact mode at 1280×720 and at 1366×768 with 125% scaling, subject to confirmation of the actual native scale behavior.

These are design budgets, not claims of verified runtime geometry.
The UI worker must establish the supported screen and scale behavior from actual inspection and rendered references.
Required review scenarios include 1280×720 at 100%, 1366×768 at 100% and 125%, 1920×1080 at 100% and 125%, and 2560×1440 at 100% and 150% where those configurations are supported.
Any unsupported combination is recorded with the actual engine limit and a concrete supported adaptation.

The action footer uses at most two rows of three controls.
It leaves room for a concise label, cost icons, and a selected or disabled state.
No label is compressed into unreadable text to preserve a decorative margin.
Scrolling bounds, selected rows, tooltips, clipping, and click regions are verified in the production renderer.

## Phase and action map

| Viewer and phase | Primary gameplay groups | Native missions visible to that viewer |
| --- | --- | --- |
| Target during negotiation | Counterproposal, protection request, defense preparation, supply preparation, ratification, refusal | Own ultimatum, at most one incoming request from another target, at most one Partition Task |
| Claimant during negotiation | Ratify, revise, invite, withdraw, contest rival when the 30-day dispute gate is met | Incoming protection request only if a different legal role permits it, plus one Partition Task |
| Claimant after rejected or expired ultimatum | Ratify a renewed offer, revise, invite when its review window remains legal, withdraw, authorize enforcement, contest rival | Relevant commitments shown as status rows, plus the bounded request and Task slots |
| Protector or mediator | Guarantee, delivery with arms or transport alternative, mediate, intervention pledge, withdraw or narrow | One incoming request and at most one Partition Task |
| Target during handover | Inspect exact agreement, inspect protection, report an invalidated term | Own handover mission, with the same maximum of two other allowed slots |
| Target after resolution | Reconstruction when applicable, reconciliation, inspect recorded result | Own reconstruction mission if active, with bounded request and Task slots |
| Observer | Inspect target, inspect proposal, offer an eligible existing protector or mediator action | Only an actually accepted role's mission or Task |

The exact gameplay button sets are T1–T6 for target negotiation, C1, C2, C3, C4 and conditionally C6 for claimant negotiation, and C1–C6 after a rejected or expired ultimatum.
Each phase-specific gate still applies, including C3's remaining review window and C6's actual 30-day material dispute.
The protector set has five buttons for P1, combined P2/P3, P4, P5, and P6.
The combined delivery button opens one mutually exclusive arms-or-transport selector and one quoted package, with no simultaneous purchase of both packages through that action.
P6 similarly selects either full withdrawal or one narrowed commitment for review.
Handover has zero new territorial purchase buttons, with inspection and a request to revalidate an allegedly invalid term treated as navigation and validation.
Aftermath has at most reconstruction activation and the player's reconciliation initiative as primary purchases.
An observer has zero gameplay buttons until it deliberately enters an available invited participant route, at which point the corresponding role's button set applies.

Inspection controls do not purchase resources or create new gameplay choices.
The shared set stays below six primary gameplay actions even when several previous outcomes remain available to read.
The dossier remembers which target the player was viewing after a notification, while immutable action identity prevents that selection from changing a pending approval.

## Required visual states

The UI must support normal, hover, selected, disabled, unaffordable, pending response, disputed, stale proposal, fully ratified, handover in progress, awarded, interrupted, defended, limited settlement, complete partition, and neutral invalidation states.
Empty and crowded views are also required.
The crowded fixture includes eight targets, six claimants on one target, long country and state names, several disputed states, a fourth cost type in detail, and an older continuing war.
Control appearance, crisis phase, state-allocation status, and terminal outcome are independent presentation dimensions.
For example, an awarded state can be selected for inspection while its award remains completed, and a neutral-invalidated crisis keeps its history while all victim-facing controls are disabled.

Color is reinforced by a distinct icon, border treatment, or short status label.
The proposed semantic palette uses muted amber for pending danger, restrained red for a contested or invalid action, pale blue for protection, and desaturated green for a confirmed completed result.
Actual colors and contrast are chosen from the matching canonical native references.
Text and selected-state recognition must remain usable without color discrimination.

The Cohesion strip shows a band marker and one immediate cause, such as an unresolved overlap or all members agreeing to the current map.
Its tooltip explains the consequence and the available response.
The full factor breakdown belongs in an optional detail view.

## Event and report map

| Report role | Audience | Information to communicate | Localisation direction |
| --- | --- | --- | --- |
| Opening wave | Actual targets and involved claimants, concise news for observers | Real target count, opening form, separate crises, no promised outcome | Formal public language with a sense of several coordinated threats |
| Claimant invitation | The invited human claimant | Proposed share, rival claims, decision deadline, participation is optional | A tempting offer with an implied price, avoiding assumed consent |
| Target ultimatum | Threatened government | Exact demand, coalition, response date, protection and refusal routes | Serious, compressed urgency with agency clearly stated |
| Counterproposal or enlarged demand | Affected signatories | Changed states, recipients, obligations, and invalidated signatures | Emphasize the concrete revision rather than repeat the opening premise |
| Protection response | Target and provider | Accepted type, due obligation, actual legal or material limitations | Distinguish a promise from completed help |
| Enforcement | Actual belligerents and affected target | Who actually entered war, how it relates to the demand, broader-war warning if needed | Direct and factual, with no predicted victory |
| Claimant break | Former partners and target | Contested share, withdrawn commitment, any actual rival war | Dry irony about an agreement that its authors could not maintain |
| Handover result | All signatories | Actual awarded states, remnant or extinction, unfulfilled terms | Specific and sober, with precise partial-result wording |
| Defense result | Target, protectors, former claimants | Actual intact survival and end of aggression | Relief with the cost of the defense acknowledged |
| Aftermath | Relevant surviving country | Repairs, remaining grievances, fulfilled protection, continuing native diplomacy | Consequence-focused rather than a second opening description |

Opening event details describe the premise, actual actors, and current form.
They do not duplicate every action's effects or every mechanical rule.
The shared event history receives one opening firing and meaningful later outcome records through its own documented interface.
Per-target outcomes retain their correct actors even after another target becomes the selected dossier row.

## Required artwork and icon families

Every row below is an accepted planning requirement for later asset production.
All basenames and sprite names are working runtime identifiers subject to the repository collision check.
The asset prompt supplies the exact final paths and owner handoff.

### Report and news art

| Asset basename | Consumer and planned size | Direction | Source mode |
| --- | --- | --- | --- |
| `report_event_113_partition_opening` | Opening and ultimatum, 210×176 | Anonymous diplomats arranging several border maps, target's vulnerability readable through composition | Generated fictional period documentary photograph, report-card treatment |
| `report_event_113_partition_protection` | Protection response, 210×176 | Diplomatic seal beside real-looking supply crates or a rail dispatch | Generated fictional period documentary photograph, no invented real-person likeness |
| `report_event_113_partition_defense` | Defense outcome, 210×176 | A surviving fortified frontier and exhausted defenders, restrained relief | Generated fictional period documentary photograph informed by period references |
| `report_event_113_partition_settlement` | Completed handover, 210×176 | Border marker and signed map, ceremony carrying a visible cost | Generated fictional period documentary photograph, report-card treatment |
| `report_event_113_partition_interrupted` | Interrupted settlement or claimant break, 210×176 | Incompatible annotated documents and a broken agreement seal | Generated fictional period documentary photograph, report-card treatment |
| `news_event_113_partition_wave` | Observer opening news, 397×153, black and white | Broad diplomatic crisis conveyed through maps and official documents | ImageGen illustration or a verified period archival alternative with a precise subject match |
| `news_event_113_partition_outcome` | Significant actual outcome news, 397×153, black and white | Changed border posts and a concluded agreement, neutral to which countries were involved | ImageGen illustration or verified period archival alternative |
| `super_event_113_partition_reckoning` | Rare Grand Partitions outcome, 457×328 | A large negotiating table with several emptied places and a divided map, emphasizing the disappeared states | ImageGen illustration for the actual alternate-history result |

The imagery must remain geographically adaptable.
All five report images use the current 210×176 black-and-white with sepia report-card processor and period documentary framing.
A picture of a specific historical conference cannot be presented as a photograph of an arbitrary later campaign agreement.
If archival material is selected, its real subject, author, date, source, rights, and limits must be documented.
The 1919 historical partition map and the 1938–1939 diplomatic documents in the research note are conceptual references, not automatic runtime art licenses or exact campaign maps.

### Decision icons

Each listed asset is a separate 32×32 native decision icon with genuine transparency and a readable silhouette.
Reusing an icon for the same action concept is intentional.
It is not a cross-size substitute for a mission or spirit asset.

| Basename suffix after `decision_113_partition_` | Consumers | Motif |
| --- | --- | --- |
| `counteroffer` | T1 and C2 | A marked border document and a single revision stroke |
| `protection` | T2 and P1 | A diplomatic shield with a seal |
| `entrench` | T3 | Compact field entrenchment tools |
| `transport` | T4 and P3 | Rail and supply movement |
| `ratify` | T5 and C1 | Two aligned document seals |
| `refuse` | T6 | A document decisively set aside |
| `withdraw` | C4 and P6 | A removed claimant marker |
| `invite` | C3 | An additional diplomatic seal beside a map |
| `enforce` | C5 | A military order beside a frontier line |
| `dispute` | C6 | Two opposed claimant markers |
| `arms` | P2 | Compact arms and equipment crates |
| `mediate` | P4 | A balanced pair of documents |
| `intervene` | P5 | A protective military commitment |
| `rebuild` | Reconstruction | Repair tools over a retained border |
| `reconcile` | Bilateral reconciliation | Two former opposing seals aligned |

The event category receives one separate category icon, working basename `decision_category_113_partition`, with a divided-map and diplomatic-seal motif.
Its canvas and frame states must come from the exact inspected native category consumer.
The dedicated dossier supplies the category's complex presentation.

### Missions and spirits

Four distinct mission icon requirements cover ultimatum, protection request, handover, and reconstruction.
Their working basenames are `mission_113_partition_ultimatum`, `mission_113_partition_protection`, `mission_113_partition_handover`, and `mission_113_partition_reconstruction`.
Their native canvases and frame treatment are taken from the exact mission references and consumer.
They use deadline, diplomatic reply, awarded-state, and repair motifs respectively.

Three 64×64 spirit icons cover emergency entrenchment, supply preparation, and reconstruction.
Their basenames are `idea_113_partition_entrenchment`, `idea_113_partition_supply`, and `idea_113_partition_reconstruction`.
Each spirit shows its own finite effect and lifetime.
It does not become a generic stacking container for unrelated rewards.

The six achievement designs in Part 10 each require their exact completed, grey, and not-eligible 64×64 image states.
Achievement state composition and root lookup placement follow the current achievement owner and asset skill.

## Localisation direction and humor

The full text handoff covers event titles and descriptions, options, decision and mission text, the dossier, state and recipient labels, blocked reasons, cost explanations, achievements, event details, and catalog summaries.
This specification supplies meaning, tone, context, and length intent.
It supplies no pasteable final localisation lines.

Humor belongs primarily to claimant correspondence, futile paperwork, and the contrast between public ceremony and incompatible private demands.
A target refusal can be defiant without promising victory.
A partial settlement report must not use triumphal wording that conceals what the target lost.
Country names, flags, state names, and current political identities come from the actual actors.

## Rare super-event research direction

The established trigger is the actual multi-country Grand Partitions outcome in Part 6.
Its title direction concerns a failed border order, its description concerns the proven scale of the division, and its main quote should reflect the consequences of treating sovereignty as negotiable.
The cultural remark should be brief, researched, and directed at the authors of the arrangement.
The text researcher must verify wording, attribution, context, and copyright before any final text is selected.

The audio direction is a restrained ceremonial opening that becomes fractured and unresolved, around 90 seconds within the current one-to-two-minute standard.
The audio researcher must find and document a suitable lawful recording, composition, or accepted sourced production route.
No tune, performer, recording, quote, or lyric is preselected in this plan.
The final cue needs a legitimate source, creator, rights, download and conversion evidence, correct WAV format, and settings-aware playback through the shared sound owner.

The production package is complete only when image, final verified text, quote, remark, sound, trigger, slot, documentation, and catalog alignment agree.
Crossing an evolution threshold or displaying a placeholder must never be reported as completion of this outcome presentation.

## Presentation evidence required later

The current canonical graphic-reference directories and their labeled native-size contact sheets must be inspected before production.
The UI worker creates or selects a concrete reference composition and maps it to native elements before implementation.
Icons use the exact matching asset family, generated raster source, preserved alpha, the standard DDS converter, and native-size round-trip review.
Report art uses the repository report-image processor.

Mandatory `hoi4.gui_inspect` and `hoi4.gui_render` evidence covers the exact event-owned identifiers before and after implementation.
The rendered states, resolutions, hierarchy, clipping, and click regions are compared under matched scenarios.
Source review and an attractive mockup do not replace that evidence.
The present package contains the full design and production requirements, with actual raster production and engine rendering remaining implementation work.

