# Event 006 decision cost and visible-selector audit — 2026-09-05

Status: unresolved findings handed off; no gameplay source edit made.

## Scope

This bounded pass inspected only `common/decisions/006_independence_wave_decisions.txt` and `common/decisions/categories/006_independence_wave_categories.txt`. The required offline Decision modding, Triggers, Effects, Modifiers, Localisation, Scopes, Data structures, On actions, Event modding, Idea modding, and AI modding wiki pages were consulted, along with the installed vanilla documentation files for effects, triggers, modifiers, and script concepts. Localization files, shared scripted helpers, AI weights, admission logic, assets, GUI, and live-game validation were intentionally not inspected.

## Findings sorted by severity

### P1 — administration major cost selector disagrees with affordability and debit

`independence_wave_establish_treasury_and_currency` at lines 491–501 selects `independence_wave_cost_administration_major` at line 496, while both `available` and `custom_cost_trigger` use `can_pay_independence_wave_administration_standard_cost` at lines 492 and 495, and `complete_effect` debits `independence_wave_decision_pay_administration_standard` at line 501. The active timer modifier reserves the major factory amount at line 497. This is a deterministic source-level selector mismatch: the visible cost row says “major” by key while the ledger affordability and debit are “standard.”

No patch was applied because changing the row to the standard key would conceal the separate major factory commitment, while changing the helper/debit to a major variant would require an unverified shared helper outside this task’s scope. The owner should decide which cost tier is intended and make display, affordability, debit, and the factory commitment agree.

### P2 — diplomatic standard-factory rows have standard affordability/debit in two decisions

`independence_wave_coordinate_recognition_campaign` at lines 895–901 and `independence_wave_request_collective_recognition` at lines 2321–2328 select `independence_wave_cost_diplomatic_standard_factory`, but both `available` and `custom_cost_trigger` use `can_pay_independence_wave_diplomatic_standard_cost`, and both completion paths debit `independence_wave_decision_pay_diplomatic_standard`. Each decision also carries only the light `civilian_factory_use` modifier at lines 898 and 2324. The `_factory` selector therefore cannot be proven to describe the actual affordability/debit path from these two files alone.

No wording-only patch was applied because the `_factory` row may intentionally expose an ongoing factory commitment that is not debited by the ledger helper. The owner should verify the localization row and shared affordability contract, then either use the standard selector or add the matching factory-aware gate/debit through the owning shared mechanic.

### P2 — charter war mandate uses a factory-aware selector but a generic standard debit

`independence_wave_request_charter_war_mandate` at lines 3049–3056 uses the factory-aware `can_pay_independence_wave_diplomatic_standard_factory_cost` for both availability and custom-cost selection, and selects `independence_wave_cost_diplomatic_standard_factory`, but completion still calls `independence_wave_decision_pay_diplomatic_standard` at line 3056. This may be intentional if the factory part is a non-consumed timer commitment, but the source does not make that relationship explicit. It should be reconciled with the two P2 entries above for consistent player-facing cost semantics.

## Visible selectors and pre-event gate review

The category source currently mixes the Event 006-specific `is_independence_wave_event6_local_content_active` gate with the legacy `is_independence_wave_active_country` gate. The following category selectors still use the legacy helper after the 2026-09-05 clarity changes: `independence_wave_altai_mountain_compact_category` line 10, `independence_wave_buryatia_frontier_compact_category` line 38, `independence_wave_network_category` line 93, `independence_wave_league_category` line 100, `independence_wave_evolution_incident_category` line 152, `independence_wave_fer_railway_compact_category` line 159, `independence_wave_iw043_middle_volga_congress_category` line 358, `independence_wave_iw058_council_of_communities_category` line 368, `independence_wave_iw093_asante_compact_category` line 399, `independence_wave_iw098_sokoto_compact_category` line 408, `independence_wave_khakassia_frontier_compact_category` line 492, `independence_wave_komi_northern_compact_category` line 501, `independence_wave_kurdistan_mountain_compact_category` line 519, `independence_wave_mari_forest_compact_category` line 528, `independence_wave_fsm_micronesia_category` line 587, `independence_wave_fij_founding_congress_category` line 595, `independence_wave_nav_iberian_category` line 651, `independence_wave_glc_iberian_category` line 659, `independence_wave_sakha_arctic_compact_category` line 667, `independence_wave_udm_industrial_forest_category` line 675, and `independence_wave_iw095_first_footprint_category` line 824.

This is a post-patch consistency signal, not a proven pre-event leak without the shared helper definitions. The source itself contains the Scotland adapter warning that Event 021 must not expose Event 006 categories, so the owner should confirm the intended origin gate for each residual category before making a gameplay visibility change. No visibility selector was changed in this read-only pass.

## Cost, category, and mission audit notes

- The decision file contains 77 decision/mission blocks, 73 custom-cost rows, and only three regular `cost = 0` rows at lines 954, 991, and 1021; those are scenario-ledger navigation/close controls rather than spendable actions.
- Every custom-cost row in the bounded source has both `custom_cost_trigger` and `custom_cost_text`. The source exposes cost selectors as keys, not literal resource prose, so texticon coverage, wording density, and implementation-facing localization cannot be proven without opening the excluded localization files.
- The source-level cost contract is otherwise structurally clear: affordability is normally repeated in `available` and `custom_cost_trigger`, and payment occurs in `complete_effect` or a named helper. The three mismatches above are the exceptions requiring owner reconciliation.
- Core categories retain compact action grouping and progression gates. The category file contains no cost rows; category visibility is the only category-side cost-adjacent surface in scope.
- Mission lifecycle review was limited to the cost/selector relationship. The flagged administration entry is a selectable mission with activation, availability, completion, timeout, and cancellation blocks; no lifecycle patch was made.
- AI probability, AI weights, target validity, route locks, GUI rendering, and live-game behavior were not audited because the resumed task explicitly excluded those surfaces. No live-game validation is claimed.

## Recommended owner actions

1. Reconcile `independence_wave_establish_treasury_and_currency` so its displayed administration tier, ledger helper, debit helper, and factory commitment are one intentional contract.
2. Reconcile the two diplomatic `standard_factory` selectors with the charter-war-mandate pattern and confirm whether the factory modifier is a player-visible commitment or merely an active timer modifier.
3. After confirming shared helper semantics, review the 20 residual legacy category visibility selectors listed above against the Event 006 origin gate and the Event 021 adapter boundary.
4. If localization review later confirms bloated or implementation-facing cost wording, make the smallest key-only source correction and update the corresponding localization in the owning pass; this audit intentionally did not inspect or edit localization.

## Validation and limits

The bounded parser found `decisions=77`, `custom_cost_text=73`, `regular_cost=3`, and balanced final brace depth `0`. A source-only selector comparison produced the three mismatch groups documented above. The two decision files were not edited by this subagent; only this handoff was added. Shared scripted definitions, localization rows/texticons, GUI evidence, AI/probability evidence, and live-game behavior remain unresolved by design.

## Follow-up localization re-audit — parent-requested screenshot check

This follow-up was allowed to inspect only the Event 006 cost localization and the exact source/constants needed to determine whether the screenshot's old bundle is still exposed. No gameplay selector, affordability trigger, debit helper, or localization entry was edited.

### Finding: the old bundled pre-event crisis row is retired

The current Event 006 localization set contains no literal `5000` and no single current localization row combining `5000 manpower`, `20 XP`, `20 command power`, `500 infantry equipment`, `100 support equipment`, and `120 days`. The only current Flanders `120 days` search hits are unrelated IW-043/IW-058 and IW-093/IW-098 package tooltips at `localisation/english/006_independence_wave_iw043_iw058_l_english.yml:359,472,516` and `localisation/english/006_independence_wave_iw093_iw098_l_english.yml:100,107,190`.

The active Flanders cost rows are split into two actions and use texticons plus dynamic constants: `independence_wave_iw005_officer_cost` and its blocked mirror at `localisation/english/006_independence_wave_minor_overlay_l_english.yml:36-38`, and `independence_wave_iw005_guard_cost` and its blocked mirror at `:43-45`. The officer row resolves from `common/script_constants/006_independence_wave_constants_registry.txt:4320-4327` to 5,000 manpower, 20 Army Experience, 500 infantry equipment, and 100 support equipment. The guard row resolves from `:4329-4336` to 20 command power, 5,000 manpower, 500 infantry equipment, and 100 support equipment. The current guard duration is 150 days at `:4298`, and the mission source consumes that constant at `common/decisions/006_independence_wave_minor_overlay_decisions_registry.txt:20-34`; the player-facing description is dynamic at `localisation/english/006_independence_wave_minor_overlay_l_english.yml:42`.

These rows are not stale localization: `independence_wave_iw005_vet_defecting_regulars` selects the officer row at `common/decisions/006_independence_wave_minor_overlay_decisions_registry.txt:108-114`, while `independence_wave_iw005_raise_factory_railway_guard` selects the guard row at `:139-146`. The category is additionally gated by the Event 006 player-surface, overlay-runtime, and Flanders-overlay-active triggers at `common/decisions/categories/006_independence_wave_categories.txt:322-325`. The overlay registry explicitly documents that these packages do not create pre-event player-facing crisis surfaces at `common/decisions/006_independence_wave_minor_overlay_decisions_registry.txt:4-8`.

Therefore, the screenshot's old single five-resource/120-day crisis display is fully retired as a combined surface, but its numeric components remain intentionally visible across two post-event overlay actions. A localization-only reduction or rewrite would hide or misdescribe active costs and would not be source-safe.

### Safe localization-only cleanup review

No deterministic localization-only cleanup was identified. The sibling rows `independence_wave_cost_administration_standard_factory` at `localisation/english/006_independence_wave_decisions_l_english.yml:40,66,68` and `independence_wave_cost_diplomatic_standard_factory_standard` at `:44,80,82` are not selected by the bounded `006_independence_wave_decisions.txt` scan, but a repository reference check finds active selectors in `common/decisions/006_independence_wave_pacific_decisions.txt:95,467`, `common/decisions/006_independence_wave_form03_decisions.txt:221,258,340,685`, and `common/decisions/006_independence_wave_form01_02_04_decisions.txt:36`; deletion or renaming is therefore unsafe without a broader audit. The Flanders cost rows have matching active, blocked, and tooltip keys, so none is an unused stale entry.

### Disposition

No patch is justified. This follow-up leaves gameplay and localization unchanged and claims no live-game validation. The remaining question—whether the two intentionally expensive Flanders overlay actions should have different design costs—is a gameplay/balance decision, not a safe wording-only repair.
