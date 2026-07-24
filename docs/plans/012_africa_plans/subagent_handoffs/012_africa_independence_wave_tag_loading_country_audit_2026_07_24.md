# Event 012 Independence Wave country-tag loading country-package audit

Date: 2026-07-24

Auditor: `/root/africa_tag_loading_audit`

Scope: commit `d8c05b7f1` (`Load Event 12 on Independence Wave Africa tags`) and the current working-tree source surfaces that the commit depends on.

This is a read-only country-package audit; no gameplay file, country history, map file, or asset-production file was changed by this audit.

## Executive status

The tag migration is structurally correct for the seven existing niche Event 006 tags and does not register a parallel Event 012 country or cosmetic identity layer.

Three high-severity acceptance gaps remain: active Event 006 provenance is not enforced by the current Event 012 origin predicates, Luba/Lunda/Kilwa remain explicitly unbound in the Event 006 allocator, and the nine vanilla-carrier institutional councils have runtime recruitment but no stable country-history ownership.

The first gap is a provenance-policy blocker rather than an authorization to add tags or territory, and the latter two require a parent design decision before implementation.

## Country-package coverage checklist

| Surface | Result | Evidence or remaining work |
|---|---|---|
| Existing niche tags | Pass for registration | `DOX`, `DSX`, `DUX`, `DYX`, `DZX`, `EMX`, and `EQX` remain in `common/country_tags/006_independence_wave_countries.txt` and point to the existing Event 006 country definitions. |
| Event 012 country/cosmetic tags | Pass | `rg` over `common/country_tags` and `common/countries` finds no Event 012 priority-member tag; `common/countries/012_africa_cosmetic.txt` contains only seven continental route cosmetics. |
| Exact original-tag predicates | Pass | `common/scripted_triggers/006_independence_wave_country_registry_triggers.txt:286-300` maps the seven niche carriers and the nine accepted vanilla carriers; Kongo additionally requires `COG_kingdom_of_kongo`. |
| Action 102 gate | Pass subject to provenance decision | `common/scripted_effects/012_africa_action_effects.txt:3169-3185` validates Action 102 and `:5901-5910` writes approval before `africa_priority_member_register_from_origin`; `africa_priority_member_can_register_package` remains the final package gate. |
| Event 006 active-origin eligibility | Open high | `common/scripted_triggers/012_africa_priority_member_triggers.txt:88-218` and `common/scripted_effects/012_africa_priority_member_effects.txt:21-120` exclude Soviet origins but no longer require `is_independence_wave_registry_event6_origin` for direct carriers. |
| Seven niche council ownership | Pass | Each dormant shell history recruits its matching institutional council at line 10 in `history/countries/DOX - Asante.txt`, `DSX - Oyo.txt`, `DUX - Kanem-Bornu.txt`, `DYX - Luba.txt`, `DZX - Lunda.txt`, `EMX - Kilwa Restoration.txt`, and `EQX - Zulu.txt`. |
| Nine vanilla council ownership | Open high | Vanilla histories for `SOK`, `MLI`, `COG`, `UGA`, `TIG`, `HAR`, `SUD`, `ZIM`, and `MAD` do not own the Event 012 councils; the current helper recruits them only at runtime. |
| DYX/DZX/EMX reachability | Open high | Event 006 scenario setup blocks `DYX`, `DZX`, and `EMX` as `IW-103`, `IW-104`, and `IW-117`; no region plan/allocator entry currently creates them. |
| Focus-tree handoff | Pass | `common/scripted_effects/012_africa_priority_member_effects.txt:244-278` loads `africa_priority_member_focus_tree` for the seven niche tags and only generic-tree vanilla carriers; meaningful vanilla trees are preserved. |
| Public country names | Pass | `localisation/english/006_independence_wave_countries_l_english.yml:615-834` supplies all seven names under every ideology; `EMX` is `Kilwa`/`Kilwan`, not `Kilwa Restoration`. |
| Territory, cores, subjects, factions, cosmetics | Pass | No Event 012 package effect contains `set_owner`, `set_controller`, `transfer_state`, `add_core`, `remove_core`, `release`, `annex`, `create_faction`, `add_to_faction`, `leave_faction`, `set_capital`, or `set_cosmetic_tag`. |
| Event 006 cleanup coexistence | Pass | Event 012 cleanup clears Event 012 runtime state only; Event 006 origin/lifecycle markers are retained. `common/scripted_effects/006_independence_wave_country_registry_effects.txt:4-7` explicitly forbids using the Event 006 registry lifecycle helper from Event 012. |
| Starting ideas and force overlay | Pass at overlay level | `common/ideas/012_africa_priority_member_ideas.txt` has package-specific lifecycle ideas, and `common/scripted_effects/012_africa_priority_member_force_effects.txt` defines bounded templates, manpower, equipment, and reserve initialization. |
| Technology and industry | Partial evidence | This migration does not edit country technology, production, or state setup; the Event 012 overlay uses existing compact viability and package force/idea effects. The installed package exposes no Technology Tree Viewer, so technology-tree reachability remains an unresolved validation limitation. |
| AI/playability | Pass with integration caveat | Per-package focus `ai_will_do` modifiers and decision AI weights are present in `common/national_focus/012_africa_priority_member_focus.txt` and `common/decisions/012_africa_priority_member_decisions.txt`; no separate tracked package AI strategy-plan file was added by this migration. |
| Portraits and flags | Handoff only | Council sprite IDs remain in `interface/012_africa_priority_member_characters.gfx`; final portrait and base/ideology flag production was intentionally outside this audit. |

## File-surface checklist

The reviewed registration surfaces are `common/country_tags/006_independence_wave_countries.txt`, `common/countries/006_independence_wave_DOX.txt`, `DSX.txt`, `DUX.txt`, `DYX.txt`, `DZX.txt`, `EMX.txt`, and `EQX.txt`, `common/countries/012_africa_cosmetic.txt`, and `localisation/english/006_independence_wave_countries_l_english.yml`.

The reviewed identity and registration surfaces are `common/scripted_triggers/006_independence_wave_country_registry_triggers.txt`, `common/scripted_triggers/012_africa_priority_member_triggers.txt`, `common/scripted_effects/012_africa_priority_member_effects.txt`, `common/scripted_effects/012_africa_priority_member_character_effects.txt`, and `common/scripted_effects/012_africa_action_effects.txt`.

The reviewed setup and allocator surfaces are `history/countries/DOX - Asante.txt`, `DSX - Oyo.txt`, `DUX - Kanem-Bornu.txt`, `DYX - Luba.txt`, `DZX - Lunda.txt`, `EMX - Kilwa Restoration.txt`, `EQX - Zulu.txt`, `common/scripted_effects/006_independence_wave_scenario_effects.txt`, `common/scripted_triggers/006_independence_wave_packages_region_09_triggers.txt`, and `common/scripted_triggers/006_independence_wave_packages_region_11_triggers.txt`.

The reviewed gameplay overlay surfaces are `common/national_focus/012_africa_priority_member_focus.txt`, `common/decisions/012_africa_priority_member_decisions.txt`, `common/ideas/012_africa_priority_member_ideas.txt`, `common/scripted_effects/012_africa_priority_member_force_effects.txt`, `common/characters/012_africa_priority_member_characters.txt`, and `interface/012_africa_priority_member_characters.gfx`.

The migration handoff under review is `docs/plans/012_africa_plans/012_africa_independence_wave_tag_loading_handoff.md`; the broader overlay contract is `docs/plans/012_africa_plans/012_africa_priority_member_packages_handoff.md`.

## Findings by severity

### High: active Event 006 provenance is not represented in the Event 012 origin gate

The direct carrier predicates in `common/scripted_triggers/012_africa_priority_member_triggers.txt:88-218` require only an exact `original_tag` or an Event 012 origin flag plus a Soviet-origin exclusion.

The matching flag-recording effect in `common/scripted_effects/012_africa_priority_member_effects.txt:21-120` has the same shape and no `NOT = { is_independence_wave_registry_event6_origin = yes }` guard or equivalent active-receipt check.

The final gate at `common/scripted_triggers/012_africa_priority_member_triggers.txt:375-389` likewise requires Event 012 active, host commitment, approval, and a valid origin, but not an active Event 006 origin receipt.

This permits a direct niche original tag to satisfy Event 012 identity without proving that the country was an active Event 006 origin, which conflicts with the handoff contract that says active Independence Wave origins are the eligible same-scope route.

The nine vanilla carriers may intentionally be eligible from their normal live country identity, so the parent must decide whether the active Event 006 condition applies only to the seven niche shells or to every overlap carrier.

Required parent decision: define the provenance rule, then add one narrow shared trigger or equivalent guard so the seven Event 006 shells cannot bypass their lifecycle receipt while the intended vanilla-carrier policy remains explicit.

### High: DYX, DZX, and EMX have no current Event 006 allocator path

`common/scripted_effects/006_independence_wave_scenario_effects.txt:1093-1104` places `DYX`, `DZX`, and `EMX` in the blocked country-entry list for `IW-103`, `IW-104`, and `IW-117`.

`common/scripted_triggers/006_independence_wave_packages_region_09_triggers.txt` contains plan/load entries for `DOX`, `DSX`, and `DUX` but not `DYX` or `DZX`, while `common/scripted_triggers/006_independence_wave_packages_region_11_triggers.txt` contains `EQX` and `MAD` but not `EMX`.

`common/scripted_triggers/006_independence_wave_country_registry_triggers.txt:271-281` intentionally omits `DYX`, `DZX`, and `EMX` from the current-map-bound carrier list.

The seven shells and their Event 012 focus predicates are present, but three of them cannot currently be produced by the Event 006 allocator. If active Event 006 provenance is enforced, these three packages remain unreachable until a bounded Event 006 creation route is designed.

Required parent decision: keep these rows dormant and hide or reject their Event 012 promotion path, or provide an accepted Event 006 route before enabling them; do not add fallback territory, a replacement tag, or a cosmetic substitute.

### High: nine vanilla-carrier councils lack country-history ownership

`common/characters/012_africa_priority_member_characters.txt` defines the institutional council characters, but vanilla histories for `SOK`, `MLI`, `COG`, `UGA`, `TIG`, `HAR`, `SUD`, `ZIM`, and `MAD` do not recruit the matching Event 012 council in their normal history setup.

`common/scripted_effects/012_africa_priority_member_character_effects.txt:10-123` recruits all sixteen councils during package registration, including the nine vanilla branches.

This meets a runtime recruitment need but not the stronger ownership requirement used for the seven dormant Event 006 shells, and directly overriding vanilla country history would replace unrelated vanilla setup.

The existing handoff records this as unresolved at `docs/plans/012_africa_plans/012_africa_independence_wave_tag_loading_handoff.md:73-79`.

Required parent decision: choose a safe ownership mechanism for the nine vanilla carriers, or explicitly accept runtime-only ownership with an updated contract and acceptance test; no generated ruler, new tag, cosmetic substitute, or unrelated history replacement is safe by implication.

### Medium: direct-carrier survey policy should be documented per carrier class

`common/scripted_triggers/012_africa_priority_member_triggers.txt:291-299` allows a survey target when it exists, has a supported identity, has a viable compact base, is not the host, has no active package, has no pending requalification, and has no active action record.

The exact identity classifier is correct, but the survey does not distinguish a dormant Event 006 shell from an already playable vanilla carrier before the provenance decision above is made.

The parent should add the resulting class distinction to the handoff and acceptance ledger so a dormant shell cannot appear as an actionable roster target merely because its original tag predicate matches.

### Low: one unused or stale Event 006 Africa-origin classifier remains

`common/scripted_triggers/006_independence_wave_country_registry_triggers.txt:21-26` defines `is_independence_wave_registry_africa_origin` with a non-Event-006 and non-Soviet condition, while the Event 012 package predicates now use direct carrier predicates and flags instead.

No direct Event 012 call site was found for this classifier during the audit, so it is not a discovered runtime blocker, but it should be either documented as legacy or removed in a separate cleanup pass.

## Map and state setup

The seven niche histories are intentionally dormant and contain only their matching `recruit_character` line; their comments state that Event 006 supplies territory, capital, politics, forces, ideas, focus loading, and AI at runtime.

The Event 012 registration code contains no owner, controller, state transfer, core, capital, release, annexation, subject, faction, or cosmetic-tag mutation.

Compact viability is checked in `common/scripted_triggers/012_africa_priority_member_triggers.txt:244-252` by requiring an African capital owned and controlled by the candidate and no capitulation.

The migration therefore preserves the no-fallback-territory contract, but the blocked DYX/DZX/EMX allocator rows mean their viable compact bases cannot currently be reached through the documented Event 006 route.

## Politics, leaders, portraits, flags, advisors, and parties

The seven niche shell histories provide stable ownership for `africa_priority_<key>_institutional_council` characters before runtime registration.

`common/scripted_effects/012_africa_priority_member_character_effects.txt:125` and later settlement logic keep councils without a political role until the country explicitly ratifies a political settlement, at which point one matching leader role and party route is installed.

The council names are institutional names, not personal random-name pools, which is correct for committee or council bodies.

No new Event 012 country leader, advisor, party identity, or cosmetic-tag definition was found in the tag-loading commit.

Final council portrait production under `gfx/leaders/012_africa/priority_members/` and the base/ideology flag completeness of the seven existing Event 006 tags were intentionally excluded from this audit and remain parent-owned asset checks.

## Focus, decision, idea, and asset surfaces

`common/scripted_effects/012_africa_priority_member_effects.txt:244-278` correctly loads `africa_priority_member_focus_tree` for the seven niche tags and for vanilla carriers only when they still use `generic_focus`.

The same loader preserves a meaningful existing vanilla tree and marks `africa_priority_member_focus_tree_overlay_skipped`; Event 012 decisions, ideas, forces, League behavior, and AI remain additive for that carrier.

Action 102 validation and full-result wiring are present in `common/scripted_effects/012_africa_action_effects.txt:3169-3185` and `:5901-5910`, and delayed ratification uses the same registration API in `common/decisions/012_africa_priority_member_decisions.txt`.

The package-specific idea, decision, focus, force, and council identifiers are present for all sixteen package keys, including `kilwa`, `luba`, and `lunda`.

The migration did not create or rename focus, decision, idea, or sprite identifiers, so the asset-production directories and generated portrait files were not modified.

## Starting military, technology, industry, supply, and production

Package registration invokes `africa_priority_member_initialize_starting_force` and the package lifecycle idea in `common/scripted_effects/012_africa_priority_member_effects.txt:565-568`.

The force helper defines five bounded profile families and scales equipment, manpower, and experience from centralized Event 012 constants in `common/scripted_effects/012_africa_priority_member_force_effects.txt`.

No Event 012 country-history technology, research slot, production-line, train, convoy, fuel, building, or state-resource mutation was introduced by the tag-loading commit.

The installed package exposes no Technology Tree Viewer, so direct technology-tree dependency and unlock validation remain unresolved for this audit and should not be treated as proven by the country-tag migration.

## AI and playability

The eight-focus Event 012 tree has package-specific `ai_will_do` modifiers in `common/national_focus/012_africa_priority_member_focus.txt`, and national force, mechanic, settlement, and post-settlement decisions have package-specific AI weights in `common/decisions/012_africa_priority_member_decisions.txt`.

The current migration does not add a separate country-specific AI strategy plan for the seven niche tags, and `common/ai_strategy_plans/012_africa_focus_plans.txt` is outside commit `d8c05b7f1`; this is a parent integration caveat rather than a confirmed loader defect.

A playable acceptance pass must still exercise each niche tag after Event 006 creation, because DYX/DZX/EMX currently have no allocator path and the active-origin policy is unresolved.

## Explicit acceptance scenarios

1. At game start, `DOX`, `DSX`, `DUX`, `DYX`, `DZX`, `EMX`, and `EQX` are absent dormant shells, no Event 012 priority-member country or cosmetic tag exists, and no priority package decision appears for an absent shell.

2. When Event 006 creates an active `DOX`, `DSX`, `DUX`, or `EQX` country, Action 102 is the only full-promotion route; successful registration keeps the same original tag, retains Event 006 lifecycle receipts, and adds no state, core, owner, subject, faction, or cosmetic change.

3. A country with Soviet-collapse provenance cannot pass any supported-carrier origin predicate or Action 102 package registration even if its original tag overlaps a listed carrier.

4. A vanilla carrier with a meaningful tree, such as `COG` or `UGA`, retains that tree while receiving Event 012 decisions, ideas, forces, League behavior, and AI additively; a vanilla carrier still using `generic_focus` receives `africa_priority_member_focus_tree`.

5. Each of the seven niche shell histories owns exactly its matching institutional council before runtime, the council has no political role until ratification, and no personal leader-name pool is used for the institutional body.

6. The nine vanilla carriers (`SOK`, `MLI`, `COG`, `UGA`, `TIG`, `HAR`, `SUD`, `ZIM`, and `MAD`) must either receive an approved stable ownership mechanism or be explicitly accepted as runtime-only council ownership with the contract and acceptance ledger updated.

7. `DYX`, `DZX`, and `EMX` must remain blocked and non-actionable while their Event 006 rows are unbound, or a bounded Event 006 creation route must be implemented and then re-audited before Event 012 promotion is exposed.

8. `EMX` must display `Kilwa` and `Kilwan` under every ideology and never `Kilwa Restoration` in player-facing country-name localisation.

9. A completed Event 012 package must not call Event 006 registry lifecycle cleanup, clear Event 006 origin proof, grant a core, transfer a state, create a faction, alter a subject relationship, or apply a replacement cosmetic tag.

## Validation performed

The audit used repository `rg` scans for tag, cosmetic, origin, map-mutation, focus-loader, council-recruitment, and allocator references, direct inspection of the touched files and handoffs, and comparison with the installed vanilla country histories for the nine carriers.

The required offline Paradox wiki pages and relevant vanilla documentation were read before inspection, including country creation, national focus, character, effects, triggers, decision, and event references.

No HOI4 MCP write was used because the local source surfaces answered the tag-loading questions; the installed package has no Technology Tree Viewer, which is recorded above as an unresolved limitation.

## Simplifications, omissions, and blockers

No gameplay fallback, replacement tag, fallback territory, new cosmetic identity, generated ruler, or unrelated vanilla-history override was added.

The audit does not claim whole-country-package completion because active Event 006 provenance, DYX/DZX/EMX reachability, and nine vanilla council ownership remain unresolved, and final portrait/flag production was outside scope.

Recommended follow-up is a parent-owned design handoff for the three high-severity findings before any gameplay patch is attempted.
