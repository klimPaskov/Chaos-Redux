# Event 23 reference and save evidence, 2026-10-03

Disposition: reference coverage recorded; native delivery integration and reload conservation remain unresolved.

The previous turn made concrete source and runtime-asset progress, including the non-yield accident branch, Event 5 transfer brackets, and 21 achievement DDS replacements.
It was interrupted before the custody registry worker returned a final handoff.
The worker handle `01a0dc96-bd9f-7353-a969-f5a5cba79e6d` returned `not_found` on this continuation; retained edits therefore require a fresh recovery review.

## Reference routes

The connected tool list exposes `hoi4.reference_context`, `hoi4.reference_search`, `hoi4.reference_read`, and `hoi4.source_lookup` with their live schemas.
The parent called reference context for the event nuclear/custody surface (limit 12) and reference search for `launch_nuke add_nuclear_bombs` across installed, wiki, and script documentation.
Neither returned an inspectable response after more than 180 seconds; the parent stopped the read-only orchestration cell.
No coverage is inferred from exposure or from those requests.
The replacement AGENTS.md permits reading pertinent local sections when a reference route is unavailable, so the sections below were read directly.
`hoi4.source_lookup` was separately requested for `nuclear_strike` and returned `timed out awaiting tools/call after 600s`.
Recovery architect, native-delivery research, and probability-audit workers failed during workspace routing discovery before returning work.
The documentation and localisation recovery handles returned `not_found` at that check.
Subsequent direct inspection found the completed `023_achievement_asset_documentation_reconciliation_2026-10-03.md` handoff and its scoped documentation patch, so that evidence is retained and reviewed rather than treated as absent.
The parent reviewed the selected inventory, stable aliases, historical dispositions, and MCP limitations; the new assembly gameplay patch remains separately parent-owned.

## Local cited sections

| Source | Read section | SHA-256 revision |
| --- | --- | --- |
| Installed `documentation/effects_documentation.md` | `add_nuclear_bombs`, lines 1804–1812; `launch_nuke`, lines 4745–4759 | `2CDC93D26775990468EED167442F7A416B13059FB8FE07D139B54250B79209AF` |
| Offline `paradox_wiki/Effects - Hearts of Iron 4 Wiki.md` | Stockpile and detonation entries, lines 1516–1517 | `997DDB09BFD63EFB41A425149C46BD812D5F8953217A403386B2F6C85196AA0C` |
| Offline `paradox_wiki/On actions - Hearts of Iron 4 Wiki.md` | `on_nuke_drop` scope and example, lines 509–528 | `6822ADC85A374A1C1364F2DEF6F32C6D66DA9FB0280319DDD6AF4B84B33D882A` |
| Installed `common/raids/_documentation.md` | Raid actor/target gates, native unit requirements and resource collection, lines 68–192 | `EAC06474FCBDE3920523B9B49364F7797851C0CC45F4F0EF41321999A93BE43E` |
| Installed `common/raids/nuclear_raids.txt` | `nuclear_strike` definition and outcome precedent, lines 3–244 | `966408C81EBA9F5928ED352D5F95F6648977B23A8E12CE9AA2CD2CDBCA76256F` |

The installed `launch_nuke` effect is a detonation effect; its documentation does not assign aircraft or start a raid.
The installed `nuclear_strike` route selects native bomber units, requires at least ten strategic bombers and one nuclear device, starts from an airbase, and includes air superiority in its outcome calculation.
Native essential equipment is collected after raid creation; vanilla outcome detonations consequently use `use_nuke = no`.
Any Event 23 native-raid integration must respect that earlier payment and prevent a second scripted bomb debit.
The creation, authorization, target, concurrency, failure, and cancellation contract remains unresolved after the specialist's workspace-routing failure.

## Assembly-selection local references

The new decision-reference attempt first returned an input validation error because the question exceeded the live 160-character limit.
A corrected shorter request returned `timed out awaiting tools/call after 600s`; no reference coverage is inferred from either request.
Pending retrieval, the parent read installed `common/decisions/_documentation.md` lines 1–48, installed `common/decisions/AFG.txt` lines 1061–1109, offline `Decision modding - Hearts of Iron 4 Wiki.md` lines 514–589, offline `Data structures - Hearts of Iron 4 Wiki.md` lines 264–340, and installed `documentation/effects_documentation.md` lines 7888–7913.
The installed decision example confirms `state_target = any_owned_state`, FROM targeting and separate cancellation handling; the references distinguish temporary chain targets from persistent global targets and variables.
SHA-256 revisions are `5E7E686B5582F32C38D898D805E17171E88F3BFEEE4A030DEB1884F9726DE019` (installed decision documentation), `DABC91C3F7FB1810D64D91D07147E827068D42540326CE10554A0752EE48D7A7` (AFG), `7713B9BCEE5F3818D63AAFBD45D18E812A9173A7C59AB238384B57DB60DB6162` (offline decision page), and `62273F37ED30E5479ACB331A8973F48DADC1867C4913C8A940E3E790E7AF32D4` (offline data structures).
Installed effects documentation retains the revision listed above.
The parent also read installed raid outcome documentation lines 175–303 and raid-instance scope/effect documentation lines 546–657; targeted searches found no raid-start or raid-cancellation callback in the inspected installed documentation and on-actions.
That search is bounded source evidence, not proof that no engine capability exists.

## Existing save inspection details

The parent inspected only Event 23-relevant data in the existing local `trailer_110_events_fired.hoi4` through the read-only save inspector.
Metadata: `HOI4txt`, player USA, in-game date `1936.1.1.21`, engine `Operation Postern v1.19.2.0.a729 (5a45)`, save version 33, file size 118.7 MiB.
Commands were `info <save>` and `find <save> 'sov_nuclear_bombs|nukes' --in countries/SOV`.
The query found two native nuclear inventory entries with `amount = 0` and `nukes_ready = 0`, and no Event 23-prefixed fields in SOV.
This save supplies no evidence that the Event 23 opening, a device transaction, or save/reload conservation occurred.
No save was changed or copied into the repository, and no game was launched.
