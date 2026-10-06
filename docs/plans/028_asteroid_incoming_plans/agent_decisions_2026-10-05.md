# Event 028 finishing decisions

Record date: 2026-10-06.
Disposition: implemented source changes, with native acceptance gates explicitly open in `takeover_status_2026-10-06.md`.
Acceptance basis: the user authorized completion of the 028 workstream and, under G6, correction of weak design and source logic without another approval round.
This document supplements the earlier `agent_decisions_2026-10-04.md`; it does not rewrite the stopped thread's historical notes.

## News and impact presentation

The L1 forecast repetition has two source barriers: a persistent queued/published news list and a per-recipient flag consumed in `immediate` and tested by both the sender trigger and `show_major`.
`fire_only_once` is not used on major news, because the offline Event modding reference says it defeats the world broadcast.
The existing single lock guard alone did not establish why the live window repeated.
A temporary saved `asteroid_incoming_forecast_delivery_count` therefore distinguishes repeated delivery from a window redraw and must be removed after the L1 live check resolves that uncertainty.
It writes no log or visible debugging text.

An unprinted opening warning is replaced by the locked forecast or terminal outcome.
The latest dust-stage bulletin replaces earlier unprinted stage bulletins, so a single sharp fall does not produce a stack of nearly identical news.
The super-event waits for open asteroid news and pending/open human country reports; queued asteroid news waits while any super-event is visible.
Impact mechanics and the announced strike date remain independent of these presentation waits.
The existing monthly host recovers news, super-event, and fragment-visual callbacks lost through annexation, without a new daily on-action.
Presentation waits inspect only living human-controlled countries.
Annexation clears the annexed country's open-news, open-report, and undelivered-report flags, while permanent delivery receipts remain intact, so a later release does not revive a phantom window.
Forced re-entry explains a locked course or a completed passage and preserves its opening date and outcome.

## Recovery targets and prices

The highest-ranked affordable state replaces the highest-ranked state regardless of price.
This retains one visible target per action while allowing a poorer country to work on a cheaper damaged state.
Candidate checks read the same state quote and protected reserve fields as the cost and payment gates, including the medical and transport first-use discounts.
The existing strict `greater_than` reserve boundary is retained deliberately, including its equality case, rather than retuned during the selection fix.
Stored prices refresh on an affected state's control change and when a surcharge expires, even after monthly recovery work stops.
Expiry refresh visits the persistent affected-state array so transfers do not retain another country's surcharge.

National network, outer-ring, and regional-economy missions cannot restart after their respective success flag.
Another repair project still performs its physical work, but cannot reopen a completed contract and later punish the country for it.
Local rescue and stabilization contracts retain their state-specific lifecycle.

Native custom costs have all 16 base/blocked/tooltip triplets.
Blocked amounts are red, inline costs show at most three resource values, and the tooltip retains the fourth resource or factory commitment.
The repair surcharge uses a two-word marker; the percentage and duration remain in the full tooltip.

## Crater competition

One highest-profile ready owned site and one ready rival site are exposed, with lower state id breaking ties.
The owned sequence is security, survey, then fortification.
The rival sequence is reconnaissance, disruption, then an offensive plan; disruption is skipped when its field or reserve conditions cannot be met.
The three dust projects can accompany these two actions, keeping the late surface within five primary actions.
Only the mineral-site array is searched, at most seven states.
Rival disruption and offensive result flags expire with their 90-day modifiers, permitting a paid renewal after the effect ends.
Survey, its material identity, and its single research use remain permanent; perimeter security still lapses with control.

## Provincial building damage

Ordinary provincial buildings use all-province zeroing for full loss and ascending original-level cohorts for fractional loss.
The remaining level is `original - round(original * profile_fraction)`.
A reduced province cannot match any later, higher original-level cohort, so it is damaged once.
This interprets the fraction per province, rather than rounding a state-total quota: four level-one forts at 22.5 percent each lose zero levels, while a level-four fort loses one.
The three ten-level fort/port types use ten cohorts; singleton installations use one.
The caller's observed before/after values remain the receipt source, with their native aggregation semantics still to be checked.

Railways and supply nodes remain outside the ordinary setter because the offline Building modding reference warns that ordinary building operations do not safely cover them.
No zero-level railway construction or unverified demolition substitute is introduced.
Complete network removal and construction/special-project cancellation remain incomplete, and suppression is not described as a queue purge.

## AI, profiles, and retained mission scopes

The friendly-ground risk check includes ownership as well as control at the target and two land steps around it, so occupation does not remove the risk to friendly civilians and buildings.
The existing 0.25 factor and all 21 decision/mission score blocks are unchanged.
Required probability comparisons were attempted but did not return usable evidence; numeric acceptance remains open.

The three profile markers use independently generated metal, fused-stone, and crystal icons, with native alpha and exact DDS decode evidence.
The parent accepted the native and 4x artwork review and wired the matching sprites; the profile markers still change no armour value.

The prior takeover's mission design scopes are retained explicitly: reconnect the pre-impact rail network and its saved industrial hub, and measure Ring 2 recovery with the 60 percent infrastructure/factory gates rather than introduce another abstract pressure score.
These are narrower than the first audit's wording demanding a railway in every damaged state, including places that never had one.
Objectives cover surviving affected holdings under current control, with separate control requirements on the captured industrial hub and reserved mission state.
The reason is to restore the network the impact broke and keep recovery possible during territorial change, while retaining concrete construction objectives instead of success from timer expiry alone.
These differences are recorded as design dispositions, not hidden behind a claim that the first audit's literal checklist was fully implemented.

## Source references

Installed `documentation/effects_documentation.md`: country events 2943-2967, damage units 3417-3436, news events 5053-5077, building removal 5838-5873, building setter 6621-6629.
Installed `documentation/triggers_documentation.md`: `any_of_scopes` 1531-1543 and `check_variable` 2110 onward.
Installed `documentation/script_concept_documentation.md`: Script Constants 215-244; `common/script_constants/documentation.md`: first-entry schema 12-31.
Offline `Event modding - Hearts of Iron 4 Wiki.md`: Triggering 117-150; `Effects - Hearts of Iron 4 Wiki.md`: news effect 901, provincial selector 3614-3616 and setter example 3669-3677.
Offline `Scopes - Hearts of Iron 4 Wiki.md`: ROOT/PREV/FROM 255-260; `Data structures - Hearts of Iron 4 Wiki.md`: variables 425-449 and arrays 1076-1105.
Offline `Decision modding - Hearts of Iron 4 Wiki.md`: native cost triplets 308-329; `Localisation - Hearts of Iron 4 Wiki.md`: recursive context 353 and namespaces 531 onward.
Offline `Building modding - Hearts of Iron 4 Wiki.md`: network exception 362; installed `00_buildings.txt` declares the ordinary province caps and `01_landmark_buildings.txt` declares landmark caps.
Vanilla precedents include `events/NewsEvents.txt:1542-1560` for `show_major`, `common/scripted_effects/SOV_scripted_effects.txt:8286-8294` for a state-owned province selector, and the existing project camp-selector zeroing pattern.
The ordinary-variable 2.147-million overflow claim from the second review is rejected: offline Data structures 427 documents approximately 2.147 billion; the smaller limit belongs to deprecated manpower readers.

MCP reference reads retain revisions in the completion handoff and final status.
The parent retrieved the installed country-event section at revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`, the wiki Triggering section at `96327b896298420d84058394a44ed08be7eb518726b8f207b392fea71f05d43d`, and the wiki news effect at `997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c`.
