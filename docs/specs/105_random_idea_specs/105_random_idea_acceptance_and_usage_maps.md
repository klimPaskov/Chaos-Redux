# Event 105 acceptance criteria and usage maps

## Evidence status

The completed-source reading and abstract calculation claims below describe the historical 9 October 2026 planning session.
Current import findings and source/catalog evidence are linked from [README](README.md#current-import-review-10-october-2026).
The current import did not rerun those calculations or execute native scenarios.

These are implementation acceptance scenarios and work assignments.
They are not a report that the engine scenarios have run.
This session completed full supplied-source reading, targeted pinned repository research, abstract count mathematics, and the design reviews recorded in the review-disposition file.
No HOI4 MCP route or installed game runtime was exposed in that historical session.

The abstract probability review checked 34,025 exact-rational count-distribution comparisons and proved the accepted monotonic ordering under its declared uniform-integer model.
That calculation does not validate the engine RNG, the loaded candidate universe, callback effects, campaign balance, or save behavior.

## Pool and native capability scenarios

| Scenario | Fixture and required observation | Pass condition |
| --- | --- | --- |
| e105_native_discovery | Installed engine documentation, complete native candidate output if available, and resolved effective source inventory | Every real loaded national-idea identity appears once, including never-owned and inactive event ideas, with documented scope and element type |
| e105_external_mod_addition | Add a valid national spirit through a small additional active mod that Event 105 has never named | Native discovery finds it directly, or the complete loadout generator finds it automatically when rebuilt |
| e105_loaded_dlc | Compare actual definition loading with and without relevant DLC content and purchase-gated UI conditions | Loaded technically addable ideas remain eligible even when their ordinary UI availability is false |
| e105_hidden_empty | A hidden spirit, an empty country spirit, and a real empty hidden carrier | All technically addable national ideas stay eligible and can dispatch, without a usefulness or icon filter |
| e105_foreign_conditions | Country-, ideology-, path-, and mechanic-specific spirits whose usual selection conditions are false for the recipient | Direct native addability determines inclusion, and thematic mismatch never causes rejection |
| e105_effect_suppressed | A technically addable national idea whose do_effect or equivalent normal modifier condition is false | It remains eligible, consumes one valid dispatch, and may remain held without useful modifiers |
| e105_type_boundary | An ordinary spirit, a custom national category, a law, a modern advisor character, a character-slot dummy, and a dynamic modifier | Membership follows verified effective national-idea type, without identifier-prefix guesses |
| e105_overlay_winner | Same-path overrides, different-file duplicate IDs, dependencies, replace_path, filename order, and supported case variants | Registry winner and category agree with the actual native loaded definition |
| e105_unknown_category | A mod-defined idea category whose native classification is not yet known | Resolve it or mark universe readiness unresolved, never silently omit it from a claimed complete pool |
| e105_reserved_entry | Any claimed default or reserved engine entry | Exclusion has registration and native-invalidity proof, and no real first entry is dropped |
| e105_stale_registry | Change an effective source, descriptor order, category, or relevant mount without regenerating | Preparation detects the mismatch where detection is actually supported, and no known stale subset is advertised as complete |

The native-discovery scenario can conclude that no supported complete iterator is available in the installed build.
That is a valid research result and selects the complete generated route, not a waiver of pool coverage.

## Counts, countries, and selection

| Scenario | Required inputs | Expected result |
| --- | --- | --- |
| e105_baseline | Valid countries, sufficient fresh pool, C below 200 | One independent direct identity per country |
| e105_fixed_boundaries | C = 199, 200, 399, 400, 599, and 600 | Requested counts are 1, 2, 2, 3, 3, and uniform 4–6 respectively |
| e105_storm_boundary | Matched B and pool at C = 799 and 800 | Storm never has a weaker requested-count distribution than Collision |
| e105_counts_grid_p24 | C = 800, 1000, 1200, 1600 with B = 0, 6, 12, 24, 48, 96 | Exact ranges match part 2, with correct inclusive endpoints and uniform integer shares |
| e105_burden_thresholds | Every S from 8 through 16, with B just below, at, and above the floor threshold | Center floor begins at ceil(24×S/5)−24, with no off-by-one count error |
| e105_evolution_history | First firing at Storm, repeated Storm, all-recipient exhaustion, then a real lower-stage firing | One first-use record for each actually dispatched frozen stage even if a later dispatch fails or settings change, no invented lower stages, no repeat evolution rows, and no effect on future count selection |
| e105_large_chaos | C beyond 1600 and representative B | One bundle remains at most 16, while the complete universe is not capped |
| e105_country_rng | Two identical countries and then two with different held sets, under a declared deterministic fixture | Separate advancing draws per recipient, cross-country duplicate identities permitted, no common-seed reset |
| e105_valid_country_roster | AI, human, subject, war, peace, capitulated, exile, unusual existing tag, dead tag, uncreated tag | Every usable existing country scope participates, and invalid scopes do not receive redirected grants |
| e105_global_snapshots | An early recipient's callback changes a later recipient's ownership, Chaos, or evolution settings | Later requested count still uses original C, B, and effective stage, while its actual fresh eligibility reflects current ownership |
| e105_without_replacement | A stable five-identity pool, several held sets, requested counts up to five | Each eligible identity has equal conditional selection share and appears at most once per bundle |
| e105_same_name | Different IDs with the same display name or icon, plus duplicate source occurrences of one ID | Different effective IDs remain distinct, while repeated source occurrences do not add weight |
| e105_uneven_files | Files or registry segments with unequal eligible counts | Every idea identity has equal probability rather than each file receiving equal probability |
| e105_pool_exhaustion | Fresh pool sizes 0, 1, 2, 3, 4, 7, and 16 | Grant at most the genuinely available fresh identities, with no duplicate filler or false retry exhaustion |
| e105_over_1000 | More than 1,000 eligible identities, including sentinel fixtures near the beginning, middle, and end | No suffix loss or loop-ceiling truncation, with equal participation of all real entries |

Statistical samples are useful for detecting distribution defects, but they cannot prove completeness by themselves.
Compare candidate inventories and selector structure as well as any sampled frequencies.
When callbacks alter eligibility, classify exact probabilities only for the transitions the scenario actually declares.
Do not label final retained outcomes uniform merely because the identity selector is uniform.

## Callbacks, persistence, and repeatability

| Scenario | Required observation | Pass condition |
| --- | --- | --- |
| e105_preowned | Recipient already owns the selected exact identity before dispatch | No native add or timer refresh for that identity, and the draw searches the remaining set |
| e105_self_remove | on_add or normal cancellation removes the selected identity | One dispatch, no retry, no compensating grant, and retained absence recorded separately |
| e105_swap | Native addition replaces an old family member or transforms itself | Native replacement survives, no family filter, no cloned permanent wrapper |
| e105_grant_next | A callback grants a candidate that has not yet been directly drawn | Recheck ownership and avoid a fresh direct add to the now-held identity |
| e105_remove_preowned | A callback removes an initially held identity | It can become eligible later if unattempted, under the specified current-ownership selector |
| e105_remove_prior_draw | A callback removes a result already dispatched in this bundle | That identity stays excluded from the remainder of the bundle |
| e105_reentry | Callback synchronously re-enters the same slot, same firing, and a separate request | Once-only own receipts, no recursive world grant, immutable outer context, and honest separate-request handling |
| e105_country_recreation | A captured country is destroyed and an unrelated new country appears under the same tag before its turn | Old scope receipts and reserved work do not attach to the new country merely through matching tag text |
| e105_country_loss | Recipient dies, changes scope, or creates another country during resolution | Remaining work stays with valid captured recipients, newly created countries wait for later firings |
| e105_repeated_event | Fire twice legitimately with unchanged first results, then after native removal | Held exact identities do not repeat, removed identities may return in a later firing |
| e105_no_cleanup_removal | Close report, disable future firings, lower Chaos, or end a cluster batch | Existing native ideas remain unless their own normal lifecycle removes them |
| e105_save_same_loadout | Save and reload before and after settlement | Stable receipt and burden identity, no replayed native dispatch or repeated Chaos credit |
| e105_save_reordered_registry | Reorder generated entries without changing semantic idea keys | Each historical identity still refers to the same idea |
| e105_save_removed_readded | Remove an idea definition, preserve its historical receipt, then restore the exact key | No numeric aliasing, no burden while absent, and correct exact-key history when restored |
| e105_native_inheritance | Native civil war, release, annexation, and proven country-continuity cases | Native ideas follow their own behavior, while direct history is neither invented nor copied to unrelated new scopes |
| e105_report_context | Queue two firing reports before acknowledging the first | Each report displays its own country, firing, and saved settlement retention, later ownership does not rewrite it, and neither acknowledgement grants again |

Arbitrary selected callbacks can execute other systems and consume randomness.
Their effects remain part of the selected idea's ordinary behavior.
The acceptance target is correct Event 105 dispatch and truthful evidence, not a guarantee that every third-party callback was designed for every recipient.

## Chaos feedback and achievement scenarios

| Scenario | Fixture | Expected result |
| --- | --- | --- |
| e105_chaos_baseline | Ten recipients retain one fresh direct identity each | +2 Chaos once |
| e105_chaos_triple | Ten recipients retain three each | +6 Chaos once |
| e105_chaos_cap | Ten recipients retain at least ten each | +20 Chaos once |
| e105_chaos_partial | Ten recipients, only one retains one | +1 Chaos once |
| e105_chaos_zero | No recipients, genuine empty pool, or no retained direct identity | Zero Event 105 Chaos |
| e105_chaos_idempotence | Re-enter settlement, reload a settled result, reopen a report, or refresh history | No second award |
| e105_chaos_stage_only | Cross an evolution threshold or change an evolution setting without a new firing | Zero direct Event 105 Chaos |
| e105_chaos_other_owner | A selected idea causes a war or another separately tracked outcome | That system uses its own ordinary source, without an extra Event 105 consequence premium |
| e105_victory_limits | Military achievement with burden 5/6, participation below/at/above 25%, and day 729/730/731 | Exact inclusive requirements and deadline, correct enemy and war identity, no ally's victory credited to the player |
| e105_victory_multiwar | Several qualifying wars, equal enemy factory counts, and any supported same-enemy/multiple-war case | Deterministic pair selection by the specified factory/country/war ordering and immutable enemy plus war identities |
| e105_victory_disqualification | Subject status, player capitulation, country switch, qualifying major ally joining or being promoted, a war merge introducing one, or target war ending without victory | Attempt ends correctly and later reattempt requires a new legitimate enrolment |
| e105_prosperity_limits | Initial factories 20/21, several F0 values, day 364/365/730/731, stability just below/at 70% | Exact start gate, ceil arithmetic, observation window, and final thresholds |
| e105_prosperity_cohort | Build inside saved states, annex factories outside them, lose a saved state, or change off-map industry | Only the specified saved-state building levels contribute, and final territorial ownership/control is exact |
| e105_achievement_history | Further firings while an attempt is active, reload, failure, and reattempt | No easier overwritten baseline, no reset deadline, stable receipts, and no debug-derived qualification |

## Presentation and artifact acceptance

Review the ordinary report and linked shared event-history/detail surfaces with matched scenarios.
Include a baseline result, an exhausted result, a hidden result, a self-removing result, a maximum sixteen-draw result, long native names, missing localisation, and two pending reports.
Verify readable native-size text, correct whole-number counts, preserved hidden presentation, useful result ordering, no clipped names, no wrong country, and no modifier wall forced into the report body.

The shared event history must remain explicitly actorless for this global event.
Old rows must not show new outcomes through mutable current-result variables.
Event Details remains premise-only, while effect and retention information belongs to the appropriate result surface.

Asset acceptance requires one report image and two separate achievement subjects, each with its complete three-state 64×64 output.
The achievement processor uses the exact immutable completed, grey, and red-cross template inputs.
Verify PNG and DDS dimensions, correct template alignment, alpha, strict decoded pixels, native-size contact sheets, sprite aliases, runtime paths, and source lineage.
No final asset can be substituted by a renamed existing icon, an unreviewed placeholder, or a manually drawn stand-in for required generated art.

## Subagent Usage Map

All provided subagent definitions were fully read during the source gate.
The following roles are the ones relevant to this event's actual work.
Instantiate new assignments with self-contained prompts and no inherited parent-thread history under the current linked subagents skill, using fork_turns="none" for Codex collaboration.spawn_agent.

| Role | Work performed in this planning session | Required implementation handoff or next assignment |
| --- | --- | --- |
| chaosx_scripted_system_architect | Investigated offline idea type, discovery, load resolution, callbacks, identity persistence, and narrow owner contracts | Complete native capability proof and settle the supported full-loadout route, including exact file/helper and save-migration contracts |
| chaosx_ai_probability_auditor | Reviewed the accepted formulas, exact abstract distributions, selector risks, callbacks, and scenario inputs | Inspect the real selector and complete pool, evaluate named scenarios, sweep boundaries, compare actual before/after source, and classify unresolved outcomes |
| chaosx_improvement_loop_planner | Fully read assigned project sources and performed the near-completion anti-bloat pass recorded in the dispositions | Close or amend only concrete design gaps, without creating unrelated systems |
| chaosx_documentation_curator | Fully read assigned project sources and audited draft terminology, source authority, and document consistency | Keep spec, technical decisions, implementation evidence, assets, and prompts synchronized without inventing completion |
| chaosx_event_completion_auditor | Fully read assigned project sources and performed the final package audit recorded in the dispositions | Audit actual implementation against accepted contracts and meaningful available evidence, separating unavailable checks from missing implementation |
| chaosx_generated_event_art | Not invoked for production during planning | Produce the one original report image from the exact consumer and canonical report references |
| chaosx_icon_artist | Not invoked for production during planning | Produce the two original achievement subjects and exact completed/grey/not-eligible triplets through the required processor |
| chaosx_localisation_auditor | Not invoked to draft final localisation during planning | Write or audit only Event 105 public text, exact dynamic result scopes, hidden presentation, encoding, and source-aligned catalog wording |
| chaosx_spreadsheet_doc_worker | Not invoked to edit the workbook during planning | Inspect the authoritative workbook, resolve the bounded identity discrepancies, mirror final implemented wording, preserve workbook structure, and run the exporter |

The parent owns event integration, shared Event Log and Event Details changes, final acceptance, and all claims of implementation completion.
The event UI worker does not acquire those shared interfaces merely because Event 105 appears in them.
The user owns live-game validation, which agents neither request nor await for delivery under current AGENTS.md.

### Role execution contracts

The final three spec parts, this acceptance map, the technical handoff, and the recorded review dispositions are the common accepted design inputs.
README records the user's 10 October 2026 acceptance of planning IDs 105 Random Idea and independent 104 Rule, with catalog migration remaining later work.
Each implementation assignment also supplies exact current source paths, source revisions, existing work status, allowed files, and its named handoff destination under the current [subagents skill](../../../.agents/skills/chaos-redux-subagents/SKILL.md).
New subagent handoffs belong under docs/plans/105_random_idea_plans/subagent_handoffs/.
The parent reviews each handoff against the source changes and meaningful available verification, retaining MCP limits separately from missing implementation.

| Role | Additional required inputs | Owned files and permitted writes | Forbidden surfaces | Dependency and parent follow-up |
| --- | --- | --- | --- | --- |
| Scripted-system architect | Installed reference results, complete loadout manifest, exact current event/helper/category definitions, immutable before source | The assigned architecture and migration handoff, plus only narrowly authorized helper work in a later coding assignment | No unilateral pool narrowing, event redesign, catalog changes, or unrelated shared refactor | First after reference discovery. Parent accepts the route and exact dispatch/persistence contract before the main implementation |
| AI probability auditor | Actual selector source, full resolved pool, count constants, explicit held sets, callback transitions, and named scenarios | Read-only probability handoff and evidence references | No gameplay tuning or source patch by the auditor, no invented missing candidate probability | After the real selector exists and after relevant changes. Parent reviews exact versus unresolved classifications and applies any accepted fix |
| Improvement-loop planner | Near-complete accepted design and disposition of every earlier addendum | The assigned closure or narrow improvement handoff only | No gameplay, assets, final localisation, GUI, or spreadsheets | Near completion, with no prior unresolved addendum. Parent dispositions every item and closes broad expansion |
| Documentation curator | Current source-of-truth and acceptance map, final source evidence, asset manifests, reviews, and prompt files | Assigned Markdown specifications, notes, dispositions, manifests, and documentation cleanup when authorized | No gameplay, spreadsheet, asset, or localisation implementation | After decisions or implementation evidence change. Parent verifies acceptance status remains separate from implementation status |
| Event completion auditor | Full accepted package, actual changed files, native/MCP evidence, final assets, catalog handoff | Read-only completion report with source-level findings | No independent redesign, code patch, asset production, or completion declaration | After integration. Parent resolves findings and owns the final completion statement |
| Generated event art | Exact 210×176 consumer, canonical report references, fictional photograph brief, report processor, final basename and paths | Source/processed PNG, final report DDS, manifest, contact sheet, and GFX handoff under the assigned asset workspace | No GFX/GUI/gameplay wiring, portraits, or icon production | After consumer/reference inspection. Parent checks source lineage and native-size card result, then wires accepted art |
| Icon artist | Two final achievement keys, exact immutable templates, canonical achievement references, source brief and processor | Original transparent subjects, processed state triplets, final DDS files directly under gfx/achievements/, manifests and handoff | No new achievement rules, gameplay, GFX or GUI edits, or generic converter substitution for the achievement processor | After final key collision checks. Parent verifies template pixels, alpha, all states, exact paths, and final native-size review |
| Localisation auditor | Implemented result scopes, saved retention semantics, key inventory, exact shared consumers, matched renders | Only authorized Event 105 localisation and scripted-localisation changes plus the wording handoff | No pool, quantity, callback, achievement-condition, catalog, or unrelated prose changes | After actual result mechanics and presentation exist. Parent reviews clarity, native hidden presentation, exact values, and rendered text |
| Spreadsheet worker | Authoritative workbook, current XLSX skill and preservation references, final implemented localisation keys and wording, scoped identity decisions | docs/spreadsheets/chaos_redux_events_catalog.xlsx and exporter-produced CSV refresh only | No direct CSV editing, gameplay, localisation, documentation, or unrelated workbook edits | Last after implemented wording and ID reconciliation. Parent reviews changed rows/fields, preserved structure, status basis, and exporter evidence |

The current session's specialist reports remain planning evidence.
They do not satisfy the later implementation assignments simply because the same role name appears in both columns.

## MCP Usage Map

Historical live discovery found no exposed HOI4 tool names in the planning session.
The configured server declarations in the source files do not establish an available service or its health.
The routes below map possible focused checks to questions and evidence, subject to the actual connected schema and the current [MCP workflow](../../systems/hoi4_agent_tools_mcp_integration.md).
No invented arguments, analysis IDs, native outputs, or artifacts are supplied.

For an underlying failed or inconclusive read-only capability, allow the initial request and at most one useful corrected or narrower retry, shared across files, tools, agents, and resumed turns.
Skip that retry when the route is known unavailable or no correction can help.
Record the failure, used attempts, and what changed input or capability would justify trying again in the owning handoff, then use pertinent local documentation and source checks.
Use actual weights, helpers, complete known pools, and named scenarios for source-derived probability calculations when the analyzer cannot represent the script.
Do not treat a missing optional render, historical baseline, or MCP output as a universal completion gate.
An actual unresolved pool subset, identity alias, unsupported exact achievement measure, or known defect remains substantive.
Do not request or await user-owned game testing to complete agent delivery.

| Route | Exact Event 105 purpose | Inputs and evidence to retain | Historical planning status |
| --- | --- | --- | --- |
| hoi4.reference_context | Identify the installed documentation and offline references for ideas, token dispatch, arrays, loops, constants, and saved identity | Paths, revisions, relevant section coverage, omittedSources and missing entries when reported | Not exposed here |
| hoi4.reference_search and hoi4.reference_read | Read complete relevant rules for candidate discovery, native addition, categories, callbacks, random bounds, and persistence | Exact search terms, cited lines, nextLine continuation where needed, installed game version | Not exposed here |
| hoi4.source_lookup | Resolve actual vanilla and active-mod definitions, overrides, idea categories, shared event entry points, and achievement measures | Exact keys, file paths, source revisions, structural keyPath/occurrence evidence where the live schema supports it | Not exposed here |
| hoi4.script_validate | Validate actual generated registry structures and Event 105 scripts | Source identity, diagnostic details, unresolved syntax and category errors | Not exposed here |
| hoi4.event_inspect | Inspect the real chaosx.nr105.1 root and every reachable helper/callback boundary | Complete source inventory, analysis mode, completeness, helper counts, unresolved edges, and scope diagnostics when provided | Not exposed here |
| hoi4.event_render and hoi4.event_inspect (mode = compare) | Review the real grant, continuation, re-entry, and settlement flow across matched before/after source | Graph-bearing source artifacts and explicit scenarios, not merely a trace or an unrelated cached analysis ID | Not exposed here |
| hoi4.probability_inspect | Establish the actual weighted and random surfaces and complete candidate universe | Exact selectors, all candidate identities and weights, external factors, source and pool hashes | Not exposed here |
| hoi4.probability_inspect and hoi4.probability_analyze (analysis = sweep) | Run counts, boundaries, burden, exhaustion, ownership, and supported callback scenarios | Named scenario inputs, exact/bounded/sampled/unresolved classification, threshold findings | Not exposed here |
| hoi4.probability_analyze (analysis = compare) and hoi4.probability_analyze (analysis = render) | Compare real source revisions or complete custom pools under identical scenarios and show the result | Actual before/after inputs, supported render artifacts, source revisions and scenario identities | Not exposed here |
| hoi4.probability_analyze (analysis = simulate) and hoi4.probability_analyze (analysis = sequence) | Use only when uncertainty or repeated firing analysis has fully declared inputs | Seed/stream assumptions, complete pool manifest, cadence, recovery, removal, reset, and terminal conditions | Deferred until inputs exist |
| hoi4.gui_inspect and hoi4.gui_render | Inspect the affected ordinary report linkage and exact shared history/detail selectors and layouts | Before/after source and matched result states, relevant resolutions, hierarchy, text bounds, and click regions | Not exposed here |

An optional GUI rewrite tool does not replace the layout review.
Use a reviewed direct edit for an authorized shared-surface change when appropriate, then retain available matched visual evidence or the source geometry, text, state, and click-region review with its limits.
Do not create a new MCP wrapper or a central tool skill for this event.

### MCP ordering and follow-up ownership

| Stage and route group | Required preceding state | Owning reviewer | Required follow-up before a completion claim |
| --- | --- | --- | --- |
| Live exposure and schema discovery | Actual connected tool list, never only config.toml declarations | Parent | Record absence distinctly from an unhealthy reachable service. Obtain the real schema before constructing requests |
| Reference context/search/read and source lookup | Exact installed game and active loadout, bounded source question | Parent and scripted-system architect | Read omitted relevant sections, resolve custom category and duplicate-ID rules, and record remaining missing installed sources |
| Script validation | Actual generated and handwritten source at a recorded revision | Parent implementation owner | Fix real diagnostics, rerun only affected checks, and preserve native uncertainty that static validation cannot resolve |
| Event inspect/render/compare | Implemented root and relevant helper closure, real source identities and before source when available | Parent with completion auditor | Investigate material unresolved edges or scope defects. Use matched graphs when useful and supported, otherwise inspect the affected source closure directly |
| Probability inspect/evaluate/sweep | Complete actual pool and selector plus explicit scenario state | Probability auditor | Distinguish exact model results from sampled or unresolved outcomes, then send concrete defects to the parent for source correction |
| Probability compare/render | Accepted source correction and the same complete scenarios | Probability auditor, reviewed by parent | Preserve exact source/pool identities. Rerun the affected comparison rather than treating a cached analysis ID as before-source evidence |
| Probability simulate/sequence | Fully declared uncertain inputs or the complete repeated-firing transition model | Probability auditor | Report assumptions and bounds. Keep undeclared native callbacks or unknown loadout members unresolved |
| GUI inspect/render | Exact existing shared selectors and report linkage, reference scenario, and before source | Parent shared-UI owner with localisation and completion review | Fix visible clipping, wrong context, stale retention, hidden-text leaks, and click defects, then use available matched renders or review those same requirements directly from source under the retry limit |

Store useful stable artifact references, exact source revisions, scenario identities, coverage diagnostics, and final unresolved limits in the owning handoff.
Do not treat a passing tool flag as permission to ignore visible defects or incomplete source coverage.
If a relevant route remains absent, name the unavailable check and the local verification used without representing either as MCP or native execution.

## Stop conditions for an implementation claim

Do not call the implemented event complete if the pool silently excludes otherwise addable national ideas, if coverage depends on a hand-maintained curated list, if a large registry loses its suffix, or if the event rolls one global bundle for every country.
Do not claim completion with duplicate callbacks, refreshed preowned ideas, wrong save identities, mutable old report context, native removals undone by compensation, incorrect fixed lower counts, or repeated Chaos credit.

Any unavailable exact achievement measure, unresolved native category, unknown duplicate-definition winner, unverified save rebinding, or missing final asset stays explicit as an implementation issue in the report.
Unavailable optional MCP checks stay explicit as verification limitations.
An honest design handoff may still be complete while those implementation gates remain open.
