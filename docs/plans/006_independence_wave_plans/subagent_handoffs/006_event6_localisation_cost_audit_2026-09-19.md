# Event 006 localisation and decision-cost audit

Date: 2026-09-19. Disposition: unresolved presentation gap. This is a bounded source audit, not an Event 006 completion claim.

## Scope and result

Inspected the Event 006 decision cost consumers, English localisation, Transcaucasus payment and affordability helpers, cost constants, scripted-localisation route inventory, Part 3 accepted spec, and the August 15 no-pre-event supersession. No gameplay or localisation change was retained. This handoff is the only changed file. No files were staged or committed.

The strongest concrete bloat is `independence_wave_cost_iw070_garrison`, `independence_wave_cost_iw071_command`, and `independence_wave_cost_iw072_oil` in `localisation/english/006_independence_wave_transcaucasus_l_english.yml:59-62`. Each inline row prints four spendable resource groups, including two addition expressions, at roughly 536-554 source characters. The matching `_blocked` and `_tooltip` keys at lines 120-127 repeat the full row. These are the exact `custom_cost_text` consumers at `common/decisions/006_independence_wave_transcaucasus_decisions.txt:71,151,215`. The current trigger and payment helpers at `common/scripted_triggers/006_independence_wave_transcaucasus_package_triggers.txt:322-359` and `common/scripted_effects/006_independence_wave_transcaucasus_package_effects.txt:221-297` confirm command power, manpower, infantry equipment, and support equipment. The August 22 overstatement of an additional standard command-power spend has already been corrected in the current strings.

The decisions/missions skill limits the inline cost to three values and requires full payment disclosure in the tooltip and a red affected amount/icon when unaffordable. A simple three-value inline truncation would conceal whichever fourth resource fails in the blocked row. Without a validated native decision-cost render or an accepted compact status/tooltip treatment, no safe replacement is established. The parent should resolve the four-resource presentation as a separate bounded decision-UI/localisation pass; do not alter the four-group payment merely to shorten text.

## Localisation audit ledger

- Missing keys: none for the three named Transcaucasus cost families; base, `_blocked`, and `_tooltip` keys are present.
- Duplicate keys: none found in the current `006_independence_wave*.yml` English file set by key scan.
- Scripted localisation issues: none proved in the inspected cost consumers. The three named rows use constant tokens, not a scripted-localisation selector. Wider Event 006 scripted localisation was not certified.
- Dynamic text opportunities: package values and costs already use constants. The three compound infantry/support displays could benefit from a single dynamic total, but introducing or reusing total constants requires a reviewed affordability/payment/display contract so independent tuning cannot make the displayed total stale.
- Cross-surface mismatch: no current command-power or Army XP mismatch remains for the three named Transcaucasus actions. The source scan found no active Event 006 decision or English localisation key advertising the retired pre-event crisis. The accepted Part 3 and August 15 supersession prohibit a category, mission, cost, queue, or history cue before the public report.
- File encoding: the inspected Transcaucasus English file has a UTF-8 BOM. No encoding concern found in that file; the rest of the Event 006 files were not byte-audited.
- Prose quality: the four-group arithmetic is dense and overcomplicated in an inline consumer. No safe narrow rewrite of vagueness, bloat, obvious explanation, repetition, or style-rule violations was proved elsewhere in this bounded pass. No sourced or attributed quotation appears in the three cost families, and no quote was changed.
- Spreadsheet handoff: no catalog wording changed; no spreadsheet action is needed from this audit.

## Evidence and limits

Offline wiki Localisation and Decision modding pages, vanilla `documentation/script_concept_documentation.md`, and the repository events, decisions/missions, and subagents skills were consulted. Read-only `hoi4.event_inspect` for `chaosx.nr6.1` returned `EVENT_INSPECTED_PARTIAL`, revision `7b46ce0f0b41b7a70558a7f9c2a50810d919f49edff91f4121893ac789909dce`, with a linked trace artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bc366da1144ab9779992ba6e2534907c4a392d7e497d93a0e1dd3aa94b327be3/b2da3d41375ee7e65b0f6f0aae352a9c5c2c73e79aba61783a44f36e669a3dc6/event-trace-7b46ce0f0b41.json`. Read-only `hoi4.event_render` returned `EVENT_RENDERED_PARTIAL` for the root neighborhood; its manifest is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f2a9f13c9a5ca7ef0682af572e0dad4a915042b2db03950a15f991002158cde7/22cfaef7778c2b3966f530ff5c4bf961735253eed0c2833d9bfe05efa688b915/event-neighborhood-7b46ce0f0b41-manifest.json`.

The installed MCP inventory exposes event, GUI, and technology inspect/render/compare routes, but no ordinary decision-row cost renderer or decision inspector. The event graph does not prove decision-row overflow. Standalone Technology Tree Viewer availability was checked separately from the exposed technology routes and no standalone viewer tool was present in this tool package; this is a package gap, not evidence that the technology service is healthy or unhealthy. No GUI or technology surface was in this bounded audit. No game session was launched. The skipped meaningful check is the available/blocked decision cost next to its real title in the native UI, because that route is not exposed.

## Parent follow-up

Resolve the named cost rows against a native decision-render route when available, ensuring every paid resource remains discoverable and an unaffordable resource remains marked. Preserve the four paid groups, dynamic tokens, and all existing requirements. No wording decision was taken here and no mechanics or quotations were simplified.
