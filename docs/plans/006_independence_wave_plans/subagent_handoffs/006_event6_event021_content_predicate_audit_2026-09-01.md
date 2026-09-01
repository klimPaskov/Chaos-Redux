# Event 006/Event 021 content-predicate audit

Date: 2026-09-01.

Scope: read-only audit of the current working-tree substitutions in `common/scripted_triggers/006_independence_wave_triggers.txt` and the changed `common/scripted_triggers/006_independence_wave_*_package_triggers.txt` files, with Event 006 and Event 021 lifecycle tracing.

Disposition: do not commit the current predicate changes as one unit.

No gameplay source was edited by this audit, and no file was staged or committed.

## Executive conclusion

The direct package-trigger substitutions from `is_independence_wave_active_country` to `is_independence_wave_package_content_active` are semantically appropriate for ordinary Event 006 packages.

The package-content helper delegates its ordinary branch to the strict Event 006 active-origin check and retains each package's `original_tag`, package-id, carrier, identity, and Soviet-origin exclusions, so the substitutions do not by themselves admit arbitrary countries or widen Event 005 behavior.

The replacements on the three founding-phase gates are also directionally required for an Event 021 adapter actor to consume Event 006 package content after the adapter receipts are proven.

The unsafe part is the new transient Event 021 branch inside `is_independence_wave_active_country` at `common/scripted_triggers/006_independence_wave_triggers.txt:9-26`.

That predicate has about 186 lifecycle, event, decision, idea, focus, scripted-GUI, on-action, evolution, and compatibility callers, so making `random_civil_war_event6_adapter_preparing` plus `independence_wave_event6_adapter_package_ready` satisfy it exposes a not-yet-complete Event 021 package as an Event 006 active country.

This conflicts with the Event 021 contract that package creation must not activate or commit Event 006 origin, fired-count, evolution-history, network, or league state, and it creates pre-completion visibility risk for Event 006 UI and incident/evolution surfaces.

Recommendation: keep `is_independence_wave_active_country` strict to the Event 006 active-origin flag, Event 006 liberation origin, and non-ended state; move any transient adapter setup allowance needed by package initialization into `is_independence_wave_package_content_active` with an explicit adapter-package/setup-input guard; retain the proven-receipt branch for post-setup content.

The duplicate Scotland/Wales adapter OR at `common/scripted_triggers/006_independence_wave_scotland_wales_package_triggers.txt:8-28` should be removed or made identical to the shared package-content contract during that follow-up because it independently admits preparing/complete flags without all four receipt flags and the package variable.

## Predicate and lifecycle map

| Surface | Scope and inputs | Output and side effects | Audit result |
| --- | --- | --- | --- |
| `is_independence_wave_active_country` | Country scope; Event 006 active-origin flag, Event 006 liberation origin, and non-ended guard. | Lifecycle eligibility only; no side effects. | Must remain strict. The transient adapter branch is too broad for its callers. |
| `is_independence_wave_package_content_active` | Country scope; strict active country, or Event 021 adapter-complete/setup-proven/origin-recorded/origin-adapter-complete receipts, package variable, and non-active/non-ended guards. | Package content eligibility only; no side effects. | Correct abstraction for package triggers and phase gates. Add the bounded transient setup branch here if setup calls require it. |
| Package country predicates | Country scope; package `original_tag`, package id, shared content predicate, and package-specific identity/carrier/origin exclusions. | Package-specific eligibility; no side effects. | Direct substitutions are safe for regular Event 006 packages. Positive Event 006-origin checks remain intentionally restrictive. |
| Event 021 transient flags | `random_civil_war_event6_adapter_preparing` and `independence_wave_event6_adapter_package_ready` are set before shared setup and cleared after the setup result. | Bounded setup input; not a committed Event 006 origin. | These flags must not satisfy the global Event 006 active classifier. |
| Event 021 persistent receipts | `random_civil_war_event6_adapter_complete`, `independence_wave_event021_adapter_setup_proven`, `random_civil_war_event6_origin_recorded`, `random_civil_war_origin_adapter_complete`, and `independence_wave_package_id`. | Origin-neutral post-setup package-content proof. | Appropriate second branch for the shared package-content helper. |

## Evidence

The current top-level predicate is at `common/scripted_triggers/006_independence_wave_triggers.txt:9-26` and includes the transient adapter OR branch.

The current shared package-content predicate is at `common/scripted_triggers/006_independence_wave_triggers.txt:28-43` and includes the strict active branch plus the four adapter receipts, package variable, and active/ended exclusions.

The current force-package gate has separate transient and complete adapter branches at `common/scripted_triggers/006_independence_wave_triggers.txt:157-185`, which is evidence that force setup already models adapter state separately from the lifecycle predicate.

The three founding-phase gates use the package-content helper at `common/scripted_triggers/006_independence_wave_triggers.txt:245-269`.

The Event 021 parent proves package setup through `event021_parent_event6_package_setup_proven` and `event021_parent_event6_package_complete` at `common/scripted_triggers/021_random_civil_war_parent_triggers.txt:60-127`.

The parent sets transient flags, invokes `independence_wave_prepare_country_origin` and package dispatch, then records the adapter receipts and clears the transient flags at `common/scripted_effects/021_random_civil_war_parent_effects.txt:2554-2634`.

The adapter origin effect explicitly sets completion receipts without activating or committing Event 006 origin at `common/scripted_effects/021_random_civil_war_effects.txt:1098-1127`.

The absorbed-adapter cleanup clears receipt flags and package state through `event021_cleanup_absorbed_event6_adapter` at `common/scripted_effects/021_random_civil_war_effects.txt:1129-1150`, with generation reset delegated to `independence_wave_reset_current_generation`.

The Event 006 normal activation and commit path requires `is_independence_wave_active_country` and is separate from adapter preparation at `common/scripted_effects/006_independence_wave_effects.txt:693-932`.

Event 006 refresh gates package content with the shared helper but gates evolution feedback and achievements again on the strict Event 006 active-origin state at `common/scripted_effects/006_independence_wave_effects.txt:71-93` and `common/scripted_effects/006_independence_wave_effects.txt:182-199`.

Event 021's explicit package registry contains `iw_070`, `iw_071`, and `iw_072` at `common/scripted_effects/006_independence_wave_event021_adapter_registry_effects.txt:43-45` and maps them to ARM, GEO, and AZR at lines 84-86.

Those three package predicates still require `liberation_origin = independence_wave` at `common/scripted_triggers/006_independence_wave_transcaucasus_package_triggers.txt:9-40`, while the Event 021 adapter intentionally leaves the Event 006 liberation origin unset/neutral.

Therefore the current substitutions cannot make those three origin-restricted package predicates adapter-compatible without weakening an origin guard, and weakening it would risk Event 005 or other-origin behavior.

Event 005 does not call either shared Event 006 predicate; its candidate and origin guards use direct active-origin/Soviet-origin checks, including `common/scripted_triggers/005_soviet_collapse_triggers.txt:14-16` and the Event 005 release logic around `common/scripted_effects/005_soviet_collapse_effects.txt:5741-5756`.

The Event 006 specification requires no pre-event pressure/category/mission/queue visibility in `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_2_event_flow_and_evolutions.md:35-41`, and the origin separation model preserves Soviet and other origins in `docs/specs/006_independence_wave_specs/diagrams/006_origin_separation_model.md:8-20`.

The Event 021 package contract requires complete package reuse with a separate origin and no Event 006 fired/evolution/history/network/league mutation in `docs/specs/021_random_civil_war_specs/021_random_civil_war_spec_part_7_event_006_country_packages_and_focus_handling.md:135-173` and `:455-475`.

## Helper, constants, targets, and migration plan

No new scripted helper or tuning constant is proposed by this audit.

The existing helper map is sufficient if the strict lifecycle predicate and origin-neutral package-content predicate remain separated.

No script constants or tuning tables need changing.

The existing regular event targets `independence_wave_setup_former_host` and `independence_wave_setup_anchor_state` are saved during Event 021 preparation and are consumed by force/package validation; no new global target is warranted.

The existing reset and absorbed-adapter cleanup paths are the correct cleanup owners for package variables, receipt flags, and setup targets.

Recommended migration order:

1. Remove the transient adapter OR branch from `is_independence_wave_active_country`.
2. Preserve the direct package-trigger substitutions and the phase-gate substitutions.
3. Add the minimum transient adapter setup branch, if still required by package initialization, to `is_independence_wave_package_content_active` with package/setup-input proof and no active-origin mutation.
4. Remove the Scotland/Wales duplicate adapter OR and rely on the shared helper.
5. Treat `iw_070`/`iw_071`/`iw_072` as a separate fail-closed registry decision: either remove them from the Event 021 allowlist until their origin-neutral package contract exists, or add a narrowly designed adapter receipt accepted only by those package predicates. Do not remove their Event 006-origin guards globally.
6. Re-run direct-caller and Event 006/Event 021 MCP inspections after the parent applies the narrow fix.

## Validation, blockers, and risks

Required offline Paradox wiki pages, the relevant Event 006/Event 021 specifications, and vanilla script/effects/triggers documentation were consulted before this audit.

Read-only Event MCP scans were run for `chaosx.nr6.1` and `chaosx.nr21.1` with `hoi4_event_inspect`.

The authoritative scan artifacts are `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6bdd4c4dca15ce54d1ea548110cd62ac2f526613ad6731edb3ac47ef29e27550/7ad88267e7b5a6b6b1d9cd7e212a185a2477803c2458d63d72e59b9b66a38710/event-scan-2725045f62d1.json` and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b12de65c319fade63633aeed14a91489ef88c1d6fa1331caf02546e4c2dea382/c75107d1df102391d8ec1beabaf5317f1851508378a26845b11ddecc2fd06667/event-scan-2725045f62d1.json`.

The MCP scans returned `EVENT_INSPECTED_PARTIAL` with a deferred workspace-wide lifecycle pass and one blocking diagnostic, so they are supporting evidence rather than a clean engine validation result.

The exact vanilla scripted-localisation documentation path requested by the repository instructions, `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/scripted_localisation_documentation.md`, is absent from the installed documentation folder.

Live game execution was not performed, per repository instructions.

Concurrent changes in the package files, including unrelated leader, threshold, and Scotland-specific edits, were preserved and are outside this audit's disposition.

The residual risk is stale adapter receipts after an interrupted effect chain; normal abort and absorbed-adapter cleanup clear them, but source inspection cannot prove recovery from every interrupted runtime transaction.

No patch is justified in this read-only audit.
