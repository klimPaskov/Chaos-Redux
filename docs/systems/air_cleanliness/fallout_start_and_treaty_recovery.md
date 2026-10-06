# Fallout start and treaty recovery

The manual strike order uses the selected aftermath intensity.
Every valid intensity retains the same all-province bombardment; the intensity changes the resulting damage classification and survivor start.
An impossible forced order produces one local explanation and launches no additional weapons.

## Ash-week orientation

Each current survivor receives five choices covering national authority, the capital, emergency supplies, government, and an office or institution.
Their delayed outcomes apply silently and remain recorded in the survivor history.
One closing report names the office and summarizes the actual outcomes, keeping a complete orientation to six visible reports.
Local settlement text is shown only when all five orders held; contested orders use their actual outcomes.

## Inherited winter recovery

Existing winter outcomes accompany the states the survivor owns and controls.
Regional relief changes Cohesion; school shelters change Shelter capacity and Medicine; rail yards and orderly shutdowns preserve Scrap; dams and plant crews preserve waterworks and electrical skills; refineries and furnaces preserve stocks at their recorded fuel costs.
Failures in other sites still subtract their losses.
Each distinct outcome contributes once nationally, irrespective of how many matching states are held.
The complete change is bounded by the existing survival range, and mixed Cohesion changes are added together before clamping.
The generation guard prevents orientation retries from applying these starting changes again.

The new magnitudes live in `common/script_constants/fallout_winter_recovery_memory_constants.txt`.
The application lives in `common/scripted_effects/fallout_winter_recovery_memory_effects.txt` and is called by the existing first-account memory effect.
The original seed, refugee, Desert City, and dead-city country-history contracts remain in the consolidated effects.

## Relief and reconstruction

A relief vote needs a strict majority of live treaty members and a willing donor who can send equipment.
No supplies means an unfunded session, no success memory, and no penalty against the recipient.
The admitted effect charges the displayed 25 PP and saves that actual amount; cancelled and unfunded sessions return it once.
Stale admission makes no debit or refund.
The caller retry and treaty-wide result-circulation windows last fourteen days.
Completed decisions retain their ordinary pacing.

Reconstruction proposals reserve one sender and one recipient.
The exact sender travels with the answer event; loss or capitulation of either country releases that pair and returns a surviving sender's deposit once.
Refusal blocks the same pair for the existing year, and stale answers explain that the talks have ended.

Treaty response presentation uses six callable families per recipient/stage: one cleaning response, one sampling/seed policy, verification, a size-appropriate convoy/brigade, the urgent relief/evacuation response, and sanctions when relevant.
These presentation gates do not cancel already paid projects or cap all concurrently running projects.

## Presentation and assets

Orientation uses the existing six `GFX_report_event_fallout_*` orientation pictures registered in `interface/fallout_consolidated.gfx`.
The declined strike uses the owned orientation closure picture.
Treaty closing notices use the existing native treaty report picture; they require no new scene art.
The Recognition cost glyph is registered as `GFX_fallout_recognition_texticon` through the graphics handoff.
Legacy treaty costs use existing support-equipment, convoy, and civilian-factory texticons, with the same component affordability predicates as payment entry.

## Validation limits and future work

The bounded source cases execute production inheritance, selector, and refund conditions with explicit native primitives and conservative helper temporary-variable lifetime.
They do not execute HOI4 or replace the required probability, GUI, callback, save/reload, or campaign checks.
The current pass's evidence, design decisions, content gaps, and exact live checks belong in `docs/plans/air_cleanliness_fallout_plans/takeover_status_2026-10-06.md`.

Country-history outcomes can be connected further to successor identities and migration allocation when those authored consumers are implemented.
The country-memory library still needs its queued second chains and wider successor coverage, and the character budget still needs its accepted coverage proof.
A bounded recipient selector may improve targeted decision density if native panel review shows too many cloned target rows.
