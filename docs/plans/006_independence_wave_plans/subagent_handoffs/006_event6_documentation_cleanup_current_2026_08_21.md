# Event 006 documentation cleanup handoff — 2026-08-21

## Disposition

This was a documentation-only reconciliation of the four stale wording items named by the current Event 006 completion audit.

No gameplay, localisation, asset, spreadsheet, generated `.qoder`, or runtime source file was edited.

The accepted Event 006 design remains authoritative, and the whole-event disposition remains **HOLD / PARTIAL**.

## Files changed

- `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md`
- `docs/events/006_independence_wave/far_eastern_republic_package.md`
- `docs/specs/006_independence_wave_specs/quality/simplifications_omissions_and_blockers.md`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_documentation_cleanup_current_2026_08_21.md`

## Before and after authority

| Surface | Before | After |
| --- | --- | --- |
| Pre-event crisis wording | The source-of-truth map told the parent to preserve a crisis queue sentence. | The map records only the current `3/4/5/7/10` ladder and reconciled `Events!C7` wording; the retired no-pre-event crisis surface is not preserved as a current requirement. |
| NAV/GLC `.350` checkpoint | The map said `chaosx.nr6.350` recruited the NAV and GLC commanders. | The map describes `.350` as a synchronous checkpoint that validates the pre-defined package rosters and writes package checkpoint flags; setup promotes a passed checkpoint to shared readiness, and the checkpoint does not recruit either commander. |
| FER anchor authority | The map and FER package doc foregrounded dormant capital state 563 before the ordered runtime anchors. | Both documents foreground the exact ordered available runtime anchors 408 and 409 and selected-anchor setup readiness. |
| Package-local versus central admission | The quality report described IW-057 as outside gameplay and separately mentioned only IW-051/IW-052 package-local work. | The quality report identifies package-local implementation evidence for IW-057, IW-051, IW-052, IW-053, IW-054, and IW-060 while keeping all six outside central runtime admission and package-count authority until their named gates close. |

## Source-of-truth map

The accepted Event 006 specifications remain the design authority.

The current Event 006 completion audit dated 2026-08-20 is the implementation-status evidence for this cleanup.

The source-of-truth map remains the routing ledger, and the FER package document remains the package-local runtime-authority summary.

The quality report records package-local implementation evidence separately from central attestation, preflight, deterministic Join, and package-count authority.

## Plan and handoff dispositions

| Item | Disposition |
| --- | --- |
| Retired pre-event crisis wording in the source-of-truth map | Corrected in place; no gameplay request remains queued. |
| NAV/GLC `.350` wording in the source-of-truth map | Corrected in place; the existing command-roster handoff remains evidence for the package-specific roster contract. |
| FER capital wording in the source-of-truth map and FER package doc | Corrected in place; the existing FER preflight and package handoffs remain evidence for the selected-anchor gate and unresolved admission receipts. |
| IW-057/IW-051/IW-052/IW-053/IW-054/IW-060 classification in the quality report | Corrected in place; all six remain package-local and fail-closed rather than promoted. |

## Contradictions, duplicates, and stale instructions

The four named contradictions are resolved in the three edited documents.

No duplicate document was merged or deleted, and no superseded notice was added because the stale claims were isolated wording in current authority documents rather than duplicate artifacts.

No prompt or instruction file was in the requested cleanup scope, so no stale prompt was changed.

Other audit-listed stale references in the resume packet and older plans remain intentionally out of scope for this bounded pass.

## Markdown hard-wrap audit

The changed prose remains on complete physical sentence lines, and no deliberate Markdown structure was flattened.

No unrelated historical hard-wraps were rewritten because the parent limited this pass to the four named authority corrections.

## Parent decisions

No new parent design decision is required for these wording corrections.

The parent still owns all six package-local identity, map/origin, rights/asset, roster/force, typed-probability, and central-admission decisions.

## Validation

- `rg` confirms the target source-of-truth map no longer contains `crisis queue sentence`, `563`, or a `.350` recruitment claim for the NAV/GLC commander IDs.
- `rg` confirms the FER package document no longer contains `563` and retains the ordered `408`/`409` anchor wording.
- `rg` confirms the quality report explicitly classifies IW-057, IW-051, IW-052, IW-053, IW-054, and IW-060 as package-local while retaining central-admission blockers.
- Targeted source evidence confirms `chaosx.nr6.350` invokes `independence_wave_apply_roster_checkpoint`, whose current helper documentation describes package checkpoint flags without character creation or country release.
- `git diff --check` was run against the three edited documentation files.
- The working-tree scope check shows only the three named documents and this handoff were changed by this cleanup; unrelated existing handoffs were preserved.

The current 2026-08-20 completion audit and the named package handoffs remain the evidence basis for the reconciled wording.

The matching HOI4 MCP event/map routes were not callable in this subagent context during the fresh check (`hoi4_event_inspect` and `hoi4_map_inspect` were absent from the callable tool inventory on retry), so no new MCP artifact is claimed here; the existing audit artifacts remain evidence rather than a replacement source of truth.

## Remaining blockers and scope notes

- Event 006 remains **HOLD / PARTIAL** at the current 32 content-attested packages across 29 compatible reservation groups, 161 unattested selectable rows, and 40 runtime adapters.
- IW-057, IW-051, IW-052, IW-053, IW-054, and IW-060 remain package-local and fail-closed, with identity, map/origin, rights/asset, roster/force, typed-probability, or related central-admission gates still owned by the parent and their package auditors.
- No package was promoted, no feature was marked complete, and no live or in-game validation claim was made.
- Other stale audit findings, including older plan/addendum wording and the resume packet's separate `.350` or parent-list references, were intentionally left unchanged because the parent limited this cleanup to the four named wording items.
- No commit was created, per the parent instruction.
