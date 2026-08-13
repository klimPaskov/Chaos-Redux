# Event 014 focus-tree final re-audit — 2026-07-12

> **Superseded snapshot (2026-07-15).** This historical re-audit predates the
> consolidated focus and asset closure evidence. Its incomplete findings are
> retained for audit history; current status is defined by the consolidated
> Event 014 focus audit and package status.

## Verdict

**Incomplete — the Event 014 focus package is not ready for a completion claim.**

The three live trees are structurally sound, explicitly loaded, fully localised, and covered by 208 distinct focus textures. Their accepted node counts are present: 72 local-warlord focuses, 108 unified focuses, and 28 Wendigo focuses. All focus reward helpers resolve, the ordinary and Wendigo terminal routes require Chaos to be strictly greater than 1000, and no pre-reveal warlord focus text exposes Hannibal or the Wendigo route.

Four completion findings remain:

| Severity | Count | Summary |
|---|---:|---|
| High | 3 | Missing route-aware campaign target scoring; inert/missing Wendigo terminal-hunt decision surface; non-rounded focus tuning without a documented exception |
| Medium | 1 | Wendigo focus progression remains materially shallower than the source specification even though its final lock is genuinely powerful |

This was a read-only gameplay, localisation, and asset audit. No gameplay, localisation, interface, or asset file was edited. This report is the only file created, and no commit was made.

## Authorities and audit scope

The audit used the following repository skills as required guidance:

- `chaos-redux-focus-trees`
- `chaos-redux-events`
- `chaos-redux-decisions-missions`
- `chaos-redux-event-assets`
- `chaos-redux-subagents`

The required offline wiki pages were read before opening the implementation: Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, National focus modding, Interface modding, and Graphical asset modding.

The corresponding current vanilla documentation was consulted from `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation`, including `script_concept_documentation.md`, `effects_documentation.md`, `triggers_documentation.md`, and `modifiers_documentation.md`, together with `common/script_constants/documentation.md`. Vanilla generic, Persian, and strategy-plan focus/AI files were used as structural precedents.

The full Event 014 source package under `docs/specs/014_cannibalism_specs/` was read, including all twelve specification parts, matrices, prompts, research notes, quality reports, and the asset manifest. The previous focus audit, unified and warlord remediation reports, Wendigo implementation/preservation handoffs, asset handoffs, and post-implementation closure addendum were also reviewed before testing the live files.

Live audit surfaces included:

- all three `common/national_focus/014_cannibalism_*_focus.txt` trees;
- all three focus-effect files and their associated triggers, decision effects, script constants, ideas, dynamic modifiers, decisions, and Event 014 AI strategy file;
- the warlord creation, unified creation, Wendigo merge, countdown, terminal lock, and terminal global-war effects;
- `interface/014_cannibalism.gfx` and `interface/014_cannibalism_warlord_focus_assets.gfx`;
- all live focus DDS files and the three focus-asset source packages/contact sheets;
- `localisation/english/014_cannibalism_l_english.yml`.

## Findings

### H-01 — High: the promised route-aware campaign target scoring is not implemented

The source design requires Hannibal to score expansion targets positively for population, weak supply, existing cells, prisons and ports, low stability, adjacency, rail/naval routes, and coalition leadership, while penalising wasteland, unusable nonhuman territory, severe contamination, impossible naval reach, and overextension. It separately requires Wendigo Hannibal to prefer cold/high-population routes before lock and remaining population centres and coalition capitals after lock. See `docs/specs/014_cannibalism_specs/specs/014_cannibalism_spec_part_9_ai_balance_and_integrations.md:224-284` and the campaign-aware focus-AI contract in `014_cannibalism_spec_part_5_focus_tree_architecture.md:560` and `:663-683`.

The live target rules and weights do not implement those dimensions:

- `common/scripted_triggers/014_cannibalism_unified_decision_triggers.txt:521-530` accepts essentially any extant ordinary non-allied, non-subject, non-capitulated country that is not already at war with the Host and has not already been targeted.
- `common/decisions/014_cannibalism_unified_decisions.txt:465-486` weights campaign and ultimatum targets only by whether the Host is already at war. The border incident adds only a major-country factor at `:489-498`, and the coalition-hub operation adds only a major-country factor at `:515-524`.
- The focus-created `cannibalism_unified_dynamic_campaign_scoring_open` flag is set at `common/scripted_effects/014_cannibalism_unified_focus_effects.txt:822`. Its live downstream effects add campaign capacity and `cannibalism_unified_campaign_planning` at `common/scripted_effects/014_cannibalism_unified_decision_effects.txt:259` and `:1178`; the resulting variable is used only as `planning_speed` in `common/dynamic_modifiers/014_cannibalism_unified_decision_modifiers.txt:48`. It is not a target score.
- Nevertheless, `localisation/english/014_cannibalism_l_english.yml:1258-1259` tells the player that borders, population, cells, ports, supply, coalition leadership, empty territory, and reachability are dynamically scored.
- Before lock, `cannibalism_wendigo_focus_prioritize_current_enemies` gives the same conquer value to every current enemy at `common/scripted_effects/014_cannibalism_wendigo_focus_effects.txt:169-178`.
- After lock, `cannibalism_activate_terminal_global_war` correctly opens global conquest, but it gives the same conquer, antagonise, and front-request weights to every surviving country at `common/scripted_effects/014_cannibalism_super_event_effects.txt:142-177`. It does not distinguish population centres or coalition capitals.

This is not a claim that Event 014 has no AI. Every focus has an `ai_will_do` block; all selectable unified decisions do as well; the Wendigo AI protects, feeds, and stabilises anchors; and the terminal effect does launch global war. The defect is the absent target differentiation that the source specification and player-facing focus text explicitly promise.

Required resolution:

1. Add a reusable target-scoring contract that evaluates the specified positive and negative factors in the target scope.
2. Use that contract in the unified cell/campaign/ultimatum/border/counterwar decision weights and in Wendigo pre-lock and post-lock target priorities.
3. Ensure impossible or unusable targets are excluded or weighted to zero rather than merely receiving a small penalty.
4. Re-audit the focus description and tooltip against the implemented score dimensions.

### H-02 — High: the Wendigo terminal-hunt unlock is inert and its advertised decisions do not exist

`cannibalism_wendigo_focus_hunt_every_remaining_capital` and `cannibalism_wendigo_focus_the_world_beneath_winter` set `cannibalism_wendigo_terminal_hunt_open` at `common/scripted_effects/014_cannibalism_wendigo_focus_effects.txt:436-450`.

A repository-wide consumer scan found only three references to the flag:

- two `set_country_flag` calls at focus-effect lines 437 and 450;
- one cleanup `clr_country_flag` call when the route is broken at `common/scripted_effects/014_cannibalism_wendigo_decision_effects.txt:544`.

No trigger, category, decision, AI block, scripted effect, or GUI reads the flag. The complete live Wendigo decision surface contains seven command actions and four counterwar actions in `common/decisions/014_cannibalism_wendigo_decisions.txt:9-238`; none is a terminal-hunt action and none is gated by `cannibalism_wendigo_terminal_hunt_open`.

The missing surface is player-facing, not merely an internal naming concern:

- `localisation/english/014_cannibalism_l_english.yml:1366-1367` says that `Hunt Every Remaining Capital` opens terminal-hunt decisions.
- `localisation/english/014_cannibalism_l_english.yml:1369-1370` says the final focus keeps that terminal hunt active.

The focuses still grant War Support, research, authority, anchor strength, Command Power, and broad AI conquest pressure, so neither focus is wholly inert. The decision unlock promised by the flag and tooltip is inert.

Required resolution: implement a paid, target-aware terminal-hunt decision family with availability, costs, failure/counterplay, AI, and cleanup keyed to this flag. If the intended design is to have no such decisions, changing the source contract and player-facing text is a design decision that requires explicit user approval; silently treating broad conquer weights as the advertised decision family is not an acceptable fallback.

### H-03 — High: warlord and Wendigo focus reward tuning still violates the required round-value standard

The required focus skill says authored gameplay tuning should use round multiples of five and specifically rejects unexplained values such as 2, 3, 7, 12, and 18. See `.agents/skills/chaos-redux-focus-trees/SKILL.md:511` and its completion checks at `:858-859` and `:882-883`.

The live warlord focus constants still contain extensive unexplained authored percentages and values outside that standard, including:

- 12% burden attack/organisation at `common/script_constants/014_cannibalism_warlord_focus_constants.txt:25-28`;
- 12% council planning at `:48`;
- 12% speed, 18% organisation regain, and 8% defence for the confederacy at `:53-56`;
- 18% regain and 12% attack for rapid consumption at `:60-61`;
- 12% mobile speed and discipline regain at `:71` and `:79`;
- 12% organisation, 4% reinforcement, and -12% supply use for alignment at `:83-86`;
- 12% political power/efficiency and 6% speed for manipulation at `:91-93`;
- 18% attack, 12% organisation, and -8% political power for defiance at `:95-99`;
- 3%/8%/12% recruitment experience and 3/7-day cooldown changes at `:108-114`.

The Wendigo focus constants also use authority gains of 1/2/3, Frenzy +4, stability +2%/+4%, War Support +3%, and pack capacity +2/+4 at `common/script_constants/014_cannibalism_wendigo_focus_constants.txt:15-29`.

No engine constraint, formula-derived reason, or specific design exception is documented for these values. The old focus audit identified the same issue, and no remediation handoff records its acceptance or resolution.

Required resolution: normalise the authored values to legible increments of five and rebalance the affected routes, or document a concrete formula/engine exception for each deliberately non-rounded family. A generic statement that the values are balanced is not the documented reason required by the skill.

### M-01 — Medium: the Wendigo focus progression remains shallower than the specified route architecture

The source requires the Wendigo overlay to deliver cold and supply warfare, enemy attrition, additional and improved supernatural formations, population and enemy-death recruitment, preserved and deepened cannibal systems, supernatural origin variants, anchor counterplay, and a categorically stronger alternate terminal route. See `docs/specs/014_cannibalism_specs/specs/014_cannibalism_spec_part_5_focus_tree_architecture.md:608-661`. Its reward standard says important focuses should be driven by units/templates, decision and mission families, map work, mechanic changes, war goals, network actions, and staged ideas; small modifiers may support those rewards but may not be their main point (`:685-701`).

The live implementation has genuine strong systems:

- the winter-stage idea supplies attack, defence, speed, recovery, supply, winter attrition, and cold acclimatisation at `common/ideas/014_cannibalism_wendigo_ideas.txt:27-38`;
- the frozen-corridor decision applies friendly logistics and adjacent hostile disruption at `common/scripted_effects/014_cannibalism_wendigo_decision_effects.txt:266-294`;
- paid Pack training removes exact population through the Deaths pipeline, adds only the resulting manpower, and creates zero-start formations at `:135-188`;
- anchors, countdown acceleration/stabilisation, pre-lock counterplay, and the terminal pulse are live;
- the locked idea is deliberately overwhelming at `common/ideas/014_cannibalism_wendigo_ideas.txt:42-65`, and the lock launches global war at `common/scripted_effects/014_cannibalism_wendigo_effects.txt:673-695`.

The focus progression leading to those systems is much thinner than the source contract:

- many helpers consist mainly of authority +1/+2/+3, Frenzy +4, 2-4% stability/War Support, Command/Political Power, or repeated one-use 50% research bonuses; representative helpers are at `common/scripted_effects/014_cannibalism_wendigo_focus_effects.txt:185-223`, `:235-270`, `:331-380`, and `:391-415`;
- `Keep the Foreign Cells` adds Political Power, authority, and an electronics research bonus at `:349-359`, but does not deepen cell operations;
- `Retain the Warlord Captains` is Command Power, Political Power, and War Support at `:343-347`, without a commander or command-system action;
- winter victories are deduplicated and counted toward countdown progress at `common/scripted_effects/014_cannibalism_wendigo_effects.txt:309-332`, but they are not converted into recruitment as specified;
- no focus reward upgrades inherited origin specialists into supernatural variants;
- the terminal-hunt unlock is missing as described in H-02.

This is Medium rather than High because the overlay preserves the original ZZZ country, contains real population-backed recruitment and anchor counterplay, and reaches a materially overpowered final lock. The remaining gap is the depth and variety of the route progression, not the existence of the alternate terminal system.

Required resolution: replace the generic middle-route rewards with a bounded set of additional paid operations, staged formation/commander upgrades, enemy-death recruitment receipts, inherited cell/origin interactions, and target-aware winter/terminal actions. Preserve the existing exact population accounting, Pack template lock, anchor counterplay, and pulse-only terminal lock.

## Route coverage proof

### Local warlord tree

The live file contains 72 focuses, exactly the upper end of the specified 60-72 range.

| Route group | Nodes | Result |
|---|---:|---|
| Survival trunk | 6 | Pass; establishes paid recruitment, emergency recovery, Larder inventory, workshops, recovery, and accounting |
| Personal tyranny / feast council / pack confederacy | 12 | Pass structurally; three mutually exclusive four-focus hierarchy routes with live operating-order effects |
| Larder economy and method choice | 11 | Pass; shared trunk plus three mutually exclusive method routes with decision/cost consumers |
| Military discipline and final doctrine | 9 | Pass; converges hierarchy and Larder progress into live recruitment and operating-order effects |
| Four origin overlays | 16 | Pass; Island, Siege, March, and Prison each have four gated focuses and origin-specific operations |
| Regional expansion, terror, and infiltration | 8 | Pass; live network, target, raid, and regional-command effects |
| Evolution II alignment / manipulation / defiance | 10 | Pass structurally; one gated entry plus three mutually exclusive three-focus endgame routes |

Each origin root has its own `allow_branch` flag gate at `common/national_focus/014_cannibalism_warlord_focus.txt:811-817`, `:894-900`, `:977-983`, and `:1060-1066`. Evolution II is hidden unless the evolution is active at `:1303-1313`.

### Unified tree

The live file contains 108 focuses, inside the specified 96-120 range and at the exact expected count.

| Route group | Nodes | Result |
|---|---:|---|
| Opening convergence | 8 | Pass |
| Three warlord-disposition routes | 15 | Pass |
| Three supreme-hierarchy routes | 15 | Pass |
| Continental Larder trunk and four methods | 23 | Pass |
| Army integration and terminal army | 14 | Pass |
| Navy | 8 | Pass |
| Air | 7 | Pass; the root has a real capability gate and zero AI weight when invalid at `common/national_focus/014_cannibalism_unified_focus.txt:1085-1100` |
| Intelligence and cells | 8 | Pass mechanically; target scoring remains H-01 |
| Continental expansion | 4 | Pass mechanically; target scoring remains H-01 |
| World-hostility counterwar | 4 | Pass mechanically; target scoring remains H-01 |
| Ordinary terminal | 2 | Pass; strict readiness and Chaos gates |

### Wendigo overlay

The live file contains 28 focuses, inside the specified 24-32 range.

| Route group | Nodes | Result |
|---|---:|---|
| Merge trunk | 5 | Pass structurally; preserves the live ZZZ country and establishes the conjoined systems |
| Winter hunger | 5 | Pass mechanically, with the depth reservation in M-01 |
| Wendigo recruitment | 5 | Pass for population-backed Pack training and capacity; enemy-death recruitment remains missing |
| Cannibal legacy | 5 | Partial; inherited systems survive, but several focus rewards do not deepen them |
| Transformation countdown | 5 | Pass; real anchors, acceleration, stabilisation, and route proof |
| Alternate terminal | 3 | Partial; lock path is real, terminal-hunt decision unlock is not |

## Structural and reward validation

| Check | Warlord | Unified | Wendigo |
|---|---:|---:|---:|
| Unique focus IDs | 72/72 | 108/108 | 28/28 |
| Expected graph roots | 1 | 1 | 1 |
| `ai_will_do` coverage | 72/72 | 108/108 | 28/28 |
| Custom tooltip coverage | 72/72 | 108/108 | 28/28 |
| Focus-specific reward helper calls | 72/72 | 108/108 | 28/28 |
| Missing reward-helper definitions | 0 | 0 | 0 |
| Missing prerequisite/mutual-exclusion references | 0 | 0 | 0 |
| Cycles | 0 | 0 | 0 |
| Duplicate coordinates | 0 | 0 | 0 |
| Asymmetric mutual exclusions | 0 | 0 | 0 |

No focus ID is duplicated across the three files. Separate prerequisite blocks were evaluated as cumulative requirements, while multiple focus references inside a single prerequisite block were evaluated as alternatives. The important multi-branch junctions use the intended structure: the unified final mobilisation has four separate required capstones at `common/national_focus/014_cannibalism_unified_focus.txt:1387-1399`, and the Wendigo countdown has five separate branch requirements before the terminal chain.

Focus cadence is explicit and centralised in each focus file:

- warlord: 47 short and 25 normal focuses at 35/70 days;
- unified: 74 short, 25 normal, and 9 terminal focuses at 21/35/56 days;
- Wendigo: 7 short, 18 normal, and 3 terminal focuses at 35/70/105 days.

The focus-state consumer scan found:

- 88 unique country flags set by warlord focus helpers, with no flag lacking a non-set/clear use;
- 219 unique country flags set by unified focus helpers, with no flag lacking a non-set/clear use;
- 8 unique country flags set by Wendigo focus helpers, with one unresolved consumer: `cannibalism_wendigo_terminal_hunt_open` from H-02.

The unified 219 include the 208 operational-domain flags plus final/package state. Their profile variables feed costs, durations, modifiers, mission progress, target effects, and terminal proof; they are not merely counted as focus completions.

## Decision and AI proof

| Surface | Selectable actions | AI coverage | Additional proof |
|---|---:|---:|---|
| Warlord | 16 | 16/16 | Four self-removing origin AI profiles plus one common profile in `common/ai_strategy/014_cannibalism_warlords.txt:10-68`; route/personality focus weights are present |
| Unified | 35, plus 4 automatically activated missions | 35/35 selectable actions | Command, Larder, army, navy, air, cell, campaign, integration, counterwar, and terminal budgets are live; campaign target differentiation remains H-01 |
| Wendigo | 11 | 11/11 | Anchor protection, population-backed Pack training, corridor freezing, acceleration, stabilisation, and counterwar AI are live; terminal target differentiation remains H-01 |

The four unified maintained missions are activated and progressed by their owning operations; they are not human-only buttons and therefore do not require selection weights.

Recruitment effects were checked in context. Warlord, unified, and Wendigo scripted recruitment uses real controlled-state population through the common Deaths-backed consumption transaction. Created formations begin with zero manpower and zero equipment and depend on paid population, Larder, and equipment contracts. No focus directly grants a free unit, free population, or a hidden equipment stockpile.

## Tree loading, secrecy, and terminal proof

All three trees are explicitly loaded with `keep_completed = no`:

- warlord creation: `common/scripted_effects/014_cannibalism_country_effects.txt:724-742`;
- unified creation: `common/scripted_effects/014_cannibalism_unification_effects.txt:508-520`;
- Wendigo merge: loader definition at `common/scripted_effects/014_cannibalism_wendigo_focus_effects.txt:15-27`, called by the surviving ZZZ host at `common/scripted_effects/014_cannibalism_wendigo_effects.txt:469-480`.

No generic focus-tree fallback is used.

Reveal ordering is correct. The ordinary route sets `cannibalism_reveal_complete` before CBL, its leader, portrait, tree, or player tag transfer at `common/scripted_effects/014_cannibalism_unification_effects.txt:491-519`. The Wendigo route sets the same public reveal flag before transforming the live host and loading its overlay at `common/scripted_effects/014_cannibalism_wendigo_effects.txt:439-480`.

The local-warlord focus title, description, and tooltip block at `localisation/english/014_cannibalism_l_english.yml:685-906` contains no Hannibal, Lecter, Wendigo, Carthage, or Barca disclosure. The three tree roots also have identity/reveal `allow_branch` gates.

`constant:cannibalism_evolution_threshold.world_end_chaos` is 1000 at `common/script_constants/014_cannibalism_core_constants.txt:708`. Both terminal families use a strict greater-than comparison:

- ordinary readiness: `common/scripted_triggers/014_cannibalism_triggers.txt:852-879`, with explicit checks repeated on both terminal focuses at `common/national_focus/014_cannibalism_unified_focus.txt:1397-1419`;
- Wendigo countdown readiness: `common/scripted_triggers/014_cannibalism_wendigo_triggers.txt:101-147`, consumed by the terminal focuses at `common/national_focus/014_cannibalism_wendigo_focus.txt:588-660`.

The unified capstone cannot complete from focus history alone: Larder, army, expansion, and counterwar package triggers require paid-operation proof, and final mobilisation additionally requires the exact population levy. The Wendigo focus does not set world-end directly; the transformation pulse alone calls the final lock at `common/scripted_effects/014_cannibalism_wendigo_effects.txt:673-725`, preserving pre-lock anchor counterplay.

## Focus-icon and localisation proof

The focus asset audit found:

- 208 focus IDs and 416 corresponding base/shine sprite definitions;
- 208 distinct texture paths;
- zero missing sprite definitions, shine definitions, or DDS files;
- every shine sprite uses `gfx/FX/buttonstate.lua`;
- every DDS decodes at 94 by 86 pixels;
- 208 distinct binary SHA-256 hashes and 208 distinct normalised RGBA hashes;
- no audited sprite-name collision elsewhere in `interface/`.

Coverage by surface is 72/72 warlord, 108/108 unified, and 28/28 Wendigo. The unified and Wendigo ranges are registered in `interface/014_cannibalism.gfx:224-439` and `:463-518`; the warlord family is registered in `interface/014_cannibalism_warlord_focus_assets.gfx`. Source, processed, and live DDS inventories match their focus ID sets. The three decoded DDS contact sheets were visually inspected; they show route-specific artwork rather than a generic/default focus icon or one resized fallback reused across the trees.

The focus-localisation audit found:

- UTF-8 BOM present;
- 624/624 required focus keys present: title, description, and tooltip for all 208 focuses;
- zero duplicate focus-localisation keys;
- all three tree-name keys present (`The Regional Host`, `The Continental Host`, and `The Winter Host`);
- no forbidden pre-reveal identity term in warlord focus text.

Thirty-one ideas and dynamic-idea surfaces reached by the focus package were also checked for localisation, sprite registration, and live texture presence; no missing presentation item was found. The remaining localisation failures are semantic rather than structural: the false dynamic-scoring promise in H-01 and the false terminal-hunt decision promise in H-02.

## Idea lifecycle and simultaneous-spirit ceiling

- A warlord begins with Closed Muster Rolls, one origin idea, and one consolidated survival-burden idea. The hierarchy capstone replaces the burden with one dynamic Host Operating Order, so the route remains at three focus-package spirits.
- Unified disposition, hierarchy, and Larder ideas clear their own route families before adding the chosen replacement. The opening command burden is removed before the three route-idea families accumulate. The maximum is three focus-created route spirits.
- The Wendigo conjoined, winter-network, and locked transformation ideas replace one another at `common/scripted_effects/014_cannibalism_wendigo_effects.txt:606-617` and `:673-690`; they do not stack as three separate transformation stages.

No route exceeds the required maximum of three simultaneously active focus-created national spirits.

## Completion checklist

| Requirement | Result |
|---|---|
| Warlord tree within 60-72 | Pass — 72 |
| Unified tree within 96-120 / expected 108 | Pass — 108 |
| Wendigo overlay within 24-32 | Pass — 28 |
| Baseline, hierarchy/Larder/military, four origins, and three Evolution II routes | Pass structurally and mechanically |
| Unified governance, Larder, army, navy, air, cell, expansion, counterwar, and terminal routes | Pass except target-scoring AI |
| Wendigo winter, recruitment, legacy, countdown, and terminal routes | Partial — M-01 and H-02 |
| Valid prerequisites and mutual exclusions | Pass |
| Real reward helpers and downstream consumers | Pass except `cannibalism_wendigo_terminal_hunt_open` |
| Route-aware AI | Fail — H-01 |
| Strict Chaos greater than 1000 terminal gates | Pass |
| Reveal secrecy | Pass |
| Unique focus icon coverage | Pass — 208/208 |
| Focus localisation coverage | Pass structurally; two semantic promises fail |
| Round authored reward tuning or documented exceptions | Fail — H-03 |
| No generic/default/fallback tree or focus art | Pass |

## Meaningful validation scenarios

1. **Origin route isolation:** each CBA-CBH warlord sees only the matching four-focus origin overlay, receives the matching operation consumers, and cannot complete a second origin overlay. Static result: pass.
2. **Evolution II route isolation:** alignment, manipulation, and defiance remain hidden before Evolution II and are mutually exclusive after the shared entry. Static result: pass.
3. **Unified terminal proof:** completing the four focus capstones without their paid Larder/army/campaign/cell/integration/counterwar receipts leaves terminal readiness closed; strict Chaos greater than 1000 and the final population levy remain required. Static result: pass.
4. **Air-route validity:** a unified host without airbase, experience, or airframes gives the air root zero AI weight, while the paid foundation project provides a non-free path to eligibility. Static result: pass.
5. **Wendigo counterplay:** a live original-ZZZ merge retains the country and Pack contract; the overlay loads only after reveal; anchors can be attacked before lock; the focus route cannot set world-end; the pulse locks only after full progress. Static result: pass.
6. **Unified target preference:** two otherwise valid targets differ only in population, cells, ports, supply, contamination, and reachability. The live AI assigns no score difference for those dimensions. Static result: fail, H-01.
7. **Wendigo terminal hunt:** finishing `ZZZ_wendigo_hunt_every_remaining_capital` sets its flag, but no new decision becomes visible because nothing reads the flag. Static result: fail, H-02.
8. **Asset identity:** every focus sprite resolves to a distinct 94-by-86 DDS; binary and decoded-pixel comparisons find no duplicate image, and contact-sheet inspection finds no default/generic fallback. Static result: pass.

## Simplifications, omissions, and blockers

No audit step was intentionally simplified, and no fallback was accepted. The source-level audit covered every requested live focus, helper, trigger, constant, idea, decision, AI, interface, localisation, and source-package surface.

Completion is blocked by H-01, H-02, H-03, and M-01. The three trees should not be described as fully complete until those findings are implemented or an explicit user-approved design change supersedes the affected source promises.

This audit did not mutate or commit the shared dirty worktree. It added only this handoff report.

## Skills used

- `chaos-redux-focus-trees`
- `chaos-redux-events`
- `chaos-redux-decisions-missions`
- `chaos-redux-event-assets`
- `chaos-redux-subagents`

No skill was created or updated during this bounded audit.
