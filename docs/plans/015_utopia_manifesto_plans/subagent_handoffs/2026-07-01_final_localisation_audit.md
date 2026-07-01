# Event 015 Final Localisation Audit Handoff

Date: 2026-07-01

Scope: `utopia_manifesto` live localisation, scripted localisation, event-log/super-event selectors, Ledger GUI labels/tooltips, decision custom-cost text, focus/decision/idea/achievement/cosmetic/opinion key coverage, and stale old Event 015 wording.

## Result

Pass after one small localisation patch.

Localisation is clean for Event 015 completion from this audit's scope. I found no unresolved missing Event 015 keys, duplicate required keys, malformed `:0` keys, BOM problems, broken Event 015 scripted-localisation selector keys, old live `World Tension Subsides/Falls` references, or unresolved event-log/super-event selector localisation defects.

## Patch

Changed file:

- `localisation/english/015_utopia_manifesto_l_english.yml`

Changed key:

- `utopia_renunciation_vote_available_tt`

Before:

- `Requires enough stability to hold a national vote.`

After:

- `Requires high Overreach and enough stability to hold a national vote.`

Reason: `common/scripted_triggers/015_utopia_manifesto_triggers.txt` requires `utopia_manifesto_overreach_high = yes` inside `utopia_manifesto_can_pay_renunciation_vote`, and both the decision and Ledger GUI button use that trigger. The previous decision availability tooltip implied stability alone was enough, while the Ledger button tooltip already named high Overreach.

## Missing Key List

None after filtering non-localisation sprite selector references.

Audited surfaces included:

- Event title/desc/options from `events/015_utopia_manifesto.txt`
- Focus IDs, descriptions, and focus tooltips from `common/national_focus/015_utopia_manifesto_focus_tree.txt`
- Decision/category/mission IDs, descriptions, custom tooltip keys, and `custom_cost_text` triplets from `common/decisions/015_utopia_manifesto_decisions.txt` and `common/decisions/categories/015_utopia_manifesto_categories.txt`
- Idea IDs/descriptions from `common/ideas/015_utopia_manifesto_ideas.txt`
- Opinion modifier names from `common/opinion_modifiers/015_utopia_manifesto_opinion_modifiers.txt`
- Achievement names/descriptions/tooltips from `common/achievements/chaos_redux_achievements.txt`
- Cosmetic tag names/DEF/ADJ variants from `common/countries/cosmetic.txt`
- Ledger GUI labels/buttons/tooltips from `interface/015_utopia_manifesto_ledger.gui`
- Event-log details and numeric event name selector `chaosx.event_name.15`

False positives reviewed and excluded:

- `GFX_super_event_utopia_new_utopia` and `GFX_super_event_utopia_marked_bounds` are scripted selector sprite keys, not localisation keys.
- `visible` / `visible_desc` came from an overly broad category parser pass, not from a player-facing localisation requirement.
- `chaosx.event_name.utopia_manifesto` was an audit expectation error; the live event-log selector uses the existing numeric convention `chaosx.event_name.15`.

## Duplicate Key List

None for required Event 015 keys across English localisation.

No duplicates were found inside the directly relevant localisation files:

- `localisation/english/015_utopia_manifesto_l_english.yml`
- `localisation/english/chaosx_event_names_l_english.yml`
- `localisation/english/chaosx_gui_l_english.yml`
- `localisation/english/chaosx_achievements_l_english.yml`

## Scripted Localisation Issues

None found.

`common/scripted_localisation/015_utopia_manifesto_scripted_localisation.txt` selectors resolve to existing keys:

- `GetUtopiaManifestoRoute`
- `GetUtopiaManifestoGeography`
- `GetUtopiaManifestoPressure`

The Ledger GUI uses those scripted texts in:

- `utopia_manifesto_ledger_gui_status`
- `utopia_manifesto_ledger_gui_network`

Super-event image selectors in `common/scripted_localisation/chaosx_scripted_localisation_super_events.txt` point to sprite keys, and Event 015 title/body/action localisation for `chaosx_super_event.151.*` and `chaosx_super_event.152.*` exists in `015_utopia_manifesto_l_english.yml`.

## Dynamic Text Opportunities

No required dynamic-text patch remains.

Current dynamic readouts already cover route, geography, pressure, ledger values, project counts, friend count, League member count, and League confidence. Decision costs are static localisation backed by script constants; the audited cost strings match the current constant values and trigger gates. A future improvement could expose cost display variables for every decision cost if the parent expects frequent tuning churn, but that would require script support beyond this final localisation patch.

## Cross-Surface Mismatch Notes

Fixed:

- Renunciation Vote decision availability text now matches `utopia_manifesto_can_pay_renunciation_vote` and the Ledger Renounce button tooltip by naming high Overreach.

Reviewed and found aligned:

- Event-log details use `chaosx.events_log.window.event_details.utopia_manifesto`.
- Event name mapping uses `chaosx.event_name.15: "Utopian Manifesto"`.
- Achievement keys in `chaosx_achievements_l_english.yml` resolve for all Event 015 achievement IDs.
- Cosmetic tag localisation resolves for all Event 015 ideology variants.
- Recent arbitration outcome/opinion modifier names resolve:
  - `utopia_manifesto_boundary_compensation`
  - `utopia_manifesto_boundary_guarantee`
  - `utopia_manifesto_boundary_refusal`
- Ledger GUI button label and tooltip keys resolve.
- Decision availability/cost/result text matches the recent decision patches after the Renunciation Vote tooltip fix.

## File Encoding Concerns

None.

UTF-8 BOM check passed for:

- `localisation/english/015_utopia_manifesto_l_english.yml`
- `localisation/english/chaosx_event_names_l_english.yml`
- `localisation/english/chaosx_gui_l_english.yml`
- `localisation/english/chaosx_achievements_l_english.yml`

No `:0` keys or leading-space localisation key definitions were found in those relevant files.

## Stale Wording

No live old Event 015 references remain for:

- `015_world_tension`
- `world_tension_falls`
- `World Tension Subsides`
- `World Tension Falls`

The only `world tension` matches during broader shared-file searching were unrelated existing Tensions Rising/shared Event Log/Achievement strings, not Event 015 Utopian Manifesto text.

No Event 015 live localisation used implementation-history wording such as rework, newly added, hardcoded, or capped.

## Validation

Meaningful checks run:

- Parsed required localisation keys from Event 015 event, focus, decision, mission, category, idea, opinion modifier, achievement, cosmetic, scripted GUI, scripted localisation, Event Log, and Ledger GUI surfaces.
- Re-ran the coverage parser after the patch: `MISSING_COUNT=0`.
- Checked duplicate required keys across English localisation: none found.
- Checked BOM on the relevant English localisation files: all preserved.
- Checked relevant localisation files for `:0` keys and leading-space key definitions: no matches.
- Searched live Event 015 files for old `015_world_tension`, `world_tension_falls`, `World Tension Subsides`, and `World Tension Falls`: no matches.
- Compared Renunciation Vote script trigger, decision tooltip key, and Ledger GUI button tooltip after the patch.

Skipped validation:

- No in-game UI inspection was run. This was a localisation/scripted-localisation audit, and the task scope asked for repository-side key coverage and handoff evidence.

## Remaining Risks

- Cost strings are still static text rather than computed from script constants. They matched the current constants during this audit, but future balance changes must update localisation or add display-variable support.
- The final handoff is uncommitted because this is a dirty shared worktree with many unrelated and untracked Event 015 files.

## Recommended Fixes

No further Event 015 localisation fixes are required for completion from this audit.

Recommended future hardening only if the parent expects repeated cost tuning:

- Add script-supported display variables for decision costs, then rewrite cost localisation to use those display values instead of repeated numbers.
