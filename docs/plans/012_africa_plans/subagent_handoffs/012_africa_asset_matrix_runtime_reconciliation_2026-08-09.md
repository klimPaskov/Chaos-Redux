# Event 012 Africa asset matrix runtime reconciliation

## Result

The 239-row asset and animation matrix remains the acceptance source of truth. Its current release-candidate distribution is 84 `installed_runtime`, 28 `installed_dormant`, 117 `deferred_controlled_pool`, 10 `deferred_runtime_gated`, zero `deferred_model_required`, zero `deferred_unique_package_required`, and zero `pending_runtime_blocker` rows.

The matching 239 `asset_item` rows in `docs/plans/012_africa_plans/012_africa_acceptance_ledger.csv` retain the same key order and dispositions. The ledger keeps its UTF-8 BOM and now records direct binary, GFX, consumer, source-frame, visual-review, and model-package evidence for the 32 promoted rows rather than repeating a status-only claim.

## Rows promoted to installed runtime

All 18 requested animation concepts are installed with separately authored source frames, processed frames, a horizontal sheet, a static fallback, runtime sheet and static DDS files, a review GIF, a contact sheet, a row manifest, and a registered consumer:

- `colonial_pressure_border`
- `selected_member_confidence`
- `congress_ready_emblem`
- `member_departure_warning`
- `rival_bloc_alert`
- `africa_is_one_completion`
- `ecological_wrath_active`
- `continent_war_terminal`
- `host_overlay_federal_amalgamation`
- `host_first_proof_state_kit`
- `federal_deadlock_warning`
- `republic_first_election_states`
- `military_commander_loyalty_states`
- `confederal_emergency_ratification_states`
- `covenant_obligation_review_states`
- `postwar_constitutional_review_states`
- `priority_member_promotion_card`
- `route_capstone_seal_family`

The first eight status families plus the host overlay and route capstone are consumed by the Event 12 Charter GUI. The remaining eight are consumed by Event 12 decisions. `interface/012_africa_animations.gfx` provides the 36 animated/static registrations.

The six promoted Tier A country visual packages are installed on their approved existing Independence Wave carriers without new tags or state substitutions:

- `country_package_pan_high_chaos`
- `country_package_gorilla_kingdom`
- `country_package_the_green`
- `country_package_living_rivers`
- `country_package_stoneborn`
- `country_package_ancient_hosts`

Each package has its three-size flag ladder, unique emblem, cosmetic identity, one adult male fictional ruler portrait on a plain background, package gameplay, AI, settlement logic, and strange-force relationship. The matrix's 52 Tier A portrait contracts now explicitly forbid female characters and council or group portraits.

The eight strange-force identity rows are installed with unique technology, decision, focus, emblem, counter, equipment, technology, subunit, formation, entity, model, action, and sourced-audio packages:

- `unit_identity_gorilla_heavy_infantry`
- `unit_identity_pan_sappers`
- `unit_identity_stone_cohorts`
- `unit_identity_riverborn`
- `unit_identity_forest_giants`
- `unit_identity_oracle_recon`
- `unit_identity_disaster_wardens`
- `unit_identity_plague_carriers`

## Evidence

- Animation source and review package: `docs/assets/012_africa/animations/`
- Animation registration: `interface/012_africa_animations.gfx`
- Charter consumers: `interface/012_africa_charter.gui` and `common/scripted_guis/012_africa_charter_scripted_gui.txt`
- Decision consumers: `common/decisions/012_africa_decisions.txt`
- Tier A visual package: `docs/assets/012_africa_tiera_visual_packages/`
- Portrait package: `docs/assets/012_africa/portrait_acceptance_2026-08-09/`
- Strange-force visual package: `docs/assets/012_africa/strange_force_identity_icons/`
- Strange-force model packages: `docs/assets/012_africa/models_3d/`
- Animation acceptance handoff: `docs/plans/012_africa_plans/subagent_handoffs/012_africa_animation_acceptance_final_2026-08-09.md`
- Tier A visual handoff: `docs/plans/012_africa_plans/subagent_handoffs/012_africa_tiera_visuals_final_2026-08-09.md`
- Model and runtime handoffs: the Event 12 model and strange-force handoffs under `docs/plans/012_africa_plans/subagent_handoffs/`

The overall animation contact sheet and both Tier A flag/emblem contact sheets were visually reviewed. Runtime DDS dimensions and headers, exact frame counts, non-empty and non-duplicated animation frames, GIF frame counts, flag sizes, emblem round trips, counter round trips, model-package manifests, and audio format evidence are recorded in their accepted handoffs.

## Remaining disposition boundary

The 117 `deferred_controlled_pool` and 10 `deferred_runtime_gated` rows are explicit controlled-pool or political-readiness dispositions, not missing runtime references. No matrix row remains model-blocked. Live in-game playback, visibility, and model rendering are owned by the user and are not claimed by this reconciliation.
