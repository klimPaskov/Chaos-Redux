# Dated institutional Records render review

Status: accepted as a source-declared visual fixture at three scales; no live-game receipt claim.
The exact scenario JSON is `../records_ger_institutional_1943_06_{1280,1920,125}.json`; `manifest.json` records request hashes, tool source revisions, source-file identity checks, original artifact hashes, and native click rectangles.

The declared state is Germany on 1943-06-01, with a supported state-88 Auschwitz experimental detention site after the 1943-05-30 gate, a living 10,000-person opening cohort, full experiment permission, and no productive allocation.
The source model yields 20 custody and 20 institutional deaths in its first month, 9,960 survivors, and zero labor, site-violence, and occupation-violence deaths.
Those numbers are a mechanical fixture, not an archival casualty estimate or proof that the engine executed the month.
The one May 1943 institutional-history row describes site establishment; the Records panel does not show a false closure or a pre-gate experiment.

The installed HOI4 MCP 3.5.1 returned `GUI_RENDERED` for each fixture and six integrity-verified original artifacts per case.
I inspected the full and cropped images and click-region overlays at 1280×720, 1920×1080, and 1920×1080 with 125% UI scale.
The displayed cause rows are `0.02 + 0.02 = 0.04` thousand for both month and recorded totals, all other causes are zero, the Germany responsibility label is legible, and no visible text clips or crosses another visible element.
The separate native Administration, Locations, Records, and close hitboxes remain bounded and nonoverlapping at each scale; the Records selected mark remains visible.
The Records layout matches the clean reference's cause/authority/history regions while using production text and the dated source-model numbers.

The validation JSON reports hidden-panel zero-area clipping, intended tab-button/label overlaps, and state coverage warnings because this batch requests Records normal only.
Those diagnostics do not correspond to defects in the inspected visible Records images; the wider view/state matrix remains separately qualified and its unresolved routes remain in `completion.md`.
The rendered fixture does not establish dynamic tooltip evaluation, click execution, persistence, or a live physical death receipt.
