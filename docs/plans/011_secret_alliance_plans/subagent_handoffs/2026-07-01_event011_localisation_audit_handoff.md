# Event 011 Secret Alliance Localisation Audit Handoff

Date: 2026-07-01

Subagent scope: localisation audit and small local patch for Event 011 Secret Alliance.

## Required Reading

- `AGENTS.md`
- Offline wiki pages consulted for localisation/event/decision behaviour:
  - `paradox_wiki/Localisation - Hearts of Iron 4 Wiki.md`
  - `paradox_wiki/Event modding - Hearts of Iron 4 Wiki.md`
  - `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md`
  - Core repo-required pages for data structures, triggers, effects, modifiers, scopes, on actions, ideas, and AI
- Vanilla documentation consulted:
  - `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/loc_formatter_documentation.md`
  - `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/loc_objects_documentation.md`
- Repo skills:
  - `chaos-redux-events`
  - `hoi4-decisions-missions`
  - `chaos-redux-subagents`
- Event specs:
  - `docs/specs/011_secret_alliance_specs/README.md`
  - `docs/specs/011_secret_alliance_specs/specs/011_secret_alliance_spec_part_*.md`
  - Event 011 decision, runtime, AI, and tuning matrix files

## Files Changed By This Pass

- `localisation/english/011_secret_alliance_l_english.yml`
- `docs/plans/011_secret_alliance_plans/subagent_handoffs/2026-07-01_event011_localisation_audit_handoff.md`

No commit was created.

## Changed Keys

- `chaosx.nr11.1.t`
  - Before: `Secret Alliance`
  - After: `Unrelated Frictions`
- `chaosx.nr11.1.a.tt`
  - Before: stated that a hidden anti-target compact had begun operating.
  - After: marks the pattern for quiet observation without revealing the compact.
- `chaosx.nr11.22.a.tt`
  - Before: stated that the hidden compact grows broader.
  - After: refers to the pressure pattern growing broader.
- `chaosx.nr11.24.d`
  - Removed semicolon punctuation and kept the public-crisis description intact.
- `chaosx.nr11.40.d`
  - Removed semicolon punctuation and kept the suspicious timing description intact.

## Dynamic Localisation Added Or Fixed

No new scripted or dynamic localisation was added in this pass.

Already-present dynamic text was confirmed for `secret_alliance_category_desc`, including suspicion, evidence, preparedness, counter-network, known-member count, readiness, hostility, and cohesion variables. Custom decision cost keys also already had base, `_blocked`, and `_tooltip` variants.

## Missing Key List

None found after scoped validation.

The audit checked Event 011 references from:

- `events/011_secret_alliance.txt`
- `events/_chaosx_news.txt`, narrowed to `chaosx.news.11`
- `common/decisions/011_secret_alliance_decisions.txt`
- `common/ideas/011_secret_alliance_ideas.txt`
- `common/achievements/chaos_redux_achievements.txt`
- Event 011 `localization_key` entries in `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`
- `localisation/english/*.yml`

Result: `MISSING COUNT: 0`.

## Duplicate Key List

None found in the scoped localisation files:

- `localisation/english/011_secret_alliance_l_english.yml`
- `localisation/english/chaosx_event_names_l_english.yml`
- `localisation/english/chaosx_achievements_l_english.yml`

Result: `DUPLICATE COUNT: 0`.

## Scripted Localisation Issues

No Event 011 scripted localisation routing issue was found.

Confirmed in `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`:

- Event 011 evolution type routing is present for view, history, selected, and event-detail surfaces.
- Event details routing is present for `constant:secret_alliance_event_log.event_id`.
- Secret Alliance title/body defined_text blocks are present for history, view, selected, and event-detail surfaces.
- Global scripted localisation brace count is balanced: `open=3639`, `close=3639`, `delta=0`.
- No direct `§` or `£` formatting/icon characters were found in Event 011 scripted localisation additions.

I did not edit this scripted localisation file. Its Event 011 additions were already present in the working tree.

## Dynamic Text Opportunities

- `secret_alliance_category_desc` already does the most important work by exposing live state values without revealing member identities.
- Cost localisation has the expected base, blocked, and tooltip variants. The text is still prose-level rather than a fully numeric breakdown for every underlying helper cost. A later owning-script pass could add more exact scripted cost breakdowns if those values are intentionally exposed.
- The Event Log/Event Details text intentionally describes the hidden compact premise. If the parent wants stricter staging for the event catalog, that should be handled as a design decision because the current specs allow the details/catalog surface to describe the premise while early gameplay popups remain indirect.

## Cross-Surface Mismatch Notes

- Early event popup text no longer reveals the secret alliance premise before the player has public proof.
- Evolution I tooltip now avoids saying that the hidden compact exists.
- Event Log and Event Details text still use hidden compact language by design-facing/catalog context, not as immediate early-stage player notification.
- The reveal/news surface remains aligned with the public-crisis stage and does not expose member identities before reveal.
- `localisation/english/chaosx_event_names_l_english.yml` maps `chaosx.event_name.11` to `Secret Alliance`. This was already present in the working tree and was not edited here.

## File Encoding Concerns

- `localisation/english/011_secret_alliance_l_english.yml` lacked a UTF-8 BOM before this pass.
- The file was rewritten as UTF-8 with BOM.
- `localisation/english/chaosx_event_names_l_english.yml` already had a UTF-8 BOM.

## Behaviour Before And After

- Before: the first Event 011 popup title and option tooltip directly framed the situation as a Secret Alliance and hidden anti-target compact.
- After: the first popup reads as unrelated friction and quiet observation, matching the spec boundary that the compact should not be exposed before appropriate escalation.
- Before: Evolution I tooltip said the hidden compact had grown.
- After: Evolution I tooltip describes a broader pressure pattern.
- Before: two event descriptions used semicolons, conflicting with Chaos Redux event-style guidance.
- After: those descriptions use sentence breaks.

## Validation Run

- Scoped missing-key audit for events, decisions, ideas, achievements, Event Log scripted localisation references, Event Details, evolution details, news, and decision cost variants.
- Custom cost variant audit verified base, `_blocked`, and `_tooltip` keys for each Event 011 custom cost reference.
- Localisation syntax audit for `:0` and leading spaces before keys in the scoped localisation files.
- UTF-8 BOM check for the scoped localisation files.
- Scoped duplicate-key audit.
- Scripted localisation global brace-count check.
- Scoped direct-formatting check for `§` and `£` in Event 011 scripted localisation additions.
- Style/reveal grep for semicolons, em dashes, update-history wording, and early hidden-compact wording.

Skipped validation:

- No in-game rendering validation was run. This was a static localisation audit and small text patch only.

## Unresolved Wording Decisions

- Event Log/Event Details text still says `hidden anti-target compact` and `hidden compact grows`. I left this intact because the specs permit catalog/detail text to describe the event premise while early gameplay text remains indirect.
- Cost text is complete and player-facing, but not every abstract helper cost is shown as an exact numeric breakdown. This is not a missing-key issue.

## Recommended Fixes

Applied:

- `localisation/english/011_secret_alliance_l_english.yml`
  - `chaosx.nr11.1.t`
  - `chaosx.nr11.1.a.tt`
  - `chaosx.nr11.22.a.tt`
  - `chaosx.nr11.24.d`
  - `chaosx.nr11.40.d`
  - UTF-8 BOM encoding repair

No additional blocking localisation fixes are recommended from this pass.
