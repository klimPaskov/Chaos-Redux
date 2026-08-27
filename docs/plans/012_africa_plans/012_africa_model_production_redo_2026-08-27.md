# Event 012 Africa 3D model production redo — 2026-08-27

Status: `incomplete_blocked_with_explicit_vanilla_reuse`.

This handoff records the full current-standard Meshy 7 production pass for the Event 012 Africa model set. The locked route, period/color/anime gates, source-first reference rules, nonhumanoid rig rules, action-source rules, audio provenance rules, and vanilla-green counter rules were applied. No unapproved local motion, humanoid substitute, transform-only animation, anime styling, monochrome final, or unlicensed runtime fallback was promoted.

## Package dispositions

| Package | Current disposition | Evidence and remaining boundary |
| --- | --- | --- |
| Elephant shared base | `custom_model_not_required_existing_elephantry_reuse` | The user explicitly directed reuse of vanilla `elephantry`. The custom `chaosx_elephant` gameplay unit now uses `sprite = elephantry`, templates leave `override_model` unset, and the retired custom entity registrations are removed from active loading. See `subagent_handoffs/012_africa_elephant_vanilla_elephantry_reuse_2026-08-27.md`. |
| Oracle Recon | `model_audio_counter_ready_parent_runtime_promotion_pending` | Existing local Meshy 7 mesh and five action exports/reimports remain staged. Entity/GFX/sound wiring, parent review, and live validation are still open; this pass did not promote them. |
| Disaster Wardens | `custom_model_not_required_existing_infantry_reuse` | Existing vanilla `infantry` consumer remains the accepted path with custom model/entity/animation registrations retired. Parent live consumer validation remains open. |
| Gorilla Heavy Infantry | `blocked_downstream_rig_and_action_route` | Meshy 7 route passed its gate but the live schema exposes no custom nonhumanoid rig input and `meshy_animate` requires a provider `rig_task_id`; no new geometry or actions were promoted. |
| Pan Sappers | `blocked_reference_component_mismatch_and_action_source` | The approved reference lacks the required readable shovel and no compliant digitigrade action source was available; no paid generation was attempted. |
| Stone Cohorts | `blocked_provider_capability_and_insufficient_balance` | The materially different retry was rejected before task creation because the live `meshy-7` schema does not support `model_type: lowpoly`; no current geometry or actions were promoted. |
| Riverborn | `blocked_generation_recovery_4_rejected_identity_and_topology` | Meshy 7 task `01a04331-33b4-7ea1-8bab-d855ed2d8765` consumed 30 credits, but the spear and shield floated beside open hands and eight loose edges remained; it was rejected before rigging. |
| Forest Giants | `blocked_fresh_meshy7_tpose_identity_loss_insufficient_recovery_balance` | Meshy 7 task `01a04333-952c-7726-a8c9-8e9ae388049a` consumed 30 credits and produced technically clean geometry, but omitted both the defining axe and bound-log implement; it was rejected before rigging. |
| Plague Carriers | `blocked_dependency_route_schema_creature_rig_transform_bake_and_verified_actions` | The live adapter lacks the locked static-bake and nonhumanoid rig/action operations; no paid or Blender work was attempted in this pass. |

## Credits and provider state

The provider route was restricted to exact `meshy-7` under the repository locks. Riverborn and Forest each record one 30-credit paid attempt; the final worker reports show 13 credits remaining, while concurrent balance deltas were not fully attributable across workers. Gorilla, Pan, Stone, and Plague did not consume new paid generation credits in their stopping points, and Elephant was explicitly skipped because vanilla reuse was selected.

## Audio and counters

Several package audio candidates were revalidated or converted to signed 16-bit PCM at 44.1 kHz mono, but action synchronization and/or the mandatory per-unit selection consumer remain unproven wherever no accepted action set exists. Counter specialists produced or refreshed evidence for some packages, but parent contact-sheet review and runtime promotion remain open; no counter evidence was used to override a blocked model or action gate.

## Parent-owned follow-up

Do not wire any blocked package's current mesh, animation, or candidate counter/audio files. A future recovery requires a materially different approved reference or provider route, sufficient balance, accepted identity QA, valid provider or explicitly user-approved professional actions, export/reimport proofs, sourced-audio synchronization, bespoke counter review, and parent-owned entity/GFX/sound/gameplay wiring before promotion. The Elephant and Disaster vanilla consumers still require ordinary live consumer validation, and Oracle requires its pending runtime promotion review.

No in-game completion is claimed for the custom packages, and no simplification beyond the explicit vanilla Elephant and Disaster reuse decisions was introduced.
