# Event 006 IW-004 BRI / IW-010 AJX commit-readiness re-audit

> **Portrait-specific supersession (2026-07-16):** Portrait reviews, hashes,
> small-card evidence, and visual dossier claims based on the 2026-07-15 art are
> superseded by the male-HOI4 package manifest and final independent audit.
> Gameplay commit-safety findings remain historical; custom advisor icons stay
> withdrawn.

- Date: 2026-07-16
- Audit mode: independent read-only source, integration, asset, documentation, and staging-boundary review; parent repair closeout appended
- Working-tree baseline: `13dd2fef4` (`98ec32e93`, `2f867e9cd`, and `d0044b22e` are ancestors)
- Package scope: IW-004 Brittany (`BRI`) and IW-010 Saar (`AJX`) only
- Write boundary: this handoff only; no gameplay, localisation, asset, staging, or commit mutation

## Executive verdict

| Package | Bounded package commit-safe? | Automatic / SCN admission | Reason |
| --- | --- | --- | --- |
| IW-004 BRI | **Yes, after parent repair** | Intentionally closed and assessed separately | The custom congress now runs shared preparation, rewards only a ready transaction, reserves the shared formable-operation slot, and leaves final commitment to DM-55. Documentation and the corrected `65x67` army dossier are aligned. |
| IW-010 AJX | **Yes, after parent repair** | Intentionally closed and assessed separately | The equivalent congress and operation-lock repairs are present, targetless war restraint is negative, and FORM-04/asset documentation is aligned. |

The closed automatic-pool and SCN-008 admission gates are **not** used as reasons to reject either bounded package tranche. They remain separate from this package-level commit-safety verdict.

`98ec32e93` closes the former shared FORM-01/FORM-04 operational blockers. The operational re-audit and readiness-promotion handoff explicitly pass those families while keeping individual package admission as a separate gate. `2f867e9cd` is Cornwall documentation only and does not change either package verdict. `d0044b22e` replaces the mechanically resized army-small portraits and closes that earlier BRI/AJX asset defect, but several untracked package documents still describe the superseded files.

## Blocking findings

### B1 — both package congresses bypass the post-98ec transaction state machine

The baseline findings below describe the pre-repair call sites. The parent repair closes them as recorded in the closeout section.

The affected baseline call sites were:

- `common/decisions/006_independence_wave_brittany_decisions.txt:306-327`, especially `319-322`;
- `common/decisions/006_independence_wave_saar_decisions.txt:259-280`, especially `272-275`.

Both decisions currently do the following at timed removal:

1. set their package-specific congress-complete flag;
2. set `independence_wave_formation_congress_complete` directly;
3. call `independence_wave_decision_request_selected_formable_commit`;
4. grant the package network reward.

That sequence is no longer valid after `98ec32e93`:

- `can_independence_wave_prepare_selected_formable_transaction` requires transaction state `discovered` (`common/scripted_triggers/006_independence_wave_formable_registry_triggers.txt:390-419`);
- `independence_wave_formable_begin_preparation` changes the state to `congress_preparation`, builds the ledgers, and resolves the vote (`common/scripted_effects/006_independence_wave_formable_registry_effects.txt:1252-1262`);
- successful resolution alone sets state `formation_ready`, shared congress proof, and `independence_wave_formable_transaction_ready` (`1187-1201`);
- `can_independence_wave_commit_selected_formable` requires the family-specific strict proof, the ready flag, state `formation_ready`, a passing vote, and commit readiness (`common/scripted_triggers/006_independence_wave_formable_registry_triggers.txt:505-540`);
- the requested commit is guarded by that trigger, so a request issued while still `discovered` does not mutate the formable. It can only publish the blocked state.

The present package decisions therefore create a player trap: the strategic package congress cost is paid, the package and shared completion flags and rewards are granted, but the selected family is not committed.

The shared DM-54 action already demonstrates the required preparation call (`common/decisions/006_independence_wave_decisions.txt:2925-2963`). Shared DM-55 is the final commit action (`2966-2995`), revalidates the selected formable, pays the selected-method commit cost, and then requests the commit.

### B2 — both custom congresses are absent from the shared operation lock

`has_independence_wave_active_formable_operation` at `common/scripted_triggers/006_independence_wave_decision_triggers.txt:93-104` includes DM-54 and the SCO, WLS, AFX, AGX, RHI, and BAY custom actions, but not:

- `independence_wave_bri_convene_celtic_delegation`;
- `independence_wave_ajx_convene_rhenish_league_congress`.

Each package's local active-project trigger sees its own congress, but shared DM-54 does not consult those package-local triggers. DM-54 can consequently be started while either custom congress is active. Each custom decision also lacks the shared-operation exclusion in its own `available` block.

Repairing this requires one new tracked shared hunk in the currently clean `common/scripted_triggers/006_independence_wave_decision_triggers.txt:93-104`: add both decision IDs to the `OR` list. Each untracked package decision must also add `NOT = { has_independence_wave_active_formable_operation = yes }` to its own start conditions.

### B3 — AJX's targetless war restraint has the wrong sign

`common/script_constants/006_independence_wave_saar_constants.txt:77-78` defines:

```text
founding_restraint = 200
settled_restraint = 400
```

Those values feed targetless `avoid_starting_wars` strategies at `common/ai_strategy/006_independence_wave_saar.txt:34`, `:61`, and `:74`. The official vanilla strategy documentation at `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/ai_strategy/_documentation.md:197-203` documents negative values for war restraint and notes that the strategy is additive with conquer pressure. Positive `200`/`400` therefore strengthen, rather than suppress, war-starting pressure.

BRI has the intended sign pattern (`-250` / `-400`) in `common/script_constants/006_independence_wave_brittany_constants.txt:84-85`. AJX's two constants must be made negative before its tranche is commit-safe. This is a package-owned gameplay defect, not an admission-gate issue.

### B4 — package documentation and audit evidence are stale

The following evidence must be updated in the same repaired package transaction:

| File | Stale claim | Required correction |
| --- | --- | --- |
| `docs/events/006_independence_wave/northern_western_europe_packages.md` (Brittany section) | The package congress directly sets shared proof and requests commitment. | Describe custom preparation, shared resolution, `formation_ready`, and final DM-55 commitment. |
| `docs/plans/006_independence_wave_plans/subagent_handoffs/006_bri_country_package_implementation_2026_07_15.md:93` | Direct shared-state/FORM-01 handoff. | Replace with the repaired two-stage transaction. |
| same file `:167-182` | `50x67`, hash `1BDD8718...`. | Record the independently composed `65x67` file and hash `12C1A20D2CC1234895E7AF557BDA9BAF7CDDCA58593527194B5EDAD3AF058684`. |
| same file `:223-233` | Debeauvais, FORM-01, and independent-audit items are presented as open package blockers. | Preserve the provenance limitation as a future named-historical-expansion constraint, but record that distinctive fictional human roles are the accepted current package; mark FORM-01 and the independent package audit as resolved by the later evidence. |
| `docs/plans/006_independence_wave_plans/subagent_handoffs/006_bri_country_package_audit_2026_07_15.md:9-11`, `:61-64`, `:69-79`, `:81-85` | The old mechanical small portrait and old FORM-01 audit are current; no call-site defect was found. | Supersede with `d0044b22e`, `98ec32e93`, and this newly proven congress defect. Update the old localisation count if retained. |
| `docs/events/006_independence_wave/northern_western_europe_packages.md` (Saar section) | FORM-04 is only an unresolved external consumer. | Record the promoted operational FORM-04 adapters while keeping AJX automatic/SCN admission separate. |
| same file `:211-216` | The commander thumbnail is `50x67`. | Record the current `65x67` dossier texture. |
| `docs/plans/006_independence_wave_plans/subagent_handoffs/006_ajx_country_package_implementation_2026_07_15.md:17-22`, `:114-121`, `:202-213` | FORM-04 consumer and asset work remain unresolved. | Supersede with the promoted formable and completed asset ledger; retain only genuinely closed admission gates. |
| same file `:162-169` | AJX small hash `5B552E36...`. | Replace with `470C29FD6CC73F5B6A269969160F1F4D721F31D4197F3D070C8388765F269312`. |
| `docs/plans/006_independence_wave_plans/subagent_handoffs/006_ajx_country_package_audit_2026_07_15.md:159-160` | The custom congress does not bypass shared preparation/commit. | Record and close the proven call-site defect. |
| same file `:191-196` | AJX restraint works as intended. | Correct after the constants receive negative values. |
| same file `:241-252` | FORM-04 is an external unresolved blocker. | Supersede with the post-98ec operational result; leave admission separate. |
| `localisation/english/006_independence_wave_brittany_l_english.yml:79` | Congress wording implies immediate commitment. | Say that the delegation resolves preparation and, on success, leaves FORM-01 ready for the shared proclamation action. |
| `localisation/english/006_independence_wave_saar_l_english.yml:90` | Congress wording implies immediate proposal commitment. | Say that the delegation resolves preparation and, on success, leaves FORM-04 ready for the shared proclamation action. |

The dirty `docs/events/006_independence_wave/overview.md:88-107` already uses the correct post-98ec distinction: FORM-04 passed its operational audit while AJX automatic/SCN admission remains separate. The Saar package reference currently contradicts it.

## Exact post-98ec transaction sequence

The two custom congresses may retain their package flavor and their lower civilian-factory burden than generic DM-54. They must replace DM-54's preparation role, not replace DM-55's commit role.

### IW-004 BRI — `independence_wave_bri_convene_celtic_delegation`

1. **Start gate:** retain `has_stable_independence_wave_bri_compact`, `can_independence_wave_prepare_formable`, strategic affordability, capital control, and no BRI package project. Add `NOT = { has_independence_wave_active_formable_operation = yes }`.
2. **Reservation:** add this decision ID to the shared active-formable-operation trigger so DM-54 and every other registered custom formable action are mutually exclusive with it.
3. **Cost and duration:** retain `independence_wave_decision_pay_strategic` in `complete_effect`, `civilian_factory_standard`, and the strategic duration. The strategic cost is paid up front and is not refunded on cancellation or congress failure.
4. **Cancellation:** retain package/capital cancellation and add loss of `can_independence_wave_prepare_formable`. If BRI remains the exact active package, cancellation calls `independence_wave_bri_apply_project_failure`; no refund is issued. If package ownership itself has disappeared, do not mutate the former scope.
5. **Timed removal revalidation:** do not set either congress flag and do not call the commit wrapper directly. Revalidate `can_independence_wave_prepare_formable`.
6. **Valid completion:** call `independence_wave_formable_begin_preparation = yes`. That shared effect owns ledger construction, congress vote resolution, shared success proof, and shared rollback/failure state.
7. **Success-only package outcome:** only if `independence_wave_formable_transaction_ready` is present after resolution, set `independence_wave_bri_celtic_congress_complete` and call `independence_wave_bri_reward_network_project = yes`.
8. **Shared failure:** if `independence_wave_formable_transaction_failed` is present, do not set the BRI complete flag and do not grant the BRI network reward. Do not also call the BRI project-failure effect; the shared failed transaction already owns the larger congress rollback and penalty.
9. **Invalid removal:** if removal is reached without a valid preparation gate while BRI is still the exact package, call `independence_wave_bri_apply_project_failure`; do not publish shared proof or a package-complete flag.
10. **Final formation:** leave the transaction in `formation_ready`. The player or AI must use shared DM-55 `independence_wave_proclaim_military_union`, which rechecks `can_independence_wave_commit_selected_formable`, charges the selected-method aggregate commit cost, and requests the atomic FORM-01 commit.

### IW-010 AJX — `independence_wave_ajx_convene_rhenish_league_congress`

Apply the same sequence with AJX-specific identifiers:

1. retain `has_stable_independence_wave_ajx_compact`, shared preparation readiness, strategic affordability, capital control, and no AJX package project; add the shared-operation exclusion;
2. register `independence_wave_ajx_convene_rhenish_league_congress` in `has_independence_wave_active_formable_operation`;
3. retain the up-front strategic payment, `civilian_factory_standard`, strategic duration, and non-refundable cost semantics;
4. cancel on package loss, capital loss, or loss of `can_independence_wave_prepare_formable`; while AJX remains exact, use `independence_wave_ajx_apply_project_failure` and issue no refund;
5. at timed removal, revalidate and call `independence_wave_formable_begin_preparation = yes` rather than manually setting shared proof or requesting commitment;
6. only after shared resolution sets `independence_wave_formable_transaction_ready`, set `independence_wave_ajx_rhenish_congress_complete` and call `independence_wave_ajx_reward_network_project = yes`;
7. on `independence_wave_formable_transaction_failed`, set no AJX completion flag, grant no AJX reward, and do not stack the package project-failure penalty on the shared congress penalty;
8. on an invalid removal that still has exact AJX scope, use only the AJX project-failure effect;
9. leave the successful transaction for shared DM-55, which pays the selected-method cost and atomically commits FORM-04.

### Cost, reward, and failure ownership

| Stage | Owner | Exact semantics |
| --- | --- | --- |
| Custom congress start | BRI/AJX decision | Strategic resource payment, standard civilian-factory use, strategic timer. Payment is non-refundable. |
| Shared congress success | `independence_wave_formable_mark_congress_ready` | Major legitimacy, major recognition, standard capacity, minor security, standard instability reduction; state becomes `formation_ready`; shared proof and transaction-ready flag are set. |
| Package success supplement | `*_reward_network_project` | Standard legitimacy, recognition, and capacity; minor security; standard instability reduction; `network_standard` standing. This supplement is granted only after the shared ready flag exists. Retaining it preserves the current package-specific reward design. |
| Invalid/cancelled package project | `*_apply_project_failure` | Standard legitimacy loss, minor recognition loss, standard capacity loss, standard security loss, major instability rise; no refund. |
| Resolved shared congress failure | `independence_wave_formable_fail_transaction` | Decisive legitimacy loss, major recognition loss, standard capacity loss, zero security delta, decisive instability rise, rollback/failed state, and clearing of shared ready proof. Do not stack the package project-failure effect. |
| Final commitment | shared DM-55 | Revalidation, selected-method aggregate commit cost, then the guarded atomic family commit. No package decision should call this early. |

The existing committed SCO/WLS/RHI/BAY custom call sites use related pre-98ec direct-proof patterns. They were not inside this re-audit's mutation or completion scope and should receive a separate shared call-site audit; their presence is not a precedent for staging the broken BRI/AJX implementations.

## Passing package evidence

### Identity, focus, lifecycle, and localisation structure

- BRI is the vanilla tag at vanilla `common/country_tags/00_countries.txt:204`; Chaos Redux does not redefine its tag, dormant history, country file, or flags. Vanilla BRI has no living dedicated national tree displaced by these package-gated nodes.
- AJX has one Chaos Redux tag definition and no collision in vanilla, the approved Workshop references (`1521695605`, `2265420196`, `1458561226`), the installed Workshop root, or the local mod root. Its tracked country history remains a dormant shell.
- The Event 006 focus parser sees 138 focuses. AJX owns ten package/neutral-commission nodes and BRI owns five package nodes. No exact raw coordinate collision involving these nodes was found.
- Setup/cleanup parity is complete for the bounded package state: BRI package flags `24/24` and decision removals `15/15`; AJX package flags `26/26` and decision removals `14/14`.
- BRI localisation is UTF-8 BOM, has no duplicate keys, and covers the targeted package-facing references. AJX has the same structural result. The semantic congress wording identified in the baseline was corrected with the parent repair.
- Both packages remain fail-closed in automatic-pool and SCN-008 admission. This is intentional and independent of the package repair verdict.

### Formable integration after 98ec32e93

- FORM-01's accepted founder set remains SCO/WLS/BRI and BRI exposes no FORM-02, FORM-03, or FORM-04 route.
- FORM-04's accepted founder set includes RHI/AJX. The dirty removal of the old active-AJX exclusion from `006_independence_wave_rhineland_bavaria_package_triggers.txt` is consistent with the approved later-wave RHI/AJX coexistence direction.
- The post-98ec formable operational re-audit and readiness promotion close the old FORM-01 and FORM-04 consumer blockers. The custom congress repair was separately necessary because it was a package call-site defect, and is now present in both decisions.

### Portrait and asset review

The distinctive-human portrait constraint passes for the current bounded packages:

- BRI's Tangi Kerbrat and Jodoc Tanet are visually distinct single humans in a subdued HOI4 portrait treatment. No group, emblem-only portrait, generic institutional collage, or macabre direction is wired. The command army-small is independently composed rather than a transform-only reduction.
- AJX's Friedrich Hoffmann and Karl Becker are visually distinct single humans. The three institutional advisors are also separate fictional human dossier portraits. The neutral-commission emblem is correctly used as a focus icon, not as a person portrait.
- BAY and RHI approved leader/portrait assets have no dirty working-tree paths and were not changed by these tranches.

Current runtime evidence:

| Asset | Dimensions | SHA-256 |
| --- | --- | --- |
| BRI civic leader | `156x210` | `64AE374585C2A8B3A26BBD9A1E8880E182FDAFA93540BFB84E6C6D87647AB6B4` |
| BRI command large | `156x210` | `F1603D707170002E7729C535E6DDD990CDFCC7E03F221684E1E6C821F12366C1` |
| BRI command small | `65x67` | `12C1A20D2CC1234895E7AF557BDA9BAF7CDDCA58593527194B5EDAD3AF058684` |
| AJX Hoffmann | `156x210` | `53C80062DB72B4B8D4696A3921351A0CC4771EC9918975BCEB147A81EE00F976` |
| AJX Becker large | `156x210` | `555EBB4619BF6A672B7EDB96DAB847CD3FF69B00FC4D6A53D6CFF376556FAF51` |
| AJX Becker small | `65x67` | `470C29FD6CC73F5B6A269969160F1F4D721F31D4197F3D070C8388765F269312` |
| AJX mine/rail advisor | `65x67` | `E2A8E4D56C9BD23DED9D07EC48FD3943E9DA2A6A88CC0A6A7D8EA3A27D48BD5A` |
| AJX accounts advisor | `65x67` | `A58836EBCB8C4B2AF6DD82B2DDA060B1CDF2C40CD18233BF98BDC271C189E22E` |
| AJX security advisor | `65x67` | `4C7A956A9F45005AC130BB1D6F3E965B3F32BA92237EC238775B445D745B3F80` |
| AJX neutral-commission focus | `94x86` | `06063478A0D1A4E0CD562E1230F31CFA46EEB718814F11BCB83E86B6C059B613` |

The AJX asset-completion ledger contains 43 inventoried artifacts; a fresh ledger-to-file check found no missing or mismatched entry. AJX flag hashes also match their current normal/medium/small files. The asset ledger remains the complete source-of-truth inventory beyond the runtime hashes reproduced here.

## Exact tracked staging boundary

Do not stage either package with `git add -A` or whole-file adds across the dirty shared files. Several Event 006 files combine BRI/AJX package work with unrelated round-number tuning and unrelated IW-006/IW-007 promotion changes.

### Tracked BRI slices

| File | Stage | Exclude / note |
| --- | --- | --- |
| `common/national_focus/006_independence_wave_focus.txt` | Only the BRI block currently at `2178-2249` (five focuses, beginning with the IW-004 comment). | It shares the `@@ -2032,0 +2091,158` diff hunk with AJX; a BRI-only commit requires a manually split patch. |
| `common/scripted_effects/006_independence_wave_package_dispatch_effects.txt` | Current added BRI calls at lines `17`, `28`, `37`. | Exclude AJX lines `19`, `30`, `39` from a BRI-only commit. |
| `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt` | IW-004 runtime-adapter entry and exact BRI runtime-preflight identity branch. | Both are non-authorizing adapter prerequisites. Automatic/SCN attestation remains deliberately closed. |
| `common/scripted_triggers/006_independence_wave_package_triggers.txt` | Exact `IW-004`/`BRI` tag-availability helper only. | This proves immutable identity without adding a readiness wrapper. |
| `common/scripted_triggers/006_independence_wave_decision_triggers.txt` | New repair line for `independence_wave_bri_convene_celtic_delegation` inside `has_independence_wave_active_formable_operation`. | This hunk does not exist yet and is required before staging. |

All other existing tracked dirty hunks are outside a BRI-only package commit. BRI runtime portraits, their sprite bindings, and their asset evidence were already committed by `d0044b22e`; do not restage BAY/RHI or unrelated portrait files.

### Tracked AJX slices

| File | Exact current hunk or content to stage | Exclude / note |
| --- | --- | --- |
| `common/national_focus/006_independence_wave_focus.txt` | `@@ -14 +14,2`; `@@ -1191,0 +1193,57`; AJX portion `2092-2176` of `@@ -2032,0 +2091,158`. | Exclude BRI `2178-2249` in an AJX-only commit. |
| `common/script_constants/006_independence_wave_focus_constants.txt` | `@@ -45,0 +46` only (`municipal_commission_vs_industrial_security = 8`). | Exclude all round-number AI/reward tuning from line 69 onward. |
| `common/script_constants/006_independence_wave_mechanics_constants.txt` | `@@ -216,0 +217` only (`neutral_commission = 7`). | Exclude all other global value/band/territory/network tuning hunks. |
| `common/script_constants/006_independence_wave_nwe_advisor_constants.txt` | `@@ -5 +5` comment only. | Exclude all advisor modifier retuning from line 36 onward. |
| `common/scripted_effects/006_independence_wave_effects.txt` | All three current AJX route hunks: `@@ -148,0 +149`, `@@ -184,0 +186`, `@@ -2463,0 +2466`. | Package-required. |
| `common/scripted_effects/006_independence_wave_focus_effects.txt` | `@@ -250 +250`. | Package-required enum maximum. |
| `common/scripted_effects/006_independence_wave_package_dispatch_effects.txt` | AJX calls currently at lines `19`, `30`, `39`. | Exclude BRI calls in an AJX-only commit. |
| `common/scripted_localisation/006_independence_wave_focus_scripted_localisation.txt` | `@@ -77,0 +78` and `@@ -88,0 +90`. | Package-required. |
| `common/scripted_triggers/006_independence_wave_focus_triggers.txt` | `@@ -54 +54` and `@@ -186,0 +187`. | Package-required. |
| `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt` | IW-010 adapter line `19` and exact AJX runtime identity branch currently `71-74`. | Exclude BRI line `14`, unrelated IW-006/IW-007 content-attestation lines `30-31`, and unrelated scenario hunks at `84-91`. |
| `common/scripted_triggers/006_independence_wave_package_triggers.txt` | `@@ -79,0 +80,5` only (exact IW-010/AJX tag trigger). | Exclude the IW-006/IW-007 comment/readiness promotion hunks at current lines `87-95`. |
| `common/scripted_triggers/006_independence_wave_rhineland_bavaria_package_triggers.txt` | Both complete deletions: old `@@ -31,6 +30,0` and `@@ -232,6 +225,0`. | Required for approved later-wave AJX/RHI coexistence. |
| `common/scripted_triggers/006_independence_wave_triggers.txt` | `@@ -202 +202`. | Package-required government-route maximum. |
| `common/scripted_triggers/006_independence_wave_decision_triggers.txt` | Repair line for `independence_wave_ajx_convene_rhenish_league_congress` inside the active-operation trigger. | Present in the parent repair. |
| `docs/events/006_independence_wave/overview.md` | AJX package section `@@ -87,0 +88,20` and regional portrait registration wording `@@ -90 +110,4`. | Both describe the AJX tranche. |
| `events/006_independence_wave.txt` | Generic roster-comment hunk `@@ -51,2 +51,2` and AJX recruitment branch `@@ -84,0 +85,6`. | Stage together with AJX character definitions. |
| `history/countries/AJX - Event 006 Country Shell.txt` | Both current hunks (`@@ -6 +6,2`, `@@ -7,0 +9,9`). | Package shell only; it remains dormant. |
| `interface/006_independence_wave.gfx` | `@@ -28,0 +29,2`. | AJX focus sprite pair. |
| `interface/006_independence_wave_region_01_portraits.gfx` | `@@ -60,0 +61,25`. | AJX leaders and advisors only; no BAY/RHI binding changes. |

### Shared checksum alignment

Commit `45bee09d2` completed the single five-line checksum-ledger transaction for ACX, AEX, AFX, AGX, and AJX. The AJX army-small entry is `470C29FD6CC73F5B6A269969160F1F4D721F31D4197F3D070C8388765F269312`. No shared army-small checksum hunk belongs in the BRI/AJX package commit.

### Explicit tracked exclusions

All other dirty tracked Event 006 hunks are outside these bounded package transactions, including Scotland/Wales decisions, general and Wallonia ideas, main/evolution/global/force/force-package/scenario/Wallonia constants, unrelated IW-006/IW-007 readiness promotion, and the Wallonia handoff. If the broad round-number retuning is intentional, it needs its own reviewed balance commit.

## Exact untracked package ledger

The counts below are the pre-handoff working-tree package paths. This re-audit file is an additional shared audit artifact and is not included in either pre-existing count.

### BRI — 11 paths

```text
common/ai_strategy/006_independence_wave_brittany.txt
common/decisions/006_independence_wave_brittany_decisions.txt
common/decisions/categories/006_independence_wave_brittany_categories.txt
common/ideas/006_independence_wave_brittany_ideas.txt
common/script_constants/006_independence_wave_brittany_constants.txt
common/scripted_effects/006_independence_wave_brittany_package_effects.txt
common/scripted_triggers/006_independence_wave_brittany_package_triggers.txt
docs/events/006_independence_wave/northern_western_europe_packages.md
docs/plans/006_independence_wave_plans/subagent_handoffs/006_bri_country_package_audit_2026_07_15.md
docs/plans/006_independence_wave_plans/subagent_handoffs/006_bri_country_package_implementation_2026_07_15.md
localisation/english/006_independence_wave_brittany_l_english.yml
```

Stage all 11 only after the BRI congress and stale-document corrections are made. They are package-owned whole files.

### AJX — 57 paths

```text
common/ai_strategy/006_independence_wave_saar.txt
common/characters/006_independence_wave_saar_characters.txt
common/country_leader/006_independence_wave_saar_advisor_traits.txt
common/decisions/006_independence_wave_saar_decisions.txt
common/decisions/categories/006_independence_wave_saar_categories.txt
common/ideas/006_independence_wave_saar_ideas.txt
common/script_constants/006_independence_wave_saar_constants.txt
common/scripted_effects/006_independence_wave_saar_package_effects.txt
common/scripted_triggers/006_independence_wave_saar_package_triggers.txt
docs/events/006_independence_wave/northern_western_europe_packages.md
docs/assets/006_independence_wave/ajx_asset_completion_2026_07_15/ajx_asset_validation_2026_07_15.json
docs/assets/006_independence_wave/ajx_asset_completion_2026_07_15/checksums.sha256
docs/assets/006_independence_wave/ajx_asset_completion_2026_07_15/contact_sheets/advisor_portraits_decoded_contact_sheet.png
docs/assets/006_independence_wave/ajx_asset_completion_2026_07_15/contact_sheets/advisor_portraits_enlarged_nearest_contact_sheet.png
docs/assets/006_independence_wave/ajx_asset_completion_2026_07_15/contact_sheets/advisor_portraits_native_contact_sheet.png
docs/assets/006_independence_wave/ajx_asset_completion_2026_07_15/contact_sheets/advisor_reviews/advisor_AJX_independence_wave_cross_border_accounts_comptroller_processor_comparison.png
docs/assets/006_independence_wave/ajx_asset_completion_2026_07_15/contact_sheets/advisor_reviews/advisor_AJX_independence_wave_factory_security_inspector_processor_comparison.png
docs/assets/006_independence_wave/ajx_asset_completion_2026_07_15/contact_sheets/advisor_reviews/advisor_AJX_independence_wave_mine_rail_dispatch_superintendent_processor_comparison.png
docs/assets/006_independence_wave/ajx_asset_completion_2026_07_15/contact_sheets/advisor_sources_contact_sheet.png
docs/assets/006_independence_wave/ajx_asset_completion_2026_07_15/contact_sheets/ajx_asset_completion_contact_sheet.png
docs/assets/006_independence_wave/ajx_asset_completion_2026_07_15/contact_sheets/canonical_all_three/advisor_AJX_independence_wave_cross_border_accounts_comptroller_canonical_all_three.png
docs/assets/006_independence_wave/ajx_asset_completion_2026_07_15/contact_sheets/canonical_all_three/advisor_AJX_independence_wave_factory_security_inspector_canonical_all_three.png
docs/assets/006_independence_wave/ajx_asset_completion_2026_07_15/contact_sheets/canonical_all_three/advisor_AJX_independence_wave_mine_rail_dispatch_superintendent_canonical_all_three.png
docs/assets/006_independence_wave/ajx_asset_completion_2026_07_15/contact_sheets/focus/goal_independence_wave_ajx_neutral_commission_comparison.png
docs/assets/006_independence_wave/ajx_asset_completion_2026_07_15/decoded_png/advisors/advisor_AJX_independence_wave_cross_border_accounts_comptroller.png
docs/assets/006_independence_wave/ajx_asset_completion_2026_07_15/decoded_png/advisors/advisor_AJX_independence_wave_factory_security_inspector.png
docs/assets/006_independence_wave/ajx_asset_completion_2026_07_15/decoded_png/advisors/advisor_AJX_independence_wave_mine_rail_dispatch_superintendent.png
docs/assets/006_independence_wave/ajx_asset_completion_2026_07_15/decoded_png/focus/goal_independence_wave_ajx_neutral_commission.png
docs/assets/006_independence_wave/ajx_asset_completion_2026_07_15/final_dds/advisors/advisor_AJX_independence_wave_cross_border_accounts_comptroller.dds
docs/assets/006_independence_wave/ajx_asset_completion_2026_07_15/final_dds/advisors/advisor_AJX_independence_wave_factory_security_inspector.dds
docs/assets/006_independence_wave/ajx_asset_completion_2026_07_15/final_dds/advisors/advisor_AJX_independence_wave_mine_rail_dispatch_superintendent.dds
docs/assets/006_independence_wave/ajx_asset_completion_2026_07_15/final_dds/focus/goal_independence_wave_ajx_neutral_commission.dds
docs/assets/006_independence_wave/ajx_asset_completion_2026_07_15/gfx_handoff.md
docs/assets/006_independence_wave/ajx_asset_completion_2026_07_15/handoff.md
docs/assets/006_independence_wave/ajx_asset_completion_2026_07_15/manifest.md
docs/assets/006_independence_wave/ajx_asset_completion_2026_07_15/metadata/crops/advisor_AJX_independence_wave_cross_border_accounts_comptroller.json
docs/assets/006_independence_wave/ajx_asset_completion_2026_07_15/metadata/crops/advisor_AJX_independence_wave_factory_security_inspector.json
docs/assets/006_independence_wave/ajx_asset_completion_2026_07_15/metadata/crops/advisor_AJX_independence_wave_mine_rail_dispatch_superintendent.json
docs/assets/006_independence_wave/ajx_asset_completion_2026_07_15/metadata/focus/goal_independence_wave_ajx_neutral_commission.json
docs/assets/006_independence_wave/ajx_asset_completion_2026_07_15/processed_png/advisors/advisor_AJX_independence_wave_cross_border_accounts_comptroller.png
docs/assets/006_independence_wave/ajx_asset_completion_2026_07_15/processed_png/advisors/advisor_AJX_independence_wave_factory_security_inspector.png
docs/assets/006_independence_wave/ajx_asset_completion_2026_07_15/processed_png/advisors/advisor_AJX_independence_wave_mine_rail_dispatch_superintendent.png
docs/assets/006_independence_wave/ajx_asset_completion_2026_07_15/processed_png/focus/goal_independence_wave_ajx_neutral_commission.png
docs/assets/006_independence_wave/ajx_asset_completion_2026_07_15/prompts/ajx_asset_prompts.md
docs/assets/006_independence_wave/ajx_asset_completion_2026_07_15/source_png/alpha_processed/goal_independence_wave_ajx_neutral_commission_alpha_master.png
docs/assets/006_independence_wave/ajx_asset_completion_2026_07_15/source_png/imagegen_raw/advisor_AJX_independence_wave_cross_border_accounts_comptroller_imagegen_raw.png
docs/assets/006_independence_wave/ajx_asset_completion_2026_07_15/source_png/imagegen_raw/advisor_AJX_independence_wave_factory_security_inspector_imagegen_raw.png
docs/assets/006_independence_wave/ajx_asset_completion_2026_07_15/source_png/imagegen_raw/advisor_AJX_independence_wave_mine_rail_dispatch_superintendent_imagegen_raw.png
docs/assets/006_independence_wave/ajx_asset_completion_2026_07_15/source_png/imagegen_raw/goal_independence_wave_ajx_neutral_commission_imagegen_raw.png
docs/assets/006_independence_wave/ajx_asset_completion_2026_07_15/visual_review_notes.md
docs/plans/006_independence_wave_plans/subagent_handoffs/006_ajx_country_package_audit_2026_07_15.md
docs/plans/006_independence_wave_plans/subagent_handoffs/006_ajx_country_package_implementation_2026_07_15.md
gfx/interface/goals/006_independence_wave/goal_independence_wave_ajx_neutral_commission.dds
gfx/interface/ideas/006_independence_wave/advisors/advisor_AJX_independence_wave_cross_border_accounts_comptroller.dds
gfx/interface/ideas/006_independence_wave/advisors/advisor_AJX_independence_wave_factory_security_inspector.dds
gfx/interface/ideas/006_independence_wave/advisors/advisor_AJX_independence_wave_mine_rail_dispatch_superintendent.dds
localisation/english/006_independence_wave_saar_l_english.yml
```

The tracked-modified AJX country shell is intentionally absent from this untracked list and appears in the tracked staging table above. Creating this re-audit adds one further untracked shared audit artifact whose filename contains both `bri` and `ajx`; it is not counted as a pre-existing package path. Stage the whole AJX asset-completion subtree and the four final runtime assets only after the gameplay/AI/documentation blockers close.

## Recommended commit partition after repair

1. **Shared army-small checksum alignment — complete:** commit `45bee09d2` contains the entire five-line `generated_nwe_hashes.sha256` transaction.
2. **IW-004 BRI package:** stage the 11 package-owned untracked files, the four BRI tracked slices listed above, and this re-audit or a short superseding closeout that records the repaired result. Do not include AJX or broad Event 006 tuning.
3. **IW-010 AJX package:** stage the AJX package-owned paths, the exact AJX tracked slices, the negative restraint fix, the congress fix, and updated documentation. Do not include BRI or broad Event 006 tuning.
4. If BRI and AJX are intentionally committed together, the combined package transaction may stage both sides of the shared focus/dispatch hunks and both new active-operation lines, but it must still exclude the unrelated global tuning and IW-006/IW-007 hunks identified above.

Before either package commit, review the staged diff rather than the aggregate working-tree diff. A package is ready only when the staged view contains its exact package surface, the repaired transaction, synced localisation/docs, and no unrelated tuning.

## Re-audit close criteria

BRI can be promoted to commit-safe when:

- its custom congress calls shared preparation, rewards only `transaction_ready`, and leaves final commitment to DM-55;
- its custom decision and the shared active-operation trigger mutually exclude concurrent formable actions;
- congress localisation and package/handoff evidence describe the same transaction;
- the BRI evidence records the `65x67` army-small and post-98ec FORM-01 result;
- a staged-scope review contains only the BRI boundary above.

AJX can be promoted to commit-safe when:

- the equivalent custom congress and concurrency repairs are present;
- `founding_restraint` and `settled_restraint` are negative and the audit text no longer asserts the positive values are restraint;
- congress localisation, FORM-04 documentation, and small-portrait evidence are current;
- the shared five-line army-small ledger correction is committed separately or otherwise present as a complete shared transaction;
- a staged-scope review contains only the AJX boundary above.

Automatic-pool and SCN-008 admission may remain closed after these bounded package commits. Opening them is a later readiness transaction requiring its own exact tag/content attestation and scenario review.

## Parent repair closeout

The parent applied the exact repair sequence prescribed above and then repeated the bounded static checks locally because the follow-up subagent reached its usage limit before patching:

- both custom congresses require stable package compacts, shared preparation readiness, strategic affordability, capital control, no package project, and no shared formable operation;
- each decision calls `independence_wave_formable_begin_preparation` exactly once and contains no direct shared-congress proof or direct commit request;
- package completion flags and network rewards occur only inside a post-resolution `independence_wave_formable_transaction_ready` branch;
- shared transaction failure does not stack a package project-failure penalty, while invalid removal or cancellation in the still-exact package applies the package failure without a refund;
- `has_independence_wave_active_formable_operation` names both exact decision IDs once;
- AJX targetless restraint values are `-200` and `-400`;
- both localisation files remain UTF-8 BOM and describe preparation followed by a separate proclamation; and
- the package references and earlier handoffs now record promoted FORM-01/04 and the corrected `65x67` BRI/AJX army dossiers.

This closes findings B1-B4 for bounded package commit safety. Both packages have their immutable runtime identity branches, but neither identity proof grants readiness: IW-004 and IW-010 automatic/content-attestation and SCN-008 admission remain closed. This is static source evidence rather than a live-engine execution claim.

## Sources and skill record

This re-audit used the repository's `chaos-redux-events`, `chaos-redux-subagents`, `hoi4-focus-trees`, `hoi4-decisions-missions`, and `chaos-redux-event-assets` guidance. It consulted the required offline Paradox wiki core pages plus focus, country, character, and AI references; the corresponding official vanilla documentation; vanilla files; the post-98ec formable audits; and the package/asset evidence listed above. No fallback, gameplay simplification, asset substitution, staging action, or commit was performed.
