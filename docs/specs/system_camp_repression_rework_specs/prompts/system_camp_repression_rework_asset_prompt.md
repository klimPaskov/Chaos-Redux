# Asset Prompt: System Camp Repression Rework

Create final assets only after the implementation agent registers stable sprite names and final paths.

For the current GUI presentation, read `../specs/system_camp_repression_rework_spec_part_6_scripted_gui_wireframe_value_display.md` and track the parent implementation and final UI report at `../../../plans/system_camp_repression_rework_plans/repression_ui_redesign_2026-09-05.md`. The current window uses native HOI4 frame, tiled panel, and button surfaces and does not request custom Ledger art.

Use `chaos-redux-event-assets` and the appropriate asset subagent split.

## Asset families

Decision category icons:

- Repression and Camps category icon.
- Gulag and Mass Repression category icon if not reusing an existing category.
- Colonial Labor Burden category icon if a separate category is implemented.

Decision icons:

- expand labor network;
- guard allocation;
- dismantle network;
- inspect site;
- evidence destruction;
- emergency relief;
- prisoner transfer to experiment site;
- colonial labor quota;
- redress or compensation;
- military review;
- contaminated evidence site.

Idea icons:

- active forced-labor network;
- camp network overreach;
- democratic legitimacy damage;
- colonial labor burden;
- gulag authority;
- famine pressure;
- Ishii influence;
- Mengele laboratory autonomy;
- tribunal pressure;
- dismantlement reform.

Report/news images:

- first severe discovery;
- Auschwitz or experiment-linked discovery;
- Pingfang exposure;
- Soviet famine crisis;
- colonial labor exposure;
- tribunal preparation.

Super-event images, only if implemented:

- global severe discovery;
- Mengele Directorate revolt;
- Soviet famine catastrophe;
- Pingfang exposure;
- colonial reckoning.

## Source mode

- Real historical leaders, real flags, and well-attested real symbols must be sourced and documented.
- Fictional UI, idea, decision, and symbolic super-event assets can be generated.
- Report/news images can be sourced when they depict real historical material. Generated period-documentary images are acceptable for alternate-history or composite discovery scenes.
- No generated readable text.
- Every final asset needs source PNG, processed PNG, final DDS, manifest, and GFX handoff.


Use Part 5 for country-specific idea, decision, and report-image asset ids. Use Part 6 for parent-verified GUI panel, navigation-mark, and action identifiers; do not create custom replacement panel, card, background, copied-texture, status-sprite, or animation art for the current window.

## Part 5 and Part 6 asset families

Use the country-specific asset id families named in Part 5 and the GUI sprite families named in Part 6. Create separate asset briefs for:

- U.K./Raj detention, burden, dominion oversight, and discovery icons;
- U.S.A. emergency authority, court review, termination, and redress icons;
- France/Vichy/North Africa camp legacy, inspection, and reckoning icons;
- Italy/Libya desert camp, colonial roads, guard burden, and dismantlement icons;
- Belgium/Congo concession, resource quota, inspection, and reform icons;
- generic activation, labor output, guard allocation, dismantlement, evidence, and discovery icons;
- parent-verified native HOI4 GUI frame, tiled panels, navigation marks, and button states only;
- optional animated warning or reform assets only when the parent explicitly wires real frame sheets and records them in the final UI report.

Do not derive decision icons from focus icons by resizing. Do not request generated Ledger background, card, copied-texture, or status-sprite art for the current GUI.
