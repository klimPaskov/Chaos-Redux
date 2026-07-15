# Event 006 NWE Route-Matrix Remediation Handoff

Date: 2026-07-15

Scope: `IW-008` Rhineland (`RHI`) and `IW-009` Bavaria (`BAY`)

Mode: parent-authorized bounded gameplay patch; no Git commit

Parent integration note: a later independent audit certified only `IW-009`
Bavaria. Its exact runtime content-attestation and `IW-009`/`BAY` SCN-008
preflight branches are applied; every other package remains fail-closed.

## Outcome

The country-package audit findings in `006_nwe_country_package_audit_2026_07_15.md` are remediated.

- RHI publishes only constitutional, popular/labor, emergency-military, and patron-client governments. Traditional and radical sovereignty remain unavailable.
- BAY publishes only constitutional, popular/labor, traditional/restoration, and emergency-military governments. Patron-client and radical sovereignty remain unavailable.
- BAY remains a South German ambition package with no selected or registered shared formable family.
- The automatic and scenario readiness gates remain fail-closed.
- No formable, asset, placeholder, fallback, or simplified route was added.

The accepted route source was reconciled against:

- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_nwe_package_implementation_map.md`
- `docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_nwe_country_package_audit_2026_07_15.md`

## Runtime changes

### Removed unaccepted government content

Deleted decisions:

- `independence_wave_rhi_proclaim_sovereign_corridor`
- `independence_wave_bay_accept_patron_estates_mandate`
- `independence_wave_bay_proclaim_sovereign_directorate`

Deleted route ideas:

- `rhi_sovereign_corridor_directorate`
- `bay_patron_estates_mandate`
- `bay_sovereign_mountain_directorate`

Deleted government state flags and their installer paths:

- `independence_wave_rhi_sovereignty_government`
- `independence_wave_bay_patron_government`
- `independence_wave_bay_sovereignty_government`
- `independence_wave_install_rhi_sovereignty_government`
- `independence_wave_install_bay_patron_government`
- `independence_wave_install_bay_sovereignty_government`
- `independence_wave_set_rhine_bavaria_sovereignty_popularities`

The associated party, idea, and decision localisation was removed. The unused sovereignty popularity fields were also removed from `independence_wave_rhine_bavaria_politics`.

### Persistent Evolution 5 exclusion

The new generic opt-out flag is:

- `independence_wave_radical_sovereignty_route_excluded`

Lifecycle:

1. `independence_wave_setup_iw_008_rhineland` and `independence_wave_setup_iw_009_bavaria` set it and clear `independence_wave_route_radical_sovereignty_available`.
2. `has_prepared_independence_wave_iw_008_package_setup` and `has_prepared_independence_wave_iw_009_package_setup` require the exclusion flag and prove that radical availability is absent.
3. `independence_wave_apply_open_sovereignty_to_country` grants the radical route only when the exclusion is absent; its excluded branch actively clears stale radical availability.
4. `independence_wave_cleanup_iw_008_rhineland` and `independence_wave_cleanup_iw_009_bavaria` clear the exclusion for generation cleanup.

Both existing callers use the guarded effect:

- `independence_wave_deliver_open_sovereignty` for active-country delivery
- `independence_wave_apply_frozen_evolution_opening` for a country born after the evolution

Countries that do not set the exclusion retain the previous Open Sovereignty route grant.

### High-chaos actions

The one-shot actions remain distinct from permanent government routes:

- `independence_wave_rhi_seize_corridor_authorities`
- `independence_wave_bay_seize_south_german_protectorates`

Their visibility requires any accepted package government. Availability uses the package trigger `can_independence_wave_use_rhine_bavaria_high_chaos_actions`, which requires:

- an exact RHI or BAY Event 006 package;
- regional-power status;
- `independence_wave_unlock_high_chaos_actions`; and
- the Open Sovereignty evolution.

The existing major security cost remains. Neither action tests, publishes, or installs Radical Sovereignty, and player-facing descriptions state that the settled government remains in force.

### AI and dispatcher alignment

- RHI corridor-command strategy and the River Defense Planner no longer test the removed RHI sovereignty government.
- BAY civic-industry strategy no longer tests a patron government.
- BAY mountain-guardian strategy no longer tests a sovereignty government.
- High-chaos strategy remains tied to the completed one-shot action flags.
- Dispatcher documentation now maps RHI to `FORM-04` and records BAY as a South German ambition with no formable family. It no longer implies a BAY dependency on `FORM-01`, `FORM-02`, or `FORM-04`.

## Files changed

- `common/ai_strategy/006_independence_wave_rhineland_bavaria.txt`
- `common/characters/006_independence_wave_nwe_advisors.txt`
- `common/decisions/006_independence_wave_rhineland_bavaria_decisions.txt`
- `common/ideas/006_independence_wave_rhineland_bavaria_ideas.txt`
- `common/script_constants/006_independence_wave_rhineland_bavaria_constants.txt`
- `common/scripted_effects/006_independence_wave_rhineland_bavaria_package_effects.txt`
- `common/scripted_effects/006_independence_wave_evolution_effects.txt`
- `common/scripted_triggers/006_independence_wave_rhineland_bavaria_package_triggers.txt`
- `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt`
- `localisation/english/006_independence_wave_rhineland_bavaria_l_english.yml`
- `docs/006_independence_wave_rhineland_bavaria_packages.md`
- `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_2_event_flow_and_evolutions.md`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_rhi_bay_gameplay_handoff_2026_07_15.md`
- this handoff

## Validation evidence

- Setup extraction proves exactly four accepted government-route helpers for each package and no unaccepted helper.
- The persistent exclusion has exactly two setup setters, two cleanup clearers, two prepared-proof requirements, and one shared evolution reader.
- Both Open Sovereignty delivery paths call the guarded effect; the non-excluded branch preserves the shared grant and the excluded branch clears radical availability.
- All thirteen removed runtime identifiers listed above are absent from `common/`, Event 006 runtime localisation, and the current package documentation.
- Both regional high-chaos decisions use the package-local unlock trigger, and neither decision nor that trigger references the generic Radical Sovereignty government state or `can_independence_wave_use_high_chaos_actions`.
- BAY setup clears formable selection, never calls `independence_wave_focus_register_formable_family`, and sets `independence_wave_bay_south_german_ambition`.
- Both content-attestation gates still resolve through `always = no`.
- All 29 remaining RHI/BAY decision and mission blocks retain unique title and description localisation.

The HOI4 MCP inspection/lint tools were not exposed in this agent's tool surface, so no MCP comparison artifact was produced. Source-level caller, route, lifecycle, localisation, and structural checks completed without a remaining finding.

## Remaining blockers and risks

1. `IW-008` cannot receive runtime or SCN-008 attestation until the shared `FORM-04` X-ending identity transaction and complete flag triplet are independently implemented and audited.
2. `IW-009` has no formable blocker, but still requires an independent package content attestation before its runtime and scenario gates may open.
3. The generic exclusion is opt-out. Any future package whose accepted matrix forbids radical sovereignty must set, prove, and clean the exclusion before its readiness attestation is granted.

The Event 006 allocator is therefore still intentionally closed for these packages. This handoff claims completion only for the audit remediation, not package admission.

## References and skills used

- `chaos-redux-events`
- `hoi4-focus-trees`
- `hoi4-decisions-missions`
- `chaos-redux-subagents`
- Required offline Paradox wiki core pages, including national focus modding
- Vanilla decision, on-action, script-concept, trigger, effect, and AI-strategy documentation
- Vanilla ARG decision visibility and CZE AI-strategy enable/abort precedents

No skill was created or updated. The persistent exclusion is an Event 006 implementation detail; adding that identifier to a reusable skill would violate the rule against event-specific skill context.
