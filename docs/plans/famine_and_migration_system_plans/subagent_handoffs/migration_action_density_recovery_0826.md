# Migration action-density recovery audit (2026-08-26)

## Disposition

The parent visibility patch is accepted. The pre-patch closed-policy witness could expose seven migration primary rows because `migration_close_border` remained visible after closure and `migration_transit_only` remained visible when its availability policy gate rejected the action. The current source removes that witness without changing AI weights, balance constants, costs, effects, or route consumers.

This audit made no gameplay changes and created no commit. The parent-owned source change is `common/decisions/migration_decisions.txt`: `migration_close_border` starts at line 671 and its policy guard is in `visible` lines 685-688, while `migration_transit_only` starts at line 1669 and its controlled/humanitarian-open policy guard is in `visible` lines 1677-1680. The corresponding availability gates remain at lines 694-705 and 1686-1694, so AI access and player visibility now agree.

The parent follow-up category patch is also accepted. `common/decisions/categories/migration_decision_category.txt:13` now includes `has_country_flag = humanitarian_corridor_offer_pending` in the category `visible` OR block, which makes the response surface reachable while preserving the normal-country and normal-civilian-system guards at lines 5-8.

The audited namespace is migration-owned (`migration_*`) with only neutral `civilian_transfer_*` and `humanitarian_*` primitives. No `famine_migration_*` or `fm_*` identifier was introduced, and famine remains a separate category/mechanic.

## Boolean phase/visibility matrix

`C` means the row can be simultaneously visible and clickable when its state/route/stockpile target conjunction is satisfied. The matrix counts distinct primary decision IDs, not one clone per state target. Corridor-offer responses are auxiliary rows and missions are counted separately below.

| Phase fixture | `C` primary IDs | Maximum |
| --- | --- | ---: |
| Emerging/inactive, no pending offer | `migration_prepare_evacuation`, `migration_open_departure_routes`, `migration_restrict_departure`, and `migration_close_border` when a valid reception target exists | 4 |
| Active controlled-border crisis with no current reception load (accepted parent fixture) | `migration_close_border`, `migration_evacuate_vulnerable`, `migration_evacuate_workers`, `migration_negotiate_corridor`, `migration_open_reception`, and `migration_transit_only` | 6 |
| Active positive-load quarantine reception | `migration_close_border`, `migration_controlled_medical_reception`, and `migration_distribute_arrivals` when the exact exposed cohort and target are valid | 3 |
| Active closed reception policy | `migration_enforce_closure` and `migration_distribute_arrivals` when the exact host/target remains valid | 2 |
| Resolution with positive load and headroom | `migration_local_integration`, `migration_third_country_resettlement`, `migration_voluntary_return`, and `migration_forced_repatriation` when each destination/authentication gate is valid | 4 |
| Pending humanitarian corridor offer | No primary row; the auxiliary pair `migration_accept_corridor_offer` and `migration_reject_corridor_offer` is selectable | 0 primary / 2 auxiliary |
| Dormant or clean | No primary row | 0 |

The exact current maximum is therefore six primary actions, reached by the active controlled-border witness above; no post-patch phase exceeds six. The closed-policy seven-row presentation is impossible because the close-border policy check excludes `migration_reception_policy >= closed`, and transit visibility now requires the same policy values already required by availability.

The 18 primary/action IDs and source line anchors are: `migration_prepare_evacuation` (466), `migration_open_departure_routes` (570), `migration_restrict_departure` (620), `migration_close_border` (671), `migration_evacuate_vulnerable` (754), `migration_evacuate_workers` (947), `migration_negotiate_corridor` (1148), `migration_open_reception` (1266), `migration_controlled_medical_reception` (1396), `migration_distribute_arrivals` (1479), `migration_transit_only` (1669), `migration_enforce_closure` (1823), `migration_local_integration` (1959), `migration_third_country_resettlement` (2079), `migration_voluntary_return` (2234), and `migration_forced_repatriation` (2440), plus the auxiliary responses `migration_accept_corridor_offer` (1223) and `migration_reject_corridor_offer` (1245).

### Six-action witness

Use a normal-civilian-systems country with `migration_decision_active` set, no resolution or pending corridor offer, a controlled reception policy, a valid active displacement/cohort context, valid controlled origin and reception targets, and the parent fixture's no-current-reception-load condition. Satisfy the six rows' target and stockpile checks, including prepared evacuation evidence, a valid humanitarian corridor origin, valid reception state evidence, and any required factories, trains, fuel, infantry equipment, support equipment, and political power. The simultaneously clickable set is exactly `{migration_close_border, migration_evacuate_vulnerable, migration_evacuate_workers, migration_negotiate_corridor, migration_open_reception, migration_transit_only}`. The available source evidence does not prove a seventh post-patch row under this witness.

## Category lifecycle and cognitive load

`migration_decision_category` is visible only for normal civilian countries with active, emerging, resolution, reveal-threshold, or pending-corridor-offer evidence, and uses `visible_when_empty = no`; dormant/clean migration without an offer is hidden. Phase refresh clears stale phase flags and enters resolution/dormancy only after live cohort, reception, origin-crisis, and corridor-offer conditions settle.

The category presents one primary displacement value plus reception capacity, border policy, phase, and current-priority context. These values have clear labels and decision relevance, although the existing report header has no dedicated meter or threshold marker; that is a presentation improvement opportunity, not an action-density defect. The six-action maximum keeps the active surface below a wall of simultaneous primary rows, and there are no extra tabs or warehouse categories in this scope.

Four migration missions can be active through the shared slot counter, but missions are not clickable primary actions. The mission constants cap active missions at three, so the fourth family is a selectable lifecycle family rather than a fourth simultaneous active slot.

## Mission quality

| Mission | Owner/category and region | Requirement and duration | Success/failure and duplicate risk |
| --- | --- | --- | --- |
| `migration_mission_hold_humanitarian_corridor` (36; activation 42; timeout 71) | Migration displacement/corridor owner; exact controlled subject state and corridor cohort | Valid active corridor subject, cohort, and route contract; 120 days; `selectable_mission = no` | Success finalizes the corridor and records outcomes; timeout applies the defined stability/war-support consequence and expires the corridor; active-family flag and slot accounting prevent duplicate activation. |
| `migration_mission_protect_evacuation_transport` (101; activation 107; timeout 153) | Migration displacement/evacuation owner; exact evacuation subject state | Positive cohort, deadline, infrastructure, safe route, and no famine/persecution/bombing/contamination/fallout/plague; 100 days; nonselectable | Success and timeout clear subject/cohort/deadline/country state and recount slots; exact subject/deadline and active flag prevent duplicate protection missions. |
| `migration_mission_prevent_reception_collapse` (183; activation 189; timeout 282) | Migration reception owner; exact observation-pending host state | Valid host capacity, exact hosted cohort, positive state load, observation deadline, and no overcrowding/breach/plague; 150 days; nonselectable | Success, timeout, and cancel clear subject/proof/cohort/deadline flags and recount slots; reception-active and observation flags prevent duplicate observation. |
| `migration_mission_prepare_safe_return_route` (360; activation 366; timeout 410) | Migration resolution/return owner; exact return subject state | Return context, deadline, valid safe state/infrastructure, and no famine/persecution/bombing/contamination/fallout/plague; 180 days; nonselectable | Success and timeout clear subject/deadline/country state and recount slots; return-active and exact subject checks prevent duplicate preparation. |

Mission `visible` keys are retained for source readability, but the offline decision rules confirm that `activation` controls mission activation and `selectable_mission = no` makes these non-clickable automatic missions.

## Cost, requirements, AI, and routes

Every clickable migration decision has zero to four distinct spendable cost types. The maximum is the four-type `migration_third_country_resettlement` cost (political power, trains, convoys, and fuel); no fifth cost is hidden in a tooltip or secondary panel. All migration cost localisation in `localisation/english/migration_l_english.yml` is icon-first through the `GetCivilianResponse...Cost` keys, with support equipment using the correct texticon. Non-consumed requirements such as worker evacuation support equipment and route safety remain separate trigger/tooltips.

All 18 migration action IDs retain centralized `ai_will_do` blocks and target/route/ownership/availability checks. No AI weight or balance constant was changed by this audit or by the accepted visibility patch. The parent full-pool probability inspection covered all 18 IDs at source hash `ef14ce12e61338d733440d0fdc85bc1ede5a883b767cc7fe7ef48edf7327d779`; the same-scenario comparison `probability-320ed8c0ab9e18a15234344a` returned `PROBABILITY_ANALYZED_PARTIAL` with `comparisonChanges=0` and 94 unresolved items, which supports no modeled score change but is not complete live eligibility certification.

Cooldowns, terminal effects, mission-slot recounts, exact cohort/route checks, and cleanup hooks are present for the audited rows. No free-equipment/unit loop, repeated transfer, stale mission slot, or cooldown bypass was found in this density pass.

## Localisation, GUI evidence, and unresolved findings

Titles, descriptions, trigger tooltips, mission text, and icon-first costs are present for the audited IDs. The migration report header is informational and has no clickable action controls. Read-only `hoi4.gui_inspect` completed with `GUI_INSPECTED` in workspace `mod_chaos_redux_ea3b2d67c2c0`, artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3f45a99fd9c14b258a0f63ea0b077f8d484b601729a0604108c8a92bc8de3068/02dee702b7f1489295d75998a8aebf6c8c210e627c0ed215c65501546a9d8c48/gui-inspect.a8a34cb6b55807e5.json`, with 13 inspected elements and fidelity counts of 137 modelled, 6 approximated, 1 ignored, 4 missing, 1 unsupported, and 1 unresolved. The prior read-only render artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ccb4623ed97b2145c0de5861bbdce1ec9d12aa9ab2c0a2be3ee90ccd1cffb3d8/dc20a074a34ec16918213254fc6493ffa35b7720feb28b618a9252b6c87ef98e/migration_report_header_window-full.svg`.

Severity-sorted findings:

1. Closed, previously medium accessibility: `common/decisions/categories/migration_decision_category.txt:13` now admits `humanitarian_corridor_offer_pending`. Both response rows at `common/decisions/migration_decisions.txt:1223-1251` additionally require `humanitarian_corridor_offer_is_valid`, whose country trigger at `common/scripted_triggers/humanitarian_corridor_triggers.txt:257-284` requires the pending flag, exact offer IDs, operation, positive cohort/generation, a live deadline, and acceptance validation. This closes the prior category reachability finding without exposing stale or invalid response actions.
2. Low, presentation warning: the report header exposes labelled phase/load/capacity/policy/priority values without a visual threshold meter. The values remain interpretable through existing localisation and this does not add primary actions.
3. Low, evidence limitation: GUI graph diagnostics are globally truncated and include unrelated index collisions, scripted-context, overlap, and missing-texture diagnostics. No migration-specific GUI control blocker was established; the header has no action buttons.
4. Low, probability limitation: the parent comparison is partial with 94 unresolved dynamic eligibility items, so it cannot certify every live scoped target even though it reports no modeled willingness-score change.

## Validation and uncertainty

The focused source census found 18 clickable migration decision IDs and four migration mission IDs, verified the two parent visibility gates against their matching availability gates, verified the category pending-offer branch against both response rows and `humanitarian_corridor_offer_is_valid`, and found no forbidden `famine_migration_*` or `fm_*` runtime ID in the audited migration source surface. The parent probability inspect/compare and the mandatory read-only GUI inspect/render artifacts are recorded above.

A post-patch GUI render retry timed out after 180 seconds; no GUI source changed, so no `hoi4.gui_rewrite` was warranted. No live game launch or gameplay test was performed, per repository instructions. The action count uses distinct decision IDs/action rows; an engine presentation that expands one state-targeted ID into multiple map targets would require a separate UI-instance count.

### Files changed

No gameplay files were changed by this auditor. This handoff is the only file created by this audit. The accepted parent patches are confined to `common/decisions/migration_decisions.txt` at the visibility gates identified above and `common/decisions/categories/migration_decision_category.txt:13` for the pending-offer category branch.
