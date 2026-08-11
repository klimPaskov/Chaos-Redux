# Event 012 Final Current-Source Localisation Audit — 2026-08-11

## Outcome

The current Event 012 localisation source is mechanically complete for every resolved gameplay reference and received 20 narrow text fixes across achievements, Nile/Gold priority-member content, and promoted Tier A content. After the audit returned, the parent applied all 32 queued W4 replacements plus two matching government-facing follow-ups in `localisation/english/012_africa_world_union_war_l_english.yml`; the earlier file-write blocker is therefore closed. The HOI4 MCP still returns `ARTIFACT_MANIFEST_INVALID` for the Event 012 event, dedicated GUI, technology, and several focus-render routes.

No gameplay, general documentation, or spreadsheet files were edited. Nothing was staged or committed.

## Source Coverage

- Audited 21 Event 012 English YML files matching `012_*_l_english.yml`.
- Parsed 4,694 keys, all unique.
- Checked 2,520 filtered direct localisation references from 133 Event 012 source files, representing 2,214 unique keys. All resolve.
- Checked 1,214 `localization_key` branches across four Event 012 scripted-localisation files, representing 967 unique keys. All resolve.
- Checked all 394 Event 012 focus IDs. Every focus has a title and `_desc` key.
- Checked all 44 Event 012 achievement IDs. Every achievement has `_NAME`, `_DESC`, and `_tooltip` keys.
- Checked all nine Event 012 technologies. Every technology has a name and description.
- Found no stale `SCN-011`, `scenario 011`, `fake scenario`, or `retired scenario` text in the audited Event 012 localisation and linked event, decision, focus, scripted-localisation, or interface source.

## Required Audit Lists

### Missing keys

None among the audited direct gameplay references, scripted-localisation branches, focuses, achievements, or technologies.

### Duplicate keys

None. All 4,694 parsed Event 012 localisation keys are unique.

### Scripted-localisation issues

None found. The 46 Event 012 `defined_text` names are unique, every branch key resolves, and the scripted-localisation files contain no literal formatting characters that violate repository rules.

### Dynamic text opportunities

Implemented dynamic capital-state naming in `africa_priority_nubia_nile_survey_tt` and `africa_priority_great_zimbabwe_plateau_survey_tt` with `[ROOT.Capital.GetName]`. No further safe dynamic substitution was identified without changing gameplay ownership or meaning.

### Cross-surface mismatches

- Fixed `africa_promoted_tiera_record_nonhuman_great_power_war_victory_desc`. The old wording incorrectly described the separate host great-power war as the Stoneborn member war. The new wording matches the current distinct war-tracking implementation.
- No stale retired-scenario wording remains on current Event 012 surfaces.
- A case-sensitive audit of all 165 uppercase Event 012 public-name keys found no value using `Council`, `Court`, `Command`, `Directorate`, `Administration`, `Authority`, `Package`, `Actor`, `Terminal`, or `Proof`. Current country-name surfaces therefore remain direct. The two required Afaan Oromoo strings remain isolated to fictional ruler/court flavour as detailed below.
- W4 package, terminal, actor, and proof vocabulary was replaced after the audit by the parent using the queued text below, with two additional direct-government follow-ups for `africa_world_package.758.d` and `africa_world_ratify_union_constitution_desc`.

### File encoding concerns

None found. All 21 Event 012 English localisation files retain UTF-8 BOM encoding. No leading-space keys, `:0` suffixes, or malformed key lines were found.

### Prose-quality issues

- Vagueness: fixed `host drift`, `existing capital state`, and an unclear great-power victory description.
- Bloat: shortened stage and cost explanations without removing their dynamic cost tokens.
- Obvious explanation: removed wording that narrated internal package maturation instead of the visible condition.
- Repetition: consolidated repeated maturation language across the four promoted Tier A response families.
- Overcomplication: replaced `authored institutions`, `complete the ... packages`, and abstract roster/proof wording with direct public-world consequences.
- Style-rule repair: removed process/meta vocabulary such as package, authored, roster, tracking, and proof from the patched achievement and promoted Tier A strings. No em dashes or sentence semicolons remain in the audited Event 012 set.
- W4 style repair: all 32 queued replacements and the two related follow-ups are now applied.

### Sourced quotations

The inspected super-event quotation surfaces attributed to Marcus Garvey, Berlin Conference Article 34, Carl von Clausewitz, and Percy Bysshe Shelley were not edited or repunctuated. Their verbatim wording and attribution remain preserved. Historical quotation accuracy was not independently researched in this localisation-only pass.

## Patched Localisation

### Changed files and keys

`localisation/english/012_africa_achievements_l_english.yml`

- `africa_the_clause_is_the_country_tooltip`
- `africa_republic_of_many_capitals_tooltip`
- `africa_walls_courts_and_caravans_tooltip`

`localisation/english/012_africa_priority_member_l_english.yml`

- `africa_priority_nubia_nile_survey_tt`
- `africa_priority_nubia_record_corridor_failure_desc`
- `africa_priority_great_zimbabwe_plateau_survey_tt`
- `africa_priority_great_zimbabwe_record_corridor_failure_desc`

`localisation/english/012_africa_promoted_tiera_l_english.yml`

- `africa_promoted_tiera_nonhuman_rampage_cost`
- `africa_promoted_tiera_nonhuman_rampage_cost_blocked`
- `africa_promoted_tiera_nonhuman_rampage_cost_tooltip`
- `africa_promoted_tiera_forest_actor_rampage_cost`
- `africa_promoted_tiera_forest_actor_rampage_cost_blocked`
- `africa_promoted_tiera_forest_actor_rampage_cost_tooltip`
- `africa_promoted_tiera_stoneborn_rights_violation_cost`
- `africa_promoted_tiera_stoneborn_rights_violation_cost_blocked`
- `africa_promoted_tiera_stoneborn_rights_violation_cost_tooltip`
- `africa_promoted_tiera_stoneborn_human_member_war_cost`
- `africa_promoted_tiera_stoneborn_human_member_war_cost_blocked`
- `africa_promoted_tiera_stoneborn_human_member_war_cost_tooltip`
- `africa_promoted_tiera_record_nonhuman_great_power_war_victory_desc`

### Display before and after

- Nile and Gold surveys previously referred generically to the `existing capital state`; they now name `[ROOT.Capital.GetName]` directly.
- Corridor-failure descriptions previously exposed `host drift`; they now say that a change of Charter host ended the survey.
- Achievement tooltips previously used internal or process-like language such as `clause roster`, `untracked annexation`, `authored institutions`, and `packages`; they now describe clauses, member annexation, public institutions, and named settlements directly.
- Promoted Tier A costs previously described package stages and maturation. They now identify the applicable polity or crisis and state the before/after cost plainly while preserving every `constant:africa_promoted_tiera_cost.*` token.
- The great-power victory text previously tied the victory to the Stoneborn member war. It now describes the distinct host great-power war and its actual completion conditions.

### Dynamic localisation changed

- Added `[ROOT.Capital.GetName]` to the two survey tooltips.
- Preserved all existing dynamic cost tokens and formatting codes in every edited cost key.

### Prose before-and-after summary

- Vagueness: generic capital and host-state language became named state and Charter-host language.
- Bloat: stage explanations became concise before/after conditions.
- Obvious explanation: internal maturation narration was removed.
- Repetition: repeated package-stage phrasing was standardized around the actual polity or crisis.
- Overcomplication: abstract roster/proof and package terminology became direct player consequences.
- Style-rule repair: process/meta vocabulary was removed from all 20 patched keys.

All sourced quotations, dynamic tokens, formatting codes, costs, requirements, names, and consequences were preserved except for the intentional correction to the great-power-war description. That correction aligns text with the current distinct host-war implementation.

## W4 Write Blocker and Applied Replacements

Repeated `apply_patch` attempts against `localisation/english/012_africa_world_union_war_l_english.yml` failed with `Failed to write file` while other localisation and handoff files remained writable. After the file freeze, the parent applied these exact 32 replacements and replaced the two remaining actor-facing values with direct government wording:

```yaml
 africa_world_package.702.d: "The convention is before the members who consented to our continental settlement. Each assembly records its own answer."
 africa_world_package.720.d: "A rival continental government has demanded a constitutional settlement. We can accept a sovereign armistice, reject the demand, or ask the attacker to hear counterterms."
 africa_world_package.727.t: "Terms for the Defeated Compact"
 africa_world_package.729.d: "The defeated compact has accepted a confederal settlement under a recorded constitutional mandate."
 africa_world_package.730.d: "The settlement releases the compact's constituent governments and records their withdrawal from the defeated union."
 africa_world_package.732.d: "The defeated compact still requires a constitutional settlement."
 africa_world_package.740.t: "The Defeated Compact Review"
 africa_world_package.740.d: "A successor may carry the compact's mandate forward. If no valid successor exists, the government in exile or the remaining constituents must receive a lawful settlement."
 africa_world_package.742.d: "No successor can lawfully receive the compact's mandate. Its constituent governments will return to separate sovereignty."
 africa_world_package.743.d: "The nominated successor has received the compact's constitutional mandate through the established transfer."
 africa_world_package.745.t: "The Compact Breaks Up"
 africa_world_package.745.d: "The old compact has ended. Its constituent governments will carry forward their own choices."
 africa_world_package.747.d: "The successor now carries the inherited constitutional mandate among the continent's recognised governments."
 africa_world_package.748.t: "A Final Settlement Is Recorded"
 africa_world_package.748.d: "The compact's final settlement is ready for review by every participating government."
 africa_world_package.751.d: "Not every participating government has answered the final union review."
 africa_world_package.752.t: "Unanimous Political Consent"
 africa_world_package.752.d: "Every participating government has approved the union and met the voluntary constituent standard. The host may record their consent."
 africa_world_package.752.a: "Record the consent"
 africa_world_package.753.t: "The Last Government's Settlement"
 africa_world_package.753.d: "The final review asks this government to confirm its constitutional settlement."
 africa_world_package.754.t: "A Government Rejects the Settlement"
 africa_world_package.754.d: "The final review cannot close while one government rejects its settlement."
 africa_world_package.755.d: "Every participating government has supplied a final settlement, and enough sovereign governments remain for the political review."
 africa_world_package.755.a: "Record the settlements"
 africa_world_package.757.t: "The Final Review Is Blocked"
 africa_world_package.757.d: "A government has refused the final settlement. Earlier approvals remain on record, and the review can be reopened after consent changes."
 africa_world_package.758.t: "Reopen the Final Review"
 africa_world_impose_constitutional_settlement_desc: "Record confederal submission without annexing the defeated compact."
 africa_world_open_defeated_package_review: "Open the Defeated Compact Review"
 africa_world_open_unanimous_union_review_desc: "Ask every participating continental government for independent approval and confirmation that its constituent governments consent."
 africa_world_open_last_standing_review_desc: "Ask every participating government to confirm its final political settlement."
```

## Afaan Oromoo and Character-Flavour Constraint

The two exact required strings remain once each and nowhere else in current runtime source:

- `africa_absurd_regnal_name_01: "qaama saalaa koo xuuxaa"`
- `africa_absurd_regnal_name_02: "haadha kee waliin wal qunnamtii saalaa raawwadhe"`

Both occur only in `localisation/english/012_africa_priority_member_characters_l_english.yml`. Their corresponding fictional characters in `common/characters/012_africa_fictional_characters.txt` are male. No additional Afaan Oromoo string was found in Event 012 runtime source.

## HOI4 MCP Evidence

### Focus inspection and rendering

All eight Event 012 focus sources returned focus-inspection artifacts. Successful render artifacts were produced for the priority-member, Asia, Europe, and Middle East trees. The continental, North America, Oceania, and South America renders failed with `ARTIFACT_MANIFEST_INVALID`.

- Continental inspect: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6a702f2745c43eea2aebab06b16ceea8264fcfc4660c695d8f554d2e77f10bfb/cdd34b8992bc5e33f2c90185a223fbd14306d2733267562788588b368eb86fa4/focus-inspect.319d0e7b8cebb2e6.json`
- Priority inspect: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d6b8eb38d5e3287c31c2157e73749f4b70532d99332f5feeadc930cec62e5d5a/8f0cc30ecf2bff549cf994bafd7040f175a6f643efaa70af2005468fc0fd22f3/focus-inspect.319d0e7b8cebb2e6.json`
- Asia inspect: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/40f9c7fa81383cd405418cdae2171b27470c15a63797c728ce81b9e80ffc9abc/8327dc3ca677e83cd4ec201c4b98a840f6c6f157a38f6ab570da07d4b8ba876d/focus-inspect.319d0e7b8cebb2e6.json`
- Europe inspect: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c6048423d125775faa8910bb381f60ad1eefd955d898f6593d889925c07be36a/95bdc81f604ee945ea1899b5b7251fa77c11e958e018393489e2753c792d1bab/focus-inspect.319d0e7b8cebb2e6.json`
- Middle East inspect: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e7bb8e8bc6bf1223477a263ca7894c6851ae0b2d2bb8a12354cbc1225dfc0895/3f592462628347e2c4e86caa80fd28ae0850b959d8139f0411d49312fb0be382/focus-inspect.319d0e7b8cebb2e6.json`
- North America inspect: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/eba26c28bc69ee9044f911358341d224704acfb585bebbd229004f736e98d8f9/41942989db8b7a70dcd30ec6508aefa9ac1bf093139b8a660b303e8d4b21ff0c/focus-inspect.319d0e7b8cebb2e6.json`
- Oceania inspect: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2e9de2096494d18145e649ec14fade4cbf72e199ee447dfdb7a5bee36f81a757/d2df949101c8dd4b9022e9a55d7ad9906ddf369f81c523db35424bf07c23a44c/focus-inspect.319d0e7b8cebb2e6.json`
- South America inspect: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a3c4a22d746ac4dbe29f690eb7201200f73dc81b58f61da81f478c021848628e/b5a7faa02448a27b38fbedf74d2c37fb207bde6ac797a67039c6582ee3f5e7a9/focus-inspect.319d0e7b8cebb2e6.json`
- Priority render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c7b5e8be08120d936ab079c3ca5727aa1477707782b4d7c409837ec7f18a812b/60116d1fcede5e7a261c87d8f38abc75b892d2963d8dba0615bdf4ea20d8a106/africa_priority_member_focus_tree.focus.html`
- Asia render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7281650fa7c6106949d579615e63ccab587023f61b5fa569d5a2065ee24333db/fa4049d597c7a01c90d5412b64b3df10e91b6c5d907cd71c94255dc1b2d89b5e/africa_asia_world_focus_tree.focus.html`
- Europe render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4c1f7ec3b2f9dfd9317719ed71afc5a071676d222edb08cbda4a5dc77d3129fc/1edf396a608be2bb411c40573771d1e338cbe3360eb63f71629699903046251d/africa_europe_world_focus_tree.focus.html`
- Middle East render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0a009854b4edb85b620d35485b4be25fe7543ca467124b78f9d49d8f59c91665/b151a26e27c0301e86e6bd48d66964e4c90ae6e7e2197e163d430edb9bf6b1ad/africa_middle_east_world_focus_tree.focus.html`

Inspection diagnostics included unrelated installed continuous-focus sprite findings; the continental tree also returned layout warnings outside this localisation-only ownership.

### Event, GUI, and technology blockers

- Event inspect for `chaosx.nr12.1` failed with `ARTIFACT_MANIFEST_INVALID`; no usable event-render artifact was returned.
- GUI inspect and `normal`, `long-text`, and `missing-localisation` renders for `africa_charter_window` at 1920x1080 failed with `ARTIFACT_MANIFEST_INVALID`.
- Technology inspect and render calls for the elephant and gorilla technologies failed with `ARTIFACT_MANIFEST_INVALID`.
- The Technology Tree Viewer is absent from the installed package.

These MCP failures are exact blockers. Source reference and encoding checks are not treated as equivalent visual or engine evidence.

## Meaningful Validation

Post-patch source validation returned `FILES=21 KEYS=4694 UNIQUE=4694 DUP=0 BOM_BAD=0 MALFORMED=0 OROMO1=1 OROMO2=1`. The retired-scenario and prose-style scans remained empty. Direct source-reference, scripted-localisation, focus, achievement, and technology coverage all remained complete after the edits.

Skipped or unavailable validation is limited to the MCP routes documented above and live in-game consumer validation, which belongs to the user under repository policy.

## Remaining Decisions, Simplifications, and Blockers

- The 32 queued W4 replacements and two related government-facing follow-ups are applied; the final parent validation reruns the Event 012 key and reference audit.
- Rerun the failed MCP event, GUI, technology, and focus-render routes after the artifact provenance manifest is repaired.
- No design mechanic was invented, simplified, or omitted in this localisation pass. No separate improvement-loop plan was warranted.
