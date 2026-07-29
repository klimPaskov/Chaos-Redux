# Event 016 stage-0 advisor template review

## Scope

This review covers `docs/assets/016_brilliant_scientist/processed_png/portraits/idea_doctor_warren_kruger_stage_0.png`, produced with `.agents/skills/chaos-redux-event-assets/tools/create_advisor_icon.py` from the complete stage-0 Kruger portrait and the canonical `advisor_template.png`.

The runtime composition has exactly two layers: the transformed portrait first and the untouched template on top. No separate frame, paper, shadow, threshold, blur, edge, or component reconstruction remains.

## Placement study

The complete `156x210` source portrait is used without a crop and resized to the native `65x67` advisor canvas before placement. An eight-candidate coarse grid and six-candidate fine grid compared sizes `28x40` through `37x52`, rotations `-3.75` through `-7`, and opening-center offsets from `-1 0` through `0 -1`.

The selected placement gives the strongest balance between full opening coverage, face readability, head and shoulder retention, left rotation, and paper overlap.

## Final transform contract

- Source portrait: complete `156x210` stage-0 Kruger portrait with no crop.
- First operation: resize the complete source to `65x67`.
- Pre-rotation transformed size: `33x46`.
- Template opening center: `25 32.5`.
- Portrait offset: `1` left and `1` up.
- Final portrait center: `24 31.5`.
- Rotation: `-6` degrees.
- Portrait-only sepia strength: `0.18`.
- Top layer: untouched native `65x67` `advisor_template.png`.

The reproducible command is:

```powershell
python -B .agents/skills/chaos-redux-event-assets/tools/create_advisor_icon.py `
	--source gfx/leaders/KRG/leader_doctor_warren_kruger_stage_0.dds `
	--portrait-size 33 46 `
	--rotation -6 `
	--portrait-offset -1 -1 `
	--preview docs/assets/016_brilliant_scientist/processed_png/portraits/idea_doctor_warren_kruger_stage_0.png `
	--output gfx/interface/ideas/016_brilliant_scientist/idea_doctor_warren_kruger_stage_0.dds
```

## Independent verdict

Reviewer: `/root/kruger_final_template_fit_review`

Verdict: `PASS`

- The compositor loads the complete source without cropping and resizes it to `65x67` before the final transform.
- Face, hair, and shoulders remain legible at native size.
- The portrait fills the exposed opening without a transparent gap or spill outside the frame.
- The face is centered in the exposed area and is not swallowed by the paper.
- The `-6` degree left rotation reads naturally.
- The template, alpha edges, fringe, and transparent corners remain clean.
- No correction was recommended; the selected transform values should remain unchanged.

## Runtime evidence

- Script SHA-256: `0080C7BA20C7A19B50C49885B66B775C1967B2CAAAEDCB63230725CB3656E0B0`
- Canonical template SHA-256: `8F594EF62AFBA6FDEC58DE66A80609350DCFE884320B11E6CB6220F1A0E19F58`
- Processed PNG SHA-256: `EEEA4A4C058722ACEBE1FECE6B45274C574BCB32E671F5EAEA6C4FCF03B08A60`
- Runtime DDS SHA-256: `53AEAE1168CFA8B20A5DF4DAB33F13D218939ACDCADC68A3D898CB4520A02802`
- All 897 fully opaque template pixels are byte-identical in the final composite.
- PNG and decoded DDS RGBA pixels are identical.
- The runtime DDS is a `65x67` one-level BGRA surface of `17,548` bytes.
