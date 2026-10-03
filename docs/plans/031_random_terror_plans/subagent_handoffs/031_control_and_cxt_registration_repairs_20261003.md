# Event 31 country-control and CXT registration repairs

## Disposition and acceptance basis

Disposition: implemented for the country-local daily disqualification and CXT pending-registration corrections.

Full player-identity anti-cheese acceptance remains unresolved.

The active user goal requires multiplayer-safe actor handling, complete achievements, and exploit controls.

Current AGENTS.md requires CXT daily hooks to register and mark pending content without applying grants.

## Country-control correction

The previous tag-switch helper wrote a global disqualification flag, and the campaign-validity trigger read it for every player country.

A detected switch from one tracked country therefore invalidated unrelated countries' achievement eligibility.

`random_terror_achievement_record_tag_switch` now writes only country flags.

The existing daily country pass detects both transitions from a previously human country to AI and from a previously AI country to human control.

It disqualifies the changed country before updating `was_human_yesterday`.

Startup already marks the initial human countries, so their first daily pass remains eligible.

The campaign-validity predicate requires the historical human marker, preventing a newly entered country from passing eligibility before the daily reconciliation.

The guard remains independent from the event-system tag-management settings.

No additional world iteration or periodic on-action was introduced.

Changed files and identifiers:

- `common/on_actions/chaosx_on_actions_system.txt`, existing Event 31 guard inside `on_daily`
- `common/scripted_effects/031_random_terror_achievement_effects.txt`, `random_terror_achievement_record_tag_switch`
- `common/scripted_triggers/031_random_terror_triggers.txt`, `random_terror_achievement_campaign_is_valid`

## Source-predicate verification

The parent evaluated the actual guard and eligibility trigger source using a bounded boolean predicate model.

The result is preserved in `../evidence/achievement-control-source-model-20261003.json`.

| Case | Guard fires | Eligible before and after reconciliation |
| --- | --- | --- |
| Initial human country marked at startup | No | Yes |
| Unchanged second player country with the former global disqualification present | No | Yes |
| Abandoned country that is now AI | Yes | No |
| Newly entered country before daily reconciliation | Yes | No |
| Unchanged AI country | No | No |

The tag-switch helper has no global disqualification writes.

These results prove the source predicate behavior under the supplied flag/control inputs and do not prove observed multiplayer execution.

## Remaining identity limitations

The daily marker observes country-level human-versus-AI control, not a client's persistent identity.

It cannot detect a same-day round trip that returns to the original country before observation, or a swap between two countries that remain human-controlled throughout.

A newly human-controlled country entering outside startup is treated as a changed context, including a late participant assuming an AI country.

Those cases require explicit player-identity engine evidence or a stronger supported callback contract before the complete achievement anti-cheese requirement can be accepted.

No player identifier or undocumented callback was invented to conceal this gap.

## CXT registration correction

`chaosx_test_country_register_extension_effect` reports a new carrier with `chaosx_test_country_extension_registration_added = 1`.

Event 31 previously tested that value as greater than 1, which prevented its pending marker from being set for a new registration.

`common/on_actions/031_random_terror_cxt_on_actions.txt` now tests greater than `constant:random_terror_value.zero` and sets `chaosx_test_country_registered_sync_pending` directly.

The daily hook does not call package application, grant resources, create units, or fire Event 31.

Initial setup and the existing player-triggered Apply Registered Systems decision remain the application owners.

The modifier-free carrier remains `chaosx_cxt_extension_event031_random_terror`, and the setup effect remains `chaosx_cxt_extension_event031_random_terror_apply`.

The parent reviewed the registration helper's 0/1 output, the pending-only shared compatibility wrapper, the manual application effect, and Event 026's established registration-only hook.

## References and route gaps

The reference routes became exposed during this pass, but the requests did not return citations.

- `hoi4.reference_context`: `timed out awaiting tools/call after 600s`
- `hoi4.reference_search` for `is_ai`: `timed out awaiting tools/call after 600s`
- `hoi4.reference_search` for `on_startup on_daily`: `timed out awaiting tools/call after 600s`
- `hoi4.source_lookup` for the tag-switch helper: `timed out awaiting tools/call after 600s`

`hoi4.reference_read` had no valid returned citation ID and revision to read.

The parent read these pertinent local references directly:

- `paradox_wiki/On actions - Hearts of Iron 4 Wiki.md`, lines 85–125, startup and per-country daily scope
- `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md`, country/global flag scope and persistence
- Installed `documentation/triggers_documentation.md`, lines 5244–5253 for `is_ai` and 3624–3653 for `has_country_flag`
- Installed `documentation/effects_documentation.md`, lines 6730–6738 for `set_country_flag`
- Installed `common/on_actions/00_on_actions.txt`, startup effect structure and tag-scoped daily precedents
- `docs/testing/chaosx_test_country.md`, lines 87–105, registration-only daily hooks and manual application ownership

The earlier capital/count repair handoffs retain SHA-256 revisions for the same installed effects/triggers documentation and offline Data structures snapshot.

No successful current MCP engine or live-game validation is claimed.

## Preserved live-QA correction

The orchestrator's accepted scenario-list labels remain `chaosx.scenarios.entry.id.global_jihad: "#016"` and `chaosx.scenarios.entry.id.random_civil_war: "#018"`.

The user explicitly requires the `#0NN` form for scenario entry IDs to keep the list label on one line.

The stable catalog ID SCN-016 remains distinct from the compact UI label.

Neither localisation file was edited by this repair.
