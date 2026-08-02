# IW-014 Catalonia implementation handoff — 2026-08-01

## Scope

Current focus-ownership decision (2026-08-02): the installed CAT carrier exposes only `generic_focus`, so the package uses the full Event 006 framework after proving that no meaningful existing tree needs preservation. This minimal-tree exception supersedes the earlier “additive” label for focus ownership; the package remains fail-closed for the separate FORM-07 identity, flag, member-adapter, and readiness gates.

The CAT carrier now has an additive Event 006 package. Vanilla CAT history, capital state 165, flag, and `CAT_lluis_companys` remain authoritative; no country, history, portrait, or advisor asset was created.

## Changed surfaces

- `common/script_constants/006_independence_wave_catalonia_constants.txt`
- `common/ideas/006_independence_wave_catalonia_ideas.txt`
- `common/scripted_triggers/006_independence_wave_catalonia_package_triggers.txt`
- `common/scripted_effects/006_independence_wave_catalonia_package_effects.txt`
- `common/decisions/006_independence_wave_catalonia_decisions.txt`
- `common/ai_strategy/006_independence_wave_catalonia.txt`
- `common/national_focus/006_independence_wave_focus.txt`
- `common/scripted_triggers/006_independence_wave_package_triggers.txt`
- `common/scripted_triggers/006_independence_wave_packages_region_02_triggers.txt`
- `common/scripted_effects/006_independence_wave_package_dispatch_effects.txt`
- `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt`
- `localisation/english/006_independence_wave_catalonia_l_english.yml`
- `docs/events/006_independence_wave/catalonia_package.md`

## Gameplay contract

IW-014 uses reservation group RG-165, state 165, industrial-breakaway archetype, p14 forces, navy-plus-air inheritance, five explicit reinforcement pathways, full framework/host/network/league registration, five researched route governments, a municipal-versus-industrial power struggle, two visible ledgers, a 420-day founding mission, eleven concrete-cost decisions, AI response layers, and cleanup adapters.

Runtime content attestation remains intentionally closed. The package selects the
Iberian Federation family for its formable lane, but FORM-07 has no reviewed
X-ending identity, territory, member, or integration adapter yet. The CAT
prepared-setup proof therefore requires the shared formable commit-readiness
gate, and the dispatcher leaves IW-014 outside the attested set until that
family is completed or an audited Mediterranean-league carrier route is chosen.

## Static validation to run

- `python -B .tools/audit_event6_allocator.py`
- `python -B .tools/audit_chaosx_country_tags.py --surface-scan`
- `rg -n "set_country_flag =" common/scripted_triggers/006_independence_wave_catalonia_package_triggers.txt` must return no matches.
- Verify the dormant dispatch adapter, exact preflight, scenario preflight, and exact CAT wrapper contain IW-014; verify the compile-time content attestation intentionally excludes it while FORM-07 remains incomplete.
- Verify the new localisation file begins with UTF-8 BOM and every decision/focus/idea/party key is present.
- Run the narrow Event 006 event lint and focus inspection after dispatch/focus loading.

## Remaining risk

Runtime QA still needs a fresh-map release/reload check for vanilla Companys recruitment, dynamic starting forces, host-target persistence, mission cancellation, and the five route government outcomes after admission. The package remains fail-closed if state 165, CAT, the vanilla character, or the FORM-07 readiness contract is unavailable.
