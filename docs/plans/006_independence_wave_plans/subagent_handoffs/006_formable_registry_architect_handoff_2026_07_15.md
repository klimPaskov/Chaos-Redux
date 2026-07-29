# Event 006 shared formable registry architecture handoff

Date: 2026-07-15

Owner: `event6_formable_registry_architect`

## Status

The shared FORM-01 through FORM-48 registry and transaction framework is implemented. All 48 source rows have stable IDs, profile data, loader coverage, and presentation names. The implementation intentionally declares **0/48 families operational**.

No country tag, cosmetic identity, annexation, autonomy change, subject arrangement, or focus-tree replacement is supplied by the shared core. A family cannot open its congress until its exact family-bound territory, X-ending identity, full flag package, identity adapter, integration adapter, and living-member policy are certified. There is no fallback tag or fallback adapter.

## Files changed

Modified shared files:

- `common/decisions/006_independence_wave_decisions.txt`
  - Rewired DM-53 through DM-56 to the shared registry.
  - DM-56 now uses the bounded `independence_wave_formable_integration_state_entries` target array.
- `common/script_constants/006_independence_wave_formable_constants.txt`
  - Added method masks, consent rules, AI and risk tiers, formable cost and duration tuning, and 48 registry profiles.
- `common/scripted_effects/006_independence_wave_decision_effects.txt`
  - Delegates the legacy commit request to the shared transaction, gates state integration on the registered array, and runs registry cleanup through the decision-layer cleanup.
- `common/scripted_effects/006_independence_wave_focus_effects.txt`
  - The narrow shared `independence_wave_focus_register_formable_family` helper now preloads the selected profile after a package sets its family ID.
- `common/scripted_triggers/006_independence_wave_decision_triggers.txt`
  - Expanded the shared active-operation lock and delegated generic preparation to the registry trigger.
- `localisation/english/006_independence_wave_decisions_l_english.yml`
  - Made DM-53 through DM-56 names and descriptions family- and method-aware.

New shared files:

- `common/decisions/006_independence_wave_formable_registry_decisions.txt`
- `common/decisions/categories/006_independence_wave_formable_registry_categories.txt`
- `common/scripted_effects/006_independence_wave_formable_registry_effects.txt`
- `common/scripted_triggers/006_independence_wave_formable_registry_triggers.txt`
- `common/scripted_localisation/006_independence_wave_formable_registry_scripted_localisation.txt`
- `localisation/english/006_independence_wave_formable_registry_l_english.yml`
- `docs/events/006_independence_wave/systems/formable_registry.md`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_formable_registry_architect_handoff_2026_07_15.md`

No RHI, BAY, SCO, or WLS package-owned decision, effect, trigger, focus, or localisation file was edited.

## Registry profile and discovery

`independence_wave_formable_family` retains the stable numeric FORM mapping `1` through `48`. `independence_wave_formable_registry` contains exactly one row per CSV family with:

- `region`;
- `methods` bit mask;
- `discovery` class;
- `minimum_members`;
- `minimum_consents`;
- `minimum_anchors`;
- `ai_willingness`;
- `risk_tier`.

`independence_wave_formable_load_selected_family_profile` has one loader branch per row and snapshots the selected family. `independence_wave_focus_register_formable_family` calls it after package registration, so the discovery trigger can enforce the stored class without copied family decisions.

Discovery classes are enforced as follows:

- mature-tree and route profiles use the common Event 006 formable-discovery focus;
- map-state profiles additionally require `independence_wave_formable_map_reveal_ready`;
- league-state profiles require league membership, `independence_wave_league_route_available`, or `independence_wave_formable_league_reveal_ready`;
- hidden profiles require `independence_wave_formable_hidden_reveal_ready`;
- hidden high-chaos profiles also require the Event 006 high-chaos action gate.

These reveal gates do not certify formation readiness.

## Shared decisions

One category, `independence_wave_formable_transaction_category`, owns nine generic choices rather than 48 copied chains.

Formation-method decisions:

- `independence_wave_select_negotiated_formation_method`;
- `independence_wave_select_dynastic_formation_method`;
- `independence_wave_select_revolutionary_formation_method`;
- `independence_wave_select_military_formation_method`;
- `independence_wave_select_league_formation_method`;
- `independence_wave_select_hidden_formation_method`.

Consent-rule decisions:

- `independence_wave_choose_voluntary_membership`;
- `independence_wave_choose_unanimous_compact`;
- `independence_wave_choose_controlled_settlement`.

Stable legacy decisions retained and rewired:

- `independence_wave_discover_regional_identity` (DM-53);
- `independence_wave_convene_formation_congress` (DM-54);
- `independence_wave_proclaim_military_union` (DM-55, dynamically presented as Ratify the selected family);
- `independence_wave_integrate_member_region` (DM-56).

The congress is a selectable 360-day window. On selection it pays the strategic cost, refreshes the bounded ledger, calculates profile/member risk, and resolves success or failure. Success and failure stat consequences are idempotent. A successful final commit clears the formation-ready lock before DM-56 becomes available.

## Public effects

Core lifecycle effects:

- `independence_wave_formable_load_selected_family_profile`;
- `independence_wave_formable_complete_discovery`;
- `independence_wave_formable_select_method`;
- `independence_wave_formable_select_consent_rule`;
- `independence_wave_formable_begin_preparation`;
- `independence_wave_formable_resolve_congress`;
- `independence_wave_formable_commit_selected_family`;
- `independence_wave_formable_cleanup_runtime`.

Ledger and consent effects:

- `independence_wave_formable_build_member_and_anchor_ledgers`;
- `independence_wave_formable_recount_member_and_anchor_ledgers`;
- `independence_wave_formable_declare_consent_for_selected_family`;
- `independence_wave_formable_withhold_consent_for_selected_family`;
- `independence_wave_formable_clear_consent_declaration`;
- `independence_wave_formable_end_consenting_member_origin`.

Adapter dispatch effects:

- `independence_wave_formable_dispatch_identity_adapter`;
- `independence_wave_formable_dispatch_integration_adapter`.

The dispatch names are numeric and exact:

- `independence_wave_formable_identity_adapter_<family id>`;
- `independence_wave_formable_integration_adapter_<family id>`.

For example, FORM-01 owns adapters ending `_1`, and FORM-48 owns adapters ending `_48`. No such adapter is defined by this tranche.

## Public triggers

Selection and discovery:

- `has_valid_independence_wave_formable_family_selection`;
- `independence_wave_formable_profile_matches_selected_family`;
- `has_independence_wave_formable_discovery_gate`;
- `can_independence_wave_discover_selected_formable_family`.

Method, consent, and AI:

- `supports_independence_wave_formable_method_input`;
- six `supports_independence_wave_formable_<method>_method` helpers;
- `is_independence_wave_formable_consent_rule_input_compatible`;
- `should_independence_wave_ai_pursue_selected_formable`.

Ledger, readiness, and commit:

- `independence_wave_formable_member_arrays_are_aligned`;
- `can_independence_wave_formable_pass_congress_vote`;
- `has_independence_wave_formable_commit_readiness`;
- `can_independence_wave_prepare_selected_formable_transaction`;
- `can_independence_wave_commit_selected_formable`;
- `can_pay_independence_wave_selected_formable_commit_cost`;
- `is_registered_independence_wave_formable_integration_state`;
- `has_independence_wave_formable_transaction_lock`.

`can_independence_wave_prepare_formable` delegates to the registry preparation trigger while retaining the existing regional-power legitimacy and instability gates.

## Family-bound readiness contract

The owning adapter must first set:

- `independence_wave_formable_readiness_family` to the same numeric value as `independence_wave_formable_profile_family`.

It must then set all six flags only after their evidence is complete:

- `independence_wave_formable_territory_adapter_ready`;
- `independence_wave_formable_x_tag_reserved`;
- `independence_wave_formable_flag_package_ready`;
- `independence_wave_formable_identity_adapter_ready`;
- `independence_wave_formable_integration_adapter_ready`;
- `independence_wave_formable_member_policy_audited`.

The trigger rejects flags bound to another family. At handoff time there are no setters for any of these six flags anywhere under `common/`, so every family remains fail-closed.

The identity adapter must set `independence_wave_formable_identity_committed` only after its atomic identity work succeeds. The integration adapter must set `independence_wave_formable_integration_committed` only after its reviewed member and territory settlement succeeds. Missing commit acknowledgements fail the transaction; they do not select a substitute identity.

## Ledgers and arrays

The proposer owns aligned bounded arrays:

- `independence_wave_formable_member_country_entries`;
- `independence_wave_formable_member_generation_entries`;
- `independence_wave_formable_member_anchor_entries`;
- `independence_wave_formable_member_consent_entries`.

The post-commit integration target surface is:

- `independence_wave_formable_integration_state_entries`.

Rows are built only by an explicit discovery/congress action over `global.independence_wave_active_countries` and its aligned generation array. There is no daily, weekly, monthly, all-country, or all-state iteration.

Human non-proposers default to observer. Family packages can expose invitations or consent UI through the three shared consent-declaration effects. AI consent is conservative and deterministic before the congress risk roll.

## Shared active-operation lock

`has_independence_wave_active_formable_operation` recognizes the generic congress, bounded integration decision, registry transaction lock, and these package conferences:

- `independence_wave_sco_convene_maritime_conference`;
- `independence_wave_wls_convene_celtic_council`;
- `independence_wave_afx_convene_meuse_industrial_conference`;
- `independence_wave_agx_convene_north_sea_coastal_conference`;
- `independence_wave_rhi_convene_rhine_congress`;
- `independence_wave_bay_convene_south_german_estates`.

Future registry work should extend this one helper when a genuinely independent package operation must be mutually exclusive. It should not add parallel local lock logic.

## Origin separation and living members

`independence_wave_formable_end_consenting_member_origin` is member-country scope and can run only during the proposing transaction. It rechecks that the country has a consenting row, rejects the proposer, sets the canonical Event 006 `formable_absorption` reason, and calls `independence_wave_end_active_origin`.

This preserves the durable Event 006 origin record and uses Event 006 package/decision/focus/league/network cleanup. It does not inspect, clear, or rewrite Event 005 active or historical origin state. The shared core does not annex the member or decide whether it remains independent, becomes a subject, or joins another identity; those actions require the family policy audit.

## Localisation and assets

Scripted localisation functions:

- `GetIndependenceWaveSelectedFormableName`;
- `GetIndependenceWaveSelectedFormableMethodName`;
- `GetIndependenceWaveSelectedFormableConsentRuleName`;
- `GetIndependenceWaveFormableCommitCostText`.

All 48 working registry names have an internal scripted-localisation mapping, but the source matrix explicitly marks them as non-final. Parent review added the full family-readiness proof to the discovery gate, so none is player-visible until its owning family supplies a researched final identity/localisation package. These internal labels do not create a national identity and must be replaced or explicitly approved before a family is certified.

The shared layer reuses four registered Event 006 decision sprites. It creates no new visual asset. Each future identity still requires the base, medium, and small flag plus every required ideology variant before `independence_wave_formable_flag_package_ready` may be set.

## Balance and validation evidence

- CSV rows, stable family IDs, profile rows, loader branches, and family-name localisation branches each count exactly 48; the family IDs are contiguous `1..48`, and all five name sets match.
- The nine generic decisions all have name and description localisation.
- Both touched English localisation files retain UTF-8 BOM encoding; the 86 new registry localisation keys are unique across English localisation.
- The six package conference IDs in the shared lock resolve to real decision definitions.
- New core files contain no tag/cosmetic-tag mutation, annexation, autonomy mutation, periodic hook, all-country scan, or all-state scan.
- No family identity/integration adapter definition and no readiness-flag setter exists, proving the runtime gate remains closed for all 48 rows.
- Congress risk weights are bounded to 5-85% failure and paired with a complementary success weight summing to 100. The proposer/member/anchor/consent thresholds are profile data rather than decision copies.
- Combined civic commits require the full 40 command-power total consumed by the strategic and administrative effects.
- Failure and success country deltas are idempotent; successful commit clears the ready lock so the bounded integration surface can open.

No commit was created by this subagent.

## Simplifications, omissions, and blockers

- **0/48 families are operational.** This is deliberate scope safety, not a completion claim for any formable family.
- The 48 matrix names remain internal working labels, not accepted final localisation. Discovery is fail-closed behind the complete readiness gate until each owning family replaces or explicitly certifies its public identity text.
- No X-ending identity has been reserved or re-audited, no country/cosmetic tag has been added, and no complete family flag package exists in this tranche.
- No exact family territory map, capital alternative, exclusion list, identity adapter, integration adapter, or living-member settlement is supplied. Each remains owning-family work.
- The shared consent helpers exist, but family-specific invitations, player-facing member consent events/decisions, capital ballots, concessions, and refusal consequences remain adapter/content work.
- Existing package conference completion effects that call `independence_wave_decision_request_selected_formable_commit` are now safely rejected unless the generic method, consent, congress, family binding, and all readiness attestations have completed. Package owners must route those conferences into the generic transaction before claiming a family operational.
- No spreadsheet row was changed. The existing 48-row CSV remains the source profile, while operational identity/territory/integration facts do not yet exist to record as completed content.
- No asset was generated and no placeholder or borrowed flag was used.

No fallback or hidden simplification was used in the shared framework. The missing family implementations are explicit blockers enforced by code.
