# Event 016 D’Rhondan Terrestrial Partner Accord Implementation

Disposition: `implemented` with validation limits.

## Acceptance basis

The accepted Event 016 diplomatic-rewards plan authorizes one paid, target-specific terrestrial partner accord after D’Rhonda exchanges maps and opens partner selection.
On 2026-09-26, the user explicitly approved reciprocal military access for both countries as the Synod outcome when Arms Against Tyranny is absent, provided the selected partner accepts.
The same approval preserves the 75 PP cost, explicit consent, matching accord receipts, and a tooltip that explains the fallback.

## Implementation

`common/decisions/016_dhrondan_country_decisions.txt` adds the accord to the existing sovereignty category and uses the existing 75 PP cost and 90-day repeat cooldown.
The launch gate requires independent D’Rhonda at peace after map exchange and partner selection, with an Imperial, Synod, or Covenant regime.
The target must be independent, not capitulated, not at war with D’Rhonda, and without a prior partner receipt; an existing non-aggression pact is allowed.
`common/scripted_triggers/016_dhrondan_country_triggers.txt` rechecks eligibility and the offer receipt at the recipient response.
`common/scripted_effects/016_dhrondan_country_effects.txt` applies the accepted route and records the matching DHR and recipient receipts.
Imperial acceptance grants D’Rhonda’s guarantee and reciprocal military access, while Covenant acceptance grants reciprocal military access and the bilateral accord opinion marker.
Synod acceptance grants market access when Arms Against Tyranny is enabled and reciprocal military access otherwise; both outcomes use the same receipts.
The installed vanilla `documentation/effects_documentation.md` entry for `give_market_access` states that one directional call gives both countries mutual market access, and vanilla `common/national_focus/austria.txt` gates its market-access effect behind the DLC.
Partner refusal or expiry creates no accord receipt or diplomatic relation effect, and any existing non-aggression pact remains untouched.
Partner offers put a visible refusal option first, so the native timeout cannot interpret silence as acceptance; the compact offer retains its previous option order and behavior.
Partner replies resolve in `.49` and do not use the compact-only `.50` and `.51` reports.
`events/016_dhrondan_country_events.txt`, `common/opinion_modifiers/016_dhrondan_opinion_modifiers.txt`, and `localisation/english/016_dhrondan_country_l_english.yml` contain the response branches, opinion marker, costs, tooltips, and route-specific acceptance wording.
`docs/events/016_brilliant_scientist/systems/dhrondan_country.md` documents the routes and now names the actual `dhrondan_diplomatic_offer_expiry_num_days` receipt.
The catalog sentence is recorded in `subagent_handoffs/016_dhr_partner_accord_catalog_sync_2026-09-26.md`; the workbook edit and exporter run are in the shared worktree.

## Review and evidence

The required offline Paradox wiki references, vanilla HOI4 documentation, and vanilla market-access precedents were consulted; no web wiki was used.
The focused Event `.49` MCP inspect and render returned partial results at revision `13bfefb0efc8ce0c8d3c24ceec0269c9b5372bd9efb2c49bf2c0afa7d556d340` with zero scoped blocking diagnostics; helper and lifecycle projections were deferred.
The render artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0c33750f2a92166c13a68bbbba14ed68f603a108d74fe2591e6d8f764c1729bc/59376f22873ec69580b3464d6fa8f09676f534ff968136ec64210d417a9fe2d2/event-options-13bfefb0efc8.json` and its manifest is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7fb7555647174dc09d21bfe4c872879bbfc84957ab2d58c2b5947a1540630310/e7a35ad471ba6e527eabc84960934cd6a625988e5e6bf5f0b915cdfb95d3be22/event-options-13bfefb0efc8-manifest.json`.
The MCP event comparison returned `EVENT_REVISION_NOT_CACHED`, so it does not prove a before-and-after difference.
The localization audit found 142 keys, no duplicates, and no missing references after the partner timeout option was added; the file retains its UTF-8 BOM.
The decision auditor’s earlier timeout and subject-country findings were addressed by the refusal-first partner option and independent-DHR launch gate; the refreshed event-completion auditor confirmed the timeout behavior and found no remaining source-level consent failure.
The event-completion auditor raised a possible ambiguity in Synod market-access directionality; the installed vanilla effect documentation resolves it by stating that one call creates mutual access.
`hoi4.probability_inspect` found a complete four-option `.49` pool with zero unresolved discovery inputs at source revision `a01050ef5c664099c796ee7789ce995e25cd7887c3d739f3cb99f0c28dc7ee17` and source hash `20f1cfa4160737e8430e9f0c542e4b5c9c457cdbfe9c9cce1f0690bb969e7365`.
The same inspect found a complete one-candidate decision-weight pool with two required inputs and zero discovery-time unresolved items at source revision `26d4166b3fe1fb80242be2797560a0e0385dfc6397edb71c4756c54b432d531d` and source hash `02cd720733108a3e8f38c3daab23898a29ae00cf430390d22a5fb37ed87b863b`.
The named event response evaluation and opinion sweep returned partial results with 17 unresolved items; `.49.a`, `.49.b`, and the partner refusal were never eligible in the adapter projection, while invalid-cleanup `.49.c` appeared dominant in all three scenarios because the fixture did not bind the active event-target and expiry state.
The evaluation and sweep used `E016_DHR_PARTNER_RESPONSE_2026_09_26.scenarios.json` with file SHA-256 `03fe3d84d9c379828152d37ee149c8654f5b9bb6874a16993a66f6a76f73349c` and normalized scenario hash `7ba4b228b97d9f9a23ccf37586b08fd614febecf465ef2a301781259c0ece432`; the sweep covered three points.
The event evaluation artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/90539555fc7843ddf79ebc927222e763d9d2d06a653bfaff2fb5236968c38bb5/7dd3084097bd67b0d24140c439b82b4d10f019c41b4805371d68dc725cbe4038/probability-fa69ae7a752631e10916c902.json`, and the opinion sweep artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4dd53b6f37dc5f56473cd653d80efa73c04a075b85ca6d12d5027f29f2c53d63/a9260e72db949f9f6be3aae019eaca70f95a6ab3c589085b073b9572d5dd6f19/probability-101c6658b4109f21c2e85926.json`.
The decision evaluation returned `PROBABILITY_ANALYZED_PARTIAL` with two unresolved items; its one-candidate `ai_will_do` value remains a score, not a click probability.
It used `E016_DHR_PARTNER_DECISION_MINIMAL_2026_09_26.scenarios.json` with file SHA-256 `079c019ece6baa1aa42e889404924549cbe735fda1425a046509280476772fb4` and normalized scenario hash `edeb6e383c3704bcfc2cc01343d68fc39b84cde34e37b586f76c2d17ad5efcd`.
The three-regime decision fixture `E016_DHR_PARTNER_DECISION_2026_09_26.scenarios.json` has file SHA-256 `68f47e1776f93f1a5a2642d072ab6a34d75d2e8a0037d7055710083f18f80821`; its first evaluation returned `INTERNAL_ERROR` without an artifact.
The direct decision comparison returned `PROBABILITY_SURFACE_EMPTY` because the exact prepatch source contains no `dhrondan_offer_terrestrial_partner_accord` candidate, and the direct event comparison returned `INTERNAL_ERROR` without an artifact.
The baseline event and decision source snapshots are `subagent_handoffs/016_dhr_partner_accord_baseline_2026-09-26/016_dhrondan_country_events_prepatch.txt` (SHA-256 `6b4d16096d3cdbc6aa2ee2fd504020b5a8707e7fab2e4e2f5e9c056e08798d56`) and `subagent_handoffs/016_dhr_partner_accord_baseline_2026-09-26/016_dhrondan_country_decisions_prepatch.txt` (SHA-256 `91d6fe6c06d422dc17a66c0e57711bcc5963660905900f319c707092e6d34583`).
The legacy compact comparison fixture is `E016_DHR_COMPACT_RESPONSE_COMPARE_2026_09_26.scenarios.json` with file SHA-256 `b6fbb227c53577c5d87520a3ff4f94df237f2dbbd5d0b307e4c77ed2f5c07388`.
The probability fixtures are retained in this handoff directory with their audit limits so the adapter-binding gap can be revisited without substituting invented inputs.
The routed `chaosx_ai_probability_auditor` terminated with HTTP 401 authentication failure; direct MCP inspection, evaluation, and sweep were used, but the required valid comparison and scenario-level balance conclusion remain unresolved.

## Validation limits and remaining work

No automated tests were added or run, and HOI4 was not launched; live-game validation remains with the user.
No model, model asset, model source image, or 3D pipeline was created, inspected, or modified for this accord.
The Event 016 catalog worker updated the workbook’s `Events!C17` and regenerated the export CSVs.
For this commit, the parent rebuilt the workbook from the committed LFS baseline, applied only the approved sentence to `Events!C17`, and generated a matching Events CSV row; the pre-existing workbook and export changes for Events 012, 042, 070, and other clusters remain only in the unstaged working-tree version.
The umbrella diplomatic-rewards plan remains partial because four focus completion rewards still call `dhrondan_focus_add_diplomatic_credit`; that separate scan/removal/deprecation step is queued.
The accord tranche remains incompletely evidenced until the weighted-logic auditor returns scenario-specific results or records the exact route blocker.
