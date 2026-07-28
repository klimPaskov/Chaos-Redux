# Event 006 IW-085 — Cyrenaica vanilla LBA autonomy overlay adapter

## Status

`PARTIAL / RESEARCH-GATED` — the safe additive source adapter is implemented, but the package remains non-selectable and does not authorize an independent Cyrenaica tag or invented claimant.

## Source contract

The accepted research resolves IW-085 to the existing `LBA` carrier under the Italian autonomy identity rather than a new country. The route gate requires `original_tag = LBA`, `is_subject_of = ITA`, `has_government = fascism`, and either `autonomy_satellite` or `autonomy_dominion`, matching the vanilla scripted identity family. The adapter preserves LBA history, cores, characters, and focus content and never fabricates a royal claimant, flag, tag, or independent country.

## Files added

- `common/script_constants/006_independence_wave_iw085_cyrenaica_constants.txt`
- `common/scripted_triggers/006_independence_wave_iw085_cyrenaica_triggers.txt`
- `common/scripted_effects/006_independence_wave_iw085_cyrenaica_effects.txt`
- `common/ideas/006_independence_wave_iw085_cyrenaica_ideas.txt`
- `common/decisions/categories/006_independence_wave_iw085_cyrenaica_categories.txt`
- `common/decisions/006_independence_wave_iw085_cyrenaica_decisions.txt`
- `common/on_actions/006_independence_wave_iw085_cyrenaica_on_actions.txt`
- `localisation/english/006_independence_wave_iw085_cyrenaica_l_english.yml`

## Implemented surface

The carrier receives Desert Mobility, Regency Legitimacy, and Coastal Security values with centralized caps and route-specific gains/losses. Five concrete-cost actions cover a regency cabinet, oasis depots, desert-cavalry integration, a timed state-663 coastal-guard mission, and a provisional assembly with a coastal-defense charter. Four lifecycle ideas expose contested regency, integrated desert command, assembly compact, and coastal-defense charter. The mission has explicit activation, availability, timeout, cancellation, failure, completion, and identity-gated pause/resume handling. State 663, the port/island archetype, and desert-nomadic force profile are recorded for shared Event 006 systems.

## Preservation and safety

No action creates units, political-power stores, country tags, states, history, flags, portraits, advisors, or focus content. The daily hook is `on_daily_LBA` and only the exact Italian-autonomy identity can initialize or resume the overlay. If the autonomy relationship changes, the overlay suspends and removes its lifecycle ideas.

## Validation evidence

- New source blocks have balanced braces and quotes and no unsupported literal `<=` or `>=` operators.
- The localisation file is UTF-8 with BOM.
- `python -B .tools/audit_event6_allocator.py` remains the allocator and scenario authority; no package selector or wave count changed.
- `hoi4.probability_inspect` read the decision source with `decision_ai_will_do` and returned validation passed, four discovered weighted candidates, and zero unresolved diagnostics. The `mission_ai_will_do` read likewise passed with one weighted mission candidate and zero unresolved diagnostics. Both pools require world-state inputs for runtime evaluation; no runtime, save/load, scenario, AI, or package-admission claim is made here.
- No HOI4 process was launched.

## Remaining acceptance work

The autonomy gate must be confirmed against the actual installed start-state relationship and the accepted historical symbol/leader research before any admission decision. Shared-focus insertion into the meaningful LBA tree, network, patron, league, host-survival, formable, symbol, save/load, and live carrier evidence remain open. Independent Cyrenaica remains deliberately suppressed unless the user authorizes a design exception.
