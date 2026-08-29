# Event 006 decision and mission cost-lock repair handoff

Date: 2026-08-29.

## Scope and status

This tranche repairs the accepted Event 006 administration-cost mismatches and package foundation mission locks in the current decision source.

The source patch is complete for the scoped decision and trigger surfaces.

The DM-35 Later cost row was completed in the follow-up localization commit `3fd0c7613` after the original source-file boundary was lifted.

## Changed files and identifiers

- `common/decisions/006_independence_wave_balkan_decisions.txt`: added the matching civilian-factory reservation to the twelve current AXX, BOS, BBX, MAC, BAX, and TRA administration route decisions.
- `common/decisions/006_independence_wave_decisions.txt`: added the shared light administration reservation to `independence_wave_retain_former_host_officials` and made the repeat branch of `independence_wave_balance_patrons` require only the command power and manpower it actually pays.
- `common/decisions/006_independence_wave_form03_decisions.txt`: added the shared light administration reservation to `independence_wave_form03_publish_member_language_codes`.
- `common/decisions/006_independence_wave_iw043_iw058_decisions.txt`: changed `independence_wave_iw043_ratify_mari_udmurt_language_rights` to use explicit command-power and manpower affordability, matching its transaction and package-specific cost text.
- `common/decisions/006_independence_wave_karelia_crimea_decisions.txt`: added the shared light administration reservation to the KAR and CRI constitutional mandate decisions.
- `common/decisions/006_independence_wave_mediterranean_decisions.txt`: added light or standard reservations to the six COR, ARX, and ASX administration route decisions.
- `common/decisions/006_independence_wave_pacific_decisions.txt`: added the shared light administration reservation to `independence_wave_fij_register_communal_veto`.
- `common/decisions/006_independence_wave_western_decisions.txt`: added the shared light administration reservation to the three BRI and two CAT administration route decisions.
- `common/scripted_triggers/006_independence_wave_balkan_package_triggers.txt`: added `has_active_mission` checks for the AXX, BOS, BBX, MAC, and BAX foundation missions to their package-local active-project helpers.

No scripted effects, scripted GUI definitions, localization identifiers, or decision categories were changed.

## Behavior before and after

The affected generic administration decisions advertised a civilian-factory requirement through `independence_wave_cost_administration_light` or `independence_wave_cost_administration_standard`, but their timed decision blocks did not reserve that capacity.

Each of the 28 current generic administration blocks now declares the matching `civilian_factory_use` modifier while its timer is active, using the package-local constant where one exists and the shared constant elsewhere.

The administration payment helpers continue to consume the existing command-power and manpower constants, so the patch aligns the declared factory burden with the existing payment and tooltip semantics without changing the accepted resource amounts.

The IW-043 Mari-Udmurt clause used a package-specific cost string that displayed command power and manpower only, while it reused a generic affordability helper that also checked civilian factories.

Its available and custom-cost triggers now check the two consumed resources directly, and the transaction effect remains unchanged.

DM-35 already pays `independence_wave_decision_pay_diplomatic_standard` on every completion and adds `independence_wave_decision_pay_administration_light` after the minimum patron-balance state.

Its repeat affordability branch now matches that payment palette with command power and manpower only, so it no longer hides a non-reserved factory-capacity requirement.

The `independence_wave_cost_patron_balance` and blocked variant now repeat the always-paid diplomatic-standard command power and convoy-or-train cost on the Later line, followed by the later administration-light command power and manpower cost.

The five package foundation missions were automatic missions outside the package active-project helper because the helper only tested decisions and stale foundation flags.

Each helper now also returns true while its package foundation mission is active, preventing package administration projects from running in parallel with that foundation mission.

## Cost and requirement audit

The current Event 006 decision source contains 153 generic administration cost blocks using the shared administration localization keys.

The post-patch static crosswalk found zero generic administration blocks without a `civilian_factory_use` modifier.

The generic light and standard administration rows remain three-value surfaces with command power, manpower, and civilian-factory capacity.

DM-35 remains three distinct resource types per branch after the source correction: command power, the selected convoy-or-train channel, and manpower on the Later path.

IW-043 now exposes and consumes two resource types: command power and manpower.

All displayed spendable values continue to use the existing texticons from their current localization keys.

## Validation

The six strict Event 006 validators passed after the patch: allocator, Statehood Ledger GUI matrix, SCN-008 scenario matrix, country API, FORM-16 contract, and registered-tag flag coverage.

The task-specific static audit reported 153 generic administration blocks and zero missing factory reservations.

The source cross-check confirmed that DM-35 contains both its unconditional diplomatic-standard payment and its repeat administration-light payment.

The localization cross-check confirmed that both DM-35 cost variants disclose those same recurring resources without static values.

The source cross-check confirmed all five foundation mission IDs resolve in the package-local active-project helpers.

The required `hoi4.gui_inspect` and `hoi4.gui_render` routes were not callable in this runtime, so no production GUI evidence is claimed.

The required `hoi4.probability_inspect` and `chaosx_ai_probability_auditor` routes were not callable in this runtime, so no quantitative AI or balance conclusion is claimed.

The agent did not launch Hearts of Iron IV or claim live-save validation.

## Remaining issues and parent follow-up

- Review the existing strategic cost rows that use `independence_wave_cost_strategic` without a local factory reservation if that broader cost-family mismatch is admitted into a later tranche.
- Retain the latest Event 006 SCN-008 failure-ledger leak and shared GUI/probability evidence blockers from `006_event6_decisions_audit_current_2026-08-29.md`; they are outside this bounded patch.

No new decision system, category, mission family, scripted GUI, formable, or broad balance redesign was introduced.
