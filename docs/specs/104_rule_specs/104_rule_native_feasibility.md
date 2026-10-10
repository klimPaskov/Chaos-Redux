# Event 104 Rule: native feasibility and research evidence

## Finding

This report retains the original planning research cutoff at revision `a3ef485c5da7e2337122eca04ac65c175050f251`.
Its missing local Windows files, unavailable HOI4 routes, empty certified pool, and unexecuted checks describe that session.
Current import facts and reference findings are in [parent import evidence](../../plans/104_rule_plans/104_import_evidence_2026-10-10.json).
Rediscover current capabilities before making a present-tense claim, and preserve the historical research observations below.

The parent's 10 October reference route succeeded.
Installed `effects_documentation.md` lines 7659-7671, revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`, defines `set_rule` as a country permission effect.
Installed `triggers_documentation.md` lines 3977-3990, revision `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29`, defines `has_game_rule` as a reader of selected options.
Offline `Bookmark modding - Hearts of Iron 4 Wiki.md` lines 218-265, revision `fcc082691cfd23a92ba00338c10a8efa552c492f2d524035586bed2c502f31b5`, distinguishes startup, continuous, and hard-coded rule consumers.
The parent's exact-token and heading search found no `set_game_rule` entry in installed effects documentation.
These cited sources establish no global native option writer and preserve the indispensable capability question, without proving engine-wide impossibility.

The specification requires genuine native game-rule option mutation during a running campaign.
This planning task did not establish a supported native writer, a certified base-game option inventory, or runtime persistence and multiplayer proof.
The design is fully developed in the six specification parts, but those implementation prerequisites remain open.
The original planning session's certified runtime pool was empty.

The research establishes a narrower useful fact: the inspected repository contains live script consumers of genuine game-rule options and separate country permission effects.
Those two surfaces cannot be treated as interchangeable.
The presence of `has_game_rule` does not prove that a corresponding runtime setter exists.
A country `set_rule` effect does not by itself change the selected native game-rule option.

The absence of a found writer is bounded evidence.
It is not an assertion that every HOI4 version lacks such a capability.
The installed engine documentation and actual implementation environment must settle that question.
If they show that the capability is unsupported, preserve the user-requested design as blocked and present the exact limitation for a design decision.
Do not silently implement a parallel rulebook, idea modifier, country override, startup replay, or save editor as completion.

## Repository identity

| Item | Evidence |
| --- | --- |
| Repository | [klimPaskov/Chaos-Redux](https://github.com/klimPaskov/Chaos-Redux) |
| Default branch reported by connector | `master` |
| Pinned research revision | [`a3ef485c5da7e2337122eca04ac65c175050f251`](https://github.com/klimPaskov/Chaos-Redux/commit/a3ef485c5da7e2337122eca04ac65c175050f251) |
| Commit date returned | 2026-10-06 |
| Research operations | Read-only repository metadata, directory listing, code search, and targeted file fetches. |
| Implementation operations | None. No branch, commit, PR, gameplay file, workbook, or runtime asset was changed. |

This is a pinned public repository snapshot, not a claim to have inspected the user's potentially newer local working tree.
The latest supplied archive contains guidance and helper contracts that are not all present in this repository snapshot.
Those differences are retained explicitly.

## Primary evidence

| Ref | Source and identity | Read scope and conclusion |
| --- | --- | --- |
| P01 | [Native lend-lease consumers](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/common/scripted_triggers/zz_condemnation_diplomacy_overrides.txt), blob `0d3924c23ec0a0ba19228b85c6ab27278005b134` | Entire file read by parent and architect. Outgoing and incoming gates read `allow_lend_lease` for five named options and preserve bilateral embargo conditions. No writer or canonical default is defined here. |
| P02 | [Compatibility rule definitions](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/common/game_rules/chaosx_game_rules.txt), blob `c956da5fc85d59b7ee7ca60f7c8a7c5d74d4a318` | Parent read the complete 361-line file. Five active AI-behaviour rules have `DEFAULT` blocks and DLC-gated alternatives. Earlier Chaos control examples are commented out. |
| P03 | [Startup repair handoff](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/docs/testing/live_qa/20260913_main_menu_startup/startup_game_rules_handoff.md), blob `0171c8beabd40a6202946ae752634587665d932d` | Entire note read. It explains the five compatibility definitions and explicitly leaves engine confirmation pending. Its reported installed paths are leads for later inspection, not files read in this session. |
| P04 | [Shared firing logic](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/common/scripted_effects/chaosx_logic_effects.txt), blob `d3bf007cd3b6ee792f17c30229ae9e23ca143c92` | Parent read registration lines 210 to 440 and handler lines 1140 to 1210. Architect also read the surrounding 1099 to 1285 lifecycle. Repeatable success updates fired state, cap, weight, pacing, and history before a possible synchronous Random Stuff attempt. |
| P05 | [Shared settings dispatch](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/common/scripted_effects/chaosx_settings_effects.txt), blob `0d281f99a045cc166e4c86b9527fa00bd010490f` | Architect read the relevant preparation and dispatch sections, including 4515 to 4625 and 4780 to 4972. Parent verified 4880 to 4972. The route schedules a root then invokes the type-specific fired handler. A later root failure cannot be assumed to undo already applied accounting. |
| P06 | [History payload support](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/common/scripted_effects/chaosx_events_log_effects.txt), blob `e03346141cab8e650fae5ce801b547cc94e156f7` | Architect read targeted payload and actor sections. Parent verified 520 to 616, including the system-owned history receipt path and global sequence. Payload identity is a viable integration surface, but Rule-specific delivery is unimplemented. |
| P07 | [Country permission precedent](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/common/scripted_effects/007_fury_effects.txt), blob `97c3407bc37d555ccdae067e376219b2d511a756` | Architect read the relevant 1362 to 1370 section. Its `set_rule` example grants country faction-creation permission. It does not demonstrate native game-rule option mutation. |
| P08 | [Settings and evolution gates](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/common/scripted_triggers/chaosx_settings_triggers.txt), blob `cafbb4e77e5b89b1b16d5da7113e97afb318ae78` | Parent read lines 1 to 140. The default-enabled allowlist does not include 104 in this section, and evolution gates separate explicit disable state from threshold evaluation. |

The repository's offline [Bookmark modding reference](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/paradox_wiki/Bookmark%20modding%20-%20Hearts%20of%20Iron%204%20Wiki.md), blob `6c355601bbef82a4e953b4112bd95a24a8db19ea`, was read for its game-rule sections.
It distinguishes startup-only effects, continuing scripted consumers, and hard-coded consumers, and notes that AI random paths can be chosen by startup flags.
This supplied-project reference guides candidate review.
It is secondary to installed engine documentation and is not runtime proof.
No public Paradox wiki page was opened.

## Bounded negative findings

The architect successfully searched the repository's default-branch code index for `set_game_rule`, `set_game_rules`, `set_game_rule_option`, and `change_game_rule` and received no matches.
The decisive searches were retried successfully after some earlier rate-limited requests.
These results cover those tokens in that index at the pinned revision.
They do not cover every possible undocumented writer, every engine version, or an uncommitted local implementation.

The parent inspected the complete `events` directory listing returned at the pinned revision, containing 162 entries.
It had no files numbered 104, 105, 107, or 110, and the literal `chaosx.nr104` code search returned no matches.
The inspected category registration function also omitted 104.
These facts do not establish that every possible dynamically constructed or differently named event root is absent from the entire repository.
They do establish that the package must not present a verified current Event 104 implementation.

The pinned `common/game_rules` directory contained exactly one file, P02.
A fetch of `common/game_rules/00_game_rules.txt` returned 404.
The architect's fetches of `documentation/effects_documentation.md` and `documentation/triggers_documentation.md` also returned 404.
The installed Windows game-documentation locations named in the supplied skills were not present as supplied files in this session.
Their content was not fully read or certified.

The supplied dynamic-effects registry names `common/scripted_effects/chaosx_forced_event_feedback_effects.txt` and `chaosx_report_forced_event_failure`.
The corresponding implementation file returned 404 at both the pinned revision and the default repository reference.
Treat the supplied helper as a documented required contract until a current local implementation is found or the shared owner implements it.
Do not assume it is ready to call because its name appears in documentation.

## Original planning tool availability

The original planning tool registry was checked for HOI4 routes and returned none.
No `hoi4.reference_context`, event inspection, probability, GUI rendering, script validation, save inspection, or engine-execution result was produced.
Absence of exposure is distinct from a failed health check.
No claim is made that an installed HOI4 service was contacted and found unhealthy.

General web searches were attempted for authoritative runtime-rule documentation.
The routine search returned mostly secondary discussions and references.
The stronger official-domain requests returned no usable tool response.
No engine claim in this package relies on those results.
Repository primary evidence and the explicit unresolved gates carry the feasibility conclusion.

The planning task did not launch the game, change player settings, manipulate a save, generate assets, or run a live multiplayer session.
Those actions were not necessary to complete a design package in this environment.
They remain useful future observation scenarios, with user-owned execution separate from agent delivery.
For implementation, consult current installed documentation and offline references, inspect the writer, reader, persistence, and authority contracts, then run representative available checks.
An unavailable optional check is a verification limit.
An unsupported native writer or insufficient meaningful pool remains a genuine missing implementation capability.
Agents must not launch HOI4 or request or await user save/load or multiplayer evidence to deliver reviewed work.

## Blocking proof sequence

| Gate | Required next evidence | Why it blocks admission |
| --- | --- | --- |
| G01: native writer | Exact installed or official engine operation, supported scope, fields, version, and option addressing. | The central mechanic cannot be implemented through an unverified analogous command. |
| G02: exact option inventory | Effective base-game definitions, defaults, complete destinations, load order, DLC conditions, and actual localised names. | Strict non-default selection and revision breadth depend on these facts. |
| G03: current effect | A controlled before-and-after native reader and consumer difference for each admitted transition. | A selected option without a current gameplay effect must not consume a firing. |
| G04: failed-write semantics | Invalid, unchanged, unintended, and unreadable result probes with a known world footprint. | Clean rejection and best effort accounting need a trustworthy distinction between failure and mutation. |
| G05: persistence and authority | Save/reload, released-country, executor-loss, same-day, and multiplayer convergence evidence. | Global persistent changes are an explicit user requirement. |
| G06: breadth | Base-game fixtures supporting the eight-rule maximum and at least four revisable altered rules, or an explicit shortfall decision. | The full four-evolution design must have substantive playable support. |
| G07: dispatch and presentation | Prefire mutation with correct one-occurrence accounting, immutable report payloads, and existing-history rendering. | Successful native changes must not be lost, charged twice, or described by a stale result. |

G01 should be resolved before gameplay integration work begins.
A proof fixture can inspect one base-game diplomatic rule first and then expand to the complete admission inventory.
It must be isolated from successful random-event accounting so a failed experimental writer does not create a misleading ordinary firing.
The fixture is development evidence rather than an alternate shipped event.

If a writer requires a restart, a reload, manual save alteration, or a startup replay for its gameplay effect, it fails the requested immediate mid-campaign mutation contract.
If only a few options work, admit only those proved directed transitions and report the breadth limitation honestly.
If a global state cannot be changed natively at all, the current design remains blocked until the user chooses a different mechanic.

## Source and design dispositions

The full supplied-source reading requirement was completed before this research and specification writing.
The portable source ledger is `104_rule_source_read_ledger.json`.
The separate authority document records all version and numbering conflicts.

The six specification parts are the proposed full design under the current user brief.
The pre-fire best effort architecture is the parent-selected implementation direction following the architect's review.
All scenario results in the validation matrix remain pending unless explicitly identified as source or mathematical review.
No blocker is labelled resolved because the planning documents now describe how to resolve it.
