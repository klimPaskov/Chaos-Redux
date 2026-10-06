# Event 005 Release Audit Decisions, 2026-10-05

## Authorization and scope

The user authorized a release-quality audit and design rewrites for Event 005, including the explicit G1–G7 requirements in the task prompt.

The user prohibited workbook and catalog CSV writes, game launch, desktop control, and log searches.

The parent assigned ownership of 005-prefixed event/common/localisation/interface/gfx files and Event 005 documentation, with parent coordination required before shared-file hunks.

## Implemented decisions

The opening Soviet popup `chaosx.nr5.2.d` was rewritten to describe the competing orders and the Soviet leadership's immediate choice in direct in-world prose.

The opening news description `chaosx.news.5.d` was shortened to two sentences, and its button text changed from a map metaphor to `Moscow must answer.`.

The reasons were the supplied `evt005_pop00.png` evidence and G3's plain-prose rule, including the ban on process language and contrast formulas.

The report/news and G3 localization work has a source-context follow-up in progress. The prior pass completed 159 report/news rewrites, 60 broad G3 rewrites, and 19 additional source-backed rewrites. Its exact-key search across 2,536 current source files marked 100 remaining candidates dormant, but a later base-key alias search found that this method missed some focus, decision, and mission consumers. The prior handoff records the exact values; the updated worker handoff will revise active/dormant dispositions and complete the context review. The zero-color result predates the four new entry-report events and will be rerun after the prose pass.



Three focus descriptions were corrected against their reward effects, and `.95` was renamed and rewritten as an internal-republic breakaway report because the initial Soviet republics may already have left before that notice fires.

The seven apparent missing focus-key pairs were not added because all seven focus definitions explicitly target existing `<focus_id>_focus` and `<focus_id>_focus_desc` keys.

The reason for rejecting duplicate focus keys is the current focus-source cross-check by the focus and localisation auditors.

The ordinary Settings path invokes the Event 005-owned `soviet_collapse_prepare_event_fire` helper before dispatch/history recording. It suppresses every root no-op state before dispatch: missing, capitulated, or landless SOV; an active Union crisis; an individual-crisis load at or above its shared cap; and a suppressed fire-once entry owned by the triggerable Soviet scenario. For a manual human request, the helper sets `chaosx_manual_event_failure_shown` before sending one cause-specific report to the saved original requester. The helper is defined at `common/scripted_effects/005_soviet_collapse_effects.txt:60` and called by the parent-owned shared file at `common/scripted_effects/chaosx_settings_effects.txt:4021`.

The root `chaosx.nr5.1` reports directly to its current country scope when the Soviet government is invalid or another gate prevents a new crisis. A valid `soviet_collapse_joint_opening_presentation_pending` flag remains the first route in both entry paths, so an intended joint opening can proceed despite an active crisis, the load cap, or the triggerable-scenario suppression flag. The cause reports are `.138` for no Soviet government, `.139` for an active crisis, `.144` for crisis capacity, and `.145` for triggerable-scenario suppression. Settings failure cases set `event_single_fire_allowed` to zero before shared dispatch/history recording.

The localized `.138`, `.139`, `.144`, and `.145` reports identify each blocked world state and give a neutral acknowledgement option.

## 2026-10-06 Entry-rejection completeness

The parent source review found that the original root could no-op when SOV existed but an active crisis, the shared individual-crisis cap, or triggerable-scenario suppression prevented `.2`. The entry now gives each state a distinct report and the Settings preflight rejects it before dispatch/history recording. The valid joint-opening pending branch remains first and bypasses those three blockers because it is a presentation continuation, not a new crisis start. This closes the observed silent no-op without bypassing the cap or creating duplicate crisis state.

## Shared Event Details and catalog disposition

The parent accepted the exact replacement recorded in `catalog_changes_pending.md` and has applied the shared Event Details body at `localisation/english/chaosx_gui_l_english.yml:693`. Workbook cell `Events!C6` remains pending under the user's no-workbook-write instruction. The parent tried the `usa_1936` GUI fixture on 1936.1.1; inspect transformed it to `usa_1936-generated-1` with 32 unresolved, 3 missing, and 21 click-region overlap diagnostics. A normal/long-text 1920 x 1080/uiScale 1 render returned `GUI_RENDERED` with 27 artifact links. The artifact reader successfully opened the Fury empty-details fixture, but it contains no Event 005 body; the standard USA scenario likewise has no seeded Soviet Event Details content. The populated-content before-render for `events_log_event_details_window` used `fury_release_details_1936`, date 1936.1.1, 1920 x 1080/uiScale 1, normal and long-text states, and `generatedScenarios=false`; it timed out after 600 seconds without a valid populated Event 005 PNG or validation. No populated before artifact exists for comparison, no layout definitions changed, and visual acceptance remains unresolved.

## Audit dispositions

The six captures at `C:/Users/klimp/Videos/chaos_redux_trailer/screenshots/evt005_pop00.png` through `evt005_pop05.png` show one Event 005 popup for the USA human chain from 10 January through 11 March 1936; the other four visible popups are unrelated vanilla events. They show earlier opening wording and support popup counts, not final prose rendering. In the task's `evt005_popKK.png` notation, `KK` is a placeholder for the numbered captures, not a literal filename.

Source tracing shows that a human Soviet player receives three opening popups: `.2`, the first released republic's single `.47` report one day later, and the `.5` world news two days later.

A non-Soviet human receives only the `.5` world news from the valid-SOV opening, while an invalid-SOV Settings force from the USA receives only `.138` and no `.2` or `.5` news.

The first eligible internal republic among `KAR, KOM, CRI, TAT, BSK, FER, YAK, BYA, TAN` emits one `.95` world summary per crisis; subsequent internal releases emit none.

The first regional-faction invite in a crisis emits `.48` world news, and later invite actions use a local `.38` notice without repeating `.48`.

The source change uses one global once-per-crisis flag for each aggregate broadcast, reset in `soviet_collapse_initialize_crisis_values`; it avoids one `.95` news card for every internal republic release and avoids paired `.48` world and `.38` local cards for the same invite action.

The final decision-cost handoff covers 12 cost surfaces and 13 decisions; emergency command power is quoted and charged at 60 rather than 80, affordability checks and debits are paired, changed costs display at most three values, and 21 unique hover keys display full icon-first payments followed by requirement/effect text, with no more than three icons. Amount evidence remains source-level because no current scenario decision inspect returned.

The reason is to keep the visible cost and the actual payment consistent, stay within the decision-skill command-power limit, and reduce payment rows that overwhelm the action's central choice.

The final G1 color audit returned `total keys with colour: 0` after the completed localization pass.

The invalid-SOV trigger snippet passed `hoi4.script_validate` for syntax, command kind, and declared scope, with parameters unchecked.

The `country_event` effect check remained partial because its native argument block was unchecked; the installed `country_event` section was read directly and its ID syntax matches the new call.

Event inspect, render, and compare returned no artifacts after bounded requests stalled; probability inspection timed out after 600 seconds; decision, focus, map, and technology routes also remain incomplete.

No AI weight, MTTH value, event probability, or weighted candidate patch was made without baseline and same-scenario comparison evidence.

The 005 asset manifest and current provenance/contact-sheet archive are missing, so runtime file presence is not treated as asset-source acceptance.

The focus fallback's eligible country set and the incomplete rendered-layout claims remain unresolved.

The exact errors, paths, artifact coverage, and task blockers are recorded in the current Event 005 implementation audit and the specialist audit handoffs.


## Final parent prose review

The final strict active-consumer pass supersedes the earlier grammatical-retention and 100-dormant classifications.
Its source-keyed before/after inventory and bounded no-consumer exceptions are in the localization handoff.
The parent also made `.139` a continuing-crisis headline and `.145` a report about another Soviet emergency, removing scenario-control terminology from their visible text.
Final colour audit remains zero; no populated GUI or native execution acceptance is claimed.

## Graphics review: Kazakhstan residuals, 2026-10-06

Acceptance basis: the user's Event 005 graphics-fix task authorizes clean cut-outs, removal of stray fragments, preservation of stable sprite names, and complete per-tree review of the October graphics plan.
The earlier shared edge repair is retained wherever current decoded art already satisfies the named defect; repeating erosion would damage thin details without restoring missing artwork.
For the Kazakhstan cavalry-school ribbons, reviewed colour-only edge bleeding preserves alpha while removing the coloured fringe and detached dash.
For the southern-republic flags, detached alpha above and below the painted frame is removed.
For the engineers and Turkish-language channels, faint outer shadow pixels below alpha 32 are removed while the subject and its antialiasing remain intact.
Both legacy aliases and the focus-consumed aliases receive identical repaired DDS bytes.
No event mechanics, focus rewards, AI weights, country identities, or catalog wording are changed by this graphics tranche.
Implementation evidence and the exact twenty-row graphics disposition are in `docs/plans/gfx_fix_2026-10/005_kaz_report.md`.
Focus-layout diagnostics remain separate open findings; this tranche does not claim full focus-tree or Event 005 completion.

## Graphics review: portrait identity and framing, 2026-10-06

Acceptance basis: the user's Event 005 portrait repairs and G6 art/design authority, together with the required grounded-source and fictional-portrait gates.
The synthetic Military Factory of Russia is interpreted from the part 6 source spec's arsenal-state/industrial-complex portrait direction, its high-chaos tag registration and its Arsenal Board identity.
Its collective board is represented by one invented chairman with a brass caliper and production-board setting, giving it a distinct painted composition and avoiding the duplicated Construction Board group.
The parent independently reviewed the source and native 156x210 PNG, then authorized only the matching MFR DDS installation after exact header/pixel proof.
Grounded Alash, Tuvan, Ukrainian, Azerbaijani and Kyrgyz identities receive attributed archival source packages, not invented faces.
Their staged source crops retain framing, annotation or style defects and are withheld from runtime until suitable user-supplied painted finals pass independent review.
The actual sources, original/crop hashes, conditional roster checks, distinct Yefremov identities, per-row verdicts and unfinished work are recorded in `docs/plans/gfx_fix_2026-10/005_portraits_report.md`.

## Graphics review: Caucasus subjects and framing, 2026-10-06

Acceptance basis: the user's eight Caucasus graphics findings and G6 authority to repair repeated or weak visual subjects.
Artillery schools use a period mountain gun, the border cabinet uses officers' caps and a map table, the three capitals' talks use architectural seals and a blank treaty, and the enduring compact uses a guarded ridge road and compact seal.
The defense-compact shield is retained for its original role, while those follow-up focuses receive independent original artwork.
Existing oil, voting and foreign-guarantee compositions are fitted and centered proportionally, with matching legacy/focus copies.
The parent independently reviewed and installed ten DDSs, with source/pixel evidence in `docs/plans/gfx_fix_2026-10/005_caucasus_report.md`.
The closed MCP transport blocks final render acceptance; implementation evidence is not promoted to an engine-completion claim.

## Graphics review: Black Banner Host subjects, 2026-10-06

Acceptance basis: the user's BBH placeholder-tree finding, per-focus subject requirement and G6 authority.
All 47 focus slots receive distinct 94x86 textures based on their actual names, descriptions and rewards.
The birth identity uses a wider painted brass frame, the existing bespoke endgame retains its design, and the other slots show their specific military, commune, logistics or diplomatic work.
Parent review rejected circled-A-like commune tokens and revised them to blank seals, and replaced a medieval free-city candidate with a period municipal gate and mounted column.
The anti-protectorate wax seal is blank; the remaining apparent native-size mark was verified at source resolution as envelope-fold shading.
The parent reviewed the complete native sheets, installed all 47 files and independently checked the runtime DDS pixels against their approved PNGs.
The closed MCP transport leaves final engine rendering unresolved; source and independent audit evidence is recorded in `docs/plans/gfx_fix_2026-10/005_bbh_report.md`.

## Graphics review: Arctic Workers' Republic subjects, 2026-10-06

Acceptance basis: the user's AOX placeholder-tree finding, per-focus subject requirement and G6 authority.
All 47 focus slots receive original native-alpha subjects tied to current names, descriptions and rewards, with the anchor-star identity reserved for Birth.
The parent rejected neon arcs on Extreme Path in favor of a physical signal mast, red lamp and harbor lights, and replaced a UI-selector endgame candidate with a fortified harbor gate, sail and broken-chain seal.
First Guard preserves its tall source proportions rather than stretching to fill a fixed box.
The five outdated plan suffixes are mapped to the current registered consumers without renaming sprites or changing gameplay source.
The parent reviewed all 47 native DDS tiles, installed the textures and independently verified their exact approved PNG pixels.
The final named-tree MCP raster returned Transport closed; `docs/plans/gfx_fix_2026-10/005_aox_report.md` records the accepted art and remaining engine acceptance gap.

## Graphics review: Baltic subjects and consumer framing, 2026-10-06

Acceptance basis: the user's Baltic graphics findings, exact consumer sizes and G6 authority.
Home Guard uses a coastal watch post, pine shore and crossed rifles; restoration uses a blank treaty and the three correct Baltic flags; War Room uses officers and a map table.
Defense Compact uses three linked shields and rifles, the rotating capital talks use three architectural seals, German Border Pressure uses a period eagle and regional map, and Estonian Forest-Coast Guard uses a coastal battery and forest.
The parent rejected incorrect flag and clipped-frame candidates, reviewed their replacements at source resolution and reviewed all 42 current focus subjects at native size.
Twenty-five mixed-size 100x88 focus canvases are normalized proportionally to 94x86 while retaining their artwork, with RGB-only cleanup for 111 confirmed chroma edge pixels.
The parent installed and pixel-verified 45 textures, including the unconsumed legacy Warroom file.
The two legacy Warroom aliases remain pointed to Home Guard because the user's explicit size/frame-only rule does not authorize their path correction; the narrow exception is awaiting a reply.
The active focus Warroom already consumes its proper installed texture, and no registry file was edited.
The final MCP raster returned Transport closed; `docs/plans/gfx_fix_2026-10/005_baltic_report.md` records the installed evidence and incomplete alias/engine acceptance.

## Graphics review: Riga audit follow-up, 2026-10-06

Acceptance basis: the user's G5 rule includes every visible size defect, including the auditor's additional Riga finding outside the original 303-row list.
The small dispatch board is replaced by an original rail junction, manual point lever, physical semaphore and blank dispatch panel in the Baltic brass-and-laurel family.
The parent reviewed the complete native-alpha source, the 94x86 PNG, decoded DDS contrasts and updated full 42-focus sheet.
The visible subject occupies 88x79 rather than 64x60, with intact paint and at least three pixels of transparent margin.
The semaphore's red-white arm is railway equipment, not a national flag.
The parent applied and committed a single ASCII punctuation correction from `Riga?s` to `Riga's`, retaining every other shared localisation byte and staged change.
The remaining legacy Warroom mapping and closed final MCP route remain explicit blockers.
Four retained textures are normalized to the approved 2D base-level DDS header after the independent decoder rejected their mip/depth fields.
Their complete pixel payloads and decoded RGBA arrays remain byte-identical.
