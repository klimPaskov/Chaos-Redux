# Event 35 Great Depression 2.0 localisation audit

Date: 2026-09-01

## Verdict

The bounded source audit is complete, and Event 35 has full source-level key coverage for its current event, decision, mission, achievement, event-log, evolution, cluster, and super-event consumers.

The package is not ready for an unconditional runtime-localisation verdict.

The inherited Event 34 opening still uses the same generic `chaosx.nr35.2.d` text as every other entry path, despite the specification requiring player-facing text that identifies the hard-landing reversal without exposing the raw Overheating implementation state.

The source audit also cannot prove runtime scripted-localisation selection or the final wrapping of the ordinary decision category.

## Scope and evidence reviewed

- Read `AGENTS.md`, `.agents/skills/chaos-redux-events/SKILL.md`, `.agents/skills/chaos-redux-decisions-missions/SKILL.md`, `.agents/skills/chaos-redux-super-events/SKILL.md`, and `.agents/skills/chaos-redux-subagents/SKILL.md`.
- Read the complete `docs/specs/035_great_depression_specs/` package and `docs/events/035_great_depression.md`.
- Inspected Event 35 events `.1` through `.6`, decisions, missions, scripted triggers used as visible requirements, scripted localisation, achievements, event history and details, evolution bridges, Negative Economy cluster strings, super-event slot 105, and inherited Event 34 references.
- Consulted the required offline Paradox wiki localisation and event/decision references, official vanilla documentation, and vanilla decision-localisation precedents.

## Changed files and keys

### `localisation/english/035_great_depression_l_english.yml`

- `chaosx.nr35.2.a`
- `chaosx.nr35.4.d`
- `chaosx.nr35.5.d`
- `chaosx.nr35.6.d`
- `great_depression_category_desc_national`
- `great_depression_action_slot_is_open`
- `great_depression_active_crisis_is_coherent`

### `docs/plans/035_great_depression_plans/subagent_handoffs/localisation_audit.md`

- Added this audit handoff.

No gameplay, scripted localisation, assets, workbook, shared GUI, shared event-log, achievement, or unrelated localisation file was changed.

## Display and prose before and after

### Vagueness

- `chaosx.nr35.4.d` previously referred to an organized movement surviving a response window and to essential administration.
- It now identifies strike committees and regional councils, the workplaces they control, and the services an emergency government would try to keep operating.
- `chaosx.nr35.5.d` previously used abstract phrases such as local capacity, territorial recovery, and preserving the old map.
- It now states that councils control workplaces and relief offices, then distinguishes negotiated recognition from forced integration.

### Bloat

- `chaosx.nr35.6.d` previously repeated several abstract claims about administrative failure before explaining the available outcomes.
- It now leads with the failed emergency program, identifies the ministries and services losing control, and states the settlement, cabinet, and armed-conflict branches directly.

### Obvious explanation

- `chaosx.nr35.2.a` previously said only `The crisis has arrived.`
- It now directs the player to survey closures and choose a recovery course.
- `great_depression_active_crisis_is_coherent` previously exposed internal validation concepts such as a valid phase, severity, and episode.
- It now states only the player-facing requirement that Great Depression 2.0 remains active in the country.

### Repetition

- No broad repetitive key family was rewritten because several trigger descriptions would require matching script-level tooltip changes to remain precise.
- The remaining repetitive `great_depression_can_*` families are listed under unresolved prose issues.

### Overcomplication

- `great_depression_action_slot_is_open` previously described a response occupying an action slot.
- It now says that no conflicting national response is underway.

### Style-rule repair

- `great_depression_category_desc_national` used vertical bars as pseudo-columns between phase and doctrine and between selected center and objective.
- Those pairs are now ordinary sentences while preserving the same dynamic calls and line count.

## Missing key list

None found in the inspected Event 35 source consumers.

All event title, description, and option keys used by `.1` through `.6` exist.

All inspected decision and mission title/description keys exist.

All six Event 35 achievement names, descriptions, and tooltips exist.

The Event 35 event-name mapping, event-history strings, event-details strings, evolution strings, Negative Economy cluster strings, debug selector, and super-event slot 105 strings exist.

## Duplicate key list

None found in `035_great_depression_l_english.yml`.

No duplicate definition was found for the inspected Event 35-owned keys elsewhere in English localisation.

## Stale or ambiguous key candidates

The seventeen `great_depression_cost_*_tooltip` keys at lines 224 through 272 have no direct non-localisation references in the repository source search.

The decisions use the corresponding custom-cost keys and blocked variants, so these `_tooltip` entries may be stale unless an undocumented engine convention consumes them.

They were not removed because source-only evidence cannot disprove a runtime convention.

## Scripted localisation issues

- Every `[This.GetGreatDepression...]` call in the Event 35 localisation has a matching `defined_text` declaration.
- `GetGreatDepressionEventPicture` is not called from the localisation file, but it is correctly consumed by the Event 35 event script's dynamic picture field.
- The second and third cause selectors can both fall back to `great_depression.causes.none`, while `great_depression_category_desc_national` always prints three comma-separated cause slots.
- A country with fewer than three material causes may therefore see `no additional material cause` repeated twice.
- Fixing that display properly requires changing the scripted-localisation composition or adding combined one-, two-, and three-cause output variants, which is outside this auditor's permitted write scope.
- Source inspection confirms references and fallbacks, but it does not prove which branches the engine resolves at runtime.

## Dynamic localisation added or fixed

The parent follow-up added `GetGreatDepressionOpeningDescription` and its base, inherited, contagion, social-collapse, worldwide, and relapse branches.

All existing variables, formatting codes, actor/state calls, severity values, band/trend/threshold/phase/cause/relapse selectors, doctrine selectors, objective selectors, and event-picture selectors were preserved.

## Remaining dynamic text opportunities

- Collapse the cause list to the number of actual causes instead of printing repeated none fallbacks.
- Where a foreign partner or contagion source is already stored, include its dynamic country name in the opening or relevant response tooltip.

## Cross-surface mismatch notes

- Event 34's event-details and Long Fall text correctly point toward Great Depression 2.0.
- Event 35 `.2` now selects ordinary, inherited, contagion, social-collapse, worldwide, or relapse prose while retaining the full Severity readout.
- Runtime branch selection and wrapping still require consumer-side evidence.
- Financial Contagion, Social Collapse, Second Great Depression, event history, selected event details, and evolution summary strings are aligned at source level.
- The six achievements match the specification's names and intended outcome descriptions at source level.
- The Negative Economy cluster registers Event 35 as a low-danger required member, and the associated cluster strings are present.

## Costs, caps, requirements, and visible trigger text

- Every inspected decision uses a custom cost text family.
- The largest displayed cost families contain four resource types, which meets the decision-surface limit.
- Blocked cost variants exist for the inspected cost families.
- The severity display uses the documented 0 to 100 cap and keeps the value dynamic.
- The `great_depression_can_*` descriptions at lines 488 through 505, 523 through 528, and 577 through 579 repeat the generic formula `The crisis state, available resources, and selected target permit...`.
- These strings do not tell the player which condition failed and should be replaced by requirement-specific custom tooltips in a gameplay-owner pass.
- The `great_depression_can_start_*` descriptions at lines 529 through 576 repeatedly expose national-response and external-response slots.
- Their mechanics are understandable, but their wording remains system-facing and should be replaced with player-facing conflict language when the owning scripted-trigger file can be changed in the same patch.

## Remaining prose-quality issues

### Vagueness

- The generic `great_depression_can_*` permission strings hide the actual resource, target, exposure, or phase requirement.
- The generic `.2` opening does not explain why this particular country entered the crisis.

### Bloat

- No remaining event passage was found to require a safe localisation-only shortening.
- Several long decision descriptions are information-dense because they carry distinct requirements and consequences, and were left intact rather than shortened without script-level proof.

### Obvious explanation

- The unused-looking `great_depression_cost_*_tooltip` family largely repeats the resource names already shown by custom cost text.
- Removal remains uncertain because runtime consumption was not proven.

### Repetition

- The permission and start-trigger families repeat common templates across many actions.
- A shared custom tooltip pattern with action-specific failure details would improve them, but that requires changes outside the permitted localisation-only scope.

### Overcomplication

- The external action-slot tooltip still combines lock exceptions and target rules in one sentence.
- It should be split by requirement in an owning decision-script pass so the player sees only the failed condition.

### Writing-style violations

- The two pseudo-column pipe separators in the category description were repaired.
- No sourced quotation was normalized to satisfy ordinary punctuation rules.

## Sourced quotation and audio preservation

- Preserved the super-event quote verbatim: `The means of exchange are frozen in the currents of trade.` attributed to Franklin D. Roosevelt's 1933 First Inaugural Address.
- The research handoff supports that wording through the Franklin D. Roosevelt Presidential Library and the American Presidency Project.
- Preserved the Keynes fragment `A bad attack of economic pessimism.` as the accepted short quotation variant recorded by the super-event text handoff.
- Preserved the audio wording and attribution for Chopin's Funeral March in C minor, Op. 72 No. 2, performed by Aya Higuchi from the documented CC0 recording.
- No quote punctuation, attribution, title, or audio string was changed.

## Encoding concerns

`035_great_depression_l_english.yml` begins with UTF-8 BOM bytes `EF BB BF` after the patch.

No replacement character was found.

No encoding concern remains in the permitted localisation file.

## MCP evidence and runtime uncertainty

`hoi4.event_inspect` successfully resolved `chaosx.nr35.1` and returned `EVENT_INSPECTED_PARTIAL` for workspace `mod_chaos_redux_ea3b2d67c2c0`, revision `649693da253f0080cfc024f91b7e937cca95387012d11c03ffcf533a05497a8a`.

Useful event lint artifact:

- `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/afd397e2dfedab28532133bd710b3668828e3ffb3a8e1c89da8d42c764d24b48/0d934d95fc8b0c394dae9a8356009ceffe49bb7dcf0fc436b98a0684a0e859c1/event-lint-649693da253f.json`

Useful overview artifacts:

- `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c1631d4c3b0114fb72a630ce05a0d0b04d2f0b9bf4c1463b235446467810f70a/570bebf0ae7b2327ad6fa9f7e1997559367c09d5490988c35de99e576c42bdc7/event-overview-d87f41ae3aab.svg`
- `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c2127d5d18e2e363d0f76f8d99361e980d6c37243861a21aa228efd0253ac75e/aa754bb379669803a6010e662917384b1fee90250c43b836fe79216980fbbc11/event-overview-d87f41ae3aab.png`

Useful option artifacts:

- `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b6c3f7064346ec246304cdd190b9cf473d095bc0eb3cdb5342833dee7e3eba7d/0fa500b736a7962e0d30565eb62ef52e7ffa0c3659f8cac7881a8187773641b3/event-options-d87f41ae3aab.svg`
- `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d2e3728be142d89c771b60aa319642fc59ad5df5b41d20e46ffc885b8b246c54/42fa1d835db543b1597a39b4ceaa808612f777dcbd13ef36f51533df61ee50ca/event-options-d87f41ae3aab.png`

The event inspection was partial because large-workspace helper projections and lifecycle analysis were deferred, and the workspace reported one blocking diagnostic plus 8,690 unresolved nodes outside a selector-clean result.

The `entries` and `unresolved` event-render views did not complete within the bounded audit window and were manually terminated after the overview and options views succeeded.

A refreshed post-change `options` render also failed to return within the bounded audit window and was manually terminated, so the successful options artifact above is pre-patch structural evidence rather than a post-patch localisation render.

No decision/localisation renderer is exposed by the installed package, and Event 35 has no event-owned scripted GUI to inspect through the GUI route.

Therefore the available MCP evidence does not prove final in-game text resolution, category overflow, clipping, or wrapping.

## Meaningful validation

- Re-ran the Event 35 event-title/description/option key scan after the patch.
- Re-ran decision and mission title/description coverage checks against the permitted localisation file.
- Re-ran Event 35 scripted-localisation call-to-definition coverage.
- Re-ran local and repository-level duplicate-key checks for Event 35-owned keys.
- Rechecked that every decision has a custom cost text and that no displayed cost family exceeds four resource types.
- Rechecked the file BOM and replacement-character count after editing.
- Rechecked the changed category string for removed pipe separators and preserved dynamic calls.

## Skipped or unavailable validation

- Hearts of Iron IV was not launched, as required.
- Runtime scripted-localisation branch selection was not tested.
- Production visual wrapping for the ordinary decision category was not available through the installed MCP package.
- Event-render `entries` and `unresolved` views timed out and were terminated.
- The refreshed post-change event-options render also timed out and was terminated.
- No workbook or shared GUI validation was performed because both surfaces were outside the permitted write scope, although their source strings and bridges were inspected read-only.

## Recommended owner fixes

1. The source-aware opening description selector is complete in the parent follow-up above; retain the live branch and wrapping check as an external validation item.
2. Change the cause-list scripted localisation so one or two real causes do not produce repeated `great_depression.causes.none` text.
3. Replace generic `great_depression_can_*` permission strings with requirement-specific custom tooltips in `common/scripted_triggers/035_great_depression_decision_surface_triggers.txt` and matching Event 35 localisation keys.
4. Confirm whether the seventeen `great_depression_cost_*_tooltip` keys are runtime-consumed; remove them only if the engine path is disproven.
5. Obtain consumer-side evidence for category wrapping and dynamic output before declaring runtime localisation complete.

## Parent follow-up

The parent added `GetGreatDepressionOpeningDescription` to the Event 35 scripted-localisation source and split the public report into base, inherited hard-landing, financial-contagion, social-collapse, worldwide-contraction, and relapse descriptions. Each branch retains the Severity value, band, trend, next threshold, phase, causes, relapse state, and worldwide stage.

The source-aware opening is now wired through `chaosx.nr35.2.d` and localized in `localisation/english/035_great_depression_l_english.yml`. Runtime branch selection and production text wrapping remain outside the available MCP route.

## Simplifications, omissions, and blockers

No in-scope source surface was omitted from the audit.

No fallback wording, quotation normalization, gameplay change, or unrelated cleanup was introduced.

The audit remains blocked from an unconditional runtime verdict by the absent decision/localisation visual route, the partial event-tool result, and the timed-out event render views including the post-change refresh.

## Parent follow-up: achievement registry and localisation audit, 2026-09-04

An isolated `chaosx_localisation_auditor` rechecked the Event 34/35 achievement registry, localisation, and GFX aliases after the parent repair. It found that the achievement registry happened clauses were testing proof flag names as undefined triggers, the second Event 35 `unique_id` violated the repository's single root registry contract, the inherited unprefixed GFX names were stale after ID-aligned aliases were added, and two achievement tooltips overstated or understated their proof gates.

The parent moved all seven contracts into `common/achievements/chaos_redux_achievements.txt`, restored the single `unique_id = chaos_redux_achievements`, changed every happened clause to `has_country_flag` over its durable proof receipt, removed the obsolete `common/achievements/035_great_depression_achievements.txt`, removed the three unprefixed Event 34 sprite definitions, and retained only the ID-aligned aliases in `interface/035_great_depression_achievement_aliases.gfx`.

The parent also kept the engine-facing `_NAME`, `_DESC`, and `_tooltip` localisation keys, removed unreferenced lower-case title and description aliases, and aligned Social Peace and Recovery of Nations text with the actual proof conditions. The two touched localisation files retain UTF-8 BOMs.

The final source audit reports one root unique id, seven unique achievement blocks, seven `has_country_flag` proof checks, one title/description/tooltip set per contract, balanced achievement and GFX blocks, and no old unprefixed Event 34 sprite names. The installed HOI4 MCP exposes no custom-achievement inspect or render route, so this remains source-level evidence rather than live engine proof.
