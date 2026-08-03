# Event 016 KRG post-commit country and project-force audit

Date: 2026-08-03

Status: audit complete; no safe narrow gameplay patch was found. The current committed country and project-force surfaces are statically covered, while the remaining concrete gap requires a broader biological-system tranche.

## Scope and source contract

This post-commit pass checked the current KRG country package and project-force consumers after the recent Event 016 commits, including the takeover cosmetic identity repair and the latest decision cost-gate commit. The audit remained read-only for gameplay and model files.

The binding sources were `docs/specs/016_brilliant_scientist_specs/specs/016_brilliant_scientist_spec_part_5_kruger_state_country_package.md`, `docs/specs/016_brilliant_scientist_specs/matrices/016_country_package_matrix.md`, the project-force section of `016_brilliant_scientist_spec_part_3_project_portfolio.md`, and the current Event 016 source files.

## Country-package coverage checklist

| Surface | Evidence | Result |
| --- | --- | --- |
| Tag, definition, dormant history, and OOB | `common/country_tags/016_brilliant_scientist_country.txt`; `common/countries/Kruger State KRG.txt`; `history/countries/KRG - Kruger State.txt`; `history/units/016_brilliant_scientist_dormant.txt` | Covered. KRG remains a dormant fixed tag until a guarded formation or takeover transaction. |
| Capital, state ownership, cores, claims, and route map | `common/scripted_effects/016_brilliant_scientist_country_effects.txt`; `common/scripted_effects/016_brilliant_scientist_territory_effects.txt`; `common/scripted_triggers/016_brilliant_scientist_territory_triggers.txt` | Covered in source. Capital viability, ownership/control, facility, logistics, and former-host survival are rechecked before mutation. Live map and save validation remain parent-owned. |
| Leader, offices, parties, politics, and cosmetics | `common/characters/016_brilliant_scientist_characters.txt`; `common/country_leader/016_brilliant_scientist_traits.txt`; `common/scripted_effects/016_brilliant_scientist_country_effects.txt`; `common/countries/016_brilliant_scientist_cosmetics.txt`; `localisation/english/016_brilliant_scientist_country_l_english.yml` | Covered for fixed Kruger, four institutional command offices, base KRG formation, takeover identity, and six route identities. |
| Focus, decisions, and ideas | `common/national_focus/016_brilliant_scientist_kruger_state_focus.txt`; `common/decisions/016_brilliant_scientist_kruger_state_*.txt`; `common/ideas/016_brilliant_scientist_country_ideas.txt`; `common/ideas/016_brilliant_scientist_project_force_ideas.txt` | Source surfaces are present and route consumers are wired. The focused KRG tree inspection recorded 100 focuses with zero KRG diagnostics. The former twenty-one-icon gap is closed statically by 28 visible assignments, 34 registered sprites, and 34 tracked DDS files; live card presentation remains parent-owned. |
| Conventional opening force and supply | `brilliant_scientist_apply_conventional_guard_package` in `common/scripted_effects/016_brilliant_scientist_country_effects.txt` | Covered in source with route, host-army, facility, security, industry, population, and war inputs plus an eight-division ceiling. Live balance remains unclaimed. |
| Project force families, equipment, technology, templates, and caps | `common/units/016_brilliant_scientist_project_forces.txt`; `common/units/equipment/016_brilliant_scientist_project_force_equipment.txt`; `common/technologies/016_brilliant_scientist_project_technologies.txt`; `common/technologies/016_brilliant_scientist_project_force_technologies.txt`; `common/scripted_effects/016_brilliant_scientist_project_force_effects.txt`; `common/scripted_triggers/016_brilliant_scientist_project_force_triggers.txt` | Covered for seven custom sub-unit families, seven locked template consumers, six bespoke equipment archetypes plus variants, operational and weaponization bridges, receipt-guarded materialization, and per-family caps. |
| AI and cleanup | `common/ai_strategy_plans/016_brilliant_scientist_kruger_state_plans.txt`; Event 016 country/project effects and triggers | Covered in source for the nineteen KRG plans, dynamic takeover entry plans, runtime revocation, cleanup, and idempotent formation receipts. Live AI and formation checks remain parent-owned. |
| Assets and model boundary | `gfx/flags/`, `interface/`, Event 016 localisation, and current asset manifests | Flags, portraits, focus/decision surfaces, and localisation are wired for the current package. No Event 016 `.mesh`, `.anim`, entity, or model package exists; no model work was attempted. |

## Concrete remaining gap

The country matrix requires Biological Deployment to inherit a stockpile, defense, and existing-system access, and the country spec requires a bounded biological delivery and consequence lifecycle. The current KRG bridge only records history and readiness:

- `brilliant_scientist_apply_biological_force_history` in `common/scripted_effects/016_brilliant_scientist_project_force_effects.txt` sets `bioweapon_available`, native delivery technologies, and route ideas from carried agent flags.
- `brilliant_scientist_biological_delivery_package_ready` is set by `common/scripted_effects/016_brilliant_scientist_project_effects.txt`, but the KRG force package does not bind a quantity ledger, per-agent stockpile cap, bounded consumption receipt, or KRG-specific delivery action to it.
- `biological_cap = 4` exists in `common/script_constants/016_brilliant_scientist_constants.txt` but has no KRG project-force consumer.
- The KRG focus and safeguard decisions test readiness and containment flags (`brilliant_scientist_kruger_focus_biological_delivery_is_valid`, `brilliant_scientist_krg_segregate_containment_logistics`, and `brilliant_scientist_krg_authorize_canonical_biological_raid`), not an owned stockpile/capacity ledger.

This is a real gameplay/content gap, but it is not a safe narrow patch. Completing it needs an approved cross-system design for agent quantity and cap receipts, delivery/consumption effects, transfer and defeat cleanup, shared CBRN interaction, tooltips/localisation, and balance evidence. Adding a single flag, free stockpile, or placeholder decision would violate the source contract and could bypass condemnation and containment systems.

## Other unresolved surfaces

- Clone, robot, paleogenetic, xenobiological, portal, exotic, and temporal force growth and sustainment are not one complete KRG-owned recurring lifecycle. Event 019 exposes derivative providers for selected families, but integrating a full KRG maintenance and recovery economy remains a broader tranche.
- The former twenty-one visible KRG lifecycle/project-idea icon gap is closed statically; live card presentation and durable portrait-source acceptance remain open.
- The installed package exposes no Technology Tree Viewer. The read-only technology inspection returned `TECH_INSPECTED_PARTIAL` with helper projections deferred for the large workspace, so direct source checks remain the authoritative evidence.
- No Hearts of Iron IV process or live formation, takeover, map, supply, AI, production, or save/load scenario was run.

## Validation evidence

- Static ID scans found seven custom sub-unit definitions, seven locked project-force template names, seven native spawn helpers, six bespoke equipment archetypes with matching `_1` variants, seven operational project-force technology bridges, seven weaponization bridges, and eight history indices including the separate biological family.
- The current target gameplay files are clean in the worktree; no country, map, equipment, technology, focus, decision, localisation, asset, or model file was changed by this audit.
- Focus inspection evidence remains the focused KRG artifact recorded by `016_krg_country_content_audit_2026-08-02.md` (`100` focuses, `0` diagnostics). The current technology check produced the linked partial artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a810b9110e0fd19270f27a9ce77874871b1eb710523dd1e9d701c06d67d7f6ac/eb00519b795ac0651d1dad0b9f2d905c90ba5a9f925672aee22c30a63235564e/technology-lint-73417ff35ecb.json` with no blockers and workspace-wide helper deferral.

## Disposition for parent

No gameplay patch is proposed. Queue the biological stockpile/delivery lifecycle as a dedicated design and implementation tranche, then rerun the KRG country/project-force audit after its receipts, cleanup, UI, and balance evidence exist. The no-model boundary remains in force.
