# Event 020 country package and Rat King terminal campaign audit handoff

Date: 2026-08-02

## Scope and source of truth

This pass audits the accepted Event 020 two-tag country package and the Rat King terminal campaign trigger, decision, effect, and target-teardown surfaces.

The identity authority is `docs/specs/020_black_plague_specs/corrections/2026-07-29_two_rat_tags.md`: exactly two runtime country tags are allowed, reusable `RTA` Rat Nation and separate `RTX` Rat King.

The terminal syntax and lifecycle review used `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md`, `paradox_wiki/Effects - Hearts of Iron 4 Wiki.md`, the vanilla `effects_documentation.md`, and vanilla targeted/state-targeted decision precedents.

No 3D model, entity, map write, technology file, spreadsheet, or live game save was changed or created.

This handoff supersedes the stale terminal-lifecycle portions of earlier two-tag country audits while preserving their historical asset and focus findings.

## Outcome

The terminal campaign is country-scoped on RTX and state-targeted through `FROM`; its target controller must be a human-host country at war with RTX, the state must carry the selected-continent marker, and rat-controlled states are excluded.

The parent terminal tranche already separates selection-time cost and flag commitment from expiry-time exposure and terminal-preparation gain, with dedicated success events `.83` and `.84` and cancellation events `.85` and `.86`.

Three narrow lifecycle fixes were applied in the current worktree: selection now cancels when the King identity or completed King core route is absent, a target is already committed, or takeover/world-end begins; teardown clears the unused target-continent selection date; and genuine cancellation reports are gated on the corresponding active campaign flag so defeat teardown cannot emit a false failure report.

No retired `RTB`-`RTM` tag is referenced by the audited terminal files.

## Country package coverage checklist

| Surface | Result | Evidence and remaining risk |
| --- | --- | --- |
| Tag registration | Covered | `common/country_tags/020_black_plague_rat_countries.txt:8-11` registers only `RTA` and `RTX`, both using `common/countries/020_black_plague_rat_country.txt`. No terminal surface introduces another country tag. |
| Country definition and history | Covered with dormant shell | `common/countries/020_black_plague_rat_country.txt:9-11` is the shared graphical shell; `history/countries/RTA - Rat Nation.txt:2-9` and `history/countries/RTX - Rat King.txt:2-9` provide dormant neutral setup with safe `capital = 1` placeholders. Runtime rebinds the capital after a valid state is selected. |
| Spawn, capital, and state control | Covered dynamically | Natural and scenario paths select a valid disease state, transfer it to the intended tag, add a core, and rebind the capital in `common/scripted_effects/020_black_plague_rat_effects.txt:1374-1437` and `:2520-2564`. No map write was performed here. |
| Politics and classification | Covered | RTA and RTX use non-election dormant history; runtime flags `black_plague_rat_country` and `black_plague_rat_king_country` feed the non-human and special-country triggers. |
| Leaders | Partial | RTA creates institutional `The Brood Voice` variants in `common/scripted_effects/020_black_plague_rat_effects.txt:1286-1313`; RTX creates `The Rat King` at `:2472-2478`. The RTX name remains a title rather than an actual-like fictional sovereign name-and-epithet pool. |
| Portraits and flags | Static coverage present | `gfx/flags/{RTA,RTX}.tga`, medium and small variants, and the Event 020 leader portraits are registered by `interface/020_black_plague_rat_identity.gfx`. The animated RTX source-frame package is documented by the asset handoff, while live consumer validation remains parent-owned. |
| Parties and localisation | Covered for current identifiers | `localisation/english/020_black_plague_rat_countries_l_english.yml` covers both country names, adjectives, party names, leader keys, ideas, and rat unit names; focus and decision localisation are in their Event 020 English files. |
| Advisors and high command | Missing by design, unresolved matrix gap | No rat advisors or high-command roles are defined. This requires identity/design work and was not invented in this narrow audit. |
| Ideas and lifecycle | Partial | `common/ideas/020_black_plague_rat_ideas.txt` contains brood, civilian-economy, fractured-instinct, dominion, and King-dominion surfaces. Fractured Instinct reuses an existing icon; route-specific lifecycle and dedicated icon depth remain an asset/design gap. |
| Decisions and terminal campaign | Covered with lifecycle patch | `common/decisions/020_black_plague_rat_decisions.txt:699-888` and the scripted trigger/effect files provide the King selection, harbor, capital, crown, and takeover surfaces. The exact terminal findings and fixes are below. |
| Focus trees | Assigned, audit-owned elsewhere | RTA and RTX load `black_plague_rat_focus_tree` and `black_plague_rat_king_focus_tree` from runtime initialization. Existing focus-icon and route-depth findings remain with the focus auditor. |
| Army and equipment | Covered for scripted non-human forces | Six inactive rat sub-units are defined in `common/units/020_black_plague_rat_units.txt`; locked templates are in `history/units/020_black_plague_rat_1936.txt`; runtime creates divisions without ordinary manpower or equipment requirements. |
| Technology, industry, and supply | Partial but intentional | Both histories use zero research slots and rat ideas suppress ordinary civilian recruitment/production. Captured-knowledge technology and explicit nest-industry progression are not represented as conventional research/building packages. |
| AI and playability | Covered at role-reference level | RTA/RTX-only role templates in `common/ai_templates/020_black_plague_rat_templates.txt` resolve the rat strategy roles; broader live AI timing, balance, and survival remain unrun. |
| Assets and models | 2D package present, no models | Flags, portraits, focus/idea references, and terminal decision icons are textually wired. No bespoke 3D model is required or was produced. |

## File surface checklist

- `common/country_tags/020_black_plague_rat_countries.txt` contains the only two rat tags, `RTA` and `RTX`.
- `common/countries/020_black_plague_rat_country.txt` is the shared definition shell.
- `history/countries/RTA - Rat Nation.txt` and `history/countries/RTX - Rat King.txt` are the two dormant country histories.
- `common/scripted_triggers/020_black_plague_rat_triggers.txt:52-91` contains the terminal country and state predicates.
- `common/decisions/020_black_plague_rat_decisions.txt:699-888` contains the selection, state-targeted campaign, crown, mission, and terminal-takeover decisions.
- `common/scripted_effects/020_black_plague_rat_effects.txt:163-300` contains terminal start, completion, cancellation, exposure, cooldown, and report effects.
- `common/scripted_effects/020_black_plague_evolution_effects.txt:356-407` contains target-continent teardown and state-marker cleanup.
- `events/020_black_death.txt:1137-1169` contains terminal success and failure report events `chaosx.nr20.83` through `chaosx.nr20.86`.
- `localisation/english/020_black_plague_reports_l_english.yml:235-246` contains the terminal success/failure report text and the `.83`/`.84` target-state localisation consumer.
- `common/national_focus/020_black_plague_rat_focus_tree.txt` and `common/national_focus/020_black_plague_rat_king_focus_tree.txt` contain the two assigned trees.
- `common/ideas/020_black_plague_rat_ideas.txt`, `common/units/020_black_plague_rat_units.txt`, `history/units/020_black_plague_rat_1936.txt`, `common/ai_strategy/020_black_plague_rat_ai_strategy.txt`, and `common/ai_templates/020_black_plague_rat_templates.txt` cover the current package mechanics.
- `localisation/english/020_black_plague_rat_countries_l_english.yml`, `localisation/english/020_black_plague_rat_decisions_l_english.yml`, and `localisation/english/020_black_plague_rat_focus_l_english.yml` cover current player-facing keys.
- `interface/020_black_plague_rat_identity.gfx` registers the current Event 020 identity and portrait sprites.

## Map and state setup issues

- Dormant country history uses state `1` only as a valid placeholder; runtime must select a live disease state and rebind the RTA or RTX capital before the country becomes active.
- Natural and scenario spawn paths save a valid state target before creation, transfer the state, add a core, and set the runtime capital; no map rewrite was made in this pass.
- Evolution V candidate viability is data-driven through the existing continent scan and requires the configured state/capital/refuge thresholds; the terminal state trigger additionally requires human-host control, a live war with RTX, exposure eligibility, and no Rat-Controlled phase.
- Seeded capital and refuge node markers are system geography and intentionally survive selected-continent teardown; selected-state, cooldown, and crown markers do not survive it.

## Politics, leader, portrait, flag, advisor, and party issues

- Both tags use dormant neutrality/no-election setup and runtime special-country/non-human flags; no ordinary faction or subject surface is introduced.
- RTA uses institutional `The Brood Voice` names for its collective portraits; RTX uses the title `The Rat King`, leaving the stronger actual-like fictional name/epithet requirement unresolved.
- Normal, medium, and small RTA/RTX flags and current static/animated portrait references are present; rights and live portrait consumer validation remain open.
- No rat advisors or high-command roles exist, which is a broad identity gap rather than a narrow terminal bug.

## Focus, decision, idea, and asset issues

- The RTA and RTX focus trees are runtime-assigned and localised; existing focus-icon and route-depth diagnostics remain with the focus auditor.
- King selection, harbor, capital, crown, mission, and terminal-takeover decisions are present with AI weights; the state-targeted harbor/capital lifecycle and teardown fixes are detailed above.
- Current ideas include Brood Instinct, Civilian Economy suppression, Fractured Instinct, Dominion, and King Dominion; Fractured Instinct reuses an existing icon and route-specific icon depth remains unresolved.
- Event `.83`/`.84` localisation consumes the chain-scoped target-state event target; `.85`/`.86` use generic failure wording and do not need a target pointer.

## Starting military, technology, industry, supply, and production issues

- Rat battalions are inactive, locked, zero-manpower scripted forces with no ordinary equipment requirements; `Rat Shock Brood` now matches its history OOB composition.
- RTA and RTX histories use zero research slots and no conventional production lines; rat ideas intentionally suppress ordinary recruitment/civilian economy behavior.
- The package has explicit rat supply consumption and division-cap tuning, but captured-knowledge technologies and nest-industry buildings are not represented as conventional research/industry surfaces.

## AI and playability issues

- RTA/RTX-only AI template roles resolve the existing rat strategy references for swarm, brutes, burrowers, carrion guard, and dock stowaway forces.
- AI target selection uses the same continent candidate ledger as human selection; terminal state targeting is hostile-state scoped and excludes rat-controlled states.
- Live AI timing, survival, balance, save/reload, and state-target cancellation behavior remain unrun and parent/user-owned.

## Terminal trigger and scope audit

`black_plague_rat_king_terminal_campaign_country_can_continue` is a country trigger that requires `black_plague_rat_country_is_king`, the Evolution V route and completed King route flags, a selected continent, an active war, and neither terminal takeover nor `world_end`.

`black_plague_rat_king_terminal_campaign_country_is_ready` delegates to that continuation trigger and additionally blocks parallel harbor, capital, or shared terminal campaigns through country flags.

`black_plague_rat_king_terminal_campaign_state_is_valid` is a state trigger that requires the selected-continent state marker, an existing controller that is a human-host country at war with `ROOT`, exposure eligibility, and no Rat-Controlled state.

`black_plague_rat_king_terminal_harbor_target_is_valid` adds coastal and naval-base requirements plus harbor cooldown exclusion, while `black_plague_rat_king_terminal_capital_target_is_valid` adds the seeded capital-target marker plus capital cooldown exclusion.

The state-targeted decisions use `target_root_trigger` for RTX country readiness and `target_trigger = { FROM = { ... } }` for the state, matching the vanilla state-targeted decision contract where `ROOT` is the acting country and `FROM` is the target state.

The audited terminal files contain no `RTB`, `RTC`, `RTD`, `RTE`, `RTF`, `RTG`, `RTH`, `RTI`, `RTJ`, `RTK`, `RTL`, or `RTM` references.

## Terminal effect and lifecycle audit

`black_plague_rat_king_start_terminal_harbor_campaign` and `black_plague_rat_king_start_terminal_capital_campaign` run in country scope with `FROM` as the chosen state, subtract the relevant Dominion, Brood Mass, and division-cap costs, refresh the division cap, and set the shared plus route-specific active country flags.

`black_plague_rat_king_complete_terminal_harbor_campaign` and `black_plague_rat_king_complete_terminal_capital_campaign` run on timer expiry, require the continuation trigger, active route flags, and a still-valid `FROM` state, then save the regular chain-scoped `black_plague_terminal_campaign_state` target, apply exposure and route-specific mortality/closure/cooldown effects, grant terminal preparation, clear active flags, dirty the mapmode, and fire `chaosx.nr20.83` or `chaosx.nr20.84`.

When expiry finds an invalid target or route, the completion helpers delegate to the route-specific cancellation helper; `world_end` suppresses the report path and still clears active flags.

`black_plague_rat_king_cancel_terminal_harbor_campaign` and `black_plague_rat_king_cancel_terminal_capital_campaign` now emit `chaosx.nr20.85` or `.86` only when the corresponding active flag was present and neither terminal takeover nor `world_end` is active, then clear both route and shared active flags.

The regular `black_plague_terminal_campaign_state` event target is consumed by the `.83` and `.84` report localisation (`localisation/english/020_black_plague_reports_l_english.yml:236` and `:239`) and is chain-scoped, carrying into the event fired from the completion effect before auto-clearing when that originating chain ends; no global target leak was found.

`black_plague_rat_king_clear_terminal_target_state` clears selected-continent flags, all target/crown counters, the crown end date, the target-continent selection date, per-state target/cooldown markers, and RTX active campaign/crown flags. Seeded static capital/refuge geography markers are intentionally preserved because they are initialized system targets rather than selected-continent progress.

## Changes made

### Changed files

- `common/decisions/020_black_plague_rat_decisions.txt` adds the selection decision `cancel_trigger` at lines `715-723`.
- `common/scripted_effects/020_black_plague_evolution_effects.txt` clears `global.black_plague_rat_king_target_continent_selection_date` at line `393` during `black_plague_rat_king_clear_terminal_target_state`.
- `common/scripted_effects/020_black_plague_rat_effects.txt` gates the harbor and capital cancellation reports on their specific active flags and terminal/world-end guards at lines `223-233` and `296-306`.
- This handoff records the full country package audit and terminal lifecycle evidence.

### Changed identifiers and behavior

- `black_plague_rat_king_select_target_continent`: before defeat/recreation could leave its timer alive with no cancellation trigger; after the patch it cancels when RTX loses the King identity, the completed King core route is absent, a target is already selected, or terminal/world-end state begins, preventing stale `chaosx.nr20.80` selection events while still allowing pre-Evolution-V target selection.
- `global.black_plague_rat_king_target_continent_selection_date`: before teardown left the only-written selection timestamp behind; after the patch the idempotent teardown clears it with the other selected-continent ledger values.
- `black_plague_rat_king_cancel_terminal_harbor_campaign` and `black_plague_rat_king_cancel_terminal_capital_campaign`: before teardown-induced cancellation could emit `.85` or `.86` after active flags had already been cleared; after the patch only genuine active-operation cancellation outside terminal/world-end emits the report.

The current `Rat Shock Brood` runtime template is already aligned with `history/units/020_black_plague_rat_1936.txt`: three `rat_swarm` regiments, three `rat_brutes` regiments, and `rat_tunnelers` support at `common/scripted_effects/020_black_plague_rat_effects.txt:1021-1036` versus `history/units/020_black_plague_rat_1936.txt:22-35`.

## Remaining setup and identity risks

- The RTX sovereign remains titled `The Rat King` rather than an approved actual-like fictional personal name and epithet pool.
- No rat advisors or high-command roles are defined.
- The matrix-level captured-knowledge and nest-industry progression is not represented as conventional technology/building content.
- The two state-targeted terminal decisions rely on daily `cancel_trigger` evaluation after teardown rather than direct `remove_targeted_decision`; they can remain in the UI until the next daily decision refresh, but the false-report path is guarded.
- The crown mission similarly relies on its activation/cancellation triggers after the teardown clears `black_plague_rat_king_crown_continent_active`; no direct mission removal was added because the helper is idempotent and activation is false.
- Live state transfer, AI timing, balance, save/reload, mapmode, report-event, and animation consumer validation remain parent/user-owned.

## Validation performed

- Read-only inspection of the offline decision/effects wiki and vanilla `effects_documentation.md` confirmed `FROM` state scope for state-targeted decisions, `cancel_effect` behavior, and `remove_decision`/`remove_targeted_decision` semantics before the patch.
- `git diff --check` is clean for the touched gameplay and handoff files.
- Targeted searches confirmed no retired RTB-RTM identifiers in the terminal trigger, decision, effect, evolution-effect, or event files.
- Targeted searches confirmed every writer and the absence of readers for `global.black_plague_rat_king_target_continent_selection_date`.
- Static comparison confirmed the runtime and history `Rat Shock Brood` templates have matching regiment and support composition.
- No HOI4 process, live scenario, save, or map write was run.

## Skipped meaningful validation

- No live game or save validation was run because repository instructions assign live consumer checks to the parent and user.
- No Technology Tree Viewer inspection was run because the installed `hoi4-agent-tools` package currently exposes no Technology Tree Viewer; this remains an unresolved limitation.
- No focus render, asset rights review, animation playback, spreadsheet update, or model validation was run because those surfaces are outside this narrow country/terminal audit.

## Parent review and commit boundary

The parent owns final diff review, merge ordering, live validation, and any commit. This handoff does not claim full Event 020 completion; it records the current two-tag country package evidence, the narrow terminal lifecycle patches, and the remaining identity/design gaps.
