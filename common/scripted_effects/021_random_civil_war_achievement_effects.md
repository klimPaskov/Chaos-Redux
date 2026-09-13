# Event 021 historical achievement receipts

These helpers own country-local capital continuity and external-capitulation receipts.
They do not create a country, modify Event 006 accounting, choose weighted outcomes, or iterate the world.

## Opening history

`event021_begin_achievement_history` runs in the original host after the core opening plan validates and the country is marked active.
It requires the original-capital pointer captured by `event021_parent_prepare_crisis_identity` before the split.
It records the actual decisive-war capital only if owned and controlled by the host, accepting the original capital or a populated, infrastructurally viable replacement using existing opening tuning.
Missing or invalid capital evidence fails closed through `random_civil_war_decisive_capital_lost`.
It resets the previous crisis's settlement-recorded, reconstruction-complete, internal-resolution, victory, and historical failure receipts, without clearing completed achievement flags or recurrence memory.
It also releases old cleanup-complete/requested, settlement pending/signed/resolved/talks commands, and completed settlement/reconstruction UI phases so a recurrence exposes its own actions and cannot consume an earlier offer.
This command reset does not erase persistent agreement obligations or violations; the treaty lifecycle must record those independently before any later reset or cleanup.
It seeds the authority minimum by calling the shared authority-band updater.
Example: `event021_begin_achievement_history = yes` is called by `event021_random_civil_war_commit_opening`, never by failed preflight.

## Continuous capital and authority checks

`event021_record_capital_continuity` runs in an active country with committed achievement history, before all internal fronts resolve.
It inspects only that country's stored decisive-capital state and latches loss if control or ownership is lost.
Recovery cannot clear the failure.
The existing bounded review calls it, and `on_state_control_changed` calls it on `FROM`, the former controller, so a loss and recapture between scheduled reviews remains recorded.
Chain-local targets `random_civil_war_history_country` and `random_civil_war_history_capital` isolate state/country references from event ROOT.

`event021_update_authority_band` lowers `random_civil_war_minimum_authority` whenever active unresolved history records a lower value.
The existing Collapse receipt remains latched, and Hold the Center requires the historical minimum to remain above the centralized Collapse threshold.

## External capitulation

`event021_record_external_capitulation` is called only from `on_capitulation`, whose installed vanilla contract defines ROOT as the defeated country and FROM as the winner.
It latches external-war failure for an unresolved Event 021 host with a qualifying opening war, unless the winner is a registered opposition actor or shares the same crisis ID.
It does not infer that a later recovered country was never defeated.
Settlement receipt refresh does not infer external defeat from `has_capitulated`; an internal claimant's victory must not be misclassified as an external capitulation.

## Origin and durable awards

The parent identity preparation captures `random_civil_war_event6_identity_at_opening` for an already existing normal human country with either ordinary Independence Wave origin or a recorded Event 021 package origin.
Fractals of Sovereignty uses that opening snapshot; A Flag of Our Own still requires Event 021 origin.
Player-at-opening flags are refreshed for each crisis so later tag control cannot inherit stale original-government eligibility.
The shared achievement registry accepts each route's current ready predicate or its previously earned flag while normal achievement eligibility remains valid.
Opening resets do not erase earned flags.

## Actor disqualification and ordinary succession

`event021_inherit_achievement_disqualification` runs for all five opening-receipt paths and committed original-host history.
Debug mode, force-trigger entry, manual scenario setup, and the bound original host's existing disqualification propagate as sticky country flags to both ordinary and Event 006 actors.
The effect never clears a previous disqualification.

`event021_inherit_successor_achievement_history` runs on the ordinary winning claimant before the former host is cleaned or annexed.
The caller explicitly binds `random_civil_war_history_predecessor`; the helper requires matching crisis IDs and committed predecessor history.
It copies the original core-state array, opening-state count, and original-capital pointer, and preserves external-war, external-capitulation, harsh-settlement, multi-front, and disqualification facts.
It does not confer original-player-government status, Event 006 identity, capital-continuity eligibility, or an achievement already earned by another country.
The predecessor white peace names the actual successor through a local event target rather than event ROOT.
Unresolved front registry transfer and signatory succession are separate lifecycle requirements and remain unverified.

## Evidence and remaining boundaries

Source references: installed vanilla `common/on_actions/00_on_actions.txt`, `on_capitulation` and `on_state_control_changed`; installed `documentation/effects_documentation.md`, variable and array scope effects; offline `paradox_wiki/On actions - Hearts of Iron 4 Wiki.md`.
These callbacks add no daily, weekly, or monthly whole-world iteration.
Full successor lifecycle, full recurrence-generation reset, all-signatory settlement history, and event-chain lifecycle certification remain acceptance work; these narrow helpers alone do not certify all six achievements.
