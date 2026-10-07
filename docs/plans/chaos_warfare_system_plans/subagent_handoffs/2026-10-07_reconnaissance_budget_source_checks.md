# Reconnaissance correction source checks

Disposition: implemented bounded source audit, reviewed and rerun by the parent with 221 checks passing; native reconnaissance semantics remain unresolved.
Acceptance basis: the parent accepted the allocation in `2026-10-07_reconnaissance_budget_review.md` and confirmed that the five numerical source changes and five shared mirrors were applied and frozen before this final execution.
The parent owns gameplay, MCP inspection/render/comparison, integration, and the commit.

## Changed artifacts and final execution

- Updated `docs/testing/2026-10-07_doctrine_reward_budget_source_tests.js` using its existing bounded parser.
- Regenerated `docs/testing/2026-10-07_doctrine_reward_budget_source_results.json` after the parent's source freeze.
- Added this handoff.

Command from the mod root:

```powershell
node docs/testing/2026-10-07_doctrine_reward_budget_source_tests.js
```

The final run at `2026-10-07T13:07:16.737Z` exited 0 with 221 passing checks and `passed_with_native_semantics_unresolved`.
The 137-check original revision coverage remains present, including all 65 retained-unit soft attack, hard attack, breakthrough, defense, and organization rows.
The original technology AST comparison now permits the original two breakthrough constants plus the three accepted secondary weather constants.
No other original protection was removed.
The historical `2026-10-07_doctrine_reward_budget_source_checks.md` handoff was not edited.

The JSON's `reconnaissanceEvidence` records all contributing source values, all 64 source subsets, both real reconnaissance company bases, before failures, revised results, the failing fractional countermodel, and the utility-recipient inventory.
Its existing `sourceHashes` and `referenceSections` retain exact source revisions and cited local paths and line spans.

## Exact source preservation

The three byte-exact secondary baseline files match every hash in `docs/testing/2026-10-07_reconnaissance_budget_review/baseline_manifest.json`.
The manifest records baseline commit `a92b35182e156822312670df7afdee7fe3ed4265`.
The current HQ AST matches that baseline after changing only `@CBRN_HQ_OPERATIONS_RECON` from 0.15 to 0.04 and `@CBRN_HQ_MEDICAL_RECON` from 0.10 to 0.02.
This comparison preserves all role IDs, categories, enabled ability IDs, manpower, equipment needs, deployment costs, training, supply, transport, planning, wounds, and sickness fields.
Operations HQ planning remains 0.05, and Medical HQ wounded/sickness factors remain -0.30 each.

The technology AST matches the secondary baseline after changing only `@CBRN_WEATHER_RECON_BASIC`, `IMPROVED`, and `ADVANCED` from 0.20/0.40/0.60 to 0.01/0.02/0.03.
All hidden grants, research costs, dates, equipment unlocks, AI, and other source fields remain equal.
The shared table matches the secondary baseline after removing only the five newly added reconnaissance mirror keys.
Each of those five keys agrees with its actual file-local constant.
No shared constant token was substituted into a native database field.
The unchanged four-doctrine comparisons preserve mastery IDs and rosters, effects, unlock flags, thresholds, XP costs, and AI.

| Current engine-facing source | Final audited SHA-256 |
| --- | --- |
| `common/units/cbrn_hq_support.txt` | `16c9ec2933911e116422fcd08b7f133753db2919816d6f923e1a378ec6982ca6` |
| `common/technologies/chaosx_technologies.txt` | `d52d48eb5796c120e5bd465dddcd5527a6597f7a60cf68f871c6240d05b1f5c1` |
| `common/script_constants/cbrn_doctrine_constants.txt` | `125542877243eba1fa24706057fa163edcde5f38ec7bcd54b24c778c5b7a18ed` |

The external ability source bodies were not part of the three-file secondary snapshot.
Their independent pre/post body equality is therefore not claimed by this audit.
The parent freeze states those bodies were untouched, and exact HQ AST equality proves preservation of their enabled IDs and role consumers.

## Recipients and source combinations

Chemical Reconnaissance Detachment retains authored reconnaissance 4 and is the sole retained member of `category_cbrn_reconnaissance`.
It also retains the ordinary `category_recon` membership.
Field Medical Support retains authored reconnaissance 2 and belongs to neither category.
It receives no weather grant through those memberships.
The only controlled country reconnaissance factor remains Integrated Command adoption at 0.25.

The three exact weather nodes are `portable_anemometer`, `meteorological_stations`, and `upper_air_soundings`.
Their existing instrument research consumers still grant them, so all three can accumulate.
The HQ role predicates expect all three sections on a leader and the Operations/Medical definitions have separate IDs, HQ-only eligibility, and no authored shared support-type lock.
The source model permits one equipped Operations and one equipped Medical section in the same command.
It does not manufacture duplicate HQ instances or infer native commander accumulation from source compatibility alone.

The 64 combinations cover all eight weather subsets, adoption present/absent, and all four HQ subsets.
Every combination checks both the base-4 reconnaissance company and base-2 medical company, using pooled weather points with pooled HQ factors, pooled weather points with independent HQ factors, and each weather point independently normalized by the unchanged company base.
Forty-one before subsets exceed 1.35 in at least one of the reviewed guards, and zero revised subsets do.
The same country/HQ-only upper bound is recorded for all thirteen retained utility recipients.
Entries with zero authored reconnaissance are explicitly nominal, with no claim that a percentage creates a useful reconnaissance stat.

| Full legal source combination under the flat-point interpretation | Before factor | Revised factor |
| --- | ---: | ---: |
| Recon, pooled weather and pooled HQ | 2.03125 | 1.344875 |
| Recon, pooled weather and independent HQ | 2.055625 | 1.34589 |
| Recon, independent normalized weather points and independent HQ | 2.1002953125 | 1.3459812868125 |
| Field Medical, country and pooled HQ | 1.5625 | 1.325 |
| Field Medical, country and independent HQ | 1.58125 | 1.326 |

The preferred revised bound is `(4 + 0.01 + 0.02 + 0.03) / 4 * 1.25 * 1.04 * 1.02 = 1.34589`, or +34.589%.
The independent normalized-point guard is `1.0025 * 1.005 * 1.0075 * 1.25 * 1.04 * 1.02 = 1.3459812868125`, or +34.59812868125%.
Field Medical's unchanged base 2 gives modeled input `2 * 1.326 = 2.652`, or +32.6%.
The before adoption-plus-Operations, adoption-plus-Medical, and adoption-plus-both-HQ combinations all reproduce failures even with no weather grant.

## Uncertainty and completion limits

These are source arithmetic bounds under the parent's accepted flat-point interpretation, rather than native +35% proof.
If technology `recon` behaves as a fractional stat modifier, the revised allocation gives `1.06 * 1.25 * 1.04 * 1.02 = 1.40556`, exceeding 1.35.
The test explicitly preserves that failing countermodel.
The result must not be described as passing every possible native interpretation.

The local reference evidence includes installed `modifiers_documentation.md:4537-4541`, offline `Modifiers:971-974`, offline `Unit modding:308-318`, vanilla `common/units/hq_support.txt:112-146`, and vanilla `common/technologies/support.txt:536-544`.
The generic offline Technology modding rule at line 105 calls unit modifiers multiplicative without documenting the reconnaissance exception.
Vanilla source precedents and the accepted owner interpretation support the point model but do not settle that exception.
Native deployed-leader accumulation, equipment fill scaling, duplicate sections, field-marshal propagation, several companies' division reconnaissance, and resulting tactic advantage remain unresolved.

Ordinary vanilla reconnaissance research, vanilla HQ Recon, commanders, and other event modifiers remain an equal baseline on both sides.
They were neither removed nor charged again against this controlled CBRN benefit.
The audit does not prove every legally buildable division, variant, or external event combination.

No MCP call was made by this worker for the follow-up.
The parent owns the exact technology inspect/render/compare evidence and reported partial generated analysis with no numeric bonus coverage for the before `portable_anemometer` render.
Those findings are not native accumulation evidence.
No game was launched and no logs were searched.

No gameplay, shared documentation, index, AI, helper, or other worker file was edited by this worker.
No fallback or hidden source simplification was implemented.
The five secondary numerical reductions are explicit parent-authored budget reallocation, not an unchanged lifetime consolidation.
This report completes the assigned source checks and makes no whole-package completion claim.
Skills applied remain `chaos-redux-events` and `chaos-redux-subagents`, with no skill changes.
