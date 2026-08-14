# Event 006 civilian-factory cost-disclosure crosscheck

Date: 2026-08-14

Scope: read-only cross-decision scan of current Event 006 `custom_cost_text` selectors paired with `modifier = { civilian_factory_use = ... }`. The scan excludes Join/admission changes, portraits, flags, workbook data, and gameplay patching. The already repaired DM-16, DM-42, HBX federal asset ledger, and DM-62 selectors were checked as resolved and are not counted as live findings.

## Historical baseline disposition (superseded below)

No gameplay source was edited by this audit. The source baseline was HEAD `7bb935ee5`; the shared decision and localisation files also contained the owner-applied DM-10/DM-36 repair in the working tree while this audit ran. The owner repair changes DM-10 `independence_wave_establish_treasury_and_currency` to `independence_wave_cost_administration_major` and DM-36 `independence_wave_buy_out_concession` to `independence_wave_cost_strategic_major`, with complete base, tooltip, and blocked keys. Those two findings were recorded as resolved in the then-current owner worktree and are superseded by the later committed source receipts referenced below.

At that historical baseline, the remaining scan found accepted-matrix cost disclosures that disagreed with the active factory reservation, plus package/formable callers that needed dedicated factory-aware text. The strongest safe selector-only recommendation was DM-49: the owner-added `independence_wave_cost_strategic_major` triplet exactly matched its existing major reservation and the accepted matrix's three-factory burden. No selector or localisation patch was applied here because the parent explicitly requested a read-only crosscheck.

## Superseding current-source disposition (2026-08-14)

Owner source repairs after the `7bb935ee5` audit baseline supersede the historical selector findings for DM-49/DM-50 through `e1af5c85b`, DM-51/DM-52/DM-56/DM-57 through `3f8c18e49`, ARX through `47c60e51a`, and DM-16/DM-42 plus the HBX federal-asset-ledger selector through `21d769e4f`.

Current source pairs DM-49/DM-50 with `independence_wave_cost_strategic_major` and a major factory modifier, DM-51 with `independence_wave_cost_border_ultimatum_major` and a major modifier, DM-52/DM-56 with `independence_wave_cost_integration_major` and a major modifier, DM-57 with `independence_wave_cost_breakaway_sponsorship_standard_factory` and a standard modifier, and ARX/DM-16/DM-42 with `independence_wave_cost_diplomatic_standard_factory` and a light modifier.

The HBX federal-asset-ledger selector uses `independence_wave_cost_diplomatic_standard_factory` with its light factory modifier. Before the owner implementation addendum below, the federal-arsenal and Sacramento convention selectors were the remaining light-factory disclosures without factory-aware text.

The factory-aware security-standard and administration-standard triplets exist, so the two selectors were aligned by the owner without changing payment or lifecycle code. No blanket HBX admission change is implied by this disclosure repair.

The historical findings below remain preserved as dated evidence, with only the repaired selector rows superseded by the current-source disposition above.

## Severity-sorted findings

### P1 — Accepted matrix still has major reservations shown as standard or omitted

The current Event 006 matrix audit (`docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_decision_mission_matrix_current_audit_2026_08_02.md`) specifies three civilian factories for DM-49, DM-50, DM-51, DM-52, and DM-56, and two for DM-57. Current source and localisation disagree as follows:

| Matrix row | Current source | Current display defect | Safe disposition |
| --- | --- | --- | --- |
| DM-49 `independence_wave_sponsor_plebiscite` | `common/decisions/006_independence_wave_decisions.txt:3044-3069`; strategic text, `CIVILIAN_FACTORY_MAJOR` modifier | `independence_wave_cost_strategic` base/tooltip/blocked keys display `civilian_factory_standard` (two), not major (three) | Safe selector-only follow-up: use existing `independence_wave_cost_strategic_major` for this ID. |
| DM-50 `independence_wave_negotiate_transfer` | `common/decisions/006_independence_wave_decisions.txt:3122-3151`; strategic text, `CIVILIAN_FACTORY_MAJOR` modifier | Same standard-two versus major-three disclosure | Same exact selector-only follow-up as DM-49; keep the two changes separately reviewable. |
| DM-51 `independence_wave_prepare_border_ultimatum` | `common/decisions/006_independence_wave_decisions.txt:3180-3212`; `independence_wave_cost_border_ultimatum`, `CIVILIAN_FACTORY_MAJOR` | All three `independence_wave_cost_border_ultimatum*` strings omit the three-factory reservation | Add a dedicated factory-aware border triplet or append the accepted major amount to all three existing variants; do not change the strategic/security payment helpers. |
| DM-52 `independence_wave_integrate_settled_district` | `common/decisions/006_independence_wave_decisions.txt:3284-3305`; `independence_wave_cost_integration`, `CIVILIAN_FACTORY_MAJOR` | Integration base/tooltip/blocked strings display the standard two-factory token | Add an integration-major triplet and switch only this ID; changing the shared integration key would affect standard-tier callers. |
| DM-56 `independence_wave_integrate_member_region` | `common/decisions/006_independence_wave_decisions.txt:3448-3471`; same integration selector and major modifier | Same standard-two versus major-three disclosure | Same dedicated integration-major treatment as DM-52. |
| DM-57 `independence_wave_sponsor_another_breakaway` | `common/decisions/006_independence_wave_decisions.txt:3506-3527`; `independence_wave_cost_breakaway_sponsorship`, `CIVILIAN_FACTORY_STANDARD` | All three breakaway-sponsorship strings omit the accepted two-factory reservation | Add the accepted standard factory amount to this dedicated triplet; do not reuse a generic strategic or integration key. |

DM-10 and DM-36 were the same class of defect and are resolved in the current owner worktree by the new `independence_wave_cost_administration_major` and `independence_wave_cost_strategic_major` triplets. Their source selectors, payment helpers, gates, AI, durations, and cleanup remain otherwise unchanged.

### P2 — Accepted FORM-03 rows show two factories while reserving one

The accepted matrix requires administration-standard resources plus one civilian factory for FORM03-D01, D02, D04, and D14. The current source uses `CIVILIAN_FACTORY_LIGHT` (one) but selects `independence_wave_cost_administration_standard`, whose complete triplet displays `civilian_factory_standard` (two):

- `common/decisions/006_independence_wave_form03_decisions.txt:207` — `independence_wave_form03_convene_language_convention` (FORM03-D01).
- `common/decisions/006_independence_wave_form03_decisions.txt:240` — `independence_wave_form03_open_multilingual_service_examinations` (FORM03-D02).
- `common/decisions/006_independence_wave_form03_decisions.txt:324` — `independence_wave_form03_establish_federal_language_appeals` (FORM03-D04).
- `common/decisions/006_independence_wave_form03_decisions.txt:666` — `independence_wave_form03_repair_language_settlement` (FORM03-D14).

This is an amount-disclosure mismatch, not a missing key. A dedicated administration-standard-plus-light-factory triplet is the narrow repair; changing the shared administration-standard key would make the many two-factory callers incorrect. FORM-03 remains subject to its separate readiness/admission evidence, so this is queued for the formable owner rather than patched here.

### P2 — Formable-family and admitted package callers have source-backed omissions

The following current decisions reserve factories but select a triplet that does not show them:

- `common/decisions/006_independence_wave_form01_02_04_decisions.txt:14` — `independence_wave_form0124_authorize_full_integration`, diplomatic-standard text with the standard factory modifier. The current generic diplomatic key has no factory; a standard-factory-specific key is required.
- `common/decisions/006_independence_wave_form01_02_04_decisions.txt:189` — `independence_wave_form01_rotate_congress_session`, custom administrative/diplomatic text with a light factory modifier. The custom triplet should disclose the existing one-factory reservation.
- `common/decisions/006_independence_wave_form01_02_04_decisions.txt:240` — `independence_wave_form01_coordinate_maritime_defence`, security-standard text with a light factory modifier.
- `common/decisions/006_independence_wave_form01_02_04_decisions.txt:307` — `independence_wave_form02_chart_convoy_routes`, diplomatic-standard text with a light factory modifier.
- `common/decisions/006_independence_wave_form01_02_04_decisions.txt:339` — `independence_wave_form02_build_air_warning_chain`, security-standard text with a light factory modifier.
- `common/decisions/006_independence_wave_form01_02_04_decisions.txt:416` — `independence_wave_form04_establish_public_peace_court`, diplomatic-standard text with a light factory modifier.
- `common/decisions/006_independence_wave_form01_02_04_decisions.txt:432` — `independence_wave_form04_coordinate_corridor_security`, security-standard text with a light factory modifier.
- `common/decisions/006_independence_wave_mediterranean_decisions.txt:54` — admitted IW-017/COR `independence_wave_cor_secure_mountain_post_road`, security-light text with a light factory modifier.
- `common/decisions/006_independence_wave_mediterranean_decisions.txt:194` — admitted IW-018/ARX `independence_wave_arx_restore_cagliari_shipping_office`, diplomatic-standard text with a light factory modifier.

The ARX selector is a particularly clean one-line candidate: `independence_wave_cost_diplomatic_standard_factory` already exists with the same standard diplomatic resources and light factory amount. The FORM-02 convoy-chart and FORM-04 peace-court selectors have the same exact source shape. The security and custom administrative/diplomatic callers do not have an existing exact factory-aware triplet and should not be forced through a shared generic key.

HBX `independence_wave_hbx_screen_federal_arsenals` at `common/decisions/006_independence_wave_pacific_decisions.txt:37-51` has the same security-standard/light-factory omission, but IW-184/HBX remains held at the canonical content-attestation gate. It is context-limited rather than an admitted-surface patch candidate. The IW-043/IW-058 security-standard callers have the analogous omission and remain behind their package-admission boundary; they are not safe to widen or normalize in this tranche.

## Safe selector-only recommendations versus design-dependent work

The recommendations below are historical baseline proposals; DM-49/DM-50, ARX, DM-16, DM-42, and the HBX federal-asset-ledger entry are superseded by the current-source disposition above, while the remaining formable and design-dependent entries retain their dated status.

Safe and mechanically complete selector replacements, not applied in this read-only task:

1. DM-49 `independence_wave_sponsor_plebiscite` -> `independence_wave_cost_strategic_major`. The accepted matrix requires three factories, the current modifier already reserves the major tier, and the owner has supplied the complete major triplet.
2. DM-50 `independence_wave_negotiate_transfer` -> the same existing major strategic triplet.
3. IW-018/ARX `independence_wave_arx_restore_cagliari_shipping_office` -> `independence_wave_cost_diplomatic_standard_factory`. The package is admitted and the existing key exactly matches its light factory modifier.
4. FORM-02 `independence_wave_form02_chart_convoy_routes` and FORM-04 `independence_wave_form04_establish_public_peace_court` have the same exact diplomatic-standard/light-factory selector shape, subject to the formable owner applying them together with the family handoff.

Design-dependent or multi-key follow-ups:

- DM-51 and DM-57 need dedicated border/breakaway triplets or carefully scoped additions to their existing custom triplets.
- DM-52 and DM-56 need an integration-major triplet because the shared integration key serves the standard tier.
- FORM03-D01/D02/D04/D14 need an administration-standard/light-factory triplet because the shared administration key serves the standard tier.
- Security-light/security-standard factory callers need dedicated keys; adding factory text to the shared security keys would misstate every non-factory caller. The same applies to the FORM-01/02/04 custom administrative/diplomatic surface.
- HBX and IW-043/IW-058 remain admission/context blockers, not grounds for central admission widening.

## Decision category lifecycle notes

- Government DM-10 and Patron DM-36 retain their existing one-time/targeted lifecycle, timeout/removal effects, AI, and cleanup after the owner selector repair.
- Borders DM-49 through DM-52 retain valid state/host/claim gates, target or operation guards, timed outcomes, and generation-safe cleanup. The current findings are disclosure-only.
- Formables DM-56 retains its controlled-member-region, one-time-per-region/origin, integration, and failure cleanup contract. Only the displayed factory tier is wrong.
- High Chaos DM-57 retains Evolution-5, candidate, cooldown, and sponsored-state output guards. Only its custom cost triplet omits the reservation.
- FORM-03 D01/D02/D04/D14 retain their carrier-state invalidation, cancellation, and one-per-lifecycle protections. The current mismatch is the displayed one-versus-two factory amount.
- COR and ARX retain package identity, capital-control cancellation, project exclusivity, timeout/failure, and focus-linked completion behavior. No lifecycle code was changed.

## Mission quality notes

| Surface | Owner/category/region | Requirement and duration | Success/failure | Duplicate risk |
| --- | --- | --- | --- | --- |
| DM-49 | Regional power / Borders / surveyed claimed state | Valid claim, local support, observer, 240-day targeted operation | Transfer or stronger claim; fraud/refusal/unrest branches | Target cooldown and state/origin markers remain present |
| DM-50 | Regional power / Borders / surveyed host-state pair | Valid host, compensation route, 180-day bilateral operation | Peaceful transfer or host mobilisation | Bilateral target cooldown and generation-safe state result |
| DM-51 | Regional power / Borders / surveyed state | Security/route commitment, 120-day crisis | Transfer, war, or mediated settlement; failed bluff/isolation branch | One active ultimatum operation guard |
| DM-52 | Regional power/formable / Borders / controlled settled state | Control, connection, local support, 360-day integration | Core/durable integration or resistance/autonomy failure | One-time state and origin markers |
| DM-56 | Formable / Formables / controlled member region | Administrative path and formable state proof, configured integration duration | Core/stability/shared institutions or resistance/secession outcome | One-time region/origin markers and formable cleanup |
| DM-57 | Radical Event 006 country / High Chaos / candidate state | Evolution 5, valid candidate, 180-day operation and 365-day cooldown | Sponsored opening-strength/route record or exposure/sanctions/host-war branch | One candidate sponsorship and sponsored-state consumption contract |
| FORM03-D01/D02/D04/D14 | LCX carrier / FORM-03 / member language and legal scope | Focus/model gates, 150–180 days, one lifecycle use | Model, accommodation, or repair result; carrier invalidation/cancellation branch | One-per-lifecycle or one-per-failure-cycle guards |

## Cost, requirement, AI, and route notes

The crosswalk found 619 current `custom_cost_text` selectors across the Event 006 decision files and 180 unique keys. Every unique key currently has base, `_tooltip`, and `_blocked` localisation entries; there are no stale or unresolved cost-key references. The live defects are amount/selector mismatches, not missing localisation keys.

The selected factory modifiers are source-backed reservations. They do not change the payment effects, but the decision card must disclose the reservation at the same tier as the modifier and accepted matrix. No new payment helper, trigger, AI score, cooldown, route gate, or cleanup behavior is proposed by this audit.

AI and route validity were not changed. The affected decisions retain their existing owner, target, route, capital, generation, cooldown, and package checks. The probability route is structural evidence only here; no balance target or AI patch is justified by a cost-text crosscheck.

## Localisation and cleanup notes

The affected base/tooltip/blocked trios are present and UTF-8 BOM localisation remains the repository contract. The needed repairs should be scoped to new dedicated keys or exact selector replacements; do not alter shared generic keys in a way that changes unrelated callers.

No exploit, free-unit loop, equipment-farming loop, core-spam loop, or cooldown bypass was found in this scan. A factory reservation is already active in source; the defect is that the player-facing card does not show the same commitment. No cleanup or admission change is required for the recommended selector-only fixes.

## Mandatory evidence and validation

Required offline Paradox wiki decision, trigger, effect, modifier, localisation, scope, and data-structure pages were consulted alongside the vanilla decision/localisation documentation and decision precedents before this audit.

Current shared decision probability inspection completed through `hoi4.probability_inspect` with `PROBABILITY_SOURCE_INSPECTED`: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/168da378b710a60edf696873ed5cc4cf23732eadf1ae7f879f75abf66cd3c210/2dc8e729a835ac609a24d2855806cffa821b98d3c3018e426ddb23cfc2c1e265/probability-inspect-ad520c11033d.json`. It reports 10 decision candidates, 79 required inputs, zero unresolved inputs, zero available candidates, and `poolComplete=false`.

Current Pacific mission probability inspection completed with `PROBABILITY_SOURCE_INSPECTED`: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/959b77780f28a9a8b3b9c46fc6c7d3567f99e0066e9d682be48cc13dc68ee31b/45b86e6f512c4efe1d4fe7bfd79ac2c9e61f28d8eac1c5f009d0e56b7a73652e/probability-inspect-9b4a668f779a.json`. It reports 28 mission candidates, 17 required inputs, zero unresolved inputs, zero available candidates, and `poolComplete=false`.

The MCP pools are incomplete and no probability compare/evaluate pass was needed because no AI or weighted source was changed. These artifacts therefore support source-linked structure only, not campaign balance or live availability. No custom scripted GUI was in scope: the affected text is rendered by the standard decision card rather than a new decision-owned GUI, so no GUI rewrite was attempted.

Validation consisted of the source/localisation crosswalk, accepted-matrix lookup, exact selector inspection for DM-10/DM-36 and the remaining candidates, and a complete custom-cost key/triplet scan. Live HOI4 execution, save/load, and runtime decision-card observation were not run; they remain parent/user validation surfaces.

No files were changed by this audit. Parent-owned concurrent changes, including the DM-10/DM-36 selector/triplet repair and unrelated working-tree edits, were preserved. No admission, Join, assets, portraits, flags, workbook, AI, payment effect, or cleanup edits were made.

## Owner implementation addendum — HBX factory disclosures (2026-08-14)

The two remaining admitted IW-184/HBX light-factory disclosure mismatches were repaired in `common/decisions/006_independence_wave_pacific_decisions.txt`: `independence_wave_hbx_screen_federal_arsenals` now selects `independence_wave_cost_security_standard_factory`, and `independence_wave_hbx_seat_sacramento_civic_convention` now selects `independence_wave_cost_administration_standard_factory`.

The existing factory-aware localisation triplets already match the one-factory modifier on each decision. The adjacent coastal-supply-bureaus project retains the generic administration-standard selector because it reserves the standard, not light, factory tier.

No payment helper, requirement, AI score, duration, route gate, project lifecycle, admission, Join, asset, or cleanup behavior changed. This is a selector-only disclosure repair; the existing structural probability receipts remain sufficient and no quantitative balance claim is made.

## Follow-up implementation addendum — FIJ and AFX disclosures (2026-08-14)

The exhaustive current-source scan found two additional selector/tier mismatches. `independence_wave_fij_convene_constituent_congress` now selects `independence_wave_cost_administration_standard_factory` for its existing light-factory reservation. IW-177/FIJ remains adapter-only and fail-closed; this source correction does not alter its portrait, flag, FORM-39, or central-admission gates.

The admitted AFX `independence_wave_afx_convene_meuse_industrial_conference` now selects `independence_wave_cost_strategic_major` for its existing major-factory reservation. The same source pass also preserves the owner’s file-scoped `@` mirrors for factory fields that reject shared constant tokens. No route, payment, AI, timing, lifecycle, admission, Join, asset, or cleanup behavior changed.
