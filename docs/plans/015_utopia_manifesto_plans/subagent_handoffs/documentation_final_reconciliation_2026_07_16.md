# Event 015 Documentation Final Reconciliation

Date: 2026-07-16  
Role: `chaosx_documentation_curator`  
Mode: documentation-only final reconciliation  
Audited event: 015 - Utopia Manifesto  
Documentation verdict: **PASS, no documentation blocker**

## Completion boundary

This report reconciles the canonical Event 15 documentation to the post-Ledger implementation and audit evidence. It is not the final whole-event completion audit. Event 15 remains incomplete until a new final read-only completion auditor passes the fully reconciled package.

No gameplay, localisation, interface, visual asset, audio, workbook, spreadsheet, binary, tool, or skill file was edited by this curator. The asset auditor owns the Event 15 asset manifest, GFX handoff, animation handoff, coverage crosswalk, and final asset report. The localisation auditor owns the fresh localisation report.

## Source-of-truth map

Use this order when records disagree:

1. Live HOI4 sources are authoritative for runtime behavior and identifiers.
2. `docs/events/015_utopia_manifesto/overview.md` is the canonical current mechanic description.
3. Accepted specifications under `docs/specs/015_utopia_manifesto_specs/specs/` are the design authority.
4. `docs/specs/015_utopia_manifesto_specs/matrices/completion_coverage_matrix.md` is the current proof and gate matrix.
5. `docs/assets/015_utopia_manifesto/manifest.md`, `gfx_handoff.md`, `icon_animation_handoff.md`, and `requirement_to_runtime_coverage_2026_07_16.md` are the asset authority owned by the asset auditor.
6. This report and `015_utopia_manifesto_source_of_truth_and_resume_2026_07_15.md` record the current documentation and resume state.
7. Dated audits remain evidence only for their inspected snapshots. Later dispositions do not rewrite their findings.
8. Dated implementation handoffs, prompts, and superseded plans remain provenance rather than current authority.

## Frozen current facts

| Surface | Reconciled fact |
| --- | --- |
| Events | 99 definitions |
| National focuses | 124 |
| Decisions and missions | 121 decisions, 43 missions, 9 categories |
| Ideas | 50 |
| Characters | 24 total. Eight institutional founder or successor entries share four people-free built-in ImageGen institutional tableaux. Sixteen advisors use distinct ImageGen portrait masters processed into HOI4 dossier cards |
| Advisor processing | The processor only crops, grades, angles, derives alpha shadows, composites the generated layers, validates, and exports. It does not draw the advisor card |
| Achievements | 14 |
| Evolutions and final identities | 5 evolution tracks and 5 final cosmetic identities |
| Flags | 21 independent built-in ImageGen designs plus 4 intentional aliases produce 75 TGAs. The flags are ImageGen-authored designs, not simple-shape substitutes |
| Required animations | Ledger seal 8, Need 8, Choice 8, Assignment 8, formation 10 |
| Additional animation | Reserve fill 8, outside the required-family count |
| Static Ledger families | 4 value icons, 6 Calling icons, 10 case cards, 7 district-role cards, 6 district-state overlays |
| District presentation | District role and state art is paired on Stores and Settlements |
| Ledger references | 46 unique scripted-GUI sprite references |
| Sprite registry | 459 base plus 5 super-event sprites, 464 total, 0 duplicate names |

## Evidence and hashes

| Gate or authority | Result | Frozen SHA-256 or fact |
| --- | --- | --- |
| Focus tree and paid-focus atomicity | PASS, unchanged current evidence | Report `16a3819a070e52a3c0eb380f4750730638d2bc698f8f9a660c5738da4b3776b6` |
| Formal improvement-loop closure | PASS, unchanged current evidence | Report `24aca5d240bbe8116d7de403027d4c5c54323709f272d03c7dc6f0ed8c62dbb1` |
| Decision and mission post-Ledger re-audit | PASS, no P0 through P3 finding | Report `823d9ae1f9956326f37fe1b8ebcdaea08d144107b112d7915827c350a99358fa` |
| Country-package post-Ledger re-audit | PASS, no blocker | Report `c0f74392ca1b1b20f7eac93de2ec23b3241291379e70f386b46b29ffd8509188` |
| Ledger state architecture re-audit | PASS after two bounded fixes | Report `c4f20170c7362a618da4128cecd608c0f090f98fb8e7b1a7276e766f451884ec` |
| Spreadsheet catalog post-localisation re-audit | PASS | Report `38fe68eed779d2634d9dedb3ea5152ee2a8ce31f6996b81031f1873d39a7c447` |
| Event workbook | PASS | Workbook `3c324b75c26f9e17eb9e73761abc5aedfa9bb642f2108a1397fb240679614031`. Only `Events!H16` changed. Event 19 and `Scenarios!A11:F11` remain preserved |
| Final asset re-audit | PASS, 24/24 accepted rows and no blocker | Report `a05d4c53f2ff775754ecdc00f9ee26789da16a13a05c0146044b095ff6891f33` |
| Asset requirement crosswalk | PASS | `8cf869a2f6f53ee9119a2bf2148c6eff4efae8c70ceae6c6d0e052f7dcae19bd` |
| Asset manifest | current authority | `1a30e4369df26ee067ea29309a5f9e2cb842519a3bc012379bdaf7efe9002148` |
| Asset GFX handoff | current authority | `113dee1ea4c70ca35b64da8c2c391b8e5bc977195c008118ee327b2189068146` |
| Asset animation handoff | current authority | `9fced786dfc0becb52945716b0503995c880e95401c6bb13878030bfb3dfeec7` |
| Machine icon and frame audit | PASS | `c85df258c4aaaf37e905fdc14883cda6b0f8a1f41840df745a3136c830a66d01` |
| Final localisation post-Ledger re-audit | PASS, no open blocker or omission | Report `72492b946760db070d1b8aaf27e927ff2b0cccfa124956b091cf6ea54e33bc3a`. It freezes 2,448 unique definitions, 507/507 event references, 328/328 decision or mission name and description keys, 125/125 public wrappers, 163/163 tooltips, 248/248 focus name and description keys, 99/99 focus wrappers, and 25/25 Ledger references |

## Historical P2 waves

Both prior P2 waves remain visible in the audit history.

1. The 2026-07-15 focus completion audit reported two P2 findings. Two focus textures were `95x85` instead of `94x86`, and one decision texture was `64x64` instead of `32x32`. The focus re-audit verified the two focus textures at `94x86` and the decision texture at `32x32`, closing both findings.
2. The 2026-07-16 repaired asset snapshot reported four P2 visual-completeness blockers. Value icons, Calling icons, case cards, and district role or state presentations were missing. The late Ledger tranche supplied all 33 static assets. The Ledger architecture re-audit verified exact scripted-localisation, GFX, GUI, file, and dimension parity.

## Working-record dispositions

| Record family | Disposition |
| --- | --- |
| Formal improvement-loop addendum | implemented, promoted into Parts 2, 4, 6, and 7, then closed by the independent improvement audit |
| Manual improvement-loop closure | superseded by the formal addendum and closure audit, retained as provenance |
| Catalog replacement plan | implemented and promoted into the live workbook and catalog evidence |
| Implementation sequence and subagent orchestration handoffs | superseded as execution plans, retained for reproducibility |
| Unresolved verification blockers handoff | superseded and resolved because its unavailable-workspace conditions no longer apply |
| Asset manifest plan | implemented and promoted. Current runtime authority is the asset auditor's manifest, handoffs, crosswalk, and final report |
| Prompts and early handoffs | historical execution recipes and evidence, not open tasks |
| Queued accepted plans | none |
| Rejected accepted plans | none |
| Unresolved accepted plans | none |

The only remaining workflow item is the new final whole-event completion audit. It is a completion gate, not an unresolved design plan.

## Dated-report dispositions

- `direct_integrated_validation_2026_07_15.md` remains valid for its inspected snapshot. Its 427-sprite count predates the late Ledger integration and is not current count authority.
- `documentation_completion_current_reaudit_2026_07_15.md` remains a historical documentation PASS for its 2026-07-15 snapshot. Its visual count and pre-correction localisation evidence do not close the current gates.
- The two reports now carry explicit 2026-07-16 disposition notices that point readers to this reconciliation and the source-of-truth packet.

## Tooling limitations

Fresh HOI4 MCP attempts covered the Event 15 focus tree, the `chaosx.nr15` event namespace, and the Commonwealth Ledger GUI. All three returned `ARTIFACT_STORAGE_LIMIT` before producing diagnostics or artifacts. This is an artifact-retention limitation, not a source failure. No MCP diagnostic was available to accept or reject.

The final asset audit was static. It verified files, hashes, decoded images, DDS and TGA headers, GFX, GUI and script bindings, codec metadata, and frozen rights evidence. It did not launch HOI4 or audition the audio in-engine. Those are tool limits, not missing deliverables or accepted fallbacks.

The final localisation audit was also static and English-only. No runtime render or clipping pass was available. Its narrow HOI4 MCP event inspection hit `ARTIFACT_STORAGE_LIMIT` before analysis. Direct source and reference validation supplied the passing evidence, and no MCP diagnostic was treated as a pass.

## Files changed by this curator

- `docs/events/015_utopia_manifesto/overview.md`
- `docs/specs/015_utopia_manifesto_specs/matrices/completion_coverage_matrix.md`
- `docs/specs/015_utopia_manifesto_specs/matrices/asset_manifest_plan.md`
- `docs/specs/015_utopia_manifesto_specs/specs/015_utopia_manifesto_spec_part_8_assets_localisation_and_acceptance.md`
- `docs/plans/015_utopia_manifesto_plans/015_utopia_manifesto_source_of_truth_and_resume_2026_07_15.md`
- `docs/plans/015_utopia_manifesto_plans/subagent_handoffs/direct_integrated_validation_2026_07_15.md`
- `docs/plans/015_utopia_manifesto_plans/subagent_handoffs/documentation_completion_current_reaudit_2026_07_15.md`
- `docs/plans/015_utopia_manifesto_plans/subagent_handoffs/documentation_final_reconciliation_2026_07_16.md`

No Git commit was created.

## Simplifications, omissions, fallbacks, and blockers

- Simplifications made in this documentation reconciliation: none.
- Documentation omissions: none.
- Fallbacks accepted: none.
- Blockers inside the delegated documentation scope: none.
- Whole-event blocker: the new final read-only event-completion audit remains pending.

Event 15 must remain reported as incomplete until that final whole-event gate passes.

## Skills and required references

This reconciliation used `chaos-redux-subagents`, `chaos-redux-events`, and `chaos-redux-event-assets`. It consulted the required offline Paradox wiki snapshot for data structures, triggers, effects, modifiers, localisation, scopes, on actions, event modding, decision modding, idea modding, AI modding, interface modding, scripted GUI modding, and national focus modding. It also preserved the vanilla documentation and precedent requirement as the authority followed by the implementation audits.
