# Event 012 Africa Final Localisation Audit Handoff

Date: 2026-08-09

Owner: `chaosx_localisation_auditor`

Scope: `localisation/english/012_africa*.yml`, `localisation/english/012_african_union_l_english.yml`, and `common/scripted_localisation/012_africa*.txt` only.

No gameplay, GFX, workbook, or other documentation file was edited during the localisation pass. No commit was created.

## Outcome

The Event 012 localisation audit and narrow patch are complete within the assigned source scope.

The final owned set contains 20 YML files and 4,569 unique localisation keys. The final audit found no duplicate keys, leading-space keys, `:0` keys, or YML files without a UTF-8 BOM.

An explicit Event 012 source-reference scan checked 1,823 localisation references from the linked event, decision, mission, focus, character, achievement, GUI, super-event, country, cosmetic, equipment, technology, subunit, model, promoted Tier A, RSA, world-order, animation, and tooltip sources. No referenced localisation key was missing from the inspected localisation set or its valid shared dependencies.

The four Event 012 scripted-localisation files contain 46 unique `defined_text` names. No duplicate scripted-localisation name, missing `localisation_key` branch, or direct `§` or `£` formatting character was found. No scripted-localisation edit was required.

## Missing Key List

None.

## Duplicate Key List

The following four duplicate sovereign keys were removed from `localisation/english/012_africa_promoted_tiera_l_english.yml`:

- `africa_fictional_the_green_sovereign`
- `africa_fictional_living_rivers_sovereign`
- `africa_fictional_stoneborn_sovereign`
- `africa_fictional_ancient_hosts_sovereign`

The retained definitions in `localisation/english/012_africa_priority_member_characters_l_english.yml` are specific male personal ruler names:

- `africa_fictional_the_green_sovereign`: `Mosi Kijani, the Baobab Mirror King`
- `africa_fictional_living_rivers_sovereign`: `Sefu Maji, the Waterfall River Sovereign`
- `africa_fictional_stoneborn_sovereign`: `Kebede Saltglass, the Salt-Glass Emperor`
- `africa_fictional_ancient_hosts_sovereign`: `Bongani Eclipse, the Leopard Eclipse King`

The final duplicate count is zero.

## Scripted Localisation Issues

None found. All 46 inspected names are unique, all inspected text branches provide localisation keys, and no scripted-localisation source contains direct formatting icons or colour characters.

## Afaan Oromoo Boundary

Exactly two untranslated Afaan Oromoo values remain, each appearing once:

- `africa_absurd_regnal_name_01: "qaama saalaa koo xuuxaa"`
- `africa_absurd_regnal_name_02: "haadha kee waliin wal qunnamtii saalaa raawwadhe"`

Both strings are confined to fictional male sovereign and court flavour in `localisation/english/012_africa_priority_member_characters_l_english.yml`. Neither string is used in an identifier. No additional untranslated source-language obscenity was added or retained in the owned localisation set.

The corresponding fictional character definitions inspected in `common/characters/012_africa_fictional_characters.txt` use `gender = male`. No council portrait wording or council portrait requirement was introduced.

## Changed Files and Key Groups

### `localisation/english/012_african_union_l_english.yml`

Materially changed keys:

- `chaosx.nr12.230.a.tt`
- `chaosx.nr12.230.b.tt`
- `africa_record_compact_promotion_proof_tt`
- `africa_promote_compact_host_tt`
- `africa_reopen_compact_promotion_docket_tt`
- `africa_select_offer_sacred_ecological_compact_desc`
- `africa_action_result_offer_sacred_ecological_compact_full`
- `africa_action_result_offer_sacred_ecological_compact_partial`
- `africa_action_result_offer_sacred_ecological_compact_failure`
- `africa_select_awaken_stone_cohort_desc`
- `africa_select_train_gorilla_heavy_infantry_desc`
- `africa_select_organise_pan_sappers_desc`
- `africa_compact_signature_secure_distinct_role_desc`
- `AFRICA_UNITED_KINGDOMS_communism`
- `AFRICA_UNITED_KINGDOMS_communism_DEF`
- `AFRICA_CONTINENTAL_COMMAND`
- `AFRICA_CONTINENTAL_COMMAND_DEF`
- `AFRICA_CONTINENTAL_COMMAND_communism`
- `AFRICA_CONTINENTAL_COMMAND_communism_DEF`
- `AFRICA_CONTINENTAL_COMMAND_neutrality`
- `AFRICA_CONTINENTAL_COMMAND_neutrality_DEF`

The succession text now states that the Charter mandate passes without transferring land, cores, or sovereignty. Compact promotion costs use live constants. Ecological compact and special-unit text describes requirements, full success, partial success, failure, withdrawal, cleanup, and the one-success limit where visible.

### `localisation/english/012_africa_priority_member_focus_l_english.yml`

Materially changed keys:

- `africa_priority_build_distinct_institution_desc`
- `africa_priority_build_distinct_institution_tt`

Package and generic-legitimacy commentary was replaced with direct institutional consequences.

### `localisation/english/012_africa_priority_member_l_english.yml`

Materially changed keys:

- `africa_survey_priority_member_candidate_tt`
- `africa_resolve_priority_member_requalification_tt`

The tooltips now describe the country, territory, institution, obligation, and later recognition requirement rather than an internal action card or package activation.

### `localisation/english/012_africa_promoted_tiera_l_english.yml`

Materially changed keys:

- `africa_promoted_gorilla_starting_desc`
- `africa_promoted_tiera_reveal_package_tt`
- `africa_promoted_tiera_advance_mechanic_tt`

The four duplicate sovereign keys listed above were removed. Package installation and dormant-mechanic language was replaced with recognition, sovereign seating, and direct institutional progression.

### `localisation/english/012_africa_world_order_l_english.yml`

Materially changed keys:

- `africa_world_order.6.a.tt`
- `africa_world_package.3.d`
- `MIDDLE_EASTERN_CONCERT`
- `MIDDLE_EASTERN_CONCERT_DEF`
- `EUROPEAN_CONCERT`
- `EUROPEAN_CONCERT_DEF`
- `EUROPEAN_CONTINENTAL_COMMAND`
- `EUROPEAN_CONTINENTAL_COMMAND_DEF`
- `ASIAN_IMPERIAL_CONGRESS`
- `ASIAN_IMPERIAL_CONGRESS_DEF`
- `NORTH_AMERICAN_COMMAND`
- `NORTH_AMERICAN_COMMAND_DEF`
- `SOUTH_AMERICAN_COMMAND`
- `SOUTH_AMERICAN_COMMAND_DEF`
- `SOUTH_AMERICAN_CONCERT`
- `SOUTH_AMERICAN_CONCERT_DEF`

Public names now use `Middle Eastern Union`, `European Union`, `European State`, `United Empires of Asia`, `North American State`, `South American State`, and `South American Union`. Administrative identifiers remain unchanged for script compatibility. Two source comments record that public names identify countries while administrative labels remain internal.

### `localisation/english/012_africa_world_sponsorship_l_english.yml`

Materially changed keys:

- `africa_world_package.20.b.tt`
- `africa_world_choose_material_sponsorship_tt`
- `africa_world_fulfil_material_sponsorship_tt`
- `africa_world_close_sponsorship_after_refusal_tt`

The text now distinguishes promised and fulfilled shipments, displays the live shipment values, and describes refusal as preventing sponsorship while affecting rivalry and diplomacy.

### `localisation/english/012_africa_world_union_war_l_english.yml`

Materially changed keys:

- `africa_world_open_union_convention_desc`
- `africa_world_open_union_convention_req`
- `africa_world_open_unanimous_union_review_desc`

Internal package-actor wording was replaced with participating continental governments and constituent consent.

### Mechanical key-indentation normalization

Leading indentation was removed from localisation key lines in these files without changing their player-facing values unless another material key is listed above:

- `localisation/english/012_africa_diaspora_protocol_l_english.yml`
- `localisation/english/012_africa_elephant_l_english.yml`
- `localisation/english/012_africa_super_events_l_english.yml`
- `localisation/english/012_africa_world_asia_north_america_l_english.yml`
- `localisation/english/012_africa_world_union_war_l_english.yml`

`localisation/english/012_africa_achievements_l_english.yml` and `localisation/english/012_africa_event_log_l_english.yml` contained concurrent changes during the pass. This subagent did not author those changes.

No Event 012 scripted-localisation file was changed.

## Dynamic Localisation Added or Fixed

The following formerly hardcoded political-power costs now display their script constants:

- Compact promotion proof: `[?constant:africa_compact_promotion.proof_pp_cost|0]`
- Compact promotion: `[?constant:africa_compact_promotion.promotion_pp_cost|0]`
- Reopened promotion docket: `[?constant:africa_compact_promotion.reopen_pp_cost|0]`

Material sponsorship fulfilment continues to display the live promised shipment quantities. No new `defined_text` block was necessary.

## Cross-Surface Mismatch Notes

Resolved mismatches:

- Public country names no longer expose administrative `Court`, `Command`, `Congress`, or `Concert` labels.
- Compact promotion localisation now matches live proof, refusal, reopening, and promotion stages.
- Sponsorship localisation now covers consent, refusal, fulfilment, and rivalry instead of claiming that a package was installed.
- Union-convention text now requires participating governments and constituent consent rather than an installed actor.
- Succession text distinguishes mandate transfer from territorial or sovereign transfer.
- Integration and ecological-compact text preserves protection, consent, withdrawal, and cleanup distinctions.

No inspected public country-name value contains `Council`, `Court`, `Command`, `Congress`, `Concert`, `Group`, `Network`, `Administration`, `Directorate`, or `Board`.

## Prose Quality Repairs

### Vagueness

Generic `package actor`, `installed package`, `dossier`, and `mechanic` wording was replaced with the government, sovereign, shipment, institution, settlement, obligation, or territorial consequence visible to the player.

### Bloat

Promotion, succession, ecological compact, and special-unit passages now lead with the live requirement or consequence. Redundant implementation explanation was removed.

### Obvious Explanation

Text explaining that a button was a helper, a mechanic was a package, a gate belonged to generation, or a receipt was one-use was replaced by the actual player-facing rule.

### Repetition

The four duplicate generic sovereign definitions were removed in favour of the retained personal male rulers. Repeated package-stage explanations were consolidated into recognition and progression language.

### Overcomplication

Overloaded semicolon constructions were split into direct sentences. Long noun stacks around package installation, model readiness, and promotion evidence were reduced while preserving requirements and consequences.

### Style-Rule Repair

Meta implementation history, fallback language, administrative map names, and exposed asset-manifest wording were removed. Dynamic tokens, costs, conditions, actor references, and outcome distinctions were preserved.

## Sourced-Quotation Preservation

The inspected super-event localisation contains attributed quotations associated with Marcus Garvey, the General Act of the Berlin Conference Article 34, Carl von Clausewitz, and Percy Bysshe Shelley's `Ozymandias`.

Their quotation wording and attribution were preserved verbatim. Only key indentation was normalized in the super-event file.

## MCP Evidence

### Events

Event inspect artifact:

`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c697599e5f4f86886665cce6b2d30fbeaba9cf6fe10844cf5ebb8015a8ca80d9/367e1ee89a925eaaf853849e7b79d73eaa5159dbe33d1dc1436f4535bfef782f/event-scan-73e269b481e4.json`

Event overview render manifest:

`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a6051714ca5f69f73fb2c81f25f002a62c84224ee095ae67c0d614ea9c8bbff8/5041bcdb24f508b65de2a17ae4c70ddef57faab0f6e55c1b66fb18a9283509ba/event-overview-73e269b481e4-manifest.json`

The event inspection and render were partial because the workspace projection was large. The overview selected 240 nodes and omitted 40,895 nodes, so it is useful structural evidence but not complete visual coverage.

### Focuses

Main continental focus inspect artifact:

`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/017c0e1d103cab24c5b47e397b45eaa6d61f3311750336c960431bd9d6d81f79/464078c1f2fe195801c6d49b216c90da8b75217f7c2c74fa031b8d95729aae23/focus-inspect.ecdc77535513f2a1.json`

Main continental focus HTML render:

`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/30b7ff8468b9cd943b92eccbbf06a4da9ab20a23193a6202ce4a07562f3a22dc/f832386c56dba1c204c62562e76f7b59855d677236a5bc87d0b28dfe245af7eb/africa_continental_focus_tree.focus.html`

The inspector resolved 276 focus titles and reported 14 blocking layout diagnostics. Those layout problems are outside localisation ownership. A parallel batch for individual priority-member and world focus trees was terminated before returning artifacts, so those trees do not have individual MCP visual proof from this pass.

### Scripted GUI

Charter window inspect artifact:

`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/51ae1bd05250bac485610352bc41937ff0c8133c2b4e706ee0a1f3a58e3811b7/8e399b04925b293d90dec62a37cb0c775bb35d14c6db03b1f1e7f9504bf70495/gui-inspect.5c6921ab6ba77286.json`

The GUI inspector reached the repository-wide diagnostic ceiling and returned truncated results, including reported overlaps, clipping, unresolved contexts, and a dropped text-overflow diagnostic. Normal, long-text, and missing-localisation renders at 1920 by 1080 failed with the exact blocker `ARTIFACT_STORAGE_LIMIT`. Visual overflow clearance therefore remains unverified and source review is not treated as equivalent GUI evidence.

### Technology

Technology scan artifact:

`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8044bd7d20dd4f956804a61313705dce830fd586bfddcf77a1ac7b9a1c4c9d97/4bcea636163c7bbc489dc5a834df5a69d9bdf2cad4794fe235d35c6db0bc2529/technology-scan-a0a8bfbc4c2d.json`

Gorilla heavy-infantry technology render manifest:

`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7f011dc15ca63bef3ac9dbf339fc3ef27e3b2a434dd5c120cd58a1b41ead267e/ef8a96e327b3eb00f00ffcc9d83d74734d729a81932630fcb2652b676eec03a0/technology-technology-a0a8bfbc4c2d-manifest.json`

Gorilla heavy-infantry technology SVG:

`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/603cd380a83fbb8eb1f8e084ad1ca5f60ef54a37ad91cff27fe5437e24db12f9/e2b6bc1f88162c576c0dd77af7623c2764e48815ba1da5ec80acb21329a86dda/technology-technology-a0a8bfbc4c2d.svg`

The technology scan was partial, and the rendered technology reported `sourceAccurate = false`. The Technology Tree Viewer is absent from the installed package, so no independent read-only viewer evidence is available.

## Validation Performed

- Audited 4,569 unique localisation keys across the 20 owned YML files.
- Confirmed zero final duplicate keys.
- Confirmed zero leading-space keys and zero `:0` keys.
- Confirmed UTF-8 BOM on every owned YML file.
- Checked 1,823 explicit Event 012 source localisation references with zero missing references.
- Audited 46 scripted-localisation names with zero duplicate names and no direct formatting characters.
- Confirmed exactly one occurrence of each required Afaan Oromoo value.
- Confirmed no inspected public country-name value exposes an administrative institution label.
- Reviewed the scoped diff for trailing whitespace after the final public-name correction.

No Hearts of Iron IV process was launched. No in-game validation is claimed.

## Unresolved Dynamic and Visual Limitations

- Some long Charter action descriptions remain structurally dense because one localisation value must describe requirements, commitment, full result, partial result, failure, and cleanup. Removing those clauses would conceal live gameplay behavior.
- Values can only be made dynamic where gameplay exposes a variable, constant, actor, target, state, or scripted-localisation route. No new gameplay helper was added because gameplay files were outside ownership.
- GUI overflow remains unverified because all requested GUI renders failed with `ARTIFACT_STORAGE_LIMIT`.
- Individual priority-member and world focus trees lack individual MCP artifacts because the inspection batch was terminated.
- Technology render accuracy remains uncertain because the MCP result was partial and reported `sourceAccurate = false`.

## Simplifications, Omissions, and Blockers

No localisation feature was intentionally simplified or omitted. The MCP limitations above are evidence blockers, not accepted substitutes for visual or engine validation.

No mechanic gap requiring a new implementation plan was identified. This file is the requested final audit handoff.
