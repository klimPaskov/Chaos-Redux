# IW-030 MNT portrait independent audit v68

Reviewer: `/root/event6_mnt_portraits_research_v68`.
Date: 2026-08-01.
Producer boundary: the raw ImageGen repaints were produced in the prior v53 tranche and copied unchanged into this package; this audit is a separate review pass.
Role family: canonical country-leader references under `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/`.

## Audit matrix

| Candidate | Unchanged master and exact crop | Raw ImageGen likeness | Processed 156x210 likeness | Male/framing/artifacts | HOI4 leader style | Source/crop linkage | Provenance/rights | Overall |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Jovanović | `PASS`: source is a named 1942 group photograph, crop rectangle is explicit, and the crop JSON proves decoded-pixel equality. | `PASS`: cap/star, thick moustache, brow width, eye spacing, nose, long face, ears, jaw, age, and uniform silhouette remain recognizable without face substitution. | `PASS`: deterministic candidate preserves the same facial geometry and visible cap/uniform at native size and 4x. | `PASS`: one adult male, restrained head-and-shoulders frame, no watermark, text, extra people, or border. | `PASS`: muted olive-brown painted treatment, controlled contrast, dark vignette, and readable small-UI silhouette align with the canonical leader family. | `PASS`: source hash, crop hash, equality JSON, raw output hash, prompt hash, and candidate metadata are linked in this package. | `NEEDS_USER_REVIEW`: Commons gives a public-domain rationale, but the photographer is unknown and the rights basis is not a legal clearance. | `needs_user_review` |
| Đukanović | `PASS`: source explicitly captions the subject, crop rectangle is explicit, and the crop JSON proves decoded-pixel equality. | `PASS`: high hairline, light hair, eyes, long nose, thin lips, broad jaw, ears, age, collar, shoulder braid, and medal silhouette remain recognizable without face substitution. | `PASS`: deterministic candidate preserves the same geometry and source-visible uniform details at native size and 4x. | `PASS`: one adult male, restrained head-and-shoulders frame, no watermark, text, extra people, or border. | `PASS`: muted steel-blue/olive painted treatment, dark vignette, controlled contrast, and readable small-UI silhouette align with the canonical leader family. | `PASS`: source hash, crop hash, equality JSON, raw output hash, prompt hash, and candidate metadata are linked in this package. | `NEEDS_USER_REVIEW`: Commons asserts `PD-old`/PDM for an unknown-photographer book reproduction, but the chain still needs independent legal review. | `needs_user_review` |
| Popović Commons | `BLOCKED`: male portrait is plausible but author, source, date, and era fit are absent from the Commons record. | `NOT RUN`: no source-locked repaint is allowed from an unprovenanced master. | `NOT RUN`. | `PASS` only for visible male framing; this cannot overcome provenance failure. | `NOT RUN`. | `BLOCKED`. | `BLOCKED`: CC BY-SA 3.0/VRTS is not enough to establish date, author, or source. | `blocked` |
| Popović Montenegrina | `BLOCKED`: article identity is plausible, but image author, date, and license are absent. | `NOT RUN`: no source-locked repaint is allowed. | `NOT RUN`. | `PASS` only for visible male framing; this cannot overcome provenance failure. | `NOT RUN`. | `BLOCKED`. | `BLOCKED`: Montenegrina’s project terms prohibit further distribution or unauthorized exploitation. | `blocked` |

## Audit evidence

`review/mnt_v68_audit_native.png` compares unchanged master previews, exact crops, raw ImageGen repaints, deterministic candidates, and three canonical country-leader references at native review scale.
`review/mnt_v68_audit_4x.png` repeats the same comparison at 4x nearest-neighbour enlargement.
`review/mnt_v68_roster_contact_sheet.png` compares the two accepted candidate rows, corroborating Jovanović source, and both blocked Popović leads.
The audit does not approve rights, DDS conversion, `.gfx` wiring, or runtime admission.
