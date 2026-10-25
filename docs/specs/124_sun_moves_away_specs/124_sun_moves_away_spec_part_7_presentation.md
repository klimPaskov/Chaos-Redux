# Event 124, Part 7: Presentation and Player Information

## 1. Player information

This specification defines Event 124 presentation as an implementation proposal under the accepted Sun Moves Away brief.
Every new title, identifier and scene label below is a working design handle pending registry, source and asset review.
The package supplies text direction, coverage and acceptance conditions without final localisation, quotations, music, artwork or executable code.
The global lifecycle and presentation gates belong to [Part 2](124_sun_moves_away_spec_part_2_evolutions_and_return.md), while action behavior and payment belong to [Part 4](124_sun_moves_away_spec_part_4_decisions_missions.md).
The presentation must preserve continuous world-map darkness and native nighttime combat behavior at every hour until Return of the Sun.
Both mechanisms remain hard implementation acceptance requirements with unresolved engine feasibility.
The panel explains their effects and cannot certify that they have been implemented.

The player needs to recognize the active crisis, its local consequences, current allocation priority, useful interventions and actual commitments.
Exactly two persistent national values appear during the crisis: Civilian Protection and Lifeline Reliability, each from 0 to 100.
Civilian Protection represents population-weighted functioning essential services, constrained locally by the weakest essential service.
Lifeline Reliability represents essential-demand-weighted delivery through critical domestic and overseas corridors.
Shared famine data supplies food-access evidence, and actual corridor delivery supplies reliability evidence.
Cold, fear, health, creatures, research, food and the Sun's return receive no additional persistent national meter.

## 2. Compact management window

The event-owned window attaches through a verified native parent and context, with its final runtime name reserved after collision checks.
A proposed content canvas of 760 by 620 pixels at 1920 by 1080 and UI scale 1 provides a starting layout for the required compositional reference.
The implementation owner must measure available parent bounds before accepting that canvas or commissioning final panel artwork.
At smaller supported resolutions, the state browser and mission area may scroll independently while the two values, selected target and primary actions remain legible.
Text sizes and hitboxes retain the inspected native interface family's usable dimensions.

The header contains the event identity, active-stage badges and the current allocation priority.
Active badges reflect the actual enabled stage set, including a higher stage whose lower stage was disabled.
The two value regions show the current number, meaningful qualitative condition and a short explanation available on hover.
Their tooltips identify population or demand weighting, the weakest failing service, recent confirmed changes and a practical response.
An unavailable denominator displays an explicit inapplicable or unverified state without a fabricated percentage.
The display never interprets a low value as proof of a particular death count or monster population.
Elapsed crisis information belongs in the episode details tooltip and supplies no predicted return date.

The left column is a state and corridor target browser with ownership, access and eligibility filters.
Each row uses qualitative protection, route and threat conditions with distinct shapes or glyphs as well as colour.
The selected target retains a visible identity, owner and access status when its eligibility changes.
An invalid selection opens its blocked explanation and offers a valid selection without silently moving an action to another target.
Exact population, delivered supplies, project requirements and recent receipts appear in target details or tooltips.

The main area contains exactly six primary action rows and at most three active missions.
Three rows serve selected-state urgent work, two serve national or network work, and one serves priority choice or review.
Each row has one executable action, its condition, up to three inline cost values and an iconed full-cost tooltip.
A row's context selector changes the displayed task within its accepted action family and never executes that task.
Filters, selectors and navigation do not create additional paid controls.
Active commitments remain visible ahead of optional new work, and duplicate work exposes its existing mission receipt.

## 3. Action-row allocation

The A numbers below are document references from Part 4, with final runtime identifiers allocated later.

| Row | Action references | Presentation contract |
| --- | --- | --- |
| S1, essential warmth and shelter | A02, A14, A15, A16 | The row selects emergency heating, refuge construction, refuge sustainment or refuge closure according to the selected site's actual lifecycle. |
| S2, civilian needs | A03, A04, A11, A18 | The row presents food distribution, rest and clinics, evacuation or a live missing-person rescue with the relevant humanitarian target and urgency. |
| S3, local safety and access | A05, A06, A09, A17 | The row presents markings and lighting, route repair, rural protection or containment using the selected state or linked corridor's confirmed need. |
| N1, national allocation | A07, A08 | The row presents fuel diversion or factory shift reorganization with the military, industrial and civilian opportunity costs together. |
| N2, network coordination | A10, A12, A13 | The row presents a protected convoy, bilateral relief shipment or observation and coordination with recipient and delivery context. |
| P1, priority and review | A01 | The row presents the current allocation commitment, its change cost and reorganization consequences through a deliberate review step. |

The selector orders tasks by live emergencies, existing obligations and ordinary improvement opportunities.
Every revealed applicable action remains discoverable through its row selector, including an unaffordable action with an explicit reason.
The selector contains task labels and status information, while the row retains the single execution control.
An emergency rescue or evacuation presents its deadline and endangered cohort before discretionary routine work.
An observation task describes uncertainty and service needs without implying that it accelerates the Sun's return.
Priority review replaces the action area with three mutually exclusive choices and one confirmation, while the original execution rows are hidden and inactive.

After Return, A19 Repair Winter Damage and A20 Reopen Essential Services occupy the relevant recovery rows.
The current crisis values retire, and a clearly dated episode summary preserves their historical record outside the active-value regions.
Recovery rows use actual outstanding damage and service obligations from their owning systems.
The window closes its active-crisis actions immediately while keeping legitimate recovery work accessible.

## 4. Required views and disabled conditions

The initial view follows the committed global entry transaction and shows the selected evolved opening exactly as installed.
Local acknowledgement presents the three allocation priorities without postponing environmental effects.
An unanswered prompt resolves through the approved safe default and shows the resulting commitment.
The normal view supports baseline, Deep Freeze, Things in the Darkness, Endless Night and every permitted disabled-lower-stage combination.

The strained view identifies a failing essential service and the actual constraint on an otherwise useful intervention.
The severe view gives active rescue, broken reception capacity and interrupted upkeep clear prominence without adding another national pressure display.
The no-target view explains whether the country lacks an eligible state, access, delivery proof or an applicable incident.
The empty-mission view remains concise, while the full view shows all three missions and explains the slot requirement on further work.
The captive or ownership-change view preserves the prior payer and receipt history while evaluating the new lawful actor.

Every action has normal, hover, pressed, selected, locked, active, partial, completed, interrupted and unavailable-after-Return coverage where those states apply.
Blocked-reason precedence follows lifecycle validity, lawful actor and target, action reveal, duplicate commitment, mission capacity, physical access, resource and reserve checks, construction capacity, and cooldown.
The tooltip may list several failures, with the first decisive reason attached to the row.
Spendable costs and retained reserve requirements occupy distinct labelled groups.
Temporary construction reservations show occupied capacity, release conditions and an existing commitment's payer.
A15 presents fuel, support equipment and maintenance factory-days as its three spendable types, with timing, ceiling and simultaneous-factory occupancy disclosed in the full quote.
Delivered quantities, paid quantities and promised quantities remain separately attributable.

Fuel exhaustion, equipment shortage, damaged access and failed receiving capacity must each produce a distinct truthful state.
Partially completed work shows retained progress and actual next requirements without implying a fresh purchase will refund its earlier costs.
A locked action has an unmistakable inactive face, a readable reason and a disabled click predicate.
Decorative overlays use supported click-through behavior, and hidden panes cannot intercept input.
Closing a popup leaves ongoing paid work and mission deadlines intact.

## 5. Paused updates and interaction integrity

All displayed values, costs, affordability, selection, availability and tooltips update while the game is paused.
The implementation uses live read-only getters or synchronously published projections after the owning mutation completes.
Each transaction publishes one coherent final state so a new price cannot appear beside an old affordability result.
Presentation updates perform no independent assessment pulse, population registration or worldwide scan.
Every dirty dependency includes owner change, access change, actual delivery, resource debit, reservation release, mission completion, policy change, stage activation and Return.

A click rechecks Part 4's current owner, target, episode, generation and payment predicates.
A stale visible action cannot spend resources after Return or apply to a newly captured target.
Concurrent changes resolve through the owning transaction, and the window then reflects its committed receipt.
The same action contract supplies the player interface and AI path.
An action completes automatically when its real success conditions are satisfied, with no second purchase click.

The fixture set must include paused changes while the window is open, changes while it is closed, reopening, quiet intervals and capture-only bindings.
It must also include an affordability change immediately before a click, a mission completion between two consequence pulses and Return during an open confirmation.
Long target names, the longest real cost strings, maximum displayed values, empty lists and fully occupied mission capacity need native-size review.
Reference-capture bindings remain invisible in engine-loaded files outside their explicit preview fixture.

## 6. Native asset inventory

This inventory enumerates every accepted presentation family and records the final consumer as a required implementation field.
Existing valid runtime art is reconciled before production, with protected textures and sprites preserved under the supplied asset rules.
A missing connection or conversion is resolved through its existing source lineage when that lineage is usable.
Each inventory row receives a required, existing-valid, production-needed or blocked disposition with a specific reason.

| Design inventory | Quantity and native target | Required use and art direction |
| --- | --- | --- |
| MAP124 | Engine-route resources pending feasibility proof | The map owner records the exact required runtime files, consumers and restoration behavior when the accepted native route is established. |
| CAT124 | One category icon at the inspected native canvas | The icon identifies the crisis beside its native category entry and links to the event management window. |
| GUI124_PANEL | One panel composition and reusable native control skin set | A restrained period administration surface groups target selection, services, commitments and actions within measured usable interiors. |
| GUI124_VALUES | Two dedicated value symbols | The symbols distinguish functioning civilian services from proven corridor delivery at the exact GUI canvas. |
| GUI124_STAGES | Four stage badges | Baseline, Deep Freeze, Things and Endless each have an intelligible native-size silhouette without embedded text. |
| GUI124_CONDITIONS | Ten qualitative condition glyphs | Three protection conditions, four route conditions including unknown, and three threat conditions remain distinguishable without colour. |
| GUI124_MISSIONS | Six status glyphs | Pending, active, complete, partial, failed and interrupted work use the inspected mission family and native states. |
| DEC124_A01 through A20 | Twenty 32 by 32 decision icons | Each accepted action receives its own surface-specific composition and a complete consumer mapping. |
| IDEA124_ENVIRONMENT | Four 64 by 64 variants | The environmental slot communicates the highest active presentation stage while its tooltip lists all actual effects. |
| IDEA124_DEPRIVATION | Three 64 by 64 human-exposure variants and one eligible nocturnal counterpart | The slot distinguishes disruption, established exhaustion, prolonged exposure and the accepted pure-nocturnal presentation. |
| IDEA124_PRIORITY | Three 64 by 64 commitment icons | Distributed relief, strategic continuity and concentrated support have distinct allocation imagery. |
| REPORT124_R01 through R12 | Twelve 210 by 176 report compositions | These scenes cover the report families described below with the required monochrome or sepia card treatment. |
| NEWS124_N01 through N06 | Six 397 by 153 compositions | These cover manifestation, Deep Freeze, organized attacks, refuge dependence, ordinary Return and recovery. |
| SUPER124_S01 through S03 | Three 457 by 328 compositions | Each accepted super-event intention has a separately composed scene and exact slot handoff. |
| ACH124 family | Eighteen 64 by 64 runtime outputs | The six achievements in Part 8 each receive completed, grey and not-eligible states using the supplied templates. |
| AUDIO124 family | Three unique final OGG tracks and twenty-one settings-volume song variants | Each accepted super-event has seven registered volume variants including silent replacement. |

The environment, deprivation or eligible nocturnal counterpart, and allocation commitment occupy at most three simultaneous spirit slots.
Mixed-army family bonuses retain their own removable mechanical carriers and do not gain a misleading blanket country spirit.
The single nocturnal counterpart icon requires an eligible pure-creature country with verified actual surviving actors.
Mission consumers may reference their corresponding action icon only when the exact native family, frame metadata and semantic meaning match.
Any mismatched consumer receives a separately cataloged asset requirement before production begins.
Control skins and reusable status glyphs use verified native assets where suitable, with their provenance and runtime consumer retained.

The accepted interface uses native control and meter motion.
Map darkness belongs to the engine presentation route and has its own implementation evidence.

## 7. Scene and text direction

R01 shows a household arranging warmth under an abnormal daytime sky, with limited fuel and ordinary domestic objects making the burden concrete.
R02 shows communal food distribution with containers, queues and documented scarcity, preserving the dignity of recipients.
R03 shows a clinic or rest space coping with exhaustion and disrupted routine, without visually diagnosing universal vitamin deficiency.
R04 shows a factory shift handover under artificial illumination, with tired workers and continuing production demands.
R05 shows road markings and guarded movement through poor visibility, using period transport and practical navigation details.
R06 shows a damaged railway or supply crossing whose repair has material and labor requirements.
R07 shows harbor handling or convoy transfer where delivery depends on working equipment, access and crews.
R08 shows an organized evacuation and reception point with manifest checking and limited shelter capacity.
R09 shows a search for missing travelers through abandoned roadside objects and cautious rescuers, with uncertainty preserved.
R10 shows evidence of a verified regional predator incident at a road or outpost, using the accepted actor identity and restrained distance.
R11 shows a functioning lit refuge with warmth, food handling, maintenance and a dark surrounding landscape.
R12 shows reopening or repair after daylight returns, with surviving damage visible in the composition.
Story variants may share an appropriate report family when the composition truthfully depicts their actual subjects and consequences.

Children appear as people receiving care, reassurance or shelter, with dignified expressions and ordinary family relationships.
Reports may communicate fear through restricted movement, uncertainty and exhausted routine without graphic suffering.
News compositions emphasize geographical reach and public consequences while retaining the same period material culture.
Ordinary Return news shows daylight returning to familiar damaged places and directs attention to continuing shared recovery obligations.
Text briefs distinguish confirmed receipts, uncertain reports and observer interpretation.
They avoid medical deadlines, invented astronomical certainty and claims that electric lamps restore nutrition or cancel native night-combat rules.
Final prose, option wording and localisation keys remain a separate reviewed writing task.

## 8. Three consequence-gated super-event intentions

SE124_MANIFEST accompanies the once-committed global manifestation after map, combat and environmental owners have applied their accepted behavior.
Its scene direction is a recognizable period city or working landscape under an impossible daytime sky, with people responding to the changed world.
Its text direction establishes visible consequences and uncertainty about cause, including any genuinely active evolved opening.
The presentation receipt prevents a second manifestation when local acknowledgement, reload or an evolution repeats a callback.

SE124_ENDLESS_CONSEQUENCE becomes eligible only after Evolution III is active and a material worldwide consequence gate is satisfied.
Gate A requires paid operating refuges in at least three independently controlled countries for 30 consecutive days.
Each country must have at least 10 percent of its own eligible population dependent on those functioning refuges during the qualifying interval.
Their sustained service must also shelter at least 1 percent of the eligible world population in total.
Gate B requires at least 20 percent of eligible world population to have a local essential-service assessment below 35 for 30 consecutive days after Evolution III.
Each resident cohort uses its actual locality's service assessment.
World-population shares use the fixed episode denominator and lawful cohort accounting defined in [Part 6](124_sun_moves_away_spec_part_6_integrations_and_chaos.md).
Gate B's duration resets when its world-share condition falls below threshold.
Both gates consume completed state and service-time facts through the existing aggregation owner, with no new public meter or polling scan.
The intention fires once for the episode when either gate qualifies, and stage activation alone produces no grant.
Its scene direction places supplied settlements within a broad abandoned landscape, with their limited working light making continued dependence visible.
Its text direction explains dependence on sustained services and the real cost of maintaining them.

SE124_RETURN_AFTERMATH follows successful immediate Return cleanup when the episode lasted at least 180 days or met one of three recorded consequence thresholds.
Those alternatives are at least 100,000 shared observed Sun-attributed civilian deaths, at least 1,000,000 unique actual Sun-caused displaced people, or at least 10 registered Sun-caused infrastructure or factory level-equivalents of damage.
Attribution and deduplication use the shared owners' receipts, including their uncertainty rules.
A shorter episode below every consequence threshold receives ordinary global news.
The super-event's scene direction shows returning daylight across people, functioning shelters and unrepaired damage.
Its text direction acknowledges survival and remaining obligations without implying that the historical harm has been reversed.

All three intention handles are unallocated design identities, with final presentation slots, audio IDs, titles, buttons, quotations and cultural references still requiring research and collision checks against [the shared identifier registry](../shared_identifier_registry.md) and the current selectors.
The `SE124_` prefix names Event 124 only and implies no presentation slot or audio ID 124, both of which the registry already reserves for another event.
The `chaosx_super_event_text_researcher` compares several verifiable candidates and records exact wording, source, author, date, fit, attribution confidence and rights status.
The `chaosx_super_event_audio_researcher` checks suitable approved repository music first, then verifies legitimate external sources when needed.
Composition rights and recording rights receive separate proof, and each accepted cue has its own track and audio ID unless the exact reuse has explicit approval.
The preferred musical duration is one to two minutes, with any exception documented under the supplied super-event rules.

Final audio uses OGG under the established music path and the settings-aware `play_current_super_event_audio` dispatch.
Each audio ID registers suffixes `0_5`, `1_0`, `1_5`, `2_0`, `2_5`, `3_0` and `0` in the music asset, song list and super-event station.
The current registrations belong in `music/chaosx_super_event_music.asset`, `music/chaosx_super_event_music.txt` and `interface/chaosx_super_events.gui`, with attribution in `music/chaosx_music_track_list.html`.
The silent variant replaces the preceding cue, and consecutive super-events retain single-cue playback.
The parent aligns `GetSuperEventImage`, all text getters, event triggers, settings, audio catalog and the authoritative catalog workbook, whose CSV exports are regenerated only through `python .tools/export_event_catalog_csv.py`.
An intention with unverified music or wording remains a planned presentation item with an explicit missing-evidence state.

## 9. Production, review and completion

Before art production, inspect the current asset library catalog, exact family contact sheet and actual runtime consumer.
Before native GUI implementation, accept a compositional reference and map its regions to element IDs, interaction, assets and states.
Generated documentary scenes and icons preserve immutable source candidates, explicit reference roles and verified transparency where the consumer requires it.
Each report, news and super-event canvas receives its own composition and native-size review.
The current 2D conversion route produces the required BGRA32 DDS, followed by decode, alpha and exact-dimension checks.
The parent completes a row-level requirement-to-source-to-texture-to-sprite-to-consumer audit.

GUI review covers normal and boundary fixtures at 1920 by 1080 and UI scale 1, plus the supported resolution and scale matrix agreed from the actual parent window.
Matched before and after evidence retains source revision, scenario identity, values, language, resolution and asset hashes.
Review includes full-window composition, detailed text and edges, disabled faces, click rectangles, clipping, scrolling, tooltips and mutually exclusive states.
Unavailable MCP previews after the retry limit restrict visual claims and trigger source-based checks within the authorized scope.
Known in-scope visual defects remain findings to correct.

Map acceptance includes ordinary daytime and nighttime, several map modes, selected states, visible frontlines, hover information and Return at the same camera position.
The overlay, terrain, sea, unit markers and selection affordances must remain readable and interactive throughout the crisis.
Presentation evidence alone cannot verify native night-combat mitigation or absence of doubled actual-night penalties.
Those claims require the engine acceptance evidence defined by the parent and implementation maps.

The `chaosx_event_ui_worker` route owns the proposed dedicated window, including its paused-update behavior, under `chaos-redux-scripted-gui`; `chaosx_generated_event_art` and `chaosx_icon_artist` own their bounded assets under `chaos-redux-event-assets`, and the parent owns shared interfaces, gameplay integration and final acceptance.
The completed handoff lists exact files, selected sources, runtime identifiers, state coverage, unavailable checks and remaining integration work.
Temporary event asset evidence remains available until durable provenance and acceptance records have been promoted to permanent documentation.

**Source note:** The current scripted GUI, event asset and super-event production contracts and the contextual sources are indexed in the [research record](124_sun_moves_away_research_and_sources.md).
