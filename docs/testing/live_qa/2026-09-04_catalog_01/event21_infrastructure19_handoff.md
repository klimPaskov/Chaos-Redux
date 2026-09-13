# Event 021 infrastructure parser correction

Disposition: implemented, native parser acceptance pending and MCP probability impact unresolved.
Acceptance basis: the parent authorized only five infrastructure comparison wrappers in the three files below, preserving scope, comparator, threshold, and surrounding logic.

## Exact changes

Every change wraps an existing bare infrastructure comparison with `check_variable = { ... }`.
Four retain `> constant:random_civil_war_value.zero`, and the ordinary viable-anchor predicate retains its existing literal `> 0`.

| File and line | Existing helper | Evaluation scope and preserved behavior |
| --- | --- | --- |
| `common/scripted_triggers/021_random_civil_war_parent_triggers.txt:82` | `event021_parent_event6_package_setup_proven` | The state stored in `independence_wave_anchor_state`, alongside existing population and ownership/control proof. |
| `common/scripted_triggers/021_random_civil_war_parent_triggers.txt:144` | `event021_parent_viable_anchor_state` | Current candidate state, preserving literal zero, host ownership/control, and the capital exception for same-tag routes. |
| `common/scripted_triggers/021_random_civil_war_parent_triggers.txt:349` | `event021_parent_secondary_state_candidate` | Current candidate state, preserving the noncapital, unused-transfer-state, ROOT ownership/control, and population checks. |
| `common/scripted_effects/021_random_civil_war_achievement_effects.txt:116` | `event021_begin_achievement_history` | Current `capital_scope`, only within the replacement-capital population/infrastructure branch. The original-capital alternative remains unchanged. |
| `common/scripted_effects/021_random_civil_war_parent_effects.txt:161` | `event021_parent_find_event6_package` | `event_target:liberation_candidate_anchor`, preserving exact package admission, ROOT ownership/control, population, noncapital/reservation gates for secondary search, and carrier preflight. |

The parent-supplied launch 18 error log reports the five locations, including repeated effects-file diagnostics during loading.
Installed vanilla `documentation/dynamic_variables_documentation.md` identifies `infrastructure_level` as a state dynamic variable at line 1133.
Installed vanilla `documentation/triggers_documentation.md` documents the short greater-than `check_variable` syntax at lines 2110–2132.
The installed vanilla state-scope precedent is `common/decisions/MTG_congress.txt:400`.
The offline Data structures game-variables section and Triggers variable-comparison entry were consulted alongside these vanilla references.
This reuses the syntax proof and parent-owned parser acceptance recorded in `event6_infrastructure17_handoff.md`, without treating that earlier launch as validation of these five additional lines.

## Helper and caller review

All five enclosing helpers were reviewed in full, together with the matching helper documentation and direct callers.
No helper, input, output, default, mutation side effect, constant, event target, cleanup hook, or direct call site was added or removed.

`event021_parent_event6_package_setup_proven` is consumed by `event021_parent_event6_package_complete`, including package actor setup at parent-effects line 2906.
`event021_parent_viable_anchor_state` filters the deterministic highest-score anchor selection at line 1182 and the bounded connected-region expansion at line 1237.
`event021_parent_secondary_state_candidate` filters `random_owned_state` at line 2484, so its candidate-pool impact is a required probability audit surface.
`event021_parent_find_event6_package` chooses the first admitted package from the existing registry and feeds route evidence at line 960 and Event 006 secondary-front setup at line 3078.
`event021_begin_achievement_history` is called only after opening-plan validation in `event021_random_civil_war_commit_opening`, at `021_random_civil_war_effects.txt:715`.
The existing target/archetype weights, state-scoring helper, and selection algorithms remain unchanged.

## Backup and change proof

Full-byte backups are under `docs/testing/live_qa/2026-09-04_catalog_01/pre_patch_event21_infrastructure19/`, using each original basename.
All three current sources were checked against their captured baseline hashes before backups and again immediately before writing.
Exactly three, one, and one comparisons changed respectively.
Removing only the five wrappers recovers every original source byte, and the post-write readbacks matched the intended content.

| Source basename | Backup SHA-256 | Post-edit SHA-256 |
| --- | --- | --- |
| `021_random_civil_war_parent_triggers.txt` | `C333001E5E7A122C73672F1EDDA780EC47ADC90EC7507A2A8A83D53B8AB6BBBB` | `7F47BA3F4DCA0D1BFE1B7BF6C586CCECF41E16E112985A97222901911D7BAFD6` |
| `021_random_civil_war_achievement_effects.txt` | `365130615F3EE29BE9647255820405B4DC525E33976310C69B0DDEEABBC7BEBA` | `095079037B360867FE7E60B750807725F68D51D1CD4B3CD53924FCFD13F8EE31` |
| `021_random_civil_war_parent_effects.txt` | `2B3010670576F3C741684AAC2C8A2E590360670871F1AB62FD0BE99C76445D3E` | `E84C38F6A64EE5C83E81E65AC4D5ED7768BBACBF43C28B4C6EBA0C0CBE6068F6` |

## MCP evidence

The linked `chaosx.nr21.1` root received a narrow read-only trace and neighborhood render with depth 1 and 8 nodes.
Trace used at most 12 edges, and helper expansion was disabled.
Both returned partial results at revision `410c82bea077b36a7e01b4ed11eb4927d40357359aad54622f2b2adf58fea5cb`, with full validation false because workspace-wide helper projections and lifecycle passes were deferred.
Trace artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/770ca88b9f7cdc62e727b2748c5c96232b42a409451d1051d8a5aba6009794f3/d2c2e116ae6e96bc92894be2d22ee4fa4b592610523e3e61d546a205a8bf3618/event-trace-410c82bea077.json`.
Render manifest: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b003118f441ae1672c0d6ff3d4f0baeb7ca99350c296ed0e50586cc2888d549d/76a79d2c54b7fe766a444e4d69d69c0a31a475da863bd1ef41f4443b4207a56b/event-neighborhood-410c82bea077-manifest.json`.
The required post-edit event comparison against that baseline revision returned `EVENT_REVISION_NOT_CACHED`, stating that the requested event graph revision is not cached, with no comparison artifact.

The read-only probability auditor established a fresh baseline before the patch.
Trigger and achievement source discovery returned `INTERNAL_ERROR`.
The parent-effects inventory exposed its existing random-list entries, while the explicit secondary-state helper probe returned `identifier_not_found` and zero custom-pool candidates.
No runtime candidate list was fabricated and no manually supplied route-weight fixture was used as eligibility proof.
Detailed source-discovery artifacts and classification are recorded in `event21_infrastructure19_probability.md`.
The mandatory before-and-after probability comparisons used the same scenario set, `E21_INFRA19_GATE_ROUTE_FIXTURE_2026_09_05`, for each source pair.
The trigger and achievement inline-source comparisons returned `PROBABILITY_SURFACE_EMPTY`, with no matching weighted block or comparison analysis.
The parent-effects comparison returned `PROBABILITY_ANALYZED_PARTIAL`, analysis `probability-7751187093fb2fc529a9e931`, with all 12 rows unresolved and `PROBABILITY_CANDIDATE_POOL_INCOMPLETE` because the archived candidate paths did not resolve alongside the current-source candidates.
Normalized probabilities were withheld, and the reported 24 comparison changes are not attributed to these wrappers.
Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9894583d777db639a1e23e84413c81d1966c696d8920c05c3ef56d63dcd5c584/296687d1538e80d265771839aad0d474bbf046fef7f9fa0b81d37186b6f4bb22/probability-7751187093fb2fc529a9e931.json`.
The comparison declared downstream route weights solely as tool inputs and did not evaluate the five infrastructure gates.
No fixture result is accepted as infrastructure eligibility, state-pool, ranking, or campaign probability evidence.

## Simplifications, omissions, and blockers

No gameplay simplification or fallback was made.
Only the five authorized infrastructure comparisons changed.
Raw building-level conditions remain outside this patch and belong to the parent's separate investigation.
No new localisation, catalog, asset, or helper-registry documentation was required because the exposed names and intended contracts remain unchanged.
Native parser acceptance for these five locations remains pending.
MCP event comparison and infrastructure-dependent candidate/route propagation remain unresolved for the reasons above.
The subagent did not launch the game or create a commit.
Skills used: events and subagents, with the prior decisions/missions guidance retained for the vanilla precedent.
No skills were created or changed.
