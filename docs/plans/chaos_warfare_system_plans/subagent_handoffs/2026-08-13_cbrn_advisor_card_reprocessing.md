# CBRN advisor card reprocessing handoff

## Outcome

The twelve live CBRN advisor and theorist cards were rebuilt from the existing approved scientist portraits through the canonical dossier workflow. The processor now measures the actual template opening, requires exact frame-plane size, center, and rotation, uniformly contains the complete source portrait without crop or stretch, fills only the residual top strip with a source-derived matte, produces mandatory placement and alignment evidence, and retains transform and output hashes.

## Changed surfaces

- `.agents/skills/chaos-redux-event-assets/SKILL.md`
- `.agents/skills/chaos-redux-event-assets/tools/README.md`
- `.agents/skills/chaos-redux-event-assets/tools/create_advisor_icon.py`
- `.agents/skills/chaos-redux-event-assets/tools/tests/test_create_advisor_icon.py`
- `docs/assets/chaos_warfare_historical_advisors_v3/`
- `gfx/interface/advisors/cbrn/*.dds`

Existing `.gfx` sprite names, character IDs, and approved `156x210` scientist portraits remain unchanged.

## Geometry and processing evidence

- Measured opening center: `24.76151027919129, 30.645146882359736`
- Measured opening size: `30.477406015014285 x 45.09450833210553`
- Measured and selected rotation: `-4.76` degrees
- Selected offset: `0,0`
- Contained portrait size: `30.477406015014285 x 41.027277327903846`
- Source-derived top matte: `4.06723100420168` pixels
- Crop: false
- Stretch: false
- Rotation alignment error: `0.0` degrees

All twelve metadata records passed the geometry, aspect, output-size, crop, stretch, and alignment audit. The independent visual reviewer passed every card at native and `4x` scale and approved the family overall.

## Runtime mapping

The package manifest maps every source to its stable runtime destination under `gfx/interface/advisors/cbrn/`. Runtime conversion uses `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py --width 65 --height 67` from the independently approved native PNGs.

## Remaining risks

No workflow simplification or unapproved fallback remains. Kitano and Olson retain minor softness from their existing approved full-size source portraits; the independent reviewer judged both acceptable at native advisor-card scale.
