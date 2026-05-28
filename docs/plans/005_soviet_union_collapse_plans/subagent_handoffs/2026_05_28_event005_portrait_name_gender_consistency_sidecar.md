# Event 005 Portrait And Name Gender Consistency Sidecar

Date: 2026-05-28

Scope: bounded audit of Event 005 country history leader packages and `soviet_collapse_randomize_single_person_leader_name` in `common/scripted_effects/005_soviet_collapse_effects.txt`. No flags, GFX, focus trees, decisions, unrelated vanilla histories, or binary assets were edited.

Result: no gameplay patch was needed. This handoff is the only file changed by this pass.

## Country Package Coverage Checklist

- Custom Event 005 tags audited from `common/country_tags/chaosx_countries.txt`: `CFR`, `MFR`, `OGB`, `KZR`, `SOG`, `KHW`, `ALN`, `KRS`, `FTH`, `BBH`, `BSC`, `RMC`, `DSC`, `NRF`, `TNC`, `ALA`, `UDC`, `SDZ`, `GAC`, `DHC`, `KHC`, `FEV`, `SZA`, `UWD`, `MRC`, `IUL`, `BAC`, `PRA`, `TSC`, `ICD`, `ARD`, `NLC`.
- Custom country history leader blocks checked in `history/countries/<TAG> - *.txt`.
- Random-name helper checked: `soviet_collapse_randomize_single_person_leader_name`.
- Existing release council helper checked for institutional bypass behavior: `soviet_collapse_apply_event_created_republic_council_leader`.
- Female-presenting one-person tags checked: `BAC`, `NLC`, `TSC`, `UDC`, `UWD`.
- Male-presenting one-person tags checked: `ALA`, `ARD`, `BBH`, `BSC`, `DHC`, `DSC`, `FEV`, `FTH`, `GAC`, `ICD`, `IUL`, `KHC`, `KRS`, `MRC`, `NRF`, `PRA`, `RMC`, `SDZ`, `SZA`, `TNC`.
- Institutional custom tags checked: `CFR`, `MFR`, `OGB`, `KZR`, `SOG`, `KHW`, `ALN`.

## File Surface Checklist

- Read: `AGENTS.md`.
- Read skills: `.agents/skills/chaos-redux-subagents/SKILL.md`, `.agents/skills/chaos-redux-event-assets/SKILL.md`, `.agents/skills/chaos-redux-events/SKILL.md`.
- Consulted offline wiki pages before gameplay inspection: Data structures, Triggers, Effect, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, Country creation.
- Consulted vanilla docs: `/home/klim/projects/Hearts of Iron IV/documentation/effects_documentation.md`, `/home/klim/projects/Hearts of Iron IV/documentation/triggers_documentation.md`, and related documentation search results for `create_country_leader`, `set_country_leader_name`, `random_list`, and `is_female`.
- Inspected Event 005 files: `common/country_tags/chaosx_countries.txt`, `common/scripted_effects/005_soviet_collapse_effects.txt`, and the 32 custom Event 005 `history/countries/<TAG> - *.txt` files.
- Inspected supporting asset evidence without editing assets: `docs/assets/005_soviet_union_collapse/manifest.md`, `docs/assets/005_soviet_union_collapse/gfx_handoff.md`, `docs/assets/005_soviet_union_collapse/generated_portrait_audit_2026_05_25/manifest.md`, `docs/assets/005_soviet_union_collapse/generated_event_art_sidecar_2026_05_28_goal_resume/gfx_handoff.md`, and portrait contact sheets.

## Missing Or Stale Country Package Surfaces

- No missing custom Event 005 country history file was found in the bounded tag set.
- No missing gender/name randomizer branch was found for the 25 one-person custom tags.
- No institutional custom tag in history calls `soviet_collapse_randomize_single_person_leader_name`.
- No stale randomizer branch was found that routes institutional custom tags into a personal `random_list`.

## Map And State Setup Issues

- Not audited by this sidecar. No map, state ownership, core, claim, supply, victory point, railway, port, resource, or building setup changes were made.

## Politics, Leader, Portrait, Flag, Advisor, And Party Issues

- No female-presenting one-person portrait in scope can receive male random names through the current helper.
- No male-presenting one-person portrait in scope can receive female random names through the current helper.
- Female-presenting one-person histories are consistent:
  - `BAC`, `NLC`, `TSC`, `UDC`, and `UWD` each set `female = yes`, set `soviet_collapse_female_single_person_leader_portrait`, do not set the male portrait flag, and call `soviet_collapse_randomize_single_person_leader_name = yes`.
- Male-presenting one-person histories are consistent:
  - `ALA`, `ARD`, `BBH`, `BSC`, `DHC`, `DSC`, `FEV`, `FTH`, `GAC`, `ICD`, `IUL`, `KHC`, `KRS`, `MRC`, `NRF`, `PRA`, `RMC`, `SDZ`, `SZA`, and `TNC` each set `soviet_collapse_male_single_person_leader_portrait`, do not set `female = yes`, do not set the female portrait flag, and call `soviet_collapse_randomize_single_person_leader_name = yes`.
- Institutional custom histories are consistent:
  - `CFR`, `MFR`, `OGB`, `KZR`, `SOG`, `KHW`, and `ALN` use fixed institutional names, set no personal portrait gender flag, set no `female = yes` metadata, and do not call the personal-name randomizer.
- The randomizer defensively treats institutional/factory/ancient tags as already randomized if called: `CFR`, `MFR`, `MOL`, `UZB`, `TAJ`, `TMS`, `FER`, `ALN`, `KHW`, `KZR`, `OGB`, and `SOG` clear personal gender flags and set `soviet_collapse_single_person_leader_name_randomized`.
- The existing release council helper keeps institutional names for `MOL`, `UZB`, `TAJ`, `TMS`, `FER`, `EST`, `LAT`, `ARM`, `KAR`, `KOM`, `CRI`, `BSK`, `YAK`, `BYA`, and `TAN`.
- No advisor, party, or flag edits were in scope or made.

## Focus, Decision, Idea, And Asset Issues

- Focuses, decisions, ideas, and `.gfx` files were not edited.
- Asset evidence used for classification:
  - `custom_country_leaders_labeled.png` visually matches the five female-presenting one-person tags and the audited male-presenting one-person tags.
  - `generated_event_art_sidecar_2026_05_28_goal_resume/gfx_handoff.md` explicitly classifies `CFR`, `SOG`, `ALN`, `KHW`, `KZR`, and `OGB` as institutional/council, and `KRS`, `RMC`, `SDZ`, `TSC`, and `UDC` as one-person gendered portraits.
- Remaining uncertainty: some one-person portraits keep institutional placeholder leader names in the initial `create_country_leader` block, then immediately call the startup history randomizer. Vanilla documentation confirms `set_country_leader_name` changes the active leader name without tooltip, so the effective in-game name is the random personal name after history execution. If future design reclassifies any of these portraits as true institutional bodies, remove the randomizer call and gender flag in the same change.

## Starting Military, Technology, Industry, Supply, And Production Issues

- Not audited by this sidecar. No starting army, navy, air force, equipment, manpower, technology, production, convoy, train, fuel, or supply changes were made.

## AI And Playability Issues

- Not audited by this sidecar. No AI strategy, focus AI, decision AI, route behavior, or playability balance changes were made.

## Changed Files

- `docs/plans/005_soviet_union_collapse_plans/subagent_handoffs/2026_05_28_event005_portrait_name_gender_consistency_sidecar.md`

## Changed Tags, State IDs, Leaders, Parties, Focus Tree IDs, Localisation Keys, Or Formable IDs

- None. No gameplay identifiers, tags, state ids, leaders, parties, focus tree ids, localisation keys, formable ids, portrait sprites, or randomizer logic were changed.

## Before And After Behavior

- Before: Event 005 custom one-person leader portraits already used gender-matched metadata and personal-name pools; institutional portraits kept fixed institutional names or defensive bypass handling.
- After: no gameplay behavior changed. The parent has current audit evidence for the Event 005 portrait/name gender invariant.

## Validation Run

- `python3` history/effect audit:
  - `issues []`
  - `female_tags BAC NLC TSC UDC UWD`
  - `male_tags ALA ARD BBH BSC DHC DSC FEV FTH GAC ICD IUL KHC KRS MRC NRF PRA RMC SDZ SZA TNC`
  - `institutional_tags ALN CFR KHW KZR MFR OGB SOG`
- `rg` audit of custom histories and helper:
  - Found `female = yes` only on scoped Event 005 female-presenting one-person histories in the custom tag set: `BAC`, `NLC`, `TSC`, `UDC`, `UWD`.
  - Found male portrait flag plus randomizer on the scoped Event 005 male-presenting one-person histories.
  - Found no randomizer call in the scoped Event 005 institutional custom histories.
- Visual spot-checks:
  - Viewed `docs/assets/005_soviet_union_collapse/contact_sheets/custom_country_leaders_labeled.png`.
  - Viewed `docs/assets/005_soviet_union_collapse/generated_event_art_sidecar_2026_05_28_goal_resume/contact/priority_portraits_plain_contact.png`.

## Skipped Validation

- No in-game validation was run.
- No binary portrait validation, conversion, or generation was run because the task was a code/history/effect audit and explicitly excluded asset edits.
- No focus, decision, flag, AI, map, military, production, localisation, or balance validation was run because those surfaces were outside scope.

## Remaining Setup Or Identity Risks

- This sidecar does not claim full Event 005 completion.
- This sidecar does not validate country setup beyond leader portrait/name gender consistency.
- The current one-person randomizer is gender-safe, but several one-person portrait sprites and initial history names still use institutional wording. That is acceptable under the current asset handoffs because those portraits are deliberately treated as one-person leaders after randomization, but future art or identity passes should keep the classification and gameplay behavior aligned.
- Existing council/committee/office portraits should continue to bypass personal randomizers unless a future pass deliberately converts them into one-person leaders with matching gender metadata and name pools.
