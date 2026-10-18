# Fuel Crisis: presentation and achievement

## A single announcement of the reserve loss

Fuel Crisis announces the world change through one native news notification with one acknowledgment.
The announcement follows the committed stockpile wipe and never controls its execution.
Leaving it open, closing it, or acknowledging it cannot postpone, repeat, or reverse the loss.
Its option offers no policy branch, fuel grant, task assignment, or recovery effect.

The public account describes emptied national reserves and the resulting uncertainty for operations.
It preserves the distinction between a missing reserve and damaged production.
Oil deposits, refineries, fuel silos, ordinary production, trade agreements, and imports continue under their existing rules.
The cause remains unexplained.
No text or image establishes sabotage, a fire, a blockade, or destroyed infrastructure that the gameplay does not implement.

The existing shared event log retains one historical record.
Its report-size picture is presentation for that record and does not create a second popup.
Shared Event Details describes the premise only.
It must not become an effects summary, a feature list, a Tasks instruction panel, or an achievement checklist.
Operational information stays in ordinary fuel and trade interfaces, while an assigned objective stays in the existing Tasks interface.

Each human observer receives at most one announcement for an accepted occurrence.
The event's coordinating country is an execution context rather than a perpetrator.
Neither actor metadata nor the image should imply that it caused the disappearance.
Exact audience dispatch and shared consumer behavior remain implementation verification requirements under the implementation handoff.

## Localisation direction

This specification does not provide final player-facing strings.
All labels and proposed identifiers below are working design references.
Final localisation is written during implementation against the verified runtime keys and the repository's player-facing prose rules.

| Surface | Required meaning and tone | Boundary and alignment |
| --- | --- | --- |
| Native news title | A short, direct identification of Fuel Crisis | Align with the accepted catalog event identity. Do not introduce a different crisis name. |
| Native news description | National reserves have disappeared across the world, creating uncertainty for military operations while ordinary supply continues | Use concrete empty stores, inventory checks, and operational concern. Do not invent a culprit, damage, embargo, mandatory response, or hidden future branch. |
| Single acknowledgment | A concise reaction to the loss | It closes the announcement only. Avoid wording that implies a selected policy or compensation. |
| Shared event log | A brief historical account of the committed reserve disappearance | One record per occurrence. Catalog mirror fields use the final in-game wording where the schema requires it. |
| Shared Event Details | The event's narrative premise and unexplained disappearance | Premise only. No effects list, numeric balance table, recovery guide, Tasks feature list, or achievement rules. |
| Tasks reserve objective | The assigned active route, frozen reserve target, observed hold progress, and deadline | Part 3 owns exact conditions. Explain that fuel is retained rather than paid. Do not promise an objective to every affected player. |
| Tasks oil-access objective | The selected real supply action and actual delivered-supply target | Nominal contracts and relations alone are insufficient. Part 3 owns the source, conversion, observed hold, and outcome. |
| Tasks requirement tooltip | The selected action, its measurable result, frozen reference basis, and the observed daily hold | At most three primary numeric groups remain visible: target or current progress, hold progress, and time remaining. Detailed rates stay in the ordinary fuel and trade UI. |
| Achievement working title | The working label Running on Empty | This is a planning label rather than final approved localisation. |
| Achievement description and requirement tooltip | Recover the full qualifying reserve through a genuine Tasks success with the stricter imported-supply and time conditions below | Explain the extra challenge accurately without creating a second mission. A normal Tasks success can receive its reward without this achievement. |
| Existing achievement description, eligibility tooltip, and unavailable icon state | Truthful requirements and the existing supported indication that the achievement is unavailable | Use the existing UI and supported state contract. Do not imply a new diagnostic panel, reveal every hidden baseline dynamically, or treat ordinary mission failure as the sole reason the badge can be unavailable. |

The announcement and shared history describe the event accurately even when Tasks is disabled or no player receives a Fuel Crisis objective.
They do not claim that every unit becomes immobile immediately, since native unit buffers and allocation remain outside the stockpile wipe.
The shared details premise must remain readable without technical implementation history or tuning explanations.

## Two static scene consumers

The presentation design selects one coherent photographic scene and two distinct static runtime outputs.
The master should show an intact period fuel depot with empty gauges, an idle pump or tanker, and personnel checking the stores.
The emptiness is the subject.
Damaged tanks, burning refineries, wrecked railways, collapsed buildings, and blocked ports would imply additional gameplay effects and are excluded.

Use 1936-1945 documentary composition, clothing, vehicles, and industrial equipment.
Avoid prominent national insignia, recognizable real people, readable generated lettering, modern pumps or vehicles, fake UI, and cinematic grading.
Frame a clear central subject with enough lateral context for the panoramic news crop.
The narrower report crop must retain the same intelligible empty-depot premise.

The parent selects a generated photographic master because the event is fictional and its simultaneous world loss is not a documented historical photograph.
Attributed archival material may inform period references and provenance where needed, with its rights and role recorded.
It is not an alternative production master in this design.
Do not present archival people or places as actual documentation of this fictional occurrence.

| Accepted design row | Intended consumer | Nominal output | Proposed runtime placement | Required binding evidence |
| --- | --- | --- | --- | --- |
| `109_scene_news` | The single native news announcement | 397x153 black-and-white scene | `gfx/event_pictures/109_fuel_crisis/news_event_109_fuel_crisis.dds` | Actual news event, image field, sprite name, owning GFX definition, exact dimensions, audience dispatch, and acknowledgment behavior. |
| `109_scene_log` | An actual report-picture slot in the shared event log or its supported presentation | 210x176 RGBA report card | `gfx/event_pictures/109_fuel_crisis/report_event_109_fuel_crisis.dds` | Exact shared consumer, field and sprite mapping, owning GFX definition, canvas and alpha behavior, and rendered consumption. The picture must not introduce a standalone report event. |

These paths and row identifiers are proposals until the parent verifies the current consumers and locks runtime names.
Preserve an existing registered basename or sprite when the actual framework requires it.
The report row requires an actual compatible picture slot.
If that slot cannot be verified, report the row as blocked rather than manufacture a popup or substitute an unrelated interface.
Any accepted change to the row must record its design basis explicitly.

One photographic source master can feed both scene consumers.
The source is not a third runtime row.
Each output has its own crop, treatment, exact canvas, final DDS, source mapping, and native-size review.
Do not reuse one incompatible texture path for both canvases.
These scene crops are not icon art and do not satisfy the separate achievement requirement below.

## Scene production and acceptance

Use the current owner `.agents/skills/chaos-redux-event-assets/SKILL.md` and its `assets/gfx_references/` library.
Before producing art, inspect the reference README and CATALOG, the `event_art/report/` and `event_art/news/` contact sheets, matching individual examples, and the exact active consumer definitions.
The earlier `assets/vanilla_reference/` and independent leader-portrait shelf are historical source paths rather than current production directions.
Reference PNGs and contact sheets are review material and cannot be wired as final art.

The selected generated non-portrait route belongs to `chaosx_generated_event_art`.
Pass exact locked consumers, output dimensions, names, folders, and handoff scope to that worker.
If archival reference research is needed, `chaosx_asset_source_researcher` supplies attributed reference material rather than replacing the selected generated master.
The parent owns final non-portrait GFX registration and shared-framework wiring.

Produce the photographic master before applying the report-card treatment.
For the report output, use the owner skill's `tools/process_report_event_image.py` workflow to produce the documentary monochrome-with-sepia card, subtle tilt, paper edge, transparent margin, and soft shadow.
Do not ask ImageGen to generate the tilted card itself.
For news, make a separate panoramic cover crop and black-and-white press treatment at 397x153.
Both source treatments must preserve a readable subject and avoid generated text.
Use the current owner `tools/convert_to_dds.py` for final 2D scene conversion after consumer verification.

For the generated master, preserve the exact actual request, input image roles, returned source dimensions, source hash, candidate lineage, and final-selected candidate.
The active built-in image tool offers no model selector, so production records must name the exposed execution path without claiming a backend selection.
For any archival reference, preserve the untouched reference and record its page, creator or archive, estimated date, license, role, and era-fit uncertainty.

| Acceptance surface | Required evidence | Failure treatment |
| --- | --- | --- |
| Requirement and consumer | Accepted row mapped to an actual native news or shared report consumer | A guessed field, nonexistent slot, or unrelated surface leaves the row blocked. |
| Source provenance | Exact generated request and source lineage, plus attribution, role, and defensible rights for any archival reference | Missing or incompatible provenance cannot be covered by a visually plausible image. |
| Premise and period | Intact empty stores, period equipment, no invented physical destruction or readable generated lettering | Repair the specific defect or reject the candidate. |
| Independent crops | Master-to-news and master-to-report mappings, crop coordinates, processed dimensions, and separate native-size review | A good master does not prove either final crop is readable. |
| Report card | 210x176 RGBA, transparent corners, complete photo edges, subtle tilt, and soft shadow | Black padding, a clipped photograph, or a thick artificial border fails. |
| News scene | 397x153 black-and-white output with a clear subject and no modern color remnants | Panoramic cropping must not remove the evidence of empty stores. |
| Final DDS | Strict 2D header and dimension checks, decoded native-size pixels and alpha, exact final hashes | PNG-only output or a malformed DDS remains incomplete. |
| Runtime linkage | Final path, registered sprite, actual consuming source and id, and shared/native rendered evidence | File presence alone does not establish consumption. |
| Review | A labeled contact sheet showing both consumer outputs decoded from final DDS, source comparison, and parent acceptance | Source previews or conversion success alone do not permit completion. |

While production is active, use the temporary event workspace under `docs/assets/109_fuel_crisis/` for sources, prompts, processed previews, crop evidence, contact sheets, manifest, and GFX handoff.
Record each accepted row's source package, final asset, registry, actual consumer, review evidence, and status in a requirement-to-runtime crosswalk.
Count file inventory, registered aliases, actual consumption, and accepted coverage separately.
At full event completion, promote durable provenance, licensing, lineage, reviews, and wiring facts into permanent documentation, verify that runtime references point to engine-facing folders, and follow the current owner cleanup contract.
Blocked or incomplete work retains its evidence workspace.

## A difficult achievement owned by a Tasks outcome

The parent selects one achievement as part of this planning design.
Its proposed registry key is `109_fuel_crisis_running_on_empty` and its working label is Running on Empty.
It is a visible achievement in the existing achievement catalog, with the supported completed, grey, and not-eligible presentation states.
This parent design choice is within the full planning request.
It is not an explicit user approval of these exact conditions, implemented gameplay, or a verified native achievement contract.

The achievement recognizes a particularly demanding recovery by the same affected player country.
It is attached to a genuine successful Event 101 Fuel Crisis reserve task.
It is not a second mission, a Fuel Crisis reward table, a passive refill award, or a recurring world recovery service.
Rewards and penalties remain entirely with Event 101.

The ordinary reserve contract in Part 3 retains its target of `min(14 × D0, 50% × C0)`, alternative active conservation or supply routes, and a dynamic 90 to 180-day duration after assignment.
The achievement is stricter and has its own 90-day completion limit measured from the wipe.
It does not shorten the ordinary task deadline or change its outcome.
An ordinary task can succeed later and receive its Event 101 reward without earning the achievement.

### Frozen eligibility and exact success conditions

D0, C0, and F0 have the definitions and common units established in Part 3.
D0 is meaningful demand implied by pre-wipe active commitments, not the reduced actual consumption caused by fuel starvation.
All rate comparisons use verified fuel-equivalent quantities per game day.
The imported contribution must not mix nominal raw oil units with stored-fuel units.

| Gate or condition | Exact requirement | Owner and capture time |
| --- | --- | --- |
| Country identity | The same country exists and is player-controlled both at the committed wipe and at task assignment | Event 109 onset context, then the Event 101 recipient record. |
| Existing war | That country is at war at the wipe and at assignment | Verified onset and assignment predicates. Starting a new war is never required. |
| Meaningful demand | D0 is positive and passes the reliable meaningful-demand gate in the Tasks selector | Freeze D0 before the wipe. An unavailable demand accessor blocks eligibility. |
| Material reserve loss | F0 is at least `7 × D0` | Read positive pre-wipe national stock before zeroing it. |
| Storage | C0 is at least `28 × D0`, and current capacity can hold the full target | Freeze C0 at onset, verify current capacity at assignment. |
| No automatic surplus | Ordinary dependable usable inflow J0 at assignment is at most D0 | Event 101 assignment measurement, alongside Part 3's no-action forecast and active-action eligibility. |
| Valid objective | An active Event 101 Fuel Crisis reserve task is assigned to that country using the same committed occurrence receipt | Event 101 selection and frozen task record. Oil-access template success alone does not earn this achievement. |
| Active imported improvement | A verifiable post-assignment ordinary imported-oil supply action creates at least `0.25 × D0` additional actually delivered fuel-equivalent flow relative to the assignment baseline | Event 101 action and supply evidence. A request, nominal agreement, one-time stock injection, or unrelated production change is insufficient. |
| Full reserve | Actual national stored fuel reaches at least `14 × D0` | Live verified stock reading during the active task. The target remains frozen. |
| Observed hold | Both the full reserve and the additional delivered imported flow qualify for seven complete daily observed intervals | Event 101's verified progress evaluator and the shared hold semantics below. |
| Time | The final qualifying observation and success resolution occur within 90 days of the wipe and by the original task cutoff | Compare against both stored cutoffs using one documented native date and tick convention. |
| Genuine success | The actual Event 101 success callback confirms the normal reserve-task contract and the full achievement conditions once | Event 101 terminal resolver sets a durable achievement completion flag after validation. |
| Eligible occurrence origin | Ordinary shared selection or a normal non-force manual trigger that satisfies shared eligibility | Use the committed receipt's frozen origin and provenance. Deliberate force and raw direct-debug occurrences are ineligible. |
| Campaign validity | The repository's existing achievement validity contract also passes | Reuse verified existing validity rules. Do not invent a new anti-console platform. |

The C0 gate means an achievement-eligible country's ordinary reserve target is already the full `14 × D0`.
The additional challenge comes from its substantial onset reserve loss, wartime exposure, delivered imported-supply intervention, and completion within the shorter onset-based window.
Winning the existing war after assignment preserves eligibility.
The task remains subject to the normal player-control and country-existence lifecycle.

The ordinary task's selected active route is not replaced by the achievement.
A conservation-selected task still requires its own qualifying conservation action.
It can earn the achievement only if the imported-supply improvement and every other stricter condition are also proven before the genuine success callback.
A supply-selected task must likewise prove the imported improvement rather than substitute a different domestic or one-time supply result.
Missing optional achievement proof does not prevent a valid ordinary Tasks success or reward.

### Delivered imported flow

The assignment baseline must isolate actually delivered imported-oil fuel-equivalent flow under the verified game rules.
The qualifying increment is the recurring usable contribution created by the ordinary post-assignment imported-oil action.
The success evaluator must attribute the increase to that action and confirm it is still delivered during each hold observation.
An unrelated conversion technology, a domestic oil change, a diplomatic promise, or a nominal trade allocation cannot prove this condition alone.

Where more than one real route contributes, Event 101 must retain enough source identity and attribution to establish the increment without double-counting.
This specification does not assert native route identifiers, production accessors, demand accessors, or delivered-oil conversion functions.
Those measurements are unresolved until the installed game and the Tasks owner provide exact supported evidence.
An implementation must not infer actual delivered fuel from an unverified agreement amount.

### Seven complete observed intervals

The first observation satisfying the full reserve, delivered imported increment, qualifying action, and all ongoing task conditions starts the achievement hold at zero elapsed days.
Seven subsequent daily confirmations establish seven complete observed days.
The final observation must still satisfy the full contract and both cutoffs.
This is eight qualifying observations over seven elapsed intervals, not seven samples mislabeled as seven complete days.

A failed condition resets the hold while the original task and achievement cutoffs continue.
A missed daily interval cannot be inferred from a later reserve value or filled in after loading a save.
Daily observations do not prove that every intraday stock or delivery value stayed above the threshold.
The description and tooltip must use observed-hold wording rather than claim uninterrupted intraday proof.
If Event 101 already provides a stricter validated continuous evaluator, it may satisfy this contract without weakening it.

The implementation must document whether the final permitted tick is inclusive and apply that convention consistently to the 90-day onset cutoff, Tasks deadline, displayed timer, hold evaluator, and success resolver.
The final permitted observation may qualify only while both cutoffs remain valid.
The first observation after either cutoff cannot rescue the achievement.
Normal Tasks success and timeout precedence remain governed by Part 3.

### Owning fields and minimum state

The following are semantic fields to bind to the verified owner API.
They are not invented script variable names or assumed runtime structures.

| Semantic field | Owning system | Purpose and lifecycle |
| --- | --- | --- |
| Committed occurrence identity, onset date, and frozen origin | Event 109 | One causal receipt shared with Tasks. Duplicate delivery cannot create a new qualifying shock. Only ordinary shared selection and an eligible normal non-force manual trigger admit achievement provenance. |
| Original recipient identity and human/war onset facts | Event 109 onset context and Event 101 assignment | Prove the same eligible player country suffered the material wipe and received the task. |
| D0, C0, and F0 | Event 109 pre-wipe context when the verified integration is enabled | Frozen eligibility and scaling references. Capture cannot delay or limit the unconditional wipe. |
| Assignment J0, commitment demand Da, capacity Ca, and imported-flow baseline | Event 101 | Establish the no-surplus condition, preserve the ordinary task's action and forecast contract, and measure genuine post-assignment improvement. |
| Selected action and actual import attribution | Event 101 | Prove a deliberate ordinary action created and maintained the delivered increment. |
| Frozen ordinary task contract and cutoff | Event 101 | Preserve the normal mission and its 90 to 180-day deadline after assignment. |
| Full reserve requirement and 90-day onset cutoff | Event 101's achievement qualification within the active task | Additional comparison values derived from the existing onset record rather than a second visible mission. |
| Observed hold and observation continuity | Event 101 progress evaluator | Confirm or reset the stricter hold during the active task. Preserve exact evidence across saves. |
| Terminal disposition and genuine success receipt | Event 101 | Resolve once, award the ordinary outcome once, and prevent repeated callbacks. |
| Durable achievement completion flag and provenance | Verified Tasks success callback and existing achievement registry | Preserve the qualifying result after active-task cleanup. Exact flag identifier is chosen during implementation. |

Reuse generic Tasks records, progress evaluation, and completion hooks wherever they already provide these facts.
The event adds no standalone polling hook, separate recovery platform, or second mission evaluator.
If generic Tasks cannot retain or observe the extra qualification safely, the achievement remains blocked until the owner provides a bounded implementation supported by evidence.
Do not lower the conditions or add a new tracking platform to make the badge easy to ship.

The parent must verify the actual achievement registry, its validity rules, and the per-country flag consumption pattern.
The pinned targeted reference shows one registry `unique_id = chaos_redux_achievements` and grouped string identifiers with country-flag completion predicates.
Add the accepted achievement to that existing registry when implementing it.
Do not create another registry file or duplicate its unique id.

### Disqualifiers and ordinary outcomes

The achievement does not qualify for an AI country, a later-created country, a recreated tag inheriting old context, a different recipient, missing onset evidence, an onset country not at war, insufficient F0 or C0, zero or unreliable D0, or an assignment with ordinary usable inflow above D0.
Its meaningful-demand gate must reject trivial reference demand rather than turn a nearly unused fuel system into an easy award.

Passive refill, an intervention made before assignment, a merely requested import, a non-delivering source, an unverified conversion, a one-off gift, a debug success receipt, a missed observation interval, an incomplete hold, or a completion after the achievement cutoff cannot establish the badge.
Deliberate forced occurrences and raw direct-debug opening calls cannot earn this achievement.
Only ordinary shared selection and a normal non-force manual trigger satisfying shared eligibility supply eligible occurrence provenance.
The existing achievement validity contract remains an additional gate.
Use the receipt's existing frozen origin rather than add an anti-console platform.

Country disappearance, relinquishment to AI, disabled Tasks, or technical invalidity follow Part 3's neutral cancellation lifecycle.
No achievement provenance or active task transfers to a successor country.
Foreseeable campaign disruption remains a risk under the original task rather than an automatic cancellation that avoids failure.
An interrupted achievement hold alone resets its progress and does not add a punishment.

A fresh deliberate forced occurrence replaces the old crisis context under the implementation handoff.
The old task is neutrally cancelled by its owner before any new-context assignment.
Old and new receipts, baseline facts, holds, and success callbacks must not be combined.
The first committed occurrence consumes the natural slot even when its origin is force or raw debug.
Later deliberate force replays never reopen that slot and remain ineligible for this achievement.

If the ordinary task succeeds without full badge proof, it resolves normally and grants its Event 101 reward.
The badge cannot be earned retroactively by later trade or fuel accumulation after that active task has ended.
Missing the 90-day badge window does not expire a still-valid ordinary 90 to 180-day Tasks contract.
There is no additional fuel payment, bonus modifier, currency, reward, penalty, or follow-up wipe.

## Achievement icon and acceptance crosswalk

The icon is a separate authorized consumer family rather than a scene crop.
Use one compact original transparent subject combining an empty period fuel can and a restored supply hose, with a readable silhouette and subdued industrial materials.
The composition should suggest recovery through supply without text, a fake gauge UI, a scene thumbnail, or a copied icon.
It must remain intelligible at 64x64.

| Accepted design row | Consumer and output | Proposed final paths | Acceptance requirements |
| --- | --- | --- | --- |
| `109_achievement_running_on_empty` | Existing achievement registry and UI, three 64x64 states | `gfx/achievements/109_fuel_crisis_running_on_empty.dds`, `gfx/achievements/109_fuel_crisis_running_on_empty_grey.dds`, `gfx/achievements/109_fuel_crisis_running_on_empty_not_eligible.dds` | Exact accepted registry id, original subject evidence, immutable templates, complete state triplet, native-size review, strict DDS decode and composition equality, actual consumer, and parent acceptance. |

The key and paths remain proposals until registry naming and UI lookup are verified.
Final achievement DDS files use the existing root-only placement convention rather than an event subfolder.
Record any sprite aliases separately from the registry id and actual runtime paths.

Route original subject production to `chaosx_icon_artist` under the current event-assets owner skill.
Inspect `assets/gfx_references/icons/achievements/contact_sheet.png`, relevant examples, the owning achievement UI, and the exact immutable inputs under `assets/gfx_references/icons/achievements/template/`.
The current supplied workflow inputs are `achievement_template.png`, `achievement_template_grey.png`, and `overlay.png`.
Verify their owner-recorded SHA-256 identities before use.
Do not resize, recolor, redraw, move, replace, or modify these inputs.

Generate one original color subject with genuine transparency and no achievement frame, square background, red cross, lettering, or fake checkerboard.
Process it into the centered 64x64 subject layer while preserving native alpha.
Derive the grey source deterministically from that same subject with exact canvas, position, and alpha.
Build the not-eligible source by applying the unchanged supplied overlay to the grey source at the exact alignment.
Do not generate three unrelated state paintings or reuse another icon family.

Use `.agents/skills/chaos-redux-event-assets/tools/process_achievement_icons.py` on the complete color, grey, and not-eligible source triplet.
It applies the supplied completed background beneath the color source and the supplied grey background beneath both other states.
Do not run the generic single-image converter independently on these final achievement states.
Retain the generated source, exact request, processed subject, complete source triplet, template identity evidence, three composited review PNGs, decoded final DDS states, native-size contact sheet, and final consumer mapping.

The icon cannot compensate for an unimplemented achievement contract.
The registry and trigger cannot compensate for absent accepted icon states.
Report gameplay outcome proof and asset acceptance separately.

## Achievement balance and evidence gates

The challenge must be observable and realistically attainable in at least one supported campaign scenario.
The parent must test its eligibility gates and the remaining time at actual task assignment rather than assume that a 90-day onset window is generous.
A late assignment can leave too little time for action, reserve accumulation, and seven observed intervals.
That does not authorize moving the badge cutoff, forcing an earlier task, changing the ordinary selector, or awarding a passive substitute.

An invented arithmetic example illustrates plausibility without establishing native or campaign feasibility.
Let D0 be 100 fuel-equivalent units per day, C0 be 3,000 units, and F0 be 700 units before the wipe.
Suppose assignment occurs on day 10 after the wipe with zero reserve and ordinary usable inflow of 100 units per day.
A verified ordinary imported-oil improvement delivering another 30 units per day exceeds the required 25-unit increment.
If demand remains 100 units per day, the resulting net 30 units per day reaches the full 1,400-unit reserve after 47 accumulation days.
The initial qualifying observation then starts zero elapsed hold time, followed by seven daily confirmations.
With immediate delivery and a compatible observation convention, completion is around day 64 after the wipe.
Any documented delivery lead time and tick scheduling must be added to that estimate and compared with both cutoffs.
These invented common units demonstrate arithmetic only.
They do not verify the demand getter, conversion, trade delivery, available action, ordinary Tasks selection, or a realistic supported campaign.

| Scenario | Required distinction |
| --- | --- |
| Qualifying wartime importer | A deliberate supported import action supplies the required increment, the full frozen reserve is restored, and the genuine callback completes the observed hold within both cutoffs. |
| Unchanged surplus or passive refill | No eligible badge despite rising stock. Enforce J0 and the active-action gates. |
| Zero or trivial demand | No spurious target or easy eligibility caused by starvation or a nearly inactive force. |
| Insufficient onset stock or capacity | Correct failure of F0 and C0 gates, without changing the ordinary world wipe. |
| Nominal agreement without delivery | No imported increment and no badge progress. |
| Domestic or technology-only improvement | Do not misattribute unrelated production as the required imported-oil action. |
| Reserve or delivery dips | Reset the observed hold without a new penalty or deadline extension. |
| First observation and seventh subsequent confirmation | Count zero elapsed at the first sample and seven complete observed intervals at the eighth qualifying sample. |
| Missed interval or reload | Preserve genuine recorded evidence and reject invented continuity. |
| Exact onset cutoff and task cutoff | Compare the final permitted observation with the first expired one using a documented date/tick convention. |
| Ordinary success after the badge window | Event 101 grants its normal outcome without the achievement. |
| Victory after assignment | Existing-war victory does not invalidate an otherwise qualifying active task. |
| Country removal, AI takeover, or receipt replacement | Normal owner cancellation, no successor inheritance, no mixed-instance proof, and no duplicate outcome. |
| Multiplayer | The actual selected player country owns its own evidence and outcome. Other observers receive no badge from its success. |
| Shared, normal manual, forced, and raw debug entry | Ordinary shared selection and an eligible normal non-force manual trigger can qualify. Deliberate force and raw direct-debug opening calls cannot qualify. Existing achievement validity remains an additional gate, and a synthetic callback is not success proof. |

Native demand, capacity, production, actual delivery, import attribution, progress accessors, and success-callback semantics remain unverified.
If the stricter challenge cannot be observed faithfully or cannot realistically be reached in any supported scenario, keep the achievement blocked and state the exact gap.
Do not weaken the target, imported increment, hold, wartime onset, material loss, or cutoffs.
Do not conceal that blocker behind an icon, a generic flag, or a working core wipe.

## Integration boundary

The parent owns native announcement wiring, shared log and details integration, achievement registry wiring, final asset registration, and cross-surface review.
The scene and icon specialists own only their bounded source, processing, conversion, review evidence, manifest, and handoff surfaces.
The existing shared interfaces do not belong to `chaosx_event_ui_worker` because this design introduces no dedicated event GUI.
Event 101 owns mission action integrity, observed progress, deadlines, all ordinary outcomes, and the validated achievement callback.

Part 5 and the implementation handoff carry the broader acceptance and verification requirements.
This part records a parent-promoted planning design with unresolved runtime paths, accessors, owner APIs, native presentation evidence, and achievement feasibility.
It creates no final localisation, assets, gameplay source, additional interface, or implementation completion claim.
