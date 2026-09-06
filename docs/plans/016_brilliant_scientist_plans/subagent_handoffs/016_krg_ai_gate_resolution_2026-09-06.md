# Event 016 KRG AI gate resolution

Date: 2026-09-06.

Scope: bounded source and documentation audit of the KRG AI strategy-plan pre-start gate, daily enable/abort lifecycle, and stale architecture wording.

Status: the architecture paragraph was corrected, no gameplay or AI source file was changed, no focus was added or removed, no plan weight changed, nothing was staged or committed, and no game was launched.

## Decision and acceptance basis

The parent accepted on 2026-09-06 that Event 016 uses broad static eligibility with dynamic KRG enable/abort checks so a valid original host can be transformed into the KRG state under the Final Completion Plan.

The prior architecture sentence at `docs/plans/016_brilliant_scientist_plans/016_kruger_state_100_focus_architecture.md:336` incorrectly described `allowed` as a KRG-sovereignty check and has been corrected to document the accepted transformed-host lifecycle.

The source header at `common/ai_strategy_plans/016_brilliant_scientist_kruger_state_plans.txt:4-9` already states that the pre-start gate uses static identity checks, that Event 016 may transform any valid non-DJX host, and that the continuously evaluated `enable` gate owns runtime KRG identity.

The offline AI-modelling references state that `allowed` is evaluated only at game start, while `enable` and `abort` are evaluated daily and control plan assignment and continuation (`paradox_wiki/AI modding - Hearts of Iron 4 Wiki.md:280-305` and `paradox_wiki/National focus modding - Hearts of Iron 4 Wiki.md:592-608`).

## Source gate review

The source contains 19 KRG plans, 19 `allowed` blocks, 19 `enable` blocks, 19 `abort` blocks, and 19 ordered `ai_national_focuses` blocks in `common/ai_strategy_plans/016_brilliant_scientist_kruger_state_plans.txt`.

Every plan uses the same static `allowed = { NOT = { original_tag = DJX } }` guard at source lines `22,55,87,113,129,174,196,218,234,255,292,308,330,354,372,398,447,499,543`.

Every plan's `enable` block contains `brilliant_scientist_is_kruger_sovereign_country = yes`, which accepts original KRG or a country carrying `brilliant_scientist_host_transformed_into_kruger_state` through `common/scripted_triggers/016_brilliant_scientist_country_triggers.txt:8-13`.

| Plan | Enable identity and route gate | Abort identity and route gate | Source |
| --- | --- | --- | --- |
| `KRG_charter_republic_plan` | KRG sovereign, charter formation, active focus lifecycle | Explicitly aborts when focus is inactive or charter formation is absent | `016_brilliant_scientist_kruger_state_plans.txt:20-28` |
| `KRG_rebellion_directorate_plan` | KRG sovereign, rebellion formation, active focus lifecycle | Explicitly aborts when focus is inactive or rebellion formation is absent | `016_brilliant_scientist_kruger_state_plans.txt:53-61` |
| `KRG_enclave_survival_plan` | KRG sovereign, enclave formation, active focus lifecycle | Explicitly aborts when focus is inactive or enclave formation is absent | `016_brilliant_scientist_kruger_state_plans.txt:85-93` |
| `KRG_takeover_consolidation_plan` | KRG sovereign, takeover formation, founding audit not complete | Aborts when focus is inactive or the founding audit is complete | `016_brilliant_scientist_kruger_state_plans.txt:110-116` |
| `KRG_takeover_post_audit_plan` | KRG sovereign, takeover formation, founding audit complete, active focus lifecycle | Explicitly aborts when focus is inactive or takeover formation is absent | `016_brilliant_scientist_kruger_state_plans.txt:126-140` |
| `KRG_clone_sovereignty_plan` | KRG sovereign, founding audit complete, cloning deployment operational, replicated-host capstone not complete | Aborts when cloning is no longer operational or the replicated-host capstone is complete | `016_brilliant_scientist_kruger_state_plans.txt:172-177` |
| `KRG_machine_ascendancy_plan` | KRG sovereign, founding audit complete, robotics deployment operational, machine capstone not complete | Aborts when robotics is no longer operational or the machine capstone is complete | `016_brilliant_scientist_kruger_state_plans.txt:193-199` |
| `KRG_paleogenetic_plan` | KRG sovereign, founding audit complete, paleogenetics deployment operational, dinosaur-host capstone not complete | Aborts when paleogenetics is no longer operational or the dinosaur-host capstone is complete | `016_brilliant_scientist_kruger_state_plans.txt:215-221` |
| `KRG_xenobiological_plan` | KRG sovereign, founding audit complete, xenobiology deployment operational, engineered-legion capstone not complete | Aborts when xenobiology is no longer operational or the engineered-legion capstone is complete | `016_brilliant_scientist_kruger_state_plans.txt:231-237` |
| `KRG_project_synthesis_plan` | KRG sovereign, founding audit complete, synthesis unlock available, synthesis capstone not complete | Aborts when synthesis is complete, synthesis is no longer unlockable, or focus is inactive | `016_brilliant_scientist_kruger_state_plans.txt:252-267` |
| `KRG_portal_plan` | KRG sovereign, founding audit complete, teleportation deployment operational, transit capstone not complete | Aborts when teleportation is no longer operational or the transit capstone is complete | `016_brilliant_scientist_kruger_state_plans.txt:290-295` |
| `KRG_temporal_plan` | KRG sovereign, founding audit complete, temporal deployment operational, continuity capstone not complete | Aborts when temporal work is no longer operational or the continuity capstone is complete | `016_brilliant_scientist_kruger_state_plans.txt:305-311` |
| `KRG_alien_arms_plan` | KRG sovereign, founding audit complete, alien arms operational, high-energy delivery, rocket or teleport weaponization, alien-arms capstone not complete | Aborts when alien arms is no longer operational or the alien-arms capstone is complete | `016_brilliant_scientist_kruger_state_plans.txt:327-342` |
| `KRG_biological_containment_plan` | KRG sovereign, founding audit complete, biological prototype operational, containment capstone not complete | Aborts when biological work is no longer operational or containment is complete | `016_brilliant_scientist_kruger_state_plans.txt:351-361` |
| `KRG_biological_last_resort_plan` | KRG sovereign, founding audit and containment complete, biological weaponization and delivery valid, high-energy delivery, rocket or teleport weaponization, last-resort capstone not complete | Aborts when biological work is no longer operational or last resort is complete | `016_brilliant_scientist_kruger_state_plans.txt:369-386` |
| `KRG_commonwealth_plan` | KRG sovereign, former-host settlement complete, commonwealth and submission capstones both incomplete | Aborts when either diplomatic capstone is complete or focus is inactive | `016_brilliant_scientist_kruger_state_plans.txt:395-401` |
| `KRG_submission_plan` | KRG sovereign, former-host settlement complete, both diplomatic capstones incomplete, military reach available | Aborts when either diplomatic capstone is complete or focus is inactive | `016_brilliant_scientist_kruger_state_plans.txt:444-450` |
| `KRG_laboratory_world_plan` | KRG sovereign, Evolution IV complete and available, laboratory-world commitment available, laboratory-world capstone not complete | Aborts when either terminal capstone is complete or laboratory-world capability is lost | `016_brilliant_scientist_kruger_state_plans.txt:496-502` |
| `KRG_singularity_plan` | KRG sovereign, Evolution IV complete and available, singularity commitment available, singularity capstone not complete | Aborts when either terminal capstone is complete or singularity capability is lost | `016_brilliant_scientist_kruger_state_plans.txt:540-546` |

The direct focus-activity abort is explicit on the three origin plans, takeover plans, synthesis, and the two diplomacy plans, while project and terminal plans close through operational, capability, or capstone invalidation instead of duplicating the focus-activity predicate.

This is an effective daily lifecycle gate review, not a claim that every `abort` block repeats the sovereign predicate textually, and the project/terminal distinction remains a source-level route risk for fresh engine validation.

The focus activity helper itself requires an active KRG state, the Kruger character, no terminal commitment lock, and no world-end flag through `common/scripted_triggers/016_brilliant_scientist_focus_triggers.txt:26-30`.

## Current DJX exclusion basis

`DJX` is the reserved Event 006 dormant country tag at `common/country_tags/006_independence_wave_countries.txt:51` and its history explicitly says that the package remains unadmitted while research and admission are unresolved (`history/countries/DJX - Unresearched Reservation.txt:2-8`).

The dormant Kruger holder is instead defined under KRG (`history/countries/KRG - Kruger State.txt:2-6`), and the tracked-holder repair handoff records that Event 016 no longer depends on DJX as a fixed holder (`docs/plans/016_brilliant_scientist_plans/016_tracked_kruger_holder_loader_repair_2026-08-02.md:9-23`).

Therefore `NOT = { original_tag = DJX }` is a loader-safe exclusion of the reserved Event 006 carrier, not a pre-start KRG ownership test, and moving the transformed-host identity predicate into `allowed` would prevent the accepted takeover path from being considered after the start check.

## Vanilla documentation and precedent

Vanilla strategy plans use static identity restrictions in `allowed` and dynamic lifecycle conditions in `enable` and `abort`, including Italy at `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/ai_strategy_plans/ITA_alternate_strategy_plan.txt:5-18`, Ethiopia at `.../ETH_alternate_strategy_plan.txt:6-20` and `.../ETH_historical_strategy_plan.txt:5-26`, and Afghanistan at `.../AFG_alternate_strategy_plan.txt:5-19`.

The Ethiopia historical and Afghanistan precedents also use a dynamic `is_subject = yes` abort, demonstrating that a route or political-state invalidation belongs in the daily lifecycle rather than the static identity gate.

## Required audit surfaces

### Route coverage table

All 19 plan routes are listed in the source review table above, and their ordered focus lists remain unchanged and cover the existing 100-focus tree.

### Missing or simplified content

No KRG focus, route family, plan, ordered focus list, or plan weight was added, removed, or simplified in this documentation-only correction.

The project and terminal plans do not repeat the sovereign predicate in `abort`; they rely on route invalidation after the dynamic enable admission, which is recorded as a remaining source-level engine-validation risk rather than silently presented as an explicit identity abort.

### Icon coverage

No icon surface was touched, and the retained 2026-09-05 focus audit records 100 unique KRG focus icons, 200 normal/shine registrations, and 100 DDS textures.

### Localisation and reward mismatch list

No localisation, focus reward, effect, trigger, or tooltip surface was touched, and no mismatch is introduced by this paragraph correction.

### AI behavior gaps

The broad static guard is resolved as accepted design, while numeric plan-weight and route-dominance acceptance remains separate and unresolved.

No claim is made here about weighted route acceptance, factor dominance, or campaign behavior.

## MCP and probability evidence

The mandatory read-only `hoi4.focus_inspect` call was attempted on `common/national_focus/016_brilliant_scientist_kruger_state_focus.txt` with tree `brilliant_scientist_kruger_state_focus_tree` and national mode on 2026-09-06, but it did not return within the bounded wait and was terminated without an artifact.

The mandatory read-only `hoi4.focus_render` call was attempted with the same source and tree on 2026-09-06, but it did not return within the bounded wait and was terminated without an artifact.

The read-only `hoi4.probability_inspect` call was attempted for adapter `ai_strategy_factor` against `common/ai_strategy_plans/016_brilliant_scientist_kruger_state_plans.txt`, but it did not return within the bounded wait and was terminated without an artifact.

The prior 2026-09-05 handoff records the exact service failure for the focus routes as `tool call failed for hoi4_agent_tools/hoi4_focus_inspect; Caused by: timed out awaiting tools/call after 180s` and the corresponding `hoi4_focus_render` timeout, while the custom `chaosx_ai_probability_auditor` route was not exposed.

Retained prior focus inspect, render, and national-focus probability artifacts remain linked in `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_krg_focus_final_plan_audit_2026-09-05.md:75-90`, but they are not presented as fresh engine evidence for this gate.

No probability compare, sweep, or weighted route acceptance claim was made because no gameplay or weight patch was applied and the attempted inspection returned no fresh artifact.

## Validation and remaining risks

Static source review confirmed 19 plan names, 19 broad allowed guards, 19 sovereign enable predicates, 19 abort blocks, and unchanged ordered lists covering all 100 focus IDs.

The architecture paragraph now records the parent acceptance basis, the offline daily-versus-start gate semantics, the DJX exclusion rationale, and the exact project/terminal abort nuance at `docs/plans/016_brilliant_scientist_plans/016_kruger_state_100_focus_architecture.md:336`.

Remaining risks are the unavailable fresh focus MCP evidence, the project/terminal aborts' reliance on route invalidation rather than repeated sovereign identity, and the separate unresolved weighted route evaluation.

No simplification or unapproved fallback was used; the correction is documentation-only and intentionally leaves focus count, plan count, and weights unchanged.
