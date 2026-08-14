# IW-050 Komi decisions handoff

## Source delivered

`common/decisions/006_independence_wave_komi_decisions.txt` defines the package-local `independence_wave_komi_northern_compact_category`, the automatic `independence_wave_komi_hold_northern_council` founding mission, and ten serialized projects:

`secure_taiga_depots`, `integrate_rail_guards`, `register_komi_communities`, `settle_former_host_ledgers`, `ratify_constitutional_autonomy`, `adopt_taiga_land_compact`, `convene_rail_councils`, `establish_taiga_emergency_command`, `codify_durable_sovereignty`, and `open_northern_ural_corridor`.

Each timed project uses the Komi package cost trigger, package-local 45/75/105-day duration constants, capital control, active-project serialization, generation-safe cancellation, bounded failure cleanup, and an explicit AI score. Completion resolves through the corresponding package-local effect alias. The founding mission succeeds only when both ledgers are stable, a route government exists, and state 397 remains secure.

## Superseding codify/corridor repair note (2026-08-14)

The package-local codify/corridor repair handoff `006_iw050_komi_codify_corridor_repair_2026_08_14.md` supersedes the earlier alias behavior.

The codify project now sets durable sovereignty and applies the major-settlement effect under an idempotent Komi package guard, while `open_northern_ural_corridor` remains a separate lifecycle-gated project with its resolved/stable compact, network, League-route, capital-control, strategic-cost, and generation-safe readiness prerequisites.

This decision-surface repair is package-local only and leaves IW-050 outside central admission and deterministic Join at the current 40/32/29/161 boundary.

## Superseding lifecycle, cost, and tooltip repair note (2026-08-14)

The follow-up handoff `006_iw050_komi_lifecycle_cost_tooltip_repair_2026_08_14.md` records the owner-applied repair committed as `b8aa313a8`. It clears durable sovereignty in package setup and cleanup, aligns the emergency decision's affordability trigger with its security payment, and reconciles the codify description and effect tooltip with the separate corridor project. The re-audit findings below are retained as historical evidence; they no longer describe the current source for those three defects.

The repair receipt supersedes the earlier 119-unresolved-input empty-state summary below: the current six-scenario mission analysis has 66 rows, 131 unresolved inputs, and 11 never-eligible diagnostics, and remains adapter-capability evidence only.

## Validation and limits

The decision file has balanced blocks, no unsupported comparison operators, and exact parity with the ten active project IDs in `common/scripted_triggers/006_independence_wave_komi_package_triggers.txt`. All owned name, description, and effect-tooltip keys resolve in `localisation/english/006_independence_wave_komi_l_english.yml`.

`hoi4.probability_inspect` on the mission surface returned `PROBABILITY_SOURCE_INSPECTED` with 11 candidates, 14 required inputs, zero available candidates, and an incomplete pool. The current six named empty-state scenarios returned `PROBABILITY_ANALYZED_PARTIAL` with 66 rows, 131 unresolved inputs, and 11 never-eligible diagnostics. This is adapter capability evidence only; no normalized mission probability, timing, rank, dominance, or balance claim is made.

The decision-category renderer is not available in the installed MCP, so UI overflow remains a source-only limitation. The package remains outside central dispatcher, attestation, scenario preflight, and Join until the portrait, flag, and runtime admission gates are separately accepted.

## Historical read-only re-audit after codify/corridor repair (2026-08-14)

### Disposition

This dated pre-`b8aa313a8` re-audit recorded the structurally correct codify/corridor split, two concrete cost/lifecycle defects, and several requirement or tooltip mismatches. The lifecycle, cost, and tooltip handoff supersedes its durable-flag, emergency-cost, and codify-wording findings, while the remaining design questions stay deferred as documented above. This re-audit was read-only and changed no gameplay source.

The package-local fail-closed boundary is preserved. No central dispatcher, content attestation, scenario preflight, deterministic Join, portrait, flag, or unrelated file was edited.

### Historical severity-ordered findings (pre-b8aa313a8)

The findings below are retained as dated evidence and are not current source authority; the superseding lifecycle, cost, and tooltip handoff above governs repaired behavior.

1. **High — durable sovereignty is not cleared by package setup or cleanup.** `common/scripted_effects/006_independence_wave_komi_package_effects.txt:306-314` sets `independence_wave_komi_durable_sovereignty`, while setup at `:329-348` and cleanup at `:411-453` clear the other Komi lifecycle flags but never clear this one. A reused or reinitialized IW-050 generation can therefore inherit the flag and permanently suppress codify visibility at `common/decisions/006_independence_wave_komi_decisions.txt:205-210`. Narrow correction: add `clr_country_flag = independence_wave_komi_durable_sovereignty` to both package-local setup and cleanup.

2. **High — emergency command gates on strategic resources but spends security resources.** `common/decisions/006_independence_wave_komi_decisions.txt:185-198` uses `can_pay_independence_wave_komi_strategic_cost` for `available` and `custom_cost_trigger`, displays `independence_wave_cost_security_standard`, and then calls `independence_wave_decision_pay_security_standard`. The strategic trigger at `common/scripted_triggers/006_independence_wave_komi_package_triggers.txt:50-55` checks spare civilian capacity, Stability, War Support, and diplomatic CP/convoy-or-train resources, whereas the security trigger at `common/scripted_triggers/006_independence_wave_decision_triggers.txt:263-268` and effect at `common/scripted_effects/006_independence_wave_decision_effects.txt:209-220` require and spend manpower, Army Experience, infantry equipment, and support equipment. Narrow correction: gate this decision with `can_pay_independence_wave_security_standard_cost`, or add a package-local composite trigger whose tooltip and effect enumerate every intended resource.

3. **Medium — codify tooltip still claims effects supplied only by the corridor alias.** `localisation/english/006_independence_wave_komi_l_english.yml:63` says sovereignty raises both compact ledgers and strengthens network and League ties, but the current codify alias only sets the durable flag and calls `independence_wave_komi_apply_major_settlement` (`common/scripted_effects/006_independence_wave_komi_package_effects.txt:306-314`), which applies country deltas at `:90-97` and no ledger, network, or League delta. The network and League rewards are supplied by `independence_wave_komi_reward_network_project` at `:134-148`, reached by the separate corridor effect at `:286-296`. Narrow correction: either add the intended Komi/network/League deltas to codify and retain the tooltip, or revise `independence_wave_komi_sovereignty_effect_tt` to describe only the country settlement actually applied.

4. **Medium — administrative standard cost text does not match the Komi reservation.** Codify and the other administrative-standard projects use `@CR_SC_INDEPENDENCE_WAVE_KOM_CIVILIAN_FACTORY_USE = 1` at `common/decisions/006_independence_wave_komi_decisions.txt:1-3`, while the Komi trigger at `common/scripted_triggers/006_independence_wave_komi_package_triggers.txt:44-48` requires more than the package floor of zero and the shared localisation at `localisation/english/006_independence_wave_decisions_l_english.yml:26,45-46` displays the shared two-factory standard. The Komi constant `independence_wave_komi_cost.civilian_factory_use = 1` at `common/script_constants/006_independence_wave_komi_constants.txt:31-34` is not used by the decision text. Narrow correction: add a Komi-local standard cost localisation using the one-factory burden, or align the modifier, trigger, and shared text to the intended two-factory standard.

5. **Medium — strategic projects require an undisplayed spare civilian factory and do not reserve it.** `can_pay_independence_wave_komi_strategic_cost` at `common/scripted_triggers/006_independence_wave_komi_package_triggers.txt:50-55` requires spare civilian capacity, Stability, War Support, and diplomatic resources, but former-host ledgers and the corridor show only `independence_wave_cost_diplomatic_standard` at `common/decisions/006_independence_wave_komi_decisions.txt:118-132` and `:262-265`, and neither decision has a civilian-factory modifier. Narrow correction: use a package-specific strategic tooltip and reservation, or remove the extra strategic gates if only diplomatic resources are intended.

6. **Medium — project readiness and cancellation do not independently reject an ended origin.** `is_independence_wave_komi_project_ready` at `common/scripted_triggers/006_independence_wave_komi_package_triggers.txt:21-26` and the ordinary project cancellation triggers rely on package/setup/current-generation and crisis flags but omit `independence_wave_origin_ended`; the exact runtime-ready trigger at `:57-71` does reject that flag. Because central Komi dispatch remains intentionally absent, a stale package-local surface could survive if cleanup is not invoked before origin termination. Narrow correction: add `NOT = { has_country_flag = independence_wave_origin_ended }` to the package-local ready and project-cancel gates, or prove that the package-local cleanup wrapper always runs before origin end.

7. **Medium — codify description implies corridor-first ordering that the source does not require.** `localisation/english/006_independence_wave_komi_l_english.yml:49-50` describes a “secured northern corridor,” but codify availability at `common/decisions/006_independence_wave_komi_decisions.txt:211-224` does not require `independence_wave_komi_pechora_corridor_open`, and the repaired design permits the corridor to complete afterward. Narrow correction: remove the corridor claim from the description, or add the corridor prerequisite only if corridor-first ordering is intended.

8. **Medium — former-host settlement has an undocumented partial-success path.** The decision checks a living, non-belligerent former host only when selected at `common/decisions/006_independence_wave_komi_decisions.txt:118-132`; its active cancellation at `:129-130` does not recheck that target. Completion at `common/scripted_effects/006_independence_wave_komi_package_effects.txt:271-283` always raises Komi ledgers and sets `independence_wave_komi_host_ledgers_settled`, but applies bilateral host deltas only if the host remains valid. This is a defensible partial outcome but the current tooltip says negotiations settle outstanding claims without naming the partial case. Narrow correction: cancel when the host becomes invalid, or add explicit partial-success localisation and a separate outcome flag.

### Category and lifecycle notes

`common/decisions/categories/006_independence_wave_komi_categories.txt:9-15` is an ordinary package-local category gated by Komi identity and `independence_wave_iw_050_setup_complete`; it has no decision-owned scripted GUI and no `visible_when_empty` override. The category contains one automatic founding mission and ten serialized timed projects, and the active-project trigger at `common/scripted_triggers/006_independence_wave_komi_package_triggers.txt:122-134` enumerates all ten project IDs.

The founding mission `independence_wave_komi_hold_northern_council` is owned by IW-050 Komi in the Northern Komi/Syktyvkar state-397 region, activates for the current setup and force generation, and runs for `constant:independence_wave_komi_duration.founding_crisis` (420 days). Its success path is the mission `cancel_effect` when both ledgers are stable, a route government exists, state 397 remains owned and controlled, and the capital remains controlled; timeout or invalidation sets `independence_wave_komi_compact_crisis_failed` and applies the one-shot project-failure effect. `available = { always = no }` is intentional for this cancel/timeout mission pattern and does not itself create a hidden player action.

The ten project lifecycle surfaces are as follows.

| Surface | Requirement, duration, and success | Failure and duplicate risk |
| --- | --- | --- |
| `secure_taiga_depots` | Ready package, administration-light resources, capital control, no active project; 45 days; calls the depot/congress alias. | Generic cancel failure; `independence_wave_komi_congress_convened` prevents repeat reward. |
| `integrate_rail_guards`, `register_komi_communities` | Ready package, administration-standard resources, capital control, no active project; 75 days; calls the respective guarded aliases. | Generic cancel failure; guard flags prevent repeat reward. |
| `settle_former_host_ledgers` | Ready package, living non-belligerent former host, strategic gate, capital control, no active project; 75 days; raises both ledgers and attempts bilateral settlement. | Host can become invalid during the timer, producing the partial-success gap above; `independence_wave_komi_host_ledgers_settled` prevents repeat. |
| `ratify_constitutional_autonomy`, `adopt_taiga_land_compact`, `convene_rail_councils` | Ready package, route-specific government choice, administration-standard resources, capital control, no active project; 105 days; install the selected route government through guarded aliases. | Generic cancel failure; route-government flags and route selection prevent duplicate installation. |
| `establish_taiga_emergency_command` | Ready package, emergency route, capital control, no active project; 105 days; intended to pay security-standard resources and install the emergency government. | Current strategic/security gate mismatch is a high-severity defect; route-government guard prevents repeat after a successful install. |
| `codify_durable_sovereignty` | Ready package, route government, resolved and stable compact, capital control, no active project; 105 days; sets durable sovereignty and applies major settlement. | Generic cancel failure; durable flag is idempotent but not reset by setup/cleanup. Corridor remains independently available. |
| `open_northern_ural_corridor` | Ready package, resolved and stable compact, network member, League route, strategic gate, capital control, no active project; 105 days; opens the Pechora flag through the separate corridor alias. | Generic cancel failure; Pechora flag prevents repeat, while strategic tooltip and undisplayed factory gate remain mismatched. |

All timed projects commit their payment in `complete_effect`, run a package-local alias from `remove_effect`, and apply the one-shot generic failure effect from `cancel_effect`. The no-active-project gate prevents concurrent projects, and alias flags make the named rewards idempotent. No free project loop, repeated ledger award, repeated network reward, or equipment-farming path was found in the current source, but the stale durable flag can suppress a later codify project after reuse.

### Costs, requirements, AI, and route locks

The light and standard administrative aliases spend command power and manpower, and the civilian-factory modifier reserves one factory for Komi projects, but standard administrative UI still reports the shared two-factory value. Diplomatic aliases spend command power plus convoys or trains, while the strategic trigger adds Stability, War Support, and an undisplayed spare-factory requirement. The emergency alias is the only confirmed trigger/effect resource mismatch.

All projects use explicit high AI scores, with rail-guard integration and emergency command doubled during war; the founding mission uses the urgent score. The codify/corridor repair did not change AI weights, so no new normalized AI-balance claim is supported. Route locks are source-valid: codify requires a selected route government, and corridor requires network membership plus League-route availability and a stable resolved compact.

### Localisation and GUI limits

All eleven decision/mission names, descriptions, and owned effect-tooltip keys resolve in `localisation/english/006_independence_wave_komi_l_english.yml`, but the codify tooltip and codify description have the semantic mismatches listed above. Shared cost strings resolve but the administrative-standard and strategic strings do not describe the Komi-specific gate/reservation exactly.

No decision-owned scripted GUI is linked to this ordinary category, so `hoi4.gui_inspect` and `hoi4.gui_render` evidence is not applicable and no `hoi4.gui_rewrite` was performed. The prior handoff's source-only renderer limitation remains for this non-GUI decision surface.

### Probability receipts and validation

The mandatory `hoi4.probability_inspect` was rerun first on `common/decisions/006_independence_wave_komi_decisions.txt` with adapter `mission_ai_will_do`; it returned `PROBABILITY_SOURCE_INSPECTED`, source revision `d863b818b3caabad74526c14c0f85ca622c5d690024e3c266d505fd4e1f5a9b2`, source hash `9583721e8b4a125ac3a6ffb64f30c549d26c8a85e89953b2d4794df3b5860765`, eleven candidates, zero available candidates, fourteen required inputs, and zero inspect-unresolved items. The current inspect artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/cf99e95cea0461f83eb41ab84345ffcab4195b57da30e08c9d2b48fbcbbfe701/73f74b3281eb786868376248f01530f7b128af04bf5a187e194152a62ed11540/probability-inspect-9583721e8b4a.json`.

The explicit empty-fixture evaluation used six named `{state:{}}` scenarios in `IW050_KOM_MISSION_SCENARIOS_POST_CODIFY_REPAIR_EMPTY_2026_08_14` and the complete eleven-ID pool; it returned `PROBABILITY_ANALYZED_PARTIAL` with analysis ID `probability-d7bcf97687f581e83b92d6f7`, six scenarios, 66 rows, 131 unresolved/bounded inputs, and eleven `PROBABILITY_OUTCOME_NEVER_ELIGIBLE` diagnostics. Those never-eligible outcomes are expected adapter limitations because the fixture cannot materialize package identity, setup, ledgers, capital, host, network, or cost state, and they are not evidence of route starvation. Evaluation artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5ce6e26836d0ecf548a8371f5e02d7b88f3f90c4a9ac65e3efe99ac33933efd6/2724c5466868eca573043b420b26a776cda37e7abd36b3c6224daf407f4773a6/probability-d7bcf97687f581e83b92d6f7.json`.

The associated ranking artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/592cf00f26e7b06fd584dc244cbc44e05cc408d037874ef1d4e3fdd1b28a7a46/aabc3a70fac96940cef1ed179aea8c7be5ed42449d35373d0b7b64d7473b0e8c/probability-probability-d7bcf97687f581e83b92d6f7-ranking.svg` and the unresolved-input artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/538682f2f1fb538191256fd2092a7cbd283d72e51dc542b268da0a9a419e0e5d/58cd7be742261e39850e7ccf96e81b45b4fbe840e9c6359b3fb677c1ad00e323/probability-probability-d7bcf97687f581e83b92d6f7-unresolved.svg`.

The existing same-source current/current compare remains a capability receipt rather than a balance proof: `comparisonChanges=0`, 66 rows, and 131 unresolved inputs with artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d74bdc011ed32a259c221ee71b50568095a46f14a3349df2a7028eb99a91ca22/1c7098593e4590cd89ea443eff46e7511605637b817e60de075861637452c70c/probability-fccf22c5ca145c9f009d38b6.json`.

The decision/effect/category/triggers/localisation source review found no missing owned localisation key, no duplicate project ID, and no new syntax issue in the repair. Live HOI4 execution, materialized non-empty probability scenarios, and GUI rendering were not claimed because they are unavailable or out of scope for this package-local read-only audit.

### Recommended correction order

1. Clear `independence_wave_komi_durable_sovereignty` in package-local setup and cleanup.

2. Correct emergency `available` and `custom_cost_trigger` to match the security payment, or define a fully documented composite resource contract.

3. Reconcile the codify tooltip and description with the deliberately separate corridor outcome.

4. Reconcile Komi factory reservation and strategic gates with their cost localisations, then decide whether the origin-ended guard and former-host partial outcome require narrow lifecycle/tooltip updates.

## Current narrow patch-pass re-audit (2026-08-14; HEAD 3ad93a39d)

### Disposition

The current HEAD already contains the three bounded source repairs requested for this pass, so no additional gameplay patch was applied. The owner-applied changes are source-backed and remain limited to the Komi package surface; this pass did not touch the central dispatcher, attestation, Join, portraits, flags, or workbook.

### Current source proof

1. `independence_wave_komi_durable_sovereignty` has exactly one package-local writer in `common/scripted_effects/006_independence_wave_komi_package_effects.txt:306-314` and symmetric clears in setup at `:329-349` and cleanup at `:412-455`. The setup/cleanup pattern now prevents a reused generation from inheriting or retaining the terminal sovereignty flag.

2. Codify and corridor wording now matches their separate effects. `independence_wave_komi_sovereignty_effect_tt` at `localisation/english/006_independence_wave_komi_l_english.yml:69` describes the legitimacy, recognition, capacity, and durable-settlement result supplied by `independence_wave_komi_apply_major_settlement` at `common/scripted_effects/006_independence_wave_komi_package_effects.txt:90-97,306-314`, while `independence_wave_komi_corridor_effect_tt` at `:70` retains the ledger, network, and League gains supplied by the corridor alias at `:286-296`. The codify description at `:50` no longer claims to secure the separate corridor.

3. Emergency command now uses `can_pay_independence_wave_security_standard_cost` in both `available` and `custom_cost_trigger` at `common/decisions/006_independence_wave_komi_decisions.txt:187-200`, matching `independence_wave_decision_pay_security_standard`. The shared security trigger at `common/scripted_triggers/006_independence_wave_decision_triggers.txt:263-268` checks the same manpower, Army Experience, infantry-equipment, and support-equipment families that the payment effect spends at `common/scripted_effects/006_independence_wave_decision_effects.txt:209-220`; the current constants preserve the established strict-greater-than gate and matching spend magnitudes.

### Scoped validation

The static current-source check found one durable-sovereignty writer, two symmetric clears, two emergency security-gate references, zero emergency strategic-gate references, no stale corridor/network phrase in the codify tooltip, the origin-ended readiness guard, eleven origin-ended cancellation guards, six Komi administration-standard cost-key references, and two Komi strategic cost-key references.

The current decision probability receipt remains the post-repair `mission_ai_will_do` inspection recorded in `006_iw050_komi_admin_standard_cost_localisation_reaudit_2026_08_14.md`, with eleven candidates, fifteen required inputs, zero inspect-unresolved items, and an incomplete pool. The cost and lifecycle repairs changed no AI score, so no new normalized probability or balance claim is made.

No decision-owned scripted GUI exists for the ordinary Komi category, so GUI inspect/render/rewrite evidence remains not applicable. Live HOI4 execution and materialized non-empty probability scenarios remain outside the available evidence boundary.

### Remaining issues

The former-host partial-success wording and central package admission/Join boundary remain deferred design or authority issues. The current three requested source defects are resolved; no further narrow source correction is justified by this pass.

## Former-host partial-success localisation clarification (2026-08-14)

The package-local former-host project can still complete its Komi ledger advancement when the former host becomes unavailable or returns to war during the timer, while `independence_wave_komi_apply_former_host_settlement` is correctly skipped because the bilateral target is no longer valid. The player-facing text now states this partial outcome explicitly in `localisation/english/006_independence_wave_komi_l_english.yml:40,64`: the bilateral settlement is recorded only when the former host remains available and at peace, otherwise the Komi ledgers advance but the external claims remain unresolved.

This is a localisation-only clarification of existing effect behavior. No decision availability, timer, cost, AI score, central dispatcher, attestation, portrait, flag, or Join surface changed. The file retains its UTF-8 BOM; no new probability or GUI claim is made because the gameplay source and weighted surfaces were unchanged.
