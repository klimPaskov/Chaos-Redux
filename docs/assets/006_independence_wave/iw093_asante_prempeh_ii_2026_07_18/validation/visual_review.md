# Prempeh II country-leader portrait — parent rejection

**Review date:** 2026-07-18
**Producer:** Chaos Redux sourced-asset subagent
**Reviewer:** parent/main agent
**Candidate:** `processed_png/portrait_DOX_prempeh_ii.png`
**Candidate SHA-256:** `f113cefba729b8a852252d48c81965cce9a89595d3c1487a085056edc2ea9941`
**Process-review sheet SHA-256:** `6c0e7c91a37182968a51d0b21fd6c9a29c12cb0ff991e90610e6dc2cbf7bcad5`
**Verdict:** **rejected; blocked; do not convert, install, wire, or use.**

## Parent finding

The candidate preserves the photographed subject's identity, but it remains a
sharpened grayscale archival photograph. It does not match the painted, colour
HOI4 country-leader style demonstrated by the same canonical references shown
on the process-review sheet.

The rejection is visual and decisive. Correct dimensions, source attribution,
processor reproducibility, crop quality, or DDS pixel equality cannot compensate
for failing the required painted/colour style.

## Reference comparison

The process-review sheet displays the explicit source crop and rejected
candidate beside canonical `den_thorvald_stauning.png` and
`fin_carl_mannerheim.png`. The canonical leader contact sheet at
`.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/contact_sheet.png`
also shows the broader painted/colour family, including
`africa_generic_1.png` and `eth_haile_selassie.png`.

Compared with those references, the rejected candidate lacks the painted colour
rendering, quiet painted background treatment, and illustrated HOI4 surface
finish required for a final country-leader portrait.

## Runtime disposition

The previously converted runtime DDS was deleted after this rejection. No
sprite was registered, no gameplay consumer was wired, and no replacement was
produced. The archival source and rejected processing evidence remain available
for audit only.

## Blocker

A replacement needs an approved real-person workflow capable of a genuinely
painted HOI4 finish while preserving Prempeh II's exact face, age, clothing,
regalia, and proportions without generating or reconstructing facial features.
The current deterministic result does not meet that standard, and a generic or
other-person fallback is forbidden.
