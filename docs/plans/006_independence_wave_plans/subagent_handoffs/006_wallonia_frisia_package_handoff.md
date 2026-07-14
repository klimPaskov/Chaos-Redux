# IW-006 Wallonia and IW-007 Frisia Package Handoff

## Ownership and completion boundary

This handoff covers only the isolated playable package implementation for AFX IW-006 and AGX IW-007. It does not edit the shared Event 006 executor, shared origin lifecycle, package allocator, Event 5, the shared focus framework, or any other package. After the independent audit passed, the parent integration review granted `independence_wave_package_content_ready` in both dormant country histories.

## Shared integration contract

### Four-pass transaction dispatch

The shared executor and compatibility wrapper own the four transaction passes. `common/scripted_effects/006_independence_wave_package_dispatch_effects.txt` now registers these regional adapters in the matching generic dispatchers; do not insert a direct Wallonia/Frisia call after an origin initializer:

```txt
independence_wave_dispatch_package_setup = {
	independence_wave_dispatch_wallonia_frisia_package_setup = yes
	# Other regional setup adapters.
}

independence_wave_dispatch_package_final_validation = {
	independence_wave_dispatch_wallonia_frisia_package_final_validation = yes
	# Other regional final-validation adapters.
}

independence_wave_dispatch_package_cleanup = {
	independence_wave_dispatch_wallonia_frisia_package_cleanup = yes
	# Other regional cleanup adapters.
}
```

The transaction contract is:

1. `independence_wave_prepare_country_origin` writes reversible country-local state. The generic setup dispatcher resets `independence_wave_package_setup_success` once before its regional adapter chain. This regional setup adapter installs the package, then `has_prepared_independence_wave_iw_006_package_setup` or `has_prepared_independence_wave_iw_007_package_setup` must pass before the adapter sets the generic and package-specific setup flags and selects setup success.
2. `independence_wave_activate_prepared_country_origin` publishes the reversible active-country, network-member, and former-host registries. No package-specific hook is required in this pass.
3. The generic final-validation dispatcher resets `independence_wave_package_final_validation_success` once before its regional adapter chain. This regional adapter requires the corresponding `has_complete_independence_wave_iw_006_package_setup` or `has_complete_independence_wave_iw_007_package_setup`, including activation readiness and exact live registry membership, before selecting final-validation success.
4. `independence_wave_commit_prepared_country_origin` appends durable generation history, released-package history, and evolution records. The shared caller may increment the initialized count and clear pending metadata only after that commit succeeds.

Do not reset either temporary result inside an individual regional adapter. The shared caller must reset each result once before its complete dispatcher chain so a later regional adapter cannot erase an earlier successful match.

On failure in any pass, `independence_wave_reset_current_generation` calls the generic cleanup dispatcher before clearing `independence_wave_package_id`. The successful `independence_wave_end_active_origin` path also calls it immediately after recording the end reason and date, before shared decision, registry, idea, and active-state cleanup. Both paths therefore preserve the package identity required by the regional cleanup adapter.

### Readiness gate

Do not grant `independence_wave_package_content_ready` from gameplay setup. The parallel asset handoff confirmed the final portrait DDS files and all AFX and AGX flag sizes, and the six character sprites are registered in `interface/006_independence_wave_region_01_portraits.gfx`. The independent package audit then passed without an unresolved finding, and the parent granted the audited history flag to these two exact dormant tags.

## Files changed

- `common/script_constants/006_independence_wave_wallonia_frisia_constants.txt`
- `common/characters/006_independence_wave_wallonia_frisia_characters.txt`
- `history/countries/AFX - Event 006 Country Shell.txt`
- `history/countries/AGX - Event 006 Country Shell.txt`
- `common/ideas/006_independence_wave_wallonia_frisia_ideas.txt`
- `common/scripted_triggers/006_independence_wave_wallonia_frisia_package_triggers.txt`
- `common/scripted_effects/006_independence_wave_wallonia_frisia_package_effects.txt`
- `common/decisions/categories/006_independence_wave_wallonia_frisia_categories.txt`
- `common/decisions/006_independence_wave_wallonia_frisia_decisions.txt`
- `common/ai_strategy/006_independence_wave_wallonia_frisia.txt`
- `localisation/english/006_independence_wave_wallonia_frisia_l_english.yml`
- `docs/006_independence_wave_wallonia_frisia_packages.md`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_wallonia_frisia_package_handoff.md`

## Important identifiers

Setup, live validation, and cleanup:

- `independence_wave_dispatch_wallonia_frisia_package_setup`
- `independence_wave_dispatch_wallonia_frisia_package_final_validation`
- `independence_wave_dispatch_wallonia_frisia_package_cleanup`
- `independence_wave_setup_iw_006_wallonia`
- `independence_wave_setup_iw_007_frisia`
- `independence_wave_validate_iw_006_wallonia`
- `independence_wave_validate_iw_007_frisia`
- `has_prepared_independence_wave_iw_006_package_setup`
- `has_prepared_independence_wave_iw_007_package_setup`
- `has_complete_independence_wave_iw_006_package_setup`
- `has_complete_independence_wave_iw_007_package_setup`

Characters:

- `AFX_walloon_provisional_assembly`
- `AFX_walloon_reserve_commander`
- `AGX_friesland_coastal_council`
- `AGX_friesland_coastal_commander`

Package mechanics:

- `independence_wave_afx_industrial_continuity`
- `independence_wave_agx_waterline_integrity`
- `independence_wave_agx_coastal_security`
- `independence_wave_low_countries_federation_candidate`
- `independence_wave_meuse_industrial_ambition`
- `independence_wave_north_sea_coastal_link`

## Package contract summary

AFX publishes constitutional, popular-council, emergency-military, and patron-client routes. It publishes negotiation, guarded-frontier, association, and reclamation host routes. Its power struggle is civilians against the army. Its opening force is the shared researched IW-006 industrial-security mapping.

AGX publishes constitutional, popular-council, and patron-client routes only. It publishes negotiation, guarded-frontier, and association host routes, with no reclamation. Its power struggle is labor councils against ministries. Its opening force is the shared researched IW-007 coastal-maritime mapping.

Both use the full shared focus framework, the independence network and league route, and `independence_wave_formable_family.low_countries_federation`.

## Validation evidence and remaining risks

- Prepared package proofs cover tag, ID, persistent anchor and former-host pointers, roster, full focus assignment, accepted and rejected routes, power struggle, league, formable, current-generation force application, package idea, and AI flag. Live completion proofs add activation readiness, aligned shared arrays, exact active-country membership, exact network-member membership, and the network-member flag before durable commit.
- The dormant tag histories provide and the setup validators prove vanilla baseline civilian-economy, export-focus, and volunteer-only laws before package mutation or force materialization.
- Decision mechanics use shared material cost predicates and pay effects. Capital loss, negotiation war, or origin termination can cancel work and produce documented setbacks. Government formalization is part of the same serialized project lane, requires capital control, and remains retryable after an occupation cancellation.
- Package missions, projects, route formalizations, and conferences deliberately do not use engine-persistent `fire_only_once`. Their package predicates, active-decision serialization, and generation-local outcome flags enforce one completion per live generation. Regional cleanup first removes every package mission or decision without firing its completion, timeout, removal, or cancellation result, then clears the generation-local outcome flags. An accepted Annexation and Return recreation therefore receives fresh timers, costs, and the complete decision layer even when reset and preparation happen in one effect chain.
- The one-factory emergency-administration predicate keeps both anchor-state openings viable while reusing the shared light-administration payment. Wallonia has a 150-day pump-and-rail baseline funded by two sequential one-factory commitments, so division reinforcement cannot consume its decision reserve. Frisia has a 270-day pump-harbor-rail baseline funded by one factory commitment and two sequential light convoy commitments. Neither crisis depends on starting Army Experience or former-host survival. Every published route government is also payable from the guaranteed post-crisis reserve: six formalizations use that one-factory light package, while Frisia's patron formalization uses the sixth convoy left after the two baseline logistics payments.
- Localisation coverage includes every package character, party, idea, category, decision, description, variable label, and custom effect tooltip.
- AI profiles are self-removing and enable only after exact package setup. Former-host threat behavior uses the dynamic shared ledger rather than static BEL or HOL targets. Frisia's AI cannot spend its standard-convoy host-settlement cost until its two waterline thresholds are stable, preserving the 270-day baseline logistics reserve.
- The character files reference the stable portrait sprite inventory supplied by the parallel asset tranche, including the two officer small portraits. All runtime files are present, passed the asset tranche's visual and format review, and are registered in the parent-owned Event 006 regional portrait `.gfx` file.
- The generic setup, final-validation, and cleanup dispatchers register the regional adapters, and shared reset and successful origin-end paths call cleanup before package provenance is lost. The four-pass shared transaction defers durable history until after exact live validation, so no package-specific durable-history rollback is required.
- The independent package audit passed every exact route, balance, cleanup, localisation, force, flag, portrait, and transaction check. The parent therefore granted the persistent content-ready history flag to AFX and AGX; no other registry row was activated by this handoff.

No fallback or gameplay simplification was used. The deliberate use of shared Event 006 focus, force, decision-cost, and icon frameworks follows the accepted architecture rather than substituting generic content.
