# Event 006 IW-043 and IW-058 signature country core

This document records the bounded country-core implementation for the `IW-043` Middle Volga and `IW-058` Assyria packages. It covers institutional characters, leader traits, staged ideas, AI strategy, party identity, and country identity, plus the focus-framework integration contract added by the package setup adapter. Decisions, incidents, formable transactions, and achievements remain owned by their dedicated Event 006 surfaces; the base package assets/GFX are resolved and IW-043/IW-058 are admitted by the shared origin-safe runtime registry.

The controlling design is `docs/plans/006_independence_wave_plans/006_iw043_iw058_signature_packages_improvement_addendum_2026_07_18.md`. Portrait and identity safeguards come from `docs/assets/006_independence_wave/iw043_iw058_source_research_2026_07_18/`. None of the optional or excluded real-person candidates is used.

## Scripted architecture contract

The package-level reusable logic lives in `common/scripted_triggers/006_independence_wave_iw043_iw058_package_triggers.txt` and `common/scripted_effects/006_independence_wave_iw043_iw058_package_effects.txt`. The shared tuning source is `common/script_constants/006_independence_wave_iw043_iw058_constants.txt`; no package helper introduces a file-scoped magic duration, strength floor, organization floor, or conversion value.

## Focus-framework integration

Both setup transactions assign `independence_wave_focus_assignment.full_framework` only after the exact package identity, opening cosmetic, institutional surface, and force receipts exist. Setup then publishes the common route, host-policy, internal-power, ambition, league, formable, and signature-module registrations and marks the layout dirty before writing the package setup-complete flag. Final validation repeats the full-framework assignment and registration receipts. FORM-12, FORM-13, and FORM-18 remain fail-closed because their adapter attestation flags are still unwritten.

| Package | Full-framework assignment | Common route/power profile | Formable profile at setup | Disconnected focus imports |
|---|---|---|---|---|
| IW-043 Middle Volga (`CHU`) | `independence_wave_iw043_*` gated nodes | constitutional, popular council, traditional, emergency military, patron client; `traditional_authority_vs_assembly`; all four former-host lanes; league and signature | `volga_ural_federation` (switches to `idel_ural` on the restoration consent focus) | `repair_cheboksary_workshops`, `trade_beyond_the_middle_volga`, `return_guard_to_civilian_law` |
| IW-058 Assyria (`ASY`) | `independence_wave_iw058_*` gated nodes | constitutional, popular council, traditional, emergency military, patron client; `traditional_authority_vs_assembly`; all four former-host lanes; league and signature | `mesopotamian_federation` | `restore_civilian_command` |

The main tree imports three capstone roots—the IW-043 federal and restoration terminals and the IW-058 settlement terminal—plus those four disconnected branch roots because a vanilla `shared_focus` import brings prerequisite ancestors but not descendant siblings. Cleanup returns the reviewed `CHU`/`ASY` carriers to `generic_focus` after clearing shared focus runtime, formable profile state, route exclusions, and package identity. The implementation and deterministic source-graph audit are recorded in `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw043_iw058_focus_audit_handoff_2026_07_18.md`.

### Relationship-aware partner reach

The public target-scope entry points are `is_independence_wave_iw043_reachable_partner` and `is_independence_wave_iw058_reachable_partner`. They are called in a candidate country's scope with the active package country as `ROOT`, reject self, war, and subject targets, and inspect only the current bilateral target. They do not perform a world iteration.

Each wrapper exposes five package-specific tier predicates: `is_independence_wave_iw0xx_major_reach`, `is_independence_wave_iw0xx_treaty_reach`, `is_independence_wave_iw0xx_league_reach`, `is_independence_wave_iw0xx_patron_reach`, and `is_independence_wave_iw0xx_diaspora_reach`. Every tier also rechecks the matching package identity on `ROOT`. Major reach uses the target's major status; treaty reach uses a non-aggression pact or a guarantee in either direction; league reach uses an active Event 006 country with league/network membership; patron reach delegates the existing validated patron-target contract; and diaspora reach uses an active same-region network member. The `iw0xx` placeholder means `iw043` or `iw058`.

### Exact force binding and conversion

`has_independence_wave_iw043_supplied_division_candidate` and its IW-058 counterpart prove the current generation's package receipt and the minimum strength/organization floors on an owned, non-reserve division. `independence_wave_bind_iw043_force_package` / `independence_wave_bind_iw058_force_package` save exactly one selected division as a global event target and record the country generation. The paired `can_bind_*` and `has_valid_*_force_binding` triggers prevent overlapping package bindings and reject stale generations.

The discipline effects mutate the selected division in place through the vanilla block form of `change_division_template`. The final player-facing template names are `Middle Volga River Guard` (IW-043) and `Assyrian Levies Detachment` (IW-058). The effects set the division-scoped `independence_wave_iw043_designated_formation_generation` / `independence_wave_iw058_designated_formation_generation` receipt and a matching country generation plus designation flag. The durable post-conversion proof is `has_independence_wave_iw043_designated_formation` or `has_independence_wave_iw058_designated_formation`; the `has_valid_*_designated_formation_binding` variants additionally require the live target and its division receipt.

Binding targets are short-lived global pointers. Bind preflight, `independence_wave_release_iw043_force_package`, and its IW-058 counterpart clear only the pointer, bound-generation variable, and active-binding flag. The division-scoped designation receipt survives ordinary release and is removed only by exact package cleanup, which also clears the durable designation, template-ready flag, generation variable, and all package force receipts. Cleanup never deletes the template from a country that may still field a converted division.

### IW-058 guardianship identity restoration

`independence_wave_restore_iw058_civilian_surface` now also calls `independence_wave_restore_iw058_preserved_civilian_cosmetic_identity`. After emergency guardianship, the helper restores the church, civic, or opening national-council cosmetic identity in that order of preserved route/applied receipts, removes the guardianship applied receipt, and leaves route and institutional effects to their owning callers. It does not select advisor portraits or alter route flags.

### Formable compatibility status

FORM-12, FORM-13, and FORM-18 remain fail-closed. Their readiness triggers require `independence_wave_form12_adapter_attested`, `independence_wave_form13_adapter_attested`, or `independence_wave_form18_adapter_attested` respectively. The keyed identity/integration adapters only set their own receipt flags when the corresponding readiness alias is true, while the achievement-writer hooks intentionally write no attestation. No owned call site sets any of the three adapter-attestation flags, so the compatibility adapters are not operational in this tranche. The IW-058 integration adapter's result constant is corrected to the declared `independence_wave_iw_formable_adapter` category, but this does not open the gate.

The migration path is intentionally narrow: callers that currently inspect pre-conversion composition should use the designated-formation receipts after discipline; callers that need the exact live formation during a timed mission should use the designated binding trigger; all old duplicated target selection remains in the package-owned bind effect until the owning decision lane migrates to these APIs.

## Institutional characters and route roles

`common/characters/006_independence_wave_iw043_iw058_characters.txt` defines four all-male institutional characters for each package. They have only a stable large civilian portrait consumer and no country-leader, advisor, officer, commander role, or recruitment at load. Standalone CHU and ASY history roster files are forbidden because they would override the vanilla carrier histories. The exact package setup effect recruits the selected institutional record immediately before it attaches the country-leader role.

| Package state | Character | Dynamic ideology | Trait | Party name key |
|---|---|---|---|---|
| IW-043 opening | `CHU_independence_wave_middle_volga_congress` | `centrism` | `iw043_middle_volga_congress_trait` | `CHU_independence_wave_middle_volga_congress_party` |
| IW-043 federal | `CHU_independence_wave_federal_presidium` | `centrism` | `iw043_federal_presidium_trait` | `CHU_independence_wave_federal_presidium_party` |
| IW-043 restoration | `CHU_independence_wave_bolgar_civic_presidium` | `conservatism` | `iw043_bolgar_civic_presidium_trait` | `CHU_independence_wave_bolgar_civic_presidium_party` |
| IW-043 emergency | `CHU_independence_wave_river_security_directorate` | `despotism` | `iw043_river_security_directorate_trait` | `CHU_independence_wave_river_security_directorate_party` |
| IW-058 opening | `ASY_independence_wave_provisional_national_council` | `centrism` | `iw058_provisional_national_council_trait` | `ASY_independence_wave_provisional_national_council_party` |
| IW-058 church-civic | `ASY_independence_wave_concordat_council` | `conservatism` | `iw058_concordat_council_trait` | `ASY_independence_wave_concordat_council_party` |
| IW-058 civic assembly | `ASY_independence_wave_civic_national_assembly` | `centrism` | `iw058_civic_national_assembly_trait` | `ASY_independence_wave_civic_national_assembly_party` |
| IW-058 emergency | `ASY_independence_wave_levies_guardianship` | `despotism` | `iw058_levies_guardianship_trait` | `ASY_independence_wave_levies_guardianship_party` |

The setup and route adapter must first call `recruit_character`, then call `add_country_leader_role` on the matching character, set `promote_leader = yes`, supply the ideology and trait from this table, and use the character's `_desc` localisation key. It must do so only after `is_independence_wave_iw043_country` or `is_independence_wave_iw058_country` succeeds. A carrier's vanilla leader is never selected or removed through `original_tag` alone.

The emergency traits improve compact defense while imposing a civil-authority cost. Civilian traits support administration, stability, supply, infrastructure, or constitutional resilience. Every numeric value comes from the package categories in `common/script_constants/006_independence_wave_iw043_iw058_constants.txt`.

## Three-slot idea lifecycles

`common/ideas/006_independence_wave_iw043_iw058_ideas.txt` defines the complete national-spirit vocabulary. Every idea has the exact package trigger in `allowed`. Setup and route effects must use `swap_ideas` within the same slot and remove all package ideas during cleanup.

### IW-043

| Slot | Opening | Civilian or emergency replacement |
|---|---|---|
| Institution | `independence_wave_iw043_congress_in_session_idea` | `independence_wave_iw043_federal_charter_idea`, `independence_wave_iw043_bolgar_constitution_idea`, or `independence_wave_iw043_emergency_navigation_council_idea` |
| Economy | `independence_wave_iw043_disrupted_river_economy_idea` | `independence_wave_iw043_reopened_river_economy_idea` |
| Defense | `independence_wave_iw043_provisional_river_guard_idea` | `independence_wave_iw043_civilian_river_guard_idea` or `independence_wave_iw043_emergency_river_guard_idea` |

The federal and Bolgar spirits reward constitutional settlement in different ways. The emergency institution and guard improve immediate defense but carry political, stability, or consumer burdens. Returning the guard to civilian law must replace the emergency defense spirit rather than add another permanent spirit.

### IW-058

| Slot | Opening | Civilian, emergency, or settlement replacement |
|---|---|---|
| Institution | `independence_wave_iw058_provisional_council_idea` | `independence_wave_iw058_concordat_charter_idea`, `independence_wave_iw058_civic_charter_idea`, or temporary `independence_wave_iw058_levies_guardianship_idea`; later replaced by `independence_wave_iw058_mesopotamian_federal_settlement_idea` or `independence_wave_iw058_sovereign_autonomy_compact_idea` |
| Security | `independence_wave_iw058_exposed_mosul_corridor_idea` | `independence_wave_iw058_secured_mosul_corridor_idea` |
| External capacity | `independence_wave_iw058_fragile_diaspora_links_idea` | `independence_wave_iw058_diaspora_liaison_idea` |

The Concordat text keeps church jurisdictions distinct and never promotes one church identity into a general Assyrian symbol. The civic route protects religious institutions without placing them over public administration. The federal and sovereign-autonomy spirits both occupy the institutional slot and therefore cannot create a fourth persistent spirit.

## AI behavior

`common/ai_strategy/006_independence_wave_iw043_iw058_ai_strategy.txt` contains origin-bounded profiles. Static `allowed` blocks restrict loading to registered CHU or ASY carriers. Every continuous `enable` block then requires the exact package trigger and setup receipt. Route profiles require the exact route flag, crisis profiles require the tracked severe-crisis trigger, and recovery profiles activate when the package reserve is unsafe.

The AI behavior has four layers:

1. A modest founding profile gives infantry, support, transport, infrastructure, and compact-army priorities.
2. Reserve recovery adds strong war restraint and rebuilds the package's equipment base whenever the safe-action-reserve trigger fails.
3. Tracked crises and emergency governments prioritize anchor bunkers, infantry, support equipment, and defensive forces without selecting offensive targets.
4. Civilian routes, normalization, and settlement profiles restore strong war restraint and direct production toward infrastructure, industry, trains, or convoys appropriate to the package.

Route choice odds, community guarantees, action costs, guarantor selection, command-power ceilings, and formable consent remain in the package decision `ai_will_do` blocks. This strategy file does not scan countries, manufacture a target, authorize subject status, or bypass a settlement vote. It also does not continue emergency behavior after the crisis and normalization triggers change state because every profile uses `abort_when_not_enabled = yes`.

## Country and party identity

`localisation/english/006_independence_wave_iw043_iw058_country_core_l_english.yml` supplies character names and biographies, trait and idea text, route-party names, AI profile labels, and the accepted cosmetic names and adjectives.

The opening Middle Volga identity is a congress in Kazan. Volga Bulgaria is a modern constitutional outcome rather than the starting government, and the federal route uses equal civic and national chambers. The Assyrian package keeps a public Assyrian state identity while its text separately names Assyrian, Chaldean, Syriac, and Aramean self-identification. The Concordat, civic assembly, and guardianship labels describe institutions rather than interchangeable communities.

The cosmetic localisation consumers are:

- `CHU_independence_wave_middle_volga_congressX`
- `CHU_independence_wave_volga_bulgariaX`
- `CHU_independence_wave_volga_federationX`
- `VOLGA_URAL_FEDERATIONX`
- `IDEL_URAL_COMPACTX`
- `ASY_independence_wave_national_councilX`
- `ASY_independence_wave_church_compactX`
- `ASY_independence_wave_civic_federationX`
- `ASY_independence_wave_security_guardianshipX`
- `MESOPOTAMIAN_FEDERATIONX`

## Asset consumers and wiring handoff

The stable portrait, focus, and national-spirit sprite registrations resolve to reviewed final textures in the IW-043/IW-058 asset package, and the base runtime content attestation is registered for both package IDs. Optional FORM-12/13/18 adapter flags and achievement-writer flags remain unset. No advisor sprite or advisor texture is registered.

The eight large institutional portraits are registered in `interface/006_independence_wave_iw043_iw058_portraits.gfx` and resolve under `gfx/leaders/006_independence_wave/` with these sprite IDs:

- `GFX_portrait_CHU_independence_wave_middle_volga_congress`
- `GFX_portrait_CHU_independence_wave_federal_presidium`
- `GFX_portrait_CHU_independence_wave_bolgar_civic_presidium`
- `GFX_portrait_CHU_independence_wave_river_security_directorate`
- `GFX_portrait_ASY_independence_wave_provisional_national_council`
- `GFX_portrait_ASY_independence_wave_concordat_council`
- `GFX_portrait_ASY_independence_wave_civic_national_assembly`
- `GFX_portrait_ASY_independence_wave_levies_guardianship`

Each must be a separately authored all-male institutional group portrait. No advisor, officer, small portrait, real-person substitute, or BAY/RHI asset is accepted.

The six shared stage-icon families are registered in `interface/006_independence_wave_iw043_iw058_idea_icons.gfx` under `gfx/interface/ideas/006_independence_wave/volga_assyria/`:

- `GFX_idea_independence_wave_iw043_congress`
- `GFX_idea_independence_wave_iw043_river_economy`
- `GFX_idea_independence_wave_iw043_river_guard`
- `GFX_idea_independence_wave_iw058_council`
- `GFX_idea_independence_wave_iw058_corridor`
- `GFX_idea_independence_wave_iw058_diaspora`

The twenty focus icon families are registered with matching `_shine` sprites in `interface/006_independence_wave_iw043_iw058_focus_icons.gfx`. Their final DDS files live under `gfx/interface/goals/006_independence_wave/volga_assyria/`; the exact crosswalk is authoritative in that GFX file and must be mirrored by the final asset manifest.

## Future plans

- Complete exact keyed compatibility audits before enabling the FORM-12, FORM-13, and FORM-18 adapter-attestation flags.
- Keep achievement-writer attestation hooks inert until the corresponding completion contracts are authored and audited.
- Recheck combined idea, trait, force, decision-cost, and AI pressure after live scenario balance review. Emergency routes should remain strong enough to survive a tracked crisis without becoming the best permanent civilian government.
