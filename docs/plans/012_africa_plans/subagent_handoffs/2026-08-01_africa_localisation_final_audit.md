# Event 12 Africa localisation final audit

Date: 2026-08-01

Scope: Event 12 English localisation, scripted localisation, player-facing GUI text, event logs and details, evolutions, cluster text, focus and decision references, sovereign and public country names, diaspora wording, world-order wording, action costs and durations, and asset consumer names.

## Changed files

- `localisation/english/012_africa_world_union_war_l_english.yml` removed six duplicate package-successor and package-certification definitions and added the two renamed defeated-review option labels.
- The parent-owned `events/012_africa_world_package_union_war.txt` now uses `africa_world_package.726.review` and `africa_world_package.727.review`; the localisation keys in the changed file match those script option names.
- No gameplay, interface, asset, tag, model, workbook, or acceptance-ledger files were edited by this localisation pass.

## Changed keys and display behavior

Removed duplicate definitions from `012_africa_world_union_war_l_english.yml`:

- `africa_world_commit_package_successor`
- `africa_world_commit_package_successor_desc`
- `africa_world_certify_package_exile`
- `africa_world_certify_package_exile_desc`
- `africa_world_certify_package_breakup`
- `africa_world_certify_package_breakup_desc`

The retained definitions in `012_africa_world_order_l_english.yml` are the dynamic target-aware versions using `[FROM.GetNameDef]`.

Added labels aligned to the parent script rename:

- `africa_world_package.726.review: "Open the defeated review"`
- `africa_world_package.727.review: "Open the defeated review"`

Before this pass, the package successor and certification keys had duplicate definitions across two localisation files, and the `.726.d` and `.727.d` option identifiers collided with event-description keys. After the pass, the Event 12 localisation package has one definition per key and the renamed review options have visible labels.

## Missing key list

No confirmed missing localisation keys remain in the audited Event 12 source surfaces.

The exact required Afaan Oromoo strings remain intentionally absent from runtime localisation pending native full-string review; they were not invented, translated, or added by this pass.

## Duplicate key list

The final Event 12 scan reports 17 `012*` English localisation files, 4,140 keys, 4,140 unique keys, and zero duplicate groups.

The former six duplicate key groups are listed above. The former `.726.d` and `.727.d` option collisions are resolved by the parent script rename to `.726.review` and `.727.review`.

## Scripted localisation issue list

No broken scripted-localisation references were confirmed.

The three Event 12 scripted-localisation files contain 35 definitions and 622 branches, and every literal `localization_key` branch resolves to an English key. The scan's `Capital` method hit is the vanilla `[ROOT.Capital.GetName]` scope accessor, not a missing custom method.

## Dynamic text opportunities

- The 102-action matrix has complete name, selector description, full-result, partial-result, and failure-result coverage for all 102 actions, with 612 expected fields present.
- Existing dynamic action cost text references 13 `africa_quote_cost_*` fields, and the action effect source sets all 13 fields.
- Existing duration-contract text references `africa_quote_duration_minimum`, `africa_quote_duration_maximum`, and `africa_quote_duration_days`, and the action effect source sets all three fields.
- Action objective class is stored in the action constants and target records but is not surfaced as a player-facing dynamic label; a future narrow pass could add an objective-class scripted-localisation branch without changing mechanics.
- The four mission description keys are intentionally generic and do not make stale duration or cost claims, but they could expose the active action objective or duration when the owner is ready for a wording pass.
- The charter GUI already uses dynamic target names such as `[?africa_selected_targets^0.GetName]` and has no remaining `GetTag` display leakage.

## Cross-surface mismatch notes

- Static source-reference coverage is complete: 84 Event 12 source files yielded 1,390 localisation references with zero missing keys, and the 12 event files yielded 598 explicit references with zero missing keys.
- Decision and scripted-GUI references yielded 158 checked fields with zero missing keys.
- Focus coverage is 394 executable focus IDs with zero missing name or description keys; idea coverage is 80 IDs with zero missing name or description keys; achievement coverage is 44 IDs with zero missing name, description, or tooltip keys; character coverage is 16 blocks with zero missing name or description keys.
- Sovereign title localisation remains separate from council and party names, so no council-style ruler naming was found where decorated sovereign identity is intended.
- No invented country tags were found in audited public-facing names, and no additional obscene source-language names were found.
- Diaspora wording explicitly describes voluntary return and no forced relocation or coercion. Unrelated historical action text still contains phrases such as “forced settlement” and “forced labour”; those require an owner decision if the historical wording is to be softened without changing mechanics.
- The world-order war package still contains implementation-facing terms such as “War Ledger Cleanup”, “bounded war arrays”, “target pool”, and “dossier”. This was recorded but not changed because the parent requested no broad wording pass.

## File encoding concerns

The changed localisation file remains UTF-8 with BOM (`EF BB BF`). The prior package-wide check found all 17 Event 12 English localisation files using UTF-8 BOM. Existing one-space localisation indentation was preserved to avoid unrelated churn.

## Recommended fixes

- Native-language owner review: add the two exact Afaan Oromoo strings only after full-string native review, in the localisation surface named by the country-package owner; do not substitute an unverified translation.
- Objective-label owner review: consider a dynamic objective-class label in `localisation/english/012_african_union_l_english.yml` backed by `common/scripted_localisation/012_africa_scripted_localisation.txt` and the existing `africa_action_objective` data.
- Wording owner review: replace the implementation-facing `africa_world_package.734.t` and `africa_world_package.734.d` text in `localisation/english/012_africa_world_union_war_l_english.yml` if the owner accepts a broader in-world wording pass.
- Country-package owner review: decide whether the sovereign value “The King of the Zulu” in `localisation/english/012_africa_priority_member_characters_l_english.yml` should be made more idiomatic; this is a wording decision, not a coverage defect.
- Historical-language owner review: verify whether the “forced settlement” and “forced labour” action-result wording is intentionally historical and distinct from the diaspora system's voluntary-relocation guarantee.

## Validation and skipped checks

- Event 12 localisation key scan: 17 files, 4,140 keys, zero duplicate groups.
- Event 12 source-reference scan: 1,390 references across 84 source files, zero missing keys; explicit event scan: 598 references across 12 event files, zero missing keys.
- Scripted-localisation scan: three files, 35 definitions, 622 branches, zero missing literal branch keys.
- Decision and GUI scan: 158 checked references, zero missing keys.
- Focus, idea, achievement, and character scans: 394, 80, 44, and 16 checked IDs or blocks respectively, each with zero missing required keys.
- Action contract scan: all 102 actions have the six expected player-facing fields, and the dynamic cost and duration fields are populated by the corresponding script effects.
- Live Hearts of Iron IV execution and in-game GUI rendering were skipped because agents must not launch the game and this was a text-only audit; the user owns live consumer validation.

## Unresolved wording decisions

The exact Afaan Oromoo strings, the “The King of the Zulu” idiom, the implementation-facing war-ledger terminology, the historical forced-settlement wording, and the future objective-class label remain owner decisions. No fallback text was introduced.

No commit was created, per the parent instruction.

