# Chaos Warfare and CBRN supported-core closure audit

Date: 2026-08-21

Status: the supported gameplay core is source-ready for in-game use. Remaining omissions are exact engine-surface blockers, current HOI4 MCP availability, or user-owned live consumer validation. No estimator, proxy receipt, neutral receipt, hidden fallback, or ordinary-air contamination approximation is retained.

## Authority and evidence boundary

This closure reconciles the accepted numbered specifications, matrices, staged plan, implementation surface map, specialist prompts, completion checklist, current source, the fresh localisation and AI handoffs, and the later direct user corrections.

Numbered specification 08 is the controlling later correction for nerve suppression. Gas-Chamber Saturation Drills unlocks a stronger nerve-agent killing method in an already active camp network once Tabun, Sarin, or Soman is researched. The doctrine does not create a free camp-building route; camp infrastructure, activation, target selection, responsibility, discovery, and cleanup remain owned by the repression system.

The general evidence-preservation rule in specification 02 has one explicit later exception from specification 08: the mastered camp method may reduce the amount of new forensic evidence generated, but it cannot erase evidence, attribution, responsibility, discovery, deaths, contamination, trauma, Condemnation, or history.

This is source and asset-pipeline evidence, not a claim that Hearts of Iron IV was launched. Repository policy leaves live game validation to the user.

## Facility rendering repair

Commit `eabebdec5` repairs the stretched chemical and biological facility models without replacing their accepted geometry, textures, scale, transforms, or silhouettes.

The biological facility is partitioned into four engine-safe streams and the chemical facility into eight. Every exported stream has a corresponding `meshsettings` registration in `gfx/entities/chaosx_buildings.gfx`.

The runtime biological mesh matches SHA-256 `6FB1DF91E6148A91709AAAF9F05EA379A7269F77F601ED3E7616D94F0E7FECD0`. The runtime chemical mesh matches SHA-256 `CA775D75AC580704E30445FBD8F201502A2DF01962C581D28E5158FE92D54794`.

Fresh reimports preserve all 30,000 biological triangles and all 58,004 chemical triangles. Detailed stream counts, dimensions, checkpoints, and preview paths are recorded in `docs/plans/chaos_warfare_system_plans/subagent_handoffs/2026-08-21_facility_render_stream_repair.md`.

The reusable 3D pipeline guidance now checks both vertex and triangle-index limits, applies a conservative 24,000-index static-building stream ceiling, and requires one GFX registration for every stream.

## Starting conditions and protection economy

`common/scripted_effects/chaosx_startup_history_effects.txt` still installs seven chemical facilities and eight biological facilities in the accepted historical state set. The startup helpers are idempotent and do not replace an existing facility.

Starting technologies and country program profiles remain present. The rework did not remove the accepted chemical, protection, decontamination, surveillance, handling, or response foundations from their assigned countries.

Gas masks remain producible equipment with model progression, national reserves, military issue, civilian distribution, filter condition, fitting loss, exposure loss, replacement demand, and population-scaled distribution transactions.

Starting mask values remain centralized in `common/script_constants/cbrn_system_constants.txt` and follow `matrices/gas_mask_starting_stockpile_matrix.md`. Britain remains strongest at 26,000 basic and 19,000 improved masks, with the values documented as gameplay tuning and bounded historical confidence rather than precise historical totals.

Routine distribution and filter work use one national program card per task. Exact-state cards require a live alert, contamination, outbreak, or other exact incident.

## Chemical delivery and consequences

Every supported chemical release route reaches `cbrn_dispatch_chemical_action_record`. Current callers cover camp use, battlefield compatibility logic, chemical doomsday, native chemical raids, occupation compatibility logic, and the historical Japan campaign.

The shared action contract validates the target and route, consumes real payload, computes protection and conditions, then records disruption, deaths, contamination, medical saturation, evidence, attribution, Condemnation, responsibility, and history.

Chemical contamination writes are centralized in `common/scripted_effects/cbrn_exposure_effects.txt`. A failed or no-release chemical raid does not contaminate its selected state.

The supported native chemical air raid preserves the selected state and reaches shared dispatch only after reservation and payload proof. Idle chemical-capable aircraft and ordinary continuous air activity never create contamination.

Four exact ground chemical operation families remain fail-closed before payload debit because the installed Army Headquarters and operation surfaces do not expose the required exact selected-state weather, terrain, and release-condition receipt.

## Biological delivery and lifecycle

The active biological delivery set is intentionally mixed rather than raid-only or decision-only: strategic raids, battlefield raids, four native espionage operations, two historically bounded Japan-China decisions, facility recovery raids, and the doomsday decision.

The twelve generic biological supply-chain state-target decision variants are migration-only. `bio_sabotage_actor_can_list_targets` returns false, so no new one-card-per-state surface can appear; existing committed records retain their resolver and cleanup helpers.

Biological raid delivery odds are agent-neutral. Agent potency and lifecycle severity remain ordered Tularemia below Anthrax below Plague below Smallpox.

Only the Smallpox doomsday path assigns `bio_lifecycle_result.severe`. Ordinary Smallpox remains the most dangerous standard agent without turning every use into a special severe result.

Each ordinary episode retains incubation, detection, spread, containment, treatment, stockpile safety, attribution, accident handling, continuing deaths, and bounded cleanup. Weaponized zombies remain a separate system except for explicitly shared infrastructure helpers.

## Doctrine, command, units, designers, and rewards

Chaos Warfare communicates and applies an aggressive CBRN identity: faster preparation, stronger physical effects, easier supported deployment, and lower bounded Condemnation impact while preserving physical and forensic consequences.

Adoption provides 15 percent planning speed and 35 percent mapped chemical-support soft attack, breakthrough, and defense. Contaminant Fire Support reaches 1.65 operational effect and 1.80 contamination output. Integrated CBRN Command reaches 1.70 operational effect, 1.60 chemical-air dose, 1.50 duration, and a 0.35 Condemnation multiplier.

Gas-Chamber Saturation Drills multiplies selected nerve-agent camp killing efficiency to 225 percent, reduces payload use to 45 percent of standard, reduces new evidence generation to 55 percent of standard, and adds agent-scaled resistance suppression. Terminal Hazard can add a further 1.75 death multiplier under Unrestricted Chaos Warfare.

Chemical Operations Commanders reduce paid CBRN Headquarters preparation time to 70 percent. The doctrine-independent academy route gives eligible new and promoted army leaders a 50 percent chance to gain the trait.

Army Headquarters owns theater preparation and abilities. Regimental support owns division-level protection, reconnaissance, decontamination, medical response, payload handling, armored delivery, containment, and the Chaos Assault formation. Powerful abilities require their mapped equipment, scale down or fail when undersupplied, charge meaningful costs, use bounded durations and cooldowns, expose AI gates, and clean up their reservations.

CBRN technologies, units, MIO families, historical scientists, theorists, advisors, officer corps content, templates, achievements, and AI profiles remain wired. Their active bonuses are substantial rather than two- or three-percent filler.

## Visibility and bloat closure

CBRN program, operations, civil-defence, disease-response, diplomacy, occupation, and campaign categories use relevance gates and hide when empty. Starting technology, facilities, and reserves do not by themselves reveal the general CBRN decision surfaces.

The generic biological state-card family and coercive occupation authorization are invisible migration surfaces.

External protective occupation aid now requires an exact chemical alert, chemical contamination, biological outbreak, or recorded nerve-suppression trauma. The category also requires an actual eligible aid target and excludes nonhuman Chaos countries.

The Repression Ledger remains owned by the camp system. Germany receives it only when its repression network becomes operational, Japan retains its accepted game-start priority, and special Chaos countries are excluded by the shared eligibility trigger. Mengele-facing content remains gated until his route is relevant.

Twelve missing Repression Ledger selector labels are restored, allowing all six pool rows and all six active-site rows to resolve to visible text.

No CBRN-specific helper was added to `chaosx_dynamic_effects.txt` or the generic dynamic-trigger registry. Reused CBRN helpers stay in dedicated CBRN, biological, chemical, occupation, camp, or consequence files.

## Localisation and assets

Smallpox text now describes it as the most severe standard agent rather than the only severe agent. Tularemia no longer promises civilian immunity, and Smallpox no longer promises permanent contamination or an automatic nationwide epidemic.

Facility descriptions identify their laboratory, containment, filling, testing, and safety functions without implementation-facing mod-name text.

Grand-doctrine and subdoctrine descriptions state the aggressive preparation, lethality, contamination, outbreak, command, and political-sustainability progression. Generic advisor disclaimers were removed, and the headquarters intelligence cell uses the accepted package name, Chemical Intelligence and Weather Cell.

Achievement and battlefield compatibility keys now follow the repository's no-leading-space localisation format. Achievement text no longer describes an "exact" capture, and the inactive battlefield compatibility strings use player-facing target and condition language instead of pipeline or receipt terminology.

The active dedicated CBRN, chemical, biological, camp, doctrine, advisor, designer, achievement, raid, and unit GFX registries have no missing texture path in the bounded filesystem audit. Existing Chaos Redux raid icons were retained; the separate `gfx/interface/raids` work did not overwrite `gfx/interface/military_raids`.

## Specialist and package validation

The fresh localisation handoff identified twelve missing selector keys, stale generic state-card routes, stale biology wording, authorial text, and a superseded occupation route. The missing keys and wording were repaired, the generic state cards and coercive route were retired, and the camp-specific evidence exception was retained because later numbered specification 08 explicitly authorizes it.

The fresh AI handoff completed a source inventory and static score trace but could not produce engine-backed probabilities. Schema-valid `hoi4.probability_inspect` calls timed out after 180 seconds and subsequent probability, event, technology, doctrine, and GUI routes returned a closed transport. No exact probability is inferred from source scores.

The source-only AI risk list was dispositioned without changing weighted behavior. Livens base, low, and medium production pressure is intentionally cumulative after confirmed enemy chemical use; its research-weight and force-research blocks use different native strategy types. Armored-delivery low pressure targets light chassis while medium pressure targets medium and heavy chassis. Smallpox keeps a lower ordinary project score because it is the uniquely severe route, while desperate posture supplies the stronger override. The retired biological state-card variants cannot enter a score race, and zero-base offensive policies receive positive additions only from their matching aggressive routes.

A fresh decision-mission specialist handoff could not be recovered because the dispatched audit task returned `not_found`. The parent therefore performed the bounded source audit recorded here, while the unavailable specialist result and current MCP transport remain explicit audit-tool blockers rather than being replaced by an invented pass result.

The previous successful technology comparison between revisions `e7171c37` and `d9a6815d` found no technology addition, removal, rename, move, or regression after the reward and layout changes. The later MCP outage prevents a fresh comparison and is not treated as a gameplay failure or as validation evidence.

The ten package scenarios remain reconciled at weak, normal, and high-chaos conditions in `docs/plans/chaos_warfare_system_plans/2026-07-29_stage_14_package_scenario_evidence.md`. The reward-density and bloat result remains recorded in `docs/plans/chaos_warfare_system_plans/2026-08-09_reward_density_and_bloat_audit.md`.

## Genuine remaining blockers, omissions, and user-owned evidence

- Continuous ordinary-air contamination is omitted because no verified current-version hook proves eligible aircraft activity and release. No estimator is retained.
- Four ground chemical operation families remain fail-closed because exact selected-state weather, terrain, and release-condition receipts are unavailable.
- The separate legacy selected-state mobile nerve-suppression operation remains fail-closed. The supported camp method is unaffected.
- Hardened Mobile Plant remains omitted because no exact bombing or facility-capture transaction exposes the decontamination-equipment model and amount lost. No substitute reliability bonus exists.
- Air Is Still Breathable, No Wind Is Friendly, The Antidote Arrived, and Unbroken Supply Corridor remain omitted because their exact receipts are unavailable and the user authorized skipping impossible content.
- Historically sourced unique national MIO corporation identities remain skipped as non-core. Distinct functional MIO families, trees, and differentiated country AI are active; no corporation was invented.
- Exact live production shares, long-duration AI campaign pacing, native random outcomes, facility rendering in the running game, and UI overflow at live resolutions remain user-owned validation.
- Fresh engine-backed technology, doctrine, event, scripted-GUI, and probability evidence is blocked by the current HOI4 MCP timeout and closed transport.
- A fresh decision-mission specialist report is blocked by the missing dispatched audit task; bounded parent source review is recorded but is not presented as specialist evidence.

No other supported-core mechanical omission, placeholder, fallback, duplicate subsystem, broad all-country periodic pulse, or unresolved source audit finding was retained in this closure tranche. Further shortening of already-correct optional tooltips remains non-core prose polish rather than a gameplay or source-readiness blocker.
