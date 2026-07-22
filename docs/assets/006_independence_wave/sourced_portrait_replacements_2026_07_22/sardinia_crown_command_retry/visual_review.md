# Gioacchino Solinas leader-finish trial review

Review date: 2026-07-22

Reviewer: parent integration agent

Verdict: `rejected_visual_style_pending_refinish`

The explicit `0,0,181,244` crop is identity-preserving and produces a readable
head-and-shoulders military portrait. The deterministic v5.0 leader finish does
not meet the user's accepted visual bar: at native size and on the comparison
sheet it remains a sharpened monochrome archival photograph, not a muted-color,
hand-painted HOI4 portrait comparable to the protected Rupprecht and Matthes
files or the canonical vanilla leader references. No DDS was created and no
runtime sprite or character was changed.

Evidence:

- candidate: `processed_png/ARX_gioacchino_solinas.png`, SHA-256
  `E65D4C9051F8054A2CAE85C2289A67482D3F5F3341208B42E2CC12FB05533D7D`;
- review sheet: `review_sheets/ARX_gioacchino_solinas_review.png`, SHA-256
  `74C8B8950E04103C079A84107CEDD3AF15C4CC6AA441B3A3E7C70CCC21DC9F35`;
- processor record: `metadata/ARX_gioacchino_solinas.json`, whose status remains
  `candidate_requires_visual_approval` as required.

The source and crop may be reused by a stronger deterministic,
identity-preserving painted-finish workflow. This rejected candidate must not be
converted, wired, or counted as package readiness.
