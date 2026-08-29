# Event 006 localisation cleanup handoff

Date: 2026-08-29

Mode: bounded localisation patch

## Outcome

The current Event 006 English localisation no longer contains indented localisation keys. All 1,880 keys identified by the current audit now begin at column one. The 140 audited static numeric cost strings now read authoritative script constants or existing nested cost keys. A small set of implementation-facing decision and tooltip strings was rewritten without changing gameplay, route visibility, transport alternatives, patron stages, or pre-event behavior.

## Changed files

- `localisation/english/006_independence_wave_balkan_l_english.yml`
- `localisation/english/006_independence_wave_bashkiria_mari_l_english.yml`
- `localisation/english/006_independence_wave_decisions_l_english.yml`
- `localisation/english/006_independence_wave_form03_l_english.yml`
- `localisation/english/006_independence_wave_frontier_l_english.yml`
- `localisation/english/006_independence_wave_gui_l_english.yml`
- `localisation/english/006_independence_wave_iw043_iw058_l_english.yml`
- `localisation/english/006_independence_wave_iw093_iw098_l_english.yml`
- `localisation/english/006_independence_wave_komi_l_english.yml`
- `localisation/english/006_independence_wave_kosovo_l_english.yml`
- `localisation/english/006_independence_wave_minor_overlay_l_english.yml`
- `localisation/english/006_independence_wave_ruthenia_l_english.yml`
- `localisation/english/006_independence_wave_scotland_wales_l_english.yml`
- `localisation/english/006_independence_wave_siberian_l_english.yml`
- `localisation/english/006_independence_wave_tatarstan_l_english.yml`
- `localisation/english/006_independence_wave_transcaucasus_l_english.yml`
- `localisation/english/006_independence_wave_udm_l_english.yml`
- `localisation/english/006_independence_wave_western_l_english.yml`
- this handoff

No scripted-localisation source file was changed.

## Changed keys

### Structural normalization

Every previously indented key was normalized without changing its value in these nine files:

| File | Keys normalized |
| --- | ---: |
| `006_independence_wave_minor_overlay_l_english.yml` | 468 |
| `006_independence_wave_balkan_l_english.yml` | 439 |
| `006_independence_wave_siberian_l_english.yml` | 333 |
| `006_independence_wave_bashkiria_mari_l_english.yml` | 259 |
| `006_independence_wave_western_l_english.yml` | 208 |
| `006_independence_wave_gui_l_english.yml` | 101 |
| `006_independence_wave_udm_l_english.yml` | 66 |
| `006_independence_wave_decisions_l_english.yml` | 4 |
| `006_independence_wave_komi_l_english.yml` | 2 |

### Dynamic cost text

- All name, blocked, and tooltip triplets under `independence_wave_iw043_cost_*` and `independence_wave_iw058_cost_*` now use `independence_wave_decision_cost`, `independence_wave_iw043`, or `independence_wave_iw058` constants. Their tooltip variants nest the matching base cost instead of repeating it.
- All name, blocked, and tooltip triplets under `independence_wave_iw093_cost_*` and `independence_wave_iw098_cost_*` now use `independence_wave_decision_cost`, `independence_wave_iw093`, or `independence_wave_iw098` constants.
- The 22 audited Transcaucasus blocked and tooltip cost keys now nest their matching dynamic base key with valid `$key$` syntax. This covers `independence_wave_transcaucasus_cost_*`, `independence_wave_cost_iw070_*`, `independence_wave_cost_iw071_*`, `independence_wave_cost_iw072_*`, `independence_wave_cost_transcaucasus_arbitration_*`, and `independence_wave_cost_form16_*`.
- `independence_wave_form03_compact_technical_mission_cost_tooltip` now nests its existing dynamic base cost without an obvious explanatory label.

### Prose keys

- `independence_wave_sponsor_another_breakaway_desc`
- `independence_wave_coordinate_reclamation_fronts_complete_tt`
- `independence_wave_coordinate_reclamation_fronts_failed_tt`
- `independence_wave_coordinate_reclamation_fronts_timeout_tt`
- `independence_wave_scotland_wales_security_project_effect_tt`
- `independence_wave_scotland_wales_route_government_effect_tt`
- `independence_wave_iw043_register_form12_member_charters_desc`
- `independence_wave_arm_arbitrate_transcaucasian_frontier_desc`
- `independence_wave_geo_host_border_conference_desc`
- `independence_wave_azr_submit_corridor_guarantees_desc`
- `independence_wave_transcaucasus_founding_success_tt`
- `independence_wave_transcaucasus_project_complete_tt`
- `independence_wave_transcaucasus_arbitration_complete_tt`
- `independence_wave_bsk_host_loss_effect_tt`
- `independence_wave_mnt_host_loss_effect_tt`
- `independence_wave_kur_host_loss_effect_tt`
- `independence_wave_kub_host_loss_effect_tt`
- `independence_wave_kos_host_loss_effect_tt`
- `independence_wave_rut_host_loss_effect_tt`
- `independence_wave_altai_host_loss_effect_tt`
- `independence_wave_bya_host_loss_effect_tt`
- `independence_wave_kha_host_loss_effect_tt`
- `independence_wave_yak_host_loss_effect_tt`
- `independence_wave_tat_host_loss_effect_tt`

## Before and after

- Before, 1,880 values existed behind keys indented away from the repository's required column-one form. After, all Event 006 localisation keys are structurally loadable under the repository contract.
- Before, 140 cost strings repeated numeric values across normal, blocked, and tooltip variants. After, every audited amount resolves from the same constants used by the owning decisions, and repeated IW-043/IW-058 and Transcaucasus tooltip prose nests the base cost.
- Before, several tooltips described packages, receipts, transactions, generic targets, and ledger bookkeeping. After, they state the public action, failure, deadline, institutional settlement, or end of bilateral negotiation directly.

## Prose before-and-after summary

- Vagueness: replaced `valid future candidate`, `configured ... ledger gain`, and package-level terms with independence movements, stated local measures, governments, and chosen routes.
- Bloat: shortened reclamation-front success, failure, and timeout text while preserving separate fronts, resource rollback, crisis, deadline, and danger-milestone consequences.
- Obvious explanation: removed `This action costs` and `Technical mission commitment` wrappers where the dynamic icon-first cost already communicates the information.
- Repetition: condensed repeated former-host ledger bookkeeping into a direct statement that bilateral negotiations end, while preserving every named value gain and dynamic token.
- Overcomplication: replaced arbitration receipts and founding-ledger language with ratified settlements, guarantees, and a founding charter.
- Style-rule repair: removed implementation-facing `package`, `synchronized transaction`, `generic target`, and `accession receipt` wording from the patched keys. No em dash, semicolon, staccato chain, or staged contrast was introduced.

## Audit results after patch

- Missing key list: none among Event 006 scripted-localisation result keys.
- Duplicate key list: none for the 8,808 keys defined by dedicated Event 006 English files when checked across all English localisation files.
- Scripted-localisation issue list: the former 70 branches depending on indented values now resolve to column-one keys. No Event 006 scripted-localisation result key is missing.
- Dynamic text opportunities addressed: the 140 audited static cost strings now use constants or dynamic nested keys. Broader non-cost prose may still contain static narrative numbers by design.
- Cross-surface mismatch: no gameplay or catalog surface was changed. The pre-existing Liberations cluster workbook member-cell mismatch remains outside this localisation-only patch.
- File encoding concerns: none. All 37 dedicated Event 006 English files retain UTF-8 BOM and the `l_english:` header.

## Sourced quotation preservation

The Wilson Point XIV quotation, the Hosea 8:7 KJV quotation, and the source-derived `They have sown the wind.` button remain byte-for-byte unchanged from the pre-patch localisation values. No other attributed quotation was edited.

## Meaningful validation

- Dedicated Event 006 localisation scan: 37 files, 8,808 keys, zero format errors, zero duplicate Event 006 keys, and zero missing Event 006 scripted-localisation result keys.
- Audited cost-family scan: zero remaining static numeric cost lines in `independence_wave_iw043_cost_*`, `independence_wave_iw058_cost_*`, `independence_wave_iw093_cost_*`, or `independence_wave_iw098_cost_*`.
- Nested Transcaucasus cost scan: zero remaining bracket-style nested cost references.
- `audit_event6_allocator.py`: passed and confirmed the pre-event crisis surface remains retired.
- `audit_event6_gui_matrix.py`: passed semantic source coverage, without runtime-rendering claims.
- `audit_event6_scenario_matrix.py`: passed all 32 scenario cells and eight edge cases.
- `audit_event6_form16.py`: passed the three-member consent, mutation, cleanup, and fail-closed contract.

## Skipped meaningful validation and exact blocker

The required HOI4 event, focus, and production GUI inspection/render routes were not callable. The runtime tool registry exposed no `hoi4_agent_tools`, `hoi4.event_inspect`, `hoi4.event_render`, `hoi4.focus_inspect`, `hoi4.focus_render`, `hoi4.gui_inspect`, or `hoi4.gui_render` route. No artifact URI exists for this pass, and the static checks above are not presented as equivalent overflow or layout evidence.

Live in-game display remains user-owned and was not attempted.

## Unresolved wording decisions

- Long country-route effect tooltips cited by the audit still need production rendering before further cuts can be judged safely. This patch does not remove concrete dynamic effects to make them shorter.
- The internal collection labels in `006_independence_wave_l_english.yml` remain unchanged because their player visibility could not be established without the missing MCP route.
- Broad country-specific rewriting of repeated Balkan and Siberian route descriptions remains a separate route-by-route writing pass. Bulk invention was not used.

## Simplifications, omissions, and blockers

No gameplay mechanic, cost, transport alternative, patron stage, hidden route, pre-event cue, or sourced quotation was simplified. Production visual validation remains blocked by the unavailable HOI4 MCP routes. No unapproved fallback was used.

## Plan handoff

None. No missing mechanic was inferred from the bounded localisation fixes.
