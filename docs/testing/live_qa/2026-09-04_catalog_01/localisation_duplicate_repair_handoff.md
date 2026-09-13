# Startup localisation duplicate repair handoff

## Scope and evidence

This patch addresses the duplicate English localisation entries reported by `logs/launch_03/active_logs/text.log`, except every Event 16/shared raid key, which remained read-only as assigned. Events 6, 12, and 23 had no duplicate entries in this log.

The six original files are preserved byte-for-byte under `pre_patch_localisation/` at their repository-relative paths:

- `pre_patch_localisation/localisation/english/chaosx_chaos_meter_l_english.yml`
- `pre_patch_localisation/localisation/english/039_murder_mystery_l_english.yml`
- `pre_patch_localisation/localisation/english/025_alien_technology_in_antarctica_l_english.yml`
- `pre_patch_localisation/events/025_alien_technology_in_antarctica.txt`
- `pre_patch_localisation/localisation/english/031_terrorist_attack_l_english.yml`
- `pre_patch_localisation/events/031_terrorist_attack.txt`

## Changed files and keys

- `localisation/english/chaosx_chaos_meter_l_english.yml`: deduplicated `chaos_meter.air.source.asteroid.name`, `.short`, `.description`, and `.behavior`, plus `chaos_meter.air.source.acid_rain.name`, `.short`, `.description`, and `.behavior`. Complementary source and recovery facts were retained in one player-facing definition per key.
- `localisation/english/039_murder_mystery_l_english.yml`: removed the earlier identical duplicate of `murder_mystery_mechanized_infiltration`; the definition beside its technology description remains.
- `localisation/english/025_alien_technology_in_antarctica_l_english.yml`: moved the fortified-camp option text from the colliding `chaosx.nr25.70.d` key to `chaosx.nr25.70.d_option`. The event description remains on `chaosx.nr25.70.d`.
- `events/025_alien_technology_in_antarctica.txt`: changed only the fortified-camp option name reference to `chaosx.nr25.70.d_option`.
- `localisation/english/031_terrorist_attack_l_english.yml`: moved the non-actor response from the colliding `chaosx.nr31.7.d` key to `chaosx.nr31.7.d_option`. The event description remains on `chaosx.nr31.7.d`.
- `events/031_terrorist_attack.txt`: changed only the non-actor option name reference to `chaosx.nr31.7.d_option`.

No gameplay effects, triggers, weights, or outcomes changed.

## Audit lists

Missing keys: none in the repaired key and consumer set.

Duplicate keys remaining from the launch log, report-only by scope:

- `brilliant_scientist_portal_containment_category`
- `brilliant_scientist_portal_containment_category_desc`
- `brilliant_scientist_seal_recaptured_portal_breach`
- `brilliant_scientist_seal_recaptured_portal_breach_desc`
- `brilliant_scientist_seal_recaptured_portal_breach_requirements_tt`
- `brilliant_scientist_seal_recaptured_portal_breach_cost`
- `brilliant_scientist_seal_recaptured_portal_breach_complete_tt`
- `brilliant_scientist_seal_recaptured_portal_breach_cancel_tt`

Each is defined in both `localisation/english/016_brilliant_scientist_projects_l_english.yml` and `localisation/english/chaosx_raids_l_english.yml`. They were not edited.

Scripted localisation issues: none found in the exact Chaos Meter selectors. The existing selectors still resolve the same eight source keys.

Dynamic text opportunities: none needed for this collision repair. Existing scripted-localisation calls and variables remain unchanged.

Cross-surface mismatches: the Event 25 and Event 31 popup descriptions and fourth option labels previously shared one key despite requiring different text. Their source references now resolve distinct keys with both intended texts preserved. No spreadsheet wording change is required because the visible wording did not change.

File encoding concerns: none in the four edited localisation files. Each remains UTF-8 with BOM.

## Prose repairs

- Vagueness: replaced implementation-facing phrases such as “accepted secondary disasters” with concrete asteroid impacts, fragments, suspended debris, and resulting disasters.
- Bloat: consolidated competing Chaos Meter entries into one description and one behavior entry per source.
- Obvious explanation: removed internal allowance, ceiling, and bounded-opening language that did not help the player understand the source.
- Repetition: removed identical name and short-label definitions, plus the repeated Event 39 technology name.
- Overcomplication: split dust recovery from its non-radioactive distinction and stated acid-rain persistence directly.
- Style-rule repair: removed the semicolon from the asteroid behavior and kept the text grounded in visible source behavior.

No sourced or attributed quotation was changed or encountered in the inspected surfaces. No dynamic token, formatting code, condition, cost, timer, actor, state, or route name was removed.

## Validation and MCP evidence

A source-level key inventory over every English localisation file confirms that each of the eleven repaired launch-log keys has exactly one active definition. Both new option keys have exactly one event reference and one localisation definition.

The focused Event Chain Viewer option renders at revision `f9436dee3f5cb09c3bdc4a12354936955b1f81519dcc79453867ce4504c92978` identify `chaosx.nr25.70.d_option` as Event 25 option index 3 and `chaosx.nr31.7.d_option` as Event 31 option index 3:

- `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f84960f29a0e93be1bace7fdfa284027a24c03bdd4a498a6739125e31dcf837d/bdc510ac8f0740fea29fe16e52df3a5c84e9607691a5f7707513302673142c87/event-options-f9436dee3f5c.json`
- `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2a13806020856c3a40008e75bd545523f87a087a12bb2c56daf4c1ddab43b699/892bb791c92631ab7cf94d5c6eafef74af84939a2bbb099f56bbb71e608144b5/event-options-f9436dee3f5c.json`

The focused event analysis is partial by service design and reports unrelated unresolved helper projections. It provides direct option-key/source evidence, not full event lifecycle acceptance.

Chaos Meter GUI inspection completed for `chaos_meter_popup_window`, scenario `air_source_details-generated-1`, with complete source coverage and no missing fidelity nodes. Its shared-source graph reports pre-existing repository-wide identifier collisions outside this localisation repair:

- `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/471be23b95be5b5f05e4da0561c4f18a6ccc30ceb965ada6b4edc85895f2dc76/265554b7f74f1a132a5248422545f78be76a71a91638f561a46ed3aba0e3d56c/gui-inspect.b7c5d05fd68ce7ab.json`

The first combined normal, long-text, and missing-localisation GUI render timed out after 180 seconds. A normal-state 1920x1080 render then succeeded. After the final prose tightening, the current-source normal-state render also succeeded with no returned layout or text diagnostic; the response was wire-truncated and links the complete SVG:

- `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/fc46081ffe5042b3e302759e3ee30cde1d7d434c45c4654188c6e0cd10a4fccf/076fd6cb7e81d04d15d13a238427ebc201d434ada177c5656e1016326b2f6c54/chaos_meter_popup_window-full.svg`

The linked SVG is the production visual artifact. The MCP resource transport returned it as a partial binary envelope, so direct visual inspection inside this subagent session remains uncertain despite the successful render and absence of returned text/layout diagnostics.

Skipped meaningful validation: no HOI4 launch was performed, as assigned. A fresh launch is required to prove the engine duplicate log is clear for the repaired keys.

## Unresolved decisions and blockers

No wording decision remains for the repaired keys. The eight Event 16/shared raid collisions require their owning agent to choose the canonical definitions and consumers. The partial visual-artifact transport limits direct review of the final Chaos Meter SVG as noted above.

No plan handoff was needed. No simplification or fallback changed player behavior.
