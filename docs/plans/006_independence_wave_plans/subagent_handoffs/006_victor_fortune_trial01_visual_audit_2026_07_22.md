# Victor Fortune trial 01 visual audit

Date: 2026-07-22  
Asset: `SCO_victor_morven_fortune_hoi4_trial_01`  
Proposed consumer: `GFX_portrait_SCO_independence_wave_territorial_commandant`  
Role: grounded real male Scottish territorial commander (Major-General Sir Victor Morven Fortune)

## Verdict

**FAIL CLOSED — `needs_user_review`; not complete and not wireable.**

The source and output share broad cues (square face, heavy jaw, short moustache,
deep-set eyes, straight nose, peaked cap, and British field uniform), but the
200x250 primary source is too low-resolution to establish a forensic same-person
likeness after a generative reconstruction. The full and 156x210 output could
plausibly be a different period officer. The package therefore fails the
required exact-likeness gate. No DDS conversion or runtime wiring is authorized.

There is also a source-mode compliance blocker: Fortune is a grounded real
person, while this candidate is explicitly an ImageGen edit. The event-assets
portrait rules require an unchanged attributed source followed by a
deterministic identity-preserving finish and prohibit ImageGen from
reconstructing, stylizing, beautifying, or filling a real face. The manifest's
`review_candidate_not_wired` status is correct.

## Criterion review

| Criterion | Result | Evidence / risk |
|---|---|---|
| Exact same-person likeness | **FAIL CLOSED** | Primary IWM close portrait (`200x250`) and both context images show matching broad structure, but the generated master alters fine facial proportions and reconstructs details unavailable in the source. At native `156x210`, the result reads as a plausible generic British officer; Fortune cannot be uniquely established. |
| Male-only compliance | **PASS** | Source and both output sizes depict one male-presenting adult; no female, advisor, dossier, or extra-person content. |
| Source-age fidelity | **CONDITIONAL / REVIEW** | 1940 source depicts Fortune at approximately 57. Output is period-correct but smoother and somewhat younger-looking; mild de-aging remains possible. |
| Uniform/cap fidelity; no hallucinated insignia | **CONDITIONAL / REVIEW** | Field-service uniform, tie, shoulder straps, and peaked cap are consistent with the source/context. The output renders a much sharper/larger cap badge and clearer buttons than the indistinct low-resolution source; exact insignia provenance cannot be certified. |
| Head-and-shoulders composition | **PASS** | Full master is a restrained bust from cap through chest/shoulders; native output retains a centered readable commander silhouette. |
| HOI4 commander painted style (full and native) | **CONDITIONAL PASS** | Muted quiet background, controlled contrast, and painterly treatment match the commander family. Native size is readable. Full master has heavier visible brush texture and a stronger vignette than the canonical references, but no text, watermark, UI, modern props, or meme treatment. |
| Rights/source traceability | **SOURCE PASS; PACKAGE BLOCKED** | Manifest gives IWM RML 342 / 51HD context, Commons `PD-scan`/`PD-UKGov` basis, direct source paths, dimensions, and hashes. Hashes match all three Fortune source JPEGs and both PNG outputs. This does not cure the prohibited generative real-person portrait route. |

## Exact files inspected

Repository instructions and skill:

- `AGENTS.md`
- `.agents/skills/chaos-redux-event-assets/SKILL.md`

Source package:

- `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/active_vanilla_conflict_retry/manifest.md`
- `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/active_vanilla_conflict_retry/gfx_handoff.md`
- `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/active_vanilla_conflict_retry/source_hashes.sha256`
- `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/active_vanilla_conflict_retry/source_masters/SCO/SCO_victor_fortune_iwm_1940_portrait.jpg` (primary, `200x250`)
- `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/active_vanilla_conflict_retry/source_masters/SCO/SCO_victor_fortune_iwm_1940.jpg` (IWM context, `800x525`)
- `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/active_vanilla_conflict_retry/source_masters/SCO/SCO_victor_fortune_51hd_mid_1940.jpg` (51HD context, `580x609`)

Refinish package:

- `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_22/scotland_commander/manifest.md`
- `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_22/scotland_commander/imagegen_sources/SCO_victor_morven_fortune_hoi4_trial_01.png` (`1081x1455`, RGB)
- `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_22/scotland_commander/processed_png/SCO_victor_morven_fortune_hoi4_trial_01.png` (`156x210`, RGB/opaque)

Canonical commander references:

- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/README.md`
- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/CATALOG.md` (commander rows)
- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/commanders/contact_sheet.png`
- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/commanders/generic_africa_land_1.png`
- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/commanders/generic_africa_land_2.png`
- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/commanders/generic_africa_land_3.png`
- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/commanders/generic_africa_navy_1.png`
- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/commanders/generic_africa_navy_2.png`

## Evidence checks

- Source hashes match the source manifest: Fortune primary `830f1757…46d049`,
  IWM context `3833223d…b8c8c6d`, and 51HD context `6f2a6862…f5f3392`.
- ImageGen master hash matches the Scotland manifest (`1fdceaed…ef2c8f40`).
- Native review PNG hash matches the Scotland manifest
  (`e0903f6b…833015d0`).
- Canonical commander examples are all full `156x210` opaque portrait textures;
  the candidate uses the correct native canvas and is not a fabricated `50x67`
  commander source.
- No final DDS exists in the named Scotland package, and the handoff does not
  claim a runtime path exists. This is correct for a review candidate.

## Residual risks / clearance requirement

1. Low-resolution primary evidence leaves no reliable way to rule out a
   plausible different officer after generative reconstruction.
2. ImageGen is disallowed for this grounded real-person portrait, regardless of
   apparent visual similarity or source rights.
3. Output cap-badge geometry and other sharpened insignia are not independently
   supported by the source pixels.
4. Output age may be mildly smoothed/de-aged relative to the 1940 source.

Do not convert, overwrite, or wire this trial. Clearance requires an
independent reviewer to establish exact same-person likeness and insignia
fidelity **and** a source-faithful non-generative portrait finish compliant with
the grounded-real-person pipeline. No fallback or substitute portrait was
approved by this audit.
