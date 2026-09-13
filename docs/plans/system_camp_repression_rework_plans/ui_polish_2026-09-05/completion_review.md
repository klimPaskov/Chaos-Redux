# Repression GUI and selected-site cost review

Disposition: implemented; parent source, native visual, interaction, balance, and bounded AI comparison reviews are complete.
The user authorized a bounded repression GUI repair, required reference images before layout work, excluded core Chaos Redux systems, removed mandatory `gui_rewrite` post-validation, and then requested correction of expensive fixed costs and debug-like presentation.
The older `review.md`, scalar proposal, and original interaction audit describe the first layout attempt; this review and the implemented cost contract supersede their pending-application claims.

## Implementation

`interface/camp_repression_ledger.gui` centers navigation and country-directive controls, aligns paired panels, gives cost text sufficient height, and implements the compact selected-site reference using native panels and existing buttons.
The selected card uses six equal 180 by 96 action groups with 148-pixel native buttons and cost fields.
Each decorative group follows its existing action's visibility; the first group also supports the territory-expansion alternative.
All decorations and text remain click-through, and existing action identities and entry points remain intact.
The name field reserves two native text lines for long location names.

`reference_compact.png` was generated and reviewed before the compact card was implemented.
Its accepted native mapping, provenance, and adaptations are in `reference_compact_note.md`.
It is a review reference rather than a baked runtime texture.

Selected-site quotes use actual detention, extermination, and Gulag building levels, with a minimum administrative charge for a registered site.
The new `camp_repression_site_cost` constants, trigger, effect, scripted-localisation, and English-localisation files keep display, inclusive affordability, and payment aligned.
The six selected GUI wrappers and their generic targeted decision equivalents use that quote.
Countrywide policies and their shared resource packages retain their separate prices.
See `cost_contract_review.md` and `common/scripted_effects/camp_repression_site_cost_effects.md` for exact formulas and consumers.

At one building level, a labor order costs 12 PP, 8 trucks, 1 train, and 12 support equipment.
It requires a retained reserve of 2 trucks, 1 train, and 3 support equipment in addition to payment.
The reserve is saved when the project starts and cleared through its lifecycle; changing the selected location cannot change that mission's requirement.
Inspection costs 13 PP; dismantlement costs 18 PP, 350 manpower, and 5 support equipment at the same size.
These are gameplay balance choices based on the work at a location, not prices per civilian death.

The selected-state figure reads the existing cumulative civilian-death total for the territory and explicitly includes all recorded causes and administrations.
The Situation page distinguishes current harm severity from the responsible country's cumulative attributed repression deaths.
The misleading latest-receipt field is not presented as a monthly total.
Core civilian accounting and casualty multipliers were not changed.
The repression-owned outbreak activation no longer records a stale receipt from an unrelated earlier loss; its ongoing losses enter the existing monthly receipt path when they occur.
Destroy Records now uses its shallow/deep evidence threshold for the outcome while retaining enemy proximity as an entry requirement.
The active territory-expansion gate no longer requires command power or infantry equipment that its payment effect never consumes.

## Evidence

`final_integrated` is the native MCP render after the explicit-state binding integration, source revision `8e35f34bc589841ad25596b6c70fed301fd394f745d14a85f4a62ae3e8d1d41c`.
It includes the normal screen and the explicit 720p/125-percent scenarios; its normal PNG is byte-identical to the already reviewed accepted normal PNG, SHA-256 `6ecdd865b3e1741d1450ad94dd11fdcd8eb89cdb374b51528d7a61732b28e255`.
The scripted-GUI layout source also retains its reviewed hash `3c320877508906c9f380d5d471be4ddd003c0f061c5c4a24edf990b8d900c45c`.
The final `gui_inspect` succeeded at that same integrated source revision, linking all 211 window elements with no skipped source or blocker; its successful tool result, immutable artifact address, and checksum are preserved in `integrated_inspect_tool_result.json`.
The desktop tool's first inspection call timed out after 180 seconds; the read-only retry used the installed 3.0.8 MCP stdio entry point with progress handling and completed successfully without modifying the package or configuration.

The final accepted MCP inspection and native scenario matrix are in `final_accepted`, source revision `751d591660a882899931c1486d832319d873855d02b2c5f3b931e906561a377f`.
This repeats the normal screen and all nine related scenarios with the corrected scroll selection after the repression action fixes; it supersedes earlier matrix evidence.
The parent viewed the current crop and matrix, and the source inspector linked all 211 window elements without a skipped source.
The reviewed output reports no text overflow, content crossing background edges, centering-expectation mismatch, conflicting click regions, click-bound mismatch, or missing sprite, texture, or localisation.
Other diagnostics remain explicit in the artifacts: intentional text and selection overlays, clipped off-viewport list rows, left-aligned two-line list labels, empty close-button font metadata, and unsupported or approximated engine fields.
Those findings were checked against the full-size native images and source; validator success alone was not used as visual acceptance.

The preserved baseline is `before_308`, with source revision `d679f95a1fa837b9a1b173b330b5f42a7d4d1f6ee76dcbc51d93a8178b54074b`.
`after_308` records the first scalar repair; `final_native` is an intermediate compact-card render superseded by `final_review` after wording and gallery-caption refinements.
`final_review` records the compact native normal screen and ten explicit scenarios at 1920x1080 scale 1, with source revision `20907bd957be9b32f68fa7239f168e9eb163c91bd1d1893481f7b191ba83693f`.
Its requested additional resolutions were overridden by explicit per-scenario resolutions; separate explicit scaled scenarios are required for smaller-screen and UI-scale evidence.
`final_scale` supplies that evidence using the explicit `scale_scenarios.json`: normal and long-name cases at 1280x720 scale 1, plus the long-name and maximum-control case at 1920x1080 scale 1.25.
Its manifest source revision is `5fe143d68ee80e2e33bc4002f3dbee87006a934642079ab3b21bd1415e8c49f1`; the parent reviewed the full smaller-screen image and all three scale cases with contained text and window bounds.
`final_long` provides full-size long-name and high-cost evidence with revision `c231232041cfb1866dddd57329d06ac74e64f7d1ad237254db4f0df6cf81fc4e`.
`final_situation`, `final_scroll`, and `final_category` preserve full-size Situation, corrected final-row selection, and launcher evidence.
`final_scroll` supersedes the older matrix's scroll fixture, whose header did not match the selected final row.
`final_pages/policy_directives` and `final_pages/accountability` preserve full-size evidence for those unchanged page sections.
The parent viewed every page, the long-name case, the corrected bottom row, and the normal click-region image; buttons occupy their native visible regions, decorative panels and cost labels do not add action regions, and cost lines remain within their action groups.
Each evidence folder retains its exact artifact manifests and hashes; concurrent workspace revisions are not inferred from file timestamps.
`final_scenarios.json` and `fixture_notes.md` distinguish route-coherent normal inputs from synthetic maximum-control stress cases.

The source evaluator exercised zero-building minimum charges, one and several camp levels, a Gulag-only location, exact funds, each resource one unit short, actual debit amounts, and reserve save/clear behavior.
Results are in `site_cost_arithmetic_scenarios.json`; changed helper and consumer boundaries are recorded in `site_cost_source_review.json`.
The arithmetic evaluator was an ephemeral `python -` invocation; its results and method are retained, but no standalone test runner was archived.
The decision auditor accepted the current coefficients after comparing L1, L3, the normal L5 shared-family ceiling, and conservative L6 cross-family headroom against the fixed mission duration and outcome.
Its findings on evidence branching, outbreak receipt timing, expansion affordability, and the size matrix are resolved in `interaction_audit.md`.
The six custom-cost actions retain their former nominal saving hints: 30 PP for each labor action, 45 for inspection, 60 for dismantlement, 25 for evidence, and 60 for the combined restricted action.
The AI specialist evaluated and compared the five decision scores and one mission score under the same four named L1/L5 adequate-funds and shortfall scenarios.
Both MCP comparisons completed with zero score changes and zero unresolved analysis inputs; `ai_hint_evidence` retains the before/after source, baseline inspection, scenarios, evaluation, comparison, and artifact provenance.
The comparison explicitly supplies eligibility outcomes to isolate score behavior from the separately audited payment gates; it does not simulate the engine's PP-saving scheduler or a running campaign.
The raw `ai_will_do` blocks were not changed.
After that comparison, a concurrent integration replaced parameter-style site helper calls with boolean calls receiving the explicit unscoped temporary `camp_site_cost_state_id`.
The parent retained and reviewed the integration: GUI callers initialize it from the selected state, decisions from `FROM.id`, and execution from its validated action state; payment initializes it again after the guard, and negated affordability initializes it outside `NOT`.
`ai_hint_evidence/state_binding_source_review.json` records every external call, and `state_binding_integration.patch` distinguishes this later integration from the six-field AI metadata patch.
The calculator's coefficients, payments, reserve behavior, and all `ai_will_do` expressions remain unchanged; the current API documentation describes the final boolean contract.
The MCP event inspection returned a partial result with helper expansion deferred, so it is not claimed as native payment execution proof.
The game was not launched.

The original optional writer attempt failed with `REWRITE_SOURCE_STALE`, then a retry rolled back with `REWRITE_POST_VALIDATION_FAILED`.
The user removed that transaction's mandatory completion gate; the reviewed source edits were applied directly and inspected/rendered through the production MCP.
The installed MCP package and configuration were not changed.

## Scope and limits

All runtime changes are repression-owned GUI, quote, consumer, and localisation changes.
`final_source_hashes.json` lists the sixteen implementation/API files with their final hashes, including the six saving hints and the evidence tooltip correction applied after native layout rendering.
The later metadata, tooltip, and explicit-state binding edits do not change layout geometry or visible price rows.
Core event-log, details, settings, super-event, registry, and civilian-accounting implementations were not edited.
The existing restricted-order inventories and casualty rates were retained; their selected-site administrative PP quote and stale-receipt handling changed as described above.
Optional event 14–39 review was not undertaken in this bounded repair.
The native implementation adapts the reference to existing HOI4 controls and conditional action visibility as explicitly permitted by the user.
No requested action or mechanic was replaced with a placeholder or simplified substitute.
Evidence archive limitation: the final inspection's linked bulk JSON/manifest could not be retrieved afterward; the MCP resource reader returned `Artifact provenance manifest is unavailable`.
The successful inspection result and the complete integrated render, layout, validation, fidelity, scenario, and provenance artifacts remain archived; the missing duplicate inspection payload is not represented as present.

Skills used: `skill-creator`, `chaos-redux-scripted-gui`, `chaos-redux-decisions-missions`, `chaos-redux-subagents`, and the image/reference asset workflow.
The new scripted-GUI skill and routing were committed in `86b6ff4045`; the optional rewrite policy was committed in `bcbe900c81`.
The visual-review checklist also records coherent fixtures, traceable numeric values, truthful counter labels, and retained reserves.
That checklist follow-up was committed in `7859cb8fa`.
The checklist also requires checking the emitted per-scenario resolution and scale rather than inferring coverage from the requested resolution list.

The final repair is saved on `codex/repression-gui-site-costs-20260906` using a temporary Git index because a concurrent operation holds the shared index lock.
This preserves the existing checkout and shared staging state while recording only the reviewed repression files, skill checklist follow-up, and this plan's evidence.
