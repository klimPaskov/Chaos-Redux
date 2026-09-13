# Individual-crisis fixed-target companion contract

Disposition: blocked for executable implementation.
The bounded source review and architecture handoff are complete.
The missing companion remains unimplemented and no runtime pressure adjustment is claimed.
Acceptance basis: the independent task authorizes a narrow shared helper only when caller semantics support a safe contract, otherwise a precise blocked handoff.

## Exact blocker and smallest next change

Repository source searches found no declaration or invocation of `apply_individual_crisis_fixed_target_event_pressure` and no declared shared fixed-target pressure input.
Current generic callers initialize `individual_crisis_candidate_base_weight`, invoke a country-ticket helper, then consume `individual_crisis_candidate_adjusted_weight` in temporary ticket pools.
Those callers do not establish the companion's event-pressure contract.
Every executable consumer is outside this task's owned files, so adding one would exceed the write scope.
Adding an unused helper would leave this dependency unresolved and would violate the task instruction to avoid inventing a caller or claiming fake completion.

The smallest next parent change is to name one existing fixed-target event-selection consumer and record its exact country resolver, eligibility gate, pressure units, evaluation timing, output variable, missing-target rule, and subsequent weight scaling.
Then authorize one direct consumed call site alongside the shared companion and its paired documentation.
Do not start with a new event registry, central router, wrapper skill, or gameplay redesign.

`evaluate_random_event_selection_candidate` in `common/scripted_effects/chaosx_settings_effects.txt` is an existing integration boundary to review, not an authorized patch or an accepted consumer mapping.
It reads `event_weight` through `get_event_weight`, multiplies the candidate weight by 100, rounds it, and excludes a result below one.
`select_weighted_random_event_id` invokes that evaluation once while summing total weight and again while accumulating running weight.
A consumer at this boundary must use the same resolved target in both passes and perform no random target selection, reservation, persistent state mutation, or additional load adjustment between passes.
Pressure should be adjusted once from the unadjusted base before owner scaling and rounding if the parent accepts that boundary.
Do not write the adjusted pressure back into `global.event_weights`, because repeated evaluation would compound the adjustment and alter recovery state.

## Current source findings

The shared candidate effect, distinct Random Terror continuation entry point, derived-load trigger, and constants already exist in the workspace.
The 2026-09-02 dependency restoration handoff describes an earlier missing-source state and is historical evidence, not proof that those candidate declarations remain absent.

`events/003_the_holy_realm.txt:38` invokes `holy_realm_select_weighted_refuge_host`.
`common/scripted_effects/003_holy_realm_effects.txt:2517` prefers an eligible `TIB`, then uses `random_country` with `can_host_holy_realm_refuge` when Tibet is absent.
That eligibility permits Bhutan or Nepal in the absent-Tibet branch.
The selector publishes the regular event target `holy_realm_prefire_refuge_host` inside the event effect chain.
The documentation's former blanket fixed-Tibet classification cannot establish a central-picker target for that fallback branch.
No Holy Realm gameplay or selector change was made.

`events/005_soviet_collapse.txt:24` defines the entry event.
Its ordinary opening branch dispatches to `SOV` after a shared capacity check, while its joint-opening presentation branch is separate.
A first consumer based on that ordinary branch would still need an explicit distinction between first package application and an already pending presentation.
No Soviet Collapse consumer mapping is accepted by this handoff.

`video_game_in_sweden_select_stockholm_controller_host` and `video_game_in_sweden_select_stockholm_owner_host` build temporary candidate pools and publish a global host target.
Calling those selectors while summing event pressure would violate the proposed pure resolver requirement.
Other previously listed packages require an owner-specific target review before being classified as fixed-target consumers.

## Proposed helper map

All new names below are proposals and have no source declaration.

| Identifier | Scope | Inputs | Output | Side effects and call sites |
| --- | --- | --- | --- | --- |
| `apply_individual_crisis_fixed_target_event_pressure` | Explicit existing country selected by the owner and entered as `THIS` | Caller-initialized temporary `individual_crisis_fixed_target_base_pressure`, with no implicit default | Caller-preinitialized temporary `individual_crisis_fixed_target_adjusted_pressure`, starting at zero | Temporary scratch only, no persistent flags, variables, arrays, ideas, targets, selection, or reservation. First consumed call site is blocked pending parent mapping. |
| `individual_crisis_load_is_below_cap` | Same country | Existing authoritative provider markers, ordinary path must set exclusion scratch to zero | Existing Boolean capacity result and temporary `individual_crisis_active_load` | Reuse the existing derivation, do not copy its fourteen providers. Existing cap callers remain unchanged. |
| `adjust_individual_crisis_candidate_ticket_weight` | Candidate country | Existing temporary candidate base | Existing temporary adjusted tickets | Preserve current candidate callers and whole-ticket semantics. It is not a normalized-pressure API. |
| `adjust_individual_crisis_existing_provider_candidate_ticket_weight` | Existing Random Terror provider country | Existing temporary candidate base | Existing temporary adjusted tickets | Preserve its one-provider exclusion. The fixed-target first-application companion must count Random Terror normally. |

Passing the explicit country through the caller's scope block matches the installed Boolean scripted-effect precedent and avoids an unverified parameter schema.
An optional wrapper accepting a numeric scope pointer, target token, or meta-text parameter is not necessary for the smallest implementation and is not proposed as an accepted API.
The caller must guarantee a country scope, check that it exists, guard absent event targets before entering them, and preinitialize the adjusted result outside that block so a skipped scope leaves zero.
Inside a valid country, the companion must initialize its result to zero before any limit, ignore nonpositive base pressure, rebuild load, and multiply the positive base by the normalized factor only below cap.
Reset `individual_crisis_exclude_random_terror` to zero before and after ordinary load evaluation so continuation scratch cannot silently exempt a provider.
Do not scope temporary variables with `ROOT`, `PREV`, or `THIS`.

## Constants and tuning plan

| Existing constant | Value | Companion use |
| --- | ---: | --- |
| `individual_crisis_targeting.zero` | 0 | Initialize result and exclusion scratch, reject nonpositive base |
| `individual_crisis_targeting.one` | 1 | Existing provider increment, no new Boolean numeric state |
| `individual_crisis_targeting.load_one_upper_bound` | 2 | Existing load-one band boundary |
| `individual_crisis_targeting.active_cap` | 3 | Fail closed at cap and above |
| `individual_crisis_targeting.load_zero_factor` | 1.00 | Positive base at load zero |
| `individual_crisis_targeting.load_one_factor` | 0.50 | Positive base at load one |
| `individual_crisis_targeting.load_two_factor` | 0.25 | Positive base at load two |

No constants need to be added or tuned for the proposed pure arithmetic.
Keep the existing fixed-point schema and `constant:` access in temporary arithmetic.
Candidate ticket multipliers remain 4, 2, and 1.
The companion must not convert those tickets into integer event pressure, clamp fractional pressure to one, add a floor, or choose a rounding rule.
Downstream scale and rounding remain the accepted consumer's responsibility.
Values smaller than the fixed-point representation can quantize, so arbitrary real-number exactness is not promised.

## Event targets, variables, and cleanup

The companion saves or clears no event target and owns no persistent variable, flag, package registration, or cooldown.
For a short effect chain, the owner may already have a regular event target that it validates before entering.
For a long-lived owner target, the owner retains its existing global-target validation and cleanup responsibility.
This proposal creates no global shared pointer and no shared cleanup effect.
All helper inputs, outputs, and scratch remain temporary and must be initialized by the caller in the enclosing effect block before invoking the helper.
The offline Data structures page explicitly warns that temporary values first created inside a scripted helper may not survive the helper boundary, while values initialized outside and modified inside do.
Provider lifecycle endings continue to change the next derived load through their existing markers.
No persistent load counter, world iteration, on-action, or reconciliation pass is added.

## Migration plan

1. Accept one explicit owner mapping and establish its complete event pool and named probability baseline through `chaosx_ai_probability_auditor`.
2. Add the narrow normalized-pressure effect with the existing cap trigger and factor constants, plus one consumed owner call site and complete helper documentation.
3. Initialize base, result, and shared scratch before entering the target scope, apply pressure once, and consume the output before scale and rounding at the accepted boundary.
4. Preserve candidate-ticket callers and provider-exclusion behavior, then compare the same named consumer scenarios through the read-only probability auditor.
5. Migrate additional proven fixed-target owners individually after their target, first-application, continuation, and cleanup semantics are documented.

There is no duplicated fixed-target arithmetic to remove in the currently inspected shared files.
This is a missing consumed adapter rather than a cosmetic helper extraction.

## Validation and evidence limits

Focused PowerShell static checks read the three shared script files and verified all seven referenced shared constants resolve, counted fourteen derived provider increment branches, found no persistent mutator or world-country scope in the shared effect and trigger bodies, and checked that each ticket band equals four times its normalized factor with cap three.
These checks establish source-contract consistency only and do not execute Clausewitz or validate a probability distribution.
Repository source searches found no fixed-target companion declaration, invocation, or declared shared fixed-target base-pressure input.
Direct review confirmed the picker's scale-and-round boundary and two-pass evaluation, the candidate input/output lifecycle, and the Holy Realm target-resolution branch.

Required probability inspection used `mcp__hoi4_agent_tools__hoi4_probability_inspect` on `common/scripted_effects/individual_crisis_targeting_effects.txt`.
It returned `PROBABILITY_SOURCE_DISCOVERED`, status `ok`, `discoveryReason = no_weighted_surfaces`, zero candidates, zero required inputs, and no available adapter for this file.
Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/acbe511d73f0f8824f65da26b41d6a0595814990084fbab1602ba4d6dadd8505/591b132b755df13f5b2ba0f8ef2ca045f482e20c81fcb83fd3cfbe8bca1d8ed2/probability-inspect-fe7abecca820.json`.
Source revision: `062979bb2370063fbcc85fab9f1109905efcad09e7c53b9bfddb576209eb7116`.
This is discovery evidence, not a complete candidate-pool baseline.

Required event inspection and target rendering were attempted on `chaosx.nr21.1` using the supported selector `{ kind: event, eventId: chaosx.nr21.1 }`.
Inspection returned `EVENT_INSPECTED_PARTIAL`, with `analysisMode = focused`, `counts.helpers = 0`, and validation false because workspace-wide helper projections and lifecycle passes were deferred.
Refreshing the inspection did not remove that boundary.
Refreshed trace artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a608eee7999949d4a07fd8da63b109ba269c66c4a47df474a9c428c072a5104e/0409962f673dfcc71ce9e64483fdadf886394fce07cd4e00fb9c13298f71520d/event-trace-3ac0bcfca142.json`.
The target render returned `EVENT_RENDERED_PARTIAL`, validation false, focused analysis, and zero selected nodes despite the source root existing at `events/021_random_civil_war.txt:13`.
Render data artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/18b16a478622461edd5b9a69c5bdfcff6f4a03b39b705c2e10cae65ef456f880/5fb1cc5ba9d6f1c12f1ef71ad75917ab4860eb46f6bbea5042d4ef49006916ab/event-targets-3ac0bcfca142.json`.
Neither route establishes helper lifecycle coverage or a valid rendered caller graph for this contract.
No artifact conversion or source-only substitute is claimed.

`chaosx_ai_probability_auditor` was dispatched read-only with no inherited context as agent `01a09b40-aa0a-7132-9fa5-666494ff7410`.
It did not return a final report after repeated bounded waits and an explicit request to return acquired evidence, and was closed while still running.
The specialized evidence pass is therefore incomplete, with no auditor result or scenario-validation claim.
The direct MCP discovery above remains the only acquired probability evidence in this task.
The parent must rerun the specialized baseline and comparison after declaring a consumed adapter rather than treating dispatch as an audit pass.

Required future contract scenarios are `FT-00` positive base at load zero, `FT-01` load one, `FT-02` load two, `FT-03` cap three, `FT-04` above cap, `FT-Z` zero base, `FT-N` negative base, `FT-M` missing or nonexistent target, `FT-F` fractional positive base, and `FT-X` preexisting Random Terror exclusion scratch.
For a representable base of 8, the proposed positive-band results are 8, 4, 2, 0, and 0.
These are acceptance expectations, not executed helper results.
The consumed surface also needs identical-target two-pass coverage, repeated evaluation from the unadjusted base, target invalidation before application, and comparison against all other events in its declared normalization pool.
Probability evaluation, sweep, simulation, sequence, render, and compare were not substituted with invented pools or manifests.
Consumer-distribution validation is blocked by the missing consumed adapter and complete scenario contract.
No gameplay patch exists to compare.
HOI4 was not launched and no live or engine execution validation is claimed.

## Files, limitations, and follow-up

Changed files: this handoff, `common/scripted_effects/individual_crisis_targeting_effects.md`, and `docs/systems/event_system/individual_crisis_targeting.md`.
Changed executable identifiers, direct call sites, constants, cleanup hooks, localisation keys, and assets: none.
No Event021 gameplay, other event gameplay, workbook, or asset was edited.
No fallback or simplification was implemented.
The companion's runtime implementation remains blocked, with its proposed inputs and output explicitly unresolved until the first owner mapping is accepted.
No commit is created for blocked executable work or for preexisting untracked shared scripts owned by other workspace work.

Skills used: `chaos-redux-events`, `chaos-redux-mtth`, and `chaos-redux-subagents`.
No skill was created or updated.
Installed vanilla `script_concept_documentation.md`, `common/script_constants/documentation.md`, and the relevant effects and triggers documentation entries were consulted alongside the offline core wiki pages.
The vanilla `common/scripted_effects/00_scripted_effects.txt` overview demonstrates the Boolean helper invocation, and the installed hidden-trigger example documents temporary side effects with `tooltip_evaluation = eval`.
The existing Chaos Redux dynamic registry and its paired documentation were inspected and provide no already consumed fixed-target pressure companion.
