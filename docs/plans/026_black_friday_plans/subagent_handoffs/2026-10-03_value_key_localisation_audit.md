# Event 026 value-key localisation audit

Disposition: `implemented` for the parent-applied source repair, with live expansion `unresolved`.
Acceptance basis: the parent requested a read-only review of the direct real-key fix for three reported startup localisation-creation errors.
This report is the only file written by this subagent.
The parent retains fix review, shared-tree commit ownership, and all completion claims.

## Finding

No source defect found in the three-getter repair.
Each getter now supplies a real, unique localisation key instead of placing a formatted variable expression in `localization_key`.
Each named key reads the matching temporary variable assigned inside that getter's own `text.trigger`.
The documented temporary-variable lifetime and the installed vanilla named-key pattern support this construction.
Expected expanded values at the inspected constants are `600`, `75`, and `5`, respectively.
These are source-derived expectations, not observed expansion results.
No claim is made that startup errors are cleared, that error.log is clean, or that Event 026 is complete.

## Exact source chain

All repository paths below are relative to `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux`.

| Getter and source lines | Named key and localisation line | Stored value and formatter |
| --- | --- | --- |
| `GetBlackFridayEvolutionChaos`, `common\scripted_localisation\026_black_friday_scripted_localisation.txt:8-16` | `black_friday_evolution_chaos_value`, `localisation\english\026_black_friday_l_english.yml:3` | `[?black_friday_evolution_chaos_display\|0]`, assigned at script line 12 from `constant:black_friday_event.evolution_chaos` |
| `GetBlackFridayEvolutionDiscountPercent`, same script lines 18-26 | `black_friday_evolution_discount_value`, same localisation line 4 | `[?black_friday_evolution_discount_display\|0]`, assigned at script line 22 from `constant:black_friday_event.evolution_discount_percent` |
| `GetBlackFridayAchievementTargetFamilyCount`, same script lines 28-36 | `black_friday_achievement_family_count_value`, same localisation line 5 | `[?black_friday_achievement_family_count_display\|0]`, assigned at script line 32 from `constant:black_friday_event.achievement_target_family_count` |

The constants resolve in `common\script_constants\026_black_friday_constants.txt` at lines 17, 31, and 38 to 600, 75, and 5.
Each getter has one definition across `common\scripted_localisation`, and each named key has one definition across repository `localisation`.
The three temporary variable identifiers occur only in their corresponding assignment and named value key within the searched runtime folders `common`, `localisation`, `interface`, and `events`.
No cross-getter overwrite or dependency on a previously executed gameplay effect was found.
Each invocation initializes its own display value before returning the key, with no country or global prefix on the temporary-variable read.

Existing consumers remain intact:

- `black_friday.evolution.1.body`, localisation line 26, calls the chaos and discount getters.
- `black_friday.evolution.1.summary`, localisation line 27, calls the discount getter and retains its external `%` sign.
- `black_friday.event_detail.evolution`, localisation line 23, aliases `$black_friday.evolution.1.body$`. No additional runtime reference to that alias was found by the exact search, so this audit does not assert it is selected by a GUI.
- `common\scripted_localisation\chaosx_scripted_localisation_events_log.txt:8434` selects the evolution body, and line 8936 selects the summary under `GetEventsLogSelectedEvolutionSummary`.
- `026_black_friday_five_departments_DESC`, localisation line 50, calls the family-count getter.
- `026_black_friday_five_departments_tooltip`, localisation line 51, aliases that description and retains the additional purchase restrictions.
- `common\achievements\chaos_redux_achievements.txt:4236-4238` declares the achievement and uses that tooltip in `custom_override_tooltip`.

The reviewed Git diff contains exactly three `localization_key` replacements and three added value keys in the two parent-patched files.
The existing temporary assignments, constant references, consumer sentences, getter names, and integer formatters are unchanged.

## Documentation evidence

Local sections read directly because the attempted connected reference route did not return a result:

- `paradox_wiki\Localisation - Hearts of Iron 4 Wiki.md:680` explicitly states that temporary variables assigned in `text.trigger` remain set while displaying its localisation key.
- The same wiki at lines 729-791 demonstrates trigger-local calculations, real named `localization_key` entries, and variable expressions in the corresponding YAML values. Line 791 limits availability to scripted localisation and its downstream localisation keys.
- `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\triggers_documentation.md:7482-7501` documents `set_temp_variable`, supported scope `any`, and the shorthand assignment pattern used by these getters.
- `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\scripted_localisation\WUW_GER_scripted_loc.txt:689-697` assigns and adjusts temporary variables in a text trigger, then returns the real key `oppositional_monroe_list`.

SHA-256 revisions of the documentation files, in the same order:

```text
wiki Localisation: 1A8F72362A34B4BB653186746B9FAE0B98E463205CB02F12CCF2C3D9CCD3A064
installed triggers: 7D27ED77DADAF3A213A4B3E2C624BF9C02DAE495317ABE8EEE833B27C2D1DE29
vanilla WUW_GER: 82233D7BB8362D933182C7DA345606089A67B92ADEDB764C37A942E1E2F67683
```

Reviewed implementation SHA-256 revisions:

```text
026_black_friday_scripted_localisation.txt: 665DD28B4CB12380ACE61FCBBAB36A11E035DA885AC5FA38B590A4FC2F17098E
026_black_friday_l_english.yml: E34F4368D7BCF67B1687CFB8CD59922C9DAA1459A5BD6FEEBEA0C3AAB3202259
026_black_friday_constants.txt: C90776E3B758F49B0AA66DF1C82E035DC0D0A03B53CEB227F868F99975AA0976
chaosx_scripted_localisation_events_log.txt: 08C3137E5BC23B738945A3EE6F75CB6FA3B15C7B424E1373DCF8FA34C71C7163
chaos_redux_achievements.txt: 25A4374CDA371490D04EC6113A8BCEB7FA89F706CA8770FB8FC4862023A9908A
```

## Audit lists and scope limits

- Missing keys: none among the three repaired keys and named direct consumer aliases.
- Duplicate keys: none for the three value keys. Duplicate getter definitions: none for the three getter names.
- Scripted localisation issues: no source issue found in the repaired chain. Live expansion remains unresolved.
- Dynamic text opportunities: the requested three dynamic values already use existing constants through temporary variables. No new opportunity or mechanic is proposed.
- Cross-surface mismatch: no token or value-source mismatch found between the scoped evolution body, summary, achievement description, and tooltip. The catalog workbook and exports were not inspected or changed, so catalog agreement is not claimed and no wording handoff is needed for this value-key-only repair.
- Encoding concerns: none found in the reviewed localisation file. Its byte prefix is UTF-8 BOM and strict UTF-8 decoding succeeded.
- Prose quality: the new keys contain only variable-display expressions. The existing consumer passages were read to establish the chain, with prose changes expressly excluded from this bounded startup repair. No broad prose approval is claimed for Event 026.
- Sourced quotations: no sourced or attributed quotation occurs in the scoped keys or direct consumer passages. Existing wording and all dynamic tokens are preserved by the parent diff.
- Recommended source fix: retain the parent's exact three real-key replacements and three YAML value keys. No additional source patch is recommended by this review.

## MCP and live evidence limits

The parent reported `hoi4.reference_context`, `hoi4.reference_search`, `hoi4.reference_read`, `hoi4.source_lookup`, and `hoi4.script_validate` absent from its connected tool list.
This subagent's inventory differs: the first four routes are exposed, while `hoi4.script_validate` is absent.
The subagent attempted `mcp__hoi4_agent_tools__hoi4_reference_context` with `{ surface: "localisation", question: "named localisation_key and set_temp_variable in scripted localisation trigger", limit: 4 }`.
That call returned no tool result during repeated short polls, and its orchestration cell was explicitly terminated to keep the review bounded.
Exact outcome: `Script terminated`, with no server status, diagnostic, revision, artifact URI, or validated reference bundle received.
This is a nonresponsive attempted route, not a confirmed server error or a successful health check.
No other reference, source-lookup, event, or GUI route was called after that unresolved service attempt, and no route result is invented.
The event and GUI inspect/render routes are exposed, but their service health and this repair's expansion, overflow, wrapping, and visual placement remain unverified.
No MCP artifact URI was produced.
The independent tool-inventory search found no standalone Technology Tree Viewer capability. This is a package/exposure gap, separate from exposed technology inspect/render/compare routes, and no technology work is within this audit.

Meaningful completed validation: exact getter/key uniqueness searches, assignment-to-key matching, downstream consumer tracing, constant-source resolution, comparison with the requested offline and vanilla pattern, and inspection of the bounded parent diff.
Skipped meaningful validation: connected reference retrieval and inspector/render evidence due to the nonresponsive attempted route, script validation because its route is absent, and live startup/dynamic expansion because no renewed live evidence was supplied and this subagent must not launch HOI4.
No gameplay, localisation, catalog, existing documentation, artwork, constants, globals, or balance values were changed by this subagent.
No implementation simplification was introduced.
Unresolved wording decisions: none within the three value keys.
Skills used: `chaos-redux-events` and `chaos-redux-subagents`, after reading current `AGENTS.md`.
No skill was created or updated, and no Git/index operation was performed beyond a read-only diff.
