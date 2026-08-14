# IW-051 Sakha Roster Source Correction

## Disposition

`SOURCE-CORRECTED / CENTRAL ADMISSION STILL HOLD-FAIL-CLOSED`

The package-local roster gate now admits only the source-backed `YAK_pavel_pevznyak` consumer for the Event 006 1936 Sakha opening. The vanilla `YAK_anatoly_pepelyayev` character remains part of the carrier's ordinary history, but the portrait audit found no valid 1936 Sakha role/date basis for using him as an Event 006 roster member.

## Changed source

- `common/scripted_triggers/006_independence_wave_sakha_package_triggers.txt`
  - `has_independence_wave_yak_command_roster` still requires the parent-owned `independence_wave_iw_051_identity_rights_cleared` flag.
  - Its roster predicate now requires `has_character = YAK_pavel_pevznyak` instead of accepting either vanilla YAK character.
  - No central adapter, attestation, preflight, scenario, deterministic Join, Event 005 origin, history, flag, portrait, or map source changed.

The corresponding package handoff was corrected so it no longer describes Pepelyayev as an approved Event 006 consumer.

## Evidence

- Vanilla `history/countries/YAK - Yakutia.txt` recruits both characters, so Pepelyayev remains a valid vanilla carrier character and was not removed from the game.
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw051_sakha_yak_portrait_source_research_2026_08_15.md` records Pevznyak as the period-fit source-backed lead and Pepelyayev as role/date-invalid for the opening.
- Trigger source SHA-256 after the correction: `08307F514442AA41C7C3B3D6E9C08E367F07BBE0EF684BD948C00FB12090D580`.
- Static check: 86 opening braces and 86 closing braces, one Pevznyak reference, zero Pepelyayev references, and no unsupported comparison operators in the package trigger.
- Mandatory Event MCP scan returned `EVENT_INSPECTED_PARTIAL` at revision `741883f50501db1f866db675ee6ad6cb4009a90ad539eb84b08ce5e82602f65b`, with workspace-wide helper/lifecycle analysis deferred and zero selected blocking diagnostics. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/95e0563c862dbfbc555ceb1ecd3a233e2b85b04de28511757e58c07db0526bd8/1518fc8d415bb6f040feff1b7a1b08861b986baf24286951c776b707b3dbfa0b/event-scan-741883f50501.json`.
- Mandatory map inspection still returns `MAP_STATE_ID_COLLISION` for explicit state `574` from `game:history/states/574-Siberia 1.txt`.
- Mandatory Sakha AI inspection returned `PROBABILITY_SOURCE_DISCOVERED` with `discoveryReason=no_weighted_surfaces`, zero candidates, and zero unresolved inputs. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/513bdad22aa76a555a65db93215a39f64e4c40d22ce9695326d5f1eed63f61d2/8d9e575b02001470c453f485c6730f7d97cd31ec8ad46c7b60918f0430de6735/probability-inspect-aecf23c812ca.json`.

## Remaining gates

IW-051 remains package-local and fail-closed. The parent-owned identity/rights flag is unset, the installed-map state-574 collision remains unresolved, the period flag lead still needs released-origin and rights acceptance, and no quantitative AI or mission balance claim is available from the empty weighted surface. Central authority remains 40 runtime adapters, 32 content attestations, 29 compatible reservation groups, and 161 unattested selectable rows.
