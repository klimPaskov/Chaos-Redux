# Gods of Africa bounded registry and review cadence

Disposition: implemented in source, with engine lifecycle and specialist audit evidence still incomplete.
Acceptance basis: the user's active goal requires independent enrollment of every valid major or player through a bounded owner registry and forbids recurring unrestricted world scans.

## Defects and resulting behavior

The previous `gods_of_africa_review_registry` ran `every_country` during recurring review.
The initial candidate census retained only countries already major or player-controlled, so replacing that scan alone would have lost later eligibility for minors.
Review also ran from both the 30-day owner tick and the separate 90-day `.607` clock.
Archival removed entries from the participant array while review iterated that array.

The one-time census now consumes vanilla's `global.countries` array and retains ordinary known country scopes, including minors, capitulated countries, and landless tags.
Actual participant eligibility still requires existence, no capitulation, and major or player control, while excluding the unifier and special or actual nonhuman actors.
The census and bounded transaction callbacks share idempotent candidate insertion, guarded by membership and the existing 640 cap.
The installed vanilla and mod tag files contain 609 distinct static definitions as counted on 2026-10-03.
Release, puppet, and peace-conference callbacks retain their individual country scopes, while an additive `on_government_change` callback remembers the changed country, including both civil-war sides.
No periodic global on-action was added.

The private `.607` clock is the sole recurring registry reviewer.
Activation sets its first due day 90 days ahead, and a due review advances that date and schedules one successor.
An early or duplicate delivery does not consume the receipt or schedule another event.
An invalid host clears the clock receipt without rescheduling.
Archival uses a separate participant snapshot and clears it after the pass, so removal cannot alter the iterated list.

## Changed implementation

- `common/scripted_effects/012_africa_gods_effects.txt`: bounded review, archival snapshot, `gods_of_africa_remember_candidate`, callback enrollment, activation due date, and guarded `.607` scheduling.
- `common/scripted_triggers/012_africa_gods_triggers.txt`: `gods_of_africa_candidate_is_valid`, `gods_of_africa_candidate_can_be_remembered`, and the existing participant predicate's retained eligibility checks.
- `common/scripted_effects/012_africa_world_order_effects.txt`: the existing one-time candidate census.
- `common/on_actions/012_africa_gods_on_actions.txt`: a country-local government-change witness.
- `events/012_africa_gods_of_africa.txt`: `.607` delegates receipt consumption to its guarded owner effect.
- `docs/events/012_africa/gods_of_africa.md` and Part 3 of the Event 012 spec: candidate coverage and the authoritative review cadence.

`gods_of_africa_remember_candidate` runs in a known country scope and requires the authoritative `africa_host`, an initialized candidate count, ordinary candidate identity, non-membership, and remaining capacity.
It adds that country scope and increases the count once, without spending resources or enrolling an ineligible country.
It has no fallback host or default count.
Use it from the existing one-time census, or call `gods_of_africa_try_register_participant = yes` from a documented country transaction after the census.

## References and source baseline

The baseline checkout HEAD was `edb861acd2e566a625d91189c9a1dc36f87bc24f`.
The Gods effects/triggers baseline hashes were `6c5c9660f69087695ecbf2ee0dcb66a9891abb330cba207d5ec019fe5f0db8fe` and `5816f4f9e6c90e4fd1472ca8c650af3a3a0c0eb3b3335f1775bad704e67fbab5`.

- Installed `documentation/effects_documentation.md:4296-4311`, revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`: `for_each_scope_loop` changes scope to each array entry.
- Offline `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md:1214-1261`, revision `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`: array iteration, scope handling, and the restriction on removing elements from an iterated array.
- Installed `documentation/triggers_documentation.md:5672-5685`, revision `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29`: `is_in_array` membership.
- Installed `documentation/dynamic_variables_documentation.md:972-976`, revision `538525747f0c285062c9ce8db14b4e07c3cf6bac1013115fa4f57291cb4ebdda`: the global `countries` array includes non-existing countries and is not a DLC-owned list.
- Installed `common/on_actions/_documentation.md:20-29`, revision `876be96cab02a3eaa9a133891bea5f963f8980aa4a794f759c1b30f87d2663c4`: supported politics callbacks.
- Offline `paradox_wiki/On actions - Hearts of Iron 4 Wiki.md:206-243`, revision `6822adc85a374a1c1364f2def6f32c6d66da9fb0280319ddd6af4b84b33d882a`: government changes include both civil-war sides.
- Vanilla `common/on_actions/00_on_actions.txt:1296-1322` supplies the country-scope government-change precedent.
- Vanilla `common/scripted_effects/COG_scripted_effects.txt:197-219` uses `global.countries` to enter country objects that do not currently exist, with a live `source_lookup` result at revision `095fa9114929e12a727315be6492de68be489da21218ef4b7c778c88afd4232e`.

The current reference routes were exposed and called, with relevant sections read through revision-bound `reference_read` or directly from their cited local files.
No Paradox web page was accessed.

## Source scenario review

| Case | Source result and limit |
| --- | --- |
| Existing minor later becomes major/player | Its known country scope remains a candidate, then passes live enrollment on the next bounded review. |
| Landless tag is released | The initial country-scope pool or supplied release callback remembers it, and actual enrollment still checks existence and eligibility. |
| New civil-war side | Government-change and existing transaction callbacks test only the supplied country, with duplicate insertion blocked. |
| Candidate callback repeats | Membership rejects a second insertion and count increment. |
| Effect-chain ROOT differs from the unifier | Candidate exclusion compares the authoritative host pointer, so a separate eligible ROOT is not skipped. |
| Candidate or participant cap reached | The existing 640 gate prevents further insertion, without adding another scan. |
| Two adjacent participants are invalid | Archival iterates the independent snapshot and can remove both from the live array. |
| `.607` arrives before its due day | No review, receipt consumption, or successor event is executed. |
| Duplicate `.607` deliveries arrive on the due day | The first advances the due date, so the second cannot start another review cycle. |
| Host is lost or generation invalid | The active-host gate rejects review and rescheduling. |

These results are source-contract analysis, not observed campaign execution.
The unchanged cap can still be exhausted by an unusually large dynamic-country population, and maximum decision-row density remains unverified.

## MCP and specialist evidence

The `.607` baseline trace returned `EVENT_INSPECTED_PARTIAL`, revision `f996ec9d3ed170e3a653534ac6f00472921e5d4594e0e8a1153ad61992a0d9f5`, with passing focused validation but zero helper projections.
Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6544973ffb41ffd4016ff27f736807dd51a997f0826b23fb6cc9a8031b92e7cd/ca73c27fe21d89bd600ada47921fc5a45ca42f0f857033c0623ff9f075fd10b2/event-trace-f996ec9d3ed1.json`.
The selected `.607` comparison against that baseline and the post-change state render both returned tool-call errors: `timed out awaiting tools/call after 600s`.
No comparison or render artifact was returned, and neither request supplies lifecycle acceptance.
No opaque job handle was supplied, so the status of any underlying server computation cannot be established from those call errors.
The scripted-system, decision, and weighted-logic specialists failed with `workspace routing discovery timed out`, so those mandatory audits are not complete.
The localisation specialist returned its separate audit, and its assigned text corrections remain a separate tranche.
No AI score, cost, doctrine tuning, asset, catalog field, or accepted route was simplified by this registry correction.
