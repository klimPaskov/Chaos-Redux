# Localisation copyedit handoff for files 001 to 004

Date: 2026-08-02.

Scope: player-facing English localisation files whose names begin with 001, 002, 003, or 004. Gameplay scripts, shared localisation files, quotes, and assets were not edited.

## Changed files and keys

- `localisation/english/001_communism_spread_l_english.yml`: 25 keys covering the insurgency root, intervention, spread, collapse, evolution incidents, and the communism evolution event-log body. The prose now uses concrete actors and consequences, with semicolon and staged contrast patterns removed.
- `localisation/english/002_zombie_outbreak_l_english.yml`: 49 keys covering cure and outbreak reports, Anti-Zombie League formation and tooltips, survivor aftermath, weaponized-zombie profiles and outcomes, archetype summaries, the Wendigo super-event description, and the zombie evolution event-log body. The super-event title now names the Anti-Zombie League consistently.
- `localisation/english/003_the_holy_realm_l_english.yml`: 110 keys covering refuge and doctrine events, status descriptions, panel text, map icons, decision and focus tooltips, super-events, false-Buddha outcomes, foreign missions, and event-log details. The Holy Realm event-detail summary now describes the premise and transformation arc without exposing the exact late-route gate list.
- `localisation/english/004_random_war_l_english.yml`: 6 keys covering border-war reports and dynamic random-war news descriptions.

The complete changed-key sets are available in the path-specific diff. The most important cross-surface keys are `chaosx.events_log.window.event_details.holy_realm`, `chaosx.events_log.window.evolution_details.holy_realm.body.generic`, `chaosx.events_log.window.evolution_details.zombie.body`, `THR_status_value_row_tt`, `THR_send_global_final_warning`, and `chaosx_super_event.2.t`.

## Audit results

- Missing keys: none found within the four owned files.
- Duplicate keys: none found. Key counts are 96 in 001, 145 in 002, 1059 in 003, and 37 in 004.
- Scripted localisation issues: no unresolved custom `Get...` methods. The scan found 30 getter names, with the four vanilla getters `GetAdjective`, `GetName`, `GetNameDef`, and `GetNameDefCap` excluded from the custom-definition check. All remaining custom methods resolve in `common/scripted_localisation/`.
- Dynamic text opportunities: no new scripted localisation was required. Existing state names, country names, division counts, Holy Realm panel values, evolution metrics, weaponized-zombie summaries, and random-war news tokens were preserved exactly.
- Cross-surface mismatch notes: the visible super-event title `The Alliance of Man` was aligned to `The Anti-Zombie League` because the body and event overview use the latter name. The visible `THR_send_global_final_warning` label now says `Send a Final Notice`, while the key, implementation comments, specs, and `chaos_meter.history.reason.special.holy_realm_final_warning` still use the old warning identifier. The parent should decide whether to align those out-of-scope surfaces. Existing sourced-looking quote strings and zombie joke options were left unchanged and need source or tone review if they are in scope.
- File encoding: all four files retain a UTF-8 BOM.

## Display and wording changes

- Before: Holy Realm event details exposed the full metric, gate, and terminal-condition checklist. After: the panel explains the refuge, governance, transformation, and aftermath arc without revealing exact late-route gates.
- Before: `THR_status_value_row_tt` described a read-only row and instructed players to hover. After: it explains that the Mandala Ledger tracks the value and the forces that change it.
- Before: the zombie evolution body used implementation labels such as `Modifiers on the evolved horde` and `Gameplay impact`. After: it uses `Current horde effects` and `On the ground` while retaining every dynamic metric.
- Before: the random-war event used `War Without Warning`. After: it uses `War at the Border` and describes the border escalation directly.
- Across 001 to 004, prose no longer uses semicolon-heavy sentences, em dashes, generic contrast formulas, raw process labels, or hidden Holy Realm route gates. Gameplay facts, options, variables, formatting codes, and line-break tokens remain unchanged.

## Validation

- Compared current keys and bracket tokens against `HEAD` for each owned file. All key sets and dynamic-token multisets matched.
- Compared escaped newline, colour-code, and currency-token counts against `HEAD`. All counts matched.
- Scanned for duplicate keys, missing UTF-8 BOMs, em dashes, en dashes, and semicolons. No issues were found.
- Scanned every custom getter referenced by the four files against the scripted-localisation definitions. No unresolved custom getter was found.
- Ran `git diff --check` on the four owned files. It reported no whitespace errors. Git emitted its normal LF-to-CRLF working-copy warning.

## Skipped validation and unresolved decisions

- No Hearts of Iron IV process was launched, and no in-game GUI or text-overflow render was run. The parent should perform a visual pass in the linked event, evolution, decision, focus, and super-event surfaces.
- Quote attribution and exact wording were not researched because the owned scope was limited to 001 to 004 localisation copyedit and the super-event text researcher owns historical quote verification.
- The remaining warning terminology in shared or implementation-facing surfaces is intentional pending parent review of the `Final Warning` to `Final Notice` naming choice.

No mechanic gap was discovered, so no additional implementation plan was created. This handoff is the required plan-surface record for the bounded localisation patch.
