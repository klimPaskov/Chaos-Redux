# CXT setup and CBRN decision repairs

Status: source repairs implemented and reviewed; live execution is unverified.
Acceptance basis: the user reported the console command creating an empty CXT country, five error lines, and overlapping CBRN decision text, and requested repairs.

## Repairs

| Reported symptom | Cause addressed | Implemented repair |
| --- | --- | --- |
| `memfile:8` country event receives scope None | The bootstrap evaluated a country event after `change_tag_from` invalidated the current country context. | Queue `chaosx_test_country.1` from CXT before transferring the player, with `change_tag_from` last. |
| CXT exists but units, equipment and projects are absent | The failed receiver dispatch bypassed the complete initialization chain. | Preserve and dispatch the ordinary full receiver rather than a country-only substitute. |
| Two generated-character name failures | CXT lacked a country keyed generated-name pool. | Add 32 male first names, 32 female first names, 64 shared surnames and 24 callsigns, providing 4,096 full name combinations. |
| Two absent Black Friday dynamic-modifier removals | Refresh removed inactive sale modifiers unconditionally. | Guard both country removals and the corresponding two leader removals with `has_dynamic_modifier`. |
| CBRN decision title and cost/status overlap | Long left titles collided with long right-aligned custom-cost text in the native decision row. | Shorten seven titles and seven blocked statuses; use existing resource icons and preserved dynamic amounts for seven ready cost rows. |

The receiver delay is one game hour, configured by the file-scoped `@CXT_SETUP_DELAY_HOURS` and inserted as a numeric meta argument.
The country switch occurs immediately and the complete setup is queued for the following game hour.
An invocation already scoped to CXT keeps the existing immediate receiver path.
The receiver remains triggered-only, CXT-gated, and unchanged from the task baseline.
Its originating country and capital event targets carry through the queued chain.

## Setup coverage and preservation

`source_contract_checks.json` records unchanged private setup helpers, unchanged receiver bytes, preserved initialization and refresh calls, and 87 static unit templates producing 261 static divisions.
The retained chain builds special facilities, supplies an occupation fixture, completes projects and technologies, grants Chaos Warfare, activates camp systems, fills equipment stockpiles, refills resources, creates the roster, and synchronizes registered content.
Package-owned runtime registrations remain connected through the existing shared registry helpers.
No roster, equipment, technology, project, facility or registry branch was removed to bypass an error.

`cbrn_source_checks.json` records exactly 21 edited public localisation keys, all fourteen preserved dynamic ready-cost amount tokens, and unchanged descriptions and full requirement/cost tooltips.
No CBRN cost, availability predicate, completion effect, AI weight or GUI geometry changed.
`black_friday_guard_checks.json` records four presence guards with unchanged removal order, country/leader scope and sale activation branches.
`name_pool_checks.json` records distinct pool entries and enough name combinations for the static roster plus generated scientists and leaders.

## Native visual evidence

The matching before fixture reproduces the screenshot overlap in the installed vanilla `decision_item` consumer.
The production MCP after render includes fourteen scenarios covering all seven decisions with ready and blocked custom-cost strings, the installed `hoi_16mbs` font, real tuning amounts, 1920 x 1080 resolution and scale 1.
Parent review of `cbrn_native_rows.png` found separate, readable title and cost/status glyph regions in every row, including the three-resource civilian fitting row.
The contact sheet consists of unscaled 512 x 41 native-row crops extracted from the MCP scenario-matrix SVG's embedded original PNGs.
`cbrn_native_row_receipts.json` records their identities and verifies the first embedded PNG against the production full-render hash.
`cbrn_gui_final_before.json`, `cbrn_gui_final_after.json`, `cbrn_gui_before_inspect.json`, `cbrn_gui_after_inspect.json`, `cbrn_scenarios.json` and `cbrn_text_sources.json` retain source, fixture, render and comparison receipts.
The final comparison reports 3,802 changed pixels; the rendered scene has no missing assets or unresolved font/text inputs.
An exploratory fixture disabled the entire row and selected the native crossed background; final fixtures keep the row normal and supply action-button states independently.
No shared background or asset was edited as a consequence of that fixture correction.
The MCP lists four unsupported retained native rendering properties, including shader/vertical-alignment behavior, so this evidence establishes text separation without proving live click behavior, eligibility, payment or every engine rendering property.

## Source references and audits

Required offline wiki core pages were consulted alongside Event modding, Decision modding, Country creation and the interface/scripted-GUI pages.
Installed vanilla effects and triggers documentation supplies country-event delay, player transfer, generated-character, meta-effect and dynamic-modifier semantics.
Vanilla `common/names/00_names.txt` documents unique full generated-name combinations and provides the country keyed pool precedent.
Vanilla `CHI_scripted_effects.txt` provides guarded dynamic-modifier removal, and `interface/countrydecisionview.gui` supplies the actual native row consumer.
The country-package auditor reviewed generated-name schema and preserved bootstrap coverage; parent review expanded its initial small pool to match the retained roster.
The localisation auditor reviewed wording, custom-cost key coverage, unchanged tooltip content and amount-token preservation.
Their reviewed handoffs are `country_name_handoff.md` and `cbrn_wording_handoff.md`.

## Files and Git scope

Tracked source changes are limited to the bootstrap effect, the new CXT name pool, twenty-one CBRN localisation keys, the bootstrap timing paragraph in `docs/testing/chaosx_test_country.md`, and two reusable scheduling rules in the events skill.
`tracked_source_changes.patch` and `tracked_source_identities.json` preserve task-baseline deltas and identities.
The applied Black Friday repair belongs to an existing untracked package with extensive unrelated content.
Its full source remains in the working tree; only `black_friday_guards.patch` and repair evidence are versioned here, preserving the unrelated package draft.
Unrelated working-tree edits to the localisation, test documentation and skill are excluded from the scoped source commit.

## Simplifications, omissions and blockers

No gameplay simplifications or omitted requested source repairs were introduced.
Existing assets were reused; no art, icon or portrait production was required.
No live game launch or computer control was performed.
Live receiver execution and absence of engine errors remain unverified.
The required event inspection/render calls returned `EVENT_INSPECTED_PARTIAL` and `EVENT_RENDERED_PARTIAL` because large-workspace analysis deferred helper projections and lifecycle passes.
The focused graph includes no projected helpers and does not prove the bootstrap initialization sequence executes.
The comparison call returned `EVENT_REVISION_NOT_CACHED`, with blocker “Requested event graph revision is not cached.”
`cxt_followup_before.json`, `cxt_followup_after.json`, `cxt_followup_render.json` and `cxt_followup_compare.json` retain those exact results.
The source preservation checks are not presented as equivalent engine evidence.

## Skills

Used: `chaos-redux-events`, `chaos-redux-decisions-missions`, `chaos-redux-scripted-gui`, `chaos-redux-subagents`, and `skill-creator` guidance.
Updated: `chaos-redux-events`, with reusable receiver-before-player-transfer scheduling and numeric meta duration guidance.
No event-specific test-country context was added to the skill.
