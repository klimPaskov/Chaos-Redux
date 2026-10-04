# Event 31 wave-target post-owner-patch comparison

Status: read-only after-source review delivered; the mandatory numerical comparison remains open. No gameplay source, weights, candidate pools, or scenario fixture were edited. No numeric or normalized probability claim is made.

## Scope and provenance

This handoff covers the owner-applied Event 31 wave scope, site-eligibility, caller-output, array-lifetime, reservation, and shared ticket-helper changes. The owner repair handoff is [031_multi_country_wave_scope_repair_20261003.md](031_multi_country_wave_scope_repair_20261003.md). Its reported accepted design and its source findings were reviewed before this comparison pass.

The worktree `HEAD` during review was `1857b35ab7dcba1707b2dee6fe1276b00ad4a64b`. The four owner-edited source/documentation files remain modified in the worktree. This is a source revision receipt only; the MCP service returned no after-source revision.

The unchanged fixture is [031_wave_scope_probability_scenarios_20261003.json](../evidence/031_wave_scope_probability_scenarios_20261003.json), local SHA-256 `C211340E65576247901EDEA1CB8308A0EB65718575F83FD7194CDBFCF3401B18`, fixture id `event31_wave_scope_baseline_20261003`. It was parsed from that exact file for both submitted comparisons. Its 17 scenario IDs remain unchanged: `wave_three_countries_root_a`, `wave_root_ineligible`, `wave_foreign_owned_root_occupied`, `wave_load_0_1_2_3`, `wave_load_case_0`, `wave_load_case_1`, `wave_load_case_2`, `wave_load_case_3`, `wave_existing_provider_exclusion`, `wave_helper_return_frames`, `wave_helper_return_frames_caller_owned`, `wave_identity_invariance`, `wave_population_cohort_invariance`, `wave_site_rejections`, `wave_short_pool`, `wave_distinct_countries_once_pacing`, and `wave_scenario_shared_callers`.

The fixture preserves the named synthetic scenario declarations, not accepted typed ROOT/A/B/C country or state bindings. State owners/controllers, provider predicates, helper-frame persistence, and complete campaign-world candidate pools remain unresolved. Its file hash is not an MCP scenario hash.

## Immutable before and current after source receipts

The eight physical before snapshots under `docs/plans/031_random_terror_plans/evidence/wave_scope_before_20261003/` were read and hashed without modification. Current after paths and hashes were read from the worktree.

| Source | Before SHA-256 | Current after SHA-256 | Source status |
| --- | --- | --- | --- |
| `common/scripted_effects/031_random_terror_effects.txt` | `8EDD15C352B0B4A8143B7A391078B5B6C0A01A41FE64FEA73CC86CED7B68B37A` | `DD87C9D0DE7AE88CE258A0D798B9410A33C37B00B7F011271C8B0AB649760E85` | Owner patch present |
| `common/scripted_triggers/031_random_terror_triggers.txt` | `3848A99005E8111A45B4BD49EF9C0821ACCD0C41029AAA5B1440182A685089C7` | `AEB0C8376214F1BF7BD498F8C266E9669284BC831984C21000287DCD2FAB0060` | Owner patch present |
| `common/scripted_effects/individual_crisis_targeting_effects.txt` | `903562C1DC27BF9367E5A8AB8A807047A798FB16DE0BD8E1DF2841B6A2C40B16` | `1D9D9A47CC514A51B9C9D40EEE1393A124CD42661AAA6B0D1CD2DF7BC8551705` | Caller-output initialization patch present |
| `common/scripted_effects/individual_crisis_targeting_effects.md` | `014ABB19AEF88D1821A10EC63BA16BE0A35A96B85D5B65B5A1B27DC0F62B8155` | `3856A9104166DDAED5DB913610F36A2EBB66988D6508ED7157BF45AC57248A4F` | API documentation updated |
| `common/scripted_triggers/individual_crisis_targeting_triggers.txt` | `AF537F93E969948CA5CB35E1D06C504F6797CCBAAF659A13C9A661DB8E510B70` | `AF537F93E969948CA5CB35E1D06C504F6797CCBAAF659A13C9A661DB8E510B70` | Byte-identical |
| `common/script_constants/individual_crisis_targeting_constants.txt` | `8B4471A8412E3A883570743E0EE17037129DCEAA889D63781AC8FC2C3529E002` | `8B4471A8412E3A883570743E0EE17037129DCEAA889D63781AC8FC2C3529E002` | Byte-identical |
| `common/script_constants/031_random_terror_constants.txt` | `84AECCA5BE338433A9A9BF2BFBA5682BE8256D790A6940E1C5561D7705EA09B8` | `84AECCA5BE338433A9A9BF2BFBA5682BE8256D790A6940E1C5561D7705EA09B8` | Byte-identical |
| `events/031_terrorist_attack.txt` | `8EA0D99D25C62DE0A4BE6F8D9A64CD827E7F575E158A01C6832A038B84C311BE` | `8EA0D99D25C62DE0A4BE6F8D9A64CD827E7F575E158A01C6832A038B84C311BE` | Byte-identical |

The local source comparison used the immutable copied files as `before.path` and current repository source as `after.path`; no same-current-source comparison was made. The exact relative paths submitted are listed in the MCP ledger below.

## Source-after findings

The candidate-country controller checks now use `PREV` inside the mapped owned-state iterators in `random_terror_country_is_normal_target` and `random_terror_country_has_valid_state` (`common/scripted_triggers/031_random_terror_triggers.txt:53-107`). The new `random_terror_state_is_eligible_incident_site` checks positive population, cooldown, and lost-local-control without an owner/controller relationship (`:74-82`). The country-valid-state iterator combines that predicate with its candidate-relative controller check (`:102-106`).

The existing action-rooted `random_terror_state_is_valid_target` still enforces `is_controlled_by = ROOT` or `is_owned_by = ROOT` (`common/scripted_triggers/031_random_terror_triggers.txt:84-90`). The intrinsic predicate is also composed into that existing trigger, in addition to the country-valid-state iterator and the automatic/scenario owned-controlled-state draws. The ROOT relationship remains explicit; this is a call-site-boundary detail, not evidence that candidate typed scopes were exercised.

The automatic selector initializes and clears its caller-owned array before rebuilding the candidate pool, revalidates a selected country, selects an owned-and-controlled state with the intrinsic site predicate, and sets a caller-owned success receipt after `random_terror_apply_incident` (`common/scripted_effects/031_random_terror_effects.txt:1015-1045`). It applies the existing two-day reservation only when that receipt is positive, using literal integer meta-effect text from the unchanged `wave_cooldown_days` constant. The scenario selector likewise initializes/clears the array before its candidate pass (`:1372-1384`). Source inspection supports the intended ordering and scope structure; array-frame lifetime, scope return, incident success, and engine execution were not demonstrated at runtime.

The Event 31 candidate adder initializes `individual_crisis_candidate_adjusted_weight` before either shared wrapper (`common/scripted_effects/031_random_terror_effects.txt:997-1013`). Both public shared wrappers initialize their forwarded output, and the private curve worker initializes active-load and adjusted-weight storage before the load trigger (`common/scripted_effects/individual_crisis_targeting_effects.txt:9-34`). The helper Markdown documents caller-owned outputs. The opening evolution resolver initializes its consumed result before the nested identifier helper (`common/scripted_effects/031_random_terror_effects.txt:922-937`). These are source-contract observations, not analyzer or engine persistence evidence.

The shared raw ticket curve remains base weight one and multipliers 4/2/1 at loads zero/one/two, with zero at load three or above and cap three (`common/scripted_effects/031_random_terror_effects.txt:997-1007`, `common/scripted_effects/individual_crisis_targeting_effects.txt:29-80`, `common/scripted_triggers/individual_crisis_targeting_triggers.txt:102-117`, and the unchanged constants above). Existing-provider self-exclusion remains a single temporary boolean exclusion. Event target-count constants, provider definitions in the supplied unchanged sources, and root-event pacing source are unchanged. These values are raw ticket settings and are not normalized probabilities.

Source-wise, the owner patch removes the receiver-rooted candidate-site mismatch and avoids reserving a country before a successful site application. This can change eligible candidates and the pool actually presented to the unchanged ticket curve. The direction and magnitude of ranking, normalized shares, success counts, starvation, dominance, or rank reversals are not established without a complete typed pool and returned MCP comparison.

## MCP request ledger

All requests used the connected `hoi4-agent-tools` probability routes. No artifact URI, source revision, scenario hash, trace, ranking, numeric value, or rendered result was returned as of this handoff.

| Request | Exact source/payload | Outcome at handoff |
| --- | --- | --- |
| `hoi4.probability_inspect` | `adapter=custom_weighted_pool`; `source.path=common/scripted_effects/031_random_terror_effects.txt`; `refresh=true` | Returned `tool call error: tool call failed for hoi4_agent_tools/hoi4.probability_inspect; Caused by: timed out awaiting tools/call after 600s`. No artifact or revision. |
| Narrow `hoi4.probability_inspect` | `adapter=custom_weighted_pool`; `source.path=common/scripted_effects/individual_crisis_targeting_effects.txt`; `refresh=true` | Returned `tool call error: tool call failed for hoi4_agent_tools/hoi4.probability_inspect; Caused by: timed out awaiting tools/call after 600s`. No artifact or revision. |
| `hoi4.probability_compare` | `adapter=custom_weighted_pool`; before path `docs/plans/031_random_terror_plans/evidence/wave_scope_before_20261003/common/scripted_effects/031_random_terror_effects.txt`; after path `common/scripted_effects/031_random_terror_effects.txt`; exact parsed fixture above; outputs `json`, `comparison`, `unresolved`; `refresh=true` | Returned `tool call error: tool call failed for hoi4_agent_tools/hoi4.probability_compare; Caused by: timed out awaiting tools/call after 600s`. No artifact, source revision, or scenario hash. This single-file attempt does not validate the transitive helper/provider closure and yields no numerical conclusion. |
| Narrow shared-curve `hoi4.probability_compare` | `adapter=custom_weighted_pool`; before path `docs/plans/031_random_terror_plans/evidence/wave_scope_before_20261003/common/scripted_effects/individual_crisis_targeting_effects.txt`; after path `common/scripted_effects/individual_crisis_targeting_effects.txt`; same exact parsed fixture; outputs `json`, `comparison`, `unresolved`; `refresh=true` | Returned `tool call error: tool call failed for hoi4_agent_tools/hoi4.probability_compare; Caused by: timed out awaiting tools/call after 600s`. No artifact, source revision, or scenario hash. This was a transport timeout, not a cancellation or a numerical comparison result. |

The initial broad compare has only the Event 31 effects file on each side, and the focused compare has only the shared curve effects file on each side. Neither includes a validated manifest for the full helper graph. No `beforeManifest`, `afterManifest`, or candidate list was fabricated because the inspect route did not return the manifest/candidate schema. The dependent 14-provider closure, typed scope-binding contract, complete world pool, controller/owner inputs, external provider states, and temporary-frame semantics are explicitly unresolved. Do not interpret a future partial response as complete-pool probability evidence.

The earlier baseline handoff records its own broad/narrow inspect and evaluate requests timing out after 600 seconds. Those are baseline-route outcomes, not after-patch numerical comparison results. They do not satisfy the mandatory same-fixture comparison.

## Scenario evidence classification and remaining work

All 17 fixture entries are present and were parsed identically for the submitted comparison requests. The four `wave_load_case_*` entries are bounded declared direct-curve inputs; the other entries describe synthetic pool, ownership/control, provider, site, identity, frame, attempt-count, pacing, or caller-boundary cases. Fixture labels do not bind engine scopes. No per-scenario analyzer result returned, so every comparison outcome, complete normalized pool, external-factor trace, and sequence result is unresolved. No sampled evidence was requested or produced.

No numeric tuning recommendation is made. Preserve the owner patch and existing raw curve pending a returned, revision-bound comparison with a matching frozen before/after helper dependency set and accepted typed scope/pool bindings. Until then, provider-derived load, valid candidate ranking, success-count behavior, repetition/cadence, terminal behavior, and exploit risk remain unverified. Parent review and live-game validation remain outside this source-only handoff.

No gameplay files were edited, no weights or balance targets were selected, no fixture or before snapshot was changed, no game was launched, and no logs were searched. The only new task artifact is this comparison handoff.
