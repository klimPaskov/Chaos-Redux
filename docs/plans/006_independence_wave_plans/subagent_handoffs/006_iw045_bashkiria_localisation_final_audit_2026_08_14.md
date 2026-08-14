# IW-045 Bashkiria final localisation and documentation audit — 2026-08-14

## Current re-audit addendum — supersedes the original disposition

**LOCALISATION COVERAGE PASS WITH NON-BLOCKING PROSE FOLLOW-UP.** The original audit below is retained as historical evidence, but its missing-key blocker and cosmetic/corridor findings are superseded by this addendum.

### Resolved findings

- `bsk_congress_charter` and `bsk_congress_charter_desc` are present. The visible constitutional idea no longer exposes a raw key. The description is concrete, concise, and consistent with the constitutional route.
- The localisation file now has 142 unique keys, with no exact duplicate keys locally or duplicate definitions elsewhere under `localisation/english`.
- All 60 route-cosmetic keys are present as four complete 15-key matrices. Each matrix contains the base name, `_DEF`, and `_ADJ` keys plus name, `_DEF`, and `_ADJ` variants for democratic, communism, neutrality, and fascism.
- `common/countries/cosmetic.txt` defines `BSK_INDEPENDENCE_WAVE_CIVICX`, `BSK_INDEPENDENCE_WAVE_AGRARIANX`, `BSK_INDEPENDENCE_WAVE_SOCIALISTX`, and `BSK_INDEPENDENCE_WAVE_EMERGENCYX`. `common/scripted_effects/006_independence_wave_bashkiria_package_effects.txt` consumes all four with `set_cosmetic_tag`. The provisional setup deliberately starts with the civic identity.
- `independence_wave_bsk_hold_frontier_congress_desc` now says `keep Ufa owned and controlled` instead of exposing `state 651`.
- `independence_wave_bsk_project_failure_effect_tt` and the event document no longer contain the scoped sentence semicolons identified below.
- The canonical decision `independence_wave_bsk_open_ural_network_corridor` now displays `Open the Volga–Ural Network Corridor`. Its description, shared focus helper, event document, and workbook summary all use the Volga–Ural geographic identity. The shorter workbook phrase `Volga–Ural corridor` is not a material contradiction.
- The event document's claim of complete scoped localisation is now supported by the current idea, party, category, mission, decision, tooltip, and cosmetic matrices.

### Current required audit lists

- Missing keys: none.
- Exact duplicate keys: none.
- Broken scripted localisation: none found. The scoped file uses direct variable and constant substitutions rather than scripted-localisation calls.
- File encoding: valid strict UTF-8 with the required BOM.
- Sourced quotations: none present, so no quotation text required preservation.
- Dynamic text opportunities: the category, founding duration, thresholds, and failure loss already use dynamic integer-formatted values. Completion tooltips still use vague qualitative terms such as `improve`, `improve sharply`, and `rise` where existing constants could show exact changes.
- Cross-surface mismatches: no current missing-key, cosmetic-name, charter-name, or corridor-name mismatch. Workbook `Events!C7` and the exported Event ID 6 Details field remain exactly mirrored under the hashes recorded below.
- Decision/category rendered overflow: unresolved because the installed HOI4 MCP package still exposes no decision-category inspection or rendering route. Source review is not treated as equivalent rendered evidence.

### Remaining prose and ownership follow-up

- Effect tooltips remain mechanically vague. `independence_wave_bsk_depots_effect_tt`, `independence_wave_bsk_guards_effect_tt`, `independence_wave_bsk_communities_effect_tt`, the four route effect tooltips, `independence_wave_bsk_sovereignty_effect_tt`, and `independence_wave_bsk_network_effect_tt` should show exact signed dynamic changes when the parent next authorizes a localisation patch.
- Semantic aliases remain. The inactive parallel idea-name pairs, old project-name aliases, BSK-specific unused cost keys, and helper-ID localisation listed in the original audit should be removed only after sibling ownership is settled.
- `bsk_oilfield_council` remains a defined and localised idea without a package lifecycle consumer. The gameplay owner must decide whether to wire or remove it before localisation cleanup.
- The event document still includes asset and admission status prose. This is acceptable in a technical package document but must remain outside player-facing localisation and workbook text.

### Current focus MCP evidence

The current shared tree was re-inspected and re-rendered after the Volga–Ural helper alignment.

- Inspect revision: `261a21cd2a97de42d51654d6b015fdb404ef256a418b87364dbdacb4392c4895`.
- Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d52ab0ddbb485d09512f723d86862292c4b0f58aa936fa04824f78d2bbf22697/712723aa7d1194619c4babf4d807107649bad26f5b7f39c6c52d7915bfc5d7ce/focus-inspect.261a21cd2a97de42.json`.
- HTML render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0d77d09877e1b590360efa25ab41318842ab937b401e728e6f8b9999a2389bef/85ba570d26e1ba03df3f37f70b978eebe7634360b023add73b0923411a97a00e/independence_wave_focus_tree.focus.html`.
- SVG render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/02a33b6e26cd319131d46e708aa7260478638f337d0a28a6efe1f823d448af30/c6273e4df4fcd2986949c668111ce7d4fb15c77bd90909cf8a36bfe832ce7151/independence_wave_focus_tree.focus.svg`.
- JSON render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/edd19123e7474d4790c8d83a4102a367a9b8620c5929a74f01290857c6f23b52/3e3364b973997d4c1075ca1153b32d06b26043a51865f31ebb17e8b10b48eb87/independence_wave_focus_tree.focus.json`.
- The MCP resolves all 184 focus titles. Current validation remains false because of 14 shared/installed focus diagnostics outside IW-045 localisation. No BSK focus-title or helper-localisation defect was reported.

### Current validation and change boundary

- Parsed all 142 keys and verified exact duplicate absence locally and across English localisation.
- Verified the 60 cosmetic keys against four tag definitions and four route consumers.
- Rechecked all canonical category, mission, decision, idea, party, tooltip, and shared-cost keys.
- Rechecked strict UTF-8 and BOM from raw bytes.
- Re-ran mandatory current-source focus inspect and render.
- No source, gameplay, workbook, export, staging, or commit edit was made. This addendum is the only re-audit change.
- No simplification or fallback was used. No current localisation-coverage blocker remains. Decision UI rendered overflow and shared-tree diagnostics remain explicit validation limitations.

## Disposition

**BLOCKED on one missing visible idea name/description pair and several player-facing clarity defects.** The canonical Bashkiria decision category, founding mission, and ten project IDs all have matching name and description keys. The constitutional government effect installs `bsk_congress_charter`, however, and neither `bsk_congress_charter` nor `bsk_congress_charter_desc` exists in English localisation. The idea will therefore expose its raw key when active.

This was a read-only audit of gameplay, localisation, documentation, focus consumers, and the workbook receipt. The only changed file is this handoff. No gameplay, localisation, workbook, export, staging, or commit operation was performed.

## Sources inspected

- `localisation/english/006_independence_wave_bashkiria_l_english.yml`
- `common/decisions/006_independence_wave_bashkiria_decisions.txt`
- `common/decisions/categories/006_independence_wave_bashkiria_categories.txt`
- `common/ideas/006_independence_wave_bashkiria_ideas.txt`
- `common/scripted_effects/006_independence_wave_bashkiria_package_effects.txt`
- `common/script_constants/006_independence_wave_bashkiria_constants.txt`
- BSK call sites in `common/national_focus/006_independence_wave_focus.txt`
- `docs/events/006_independence_wave/bashkiria_package.md`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw045_bashkiria_catalog_update_2026_08_14.md`
- `docs/spreadsheets/chaos_redux_events_catalog.xlsx`, read-only `Events!A7:C7`
- The three exported catalog CSV files, read-only hash and mirror checks

The required offline wiki localisation, data-structure, trigger, effect, modifier, scope, on-action, event, decision, idea, AI, and national-focus pages were consulted. Installed vanilla localisation formatter/object documentation was also consulted.

## Missing key list

| Missing key | Visible consumer | Recommended fix |
| --- | --- | --- |
| `bsk_congress_charter` | `common/ideas/006_independence_wave_bashkiria_ideas.txt:25`; installed by `independence_wave_install_bsk_constitutional_government` in `common/scripted_effects/006_independence_wave_bashkiria_package_effects.txt:174` | Add a specific constitutional-route idea name in `localisation/english/006_independence_wave_bashkiria_l_english.yml`. Suggested name: `Bashkir Congress Charter`. |
| `bsk_congress_charter_desc` | Same idea and route | Add a concise description that explains the congress charter, elections, civic administration, and community guarantees without inventing new mechanics. |

No missing name/description keys were found for the canonical category, founding mission, or ten canonical project IDs.

## Canonical decision ID and key resolution

The decision source, cleanup list, and active-project trigger agree on these canonical IDs:

| Canonical ID | Name key | Description key | Coverage |
| --- | --- | --- | --- |
| `independence_wave_bsk_hold_frontier_congress` | same as ID | `_desc` suffix | Present |
| `independence_wave_bsk_secure_frontier_depots` | same as ID | `_desc` suffix | Present |
| `independence_wave_bsk_integrate_frontier_guards` | same as ID | `_desc` suffix | Present |
| `independence_wave_bsk_register_bashkir_communities` | same as ID | `_desc` suffix | Present |
| `independence_wave_bsk_settle_former_host_ledgers` | same as ID | `_desc` suffix | Present |
| `independence_wave_bsk_ratify_constitutional_autonomy` | same as ID | `_desc` suffix | Present |
| `independence_wave_bsk_adopt_agrarian_compact` | same as ID | `_desc` suffix | Present |
| `independence_wave_bsk_convene_socialist_councils` | same as ID | `_desc` suffix | Present |
| `independence_wave_bsk_establish_frontier_emergency_command` | same as ID | `_desc` suffix | Present |
| `independence_wave_bsk_codify_durable_sovereignty` | same as ID | `_desc` suffix | Present |
| `independence_wave_bsk_open_ural_network_corridor` | same as ID | `_desc` suffix | Present |

The category key `independence_wave_bashkiria_frontier_compact_category` and its `_desc` key are present.

The canonical decisions use shared cost keys from `006_independence_wave_decisions_l_english.yml`: `independence_wave_cost_administration_light`, `independence_wave_cost_administration_standard`, `independence_wave_cost_security_standard`, `independence_wave_cost_diplomatic_standard`, `independence_wave_cost_security_major`, and `independence_wave_cost_strategic`. All six shared keys are present.

## Duplicate and orphan key list

There are **no exact duplicate keys** within the 92-key Bashkiria file and no exact duplicate definitions for those keys elsewhere under `localisation/english`.

There are several semantic duplicates or unconsumed aliases:

- `bsk_bashkiria_frontier_compact` duplicates the active `bsk_bashkir_frontier_compact` wording but has no source consumer.
- `bsk_agrarian_land_compact` duplicates active `bsk_steppe_land_compact` wording but has no source consumer.
- `bsk_frontier_workers_council` duplicates active `bsk_oilfield_workers_council` wording but has no source consumer.
- `bsk_emergency_frontier_command` duplicates active `bsk_frontier_emergency_command` wording but has no source consumer.
- `bsk_oilfield_council` is a defined idea with localisation, but the package effect lifecycle never adds or removes it. This is a gameplay ownership question, not a localisation-only deletion candidate.
- The old project aliases `independence_wave_bsk_secure_oilfield_depots`, `independence_wave_bsk_register_community_compacts`, `independence_wave_bsk_establish_emergency_command`, and `independence_wave_bsk_open_volga_ural_corridor`, including their descriptions, are not canonical decision IDs and have no source consumers.
- `independence_wave_bsk_cost_administration_light`, `independence_wave_bsk_cost_administration_standard`, and `independence_wave_bsk_cost_strategic` are not consumed. The decisions use the shared `independence_wave_cost_*` keys instead.
- `independence_wave_bsk_focus_integrate_frontier_guards`, `independence_wave_bsk_focus_open_ural_network_corridor`, `independence_wave_bsk_focus_register_bashkir_communities`, `independence_wave_bsk_focus_secure_frontier_depots`, and `independence_wave_bsk_focus_settle_former_host_ledgers` localise effect/helper IDs, not focus IDs, and have no visible source consumers.
- The four `BSK_INDEPENDENCE_WAVE_*` cosmetic-tag families are not referenced by `set_cosmetic_tag` or another searched consumer. Keep them only if parent-owned route identity wiring is still planned.

Recommended cleanup is to remove aliases only after the parent confirms no pending sibling patch depends on them. The repository is heavily concurrent, so this audit does not treat unused text as permission to delete it.

## Scripted localisation issue list

No scripted-localisation call or broken scripted-localisation reference occurs in the scoped Bashkiria file.

The category and mission use direct variable/constant substitutions with integer formatters, and the format tokens are syntactically consistent with the installed localisation documentation. The direct `§` and `£` tokens occur in ordinary localisation, not scripted-localisation definitions.

## Dynamic text opportunities

- `independence_wave_bsk_hold_frontier_congress_desc` exposes the internal phrase `state 651`. Replace it with the player-facing state name `Ufa`, preferably through a supported state-scope localisation object if the consumer context proves it resolves safely. At minimum, write `Ufa` rather than a database number.
- Completion tooltips repeatedly say values “improve”, “improve sharply”, “rise”, or “fall” even though the effects use stable constants. Exact signed dynamic values would make project comparisons intelligible. Candidate keys include `independence_wave_bsk_depots_effect_tt`, `independence_wave_bsk_guards_effect_tt`, `independence_wave_bsk_communities_effect_tt`, all four route effect tooltips, `independence_wave_bsk_sovereignty_effect_tt`, and `independence_wave_bsk_network_effect_tt`.
- The category correctly shows current Congress Cohesion and Frontier Readiness, their maximum, and their stability target dynamically. Preserve those tokens.
- The founding-mission duration and failure loss are dynamic and integer-formatted. Preserve those tokens.

## Cross-surface mismatch notes

- The event document claims “complete scoped localisation keys,” but `bsk_congress_charter` and its description are missing. Revise this validation claim after the keys are added.
- The event document says “Ten paid projects.” The source has one founding mission plus ten projects, which is internally consistent. The route and corridor summaries also agree with the canonical decision set.
- The document uses `is_independence_wave_bashkiria_package`, matching the category and package core. Some decision blocks use the alias trigger `is_independence_wave_bsk_package`; this is mechanically outside the present localisation audit but should remain visible to the owning integration review.
- The workbook summary says the Volga–Ural corridor shapes the package. The canonical playable decision is named `Open the Ural Network Corridor`, while the shared focus helper and documentation use `Volga–Ural`. This is understandable but inconsistent. Pick one public name and mirror it across the canonical decision, docs, and workbook.
- The workbook summary names constitutional, agrarian, socialist, and emergency routes, matching the decision and document surfaces.
- The workbook summary says oilfield and railway administration, mounted frontier security, community registration, former-host ledgers, and the corridor shape the compact. That accurately mirrors the implemented package premise without exposing numeric tuning.
- The documentation’s “source-placeholder portrait” and absent runtime override are implementation/asset-status notes. They belong in a handoff or limitations section, not in player-facing event detail text. The workbook correctly omits them.

## Workbook `Events!C7` mirror receipt

The receipt in `006_iw045_bashkiria_catalog_update_2026_08_14.md` is verified against the workbook and exports.

- `Events!A7 = 6`
- `Events!B7 = Independence Wave`
- `Events!C7` contains the preserved general Independence Wave paragraph followed by the additive Bashkiria paragraph.
- The exported Event ID 6 `Details` field is exactly equal to workbook `Events!C7`.
- Workbook SHA-256: `f739ffbefe358917eb2f6843a3fb0d234206e8cca19dc300b7812847ab8beb92`.
- Events CSV SHA-256: `d486dffcb1208a4c97ed147629379e520084f822c1e4f3bd4ddb564f5bcab170`.
- Clusters CSV SHA-256: `0bdd2e73f4c556af5fbdb028a2bbae258ef4d3402450d4bb112a63644047d299`.
- Scenarios CSV SHA-256: `66ea4a5802862c1c72f0f3e8ead04cb4f1bfde5e62f88411e3b29f64cb5cf760`.

The C7 Bashkiria paragraph is clear and appropriately non-mechanical. Its only reconciliation issue is the `Volga–Ural corridor` versus canonical `Ural Network Corridor` name split.

## File encoding concerns

- `localisation/english/006_independence_wave_bashkiria_l_english.yml` is valid strict UTF-8 and begins with the required UTF-8 BOM.
- The document and catalog receipt are valid strict UTF-8. Markdown files do not require a BOM.
- The apparent `0â€“100` and `Volgaâ€“Ural` sequences seen through default PowerShell output are console-decoding artifacts. The source bytes decode correctly as `0–100` and `Volga–Ural` under strict UTF-8.

## Prose-quality issue list

### Vagueness

- Most effect tooltips use qualitative terms such as “improve sharply”, “rise”, “gains”, and “pays the cost” without the exact values needed to compare projects. Dynamic constants should replace this ambiguity.
- `independence_wave_bsk_sovereignty_effect_tt` and `independence_wave_bsk_network_effect_tt` list broad ledger categories without quantifying their changes.

### Bloat

- `independence_wave_bsk_register_bashkir_communities_desc` stacks four settlement types and three abstract nouns. It is readable but can be tightened to the concrete act: register each community’s representation, rights, and duties.
- The event document’s validation paragraph combines source validation, map evidence, focus evidence, probability limitations, setup surfaces, and admission status in three long sentences. Split audit evidence from admission status.

### Obvious explanation

- The category’s last line is useful because it states the threshold condition and is not redundant.
- The decision descriptions generally add context beyond their titles. No title-repeating description requires deletion.

### Repetition

- Multiple alias idea and decision keys repeat identical descriptions, as listed in the orphan section.
- `independence_wave_bsk_host_ledgers_effect_tt` repeats much of the decision description instead of prioritising the actual ledger changes.

### Overcomplication

- “secure ownership and control of state 651” combines engine vocabulary with a raw database ID. Use “keep Ufa owned and controlled” or equally direct player language.
- “Former-host property, border, population, and recognition ledgers” is an internal system inventory. State what the agreement settles in-world, then show exact visible ledger changes separately.

### Style-rule repair

- `independence_wave_bsk_project_failure_effect_tt` contains a sentence semicolon: `Security fall; Instability rises.` Replace it with two sentences or a conjunction.
- `docs/events/006_independence_wave/bashkiria_package.md` contains three sentence semicolons, on the focus/portrait line, the flag line, and the validation line. Rewrite them as separate sentences.
- The event document contains implementation-history/status phrasing such as “currently a source-placeholder archive”, “no generated runtime flag is installed”, and “pending parent review”. This is acceptable only as explicit limitations/audit documentation, not as player-facing prose. Keep it out of localisation and workbook fields.
- No em dash occurs in the Bashkiria localisation. En dashes in `Volga–Ural`, `blue–green–white`, and numeric ranges are not em dashes.
- No staccato chain, dialectical hedge, staged contrast formula, fake quotation, or empty dramatic filler was found in the scoped localisation.

## Sourced-quotation preservation notes

No sourced or attributed quotation appears in the localisation, event document, or workbook C7 mirror. There is therefore no quotation text to preserve or normalise.

## Focus consumer MCP evidence and limitation

Mandatory read-only focus inspection and rendering were run against `independence_wave_focus_tree` after the current BSK helper call sites were present.

- Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3a7c60ef9a95ed37287260b3afb8e9db45adad9d02fa3d3b49c00abf3eddacdf/401409ba1bbf58f5faaa5a169885ad352cfbae5ab8cb01758d00d640c6cbf772/focus-inspect.8ddba04dcb6226a4.json`
- HTML render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b1bd43c2ce2d29af97948ad2eb42c6bb77d5f150b57a85e79c1ea13a65572f9e/4a40a4d45da02c99db891831d4a801acdc78d73c9f11651c710d7b74cce7ec19/independence_wave_focus_tree.focus.html`
- SVG render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c51a07eee7fcbe60e40231211902e20aa68aff6e2313b7484db6ee1705a5bf19/f172328f19fe24d21b315c79224eeedb64bbda6a3f6c5e6f7c722ddeb8f00d3a/independence_wave_focus_tree.focus.svg`
- JSON render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4414499d0057dcff6c2933035a687e82740c98d0b3695c25662498f649856367/8ac6605324b638bf39a38d924aab46096d42981ffe4b67d2cec793ce8f9a58a9/independence_wave_focus_tree.focus.json`

The MCP inventory resolved all 184 shared focus titles, and the BSK package adds guarded helper effects rather than new focus IDs. No missing focus title/description key is attributable to IW-045. The current tree validation remains false because of 14 workspace-wide focus diagnostics, including installed-vanilla missing sprites and shared layout/reference findings unrelated to these BSK localisation consumers.

The installed HOI4 MCP package provides no decision-category localisation renderer or decision UI overflow inspection route. Therefore decision/category overflow, wrapping, and rendered cost alignment remain **unresolved**. Source review and the focus renderer are not equivalent evidence for that missing decision UI route.

## Recommended fixes

1. Add `bsk_congress_charter` and `bsk_congress_charter_desc` to `localisation/english/006_independence_wave_bashkiria_l_english.yml`.
2. Replace `state 651` in `independence_wave_bsk_hold_frontier_congress_desc` with `Ufa` or a proven dynamic state-name token.
3. Replace vague effect language with exact dynamic gains/losses where existing constants expose those values, preserving all current mechanic names and format tokens.
4. Replace the semicolon in `independence_wave_bsk_project_failure_effect_tt` and the three sentence semicolons in `docs/events/006_independence_wave/bashkiria_package.md`.
5. Reconcile `Volga–Ural Corridor` and `Ural Network Corridor` across the canonical decision keys, event document, and workbook C7 mirror.
6. After sibling ownership is settled, remove unconsumed aliases and BSK-specific cost keys, or wire them intentionally. Do not delete `bsk_oilfield_council` localisation until the gameplay owner decides whether the defined but unused idea should be wired or removed.
7. Correct the document’s “complete scoped localisation keys” claim only after the missing constitutional idea keys land.

## Validation performed

- Parsed all 92 keys in the scoped localisation file and checked exact duplicates locally and across `localisation/english`.
- Cross-referenced category, mission, decision, cleanup, active-project, idea, party-name, cosmetic-tag, tooltip, shared-cost, and shared-focus-helper consumers.
- Verified strict UTF-8 decoding and the localisation BOM from raw bytes.
- Read workbook `Events!A7:C7` without saving it, compared C7 exactly to the exported Event ID 6 Details field, and verified the receipt hashes.
- Ran the mandatory current-source focus inspect and render routes and recorded their artifact URIs and limitations.

## Skipped meaningful validation and why

- Decision/category rendered overflow and clickable-cost presentation could not be inspected because the installed MCP exposes no decision UI inspection or rendering route.
- No live HOI4 validation was performed. Runtime consumer validation belongs to the user and parent boundary.
- No localisation patch was applied because the parent explicitly requested a read-only audit.

## Unresolved wording decisions

- Whether the public corridor name should be `Volga–Ural Corridor` or `Ural Network Corridor` requires parent selection because changing the canonical decision name may affect accepted route terminology.
- The exact constitutional idea title can be `Bashkir Congress Charter` or another established package term, but it must remain distinct from the matured `Bashkir Frontier Compact` idea.
- Exact numeric effect-tooltip wording should be derived from the final accepted constants and shared effect semantics during the localisation patch, not guessed from qualitative labels.

## Simplifications, omissions, and blockers

- No simplification or fallback was used.
- The audit remains blocked on the missing `bsk_congress_charter` name/description pair.
- Decision/category rendered overflow remains unresolved because the required MCP route is unavailable.
- The shared focus tree’s 14 blocking diagnostics are outside this bounded localisation task and prevent a clean whole-tree validation claim.
