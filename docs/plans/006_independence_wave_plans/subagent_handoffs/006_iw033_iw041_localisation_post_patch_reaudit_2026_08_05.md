# IW-033 / IW-041 localisation post-patch re-audit

Date: 2026-08-05

Mode: read-only re-audit. No gameplay, localisation, scripted localisation, AI, or interface source was changed.

> Superseded source-status note (2026-08-05): a later current country-package audit confirms that all four Emergency Directorate and Frontier/Coastal command keys exist. This handoff preserves the earlier post-patch scan as historical evidence; country-name policy and concise custom trigger tooltips remain the current localisation limits.

## Result

The cost, encoding, live-ledger, and implementation-language repairs requested after the first audit are present. The initial re-audit identified four missing fascist-party `Emergency Directorate` keys, but those four keys were restored in the current localisation source after this receipt was written. The earlier direct blocker is therefore historical; both the initial `Emergency Directorate` and later `Frontier Command`/`Coastal Command` families are present now.

The package also retains unresolved country-name policy and lacks concise custom trigger tooltips for non-cost availability gates.

## Resolved findings

- `KAR_independence_wave_frontier_command`, `KAR_independence_wave_frontier_command_long`, `CRI_independence_wave_coastal_command`, and `CRI_independence_wave_coastal_command_long` now exist and match the route-install effect references.
- All eight package cost families contain one normal, one `_blocked`, and one `_tooltip` key.
- All eight normal, blocked, and hover cost variants read the existing package script constants with integer formatting.
- The cost text uses valid command power, train, infantry equipment, support equipment, manpower, convoy, and fuel text-icon identifiers. The support-equipment icon is supplied by `interface/chaosx_texticons.gfx`; the other inspected identifiers resolve through vanilla text icons.
- The file contains no `U+00C2` mojibake character. It contains the expected single `U+00A3` text-icon markers.
- The file retains the required `EF BB BF` UTF-8 BOM, contains no Unicode replacement character, and uses unversioned localisation keys.
- The Karelian founding mission now displays Forest Supply Integrity and Civic Mandate as live integer values against the dynamic stable threshold.
- The Crimean founding mission now displays Return Capacity and Land Settlement as live integer values against the dynamic stable threshold.
- Colour formatting is balanced: 57 opening colour codes and 57 `§!` terminators.
- The phrases `free formation loop`, `selected government route`, and `Event 006 ledgers` are gone.
- The patched command-party and custom-cost companion keys occur only in the target localisation file in the targeted duplicate scan.

## Historical missing-key finding (repaired)

These four keys were directly referenced by the initial party setup and were absent during the original re-audit. They now exist in the target file:

- `KAR_independence_wave_emergency_directorate`
- `KAR_independence_wave_emergency_directorate_long`
- `CRI_independence_wave_emergency_directorate`
- `CRI_independence_wave_emergency_directorate_long`

Current source locations:

- Karelia fascist party setup: line 27.
- Crimea fascist party setup: line 42.
- Karelia emergency-route neutrality party setup uses `Frontier Command`: line 384.
- Crimea emergency-route neutrality party setup uses `Coastal Command`: line 428.

These are separate consumers, not alternate names for one consumer. Add the four `Emergency Directorate` keys back unless the setup effects are intentionally changed. Retain the four command keys for the route-install effects.

## Duplicate keys

No duplicate was found among the 20 newly added command-party and custom-cost companion keys. The earlier full target-key scan found no duplicate under `localisation/english/`; this re-audit did not repeat that expensive repository-wide scan after the command timed out, but the targeted scan confirms every newly added key appears only once.

## Scripted localisation and dynamic text

- The four ledger variables and the stable threshold are now referenced directly and formatted as integers.
- All package-specific cost values are dynamic constants.
- No broken `defined_text` or scripted-localisation call was introduced.
- The category remains static. It still cannot name the active package or show the live ledger summary outside the founding mission.

## Remaining naming issues

1. Runtime Crimean identity remains unresolved. The package defines `CRI: "Crimean Tatar State"`, while vanilla ideology-specific runtime names remain `Crimea`, `Crimean People's Republic`, `Crimean Regime`, and `Crimean Khanate`. The bare `CRI` key does not make the country consistently display as the Crimean Tatar State. The parent still needs an explicit decision to preserve vanilla names, override the ideology-specific families, or use a cosmetic tag.
2. `independence_wave_karelia_crimea_category` remains `Karelian and Crimean Statehood`, so either carrier sees both package identities despite only one package being active.
3. The Crimean constitutional route uses `Civic Return Union` for the party and decision but retains the generic idea name `Constitutional Mandate`. This is mechanically valid but less distinctive than the other Crimean route naming.
4. `Emergency Directorate` and `Frontier Command` or `Coastal Command` represent different party setup stages in current source. The localisation must preserve both families unless the gameplay owner deliberately merges those stages.

## Remaining trigger-tooltip issues

No `custom_trigger_tooltip` or `custom_trigger_tooltip_with_args` appears in `common/decisions/006_independence_wave_karelia_crimea_decisions.txt`.

The following non-cost gates can therefore surface raw or mechanically generated trigger text:

- capital control on every project and route action
- the one-active-project exclusion on every project and route action
- former-host survival and peace for border transit and the former-host settlement
- stable Karelian or Crimean ledgers for the durable-sovereignty decisions
- the shared founding-settlement receipt for durable sovereignty
- the settled-foundation and live-league-phase requirements for the regional network corridor

Recommended tooltip families:

- `independence_wave_kc_requires_capital_control_tt`
- `independence_wave_kc_requires_no_active_project_tt`
- `independence_wave_kc_requires_peaceful_former_host_tt`
- package-specific durable-sovereignty requirement tooltips that name both live ledgers and the stable threshold
- `independence_wave_kc_requires_live_league_phase_tt`

The founding mission descriptions now show the ledger threshold, which materially improves clarity, but the durable-sovereignty availability block should reuse that clarity instead of exposing `has_stable_independence_wave_*_ledgers` and internal receipt flags.

## Remaining prose-quality issues

### Vagueness

- `opening force`, `surviving anchor`, `both regional ledgers`, `shared capacity ledger`, and `forest ledgers` remain abstract. The new live values clarify the founding missions, but the effect tooltips should still name the affected metrics.
- `independence_wave_kc_foundation_failure_effect_tt` does not name the two package-specific ledgers or quantify their loss.

### Cost presentation

- Every blocked package cost begins with `Unavailable: requires`. The decision skill prefers short icon-first blocked costs without repeated filler.
- Each blocked variant colors every component red when the combined trigger fails, even if the country is missing only one component. A scripted or bindable requirement summary could distinguish missing from satisfied resources, but this is a quality improvement rather than a missing-key blocker.

### Bloat and overflow uncertainty

- The rendered cost rows should be much shorter than their source because dynamic tokens collapse to numbers, but the longest source values are over 300 characters.
- The two founding descriptions now combine prose with two live metrics. Their rendered length may be acceptable, but no dedicated decision-category localisation renderer is exposed by the installed HOI4 MCP, so in-window wrapping and overflow remain unverified.

### Style rules

- No em dash, semicolon, working label, prompt fragment, TODO, placeholder, or update-history wording was found.
- The explicit implementation phrases identified in the first audit were repaired.

## MCP evidence and limitations

- Fresh `hoi4.probability_inspect` scan of `common/decisions/006_independence_wave_karelia_crimea_decisions.txt` completed with source revision `3b5d3c5aee7b5f034755bbbedc450ad41e99116c12750b9b4110c8a50453007f`.
- Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7ece43861c79095eb9e7b73d3aceb1a36f8edd6ca68746e4765d49918874f8c7/7822fdd846972d158304b6c437f37f062996bf2686160b3d03a901cb4600236e/probability-inspect-0ade9f81b363.json`.
- The inspector again reports an incomplete pool and only two candidates. This is source-linked evidence, not a complete decision-balance audit.
- The installed HOI4 MCP still exposes no dedicated decision-category localisation inspection or render route. Trigger presentation, blocked-cost rendering, wrapping, and overflow could not be visually verified. Source review is not treated as equivalent visual evidence.
- No linked focus, scripted GUI, map, event-chain, technology, or doctrine surface was introduced by this localisation patch.

## Sourced quotation preservation

No sourced or attributed quotation appears in the target package localisation. No shared super-event quotation or numbering surface was changed or re-audited in this patch-only pass.

## Recommended next fixes

1. Restore the four `Emergency Directorate` keys while retaining the four command-party keys.
2. Add concise custom trigger tooltips for capital control, active-project exclusion, former-host peace, durable-sovereignty ledgers and settlement, and the live league phase.
3. Decide and document the runtime `CRI` naming policy.
4. Consider package-aware category naming and replace the remaining generic ledger phrases with the affected metric names.
5. Shorten blocked cost text to icon-first presentation. Add per-resource missing-state text only if the owning agent accepts the additional scripted-localisation complexity.

## Changes made

Only this post-patch audit handoff was added. No source key, identifier, dynamic localisation, behavior, or display was changed.
