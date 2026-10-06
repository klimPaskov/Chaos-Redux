# Event 004 release QA reconciliation, 2026-10-06

Disposition: implemented for the bounded Random War source repair tranche committed as `c45a0f4988574390182f3683eb1d4b8e249e8bf4`; full release signoff remains incomplete.
Acceptance basis is the parent-relayed user's 5 October 2026 release-QA direction, including G6 authority for coherent repairs, low popup counts, concrete costs and complete forced-launch feedback.
The parent retains final integration review and the user owns live acceptance.

## Source-of-truth map

| Surface | Current authority or evidence | Disposition and limit |
| --- | --- | --- |
| Existing Random War design | `docs/events/004_random_war/overview.md`, current source and accepted entries in `agent_decisions_2026-10-05.md` | Accepted bounded repairs preserve the existing stages and option weights; broader future ideas remain proposals. |
| Source completion audit | `subagent_handoffs/completion_audit_20261005.md` | Historical snapshot; later prepared-context and random-bound repairs require current source review. |
| Weighted behavior | `subagent_handoffs/probability_baseline_20261005.md`, `probability_before_20261005/` | Current complete option pools evaluated; old timeout prose is historical, and before/after/direct-random coverage remains unresolved. |
| Catalog | `catalog_changes_pending.md` | Accepted and queued under the explicit no-workbook-write boundary; no Playable approval. |

## Current implementation and files

Each invocation completes its declaration chain before sending one observer news and at most one participant response per involved country.
An attacked country receives the defender response even if it also declared war.
The summary counts distinct countries rather than substituting declaration count.
Prepared stage, tier, declaration target and special-country chance persist on the dispatching country with the selected pair, are restored across helper frames, and are consumed/reset after firing.
Repeated Wars-cluster invocations prepare fresh context and retain the actual aggressor for history.
Settings preparation and direct root entry own their once-only unsuccessful-launch feedback receipt.

Field defenses cost 25 PP and give three modest modifiers for 45 days: 10% core defense, 5% organization recovery and 25% faster entrenchment.
Reserve mobilization retains its stability cost, adds 25% mobilization speed, 5% relative recruitable population and 10% training speed for 45 days, and grants no flat or weekly manpower or conscription-percentage gift.
Static idea tuning uses six file-local constants because those modifier fields reject global constant tokens.
The special d100 draw uses the half-open upper bound 101 and the final-stage declaration draw upper bound 9, preserving intended 1-100 and 7-8 outcomes with documented temporary-random storage.
The six declaration profiles remain 1,3,4,5,6,7–8 and the special thresholds remain 0,0,20,35,55,70.
Current source retains aggressor option weights 80/20 and defender weights 70/30.

Owned/shared implementation paths are `events/004_random_war.txt`, `events/_chaosx_news.txt`, `common/scripted_effects/004_random_war_effects.txt`, `common/scripted_triggers/004_random_war_triggers.txt`, `common/script_constants/004_random_war_constants.txt`, `common/ideas/004_random_war_ideas.txt`, `common/scripted_localisation/004_random_war_scripted_localisation.txt`, `localisation/english/004_random_war_l_english.yml`, and the shared Settings/cluster caller initializers recorded in the dated decision log.
Existing report/news/idea sprites are reused; no new portrait, model, audio, world-end branch or scripted GUI was introduced by this repair tranche.

## Meaningful evidence and limits

The dedicated probability auditor evaluated each complete two-option pool under four named scenarios: `calm_baseline_1936`, `tier2_special_available`, `tier3_special_unavailable` and `final_declaration_count`.
Its updated handoff records exact conditional shares 80%/20% and 70%/30% for those source-local pools.
Those evaluations do not establish special-country selection or final declaration-count distributions because the country-state/legal-pair pools and transition state were not encoded by those labels.
Before/after option comparisons, historical direct-random comparison, fresh direct-random inspection and separate probability-render calls timed out at 600 seconds.
The successful evaluations themselves returned ranking/matrix/waterfall resources and complete JSON; those evaluation-provided artifacts remain available even though the separate render route timed out.
The attacker and defender analysis IDs are `probability-26a7600c072928d38ff45e45` and `probability-a9775cecdb4a46a4ac23547d`; the specialist handoff retains their exact scenario hashes and artifact URIs.
The frozen current effect hash in the handoff is `5B4E3DBD5CE2479B393731A7D4FB6D83277B5E64D25083EA06205726D76460F5`; a comparison attempted before the last persistence change does not certify that later source.
No live repeated-selection frequency, realized stage total or special-country share is claimed.
The committed source tranche remains `c45a0f4988574390182f3683eb1d4b8e249e8bf4`; later service transport failures on other event windows supply no additional Random War balance evidence.

Focused event trace revision `3847e34a08e7d75169959ca12d9b601e0b82e964aff636ccd37c531ff000cd41` defers helper/lifecycle projections and does not prove the absence of existing helpers.
The namespace options render and narrow historical comparison each timed out awaiting `tools/call` after 600 seconds.
The report-aggregation snippet validator returned `SCRIPT_CHECK_PARTIAL`, `valid=null`, leaving `country_event` arguments unchecked and `else` undocumented; the owner read underlying references instead of treating that result as full validation.
Tool exposure is recorded separately from service health, and no standalone viewer availability is inferred.

The supplied `evt004_pop00.png` and contact sheet show one baseline observer news on 1 January 1936 with readable report content; other identified popups are vanilla.
This establishes supplied baseline presentation only, not post-change evolved chains or defender responses.
The save-inspection receipt identifies the supplied baseline as USA, democratic, normal difficulty, `1936.1.1.12`, Operation Postern 1.19.2.0.a729; it does not establish post-change outcomes.

## Dispositions, contradictions and outstanding work

| Document or finding | Reconciled disposition | Reason or limitation |
| --- | --- | --- |
| Dated QA decision log | Implemented | Current source and committed tranche support its accepted repair claims; final runtime acceptance remains open. |
| Probability handoff's older failed evaluation paragraphs | Historical, superseded for current option shares | Its updated successful current-pool section governs those results; retain the same frozen scenarios and unresolved compare/direct-random coverage. |
| Completion audit | Historical source snapshot retained | Do not repeat already-applied preparation/profile/aggregation repairs or use the earlier hash as current source evidence. |
| Regional weighting and richer cluster interactions | Unresolved proposals | Future-work ideas are not accepted implementation requirements in this bounded QA task. |
| Catalog note | Accepted and queued | Explicit no-workbook/CSV-write boundary; status remains Needs Testing until approval. |

No individual handoff, historical source snapshot or source specification was edited.
No bounded source simplification is identified for this tranche; its missing same-scenario comparisons, dynamic target-pool analysis and live acceptance are explicit release-proof limitations.
The preserved old evidence is cross-linked rather than deleted.

## Parent and user acceptance checks

The supplied baseline is fresh USA 1936, first option and two months, counting vanilla reports separately.
The orchestrator's checks cover baseline plus Chaos 200/400/600/800/1000+, disabled highest evolution, an interrupted chain with truthful distinct participants, repeated cluster slots with fresh pairs and actor history, no legal pair with one failure report, and both defender choices in separate fresh states.
Participants must receive at most one response plus the observer news, costs/modifiers must match the current source, and reserves must generate no flat/weekly manpower gift.
The parent must obtain or explicitly retain blockers for same-scenario option/direct-random comparisons against genuine before sources and complete legal-country scenarios before claiming full balance completion.
No game, desktop, workbook, CSV, index or commit action was performed by this documentation task.

## Curator evidence snapshot and cleanup handoff

Snapshot UTC: 2026-10-05T23:50:19.091016+00:00.
Only the relevant source blocks were reviewed; the hashes identify their complete current files without claiming whole-file or engine validation.
Concurrent edits may supersede this snapshot, and parent review must bind final evidence to final source.

| Source path | SHA-256 at reconciliation |
| --- | --- |
| `events/004_random_war.txt` | `7bc426ffa7c281106a2bc15e7a7ca39585863416110057857f1a6b4b58095cb5` |
| `common/scripted_effects/004_random_war_effects.txt` | `624c579e7ed14b9c395b202ba06b5423b9430c7c6311b38e9f16ff6fe006b860` |
| `common/script_constants/004_random_war_constants.txt` | `707c9d3a80c6232d0ed5d6b41546f98815a6d7af3eab6bd0fd63aa0ca2639dfe` |
| `common/ideas/004_random_war_ideas.txt` | `f533e788715b39d0577c789149021dc03c40aba61cc255eebc185f0d06586ea1` |

Curator MCP event trace used workspace `mod_chaos_redux_ea3b2d67c2c0`, exact root `chaosx.nr4.1`, downstream depth 1, at most 8 nodes and 12 edges, helpers disabled and refresh false.
The result was `EVENT_INSPECTED_PARTIAL`, graph revision `cbef47af49d785c1f3104fe5627678fd5bb0b5f4a6b3bf0ff968893077a95f05`, helper projection deferred, one blocking diagnostic and validation false.
The authoritative report is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/82f38bfd5133495f34910f1e417195ad56d041974709b120ab3c51e372643603/70b48b9ddfffd89345680fb83f8e4fef5980a1cd065ba4d49db8c1f57de504c9/event-trace-cbef47af49d7.json`.
The first 8192-byte range identifies `complete=false`; the full 1079988-byte report was not reconstructed in this documentation task.
Its continuation URI is the same report with `?offset=8192&length=8192`, so detailed diagnostics beyond the retrieved boundary remain unreviewed.

Changed documentation is this report, the matching event overview, `agent_decisions_2026-10-05.md` and `catalog_changes_pending.md`.
The report is also the bounded resume packet; no separate duplicate packet was created.
Individual evidence handoffs, source specs, prompts and historical snapshots were left unchanged and cross-linked by disposition rather than merged or deleted.
No stale prompt file was changed in this owned scope.
Meaningful reconciliation checked current host dispatch, memorial or actor/terminal criteria against named source blocks and compared installed-asset status against reviewed owner handoffs.
Binary models/assets, workbook cells and live execution were not independently re-audited because they belong to their assigned owners; provenance and visual limitations are retained explicitly.
Curator skills applied: events, subagents and the relevant focus/assets/super-event/GUI documentation boundaries; this curator edited no skill.
The parent implementation used events, decisions, assets, GUI, focus, super-events, MTTH, save inspection, subagents, shared-commit, frame-animation, 3D and official skill-creator workflows.
The parent updated the existing events frozen-source/candidate-matching contract in commit `81571bcf3c2b1b5a70dfb13cff99c2dd5b179493`; no new skill or central MCP wrapper was created.

No new scripted-GUI, focus, technology or map surface is introduced in this bounded Random War repair; the preserved existing report references do not imply an absent custom GUI requirement.
The scoped Markdown audit found no accidental prose hard wraps.
Five apparent candidates in Event002's Anti-Zombie League manifest/rules/goals section are intentional indented list continuations and were preserved.
Changed report/overview cross-links and named current evidence paths were checked; no individual evidence file or source-spec text was modified.

## Final bounded release snapshot, 2026-10-06

Full release signoff remains incomplete.
This section supersedes earlier pending-current-status wording only where a later named source or receipt is supplied; historical snapshots and their limits remain intact.
The bounded source commit remains `c45a0f4988574390182f3683eb1d4b8e249e8bf4`; the current option-pool evaluations do not complete direct-random target or sequence analysis.
No later Random War gameplay commit was supplied in the current parent commit ledger.
The shared frozen-source/candidate matching workflow in the events skill is maintained by the parent through official skill-creator in commit `81571bcf3c2b1b5a70dfb13cff99c2dd5b179493`; it is tooling guidance, not additional Random War gameplay or balance evidence.
Fresh responding focus/GUI clients on other events supersede a global transport-unavailable description, but do not supply Random War target-pool or same-scenario comparison evidence.

### Concrete acceptance fixtures

These are declared checks for the parent/user acceptance ledger, not new observed outcomes or permission to launch the game.
Keep baseline and changed-state inputs equal except for the stated variation and record actual country/state identities where a campaign-derived pool is required.

| Case | Fixture inputs | Required outcome and current limit |
| --- | --- | --- |
| Calm observer | Fresh USA; 1936.1.1; Chaos 0; legal major-major pair; force one invocation | One declaration and one observer report; selected actor matches Event Log. |
| Enabled stages | Separate identical legal-country pools at Chaos 200/400/600/800/1000+; disable only the highest eligible evolution in a matching fixture | Declared profile 3/4/5/6/7-8 or next enabled lower profile; exact realized counts depend on legal remaining targets. |
| Interrupted chain | Chosen profile exceeds remaining eligible legal participants; cooldown/alliance/war filters applied; no illegal pair permitted | Distinct-country count remains truthful and each participant receives at most one response plus news. |
| Repeated cluster slots | One Wars cluster with repeated enabled Random War slots and recorded actual aggressor/target/cooldown state after each | Fresh prepared pair/profile per successful slot; no reuse of consumed context. |
| No pair and defender choice | No legal pair fixture; separate defender fixtures selecting defenses/reserves, with sufficient displayed cost | One owned rejection for no pair; current three modifiers expire after 45 days; no flat/weekly manpower or conscription gift. |

### Current source identities

Snapshot UTC: 2026-10-06T03:13:39.031529+00:00.
These file hashes bind source identity for parent review; they do not prove service indexing freshness, decoded model QA, current renders or live behavior.
The parent may append final integration commit references after its own isolated source review.

| Source | Current SHA-256 |
| --- | --- |
| `events/004_random_war.txt` | `7bc426ffa7c281106a2bc15e7a7ca39585863416110057857f1a6b4b58095cb5` |
| `common/scripted_effects/004_random_war_effects.txt` | `624c579e7ed14b9c395b202ba06b5423b9430c7c6311b38e9f16ff6fe006b860` |
| `common/script_constants/004_random_war_constants.txt` | `707c9d3a80c6232d0ed5d6b41546f98815a6d7af3eab6bd0fd63aa0ca2639dfe` |
| `common/ideas/004_random_war_ideas.txt` | `f533e788715b39d0577c789149021dc03c40aba61cc255eebc185f0d06586ea1` |

No further MCP request, source patch, model decode, binary inspection, spreadsheet edit, index mutation, commit or desktop action was performed for this final documentation update.
