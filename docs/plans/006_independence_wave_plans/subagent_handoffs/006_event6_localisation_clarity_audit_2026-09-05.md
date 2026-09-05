# Event 006 Localisation Clarity Audit

Date: 2026-09-05

Status: implemented

## Scope

This bounded audit covered the player-facing names, descriptions, custom costs, trigger tooltips, and effect tooltips referenced by `common/decisions/006_independence_wave_decisions.txt` and `common/decisions/categories/006_independence_wave_categories.txt`, with supporting checks in the Event 006 English localisation and scripted-localisation registry. Gameplay, AI, weights, assets, GFX, GUI, and spreadsheet files were not edited.

## Changed files and keys

- `localisation/english/006_independence_wave_decisions_l_english.yml`
  - `independence_wave_cost_selected_formable_commit_blocked`
- This handoff.

Before: `Unavailable until the selected formable family, carrier, member consent, and material requirements are all valid.`

After: `Select an eligible regional union, secure member consent, and meet its resource requirements.`

The revised line removes the implementation terms `family` and `carrier`, leads with the required player action, and preserves the existing selection, consent, and resource gates.

## Audit results

### Missing keys

None among the 190 explicit `name`, `desc`, `custom_cost_text`, `custom_effect_tooltip`, and direct tooltip references extracted from the two assigned decision/category source files.

### Duplicate keys

None among those 190 referenced keys across `localisation/english/*.yml`.

### Scripted localisation

No missing selector definitions were found for the dynamic cost calls inspected. `GetIndependenceWaveProvisionalCapitalCostText`, `GetIndependenceWaveProvisionalCapitalCostBlockedText`, the four diplomatic transport cost selectors, and `GetIndependenceWaveFormableCommitCostText` are defined in `common/scripted_localisation/006_independence_wave_scripted_localisation_registry.txt`.

### Dynamic text opportunities

No new dynamic localisation is required for the assigned core file. Cost amounts already resolve from script constants, transport alternatives resolve through scripted localisation, and the selected formable cost resolves through `GetIndependenceWaveFormableCommitCostText`.

### Pre-event exposure and cross-surface notes

No player-facing Event 006 decision/category localisation says that content is queued, records pre-event history, or describes a pre-event wave-pressure state. Category visibility is owned by source triggers rather than localisation. The assigned category source uses Event 006 activation guards, including `is_independence_wave_event6_player_surface_allowed`, `is_independence_wave_event6_local_content_active`, or post-setup/active-country gates. Localisation alone cannot prove engine-time visibility, so the parent should retain the source-side pre-event visibility audit as the controlling evidence.

The event catalog workbook was not inspected or edited. No spreadsheet wording handoff is needed for the one changed blocked-cost line because it is a decision UI requirement rather than an event-detail/catalog field.

### File encoding

The changed localisation file remains UTF-8 with BOM (`EF-BB-BF`). No encoding concern was found in the two core Event 006 English localisation files checked.

### Prose quality

- Vagueness: repaired the selected-formable blocked-cost line by naming the player actions and requirements.
- Bloat: removed the redundant opening `Unavailable until` construction and compressed four implementation-oriented nouns into three player-facing requirements.
- Obvious explanation: no other assigned line was changed solely to narrate an obvious button action.
- Repetition: no duplicate sentence or repeated requirement requiring a safe localisation-only repair was found.
- Overcomplication: removed `formable family` and `carrier`, which expose internal registry concepts.
- Style-rule repair: no em dash, semicolon, staccato chain, prompt fragment, or update-history phrasing was introduced.

### Cost wording requiring owner review

- `independence_wave_cost_security_standard_factory` and its blocked variant display four spent resources plus one committed civilian factory. This exceeds the decision skill's four-cost presentation ceiling if factory commitment is counted as a fifth spendable cost. The key is not referenced by the assigned core decision file, and changing the text would conceal gameplay, so no localisation-only patch was made. The owning decision agent should confirm the consumer and redesign the cost package if it is active.
- `independence_wave_cost_patron_balance` and its blocked variant retain `Every use` and `After the first` labels because the cost escalates after first use. Removing those labels without a replacement mechanic-aware display would make payment less clear.
- Cost rows broadly use centered-dot separators. They remain icon-first and readable, but the decision skill's canonical examples use spaces only. A repository-wide separator rewrite was outside this bounded audit.

### Sourced quotations

No sourced or attributed quotation appeared on the inspected decision/category surfaces. No quotation was changed.

## Validation and evidence

- Confirmed the changed key has a single English definition and remains referenced through the selected-formable dynamic cost path.
- Confirmed the seven inspected scripted-localisation cost selectors exist in the Event 006 registry.
- Re-ran the assigned explicit-key coverage and duplicate scan after the patch: 190 references, no missing keys, no duplicate definitions.
- The read-only HOI4 event service completed a repository event scan at revision `c61f85261a222e9683f1688e39eee9b264cdc8b2640dea815a6f20cf11e22e1e`; artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ae4776fb5389787f44efd16d1ee30de0410e0b357c6723ec142397ab86153c67/2d7647397b0bde3dc58bdcb2b82919fccc84be31f063b0267e6b04704f748dc9/event-scan-c61f85261a22.json`.

The event inspector rejected the attempted string selector for `chaosx.nr006` with `Invalid input: expected object, received string at selector`. The fallback scan was repository-wide and reported unrelated global diagnostics, so it does not provide a narrow Event 006 localisation render or engine proof. This is an MCP evidence limitation, not a substitute for the source checks above.

## Skipped validation and unresolved decisions

- No live-game validation was performed. Live consumer validation belongs to the user.
- No decision-category production render route was available in this bounded audit. The event graph tools do not render ordinary decision-category localisation, and this scope did not include a scripted GUI window.
- The active consumer, if any, of `independence_wave_cost_security_standard_factory` remains for the owning decision agent to confirm.
- No plan handoff beyond this audit was written because the proven localisation defect was narrow and repaired directly.

## Preservation confirmation

All dynamic tokens, formatting codes, resource texticons, costs, conditions, and consequences in the changed key set were preserved. The changed key contained no sourced quotation and no dynamic token.
