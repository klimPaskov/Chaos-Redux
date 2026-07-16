# Event 006 IW-004 Brittany country-package audit

Date: 2026-07-15
Auditor role: `chaosx_country_package_auditor`
Scope: bounded `IW-004` / `BRI` package only

## Verdict

The BRI gameplay package is structurally complete and **bounded-package commit-safe after the later parent repair**, but it is not admitted to automatic runtime or scenario selection. The corrected corps-commander small portrait is a separately composed `65x67` HOI4 army dossier, and the repaired custom congress follows the shared preparation/ready/proclamation transaction.

FORM-01/KCX passed its later operational re-audit and readiness promotion. The unresolved Debeauvais rights-cleared source remains documented. The immutable BRI identity proof is present, while runtime content attestation and SCN-008 admission remain separately fail-closed.

## Narrow corrections made

### `common/script_constants/006_independence_wave_brittany_constants.txt`

- Corrected `independence_wave_brittany_ai.founding_restraint` from `250` to `-250`.
- Corrected `independence_wave_brittany_ai.settled_restraint` from `400` to `-400`.
- Evidence: official `common/ai_strategy/_documentation.md` defines targetless `avoid_starting_wars` as additive with `conquer` and demonstrates `value = -200`; vanilla `common/ai_strategy/default.txt` uses `-400`. The previous positive values encouraged the opposite of the named defensive posture.

### `localisation/english/006_independence_wave_brittany_l_english.yml`

- Made `independence_wave_bri_project_failure_effect_tt` disclose the recognition loss actually applied by `independence_wave_bri_apply_project_failure`.
- Replaced duplicated BRI compact maxima, threshold, and delta numbers with the existing `independence_wave_brittany_pressure.*` script-constant localisation tokens. The visible values now remain aligned with tuning.

### `docs/plans/006_independence_wave_plans/subagent_handoffs/006_bri_country_package_implementation_2026_07_15.md`

- Corrected the cleanup description. The live adapter does not retire the two generated characters; it leaves them registered behind exact package gates, matching `docs/006_independence_wave_brittany_package.md` and preserving guarded repeat initialization.

The later parent repair adds the dormant exact BRI identity helpers required by the runtime adapter. It does not change an asset, FORM-01 readiness, content-attestation, or SCN-008 admission gate. No audit subagent commit was created.

## Identity, state, and allocator evidence

- Vanilla owns `BRI` through `common/country_tags/00_countries.txt` and `countries/Brittany.txt`; vanilla history fixes the capital at state `14` and provides the existing country leaders, politics, technologies, and adviser recruitment.
- Chaos Redux adds no competing `BRI` country-tag definition, country file, country-history file, or flag family. All twelve vanilla base/ideology flag variants across normal, medium, and small sizes remain authoritative.
- `independence_wave_load_package_iw_004` binds only `BRI`, reservation group `rg_14`, and state `14`, taking the live owner of state 14 as the primary host. `independence_wave_reserve_package_iw_004` publishes only that anchor and no compact or extended state.
- `can_initialize_independence_wave_iw_004_package` and the prepared/final proofs require the exact original tag, package ID 4, state-14 ownership and control, state-14 capital, and a living former host distinct from BRI.
- The shared reservation layer computes each host's loss ceiling as `num_owned_states - 1` and rejects the anchor with `host_survival` when the host cannot lose it. The package cannot consume the host's protected last state.
- `.tools/audit_event6_allocator.py` passed with 149 publishers, the frozen automatic counts, and the required `all anchors -> compact -> extended -> lock` order. BRI's publisher remains isolated by package ID, tag, reservation group, and state.
- Full-framework assignment is confined to the active package. Vanilla BRI has the reviewed generic/minimal tree rather than a bespoke meaningful tree; the mod does not overwrite vanilla files or a living BRI merely to install Event 006 content.

## Characters, politics, and vanilla preservation

- Setup creates only the guarded fixed-name fictional humans `BRI_independence_wave_civic_delegate` (Tangi Kerbrat, oligarchism role) and `BRI_independence_wave_coastal_commandant` (Jodoc Tanet, despotism role and corps commander). Both names and portraits are male-presenting and neither character is marked female.
- Character generation is guarded by exact `NOT = { has_character = ... }` checks. Portrait application is separately guarded by `has_character`; Jodoc's commander proof requires `is_corps_commander = yes`.
- The package readiness proof requires the vanilla advisers `BRI_coi`, `BRI_stc`, `BRI_acd2`, `BRI_nccr`, and `BRI_mt` to exist and retain adviser roles. The mod neither regenerates nor duplicates them.
- Vanilla's Yann-Morvan Gefflot, Morvan Marchal, Olier Mordrel, and Maurice Duhamel leader definitions and their official sprite bindings remain untouched. The democratic baseline uses the accepted Duhamel political family; no generated historical substitute is installed.
- All six configured popularity sets total exactly 100. Five mutually exclusive route governments map to constitutional, popular-council, traditional, emergency-military, and patron-client outcomes; radical sovereignty and a Mordrel government remain explicitly excluded.

## Lifecycle, decisions, focuses, forces, and AI

- The two visible values start at `30` and `25`, clamp to `0..100`, and require both to reach `60`. Lifecycle refresh keeps exactly one of `bri_divided_ports_and_language_state` or `bri_bilingual_maritime_compact` active.
- The five package focuses form one bounded branch. Their compact deltas take the focus-only path from `30/25` to `70/75`, so the stable threshold is reachable without decision farming.
- The category contains 15 entries: one 480-day mission and fourteen decisions. All 15 have matching cleanup removal calls. The eleven timed projects are included in the serialization trigger; the remaining one-shot decisions are immediate.
- Every custom cost gate has a matching payment helper. Timed projects pay on start, apply rewards on completion, and apply bounded failure logic on relevant cancellation. Capital loss and mission timeout are handled. Both persistent BRI variables and all 26 package/IW-004 flags set on the bounded surfaces have cleanup partners; route and lifecycle ideas are removed.
- Force package row `p4` resolves to profile `5` (`coastal_maritime`), tradition `58`, reinforcement mask `1543`, inheritance mask `1`, and research-sensitive value `0`. Mask `1543` decodes to exactly the accepted five paths: integrate militias, regional guards, secure depots, professional officers, and capital/border defense.
- Inheritance mask `1` enables navy and excludes air. The shared transfer effect sets size, stockpile, army, and air ratios to zero and supplies only the approved navy ratio when the force/port gates pass.
- The package has no scripted war declaration. After correction, founding, civic, labor, emergency, and patron AI profiles apply negative war-start restraint while retaining route-shaped construction, equipment, and severe-host-threat defense priorities.
- The French-ledger decision and matching focus use the stored living former host, reduce claim/hostility/obligation/property/pressure/reconquest-fear ledgers, improve the border settlement, and never assume FRA as the runtime scope.

## FORM-01 and readiness closure

- BRI selects only `celtic_cooperation_state`, sets only `independence_wave_bri_form01_candidate`, and proves that BRI FORM-02/03/04 candidate flags are absent. Its custom congress now calls `independence_wave_formable_begin_preparation`, grants the BRI result only after `independence_wave_formable_transaction_ready`, and leaves final commitment to the shared proclamation action.
- The earlier direct-commit call-site defect and the shared FORM-01/KCX blockers are superseded by `006_bri_ajx_commit_readiness_reaudit_2026_07_16.md`, `006_form01_04_operational_reaudit_2026_07_16.md`, and `006_form01_04_readiness_promotion_2026_07_16.md`.
- Package ID 4 is present in the adapter registry, its exact `IW-004`/`BRI` availability helper exists, and the runtime preflight OR has the matching immutable identity branch. The compile-time content-attestation and SCN-008 scenario-preflight registries still admit only IW-006, IW-007, and IW-009, so these identity helpers cannot open BRI admission on their own.

## Localisation and asset evidence

- Mechanical coverage found 15/15 decision or mission title/description pairs, 5/5 package focus pairs, 7/7 idea pairs, both character pairs, the category, parties, and referenced tooltips. The 89 expected BRI keys are all present among 94 package localisation keys. The file remains UTF-8 with BOM.
- The final portrait contact sheet was visually inspected. Tangi Kerbrat is one distinctive fictional human civic leader in an authentic subdued HOI4 portrait style; he is not the withdrawn group, council, or emblem direction. Jodoc Tanet's large portrait is likewise a single fictional officer.
- Approved real vanilla BRI art was not regenerated, copied, or rebound. No BRI flag was replaced.
- Runtime DDS evidence:
  - civic leader: 156 by 210, SHA-256 `64AE374585C2A8B3A26BBD9A1E8880E182FDAFA93540BFB84E6C6D87647AB6B4`;
  - commandant large: 156 by 210, SHA-256 `F1603D707170002E7729C535E6DDD990CDFCC7E03F221684E1E6C821F12366C1`;
  - commandant small: **65 by 67**, SHA-256 `12C1A20D2CC1234895E7AF557BDA9BAF7CDDCA58593527194B5EDAD3AF058684`.
- The corrected commandant small is a separately composed HOI4 army dossier, documented and reviewed in `army_small_dossier_correction_2026_07_15`; it is not a mechanical reduction of the large portrait.

## Simplifications, omissions, and blockers

1. **Debeauvais provenance blocker:** no rights-cleared individual source suitable for a distinct Debeauvais portrait is available. The weak 1928 group image was not misrepresented, sharper uncertain-rights images were not used, and no generated likeness or substitute person was created.
2. **Admission gates intentionally closed:** runtime content attestation and SCN-008 remain outside this bounded package transaction and fail closed. The exact BRI identity proof is a non-authorizing prerequisite, not an admission grant.

The earlier Jodoc army-small and shared FORM-01 blockers are closed by the corrected `65x67` dossier package, the post-repair family operational re-audit/readiness promotion, and the repaired custom congress transaction.

No other gameplay route, focus, decision, mission, lifecycle value, force row, AI profile, localisation key, vanilla identity surface, or BRI cleanup surface was omitted or replaced with a fallback.

## References and skills used

Read directly and applied: `chaos-redux-subagents`, `chaos-redux-events`, `hoi4-focus-trees`, `hoi4-decisions-missions`, and `chaos-redux-event-assets`. The mandatory offline wiki pages, official vanilla documentation, vanilla BRI files, vanilla commander portrait precedents, accepted IW-004 specs/matrices/research, package documentation, implementation handoff, asset manifest, and GFX handoff were all consulted. No web Paradox wiki was used.
