# Event 012 localisation bounded wording audit — 2026-08-02

## Scope

Audited Event 012 English localisation and scripted localisation for missing keys, duplicates, stale implementation-facing wording, public country-name exposure, scripted localisation coverage, portrait/council wording, and UTF-8 BOM encoding.

## Bounded patch

Changed `localisation/english/012_africa_world_order_l_english.yml`.

Changed keys:

- `africa_world_order.8.d`: removed the implementation-facing qualifier “bounded” from the Scramble response roster sentence.
- `africa_select_scramble_coalition_member_target_desc`: replaced “bounded intervention roster” with “intervention coalition” while preserving the selection and action meaning.

Changed `localisation/english/012_african_union_l_english.yml`.

Changed keys:

- `africa_priority_member_refresh_natural_disaster_targets_desc`: removed “bounded” from the player-facing nature-action description.
- `africa_priority_member_natural_disaster_ai_cycle_desc`: replaced “package AI” with “the priority member's court” so the visible description names an in-world actor rather than an implementation layer.

No dynamic localisation was added or fixed by this patch. Existing dynamic action-cost and nature-invocation localisation remains wired.

Before the patch, the four strings exposed internal scope/implementation terms. After the patch, they describe the same roster, coalition, target refresh, and AI action in player-facing language without changing gameplay meaning.

## Audit results

- Missing Event 012 localisation keys: none found across the 17 English files.
- Duplicate key groups: none found. Current scan covers 4,201 unique keys.
- Scripted localisation issues: none. The three Event 012 scripted-localisation files contain 41 unique defined-text names and 1,188 literal localisation-key references; all references resolve to Event 012 English keys.
- Unresolved custom scripted-localisation methods in Event 012 English localisation: none after allowing the vanilla `GetName`, `GetNameDef`, `GetNameDefCap`, and `GetAdjective` methods.
- Direct public-country tag exposure: none found. Public package names use direct display names or scripted display-name keys; no `GetTag` or raw-tag references were found in Event 012 localisation.
- Female/council portrait wording: no mismatch found. Female sovereign keys for Aksum, Nubia, and Merina are distinct from the separate council-party keys. The generated fictional portrait handoff contains no female or council portrait, so no additional wording was needed.
- UTF-8 BOM: all 17 Event 012 English localisation files begin with UTF-8 BOM bytes.

## Cross-surface and unresolved wording notes

The public priority-package display names and `GetAfricaPriorityPackageName` branches agree. Dynamic action-cost, blocked-cost, duration, and natural-invocation keys remain present and referenced. “The King of the Zulu” remains an owner-level idiom decision from the earlier audit and was not changed here. Historical “forced settlement” and “forced labour” wording remains an owner review item; no gameplay-connected text change was justified in this bounded pass.

## Validation

Ran a key/duplicate/BOM scan over all Event 012 English localisation files, a scripted-localisation definition/reference scan, and a stale-phrase/public-tag check after the patch. `git diff` was limited to the four changed keys in the two localisation files plus unrelated pre-existing working-tree edits from other agents; no scripted-localisation file was changed by this audit.

Skipped live-game validation because repository instructions reserve Hearts of Iron IV runtime testing for the user.

No new plan handoff was required; the wording issues were local and did not reveal a missing mechanic.
