# Event 24 foreign-response probability post-patch audit

Audit date: 2026-09-26.

Workspace root: `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux`.

Classification: the source-to-source comparison is valid and bounded over the same five event options and the same F1-F4 scenario set. Its `comparisonChanges = 0` is only a no-delta unresolved control because the comparison is partial and reports 16 unresolved or bounded items. It does not prove that the four changed predicates have no numeric effect, and it supports no exact selection probabilities or complete rankings.

This is a read-only audit. No gameplay source was edited.

## Audited surface and source identity

Weighted surface: event option `ai_chance` in `chaosx.nr24.40`, “foreign response,” in `events/024_hearts_of_iron.txt`.

| Source | SHA-256 |
| --- | --- |
| Pre-patch copy `docs/plans/024_video_game_in_sweden_plans/probability_evidence/2026-09-26_foreign_response/before_events_024_hearts_of_iron.txt` | `B5D786C1D96DF7D8B9005BF61C3A925E71D30A6B928EADBBB7066215A7157655` |
| Current `events/024_hearts_of_iron.txt` | `9C445072F4A8AB6F0BA7D00E019B6CDEF5A4C2088C9E36A5A5BBA285EE40B2F7` |
| Pre-patch copy `docs/plans/024_video_game_in_sweden_plans/probability_evidence/2026-09-26_foreign_response/before_024_video_game_in_sweden_constants.txt` | `7CC3F47614447D18C53826959432E76A6F141DF9058B6C2A1E661EFEAB31BAD2` |
| Current `common/script_constants/024_video_game_in_sweden_constants.txt` at final audit check | `622621C00D24CF036CF3FEC3F1F82949DB6D92B3AF4701AF396BEF4E132D632C` |
| Scenario fixture `docs/plans/024_video_game_in_sweden_plans/probability_evidence/2026-09-26_foreign_response/P24_FOREIGN_RESPONSE_F1_F4.json` | `9D038322A599D80A41B0AED3A64D6295396E770C563633C8F460D51F2A6F7C48` |

The event-file diff contains exactly four changed modifier predicates at `chaosx.nr24.40.a`, `.40.b`, `.40.c`, and `.40.ridicule`. Each replaced `has_war_with = event_target:video_game_in_sweden_host` with a `meta_trigger` checking whether the response country’s opinion of that saved host is strictly below the centralized threshold. The constants diff adds the intended `video_game_in_sweden_event.foreign_hostile_opinion = 0` threshold and also contains `video_game_in_sweden_cost.backlash_stability_display = 3`, an unrelated cost-display constant. The latter is not used by the foreign-response AI weights. No base weight or modifier factor changed. The four hostile factor values remain `0.35`, `2.5`, `1.8`, and `1.4` for copy, study, ban, and ridicule respectively.

The constants file’s hash was `4494E44FB74FC89AF8793F4F2DCC5BC6176D7C2DA7F4848968E2E6B7F6E2095D` at the first post-read check and `622621C00D24CF036CF3FEC3F1F82949DB6D92B3AF4701AF396BEF4E132D632C` at the final check. The added display constant was absent at the first check. Its author and timing are unknown from this read-only audit. The foreign-response event file remained at SHA-256 `9C445072F4A8AB6F0BA7D00E019B6CDEF5A4C2088C9E36A5A5BBA285EE40B2F7`.

## Named scenarios and candidate pool

The MCP scenario set is `P24_FOREIGN_RESPONSE_F1_F4`, with scenario hash `978a2aa4d2edcb38550d48d5d5bdf517c82a82dc35ea791b67ca700d9b8b16a2` in this audit’s evaluation and comparison.

| Scenario | Actor and declared state | Host state |
| --- | --- | --- |
| `P24-F1` | NOR, peace, democratic, non-major, army XP 30, stability 0.78, world tension 0.20 | Recent victory false, Reality Check disqualified false |
| `P24-F2` | GER, peace, fascist, major, army XP 70, stability 0.64, world tension 0.75 | Recent victory false, Reality Check disqualified false |
| `P24-F3` | ITA, peace, fascist, major, army XP 24, stability 0.22, world tension 0.60 | Recent victory false, Reality Check disqualified false |
| `P24-F4` | FRA, peace, democratic, major, army XP 60, stability 0.72, world tension 0.10 | Recent victory true, Reality Check disqualified false |

The complete option pool conditional on event dispatch is `chaosx.nr24.40.a` copy, `.40.b` study, `.40.c` ban, `.40.ridicule` ridicule, and `.40.e` no action. The focused inspect and the comparison both selected these five candidates, and the comparison contains 20 rows across four scenarios.

The fixture declares `has_war_with = false` for every actor and provides the Swedish host event-target scope. It does not provide actor-to-host opinion values, `global.threat`, or the complete partner-entry state. Thus the five-option pool is complete conditional on dispatch, while the external factors are incomplete for an exact evaluation. In particular, F1 does not declare whether NOR passes the neighbor, market-access, faction, or subject relationship clause. The fixture’s `world_tension` value does not supply the separate `global.threat` variable used by the ridicule modifier.

`P24-F5` is the exhausted-pool terminal contract, not a sixth normalized option race. When partner selection finds no valid partner, `video_game_in_sweden_select_foreign_partner` has no saved partner target and sets `video_game_in_sweden_foreign_pool_exhausted`. The dispatcher then has no target to send `chaosx.nr24.40` to. No option denominator exists in F5, so it is excluded from the 20-row F1-F4 comparison.

## Base weights and modifier traces

These are source constants and trigger traces, not MCP-computed rankings. Event `ai_chance` uses probability-proportional weighting among the options available when the event is dispatched. The raw values below are not click probabilities.

| Option | Base | Modifiers and source factors |
| --- | ---: | --- |
| `chaosx.nr24.40.a` copy | `foreign_copy = 1.0` | Friendly `2.5` when opinion is `> 50`; low army XP `1.8` when XP is `< 25`; hostile `0.35` when opinion is `< 0`; mismatch `0.4` when the Swedish host has `video_game_in_sweden_reality_check_disqualified`. |
| `chaosx.nr24.40.b` study | `foreign_study = 1.0` | Friendly `1.3` when opinion is `> 50`; hostile `2.5` when opinion is `< 0`; low army XP `1.5` when XP is `< 25`; major-country factor `2.0` when `is_major = yes`. |
| `chaosx.nr24.40.c` ban | `foreign_ban = 0.8` | Fascist-government factor `2.2`; hostile `1.8` when opinion is `< 0`; mismatch `1.5` when the Swedish host is Reality Check disqualified. |
| `chaosx.nr24.40.ridicule` ridicule | `foreign_ridicule = 1.0` | Hostile `1.4` when opinion is `< 0`; low-threat factor `1.8` when `global.threat < 0.30`; mismatch `2.0` when Reality Check is disqualified; recent-victory factor `0.15` when the Swedish host has `video_game_in_sweden_recent_victory`. |
| `chaosx.nr24.40.e` no action | `foreign_no_action = 0.8` | No modifiers. |

The comparison sweep could not test the opinion cutoff. Under source syntax, `foreign_hostile_opinion = 0` and the comparator is strict `< 0`; the existing friendly comparator is strict `> 50`. The values between those cutoffs, including exactly 0 and exactly 50, activate neither relation modifier.

## MCP evidence and comparison classification

Workspace: `mod_chaos_redux_ea3b2d67c2c0`. Adapter: `event_option_ai_chance`.

| Tool | Result and artifact |
| --- | --- |
| Parent after-patch inspect | The artifact URI was supplied, but its counts and diagnostics were not included in the task summary. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c637d2e04a1887b42f880d68f7f59e7a26d120ae57b32747e2cac63dc0925e30/66bf3896e0ec5ae50c19512ba1636af0f123c3a518a23754996f04d5ebdde116/probability-inspect-30b478d36411.json`. |
| Parent-supplied baseline inspect summary | Complete five-candidate pool, seven required inputs, zero inspect unresolved. Its artifact URI was not supplied. |
| Parent before/after compare | Parent-reported partial result with four scenarios, 20 candidates, 16 unresolved, and zero `comparisonChanges`. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e9b0c3b4c082ab7aabaa4e93b3905d239f2a0151d9601fa912790b09c398602d/4456f466b79aa2a58932527fd105a59ffa62e8e4098647183a50c69737ab0cd3/probability-a7e4b4882843390f6dcc5f1c.json`. |
| This audit’s initial source-wide inspect | `PROBABILITY_SOURCE_INSPECTED`, source revision `9083aa25f35a4c7e22d94bb388ffb7a39b7ab3c160128747c8d1f816fb1cd9f0`, MCP source hash `30b478d36411e695516c50c2dc07c6aff5818ab9e6abed3f9863bff58b508c90`, 47 file-wide candidates, 21 required inputs, one unresolved. This is broader than Event 24.40. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f17243d4bf33ab08fc7f88416ddbc25edc44f10cd6b70b9106dc30a233fd9d6d/6293bb5970c10c067f06e094ed7eda454bf48d0910309762c33370eeb0ccb071/probability-inspect-30b478d36411.json`. |
| This audit’s final focused inspect | Five explicit option IDs, `poolComplete = true`, five candidates, six required inputs, zero inspect unresolved. The six-input count differs from the parent-supplied baseline count of seven. The pool agrees, while the reason for the input-count difference is unresolved. Source revision `2985eda8aafffc741333d69685fac002700415e211816cc68365d08a3782ccd0`; MCP source hash `30b478d36411e695516c50c2dc07c6aff5818ab9e6abed3f9863bff58b508c90`. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ac9a4fe7fdd30109f4e35bd7bb4f9910ef3ba4725e5aa4da1addbc964e26e8cc/20d26b160c6b93ac683fd89737c7c44c02d7da46a0fb14804d75ceaec5eef37f/probability-inspect-30b478d36411.json`. |
| This audit’s final post-patch evaluation | `PROBABILITY_ANALYZED_PARTIAL`, analysis `probability-db69bebea1218ec6dbed2f79`, four scenarios, 20 rows, seven unresolved or bounded items, four diagnostics, source revision `2985eda8aafffc741333d69685fac002700415e211816cc68365d08a3782ccd0`, scenario hash `978a2aa4d2edcb38550d48d5d5bdf517c82a82dc35ea791b67ca700d9b8b16a2`. No numeric ranking claim is taken from this partial result. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f82887b20a2584dd39abc284b88ae2f103b221da90607cc9739f533db3ede865/babc9c8efb8a6d886f6fb48cc825b750279d353accde115163245fc19f1c4d37/probability-db69bebea1218ec6dbed2f79.json`. |
| This audit’s final before/after compare | Used the exact pre-patch event copy and current `events/024_hearts_of_iron.txt` as nonempty source paths, the five-option pool, and the same `P24_FOREIGN_RESPONSE_F1_F4` scenario set. `PROBABILITY_ANALYZED_PARTIAL`, analysis `probability-b16b3048dd81d01444972fd9`, four scenarios, 20 rows, 16 unresolved or bounded items, `comparisonChanges = 0`, four diagnostics, source revision `2985eda8aafffc741333d69685fac002700415e211816cc68365d08a3782ccd0`, scenario hash `978a2aa4d2edcb38550d48d5d5bdf517c82a82dc35ea791b67ca700d9b8b16a2`. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5e460863b998ac92ab3dba9163fb35da3899f3094e43c93e1f6510759cbdd046/3c91e12879268aee83270beb7be44105c366876e0232bfcadc27f152522d1098/probability-b16b3048dd81d01444972fd9.json`. |

The final compare call emitted comparison SVG and PNG, matrix SVG and PNG, and unresolved SVG and PNG. The comparison view artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2450d67f32f665574260ffbd84f57cc7db1a9cf58aca09b66d13c1108a27cc49/e6a654d1c72fe2a4d7feae00feb836c3876722cf7801e7742c3418e03d727a3a/probability-probability-b16b3048dd81d01444972fd9-comparison.svg`. The matrix view artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/dbae9b13c198533df0d53594310c6d0488c93f2dd0117007710ebe67f1604420/29149c76fd40cdcac46918ad5204b9dc1c3640cabee434276a41b9ae4036c723/probability-probability-b16b3048dd81d01444972fd9-matrix.svg`. The unresolved view artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/495d4ac2985a282808a46ec00cdbe6035f5edb7250b409718da075c8a18db73c/55df34e4d004e2f4e26e99beb268d621896275c5d78602178df9a2416f12710e/probability-probability-b16b3048dd81d01444972fd9-unresolved.svg`.

The final evaluation also emitted ranking, matrix, waterfall, and unresolved views. Its matrix artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/dbae9b13c198533df0d53594310c6d0488c93f2dd0117007710ebe67f1604420/f3539899c18084788e3a5130e200c66dad351e2372196de460f6d9068da58dbb/probability-probability-db69bebea1218ec6dbed2f79-matrix.svg`. Its unresolved artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/be7e0835fd45266e202e1a6e57dad593baa7af928f9da606a1ea9b89132d0c03/342a941d7effd9c0ee40155300d11b87bf00040a3d38f47ea772454f3e6b2d18/probability-probability-db69bebea1218ec6dbed2f79-unresolved.svg`.

An explicit `hoi4.probability_render` request on the final comparison returned `PROBABILITY_ANALYSIS_STALE`, with current workspace revision `fa373e906d4e26f7a8833a7356e68bf97230ebf8502d8d92beee922a35317480` after comparison revision `2985eda8aafffc741333d69685fac002700415e211816cc68365d08a3782ccd0`. It returned no visual resources. The stale diagnostic does not identify which source changed. Stale-render artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/27e20b751bf2dfbd1a60901ea72c61904b7fb92dbe574837b6ebc35ea250a3f7/4c6b8fd7c85535d70dbc351d69af3a8d0ffaf15f4ba4ebfbf068269287eff277/probability-b16b3048dd81d01444972fd9.json`. The final compare call’s own rendered artifacts remain available as linked evidence.

Four inline diagnostics state that the copy mismatch factor, ban mismatch factor, and ridicule mismatch factor are inactive in all supplied scenarios, which matches the declared false host-disqualification flags. The fourth states that the ridicule recent-victory factor is inactive in every scenario even though F4 explicitly sets the Swedish host’s recent-victory flag to true. That is a scenario-to-adapter projection inconsistency and leaves the F4 recent-victory trace unresolved.

The comparison result is a valid bounded source comparison because it uses the real pre-patch source copy and current source with an identical scenario set. Its zero change count only says that the partial comparison produced no resolved delta. It is an unresolved control for the changed opinion predicates, not evidence that the patch changed nothing.

## Structural event evidence and source gates

`hoi4.event_inspect` used selector `{kind: event, eventId: chaosx.nr24.40}`, mode `trace`, direction `both`, depth 3, 60-node limit, and helper expansion. It returned `EVENT_INSPECTED_PARTIAL`, revision `f95e58711c7ffdcda2bae4e59e7e030aa20b045e86c1e5e9d35a647536d55fa0`, graph hash `06fc0bb73dcf1f3e4c47694633ac804b9d812ab3372152192f305b3b10a289e3`, zero indexed helpers, 8,908 unresolved nodes, 2,194 diagnostics, and no blocking diagnostics. It also returned `MCP_INLINE_FILES_TRUNCATED` because 384 source paths were indexed while the inline inventory returned 64. The exact focused-analysis limit says workspace-wide helper projections and lifecycle passes were deferred. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/48e3549d306b8f47f2f681f146621b72ed26ecff0926f75a66477fa394efdb7f/277ae3eed153a3906471137dbc0915b25722cadd41c9c20c6d058da6cd7a8da4/event-trace-f95e58711c7f.json`.

`hoi4.event_render` rendered the same selector’s `options` view at that revision. It returned `EVENT_RENDERED_PARTIAL`, 11 selected nodes, 42,851 omitted nodes, zero indexed helpers, and no blocking diagnostics. The source-linked SVG is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b68f0582128338318a54330be0e58ff6d8a7dcb3d12c35093a2237b7a1995fc3/444d4d5d9f737c72d94bb6e3d4759aa5cb7571199261486c0408f23e5d0bf0e4/event-options-f95e58711c7f.svg`. These partial structural artifacts do not certify lifecycle behavior.

Source review confirms the active-war exclusion at three relevant points. The event trigger for `chaosx.nr24.40` requires the saved host and partner, pending-response flag, current-host validity, partner existence, non-capitulation, and `NOT = { has_war_with = event_target:video_game_in_sweden_host }` at `events/024_hearts_of_iron.txt:527-536`. `video_game_in_sweden_is_valid_foreign_partner` excludes war with `ROOT` at `common/scripted_triggers/024_video_game_in_sweden_triggers.txt:247-259`. `video_game_in_sweden_dispatch_foreign_response` revalidates the pending partner and excludes war with `ROOT` before sending `chaosx.nr24.40` at `common/scripted_effects/024_video_game_in_sweden_effects.txt:2160-2184`.

The selector caps responses at `maximum_foreign_responses = 3`, excludes countries already marked `video_game_in_sweden_foreign_response_seen`, and tries neighbor, major/faction/subject, market-access, then any-valid-partner pools. When no partner target is found, it sets `video_game_in_sweden_foreign_pool_exhausted` at `common/scripted_effects/024_video_game_in_sweden_effects.txt:2152-2157`. F5 therefore has no dispatch and no normalized option race.

## Risk findings and unresolved analysis

The original hostile predicates were unreachable through the intended foreign-response route because the event and valid-partner gates reject active wars. The opinion predicates now express hostility independently of war. The four numeric hostile factors and all five positive base weights remain unchanged. This supports the source-level correction, not a balance conclusion.

The post-patch evaluation reports seven unresolved or bounded items. The inline response does not enumerate these seven as field-level rows. The exact missing scenario facts identified from source are each actor’s opinion of the saved Swedish host and `global.threat`, plus full partner-entry state. The new hostile and existing friendly opinion predicates cannot be traced for F1-F4 without those opinion values. `world_tension` does not replace `global.threat`. The F4 recent-victory diagnostic also remains inconsistent with the fixture.

The comparison reports 16 unresolved or bounded items. This count is consistent with the parent-supplied baseline evaluation count of nine plus this audit’s post-patch evaluation count of seven, but the compare result does not expose a per-side item breakdown inline. Neither the baseline inspect artifact URI nor the baseline evaluation artifact URI was included in the parent request, so their detailed rows could not be independently inspected here.

The five-option pool is complete for the response event once dispatched. External validity is not complete for every F scenario because event targets, pending state, capitulation, partner relationship, response count, seen flags, and pool-exhausted state are not all represented. Source gates are present and exclude active wars, while MCP scenario evaluation does not certify all dispatch gates.

No dominance, starvation, rank reversal, or exact selection-probability conclusion is supportable. The current base weights and factors are traceable, but incomplete opinion and threat inputs prevent complete normalized results. Source review shows a three-response cap and a per-partner seen flag. No sequence model was run to test repetition over time.

## Sweep, skipped analyses, and recommended follow-up

`hoi4.probability_sweep` was attempted on the same F1-F4 set and five options with path `state.has_army_experience`, five steps, pairwise comparison, and rank-reversal search. MCP returned `PROBABILITY_SWEEP_RANGE_REQUIRED` and no artifact, stating that every sweep path needs a scenario range, numeric alternatives, or a numeric state value. The requested opinion threshold has no declared opinion range in the fixture, so no threshold sensitivity or rank-reversal conclusion is available.

`hoi4.probability_simulate` was skipped because no uncertain-input distributions, correlations, or seed contract were declared. `hoi4.probability_sequence` was skipped because this audited surface is an event-option `ai_chance` race, not a complete declared custom weighted pool with cadence and state transitions. F5 is a no-dispatch terminal and cannot be normalized with the five event options. MTTH analysis was not applicable because this surface is event-option `ai_chance`, not an MTTH entry or MTTH-backed AI weight.

Recommended follow-up for the source owner, without applying changes in this audit:

1. Extend the F1-F4 scenario fixture with explicit actor-to-Sweden opinion values and `global.threat` values, preserving the named scenario intent and recording the source for each value.
2. Add the required valid-partner and dispatch-gate inputs where a scenario is intended to prove that the event can fire, including the relationship clause for F1 NOR.
3. Resolve why the adapter reports F4’s true Swedish recent-victory flag as inactive, then rerun the focused inspect, evaluation, and before/after comparison with the same source snapshots and scenario hash.
4. Supply a declared numeric opinion range accepted by the installed sweep route, then rerun the hostile-threshold sensitivity and rank-reversal search. If the installed route still rejects that range, preserve the exact MCP validation error and leave sensitivity unresolved.
5. Preserve a link to the baseline evaluation artifact with the handoff so the nine baseline unresolved rows can be matched against the seven post-patch rows.

The next audit conclusion should remain bounded until those inputs are present and the comparison resolves the changed opinion modifiers. No source recommendation to change the numeric base weights or hostile factors is supported by this evidence.
