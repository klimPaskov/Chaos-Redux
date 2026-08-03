# Event 006 country registry and package-admission audit

Date: 2026-08-03

Audit mode: read-only country-package and registry/API audit.

Scope: current Event 006 registry shape, collection/API readiness boundaries, unadmitted rows, host survival, tag reuse/collision scope, vanilla identity exclusions, and generic focus-tree adoption. No gameplay, map, asset, localisation, or spreadsheet files were patched.

## Verdict

The Event 006 country registry and collection API are statically present, but package admission remains HOLD / PARTIAL. The runtime gate is fail-closed: 23 package adapters are listed, while only 15 exact package IDs have compile-time content attestations. The remaining adapters and all other registry rows cannot execute merely because their tags appear in a collection or because an exact tag/anchor predicate exists.

The current post-TRA boundary is 15 of 193 selectable non-overlay packages, spanning 14 compatible reservation groups and 15 distinct anchors. The admitted set is `IW-001`, `IW-002`, `IW-004`, `IW-006`, `IW-007`, `IW-008`, `IW-009`, `IW-010`, `IW-012`, `IW-017`, `IW-018`, `IW-019`, `IW-023`, `IW-173`, and `IW-184`. IW-023 TRA is admitted by `006_iw023_tra_runtime_scenario_admission_reconciliation_2026_08_03.md` and commit `712c7c868`. Eight adapter-only rows remain outside the central attestation gate, 178 selectable rows remain unattested, and FORM-08 remains a separate fail-closed member/consent/anchor gate. Any former fourteen-package, thirteen-group, or fourteen-anchor wording below is pre-TRA evidence and is superseded for current status.

## Country package coverage checklist

| Surface | Current coverage | Evidence and boundary |
| --- | --- | --- |
| Registry rows | PASS static | `docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv` has 206 rows. The constants mirror 206 total, 193 selectable, 13 overlay-only, 102 Event 006-owned X rows, 91 reuse rows, 191 unique resolved carriers, 138 bound selectable rows, and 55 unbound selectable rows at `common/script_constants/006_independence_wave_country_registry_constants.txt:182-197`. |
| Collection/API surface | PASS static, not admission | `common/collections/chaosx_country_collections.txt` and `docs/events/006_independence_wave/country_api.md:5-23` expose owned, registered, bound, unbound, overlay, Africa, Soviet, and regional views. The collection documentation explicitly says membership does not create a country, transfer ownership, or select a focus/API package (`docs/events/006_independence_wave/systems/country_registry.md:44-88`). |
| Exact package admission | BLOCKED outside 15 IDs | `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:10-39` lists 23 adapters, while the current attestation list contains 15 IDs. The outer preflight requires both adapter and attestation (`:95-99`). |
| Adapter-only rows | FAIL CLOSED | The eight current adapter-only IDs are `IW-014` CAT, `IW-030` MNT, `IW-043` CHU, `IW-058` ASY, `IW-093` DOX, `IW-098` SOK, `IW-177` FIJ, and `IW-179` FSM. Their exact tag branches exist in `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:151-206`, but the central attestation list excludes them. |
| Other non-overlay rows | FAIL CLOSED | Of 193 selectable non-overlay rows, 178 are not attested. The registry disposition counts remain metadata only and do not prove complete country packages. |
| Overlay rows | Route-only by design | The 13 `vanilla_route_overlay_only` rows have no `resolved_tag` and are not standalone release candidates (`docs/events/006_independence_wave/systems/country_registry.md:12-17`; `docs/events/006_independence_wave/country_api.md:16`). |
| Shared carrier identity | Exact package required | `CHU` is intentionally shared by `IW-043` and `IW-046`; `BIA` is shared by `IW-096` and `IW-107`. The API requires package ID, anchor, and reservation-group resolution; a tag alone cannot select content (`docs/events/006_independence_wave/country_api.md:27-29`, `:43-50`). |

## File surface checklist

| Surface | Current source | Audit result |
| --- | --- | --- |
| Candidate registry authority | `docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv` | 206 rows parsed; no row was added or removed. |
| Installed map/binding ledger | `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv` | 206 rows; 55 unbound, 13 overlay routes, 134 fixed-anchor rows, 4 choose-one host rows, and no non-empty `missing_current_state_ids` field in the current CSV. Static binding does not prove live ownership. |
| Reservation-group ledger | `docs/plans/006_independence_wave_plans/package_bindings/006_current_map_reservation_groups.csv` and `docs/specs/006_independence_wave_specs/research/006_state_anchor_and_reservation_groups.csv` | 111 reservation groups are represented. Runtime still has to reserve the exact group and state. |
| Tag registration | `common/country_tags/006_independence_wave_countries.txt` plus the Soviet registrations checked by `.tools/audit_chaosx_country_tags.py` | Event 006 X-tag registry is present; no new tag was created by this audit. |
| Registry triggers/effects | `common/scripted_triggers/006_independence_wave_country_registry_triggers.txt`, `common/scripted_effects/006_independence_wave_country_registry_effects.txt` | Membership and origin lifecycle are defined. The effects only record/clear Event 006 origin markers and do not create tags, actors, or assets. |
| Package dispatch | `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt`, `common/scripted_effects/006_independence_wave_package_dispatch_effects.txt` | Adapter, attestation, exact identity, setup, final-validation, and cleanup barriers are wired. |
| Focus ownership | `common/scripted_effects/006_independence_wave_focus_effects.txt`, `common/scripted_triggers/006_independence_wave_focus_triggers.txt` | Full generic-tree and reviewed additive-carrier contracts are explicit and fail closed. |

## Missing or stale country-package surfaces

The 178 unattested non-overlay rows still need country-specific identity, history/territory, leaders and character consumers, portraits/provenance, flags/cosmetic identity, politics and party setup, advisors/high command, ideas and decisions, forces/technology/industry/supply, AI, localisation, focus contract, cleanup, and package attestation before they can be promoted. Concrete current examples are `IW-182` GZX (`GZX` shell/history and binding only; `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw182_gzx_country_package_audit_current_2026_08_03.md`), `IW-030` MNT, `IW-177` FIJ, `IW-043` CHU, and `IW-058` ASY. IW-023 TRA is no longer in this gap.

The eight adapter-only rows are not stale API entries; they are deliberately registered for later re-audit and remain blocked by the central attestation list. Do not promote them by adding a generic readiness flag or by selecting from a collection.

Historical collision handoffs from 2026-07-28 are not current all-Chaos proof. The current scanner's documented scope is narrower and must remain the authority for the exact protected set described below.

## Map and state setup / host survival

The current map ledger is static and complete as a row table, but 55 selectable rows remain unbound and therefore cannot be automatic current-map candidates. `IW-003` ACX and `IW-032` BFX are concrete unbound examples; the CSV records `anchor_binding_mode = unbound` and a non-selectable host-survival implication.

Planner reservation is host-first and attestation-gated. `common/scripted_effects/006_independence_wave_package_planner_effects.txt:95-138` requires the exact content attestation, force-package mapping, candidate country, anchor, and primary host before reservation; `:270-313` computes host loss capacity as owned states minus one protected remnant and rejects an anchor with `host_survival`; `:317-370` applies the same check to compact and extended territory. The shared coordinator's host selection also excludes the mandatory anchor and protects a legal remnant (`common/scripted_effects/chaosx_liberation_release_effects.txt:247-349`; `common/scripted_triggers/chaosx_liberation_release_triggers.txt:150-185`).

Before ownership mutation, the execution path validates all frozen package rows and exact host/anchor ownership (`common/scripted_effects/006_independence_wave_execution_effects.txt:1-86`), relocates host capitals only while the plan is locked (`common/scripted_effects/006_independence_wave_execution_effects.txt:488-526`; `common/scripted_effects/chaosx_liberation_release_effects.txt:1430-1479`), and rejects a failed relocation. Pre-execution cancellation restores every original capital (`common/scripted_effects/006_independence_wave_execution_effects.txt:658-674`; `common/scripted_effects/chaosx_liberation_release_effects.txt:1376-1429`). Post-mutation failures use the compensating rollback ledger (`common/scripted_effects/006_independence_wave_execution_effects.txt:650-668`; `common/scripted_effects/chaosx_liberation_release_effects.txt:1797-1839`).

The shared host validator checks planned loss count, owned-state snapshots, protected-state identity, and protected-state ownership (`common/scripted_effects/chaosx_liberation_release_effects.txt:1192-1290`). This is strong source-level protection, but no live allocator, save/load, or in-game host-survival observation was performed in this read-only audit.

## Politics, leaders, portraits, flags, advisors, and parties

No new political, leader, portrait, flag, advisor, or party surface was changed by this audit. The 15 attested package set has package-specific evidence in its current handoffs, but the 178 unattested rows remain blocked until those surfaces are individually audited. In particular, the current completion evidence keeps MNT, FSM, CHU/ASY, FIJ, DOX, and SOK outside attestation for source/provenance or package-completeness reasons (`docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_current_completion_evidence_v106_2026_08_03.md`).

Vanilla/reused carriers retain vanilla history, flag, meaningful tree, and identity; Event 006 must add only an origin-gated overlay or package after proving the carrier is not living under another protected origin (`docs/events/006_independence_wave/country_api.md:27-31`). Africa overlap rows preserve the same boundary: `COG` IW-101 is overlay-only, and MLI/TIG/SUD/ZIM are Event 012 vanilla identities rather than Event 006 same-identity overlaps (`docs/events/006_independence_wave/systems/country_registry.md:127-145`).

## Focus, decisions, ideas, and asset adoption

Event 006 uses one shared `independence_wave_focus_tree`, with 318 unique definitions (184 direct, 134 full shared definitions, and 27 import roots) documented at `docs/events/006_independence_wave/systems/generic_focus_tree.md:3-17`. Full-framework assignments load that tree only through `common/scripted_effects/006_independence_wave_focus_effects.txt:33-72`; additive assignments never call `load_focus_tree` and require a reviewed owning carrier.

The final package barrier rejects an adapter unless it has either the generic focus contract and the baseline generic AI profile (`common/scripted_effects/006_independence_wave_package_dispatch_effects.txt:32-60`). The current carrier trigger statically recognizes ICE/`iceland_tree` and TRA/`austro_hungarian_releasable_focus` (`common/scripted_triggers/006_independence_wave_focus_triggers.txt:55-80`); TRA is now admitted as IW-023 by the post-TRA runtime/scenario reconciliation. Older handoffs that say ICE is the only recognized carrier are superseded by this current trigger. FORM-08 remains a separate fail-closed gate.

No package may claim that a `shared_focus` declaration injects nodes into an unrelated living tree. Existing meaningful vanilla trees remain authoritative; an unreviewed carrier must fail closed (`docs/events/006_independence_wave/country_api.md:37-39`; `common/scripted_triggers/006_independence_wave_focus_triggers.txt:55-69`). Decisions, ideas, assets, and AI are likewise package-owned obligations and cannot be inferred from registry membership.

## Tag reuse, collision scope, and vanilla exclusions

The current command `python -B .tools/audit_chaosx_country_tags.py --surface-scan` returned: `Protected Event 006/Soviet tags: 136; external country-definition collisions: 0; external identity-surface collisions: 0; random-event roots skipped: 1`.

This is a scoped PASS, not an all-Chaos namespace guarantee. The scanner protects Event 006 plus 34 Soviet Collapse tags and scans vanilla, Workshop, and sibling local roots (`.tools/audit_chaosx_country_tags.py:2-15`, `:182-214`, `:300-377`). By policy it excludes CBB/CBD, Fallout, and other event namespaces, excludes existing ChaosX carriers `REV`, `ZIN`, and `ZZZ`, and skips Random Events Mod workshop ID `3199436992` (`.tools/audit_chaosx_country_tags.py:9-15`, `:38-48`, `:175-203`). Vanilla is included in the scanned external roots, so the zero result covers protected-tag collision against vanilla; it does not prove absence of collisions for excluded Chaos/event surfaces.

Shared tags are intentional reuse, not duplicate definitions. The API requires exact package ID, anchor/location, reservation group, and origin/provenance before loading content (`docs/events/006_independence_wave/systems/country_registry.md:152-172`). No duplicate vanilla history or second tag was introduced by this audit.

## AI and playability

The generic AI assignment is tied to the same focus contract and is required by the final package barrier. Source-level AI profiles exist for accepted packages, but this audit did not run live weighted selection, allocator execution, save/load, or player-owned scenario play. The current completion authority still marks overall AI/balance acceptance unverified, the 14-country simultaneous witness unresolved, and the 20-country capacity structurally impossible with the current 15 attestations (`docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_current_completion_evidence_v106_2026_08_03.md`).

## Validation and skipped checks

Meaningful checks run:

- Parsed the candidate registry CSV and confirmed 206 rows, disposition counts, 13 overlay-only rows, and 178 unattested non-overlay rows by comparing its package IDs against the current adapter/attestation triggers.
- Parsed the installed map-binding CSV and confirmed 206 rows, 55 unbound rows, 13 overlay routes, 134 fixed-anchor rows, 4 choose-one host rows, and zero non-empty `missing_current_state_ids` values.
- Ran `.tools/audit_chaosx_country_tags.py --surface-scan`; result is recorded above.
- Re-read current adapter/attestation, planner host checks, execution rollback, generic focus, collection/API, and current completion-evidence sources.

Skipped meaningful validation: no Hearts of Iron IV process, live release, map write, save/load, player-owned scenario, live focus rendering, runtime AI probability, or Technology Tree Viewer inspection. The installed package exposes no Technology Tree Viewer, so technology-tree runtime coverage remains unresolved.

## Remaining blockers and handoff

1. Keep the central attestation gate unchanged until each candidate package has complete country-specific identity, map, host, politics, leader/portrait, flag, advisor, forces/technology/industry, ideas/decisions, focus/overlay, AI, localisation, asset, cleanup, and provenance evidence.
2. Do not treat 15 attested IDs as a simultaneous 14-package witness; the current completion authority explicitly says the 14-country witness is unresolved and the 20-country capacity is structurally impossible at the current attestation count.
3. Do not broaden the collision scanner or remap excluded tags without an explicit namespace decision; the current zero result is limited to 136 protected Event 006/Soviet tags and one skipped Random Events root.
4. Preserve vanilla histories and meaningful trees for reused carriers; resolve shared CHU/BIA package identity by package ID and anchor, never by tag alone.
5. Keep overlay-only rows non-selectable and all unbound rows fail-closed until an authoritative map binding exists.

No fallback, admission bypass, broad identity redesign, new country package, gameplay patch, or asset substitution was introduced. The only changed file from this audit is this dated handoff.
