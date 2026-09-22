# Implement Event 076 achievements and their icons

Read `docs/specs/076_usa_tests_weapons_specs/gameplay/18_achievements.md` together with the actual wave, reward, recovery, war and owner-attribution design. Follow current `AGENTS.md`, the full event-assets skill, the project achievement rules and all locked-template requirements. Inspect the current achievement registry and unique-ID allocation before editing.

Use only `common/achievements/chaos_redux_achievements.txt` for registration. Preserve every existing unrelated entry and unique ID. Do not create an event-specific achievement registry file. Keep actual work, evidence and handoffs in `docs/plans/076_usa_tests_weapons_plans/`.

## Implement the six proof contracts

`chaosx_076_multi_service_research` requires a human USA to receive useful analysis rewards from eight distinct families covering land, air and naval roles, across four foreign minor countries and three continents, within four game years from the first counted success.

`chaosx_076_prototype_development` requires a real restricted foreign nuclear prototype before mature capability, its actual development benefit, and a later real mature research or project completion. A free mature stockpile or a narrative claim does not qualify.

`chaosx_076_repeated_victim_rebuild` requires three completed waves against the same human minor, verified access and productive recovery for the required incidents, and the specified 365-day independent survival condition. Dead population is never rebuilt or erased from the record.

`chaosx_076_refusal_survival` requires a real valid refusal, a USA-led war, independent survival and an actual end of that conflict while controlling the demanded state. Do not invent a free scripted peace to satisfy it.

`chaosx_076_international_reconstruction` requires paid useful contributions to completed access restoration in three foreign victim countries across two continents. Prevent donation-return loops, payments after completion and undamaged objectives from counting.

`chaosx_076_containment_recovery` requires the real owner-defined recovery of the test-linked affected states and the specified 180-day period without renewed local spread or unresolved contamination. A timer or modifier expiry alone is not proof of medical containment.

These descriptions summarize the goals. The complete specification owns the exact conditions, exceptions and receipts. Do not replace them with easier UI counters. Preserve campaign identity, dates, distinct sets, once-only progress, actual reward delivery and source-linked recovery through save and reload.

## Final wording and icon production

Write final achievement names, descriptions and progress tooltips during implementation. The planning package intentionally provides no finished player-facing achievement text. Keep the wording accurate and avoid awarding credit merely for a greater civilian death count.

For each full achievement ID, create one original color subject with genuine alpha and the specific simple icon direction in document 18. Inspect the current vanilla references and immutable achievement templates. Do not create three independently generated variants that only roughly resemble one another.

Use the locked 64 by 64 template inputs `icons/achievements/template/achievement_template.png`, `achievement_template_grey.png` and `overlay.png`. Preserve the exact red not-eligible overlay. Run `.agents/skills/chaos-redux-event-assets/tools/process_achievement_icons.py` with actual validated arguments, then the required conversion and round-trip checks.

Place final files directly under `gfx/achievements/` using `<full_id>.dds`, `<full_id>_grey.dds` and `<full_id>_not_eligible.dds`. No extra event subfolder is used for those final DDS triplets. Preserve original masters and processing evidence in the asset workspace and actual handoff locations.

## Validate

Use actual supplied icon, localisation and completion specialists where available. Prove that canceled tests, partial results, ungranted rewards, duplicate callbacks, repeated variants and invalid war proposals do not count. Verify the real owner recovery and identity rules, including releases, tag changes and multiplayer.

Inspect all 18 final DDS states at native size and in the achievement UI. Verify template alignment, alpha, grayscale, overlay, sprite paths and unique IDs. Test one below-threshold and one valid award case for every achievement, plus save and reload during an observation period.

Return real registry and localisation changes, final icon triplets, source and template provenance, exact test results and unresolved blockers. A supplied achievement definition or icon prompt is not a completed achievement. This planning task produced no registry entries or artwork.
