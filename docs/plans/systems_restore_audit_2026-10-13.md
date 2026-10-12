# Gameplay systems restoration audit — 13 October 2026

Owner assignment: audit chemical deployment, contamination, cylinders, projectors, deaths, condemnation, air contamination, camps, raids, Chaos Meter, event selection/timers, clusters, and triggerable scenarios over the last 14 months.
The owner authorized exact historical restorations of clear regressions and required ambiguous changes to remain untouched.
Biowarfare, migration, famine, scientists, and abilities were excluded as assigned to other jobs.
The [owner's plan](chaos_redux_restore_plan_2026-10-12.md) was read fully before work.

History window: 2025-08-13 through this audit, beginning from committed `b091ea0ca2b22e206ed6c2421d3e89932bd983f3`.
Evidence uses path-scoped and rename-aware `git log`, `git log -S/-G`, actual commit diffs, `git show <change>^:<path>`, and historical/current caller searches.
Commit titles, code volume, and a document's status label were not treated as approval or proof that a removed definition was reachable.
The sections distinguish recorded user/parent acceptance, source behavior, and unresolved choices.

## Result and restoration disposition

No gameplay restoration has been applied by this audit.
The investigation found historical outages and reductions, but the identified outages have replacements or prior repairs, several retired definitions were already unreachable, and the remaining alternatives require an owner decision about an intentional replacement or balance policy.
The exact historical sources for those alternatives are recorded below; none was rewritten or silently reinstated.
New mechanics, original art, dynamic tuning, existing restorations, and concurrent work were preserved.
No gameplay simplifications were introduced.
Execution stalled during final review and then resumed; the narrow nuclear and camp chronology comparisons were subsequently completed.
The four French/Belgian camp outcomes are confirmed historical source losses, with no exact current counterpart established; their restoration alongside the newer civil-Administration model remains an owner decision rather than a silent revival of its retired bridge.

## Chemical deployment and chemical raids

Strong historical baseline: `5740285289001f6361b1426b3acf0422ac9d98da` (12 February 2026) has cylinder releases, projector/tank support, chemical air bombs, direct nerve/special-agent raids, projects, equipment, and AI.
The old six raids in `common/raids/chemical_nerve_raids.txt` and `chemical_special_raids.txt` were visible from their research/project gates and had ordinary target launch checks.

`c17569ee599cbf82d1fd51e63d792ad20b101435` (14 July) placed `always = no` in visibility, availability, and launchability for Sarin/Soman air/rocket strikes and Malodor/behavioral-agent strikes before the replacement selected-state paths were wired.
This was a real historical loss; the exact old definitions are in that commit's parent.
Current `common/raids/cbrn_chemical_air_raids.txt` provides those agent/air/rocket route families, so returning the old definitions would duplicate the current delivery routes rather than close an outstanding omission.

`067d392c13b19c72a07c61879384793aba7fe2db` (9 August) reactivated Japan's exact-state decision path with a free agent selector and actual payload debit.
`33b6946dd923b9fc90fbf29bc5798dce3c76a76f` (22 September) removed those decisions in favor of native raids with an assigned division, supply-node origin, and five-day preparation.
That is an identifiable increase in operational steps, but the [Japan source account](../systems/cbrn_warfare/chemical_warfare/japan_chemical_campaign_decisions.md) records the user's 20 September request accepting the two shared raid categories and native land delivery.
The [accepted CBRN amendment](../specs/chaos_warfare_system_specs/specs/13_2026_09_20_accepted_cbrn_overhaul.md) supplies the governing design basis.
The direct Japan decisions are recoverable from `33b6946dd^`; they were not reinstated against that acceptance.

`752e25a6ff5509bcedb28af435c745f57889d176` (25 September) removed `cbrn_nerve_suppression_sarin` and `cbrn_nerve_suppression_soman` and their occupation helper.
The parent decisions already required `cbrn_occupation_current_version_condition_hook_verified`, whose body was `always = no`, and a target risk flag with no setter.
Their complete payment/outcome definitions did not make them usable through the normal interface.
The [retirement handoff](chaos_warfare_system_plans/subagent_handoffs/2026-09-25_occupation_attack_retirement_documentation_cleanup.md) records user-approved removal of decision-based CBRN attacks under the native-only delivery direction.
These blocked definitions were not restored.

Disposition: historical July outage already replaced; Japan conversion and occupation retirement have recorded acceptance.
No remaining unambiguous chemical delivery omission was established.
Native engine cancellation/reservation behavior was not observed; source definitions alone do not prove it.

## Other raids within scope

`ff4adef81` (4 October 2026) introduces `common/raids/nuclear_raids.txt`; there is no earlier version of that mod file in the requested history window.
The complete predicate in `common/scripted_triggers/023_sov_nuclear_bombs_event_triggers.txt:38` requires SOV, AI control, and a valid active Event 23 actor/ledger with Chaos Meter enabled and no terminal world state.
The six `factor = 0` additions are at lines 18, 265, 442, 621, 880, and 1059 in the reviewed raid file.
After removing the exact four-line header and six identical added blocks and normalizing CRLF/LF, the remainder equals installed `common/raids/nuclear_raids.txt`.
Mod SHA-256 is `796ff56da41dee1d1cd6b8edfd397d56cad7a44cbb0af3f8efc6fa47ff9d2f78`; installed vanilla is `966408c81eba9f5928ed352d5f95f6648977b23a8e12ce9aa2cd2cdbca76256f`.
The independent weighted reviewer confirmed four named cases: active valid AI SOV has zero scores for these six raids; human SOV, inactive/invalid AI SOV, and non-SOV AI retain the vanilla scores from these modifiers.
These are AI score changes, not human availability gates or measured selection probabilities.
Disposition: preserve the new Event 23 AI-routing policy; no old mod-file version was invented as a restoration source.
`33b6946dd` introduces the chemical stockpile-doomsday native raid under the accepted native-delivery direction; `ccca51294` corrects its war-support engine read.
No earlier version of that native raid file exists before September; it was not rolled back into a deleted decision/operation flow.
Biological/zombie raid routes and scientist-owned portal raids were excluded with their assigned systems.

## Chemical state contamination and civilian protection

The March baseline `1b2cd634a4fbf130c6d5e1f02a2bb46d49c697fd` adds Air Cleanliness, condemnation, and Deaths to chemical consequences.
`e79ba516cc931963ed4f9b5667acd8a0ee4344b6` (14 July) adds the shared payload/protection/exposure pipeline and exact chemical state records.
Current `common/scripted_effects/cbrn_chemical_state_effects.txt` retains contamination modifiers and their atmospheric contribution through those records.
The architectural change was not evidence that contamination effects disappeared.

`d4a27b58facddf55def7f13dffb7de94eac3429` (15 August) replaces four individually targeted civilian protection decisions with timed country programs that distribute capital-first across eligible controlled states.
It removes independent state choice and concurrent per-state projects.
`33b6946dd` subsequently removes routine priority/full issue and filter programs from decisions and moves priority issue/filter replacement into automatic protection maintenance.
The accepted 20 September amendment explicitly states that military and civilian mask issue is automatic and debits actual stock.
The old 95% full-state issue decision has no current gameplay caller, while occupied-population distribution remains a separate paid program.
That old option is recoverable from `d4a27b58^` or its later program form from `33b6946dd^`; restoring it would require deciding to supplement the accepted automatic allocation model.

Disposition: retain the shared consequences and accepted automatic issue.
Needs the owner's decision: an optional manually selected full-coverage issue route alongside automatic maintenance.

## Cylinders and projectors

`d6abbc6fd0944d854b0c250d36712c5604852703` (31 August 2025) adds chemical facilities/research; `46cafaedc` (16 September 2025) adds the Livens designer.
The February 2026 baseline has the concrete cylinder/projector equipment and support roles.
Current `common/units/equipment/cylinders.txt`, `livens_projectors.txt`, and `common/units/livens_projector_support.txt` retain those families.

`067d392c13b19c72a07c61879384793aba7fe2db` deletes the 482-line `common/scripted_effects/chemical_livens_support_effects.txt`.
A search of its complete parent `common/` and `events/` trees finds definitions but no callers for `chem_livens_support_apply_state_dispersal` and the two combat-condemnation helpers.
The deleted file therefore does not establish an earlier working passive release path.
Current native projector-barrage raids consume projector hardware and matching payload and require a capable formation and target.
Commander abilities and original cylinder art are already recorded as restored under A13/A4 and were outside this audit's edits.

Disposition: no remaining clear equipment/projector mechanic deletion established.
Returning unused effect bodies would add code without demonstrating restored gameplay.

## Deaths accounting

The shared Deaths system starts in `1b2cd634a` (March 2026).
The pre-`b45c83d41` combat callback applies losses to each qualifying controlled/neighbor enemy-state context.
`b45c83d4184b9a0cb305815aa8284e8ca69af7a6` replaces that broad placement with a chance roll and one randomly selected eligible state.
`6c266388bf843948b7f7db9d3d05bb66926305ce` supersedes that restriction with weighted allocation across eligible enemy front states and changes rates, caps, and unit scaling.
For example, the fascist combat base share moves from `0.000140` to `0.000900` and the trigger chance from `0.55` to `0.98` in the April diff.
Current combat accounting uses multi-state weighted allocation, so the transient single-state restriction is not a remaining restoration target.

`0cfdf83c2` changes `apply_exact_state_civilian_population_loss` to remove population once, measure actual reduction, and register the measured loss without a second population mutation.
That correctness repair was preserved.
`4b443daf5`, `5b46c56be`, and `307fb945b` add event-specific cause attribution rather than deleting existing death records.
The Deaths-row spacing restoration is already recorded in `1fca4df6a7`.

Disposition: no complete Deaths recording path was shown to be missing.
Needs the owner's decision: the broad early combat-placement/rate model versus current weighted distribution and April tuning.
Exact comparison sources are `b45c83d41^` and `6c266388b^` for the effect/constant pair.

## Condemnation and sanctions

The direct early foreign response is `genocide_enact_sanctions` in `fa1322b37^:common/decisions/genocide_crisis_decisions.txt`.
Its helper `genocide_foreign_sanction_target` applies an opinion penalty, a hidden international-sanctions idea, and foreign pressure immediately.
`fa1322b373c084093e9291032cb96b9b4845f7d0` (10 July) removes that package and replaces it with source-aware condemnation, sanction-pair records, tiered enforcement, and compliance/defiance responses.
The exact historical package includes the old decision, helper, idea, and opinion modifier; copying only its decision would leave an incomplete restoration.

Current enforcer-side `condemnation_join_arms_embargo` and the strategic/total/pariah escalation actions still select a target directly and call `condemnation_apply_sanction_pair` after tier/cost checks.
Current target posture/compliance choices belong to the sanctioned country; they must not be counted as required clicks for the foreign enactor.
Later changes `76d2bc4a4`, `04f3ab38e`, `225b99688`, and `b78564999` centralize repeated scoring, align affordability, and bound/refresh inspection burden.
The Condemnation description/layout is already restored in `1fca4df6a7`.

Disposition: the July package is a changed sanctions model, not an established disappearance of all enforcement.
Needs the owner's decision: whether to restore the old immediate foreign-pressure action alongside, or instead of, the current source-aware sanctions.

## Air contamination, Air Winter, and treaty

The early atmospheric baseline is `1b2cd634a` (March 2026).
The five pressure tiers, escalation bands, and contamination consequences survive; later natural sources, Air Winter responses, treaty lifecycle, and source ledger expand this system.
`f564e3cdf` adds bounded natural sources; `fe10e92d9` adds deterministic Air Winter responses; `11c8553e9` adds the source-ledger UI.
Those additions were retained under the owner's rule for genuinely new mechanics.

`48255b6781aef430ac7e1fd332ba180fa2b0c491` moves the five pressure ideas from `country` to `hidden_ideas` while retaining their modifier values.
That is the owner-plan B7 spam fix, not removed pressure gameplay.
`182b1186c` keeps Air Winter active under Fallout's atmospheric lock; July shutdown guards prevent stale source writes rather than removing ordinary pollution.

Disposition: no remaining unambiguous atmospheric gameplay regression established.
Fallout's terminal handoff is discussed with scenarios below; no independent Fallout rewrite, biological source behavior, migration, or famine was implemented in this job.

## Camps

The older genocide/camp package grows into the Repression Ledger in `5713c362e` and the connected camp rework in `be6f9e53b`.
Camp Administration later adds site controls, priorities, mandates, budgets, development, and records.
This is substantial expansion; the historical existence of a decision alone does not prove it remained reachable after ownership moved into Administration.

`1d123f711` replaces fixed-date gates with campaign conditions and removes the managed-network visibility gate from country actions.
`1850d88c3` removes 74 decisions/missions and associated payloads; their actual prerequisite/caller history must be distinguished from the deletion count.
In its parent, `camp_rework_run_versioned_migration` iterates countries through `camp_rework_initialize_country_variables` and `camp_admin_initialize_country`, which sets `camp_admin_initialized`.
Consequently the legacy branches requiring `NOT camp_admin_initialized` are unreachable after that migration.
This proof does not settle separate `camp_admin_civil_initialized` checks or prove that those branches had never been reachable earlier.
`04c401937` and `15f851abb` add the Event 022 baseline and relief/retreat/closure behavior rather than stripping an earlier playable Event 022 system.

`630c655e1` redesigns `interface/camp_repression_ledger.gui` and adds meter presentation to `common/scripted_guis/camp_repression_ledger_scripted_gui.txt`.
Its scripted-GUI diff does not replace the button click effects; the new properties are meter frames and visibility checks.
The source defect behind the owner's B9 report was introduced in `3098ed9d2`: the Administration display array stored `THIS.id` instead of the actual State scope.
The separate C1/B9 job repairs that token in `4b0967bd7ad2d8386a2ec137146af8b0cd225ad5` and documents an independent 63-button source audit in [its current report](chaos_redux_load_camps_repair_2026-10-13.md).
This historical audit preserves that repair and does not claim live button execution or an original-layout rollback as evidence for it.
Concurrent edits to the camp UI effects/triggers were preserved.

The final chronology establishes the source loss rather than accepting the cleanup commit's explanation:

- `5713c362e` (11 July) introduces the versioned startup migration's country pass and country-variable initializer.
  Its actual tree has no `camp_admin_initialized` setter or `camp_admin_initialize_country` reference; those Administration definitions are later additions.
- `be6f9e53b` (11 July, descendant of that core commit) adds `fr_inspect_camp_legacy`, `fr_close_camp_legacy_sites`, `bel_open_international_inspection`, and `bel_reform_concession_system` without the later initialization exclusions.
  They have focus/government/pressure/site requirements and inspection/closure/concession outcomes.
  Their player visibility follows the managed-network toggle then provided in `camp_repression_generic_decisions.txt`.
- `3098ed9d2` adds `camp_admin_initialize_country` and its general initialization flag, plus the civil-initialization exclusion before the civil setter exists.
  The civil exclusion alone is inert at that point.
- `72aa7ba56` adds the general initialization exclusions and the supported-country civil initializer, including France/Vichy and Belgium.
  The four actions become hidden under the migration/initialization path here.
- `1d123f711` removes the managed-network toggle gate but retains the initialization exclusions, so it does not reopen them.
- `1850d88c3` deletes the decisions and `camp_rework_update_colonial_country_monthly_bridge` together.
  The bridge was not removed by an earlier separate commit; its old calls/outcomes are in that commit's parent.

Current GUI country-action slots dispatch generic civil-policy/review handlers; they do not call the four named legacy routes or preserve their specific inspection/concession flags.
Needs the owner's decision: revive those direct named outcomes and their retired bridge alongside the current civil model, or retain their replacement by generic Administration actions.
An exact restoration would need the pre-gate decision definitions from `72aa7ba56^` and the corresponding pre-deletion bridge/outcome dependencies from `1850d88c3^`; simply returning the latter decisions would keep their dead initialization gates.
No partial or rewritten route was substituted.
No camp source or current repair was overwritten.

## Chaos Meter

The August 2025 meter already has six tiers at 0/200/400/600/800/1000, world tension, war/peace, territory/factions, ideology, military build-up, stability/democracy, monthly decay, and a final-tier lock.
`574028528` centralizes tuning without replacing those mechanics; `1b2cd634a` adds attributable history, Deaths, and Air Cleanliness.
Most of the early meter remains present.

- `e9946ac166bcaa82c163695e92f775724879c125` changes territorial/nuclear/faction values and comments out the civil-war helper.
  The whole parent-tree caller search finds only its definition, so no reachable civil-war hook was established.
- `d6abbc6fd0944d854b0c250d36712c5604852703` disables the active war-justification pulse.
  `1b2cd634a` disables the major-election contribution (-1) explicitly and replaces the direct 250k military-casualty contribution with integrated Deaths accounting.
- `6c266388b` restricts ruling-party contributions to crossings of the democratic boundary.
  A fascist-to-communist change ceases to contribute; a change into/out of democracy still does.
- `937943904fb5bda4fcffe22eaa33b6c59df7f011` excludes faction follow-up relations and caps an actor's same-day minor declarations at +5.
  Seven independent eligible minor declarations yield +5 rather than +7; an independent major declaration remains +5.
- `76d2bc4a48e06ae24beb7023b5aaac8bd195d6fd` deletes mobilization, generic-coup, faction-disband, and already-disabled election helpers.
  Its complete parent-tree searches find no callers for the first three; the staged/successful coup hooks survive.
- `76bfc2885`, `400501400`, and `aa1435e5c` add a diminishing nuclear ladder and distinguish Event 23 tests/accidents/demonstrations.
  `21e812c8e`, `480b47bff`, and `e2dc84c0c` add missile and UI-wear integration.
  Those genuinely new integrations were retained.

Disposition: no missing core meter mechanic was established that can be restored without a balance choice or recreating an unconnected helper.
Needs the owner's decision: justification pulses, election relief, broader ideology contributions, early territorial value reductions, the minor-war cap, and direct military-casualty scaling.
Exact old bodies are in the respective offending commit's parent, using `common/scripted_effects/chaosx_chaos_meter_effects.txt` before the November rename and `chaos_meter_effects.txt` afterward.
The earlier history alignment restoration `1fca4df6a7` was preserved.

## Event selection and timers

The August–November 2025 baseline (`e9946ac16`, `aa371107e`) already uses per-country timers and weighted selection inside `common/on_actions/chaosx_on_actions_system.txt`.
The March refactor moves the weighted pool and eligibility into `common/scripted_effects/chaosx_logic_effects.txt`; it retains the timer-triggered model.

`0b0ddd625` adds pool-sensitive dynamic major-weight gain instead of a flat configured gain.
`2ba683add` adds per-event Chaos-level gates; White Peace's default becomes tier 1 and other event defaults remain tier 0.
`291990433` clarifies recovery-rate wording; its parent already uses `global.minor_event_recovery_rate`, so the commit is not a behavioral regression.
`44748907a` counts synchronous clustered majors as major pacing; `292847723` carries that accounting across the delayed Acid Rain batch once.

Disposition: no missing earlier direct timer/selection route established.
New per-event Chaos-level configuration was preserved.
Needs the owner's decision: pool-sensitive major gain and major-containing cluster pacing versus their earlier behavior.

## Event clusters

The initial system `e87fb80e0` (8 May 2026) provides definitions, ordered members, eligibility, and required/optional participation.
The compact pre-overhaul constants at `4c1513475^` have required 100%, default optional 50%, and high/medium/low 85/60/35 participation values plus member overrides.

`4c1513475` (28 August) replaces that model with severity/tier participation, activation factors, eligible-member count, fatigue, memory, bounds, and aligned queue/history metadata.
`8aa811ce2` adds ordering and multiple memberships.
The old member set (Random War, Soviet Collapse, Liberations, Fury, Africa, Plague, Natural Disasters, Random Faction, Resources, Tensions, White Peace, Zombies) is contained in the current registry.
No former member was established as missing.
`e6d856be3` limits ordinary cluster rolls to automatic firing while preserving separate manual activation.
The layout restores `360245b7ff` and `13aea99060` were preserved.

Disposition: a real probability-model replacement and complexity increase, with no demonstrated missing member/manual trigger.
Needs the owner's decision: return to the compact pre-`4c1513475` probability model while retaining later memberships, context, and queue repairs.
The paired old sources are `common/script_constants/event_cluster_constants.txt` and `common/scripted_effects/chaosx_event_cluster_effects.txt` in that commit's parent.

## Triggerable scenarios

The initial `e87fb80e0` scenario routes 1 and 2 survive.
Current source IDs are 1–3, 5–16, and 19; shared ID 4 is the retired Final Silence alias, 17 remains reserved, and 18 is unregistered.
`584ccd486` introduces the original Final Silence manual route.

`3b5312c87314fe9db94e5dfa2e19b619f4679e3d` replaces its registry row/type controls and direct helper with Fallout, including redirection of legacy selectors/callers.
Its parent holds the exact original manual helper, selectors, report event, and registry entries.
The old helper invokes Holy Realm prepare/wave effects that the same Fallout change also alters; copying only the launcher would not recover its old terminal behavior.
The [Holy Realm decision log](003_holy_realm_plans/agent_decisions_2026-10-05.md#accepted-release-qa-follow-up---2026-10-06) records parent acceptance of the terminal Fallout handoff under the user's October release-QA/G6 direction.
The separate manual Final Silence row/type retirement lacks an equally specific acceptance record in the inspected evidence.
It remains an owner decision about restoring an independent old terminal scenario alongside the accepted Fallout consequence, not an isolated safe launcher repair.

`10b7f5e3c` repairs the Soviet Collapse scenario suppression that removed its event ID from the fire-once type registry.
Current code keeps the registry entry and marks it fired/disabled, so that known regression is already fixed.
Scenario intensity/confirmation features accompany the original expanding manual framework; no earlier general launch route was shown to be replaced by them.

Disposition: retain the prior registry repair and genuinely new scenario packages.
Needs the owner's decision: independent Final Silence manual scenario and nuclear/thermonuclear type selector, with the complete pre-`3b5312c87` dependencies rather than a partial helper copy.

## Weighted checks, evidence limits, and commits

The independent weighted reviewer compared exact parent sources at `4c1513475^` and `0b0ddd625^` with the current cluster/selection helpers and constants.
No balance change was applied.

| Declared scenario | Earlier source | Current source | Meaning |
| --- | --- | --- | --- |
| Wars/Event 004, tier 1, exactly trigger + Fury eligible, fatigue 0, prior optional participation 20% | Cluster activation 10%; Fury participation 70% | Activation 25%; Fury participation 52% | Conditional per-cluster/per-member rolls, not share of all competing clusters |
| Same Wars scenario, fatigue 0/1/2/3/4 | Activation remains 10% | Activation 25/22/20/18/16% | Bounded fatigue sensitivity under fixed eligibility; current activation floor is 1% |
| Three minor updates, stable 10 majors/90 non-majors, baseline gain 150 | Each applicable major score 450 | Each active major score 450 | Baseline score matches |
| Three minor updates, stable 5 majors/90 non-majors | Score 450 per applicable major | Score 900 per active major | Inverse active-pool scaling; score only |
| Three minor updates, stable 20 majors/90 non-majors | Score 450 per applicable major | Score 225 per active major | Inverse active-pool scaling; score only |

Current Wars activation arithmetic is `round(10 × 1.35 × 1.30 × 1.00 × 1.40) = 25`; Fury uses `round(40 × 1.30) = 52` before optional-row decay.
The major gain is `baseline_gain × active_non_major / active_major × baseline_major / baseline_non_major`, rounded and settings-clamped.
These cases assume the declared gates pass and candidate counts stay fixed; campaign probabilities require the full live pool and weights.
Current major gain also reaches only currently eligible majors, whereas the earlier helper assigned accumulated minor progress to all unfired majors.
Needs the owner's decision: whether a major becoming eligible late should receive earlier minor-event progress.

The probability-inspect source request exceeded the reviewer's 150-second bound and returned no result; its one follow-up was rejected because `source.id` is unsupported.
No MCP probability artifact or render was obtained.
The results above are source-derived calculations, not a passed MCP analysis or observed game behavior.
The shared retry allowance for that attempted inspection is exhausted; a supported selector/full pool description would justify another check.
The reviewer found no definite broken selection in these scenarios.

Reviewed source SHA-256 identities: cluster effects `6B25B6B55DF733550FEF571BE69BBC64721248ED06F72AF430B759B1F5DE6781`, cluster constants `8D8CA9CD157E4FDD4FB5AF8FD76882C326C6466FDEACB79CC27574147D7F0445`, selection effects `B52E681C3FAA219F3A85F99B5D3ED38A0FF8F3750BF6197F3176C6C492E0D765`, and event constants `0BCD35CF6C7363B37DD89C6B49A0C3353B967C46131FB7AD5CBF6FF171726272`.
The calculation receipts describe those source identities; they do not certify later concurrent changes.
No HOI4 launch, live test, log search, push, gameplay/localisation/art edit, or out-of-scope system implementation occurred.
The audit distinguishes historical source behavior from engine observation.
Concurrent changes to shared meter, event-system, camp, condemnation, and localisation files were left intact.
The reported historical baseline is committed source, not a certification of those other agents' pending edits.

Reference discovery/read routes were exposed and used without web access to the Paradox Wiki.
The narrow flag references actually read were installed `documentation/effects_documentation.md:7085–7093`, revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`, and offline `paradox_wiki/Effects - Hearts of Iron 4 Wiki.md:352`, revision `997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c`.
These excerpts are not comprehensive syntax validation for the audited systems; no engine-facing source was edited.

Skills used: `chaos-redux-subagents`, `chaos-redux-shared-git-commit`, `chaos-redux-ideas-modifiers`, and the delegated event/weighted reviewers' `chaos-redux-events` and `chaos-redux-ai-strategies` guidance.
No skill was created or changed.
Publication uses a temporary index, exact owned content, compare-and-swap `update-ref`, and path-specific real-index reconciliation.
The owner plan has no existing line for the overall mass systems audit; its registration is one new job-owned `C-SYSTEMS-AUDIT` line with the audit commit hash, preserving every other item line.
No separate gameplay restoration commit is claimed: every source change identified as currently outstanding is recorded as an unresolved owner decision above.
The incoming C2 timer-pressure call was identified in the final committed-source comparison and preserved as another job's implementation; it does not alter the recorded cluster/major-gain arithmetic.
