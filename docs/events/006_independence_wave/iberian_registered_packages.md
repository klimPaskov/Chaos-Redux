# Event 006 Iberian registered packages

## Scope

IW-013 Basque Country reuses the vanilla `NAV` carrier and the installed-map País Vasco state 792 as its compact release anchor. Navarra 172 and French Basque 806 are optional territorial objectives after release. IW-015 Galicia reuses the vanilla `GLC` carrier and state 171 as its compact anchor. Neither package creates a country, history file, replacement tag, advisor, or new leader identity.

Both carriers receive the shared Event 006 full framework because their vanilla carrier histories expose only the generic focus surface. The setup adapter preserves their vanilla history, flag, existing ruling-leader roster, and non-Event-006 identity surfaces. Startup history supplies the additive sourced male corps-command consumer for NAV; GLC reuses its vanilla Fuco Gómez and Alfonso Daniel Castelao country-leader roles and receives no second Castelao character. The synchronous Event 006 roster checkpoint validates NAV's pre-defined commander and GLC's preserved leader roster, writes their checkpoint flags, and applies the package-scoped Castelao portrait override only to GLC's existing liberal leader. These roles do not replace vanilla leaders or create advisor art.

## Runtime flow

1. The frozen allocator publishes package ID, anchor, former host, region, depth, archetype, and force level before the synchronized release transaction.
2. `independence_wave_dispatch_iberian_package_setup` initializes the matching carrier only when the package's prepared anchor and former-host targets remain valid.
3. NAV tracks `independence_wave_nav_fueros_legitimacy` and `independence_wave_nav_industrial_capacity`; GLC tracks `independence_wave_glc_council_legitimacy` and `independence_wave_glc_port_capacity`. Each lifecycle swaps its contested or compact idea at the shared stability threshold.
4. Paid decisions and the founding mission write country, host, Network, and League ledgers. Route decisions lock constitutional, popular-council, traditional, emergency, or patron-client government ideas. NAV and GLC founding missions participate in the shared active-founding-mission lock, so neither Iberian crisis can start while another Event 006 founding mission is active and generic founding actions cannot overlap either crisis. NAV and GLC projects remain hidden and unavailable until their exact setup checkpoint is complete and their founding crisis has not failed; the network project additionally waits for founding-settlement and crisis-resolution flags plus a stable compact. Timed projects cancel on package invalidation, capital loss, host loss where applicable, or withdrawal of the required League route, and the guarded cancellation path does not apply a second failure penalty after a terminal founding failure.
5. The package loads the centralized force mapping (`p13` mountain-frontier for NAV and `p15` territorial-defense for GLC) and materializes the generation-aware dynamic starting force only after the package's roster gate is present. NAV requires its named corps commander; GLC requires its preserved Fuco Gómez/Castelao country-leader roster and uses an institutional officer commission for the p15 force.
6. NAV route selection applies one of four generated route-specific cosmetic identities (`NAV_INDEPENDENCE_WAVE_CIVICX`, `NAV_INDEPENDENCE_WAVE_AGRARIANX`, `NAV_INDEPENDENCE_WAVE_SOCIALISTX`, or `NAV_INDEPENDENCE_WAVE_EMERGENCYX`) while leaving vanilla NAV unchanged before setup and after cleanup.
7. Generation cleanup retires only NAV's additive Event 006 corps-command consumer, clears the shared command-roster readiness bit, restores GLC's vanilla Castelao portrait if the package override was applied, drops any NAV route cosmetic identity, and removes the package's own decisions, ideas, variables, and flags. It does not remove vanilla history, ruling leaders, flags, or unrelated diplomatic relations.

## Politics and parties

Setup normalizes each carrier's authored starting popularity and democratic provisional government before the founding mission opens. Route governments then replace the provisional party labels with institutional Basque or Galician names while preserving the vanilla leader roster and country tag.

## File ownership

- `common/script_constants/006_independence_wave_constants_registry.txt` owns politics, ledger, duration, and AI tuning.
- `common/scripted_triggers/006_independence_wave_iberian_package_triggers.txt` owns carrier identity, anchor, lifecycle, force, route, and completion proofs.
- `common/scripted_effects/006_independence_wave_iberian_package_effects.txt` owns setup, ledger transactions, routes, dynamic force handoff, final validation, and cleanup.
- `common/decisions/006_independence_wave_iberian_decisions.txt` owns the two paid project categories and their founding missions.
- `common/ideas/006_independence_wave_ideas_registry.txt` owns the mutually exclusive carrier lifecycles and route ideas.
- `common/ai_strategy/006_independence_wave_ai_strategy_registry.txt` owns survival, host-restraint, settled-economy, and emergency command weights.
- `localisation/english/006_independence_wave_iberian_l_english.yml` owns all player-facing names, descriptions, tooltips, and idea text.
- `common/countries/cosmetic.txt` and `gfx/flags/{,medium,small}/NAV_INDEPENDENCE_WAVE_*.tga` own the four generated route-specific NAV identities; their alternate-history provenance and QA are recorded in `docs/assets/006_independence_wave/iw013_nav_flags_2026_08_13/`.

## Icon surface

The decisions reuse the audited Event 006 decision sprites `GFX_decision_independence_wave_integration_missions`, `GFX_decision_independence_wave_army_integration_actions`, `GFX_decision_independence_wave_government_actions`, `GFX_decision_independence_wave_former_host_negotiations`, and `GFX_decision_independence_wave_league_votes`. Ideas reuse the audited Event 006 idea pictures `independence_wave_fragmented_command`, `independence_wave_founding_identity`, and `independence_wave_improvised_government`. No advisor icon is requested or referenced.

## Admission boundary

The package adapters and dispatch hooks are source-wired, and each command-roster gate proves the package's required leader or commander before force mapping. NAV route flags are generated alternate-history identities with validated runtime ladders, not claims of a newly attested historical 1936 state flag. The GLC duplicate-identity issue is resolved at source by preserving the vanilla Castelao country-leader role, applying the supplied portrait through a generation-scoped override, and using an institutional officer commission rather than recruiting a second Castelao. Central content attestation remains fail-closed until the rights caveat, independent country-package audit, current AI/probability evidence, and current MCP evidence are accepted. FORM-07 remains separately fail-closed until its X-ending identity, flag package, and all-member integration proof are reviewed. This boundary is intentional and prevents a partial package from entering the automatic ladder.

## Current GLC identity gate

Vanilla Galicia already owns Alfonso Daniel Castelao as a country leader. Event 006 no longer defines or recruits a second Castelao character: `has_independence_wave_glc_command_roster` proves the existing Fuco Gómez and Castelao country-leader roles with `ruling_only = no`, and the synchronous roster checkpoint applies `GFX_portrait_GLC_alfonso_daniel_castelao` to the existing liberal role once per package generation. The p15 force mapping uses an institutional officer commission, and cleanup restores `GFX_portrait_Alfonso_Daniel_Castelao` before clearing the override flag. This resolves the duplicate identity at source; central admission remains fail-closed for the independent rights, package, AI/probability, and MCP gates and does not follow from this repair alone. The former duplicate-identity audit remains dated provenance: `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw015_glc_duplicate_identity_audit_2026_08_14.md`.

## Current portrait-source policy

The current exact-input wiring audit records the selected supplied portrait rows as grounded `source_placeholder` inputs, while the older 2026-08-26 closure uses `styled_final` terminology for the NAV and GLC runtime states. GLC Alfonso Daniel Castelao is now consumed only by the generation-scoped override on the existing vanilla liberal country-leader role; GLC Bóveda remains an unmapped supplied input and is not relabelled to Castelao. The installed basenames remain stable, rights remain `PASS_WITH_CAVEAT / NEEDS_USER_REVIEW` for the reviewed NAV and GLC outputs, and no central package admission follows. NAV projects still fail closed after an IW-013 founding-crisis failure through the shared project-ready trigger, and independent source, identity, rights, flag, role, package, central-attestation, and gameplay gates remain open. No Event 006 advisor icons are authorized. See `../../plans/006_independence_wave_plans/subagent_handoffs/006_portrait_wiring_reconciliation_2026-08-30.md` and the dated closure `../../plans/006_independence_wave_plans/subagent_handoffs/006_iw013_iw015_user_supplied_portrait_final_audit_2026-08-26.md`.

## Future depth

The next approved tranche is the independent country-package and AI/probability audit for the existing NAV and GLC rosters. NAV's named command consumer remains a grounded source-placeholder role, while GLC uses the supplied Castelao portrait only on its existing country-leader role and has no additive Event 006 commander. A styled replacement is only an explicit-request work item; optional NAV extension states should only be added through the current-map binding after a fresh host-survival and reservation-group check.
