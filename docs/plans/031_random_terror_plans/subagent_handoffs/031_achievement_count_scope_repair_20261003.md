# Event 31 achievement active-state count repair

## Disposition and acceptance basis

Disposition: implemented for the bounded count repair.

The active Event 31 goal explicitly requires one global firing across several governments, complete achievement tracking, and multiplayer-safe handling.

This correction preserves the accepted count threshold and changes only the country receiving the count.

## Defect and repair

`random_terror_achievement_count_active_states` zeroed the caller country's counter, iterated its owned active states, and then incremented `ROOT`.

The incident path calls the achievement ledger from `CONTROLLER` inside `random_terror_apply_incident`, which itself can execute for a country different from the global entry event's root country.

`ROOT` remains the root of the enclosing engine block, so the previous write could credit the host and leave the affected government's freshly zeroed count at zero.

The helper now increments `OWNER` from each state enumerated by `every_owned_state`.

All enumerated states are owned by the caller country, so the destination matches the country whose counter was zeroed even when the event root is another country.

Changed file: `common/scripted_effects/031_random_terror_achievement_effects.txt`.

Changed identifier: `random_terror_achievement_count_active_states`.

The change does not alter any AI weight, probability, cost, threshold, or achievement condition.

## Reference evidence

The connected tool list on 2026-10-03 did not expose `hoi4.reference_context`, `hoi4.reference_search`, `hoi4.reference_read`, or `hoi4.source_lookup`.

The relevant local sections were read directly under the fallback specified by AGENTS.md.

| Source | Read section | Revision |
| --- | --- | --- |
| `paradox_wiki/Scopes - Hearts of Iron 4 Wiki.md` | Lines 252–270, especially ROOT, PREV, OWNER, and CONTROLLER | SHA-256 `18EF5249E4991F5427ECA9EC4A2F66DD47F51E26A491C730ADC622F1F5DB1B49` |
| `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md` | Lines 107–133, country/state flags and targeting | SHA-256 `62273F37ED30E5479ACB331A8973F48DADC1867C4913C8A940E3E790E7AF32D4` |
| `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md` | Lines 2343–2360 for `add_to_variable` and 4076–4095 for `every_owned_state` | SHA-256 `2CDC93D26775990468EED167442F7A416B13059FB8FE07D139B54250B79209AF` |
| `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/scripted_effects/ETH_scripted_effects.txt` | Lines 595–619, country-owned state iteration entering state scope | Installed vanilla precedent |

## Validation and limits

Parent source review traced the caller from `random_terror_apply_incident` into `CONTROLLER`, then the achievement ledger and count helper.

The three-state case now credits the caller three times through the three owned states instead of crediting a possibly different event-root country.

No live-game claim is made.

The full achievement audit remains unresolved because the named architect failed before execution with `workspace routing discovery timed out`.

## Open findings from the wider achievement review

The tag-switch helper still sets a global disqualification flag, and the campaign-validity predicate reads it for every player country.

That can disqualify unrelated multiplayer participants when one player changes country.

The daily guard detects the abandoned human country but does not establish a player-specific origin-to-destination identity transaction.

This finding requires a complete replacement that preserves tag-switch anti-cheese protection for the switching player and eligibility for unrelated players.

The original-capital state marker is also shared between country ledgers and requires owner-specific identity verification during transfers and actor recycling.

These open findings prevent achievement-package completion and are not resolved by the active-state count correction.
