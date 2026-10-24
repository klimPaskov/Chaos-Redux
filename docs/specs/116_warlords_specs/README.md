# Warlords 116: imported planning package

## Current import disposition

This directory is an imported planning package. The user explicitly confirmed on 24 October 2026: “Adopt uploaded IDs and migrate the catalog.” This accepts the uploaded planning identities Event 115 Heroic Crusade and Event 116 Warlords and authorizes catalog migration; the parent has installed that shared migration. It does not accept either gameplay design or authorize its implementation, asset production, or live testing. Treat design commitments, numeric profiles, historical approval claims, and production prompts below as proposal/history pending parent review.

The user-confirmed catalog migration is installed: Event 116 is Warlords, Event 111 is This is SPARTA!!!, and former catalog IDs 127 and 116 are preserved as migration history. Event 115 is Heroic Crusade and Event 110 is IMRO; former catalog IDs 126 and 115 are history. All migrated destination rows remain Unavailable because no runtime event roots are present. The [shared identifier registry](../shared_identifier_registry.md) and parent migration report `docs/plans/repo_cleanup/planning_package_import_2026-10-24.md` record the crosswalk. Catalog identity acceptance does not approve gameplay design or register runtime content.

A general turns a coherent part of a large country into a personal military state. Further generals can follow, later breakaways can become stronger, and each surviving regime must recruit, govern, obtain equipment, and fight through the ordinary world. Generalissimo can unify the rivals through actual campaigns and genuine military subordination. Supreme War State formation precedes the later international dominance required for The Final Warlord.

**Historical package status:** the archive describes a complete planning baseline with proposed balance and engineering gates. The user has confirmed its 116 planning identity and authorized catalog migration; that decision does not accept the gameplay design. No gameplay implementation, live testing, final localisation, or asset production is claimed. Minor Fire-Once, Chaos 1, Liberations High membership, and balance remain design proposals. The catalog migration was installed by the parent under the user-authorized migration.

## Read the design

| Part | Specification |
| --- | --- |
|1 | [Core experience and fixed promises](specs/01_breakaway/116_warlords_spec_part_1_core.md) |
|2 | [Targets, regions, and birth](specs/01_breakaway/116_warlords_spec_part_2_targets_regions_and_birth.md) |
|3 | [Forces and recruitment](specs/01_breakaway/116_warlords_spec_part_3_forces_and_recruitment.md) |
|4 | [Country identity and Command Cohesion](specs/02_country_play/116_warlords_spec_part_4_country_identity_and_cohesion.md) |
|5 | [Parent recovery](specs/02_country_play/116_warlords_spec_part_5_parent_recovery.md) |
|6 | [Warlord statecraft and diplomacy](specs/02_country_play/116_warlords_spec_part_6_warlord_statecraft_and_diplomacy.md) |
|7 | [The two evolutions](specs/03_escalation/116_warlords_spec_part_7_evolutions.md) |
|8 | [Generalissimo and Supreme War State](specs/03_escalation/116_warlords_spec_part_8_generalissimo_and_supreme_war_state.md) |
|9 | [The Final Warlord](specs/03_escalation/116_warlords_spec_part_9_the_final_warlord.md) |
|10 | [Settlement, liberation, and successors](specs/03_escalation/116_warlords_spec_part_10_settlement_liberation_and_successors.md) |
|11 | [Focus routes and national ideas](specs/04_play_and_presentation/116_warlords_spec_part_11_focus_routes_and_ideas.md) |
|12 | [Decisions and missions](specs/04_play_and_presentation/116_warlords_spec_part_12_decisions_and_missions.md) |
|13 | [Integrations, AI, and Chaos](specs/04_play_and_presentation/116_warlords_spec_part_13_integrations_ai_and_chaos.md) |
|14 | [Manual scenarios and presentation](specs/04_play_and_presentation/116_warlords_spec_part_14_manual_scenarios_and_presentation.md) |
|15 | [Assets, localisation, and super-events](specs/04_play_and_presentation/116_warlords_spec_part_15_assets_localisation_and_super_events.md) |
|16 | [Ten difficult achievements](specs/04_play_and_presentation/116_warlords_spec_part_16_achievements.md) |
|17 | [Acceptance and evidence limits](specs/04_play_and_presentation/116_warlords_spec_part_17_acceptance_and_limits.md) |

The gameplay chapters are the primary design. They intentionally use branch-level focus architecture rather than an arbitrary fixed node count. All introduced labels are structural working labels. Player-facing text remains direction-only.

## Implementation review

- [Owner and transaction contracts](implementation/116_warlords_owner_and_transaction_contracts.md) distinguish existing cost helper names from proposed owner interfaces.
- [Starting tuning profile](implementation/116_warlords_tuning_profile.md) defines birth bands, Cohesion behavior, all 29 action prices and timing, and political/terminal thresholds.
- [Adversarial acceptance sequences](implementation/116_warlords_adversarial_acceptance.md) give twelve concrete future tests in addition to the broader Part 17 matrix.
- [Source authority and integration status](implementation/116_warlords_source_authority_and_status.md) preserves historical source claims and records confirmed catalog identity separately from unimplemented runtime behavior.
- [Research and presentation directions](research/116_warlords_research_and_bibliography.md) provide a limited historical grounding and contextual super-event candidates.

The most important implementation gates are exact live-general transfer, exact ordinary-force and resource custody, current/future subject army command, reliable supply and global control evidence, owner integration, and identifier collision review. An unknown capability cannot be replaced by cosmetic flags or an uncosted reconstructed army.

## Production prompts

Use the [goal prompt](prompts/116_warlords_goal_prompt.md) with the full package. It is a short orchestration brief, not a substitute for reading the specifications.

| Workstream | Prompt |
| --- | --- |
| Code and integration | [Coding prompt](prompts/116_warlords_coding_prompt.md) |
| Shared scripted boundaries | [Scripted systems prompt](prompts/116_warlords_scripted_systems_prompt.md) |
| Decisions and missions | [Decision and mission prompt](prompts/116_warlords_decisions_missions_prompt.md) |
| Focus and country routes | [Focus prompt](prompts/116_warlords_focus_prompt.md) |
| Art and visible assets | [Asset prompt](prompts/116_warlords_asset_prompt.md) |
| Achievements | [Achievement prompt](prompts/116_warlords_achievement_prompt.md) |
| Super-event text and audio | [Research and audio prompt](prompts/116_warlords_super_event_research_audio_prompt.md) |

## Historical package and evidence record

The imported ZIP supplied the `116_warlords_specs/` tree. The README records a companion review ZIP with `116_warlords_plans/`, but that companion archive was not among the eight ZIPs imported for this task, so its contents are not present or verified here. The current import-review handoff records the actual imported member-to-destination map.

All 132 supplied text instances, representing 90 distinct complete versions and 2,594,283 representative raw bytes, were fully read by the named team before specification writing. In addition, 42 selected available repository references totaling 1,537,768 raw bytes were fully read at the recorded pinned revision. Recovered clipping and missing external supporting references are documented. This is a team full-read claim, not a claim that the root alone read every byte or that every transitive reference and historical book was read.

No HOI4 runtime or game session was used. The source package was presented as ready for design review. Current parent review is still required before any design is accepted or implementation is authorized. It is not a declaration that the event is playable or ready for a catalog completion status.
