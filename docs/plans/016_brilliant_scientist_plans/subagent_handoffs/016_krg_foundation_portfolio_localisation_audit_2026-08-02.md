# Event 016 Kruger State foundation portfolio localisation audit

Date: 2026-08-02

## Scope

This audit covers the presentation tranche for `chaosx.brilliant_scientist_krg.1` through `.4`, including the four event descriptions, the origin and portfolio scripted-localisation helpers, the nine portfolio clause keys, and the related Event 016 documentation. The audit is localisation-only. No gameplay source, decision, focus, event ID, asset, or spreadsheet surface was edited.

## Changed files

None. This was an audit-only pass and no concrete localisation defect was found that justified a patch.

## Missing key list

No missing keys were found in the scoped Event 016 KRG set. The four report descriptions, five origin-clause outputs, and nine portfolio-clause outputs were all present in `localisation/english/016_brilliant_scientist_kruger_state_decisions_l_english.yml` when inspected.

## Duplicate key list

No exact-case duplicate keys were found in the target file or across the fifteen `localisation/english/016_*.yml` files. The target file contained 388 keys and the Event 016 set contained 2,612 keys in total. A case-insensitive pre-existing pair named `KRG_XENOBIOLOGICAL_ASCENDANCY` and `KRG_xenobiological_ascendancy` is outside this tranche and was not classified as a target duplicate.

## Scripted localisation issue list

The observed `GetBrilliantScientistKrgOriginClause` and `GetBrilliantScientistKrgPortfolioClause` helpers use ordered `defined_text` blocks with a final default branch. The portfolio order is deterministic: temporal, alien arms, xenobiological synthesis, robotics, cloning, paleogenetics, teleportation, biological weapons, then default. This matches the existing runtime package reconstruction and deliberately presents one highest-priority surviving family rather than exposing every active flag.

The four events are `country_event` blocks fired directly from KRG decisions, so the helper's current-country scope is safe for `.1` through `.4`. The helper reads the eight existing active-family flags created by the carried-ledger runtime rebuild and introduces no new flag or effect.

During this audit, a concurrent workspace change removed the tracked `common` subtree from the working tree, including `common/scripted_localisation/016_brilliant_scientist_kruger_state_scripted_localisation.txt`. The helper conclusions above are based on the last observed file content and the runtime source review completed before that deletion. I did not restore or reset the deletion. The parent agent must reconcile that concurrent change and confirm that the helper file is present before relying on the tranche.

## Dynamic text opportunities

No required dynamic-localisation patch was identified. The existing helper already supplies formation origin and the highest-priority surviving project-force family. Adding all active families, exact stages, costs, or route names would expose implementation state and would contradict the presentation-only contract documented in `docs/events/016_brilliant_scientist/systems/kruger_state_decisions.md`.

## Cross-surface mismatch notes

The four descriptions retain the existing origin helper and append the portfolio helper once. The wording describes institutions and public dilemmas without listing effects, rewards, costs, route names, raw flags, or exact project stages. It is consistent with the linked Kruger State decisions documentation and the existing origin-flavour handoff.

Static source lengths do not indicate an obvious event-window overflow. The longest resolved combination is approximately 650 characters against the vanilla event-window description area. A live render was not performed, so visual wrapping remains an in-game verification boundary rather than a confirmed defect.

## File encoding concerns

The target YAML was verified as UTF-8 with BOM. It contained no `:0` keys or leading-space keys, and the appended helper references had balanced localisation brackets. Scripted-localisation `.txt` syntax was reviewed as Clausewitz text rather than YAML, so the YAML BOM check does not apply to that file. The current concurrent deletion prevents a fresh encoding check of the scripted-localisation file until it is reconciled.

## Recommended fixes

- No localisation text patch is recommended for the inspected tranche.
- Reconcile the concurrent deletion of `common/scripted_localisation/016_brilliant_scientist_kruger_state_scripted_localisation.txt` and verify that both KRG helpers remain wired before merge. Do not blindly restore the file if another agent intentionally moved it; resolve the ownership change against the parent plan.
- If a future design requires multiple surviving project families in one report, update the event specification first and then add a deliberately designed multi-clause helper rather than changing this selector implicitly.

## Validation performed

- Read the Event 016 event and decision sources and verified the four report descriptions, fire paths, and current-country scope.
- Compared all eight portfolio flag names with the existing project-force runtime rebuild and confirmed that no new flag is referenced.
- Checked target and Event 016 localisation key coverage, exact-case duplicates, `:0` keys, leading-space keys, and helper bracket balance.
- Verified the target YAML UTF-8 BOM.
- Reviewed vanilla event-window dimensions for a static overflow estimate.
- Ran a read-only `hoi4.event_inspect` scan for `chaosx.brilliant_scientist_krg.1`. The scan returned `EVENT_INSPECTED_PARTIAL` with artifact URI `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5aa2951543c32cb393db49f56053c34586a5fed4a81ecfb5a221601dbb797ba6/f0b36e37809cc906109f4b6acc2108fe85bd9b6cb97ed776dc632839d32ebac5/event-scan-582f1ba583a9.json` and reported inline-file truncation. Direct source inspection remains authoritative for this audit.

## Skipped meaningful validation

No game launch or live event-window render was performed, as required by the repository workflow. The read-only MCP scan was partial because inline files were truncated. The concurrent `common` subtree deletion also prevented a final fresh read of the scripted-localisation file. These are verification limits, not identified wording defects.

## Unresolved wording decisions

No unresolved player-facing wording decision remains for this tranche. The intentional choice to show one highest-priority portfolio family is documented above and in the existing Event 016 decisions system document.

## Plan handoff

No additional plan was written. This file is the complete localisation audit handoff for the bounded tranche.
