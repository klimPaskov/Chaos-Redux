# Event 006 settled formable state-puzzle filesystem audit

## Audit result

The settled Event 006 state-puzzle surface is internally aligned for the accepted families FORM-01, FORM-02, FORM-03, FORM-04, FORM-05, FORM-07, FORM-08, FORM-09, FORM-12, FORM-13, FORM-16, FORM-18, FORM-39, and FORM-48. No Event 006-local gameplay, scripted-GUI, category, asset, activation, tooltip, or localisation defect was found. No gameplay source was patched; this handoff is the only file added by this audit.

## Severity-sorted issues and deliberate limits

| Severity | Finding | Disposition |
| --- | --- | --- |
| High | None. | No blocking mismatch found in the settled filesystem. |
| Medium | `hoi4.gui_inspect` and `hoi4.gui_render` report aggregate workspace diagnostics, including truncated collections, graph collisions, unresolved values, missing/invalid contexts, and overlaps when mutually exclusive family overlays are rendered together. | Evidence limitation only. Runtime source guards one family activation at a time; no local repair was justified, and `hoi4.gui_rewrite` was not used. |
| Low | FORM-08 exposes two researched candidate states while requiring three. FORM-07 remains identity/package fail-closed, and FORM-48 remains operationally unreachable until its reviewed identity and exact member package are live. | All three are explicitly settled design gates, not regressions or fallbacks. |

## Accepted-family crosswalk

All fourteen consumer specs and generated manifests are `status = complete`, share `independence_wave_formables`, `independence_wave_formable_state_puzzle_scripted_gui`, and `chaosx_independence_wave_formable_state_puzzle_window`, and use the matching family activation and territory helpers.

| Family | Candidate states | Required count | Member / invitation scope |
| --- | --- | ---: | --- |
| FORM-01 | 121, 133, 122, 14 | 4 | SCO/WLS/BRI package members; pending invitation precedence. |
| FORM-02 | 100, 337, 331, 121, 133 | 3 | ICE/AKX/GZX/SCO package members; AKX remains scenario/package-bound and the Scottish compact includes both states. |
| FORM-03 | 34, 36, 6 | 2 | AFX/AGX exact carrier anchors; state 6 is only the frozen `BEL_flanders` delegation and does not transfer Belgian territory. |
| FORM-04 | 51, 42 | 2 | RHI/AJX package members with the reviewed capital and adjacency checks. |
| FORM-05 | 1, 114, 115 | 2 | COR/ARX/ASX dedicated charter/proclamation path; not admitted through the generic commit family allowlist. |
| FORM-07 | 165, 792, 171 | 3 | CAT/NAV/GLC corridor package members; identity/flag/package readiness remains fail-closed. |
| FORM-08 | 84, 82 | 3 | TRA/AXX only; the finite candidate set is intentionally two states while the minimum is three. |
| FORM-09 | 185, 184, 104, 106, 105, 802 | 3 | BBX/BAX/BOS/MAC/MNT/KOS package members; territory helper enumerates all twenty reviewed three-of-six triplets. |
| FORM-12 | 249, 651, 256, 399, 397 | 4 | CHU carrier plus BSK/MEL/UDM/KOM frozen accepted invitations; carrier state plus any three members. |
| FORM-13 | 249, 651, 256, 399, 397 | 4 | Same CHU carrier/member geometry with the IDel-Ural family policy and frozen invitation scope. |
| FORM-16 | 230, 231, 229 | 3 | ARM/GEO/AZR exact Event 006 anchors and ownership/control proofs. |
| FORM-18 | 676, 421, 413 | 3 | ASY carrier plus KUR/CJX frozen accepted invitations; all three are required. |
| FORM-39 | 636, 523, 669 | 3 | FIJ/PNG/WPG reviewed member contracts. |
| FORM-48 | 378, 629, 684 | 3 | HBX carrier plus HAW/FSM exact autonomous-member contract; readiness remains operationally unreachable until the settled package gates pass. |

The wrappers in `common/scripted_triggers/006_independence_wave_formable_state_puzzle_triggers.txt` bind each state to the existing package/tag/anchor and frozen-invitation contracts. `has_pending_independence_wave_formable_founding_invitation = yes` is checked first in every activation helper; selected/profile and post-formation branches are nested under its `NOT` guard. This gives pending proposals activation precedence and prevents stale or competing invitation scopes from being treated as a current family overlay.

The generic invitation trigger requires a valid live pending flag and rejects accepted, withheld, stale-generation, wrong-family, wrong-sequence, or competing invitations. FORM-12, FORM-13, and FORM-18 member rows additionally require a frozen accepted invitation from the exact carrier and generation. FORM-03's Belgian delegation is the documented non-transfer sentinel, not a generic member shortcut.

## Decision-category lifecycle

Source inspection found exactly seventeen `scripted_gui = independence_wave_formable_state_puzzle_scripted_gui` attachments:

- `independence_wave_formables_category`;
- `independence_wave_formable_transaction_category`;
- `independence_wave_form0124_membership_category`;
- `independence_wave_form01_congress_category`;
- `independence_wave_form02_union_category`;
- `independence_wave_form04_league_category`;
- `independence_wave_form03_low_countries_category`;
- `independence_wave_form05_charter_category`;
- `independence_wave_form08_danube_category`;
- `independence_wave_form09_balkan_category`;
- `independence_wave_iw043_middle_volga_congress_category`;
- `independence_wave_iw058_council_of_communities_category`;
- `independence_wave_form16_integration_category`;
- `independence_wave_form39_invitation_category`;
- `independence_wave_form39_federal_compact_category`;
- `independence_wave_form48_invitation_category`;
- `independence_wave_form48_federal_compact_category`.

The generated scripted GUI has `context_type = decision_category`, a single independent root window, a human-only visibility gate, and one activation OR block for all fourteen accepted families. Fourteen overlay containers each have a family activation trigger; all 50 state pieces are therefore presentation-only until their exact family helper qualifies. `ai_enabled = { always = no }` is appropriate because AI consumes the decisions and does not need a presentation click surface.

The shared generic commit path is locked by `can_independence_wave_commit_selected_formable` in `common/scripted_triggers/006_independence_wave_formable_registry_triggers.txt`. Its first family gate is `has_independence_wave_selected_formable_state_puzzle_territory = yes`, which dispatches to the same family-specific territory helper represented by the GUI summary. The final `independence_wave_proclaim_military_union` decision repeats that helper through `available` and `custom_cost_trigger`; decision availability is also the AI's execution gate. Its `ai_will_do` willingness modifier uses `should_independence_wave_ai_pursue_selected_formable`, but that score does not replace the shared territory/commit availability gate.

FORM-05 is intentionally separate. `can_independence_wave_form05_proclaim_league` requires `independence_wave_formable_state_puzzle_form05_territory = yes`, and the dedicated `independence_wave_form05_proclaim_island_league` decision repeats that helper in both `available` and `custom_cost_trigger`, so player and AI use the same narrow helper. The generic selected-family gate correctly excludes this dedicated charter path.

## Costs, requirements, AI, and route locks

No state-puzzle cost was added or flattened. The shared commit decision still delegates to `can_pay_independence_wave_selected_formable_commit_cost`; FORM-05 keeps its existing strategic, administration, light-factory, and project-duration checks. Requirements remain finite family helpers and reviewed package contracts rather than raw player-facing trigger dumps.

The AI has no separate bypass route: the same decision availability helper gates both player and AI execution, while `ai_will_do` only supplies strategic willingness. The explicit allowlist in the commit trigger prevents generic receipts from promoting unresearched families. FORM-07 and FORM-48 identity/package gates and FORM-08's always-false territory helper keep their settled fail-closed routes. No war-goal, free-unit, equipment, invitation, relation-cleanup, or repeated-commit loop was introduced by this surface; the state-puzzle layer owns no persistent flags, variables, event targets, or cleanup effects.

No missions or timed objectives are introduced or changed by this state-puzzle surface. Mission owner, category, region, requirement, duration, success/failure, and duplicate-risk review are therefore not applicable here; existing formation/integration missions remain outside this GUI audit.

## Asset and localisation crosswalk

The fourteen manifests map 50 reviewed states to exactly two runtime DDS pieces each (`unresolved` and `qualifying`), for 100 DDS files total. Every file exists, begins with a valid `DDS ` header, and matches its manifest `dds_sha256`; no hash mismatch was found. The grouped `.gui` overlays, GFX state sprite IDs, state tooltip keys, and scripted-localisation `State…Sprite`, `State…Qualification`, `QualifyingCount`, and `SummaryStatus` helpers deduplicate to the exact manifest state sets for all fourteen families. The English file contains one summary and one state tooltip per accepted state, with required-count denominators matching the manifests, including FORM-08's `… / 3` fail-closed summary.

## MCP evidence and validation

- `hoi4.gui_inspect` returned `GUI_INSPECTED` for `chaosx_independence_wave_formable_state_puzzle_window`: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7ef2673ff8f17120d4af57ee1ea186242cab51bbd0de180293f6dee95f5ba358/466d18177cb6f43241458de2d3e61a09c36b90b67dbddf56274eade7e6cc18a1/gui-inspect.fc2200e9c790f7c3.json`.
- `hoi4.gui_render` returned `GUI_RENDERED` for the normal, hover, selected, disabled, warning, long-text, and missing-localisation states at 1366×768 and 1920×1080: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e5cf4a0e6908e7549e1bae29b05ae013092399118afcfe42cedf62d2833fe9/bad290e958062d59c6887532469bc60e48c725f8a9ce6ea2fd8f95c81eb43eb5/chaosx_independence_wave_formable_state_puzzle_w-full.svg`.
- The read-only static crosswalk reported `forms=14 manifests=14 dds=100 dds_hash_mismatches=0 attachments=17 errors=0`.
- No game process was launched, and no `hoi4.gui_rewrite` was used. Live gameplay and consumer validation remain parent/user responsibilities.

The MCP validation flag is false only because the offline aggregate scenario reports workspace-wide graph and overlap diagnostics and truncates portions of the response. Those diagnostics are not evidence of an Event 006-local source mismatch; the source activation guards and category context remain aligned.

## Remaining review items

No source fix is recommended in this audit. The parent should retain the existing FORM-07, FORM-08, and FORM-48 fail-closed documentation and fold any separate probability-auditor result for the decision `ai_will_do` surfaces into the final Event 006 completion report. No simplification or unapproved fallback was used.
