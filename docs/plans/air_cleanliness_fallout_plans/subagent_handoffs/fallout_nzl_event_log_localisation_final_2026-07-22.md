# Fallout NZL Event Log localisation handoff

Date: 2026-07-22
Scope: dormant Fallout NZL country-memory Event Log rows, detail strings, and Fallout world-end package-card presentation.

## Current-source reconciliation

This historical handoff predates the Fallout consequence boundary correction.
The consequence is not an Event Details row, evolution, ordinary event-log row,
or world-end details card. The composite key and branch described below are
retired. The remaining NZL surfaces are post-consequence country-memory history
and must stay dormant until their own activation proof is accepted.

## Changed files

- `localisation/english/fallout_nzl_event_log_l_english.yml`
- `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`

`common/scripted_localisation/chaosx_scripted_localisation_debug.txt` was audited but not changed in this pass.

## Changed keys and behaviour

- `fallout_nzl.event_log.route.humanitarian`
- `fallout_nzl.event_log.route.isolation`
- `fallout_nzl.event_log.route.uncommitted`

Route labels are now adjective fragments. The card renders `the humanitarian course`, `the isolation course`, or `the uncommitted course`. Detail strings render `The humanitarian route guided the decision` and equivalent wording for the other routes.

- `fallout_nzl.event_log.card.partner_pair`
- `fallout_nzl.event_log.card.partner_present`
- `fallout_nzl.event_log.card.partner_absent`
- `fallout_nzl.event_log.card.aggressor_absent`

Partner and aggressor clauses now have grammatical relative clauses and concrete surviving-government wording.

- `fallout_nzl.event_log.card`
- `fallout_nzl.event_log.detail.opening`
- `fallout_nzl.event_log.detail.domestic`
- `fallout_nzl.event_log.detail.external_partner`
- `fallout_nzl.event_log.detail.external_no_partner`
- `fallout_nzl.event_log.detail.late`

The four detail surfaces use the corrected route sentence. The card still names Wellington, Auckland, Canterbury, Marlborough, and Otago and keeps the dynamic metrics, dates, actors, partners, and aggressor values.

- `fallout_nzl.event_log.card.composite`

The former nested key that combined a Fallout world-end details string with the
NZL package card is retired. It must not be restored because the Fallout
consequence has no public details surface.

- `GetEventsLogSelectedWorldEndScenarioDetails` in `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`

The Fallout consequence branch is absent. Any future NZL package view must be
opened only from a post-consequence country-memory context.

## Localisation audit

### Missing keys

None in the owned package surface. All 36 `fallout_nzl.*` localisation keys referenced by the allowed scripted-localisation files resolve. The two nested keys in `fallout_nzl.event_log.card.composite` also resolve.

### Duplicate keys

None in `fallout_nzl_event_log_l_english.yml`. The target scripted-localisation files have no duplicate `defined_text` names.

### Scripted-localisation findings

- Dedicated history ids 9101, 9102, 9103, and 9104 map to the four dedicated Fallout NZL names in both the shared Event Log name helper and the debug name helper. They do not borrow `chaosx.event_name.*` keys.
- The new `GetFalloutNZLEventLogHistoryRowResultLabel` comparisons are valid against the current parent effect change because `events_log_system_payload` is set to the result snapshot values 1, 2, and 3. The detailed payload remains in the private NZL payload array.
- Fallout row, detail, route, result, partner, aggressor, and package-card helpers all resolve to owned keys.

### Dynamic text opportunities

The package already exposes dynamic state names, metrics, dates, event actors, partner governments, and pirate aggressors. No additional dynamic value was required after the grammar and composite-key correction.

### Cross-surface mismatch notes

- The former world-end details mismatch is retired with the consequence details
  branch. No live localisation key named
  `chaosx.events_log.world_end.fallout.details` is required.
- Event 2 remains Zombie-only at the Event Log and catalog surface. A pre-existing Air Winter source event named `chaosx.fallout.2` was not changed by this localisation patch. This handoff does not claim that no raw Event 2 exists anywhere.
- No ordinary `chaosx.event_name.9101` through `chaosx.event_name.9104` mapping was found.
- No new `event_id = 9101` through `event_id = 9104` source event was found.
- `SCN-014` remains absent from the live implementation surface. Existing documentation and reservation constants only record the reserved identity.

### File encoding concerns

- `fallout_nzl_event_log_l_english.yml` starts with UTF-8 BOM `EF BB BF`, has 39 unique localisation keys, and contains no replacement characters.
- Both scripted-localisation files are valid UTF-8 plain text without a BOM, matching their existing script-file format. No replacement characters were found.

## Validation run

- Parsed the target YAML key format and checked duplicate keys.
- Resolved all 17 bracketed scripted-localisation calls in the package file against 108 event-log `defined_text` names and 2 debug `defined_text` names.
- Resolved both nested localisation references used by the composite key.
- Confirmed Wellington, Auckland, Canterbury, Marlborough, and Otago each occur five times in the package file. No stale candidate state names were found.
- Confirmed no semicolon, em dash, or en dash appears in the package localisation.
- Searched implementation files for ordinary dedicated-id name borrowing, new dedicated source event ids, and SCN-014 rows.

## Skipped meaningful validation

Hearts of Iron IV was not launched, as required. Therefore the selected world-end details GUI, nested localisation expansion, dynamic country scope rendering, and live Event Log filtering remain runtime-unobserved.

## Remaining risk and wording decisions

- The broader NZL package remains dormant and its runtime activation, save recovery, multiplayer behaviour, and GUI rendering are outside this handoff.
- `uncommitted` is intentionally rendered as a course adjective when no route flag is present.
- The composite presents the base Fallout description first and the NZL card second. Reordering is a presentation choice, not a missing localisation key.

This is a localisation handoff for the owned Event Log surfaces only. It is not a broader Fallout NZL completion claim.
