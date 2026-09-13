# Startup game-rule repair handoff

Status: implemented in the bounded source scope; parent cycle03 engine validation is pending.

Owner: `/root/startup_game_rules`.

Date: 2026-09-13.

## Finding

The fresh cycle02 error log reported 20 `has_game_rule` validation errors at 20 caller sites, covering five unique rule identifiers: `AFG_ai_behavior`, `BUL_ai_behavior`, `GRE_ai_behavior`, `INS_ai_behavior`, and `TUR_ai_behavior`.

| Rule | Fresh-log caller lines | Installed vanilla source block | Native DLC gate |
| --- | --- | --- | --- |
| `AFG_ai_behavior` | `AFG_scripted_triggers.txt:21,27` | `00_game_rules.txt:2923-2979` | `Graveyard of Empires` |
| `BUL_ai_behavior` | `BUL_scripted_triggers.txt:308,314,324,334,344,354,364,374` | `00_game_rules.txt:1949-1999` | `Battle for the Bosporus` |
| `GRE_ai_behavior` | `GRE_scripted_triggers.txt:20,26` | `00_game_rules.txt:1892-1947` | `Battle for the Bosporus` |
| `INS_ai_behavior` | `INS_scripted_triggers.txt:65,82,99,120,134,140` | `00_game_rules.txt:3126-3166` | `Thunder at Our Gates` |
| `TUR_ai_behavior` | `TUR_scripted_triggers.txt:20,26` | `00_game_rules.txt:2001-2066` | `Battle for the Bosporus` |

The install has no `Graveyard of Empires`, `Battle for the Bosporus`, or `Thunder at Our Gates` DLC directory. The vanilla rules are top-level DLC-gated, so their rule objects are omitted while the vanilla scripted trigger files still load. `descriptor.mod` only replaces `gfx/loadingscreens`, and the pre-edit local `common/game_rules/chaosx_game_rules.txt` contained commented examples with no active definitions.

## Applied source repair

`common/game_rules/chaosx_game_rules.txt` now appends exact vanilla payloads for all five rule identifiers.

| Rule | Ungated default | Non-default options and preserved DLC gate |
| --- | --- | --- |
| `AFG_ai_behavior` | `DEFAULT` | `HISTORICAL`, `FASCISM`, `DEMOCRATIC`, `COMMUNIST`, `CALIPHATE`, `EMPIRE`, `MUGHALS`, `RANDOM` → `Graveyard of Empires` |
| `BUL_ai_behavior` | `DEFAULT` | `HISTORICAL`, `COMMUNIST`, `COMMUNIST_BALKAN_FEDERATION`, `FASCIST`, `THE_RETURN_OF_FERDINAND`, `DEMOCRATIC_SOCIALIST`, `DEMOCRATIC_LIBERAL`, `RANDOM` → `Battle for the Bosporus` |
| `GRE_ai_behavior` | `DEFAULT` | `HISTORICAL`, `MONARCHIST`, `MONARCHIST_ALTERNATE`, `COMMUNIST`, `COMMUNIST_ALTERNATE`, `DEMOCRATIC`, `FASCISM`, `FASCISM_ALTERNATE`, `RANDOM` → `Battle for the Bosporus` |
| `INS_ai_behavior` | `DEFAULT` | `TRUE_HISTORICAL`, `LOYALIST`, `REVOLUTION_DEMOCRATIC`, `REVOLUTION_UNALIGNED`, `REVOLUTION_COMMUNIST`, `RANDOM` → `Thunder at Our Gates` |
| `TUR_ai_behavior` | `DEFAULT` | `HISTORICAL`, `ALTERNATE_KEMALIST`, `TUR_DEMOCRATIC_KEMALIST`, `TUR_DEMOCRATIC_ALTERNATE`, `FASCISM_TUR_AI`, `TUR_FASCISM_ALTERNATE`, `COMMUNIST_TUR_AI`, `TUR_COMMUNISM_ALTERNATE`, `BALKAN_ENTENTE`, `OTTOMAN`, `RANDOM` → `Battle for the Bosporus` |

The native top-level `required_dlc` field was moved to every non-default option in the compatibility copies. The five `DEFAULT` blocks have no DLC gate, which registers the rule object needed by the always-loaded callers without exposing unavailable DLC routes. The native `name`, `group`, option names, `text`, `desc`, option order, and `allow_achievements` fields are preserved. There are 42 guarded non-default options and five ungated defaults.

The AFG caller uses both uppercase and lowercase spellings in vanilla (`AFG_AI_BEHAVIOR` and `AFG_ai_behavior`); the canonical native rule identifier is retained exactly as `AFG_ai_behavior`.

Vanilla localization keys are reused from the installed `localisation/english/game_rules_l_english.yml`; no localization file was changed.

## Coverage and file surface

| Surface | Result |
| --- | --- |
| Country tags and scripted trigger references | Five caller families covered: AFG, BUL, GRE, INS, TUR. No tag or trigger source was edited. |
| Rule source | `common/game_rules/chaosx_game_rules.txt` only; five active compatibility definitions appended after the pre-existing comments. |
| Static loading and overrides | `descriptor.mod` has no `common/game_rules` replacement. No competing local active definitions were found before the repair. |
| State, map, ownership, cores, capitals, supply, railways, ports, resources, and buildings | Outside this game-rule scope; no changes or claims of coverage. |
| Politics, leaders, portraits, flags, advisors, parties, focus trees, decisions, ideas, assets, military, technology, industry, production, and supply | Outside this game-rule scope; no changes or claims of coverage. |
| AI behavior and playability | Rule option/default registration mirrors vanilla payloads. AI weights and strategy factors were untouched; parent live validation remains pending. |

## Before and after behavior

Before the repair, the startup database validator emitted 20 missing-rule errors for the five identifiers above. After the repair, the no-DLC installation has a registered default object for each identifier, while all DLC-specific alternatives remain gated by their native DLC name. Cycle03 must confirm the resulting engine log and startup behavior.

This repair does not add generic empty rules, delete vanilla triggers, disable country content, or change probability-bearing weights. It intentionally changes only the registration boundary required for the no-DLC installation: a top-level native gate becomes per-option gates, with the native default retained.

## Evidence and validation

- Fresh-log extraction: `docs/testing/live_qa/20260913_main_menu_startup/logs/cycle_02/error.log` contained 20 missing-rule lines and five unique identifiers.
- Vanilla source inspection covered each listed block, all actual caller option names, and the installed game-rule localization keys.
- Source parity inspection confirmed five active rule IDs, five ungated `DEFAULT` blocks, 42 non-default `required_dlc` fields, and the full native option sets.
- The pre-edit source was backed up at `baseline/game_rules/chaosx_game_rules.txt` before editing. The backup is 1,173 bytes with SHA-256 `d036536d2b74f4bf2c6ebb4e1a4cf1d6914277787452aa4f52b30373552515dd`; those bytes remain an exact prefix of the repaired source.
- No probability audit was required because no AI weight, strategy factor, MTTH, random weight, or other probability surface changed.
- No live-game process was launched by this subagent. Parent `/root` owns cycle03 launch and engine-log validation.

## Changed files and remaining risk

Changed gameplay file: `common/game_rules/chaosx_game_rules.txt`.

Changed documentation file: this handoff.

No tags, state IDs, leaders, parties, focus IDs, localization keys, formables, or assets were changed. No commit was created, per the parent task boundary.

Remaining risk is limited to engine confirmation that per-option DLC gates resolve the five always-loaded trigger callers as intended. If a relevant DLC is later enabled, the native rule IDs and option payloads remain aligned with the installed vanilla source.

No simplification or omission was made within the requested five-rule repair. Country package surfaces outside game-rule registration remain intentionally unreviewed by this bounded subtask.
