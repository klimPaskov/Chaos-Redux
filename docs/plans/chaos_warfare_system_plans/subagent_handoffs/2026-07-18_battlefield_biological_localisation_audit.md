# Battlefield Biological Native-Raid Localisation Audit

Date: 2026-07-18
Scope: Stage 7 battlefield biological native-raid localisation only

This is a localisation audit handoff. It does not claim Stage 7 completion or overall Chaos Redux completion.

## Files inspected

- `common/raids/biological_battlefield_raids.txt`
- `common/raids/categories/chaosx_raid_categories.txt`
- `common/scripted_effects/biological_battlefield_effects.txt`
- `common/scripted_triggers/biological_battlefield_triggers.txt`
- `localisation/english/biological_battlefield_raids_l_english.yml`
- `localisation/english/cbrn_hq_l_english.yml`
- `docs/plans/chaos_warfare_system_plans/2026-07-18_stage_7_battlefield_dissemination_validation.md`
- Relevant offline Paradox wiki localisation, decision, trigger, effect, and raid references, plus vanilla raid documentation and examples.

## Files changed

- `localisation/english/biological_battlefield_raids_l_english.yml`
  - Narrow wording-only patch; UTF-8 BOM preserved.
- `docs/plans/chaos_warfare_system_plans/subagent_handoffs/2026-07-18_battlefield_biological_localisation_audit.md`
  - This handoff.

`localisation/english/cbrn_hq_l_english.yml` was inspected but not changed. Its existing concurrent edit was preserved.

## Key coverage

All 26 localisation keys referenced by the raid script, category, and result helpers are present exactly once in the English localisation set, with no missing keys or key collisions:

- Category: `raid_category_biological_battlefield_raids`, `raid_category_header_biological_battlefield_raids`, `tooltip_raid_category_biological_battlefield_raids`.
- Category availability: `biological_battlefield_raid_available_tooltip`.
- Four raid names and descriptions: `raid_type_anthrax_battlefield_dissemination`, `raid_type_anthrax_battlefield_dissemination_desc`, `raid_type_plague_battlefield_dissemination`, `raid_type_plague_battlefield_dissemination_desc`, `raid_type_tularemia_battlefield_dissemination`, `raid_type_tularemia_battlefield_dissemination_desc`, `raid_type_smallpox_battlefield_dissemination`, `raid_type_smallpox_battlefield_dissemination_desc`.
- Target and tooltips: `raid_target_name_biological_battlefield_state`, `bio_battlefield_target_available_tt`, `bio_battlefield_preparation_available_tt`, `bio_battlefield_launch_available_tt`.
- Results: `bio_battlefield_failure_actor_tt`, `bio_battlefield_failure_target_tt`, `bio_battlefield_limited_actor_tt`, `bio_battlefield_limited_target_tt`, `bio_battlefield_success_actor_tt`, `bio_battlefield_success_target_tt`, `bio_battlefield_critical_actor_tt`, `bio_battlefield_critical_target_tt`, `bio_battlefield_context_rejected_actor_tt`, `bio_battlefield_context_rejected_target_tt`.

### Audit lists

- Missing keys: none.
- Duplicate keys: none.
- Scripted-localisation issues: none found; every localisation helper referenced by the inspected category, raid, and biological result scripts resolves.
- Dynamic text opportunities: `$LOCATION$` is already used for the native target name. No additional dynamic localisation was unambiguously necessary within the two permitted gameplay files; runtime values remain script-owned.
- Encoding: both permitted localisation files have UTF-8 BOM; no `:0` entries were found.

## Findings and applied fix

The key set was complete, but several existing strings were materially inaccurate or exposed implementation-facing details. The original category, availability, target, preparation, and launch text did not explain the exact state target, active valid Combined CBRN Overmatch authorisation, full native payload reservation/loss, or fail-closed resolution. Result text exposed hidden incubation, attribution, forensic-evidence, and evidence-substitute concepts, and did not consistently describe shared ordinary biological consequences, friendly blowback, or occupied-friendly exposure.

The following 19 keys were narrowed and corrected in `localisation/english/biological_battlefield_raids_l_english.yml`:

- `tooltip_raid_category_biological_battlefield_raids`
- `biological_battlefield_raid_available_tooltip`
- `raid_type_anthrax_battlefield_dissemination_desc`
- `raid_type_plague_battlefield_dissemination_desc`
- `raid_type_smallpox_battlefield_dissemination_desc`
- `raid_target_name_biological_battlefield_state`
- `bio_battlefield_target_available_tt`
- `bio_battlefield_preparation_available_tt`
- `bio_battlefield_launch_available_tt`
- `bio_battlefield_failure_actor_tt`
- `bio_battlefield_failure_target_tt`
- `bio_battlefield_limited_actor_tt`
- `bio_battlefield_limited_target_tt`
- `bio_battlefield_success_actor_tt`
- `bio_battlefield_success_target_tt`
- `bio_battlefield_critical_actor_tt`
- `bio_battlefield_critical_target_tt`
- `bio_battlefield_context_rejected_actor_tt`
- `bio_battlefield_context_rejected_target_tt`

The revised text describes four native raids, the exact selected state and adjacency/eligibility conditions, matching full-payload reservation and loss, active Combined CBRN Overmatch authorisation, the shared ordinary biological response, bounded adjacent friendly-state blowback, higher exposure in occupied territory belonging to us/faction/subjects, and fail-closed loss without a release or Command Power refund. Doctrine is described as increasing harm and possibly refunding bounded Command Power while reducing only Condemnation. No fallback, proxy, estimator, inferred launch state, weaponized-zombie implication, or hidden incubation/attribution value is presented to the player.

## Validation

- Exact-key scan after the patch returned 26 definition lines for the 26 expected keys; all were in the intended battlefield localisation file and no duplicate/collision was found.
- Source-level BOM/format scan returned UTF-8 BOM and zero `:0` entries for both permitted localisation files.
- Player-facing battlefield localisation scan returned zero matches for incubation, attribution, evidence-substitute, or weaponized-zombie wording.
- No in-game native-raid render or runtime test was run; this handoff records source-level validation only.

## Remaining risks

- The native raid UI's runtime line wrapping and rendered tooltip layout remain unverified.
- The concurrent `cbrn_hq_l_english.yml` edit was intentionally left untouched and should remain under its owning worker's review.
- Raid gameplay scripts were not changed in this localisation-only pass. Any later mechanic change requires a fresh wording audit.

Skills applied: `chaos-redux-decisions-missions` and `chaos-redux-subagents`.

## Parent disposition

The main implementation pass accepted the exact-state, payload, headquarters, shared-lifecycle, friendly-blowback, occupied-friendly, doctrine, and fail-closed wording changes. It adjusted the category requirement to describe national last-resort safeguards without implying that the Kruger-specific authority is a universal named mechanic.

The failure result text was also corrected to disclose the real non-physical consequences that the script applies: recovered material creates forensic evidence, the attempt may be attributed, and Condemnation may rise. It still hides numerical evidence values and attribution thresholds and does not claim that an outbreak was seeded. Hiding secret values does not permit a player-facing outcome tooltip to omit an actual consequence.
