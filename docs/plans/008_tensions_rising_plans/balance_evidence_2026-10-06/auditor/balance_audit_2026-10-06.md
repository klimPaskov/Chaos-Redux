Workspace root: C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux

# Event 008 read-only balance and probability audit

**Disposition:** Incomplete; source snapshots and a bounded scenario request are preserved, but the HOI4 probability service returned no inspect or compare artifacts, so numeric probability, targeting, timing, and post-patch conclusions remain unresolved.

This report covers only weighted and probability-bearing Event 008 behavior and its directly related display values; no gameplay, AI, event, localization, or runtime files were edited.

## Readings and scope

Read AGENTS.md and the chaos-redux-subagents, chaos-redux-events, and chaos-redux-mtth skills before the audit.

The exact source files reviewed are events/008_tensions_rising.txt, common/scripted_effects/008_tensions_rising_effects.txt, common/scripted_triggers/008_tensions_rising_triggers.txt, common/script_constants/008_tensions_rising_constants.txt, common/scripted_localisation/008_tensions_rising_scripted_localisation.txt, and localisation/english/008_world_tension_rises_l_english.yml.

The entry event chaosx.nr8.1 is is_triggered_only and has no event MTTH or ai_chance in the six-file source set; no focus, decision, mission, doctrine, research, or direct AI-strategy score is part of this surface.

The weighted surface is direct recipient selection within apply_tensions_rising_distributed_world_tension and its automatic-event eligibility gate; the helper?s recipient count is a random selection size, not a score race or a normalized click probability. The same effects file also contains separate timer, relation-pair, follow-up random_list, AI-posture, and border-war random surfaces, which are outside this packet-target and automatic-gate audit.

The audit used the baseline source commit e99130b84519be8026068502e594507b3979f73d and the owner?s submission after-hash manifest at .tmp/event008_balance_after_hashes.json.

## Immutable source evidence

The baseline manifest is auditor/baseline_manifest.md; the exact source bytes are mirrored below auditor/baseline/sources/.

| Baseline source path | SHA-256 |
| --- | --- |
| events/008_tensions_rising.txt | 2af86814b0d1ca15bfb93dcf42d386faccb533c3b077de0e58150b87e5911664 |
| common/scripted_effects/008_tensions_rising_effects.txt | d7507889ad7c110f969f3e56ead3c9cf98b138271bf6e47cd6f90a78d84cba2b |
| common/scripted_triggers/008_tensions_rising_triggers.txt | 9a79f56008bb7f6c2b6a3a6f89af9acc9d42fade3938724255d035c67dec687e |
| common/script_constants/008_tensions_rising_constants.txt | f8ae3ae6e8a688c618082e1d77c18bd2523d960bca14288e54d87d7d30dfd419 |
| common/scripted_localisation/008_tensions_rising_scripted_localisation.txt | 0e5f498dc0c807e6f69b033f6477b6d38895f59621533fa07ca58870de9e334d |
| localisation/english/008_world_tension_rises_l_english.yml | 08700adaf263a060e22ec85123b096dbe048323c8d16ea4d4f7c1d7eb3930bc6 |

The baseline values in common/script_constants/008_tensions_rising_constants.txt:38-43 are packet requests 100, 100, 200, 500, and 1000 for baseline and Stages I-IV, with a minimum country slice of 0.1.

The baseline recipient limits in common/scripted_effects/008_tensions_rising_effects.txt:9-13 and 186-265 are 1000, 1000, 2000, 5000, and 10000 for baseline and Stages I-IV.

The baseline distribution counts eligible source countries using is_tensions_rising_world_tension_source_country, whose source predicate is exists = yes and not is_special_chaos_country in common/scripted_triggers/008_tensions_rising_triggers.txt:73-76.

At or below the source cap, the baseline helper divides the requested packet by the eligible-country count and applies a slice to every eligible source; above the cap it invokes random_select_amount at the configured cap and applies the minimum slice to the selected countries.

The baseline event report accumulates the requested packet before applying add_named_threat, while the baseline English text presents that value as the amount by which world tension increases; this does not prove the actual global threat delta when native threat is near its cap.

The baseline full-threat predicate is threat greater than 0.9999, and automatic availability also blocks world_end; the baseline source has no Event008-specific recent-shock or 30-day cooldown gate in common/scripted_triggers/008_tensions_rising_triggers.txt:9-10, 22, and 49-56.

## Owner submission snapshot

The exact owner submission bytes are frozen under auditor/after_submission_2026-10-06/sources/ and indexed by auditor/after_submission_2026-10-06/after_manifest.md. A final reread after the compare attempt confirmed all six live files still match the frozen after hashes; no later source differences were present.

| After source path | SHA-256 |
| --- | --- |
| events/008_tensions_rising.txt | 5a484db959e640a82f99c6e11005c271ddf33693e3ba4f672c1c8ef376532868 |
| common/scripted_effects/008_tensions_rising_effects.txt | 1481ff8bada2831f55bc3b13961d0e357a0f0d5249f7e71aabab1f52e6b0ab29 |
| common/scripted_triggers/008_tensions_rising_triggers.txt | e1b4bd4b6fe0a63fab983e7e67bd7512d423f801e9747ee28194a1104fbe7278 |
| common/script_constants/008_tensions_rising_constants.txt | 8abaa05539f54377fd31bc5ac2acec60f4a98bae9a65d998d849ef9619c087bc |
| common/scripted_localisation/008_tensions_rising_scripted_localisation.txt | b93a38b97c17ccc8f9588ae9282c8e9926b476d83ff8adb13c39b7ec2cdf8dfe |
| localisation/english/008_world_tension_rises_l_english.yml | aa7b4e9ba811d44b7da5bb52c214ffe4c349a70011e2056cf2ae00b6ef37c20e |

The owner?s submitted packet constants are 2, 3, 5, 8, and 12 with the same 0.1 minimum country slice; common/script_constants/008_tensions_rising_constants.txt:38-43 records these inputs. The stage Chaos request constants remain 10, 15, 25, and 50; the actual global change is captured by a before/after meter read.

The after helper computes a recipient cap from packet divided by the minimum slice, clamps it to at least one, chooses the lesser of eligible-source count and that cap, divides the packet by the chosen count, and injects the resulting integer into random_select_amount through meta_effect; common/scripted_effects/008_tensions_rising_effects.txt:191-236 contains the source path.

The after helper measures global.threat before and after the recipient effect, multiplies the native 0..1 difference by the configured 100-point scale, and clamps the displayed world-tension delta at zero; common/scripted_effects/008_tensions_rising_effects.txt:191-236 and common/script_constants/008_tensions_rising_constants.txt:266-267 define this source calculation.

The main effect captures global.chaos_meter_value before and after all Event008 effects and adds the signed difference to the report total; common/scripted_effects/008_tensions_rising_effects.txt:112-179 defines that trace.

The owner?s English localization displays one decimal place for the reported actual delta and includes a negative-chaos label at localisation/english/008_world_tension_rises_l_english.yml:8-21 and 88; the scripted selector is common/scripted_localisation/008_tensions_rising_scripted_localisation.txt:82-96.

The automatic availability trigger now blocks when tensions_rising_recent_shock is set and continues to block world_end; common/scripted_triggers/008_tensions_rising_triggers.txt:49-56 contains the source gate, and common/script_constants/008_tensions_rising_constants.txt:267 sets its duration to 30 days.

The owner?s accepted behavior is that every actual shock, including a manual force, starts or refreshes the global 30-day recent-shock flag, while manual forces bypass the automatic availability gate and remain immediate and coalesced; this prevents an automatic notice immediately following manual alarming news.

The report-effectful flag preserves the first effectful report stage through later coalesced shocks and is cleared at the next report-batch initialization and on acknowledgement; common/scripted_effects/008_tensions_rising_effects.txt:94-100 and 119-130 and events/008_tensions_rising.txt:62-70 show this lifecycle.

These are source-trace facts only; actual global threat and chaos deltas, native effect semantics, event-pool cadence, cooldown behavior under campaign state, and popup refresh behavior remain unverified without returned analyzer or runtime evidence.

## Scenario declaration and completeness

The one compare request used scenario-set ID E008_BALANCE_SOURCE_MODEL_2026-10-06, with 60 IDs listed below and serialized in auditor/scenario_matrix_2026-10-06.json.

The scenario fixture SHA-256 is c8d4a7866bd706e25fc5abdb5ab8a4c6dfcaaed21b9e661610d6e5613acb9f02; this is a local request-fixture hash, not an MCP scenario hash.

Each record uses actor GER and date 1936.1.1, with state fields for tensions_rising_stage 0-4, synthetic eligible_source_count 10/50/180, global.threat 0.99/1.0, and tensions_rising_recent_shock on/off.

The eligible-source counts are declared source-model inputs only and are not claims about the number or identity of countries in a campaign; the 0.99 WT case reflects the parent-supplied evt008_pop00.png scenario premise, and the parent also identified vanilla GER Rhineland as a +5-point contribution.

The screenshot bytes were not present in the auditor workspace, and neither the screenshot premise nor the Rhineland contribution was independently verified by MCP or live-game inspection.

The scenario state record shape is known from a prior compare workflow, but the nested state keys above were not confirmed by the pending probability inspect call; they are therefore declared model inputs, not engine-validated aliases.

The candidate identities are absent; the direct_random candidate pool is count-only and incomplete for every scenario because the real country roster and source-trigger membership are unknown.

External factors are incomplete for every scenario, including actual country existence and special-country exclusions, chaos tier and evolution enablement, world_end, current event-system settings and active event weights, start-of-event chaos meter value, and shared chaos-meter effects.

The full global Event008 selection pool and cadence are outside this direct_random comparison; no complete pool manifest, event timer transition, recovery, or terminal-state sequence was provided.

The same scenario IDs are intended for before and after; a returned comparison would still be partial because the compare input binds only the effect source path and cannot prove before-side constant, trigger, event, scripted-localization, or English dependencies.

### Declared scenario IDs

- e008_balance_baseline_eligible_source_count10_belowfull_cooldown_off
- e008_balance_baseline_eligible_source_count10_belowfull_cooldown_on
- e008_balance_baseline_eligible_source_count10_full_cooldown_off
- e008_balance_baseline_eligible_source_count10_full_cooldown_on
- e008_balance_baseline_eligible_source_count50_belowfull_cooldown_off
- e008_balance_baseline_eligible_source_count50_belowfull_cooldown_on
- e008_balance_baseline_eligible_source_count50_full_cooldown_off
- e008_balance_baseline_eligible_source_count50_full_cooldown_on
- e008_balance_baseline_eligible_source_count180_belowfull_cooldown_off
- e008_balance_baseline_eligible_source_count180_belowfull_cooldown_on
- e008_balance_baseline_eligible_source_count180_full_cooldown_off
- e008_balance_baseline_eligible_source_count180_full_cooldown_on
- e008_balance_stage1_eligible_source_count10_belowfull_cooldown_off
- e008_balance_stage1_eligible_source_count10_belowfull_cooldown_on
- e008_balance_stage1_eligible_source_count10_full_cooldown_off
- e008_balance_stage1_eligible_source_count10_full_cooldown_on
- e008_balance_stage1_eligible_source_count50_belowfull_cooldown_off
- e008_balance_stage1_eligible_source_count50_belowfull_cooldown_on
- e008_balance_stage1_eligible_source_count50_full_cooldown_off
- e008_balance_stage1_eligible_source_count50_full_cooldown_on
- e008_balance_stage1_eligible_source_count180_belowfull_cooldown_off
- e008_balance_stage1_eligible_source_count180_belowfull_cooldown_on
- e008_balance_stage1_eligible_source_count180_full_cooldown_off
- e008_balance_stage1_eligible_source_count180_full_cooldown_on
- e008_balance_stage2_eligible_source_count10_belowfull_cooldown_off
- e008_balance_stage2_eligible_source_count10_belowfull_cooldown_on
- e008_balance_stage2_eligible_source_count10_full_cooldown_off
- e008_balance_stage2_eligible_source_count10_full_cooldown_on
- e008_balance_stage2_eligible_source_count50_belowfull_cooldown_off
- e008_balance_stage2_eligible_source_count50_belowfull_cooldown_on
- e008_balance_stage2_eligible_source_count50_full_cooldown_off
- e008_balance_stage2_eligible_source_count50_full_cooldown_on
- e008_balance_stage2_eligible_source_count180_belowfull_cooldown_off
- e008_balance_stage2_eligible_source_count180_belowfull_cooldown_on
- e008_balance_stage2_eligible_source_count180_full_cooldown_off
- e008_balance_stage2_eligible_source_count180_full_cooldown_on
- e008_balance_stage3_eligible_source_count10_belowfull_cooldown_off
- e008_balance_stage3_eligible_source_count10_belowfull_cooldown_on
- e008_balance_stage3_eligible_source_count10_full_cooldown_off
- e008_balance_stage3_eligible_source_count10_full_cooldown_on
- e008_balance_stage3_eligible_source_count50_belowfull_cooldown_off
- e008_balance_stage3_eligible_source_count50_belowfull_cooldown_on
- e008_balance_stage3_eligible_source_count50_full_cooldown_off
- e008_balance_stage3_eligible_source_count50_full_cooldown_on
- e008_balance_stage3_eligible_source_count180_belowfull_cooldown_off
- e008_balance_stage3_eligible_source_count180_belowfull_cooldown_on
- e008_balance_stage3_eligible_source_count180_full_cooldown_off
- e008_balance_stage3_eligible_source_count180_full_cooldown_on
- e008_balance_stage4_eligible_source_count10_belowfull_cooldown_off
- e008_balance_stage4_eligible_source_count10_belowfull_cooldown_on
- e008_balance_stage4_eligible_source_count10_full_cooldown_off
- e008_balance_stage4_eligible_source_count10_full_cooldown_on
- e008_balance_stage4_eligible_source_count50_belowfull_cooldown_off
- e008_balance_stage4_eligible_source_count50_belowfull_cooldown_on
- e008_balance_stage4_eligible_source_count50_full_cooldown_off
- e008_balance_stage4_eligible_source_count50_full_cooldown_on
- e008_balance_stage4_eligible_source_count180_belowfull_cooldown_off
- e008_balance_stage4_eligible_source_count180_belowfull_cooldown_on
- e008_balance_stage4_eligible_source_count180_full_cooldown_off
- e008_balance_stage4_eligible_source_count180_full_cooldown_on

## MCP evidence and result classification

Live tool metadata exposed mcp__hoi4_agent_tools__hoi4_probability_inspect, probability_evaluate, probability_sweep, probability_compare, and probability_render; the relevant compare source and scenario properties are typed as unknown in the exposed schema.

The read-only direct_random inspect targeted common/scripted_effects/008_tensions_rising_effects.txt with refresh=false and the existing workspace ID mod_chaos_redux_ea3b2d67c2c0; the event_mean_time_to_happen inspect targeted events/008_tensions_rising.txt with refresh=false.

Both inspect calls remained pending for 44 seconds and were manually stopped under the parent?s no-retry instruction; neither returned a tool payload, artifact URI, source revision, adapter report, accepted nested state schema, or blocker code.

The mandatory same-scenario direct_random compare was submitted once with scenario-set ID E008_BALANCE_SOURCE_MODEL_2026-10-06, immutable before path auditor/baseline/sources/common/scripted_effects/008_tensions_rising_effects.txt, current after path common/scripted_effects/008_tensions_rising_effects.txt, and refresh=false.

That compare remained pending for 44 seconds and was manually stopped under the parent?s no-retry instruction; it returned no comparison ID, artifact URI, source revision, scenario hash, numeric result, ranking, delta, or terminal error code.

The compare binds the baseline effect file only; the baseline constants, trigger, event, scripted-localization, and English dependencies are explicitly unbound, so any hypothetical effect-only response could not establish a complete before/after result.

No probability_evaluate or probability_sweep call was submitted because the mandatory inspect route returned no source analysis or accepted nested input schema.

No probability_simulate call was submitted because the declared source counts and state bands are deterministic model inputs, not uncertainty distributions with declared seeds or sampling assumptions.

No probability_sequence call was submitted because the global weighted event pool, candidate set, cadence, state transitions, recovery, cooldown lifecycle, and terminal states were not complete.

No probability_render call was submitted because no analysis ID or comparison artifact was returned; no rendered evidence URI or path exists.

The parent reported the latest reference resource-read route failure as Transport closed; this audit records that service gap and the two pending-and-stopped probability batches without retrying.

The exact result classification is: requested packet constants and source control flow are source-confirmed; direct target selection, actual applied effects, automatic firing frequency, and timing are unresolved; no exact, bounded, or sampled probability estimate was produced.

## Findings

The baseline packet and country-slice values are large requested contributions whose display was not tied to the native global-threat delta; the parent?s screenshot premise at 99% WT therefore cannot be treated as proof of a 100-point actual change.

The after source corrects that reporting mismatch by reading the native global.threat difference and the final global chaos meter difference, but actual values at the parent?s scenario inputs remain unresolved without MCP or runtime evidence.

The baseline source has no Event008-specific cooldown; the after source adds a global 30-day automatic eligibility gate, while manual requests bypass the gate and intentionally start or refresh the timer under the parent?s accepted behavior.

The source candidate predicate includes every existing non-special Chaos country; subjects and capitulated countries are not excluded from the world-tension recipient predicate, so scenario counts cannot be mapped to real candidate IDs without a complete campaign roster.

No weighted score ranking or probability-proportional candidate pool exists in this helper; random recipient selection among eligible source countries is distinct from the amount-per-recipient calculation.

Dominance, starvation, rank reversals, and per-country selection frequencies are unresolved because the actual candidate identities, exact pool, and supported direct_random analyzer response were unavailable.

Automatic repetition is bounded by the new 30-day global flag at the source gate, but campaign-level frequency and any interaction with the shared event pool remain unresolved; manual repetition and report coalescing are intentional accepted behavior.

No AI weight, AI score, MTTH timing, event-option ai_chance, or focus/research/doctrine selection weight was found in this six-file Event008 surface; the root event is triggered-only.

The source values are fixed tuning constants rather than dynamic weights; the packet, recipient-cap, and cooldown choices supplied by the owner are not independent balance recommendations from this auditor.

## Recommended follow-up

The owner-supplied packet values 2/3/5/8/12, 0.1 minimum slice, dynamic cap, and 30-day automatic gate are recorded as implementation choices; this auditor does not select balance targets.

If the analyzer route becomes available, re-run a verified inspect and evaluate/sweep for the same named direct_random scenarios, supply a complete real or explicitly synthetic candidate set supported by the live adapter, and use a compare source schema that binds the before-side constants and trigger dependencies.

Keep world-pool recurrence unresolved until a complete active event-pool manifest includes current weights, settings, timer cadence, cooldown changes, recovery, and terminal states.

No source changes were applied by this auditor.

## Skipped surfaces and remaining uncertainty

The structural event_inspect/event_render route was not used because the parent narrowed this handoff to a single direct_random/MTTH probability inspect batch and one compare; structural event evidence is not claimed. The separate Event008 random_list follow-up pools, timer draws, AI-posture recipient selection, relation-pair selection, and border-war target selection remain skipped, because the owner?s requested scenarios and source snapshots target the recipient packet cap and automatic gate.

The offline wiki and installed-game documentation were not queried in this weighted-only read-only pass; the reference resource-read route was reported by the parent as Transport closed, and no documentation claims are made here.

No vanilla source comparison, runtime playtest, screenshot validation, or campaign save inspection was performed.

No comparison/render artifact, scenario hash, or engine probability evidence was available at final document freeze.
