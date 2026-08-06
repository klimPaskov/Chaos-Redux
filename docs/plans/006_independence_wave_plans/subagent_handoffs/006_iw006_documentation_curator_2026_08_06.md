# IW-006 documentation curator handoff — 2026-08-06

Documentation reconciliation is complete for the Event 006 package-admission scope named by the parent; no gameplay, localisation, asset, spreadsheet, or source-spec design file was changed.

## Source-of-truth map

| Surface | Current authority | Reconciled state |
|---|---|---|
| Package arithmetic | `docs/specs/006_independence_wave_specs/quality/package_manifest.md`, the current amendment in `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md`, and the current sections of `docs/events/006_independence_wave/overview.md` and `006_independence_wave_resume_packet.md` | 22 content-attested selectable packages across 21 compatible reservation groups, 171 unattested selectable rows, and 32 central adapters. The exact current IDs are IW-001, IW-002, IW-004, IW-006, IW-007, IW-008, IW-009, IW-010, IW-012, IW-014, IW-017, IW-018, IW-019, IW-023, IW-029, IW-033, IW-041, IW-070, IW-071, IW-072, IW-173, and IW-184. |
| Adapter-only boundary | Package manifest and current source-of-truth/resume sections | Ten fail-closed adapter-only IDs remain IW-013 NAV, IW-015 GLC, IW-026 MAC, IW-030 MNT, IW-043 CHU, IW-058 ASY, IW-093 DOX, IW-098 SOK, IW-177 FIJ, and IW-179 FSM. |
| IW-029 Bosnia | `subagent_handoffs/006_iw029_bosnia_country_package_audit_2026_08_06.md` plus the current amendment in the source-of-truth map | BOS is admitted on states 104 and 804 in RG-104 with YUG preserved as former host, and all three fixed setup/runtime proofs require `tag = YUG`. The only remaining BOS package evidence blocker is the MCP `ai_strategy_factor` result `PROBABILITY_SURFACE_EMPTY` for `common/ai_strategy/006_independence_wave_bosnia.txt`. |
| Ordinary super-events | The current super-event override in the source-of-truth map, overview, and resume packet | Runtime/display identifiers are ordinary `23` for The League of New States and `24` for Every Border a Casus Belli. Four-digit `6001`/`6002` labels are retained only in dated traceability. |

## Plan and handoff dispositions

| Plan or handoff | Disposition | Reason |
|---|---|---|
| IW-029 Bosnia package audit | Source-promoted for the current 22/21/171 boundary, with admission still HOLD / fail-closed | The package evidence is present and the YUG former-host contract is explicit, but the required weighted-logic adapter returned `PROBABILITY_SURFACE_EMPTY`. |
| IW-033/IW-041 package-admission amendment | Historical and superseded for arithmetic by the IW-029 current amendment | Its 21/20/172 snapshot remains useful traceability and is not a competing current count. |
| CAT and Transcaucasus admission snapshots | Historical and superseded for arithmetic | Their dated 16/15 and 19/18 boundaries remain bounded evidence only. |
| Static 20-package capacity witness | Retained as static witness evidence | It does not replace the current 22-package attestation boundary or prove live host, collision, transaction, formable, or save/load behavior. |
| Other Event 006 plans | Left unchanged | This pass was limited to current counts, the BOS YUG assertion, ordinary super-event IDs, and documentation cross-references. |

## Contradictions resolved

- Current authority sentences that still said 21/20/172 now state 22/21/171, and current 31-adapter wording now states 32 adapters.
- Current exact-ID lists now include IW-029 BOS and preserve the ten adapter-only IDs without changing any runtime IDs.
- Current BOS wording no longer leaves the former host implicit or ROOT-scoped; it records the required `tag = YUG` assertion in all three proofs.
- Current super-event wording consistently uses ordinary IDs 23 and 24, while four-digit historical labels are explicitly dated traceability.

## Open contradictions and risks

- IW-029 remains package-evidence HOLD / fail-closed until the `ai_strategy_factor` adapter can discover the Bosnia weighted surface or a supported adapter is supplied; no quantitative BOS AI claim is made.
- Event 006 remains **HOLD / PARTIAL**; this documentation pass does not claim whole-event completion.
- Historical 21/20/172, 31-adapter, and older super-event references remain intentionally visible inside dated sections for traceability and are not current authority.
- Shared MCP limitations remain evidence boundaries rather than new BOS blockers: Event lint returned `EVENT_INSPECTED_PARTIAL` with zero blocking diagnostics but deferred large-workspace projections; focus inspection returned `FOCUS_INSPECTED` with shared missing-icon/layout diagnostics; map inspection returned `MAP_INSPECTED` with unrelated global `MAP_BUILDING_POSITION_INVALID` and `MAP_PORT_ADJACENT_SEA_INVALID` diagnostics; GUI inspection returned `GUI_INSPECTED` but the global graph still has unrelated blocking context diagnostics and overlap findings. The Technology Tree Viewer remains unavailable as recorded by the Bosnia handoff.

## Duplicate, superseded, and stale-document review

- No duplicate current authority document was found inside the named scope; the current source-of-truth amendment and current resume/overview sections are the canonical routing points.
- The historical IW-033/IW-041 amendment section in `006_source_of_truth_map.md`, older CAT and Transcaucasus arithmetic, and earlier 21-package paragraphs in the overview/resume packet are retained with historical or superseded wording rather than deleted.
- No stale prompt or instruction file was named or found in the reconciliation scope; older dated terminology is traceability, not an instruction to repeat work.

## Markdown and validation notes

- The named Markdown files were checked for accidental prose hard-wraps; none were found, and deliberate headings, tables, lists, block quotes, and code/path lines were preserved.
- Targeted `rg` checks covered the current counts, exact ID set, `tag = YUG`, `PROBABILITY_SURFACE_EMPTY`, and ordinary super-event IDs 23/24 across the reconciled files.
- `git diff --check` was run against the five pre-existing named documentation files and this handoff after patching.
- Read-only MCP evidence used for this reconciliation includes Event 006 root/checkpoint lint resources `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a47195f4e1d41547d15b635b095b537b07350e302e226bd34df178da9b26daee/4e80cb675cb39ec8d1126be96d178fdc33496b6dbf09d5aef6d252766017708d/event-lint-be8a459e7129.json` and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8d911511f5ba05071c2d7f52e49051e924f924cccd11b866d3c5d6f812869db7/a3d3c637c6d5f9221ec3a08fb6043eb7e3c7e19cec11089f8cdcfd4a857fa3bf/event-lint-be8a459e7129.json` (`EVENT_INSPECTED_PARTIAL`), focus resource `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7f75c782d62543e109c40ddc23db362664e4219bd57220f1327d44114d61c902/06ee5e9d5fd2429b54b9a7b32c2417e2f9fdbdfbf440a20e58b37b2cdf37d604/focus-inspect.189e5ba5b4a5dec8.json` (`FOCUS_INSPECTED`), map resource `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7a1f85c08fc487192e39673c54c476cfbe09659e3d19bb8575470884b3309591/355a9e9025b7dc5151950f33c72a42a77ab2a5fffc38c534e2ce097c287143d9/map-inspect.181a16b4b11bb771.json` (`MAP_INSPECTED`), GUI resource `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ca807cfe2558a7a1da8b16b35aeb9e45fca9c32ad7e5eb755725872009116e14/037f5acb081ea635305ee548808f05d11d4b2c90153f39520483d32a9528d993/gui-inspect.4bf11e0423f2e383.json` (`GUI_INSPECTED`), and the BOS probability attempt (`PROBABILITY_SURFACE_EMPTY`, no artifact). These are evidence receipts, not replacements for the accepted source documents.
- Full runtime execution, Technology Tree Viewer inspection, live save/load observation, and gameplay validation were not repeated because the parent limited this pass to documentation and the existing handoff records the unavailable or out-of-scope routes.

## Parent handoff

Use the current sections of the package manifest, source-of-truth map, overview, and resume packet as the 2026-08-06 authority for the 22/21/171 and 32/10 boundaries and ordinary super-event IDs 23/24. Keep the IW-029 package on HOLD / fail-closed only for the documented `PROBABILITY_SURFACE_EMPTY` evidence blocker, preserve YUG in all future BOS setup/runtime proofs, and do not promote historical arithmetic or claim whole-event completion without a later owner review.
