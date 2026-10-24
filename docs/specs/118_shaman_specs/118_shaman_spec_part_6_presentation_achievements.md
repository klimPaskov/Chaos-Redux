# Shaman, Part 6: Presentation, achievements and assets

All invented labels in this part are working identifiers or text direction.
The implementation agent writes final player-facing names, descriptions, options and tooltips after the mechanics are accepted.

## Text direction

The event should feel like an encounter between a government, a local community and a person whose abilities remain uncertain.
Give the community practical concerns and the visitor an intelligible local purpose.
Officials can be skeptical, anxious, respectful or opportunistic.
Avoid a single omniscient narrator who certifies every miracle or exposes every fraud.

| Surface | Required content | Tone and limits |
| --- | --- | --- |
| Catalog Details and Event Details opening | Regional visitor, direct controlling government, offer of aid and uncertain bargain | Complete premise prose, not a modifier list |
| Arrival report | Local identity, named home, intermediary, current problem and evidence of backing | Concrete local scene, no generic exotic mysticism |
| Audience choices | Peaceful refusal, welcome and persecution as distinct acts | Explain consequential treatment without final sample wording |
| Rite offer | The two purposes and eligible state selection | The military purpose must identify its local operational need |
| Confirmation | Quote, target, pace, duration, principal benefit and downside | Clear practical consequences, harmless first cancellation |
| Effective result | Actual food, assistance or local service delivered | Practical and supernatural interpretations can coexist |
| Exceptional result | A striking observed improvement with an unexplained element | No universal statement that this culture's beliefs are proven |
| Inconclusive result | Useful conventional work where delivered, and uncertainty | No dishonest claim that the paid action did nothing when supplies arrived |
| Adverse result | Specific damaged stores, disruption or dangerous guidance | Critique this event and its judgment, not an ethnic group |
| True Sight activation | Visions become more specific after welcome and high Chaos | Unease and specificity, without explaining hidden flags |
| Vision | State, danger, window, public evidence and useful preparation | Distinguish a conditional warning from a guaranteed future |
| Inquiry | Actual corroborating, mixed or contradictory evidence | No paid authenticity certificate |
| Resolution | Owner evidence, response result, remaining harm and next work | Separate observed effect, modelled reduction, prevention and unused readiness |
| Contact closure | Visitor leaves, relationship ends or authority is lost | Preserve the original community and historical actor |

Humor, if used, belongs in restrained bureaucratic irony about officials attempting to budget for the unknown.
It must not mock pronunciation, poverty, religion, local clothing or colonial subjects.
Do not invent a sacred saying as a quotation.
Parchment descriptions use readable plain text.
Tooltips may use supported native colors and texticons.
Dynamic proper names remain intact.

## Four achievement contracts

The following achievements reward sustained outcomes.
Their titles are working concepts, not localisation.
All use the encounter's recorded host and a qualifying non-test campaign.
A debug or forced fixture sets an achievement-ineligible source marker.
Switching tags, replaying an old popup, duplicating a callback or inheriting a conquered state cannot transfer eligibility.

### A1: Sustained local recovery

Difficulty: moderate.
Theme: material relief that lasts beyond the ceremony.

At rite commitment, the selected state must have a real famine stage of 2 or higher under the owner model.
The food blessing must deliver at least seven covered days of its frozen daily need through measured positive deposits.
Within 120 days of first delivery, that same state must improve by at least one famine stage and remain below its commitment stage for 30 consecutive owner-observed days.
The host must retain direct control throughout the qualifying period.

This achievement records a paid blessing followed by real local recovery.
It does not claim the blessing caused every part of that recovery.
Other legitimate relief may contribute.
Full stores with no delivered credit, an owner baseline seed, a closed or changed target, population manipulation, authority loss and merely clicking the rite do not qualify.

Tracking requires the frozen famine stage, daily need, measured Shaman-added reserve total, first delivery date, continuous below-stage interval and authority record.
The icon direction is a plain covered food store with a healthy new shoot.
It must not use a ceremonial emblem from any profile.

### A2: A prepared local defense

Difficulty: hard.
Theme: choosing useful local guidance and sustaining an exposed position.

The military rite must resolve effective or exceptional.
The selected focus state must border a current enemy-controlled state for at least 30 cumulative days during its active benefit.
At least two eligible host divisions must satisfy 21 cumulative daily presence checks in that focus state.
The host must retain the focus state for the first 90 days of the benefit, and its original guidance receipt must remain valid rather than being canceled for a refund.

Exceptional duration beyond day 90 is not necessary.
A quiet garrison without the enemy-frontier exposure, war elsewhere, troops outside the actual state, allied troops outside host control, a peacetime conversion, an inconclusive rite and a state loss disqualify the attempt.
Combat kills are not required or fabricated.
The achievement is about holding a prepared local defense under actual frontier pressure.

Tracking uses the exact receipt, focus state, frontier-exposure days, qualifying presence days and uninterrupted control.
The icon direction is a sheltered field position overlooking a winding route, with one clear supply crate as a secondary element.

### A3: Preparation with a recorded result

Difficulty: hard.
Theme: an uncertain warning followed by effective public action.

One natural vision must bind an exact Event 013 job and meaningful component threshold.
Full preparation must finish before its deadline.
The owner must record that the pre-Shaman consequence request crossed the predicted threshold and that the matching credit produced positive accepted modelled reduction.
The affected state's same-incident recovery card must then reach stabilization complete or a later closed phase within 120 days of the impact, through the owner's actual progression.

The achievement description must not advertise an exact number of lives saved.
An unrelated disaster, a zero-headroom credit, a fabricated future snapshot, a void warning, an independently canceled job without a Shaman contribution, forced phase completion and a merely installed modifier do not qualify.
A warning about a queued follow-up can qualify only through that follow-up's exact owner prevention receipt and the corresponding parent card's observed stabilization.

Tracking includes the source job, component, threshold, paid response, completion date, owner request before and after credit, actual measured consequence, and recovery-card result.
The icon direction is a braced barrier protecting a small settlement from a visible approach of water, with the barrier as the dominant silhouette.

### A4: Judgment under uncertainty

Difficulty: rare.
Theme: using evidence across different warnings.

During one encounter, dismiss a natural vision after a completed contradicting inquiry and later receive an owner result that disproves its named consequence.
On a different natural vision, complete a paid response after corroborating evidence and receive the useful-preparation result defined in Part 3.
Either order is allowed.
Both source jobs must be distinct and non-test, and both outcomes must remain observable.
The contact must close peacefully after the third vision or by the government's deliberate peaceful ending after both records exist.

An unused military readiness window is not evidence of a false natural prediction.
Void or canceled sources do not count.
Secret identity is not a condition.
A player who simply buys every response or dismisses every warning cannot qualify.
This achievement is deliberately constrained by the finite vision pool and the availability of suitable sources, so it may be unattainable in a particular campaign.

Tracking retains two distinct source receipts, their inquiry outcomes, the opposed response choices, their adjudications and the final peaceful closure.
The icon direction is a simple pair of observation lenses and a balanced weight, composed as one readable emblem without religious symbols.

## Achievement state and presentation

Each achievement receives a 64 × 64 completed icon plus the project's required grey and ineligible variants.
Derive those states from the accepted completed image using the current immutable achievement template triplet.
Do not independently generate three different subjects.
Use the actual achievement framework's possible and happened contracts, with tooltip directions matching the conditions above.

Eligibility text should explain the main public condition and relevant failure.
It must not reveal hidden identity, advertise internal arithmetic or expose private hypothesis-support flags.
The detailed tracking contract belongs in the achievement implementation prompt and owner code.

## Asset family and consumer inventory

Use the current canonical reference root `.claude/skills/chaos-redux-event-assets/assets/gfx_references`, its README, CATALOG, REFERENCE_MANIFEST and matching family contact sheets.
Before requesting fresh art, reconcile existing source images, prompts, processed files, candidates, aliases and runtime consumers.
A missing proposed DDS filename is not proof that no suitable existing source exists.

The package requires the following semantic assets.
Proposed sprite names are owner-local working identifiers and must be checked for collision before wiring.

| Asset IDs | Count | Consumer and proposed sprite family | Source mode and native canvas | Subject and coverage |
| --- | ---: | --- | --- | --- |
| RPT-R1 through RPT-R6 | 6 | Arrival, ordinary result and closure reports, `GFX_report_shaman_region_r*` | Original fictional documentary group scenes informed by attributed period research, report family 210 × 176 | One distinct local community scene for each accepted profile |
| RPT-VISION | 1 | True Sight activation, inquiry and warning reports, `GFX_report_shaman_vision` | Original fictional documentary scene, 210 × 176 | Workers raising protective covers over supplies as a messenger brings a warning, active practical work in rain, anonymous silhouettes and no culturally specific ritual props |
| RPT-SETBACK | 1 | Adverse rite and local disruption reports, `GFX_report_shaman_setback` | Original fictional documentary scene, 210 × 176 | Spoiled or scattered supplies after failed work, no ethnic costume or sacred objects as the cause |
| CAT-R1 through CAT-R6 | 6 variants from approved regional scene sources | Ordinary category picture, `GFX_decision_cat_shaman_r*` | Deliberate derived crop of accepted RPT source, native consumer dimensions must be inspected | Current regional identity while category is active, source lineage retained |
| DEC-LAND | 1 | Land selector and land work, `GFX_decision_shaman_land` | Original decision icon, 32 × 32 | Covered store and a leaf, clear native-size silhouette |
| DEC-GUIDE | 1 | Warrior selector and guidance work, `GFX_decision_shaman_guide` | Original decision icon, 32 × 32 | Winding local route and a field marker |
| DEC-CARE | 1 | Aftercare and reconciliation, `GFX_decision_shaman_care` | Original decision icon, 32 × 32 | Repaired crate and a practical tool |
| DEC-INQUIRY | 1 | Evidence inquiry, `GFX_decision_shaman_inquiry` | Original decision icon, 32 × 32 | Magnifying lens and a plain document |
| DEC-LIMITED | 1 | Limited preparation, `GFX_decision_shaman_limited` | Original decision icon, 32 × 32 | One organized supply stack |
| DEC-FULL | 1 | Full preparation and upgrade, `GFX_decision_shaman_full` | Original decision icon, 32 × 32 | Reinforced barrier with supply stack, clearly distinct from limited |
| DEC-CLOSE | 1 | Peaceful closure, withdrawal and cancel review | Reuse an exact verified native cancellation or closure sprite | Existing native meaning, not a newly invented religious symbol |
| MOD-LAND | 1 | Timed local repair or harvest status where an icon is supported, `GFX_modifier_shaman_land` | Original modifier/idea-family badge, 64 × 64 | Substantial food and recovery, no generic national economic miracle |
| MOD-GUIDE | 1 | State-local guidance status, `GFX_modifier_shaman_guide` | Original modifier/idea-family badge, 64 × 64 | Local supply and a defensive position |
| MOD-DISRUPTION | 1 | Event-owned local panic, adverse guidance or repair disruption, `GFX_modifier_shaman_disruption` | Original modifier/idea-family badge, 64 × 64 | Broken route marker and scattered supplies |
| ACH-A1 through ACH-A4 | 4 completed subjects, 12 runtime states | Achievement framework, exact registered IDs from implementation | Original 64 × 64 achievement art plus template-derived states | The four subjects and completion conditions above |

The six category pictures are crop variants, not six additional independently invented scenes.
Their exact size is a consumer verification gate.
Event 013's documented 114 × 101 family picture is a nearby precedent, not proof that every category picture uses that size.
Use the actual Shaman category consumer and matching reference sheet before producing the derivatives.

Report art uses the project documentary treatment with black-and-white sepia, subtle paper tilt, shadow and genuine transparent corners where required by the reference family.
The source composition must remain legible after the 210 × 176 crop.
Native icon families use the project's matching small-format style, not miniaturized report illustrations.

## Source and production requirements

Anonymous fictional group scenes must be clearly treated as generated event art.
They are not archival photographs or portraits of a real person.
Avoid a centered isolated head that would effectively create an unsourced grounded character portrait.
If an identifiable real person becomes necessary, route that consumer through `chaosx_portrait_creator` and the exact sourced identity process before production.

For each regional scene, the source researcher assembles a small attributed period reference set for ordinary clothing, settlement form, transport and tools.
The regional source register supplies cultural boundaries, not automatic reproduction permission.
Review sacred, clan-owned or private material before use.
Practical compositions make it possible to convey place without copying protected ceremonial objects.

The asset manifest must record consumer, semantic role, exact saved generation or edit arguments, referenced inputs and their roles, source URLs and rights status, source hashes, output hashes, crop and processing recipe, alpha evidence, native-size review, selected candidate and DDS conversion.
Keep rejected candidates and their review disposition distinct from final bindings.
Existing runtime art that resolves must not be silently replaced.

The generated-event-art worker owns original scenes.
The asset-source researcher owns non-portrait reference research.
The icon artist owns decision, modifier and achievement subjects.
Parent integration owns GFX bindings unless a narrowly assigned handoff says otherwise.
All sprites are named and wired only after the owning semantic asset is accepted.

## Required visual checks

Inspect every regional source at full size and in the report crop.
The correct community, ordinary material details, group composition and era must remain defensible.
Check that the same accepted scene supports its category crop without losing the meaningful subject.

Review icons at 32 × 32 or 64 × 64 against the actual reference contact sheet.
Limited and full preparation must remain distinguishable in monochrome and at the smallest UI scale.
Achievement grey and ineligible states must derive from the same complete subject.

After conversion, reopen the runtime DDS and verify dimensions, alpha, crop and color against the accepted source.
Test category and event consumers with long state names, all three cooperation bands, the maximum three-entry cost row, one inquiry plus one preparation mission, and the final closed state.
Source review and rendered previews are evidence about those surfaces.
They are not a claim that gameplay behavior has been tested in a live campaign.
