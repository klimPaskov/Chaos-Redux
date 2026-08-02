# Event 020 localisation incremental audit handoff

## Scope and result

This audit covers the ten `localisation/english/020_*.yml` files, the Event 020 event consumers in `events/020_black_death.txt` and `events/020_black_plague_weaponization.txt`, the seven new RTA and RTX route-operation call sites, and the Event 020 scripted-localisation definitions used by the current text surfaces.

The new `chaosx.nr20.78` and `chaosx.nr20.79` surfaces are complete and resolve all route and policy branches.

## Changed files and keys

- `localisation/english/020_black_plague_reports_l_english.yml`: `chaosx.nr20.78.d`, `chaosx.nr20.79.t`, and `chaosx.nr20.79.a`.
- Before: `The carrier has committed another route operation, and the warrens are already moving to make it part of their living map.`
- After: `The carrier has completed a route operation, and the warrens are already moving to make it part of their living map.`
- Before: `A Decree in the Royal Court` and `Record the decree.`
- After: `The Royal Court's Policy Takes Shape` and `Record the policy.`

The fallback no longer implies that an earlier route operation necessarily occurred, which keeps the text accurate if the variable is absent or unexpected.

The `.79` title and option now cover Crown Tithe, Council Audit, and Hierophant Broadcast without calling every policy operation a decree.

## Missing key list

- No missing Event 020 event title, description, option, decision, focus, or scripted-localisation key was found.
- `chaosx.nr20.78` resolves `t`, generic `d`, seven route-specific `d` branches, and `a` in `events/020_black_death.txt`.
- `chaosx.nr20.79` resolves `t`, generic `d`, three policy-specific `d` branches, and `a` in `events/020_black_death.txt`.

## Duplicate key list

- No duplicate key exists across the ten Event 020 localisation files.
- No Event 020 key collides with another key anywhere under `localisation/`.

## Scripted-localisation issue list

- No new scripted-localisation selector is required by `.78` or `.79` because their route and policy branches use ordinary event description keys selected by event triggers.
- Existing Event 020 methods `GetBlackPlagueRatBroodCategoryDescription`, `GetBlackPlagueRatKingDefeatActorName`, `GetBlackPlagueSharedSupportAmount`, `GetBlackPlagueSharedMotorizedAmount`, and `GetBlackPlagueSharedFuelAmount` resolve to definitions under `common/scripted_localisation/`.
- No unresolved bare scripted-localisation token was found in the ten Event 020 English files.

## Dynamic text opportunities

- The `.78` event has route-specific branches for Citadel Stockpile, Migration Lanes, Tide Manifest, Rail Breach, Distributed Nests, Dominant Alpha, and Emergent Route Memory, so it does not need a new dynamic route-name helper.
- The `.79` event has route-specific branches for Crown Tithe, Council Audit, and Hierophant Broadcast, so it does not need a new dynamic policy-name helper.
- The generic `.78.d` and `.79.d` fallbacks remain intentionally static because they are only safety branches for an absent or invalid operation value.
- Existing shared-response cost rows still contain a few literal civilian-factory counts while the decisions use `civilian_factory_use`; this is a future centralisation opportunity outside the new `.78` and `.79` text.

## Cross-surface mismatch notes

- The route and court depth docs describe the same seven operation reports and the same branch names as the new localisation, with no remaining wording mismatch found in `docs/events/020_black_plague/rat_route_depth.md`, `docs/events/020_black_plague/rat_king_depth.md`, or `docs/events/020_black_plague/overview.md`.
- The seven RTA and RTX completion call sites set the matching enum variable before firing the event, and the enum values in `common/script_constants/020_black_plague_rat_constants.txt` match every localisation branch.
- Existing Event 020 reports contain older semicolon-separated sentences in unrelated keys, but the new `.78` and `.79` keys contain no semicolons, em dashes, hidden-route leaks, or implementation-history wording.

## File encoding concerns

All ten Event 020 English localisation files are valid UTF-8 with BOM and contain no replacement characters.

Several files use mixed LF and CRLF line endings, and Git reports the normal LF-to-CRLF normalization warning for the modified reports file, but no encoding failure was found.

## Validation

The focused audit counted 1,088 Event 020 keys, found zero duplicate keys across Event 020 or repository-localisation collisions, parsed all 195 Event 020 event title/text/name references with zero missing keys, checked all new `.78` and `.79` references, verified all ten BOMs, checked quoted one-line localisation syntax and colour-marker balance, and resolved all 270 `constant:` tokens used by Event 020 English text against the script-constant sources.

No Hearts of Iron IV executable was launched, and no live GUI or in-game validation was run because those checks are parent/user-owned.

## Unresolved wording decisions

No unresolved wording decision remains for `.78` or `.79` after neutralising the generic `.78.d` fallback and the `.79` title and action across all operation branches.

## Recommended parent actions

Keep the fallback wording change and review the existing unrelated semicolon style violations during a broader Event 020 prose pass if desired.

Handoff path: `docs/plans/020_black_plague_plans/subagent_handoffs/2026-08-02_event20_localisation_incremental_audit_handoff.md`.
