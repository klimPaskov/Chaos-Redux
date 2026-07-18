# Event 015 Post-Ledger Localisation Completion Re-audit

Date: `2026-07-16`

Auditor: `chaosx_localisation_auditor`

Verdict: **PASS at the static-source level.** No open localisation blocker, omission, placeholder, exact duplicate, stale Event 15 catalog value, or hidden-achievement disclosure remains.

## Frozen inventory

- Nine Event 015 English files, `2,614` lines, and `2,448` quoted definitions.
- All nine files have a UTF-8 BOM. Versioned `:0` keys: `0`.
- Exact duplicate Event 015 keys inside the package or elsewhere in English localisation: `0`.
- Events: `99`; direct popup references: `507/507`.
- Decisions and missions: `164`; name and description keys: `328/328`.
- Decision categories: `9`; name and description keys: `18/18`.
- Public requirement wrappers: `125/125`; effect tooltips: `163/163`.
- Custom-cost families: `92`; base, blocked, and tooltip keys: `276/276`.
- Core event and decision union: `1,417/1,417`.
- Focuses: `124`; name and description keys: `248/248`; availability and bypass wrappers: `99/99`.
- Ideas: `50`; name and description keys: `100/100`.
- Characters: `24`; name and description keys: `48/48`.
- Advisor traits: `16`; name and description keys: `32/32`.
- Dynamic state modifiers: `19`; name and description keys: `38/38`.
- Opinion modifiers: `5/5`.
- Achievements: `14`; names, descriptions, and bespoke proof tooltips: `42/42`.
- Cosmetic identities: `5`; base, definite, adjective, and required ideology variants: `75/75`.
- Event 15 scripted-localisation functions: `34`; unique output keys: `200/200`.
- Ledger GUI direct text references: `25/25`.
- Shared Event Details and evolution keys: `20/20`.
- Route super-event keys: `20/20`; music display keys: `6/6`.

## Public-language corrections

The post-Ledger pass removed implementation-facing wording from player-visible text. Final exact scans report zero visible instances of `dynamically timed`, `dynamically paced`, `dynamically prepared`, `dynamically bounded`, `dynamically determined`, `runtime`, `active record`, `objective lock`, `shared Calling lock`, `identity package`, `state modifier`, `route modifier`, and `coercive modifier`. Visible uses of `dynamic`, `capped`, `implementation`, `scripted return`, `machinery`, and `system state` are also zero.

Opaque timer prose was replaced with public ranges and the circumstances that alter them. The final text covers the implemented `90-210`, `90-270`, `90-330`, `90-420`, `90-180`, `90-240`, `180-660`, `270-990`, `365-540`, `180-360`, and `540-900` day families where they apply.

Lifecycle narration now describes public conclusions, withdrawals, reassessments, expiring obligations, and ended agreements rather than records, locks, refreshes, or proof machinery. In particular:

- `chaosx.nr15.47.option_d` discloses the halted labor columns, restored ordinary role-plan obligation, `500` civilian deaths, and durable coercive history.
- Events `.120` through `.123` and all twelve aftermath tooltips describe the real teardown, succession, territorial-return, practical-legacy, and book-settlement consequences.
- `utopia_manifesto_the_island_made_real_desc` states that continued recognition requires the necessary ground to remain held.
- Non-achievement keys containing `achievement` or `disqualif*`: `0`.
- `utopia_manifesto.evolution.5.body` is frozen to the accepted wording and matches workbook cell `Events!H16` exactly.

## Frozen hashes

| File | SHA-256 |
| --- | --- |
| `015_utopia_manifesto_country_package_l_english.yml` | `42bbc60ef46e9f3c8233c9842a0646b02a72560cd77649195b739fb57416ae92` |
| `015_utopia_manifesto_decision_completion_l_english.yml` | `3fdcc797d5a18d07521837c0d0014c4386e1b78785ea773c1ef4dfa7f09861d3` |
| `015_utopia_manifesto_events_l_english.yml` | `9d6ecdb2b405dc771e49380858e75f8a2b9e9a37e031fc71460611293752cd9b` |
| `015_utopia_manifesto_evolution_consumption_l_english.yml` | `8205917030d34a204b95fb6fd198859b1e7c8b77acc1b8d242fcd46ebf8a92dc` |
| `015_utopia_manifesto_evolutions_l_english.yml` | `508786fb2a6d8b0b1efa51dca67467a8241c25d9aa141528c9e44b590b1d1c01` |
| `015_utopia_manifesto_focus_l_english.yml` | `44ad996d4b7ca05f641ca9a7ea3c75bcd36f3bac84f6e334b93531f6be09c4d8` |
| `015_utopia_manifesto_ideas_l_english.yml` | `f838c2a2356e2c46f7500d3ce35835cfd794df9161c7251a35ce3e195a51bdfb` |
| `015_utopia_manifesto_l_english.yml` | `089fc8072611c3a5fb15c12f31b32aaf6dd98373b60a619a3b9ea4c0d25d5d78` |
| `015_utopia_manifesto_super_event_l_english.yml` | `8f14e4fb22578e942ba5019e1022032b12a794c464e61fcef8d7d01bb5527e32` |

Key authority hashes:

- Event source: `8e3e0c24ebb7c243761c4391965909b7f5d823878a07ec4798ac4f2f8ae688f4`.
- Focus tree: `8a905d4b1922ab88bfab97716ba79721fc5b42679863c9543fb04d2cd489fc05`.
- Main decisions: `5dcd41ef8669a4384fedb2efa9761e657fe8a5ff8ea686e45046005fd23d17fd`.
- Event 15 scripted localisation: `6e44014672139189c53bedb4dd441b9d27900d934a42b6f1fb2166287b6701ed`.
- Ledger GUI: `82c07b4ac7dde3dbee92745ddb7a64e515682e813133904dc31df026d9669593`.
- Workbook: `3c324b75c26f9e17eb9e73761abc5aedfa9bb642f2108a1397fb240679614031`.

## Files changed by the auditor

- `localisation/english/015_utopia_manifesto_decision_completion_l_english.yml`
- `localisation/english/015_utopia_manifesto_evolution_consumption_l_english.yml`
- `localisation/english/015_utopia_manifesto_l_english.yml`
- `localisation/english/015_utopia_manifesto_events_l_english.yml`
- `localisation/english/015_utopia_manifesto_focus_l_english.yml`

## Meaningful validation limits

The narrow HOI4 MCP event inspection returned `ARTIFACT_STORAGE_LIMIT` before scanning files or producing diagnostics. Direct source and reference validation supplied the completion evidence instead. No runtime render or clipping pass was available, and English was the audited language. These are validation limits, not content substitutions.

## Simplifications, omissions, fallbacks, and blockers

- Content simplifications: none.
- Localisation omissions: none.
- Content fallbacks: none.
- Open localisation blockers: none.
- Tooling limitation: the HOI4 MCP artifact store rejected the narrow inspection before analysis; no diagnostic result was treated as a pass.

No commit was created by the auditor.
