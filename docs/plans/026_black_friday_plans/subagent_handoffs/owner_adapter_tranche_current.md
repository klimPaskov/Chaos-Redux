# Event 026 Black Friday — current owner-adapter tranche handoff

Audit date: 2026-08-30.
Documentation refresh: 2026-09-02 against the current worktree; this refresh changes documentation only.

Status: source-bounded and live-blocked; this handoff does not claim universal cost coverage or approve enabling Event 26.

## Implemented bounded tranches

The current source adapters cover 104 registered logical cost components across ten bounded owner tranches: five Communist-spread logical actions with 15 components, seventeen reachable Fury decisions with 42 components, the Japan chemical campaign attack with two components, biological medical-capacity expansion with three components, CBRN civilian-shelter movement with three components, the two Japan biological campaign agents with eight components, four Germany Mengele command-power actions with four components, the D'Rhondan alien-infantry landing reservation with one component, ten Random Faction paid actions with 21 components, and the Africa Elephant logistics contract with five components.

The bounded adapters quote the ordinary current payable cost through the shared Black Friday source, round upward once, preflight every component, pay the quoted amount, record the actual amount in a payer-scoped transaction, settle only after owner completion, and route the registry-defined primary family to the achievement ledger.

Japan chemical and Japan biological payloads are owner-controlled custom equipment components, so their adapters perform the dynamic equipment debit and explicitly acknowledge the external refund before marking the component refunded.

The biological medical-capacity and CBRN adapters preserve their ordinary requirements and delayed effects while discounting only the registered payable components; capacity gains, civilian transfers, time, and other non-cost effects remain outside the sale.

## Source files and identifiers

- Communist-spread adapters: `common/decisions/001_communism_spread_decisions.txt`, `common/scripted_effects/001_communism_spread_effects.txt`, and the Event 026 trigger/effect wrappers.
- Fury adapters: `common/decisions/007_fury_decisions.txt`, `common/scripted_triggers/007_fury_triggers.txt`, `common/scripted_effects/007_fury_effects.txt`, `common/script_constants/007_fury_constants.txt`, and the Event 026 trigger/effect wrappers.
- Japan chemical adapter: `common/decisions/japan_chemical_campaign_decisions.txt`, `common/scripted_effects/JAP_chemical_campaign_effects.txt`, and the Event 026 trigger/effect wrappers.
- Biological medical-capacity adapter: `common/decisions/biowarfare_disease_containment_decisions.txt`, `common/scripted_effects/biological_countermeasure_effects.txt`, and the Event 026 trigger/effect wrappers.
- CBRN shelter adapter: `common/decisions/cbrn_protection_decisions.txt`, `common/scripted_effects/cbrn_protection_decision_effects.txt`, and the Event 026 trigger/effect wrappers.
- Japan biological adapters: `common/decisions/japan_biological_campaign_decisions.txt`, `common/scripted_effects/026_black_friday_effects.txt`, and `common/scripted_triggers/026_black_friday_triggers.txt`.
- Germany Mengele adapters: `common/decisions/germany_mengele_decisions.txt`, `common/scripted_effects/germany_mengele_effects.txt`, `common/scripted_triggers/germany_mengele_triggers.txt`, and `localisation/english/germany_mengele_l_english.yml`.
- D'Rhondan alien-infantry reservation adapter: `common/decisions/016_alien_infantry_landing_decisions.txt`, `common/scripted_effects/016_alien_infantry_api_effects.txt`, `common/scripted_triggers/016_alien_infantry_api_triggers.txt`, `common/scripted_triggers/026_black_friday_triggers.txt`, and `common/scripted_effects/026_black_friday_effects.txt`.
- Shared framework: `common/scripted_effects/chaosx_universal_cost_effects.txt`, `common/scripted_triggers/chaosx_universal_cost_triggers.txt`, `common/script_constants/chaosx_universal_cost_constants.txt`, and their Markdown contracts.

## Registry and inventory evidence

`docs/plans/026_black_friday_plans/event26_cost_surface_registry.md` records the 104 bounded logical component rows with source-adapter status and the remaining native, static, and inaccessible surfaces.

`docs/plans/026_black_friday_plans/event26_cost_surface_custom_inventory.md` currently records 2,224 custom-cost triggers and 2,225 custom-cost text references across 81 Chaos Redux decision files, with the single text-only requirement disclosure at `common/decisions/020_black_plague_rat_decisions.txt:923`. The eight paired rows in `common/decisions/016_brilliant_scientist_technology_actions.txt` are included in this count and remain outside the bounded adapters.

`docs/plans/026_black_friday_plans/event26_cost_surface_native_inventory.md` currently records 1,328 native `cost =` declarations across 62 Chaos Redux decision files, including 1,033 declarations not written as the literal `cost = 0` and 295 zero/free sentinels.

## Validation boundary

Source-level brace, key, line-inventory, localisation, asset, and catalogue checks were reviewed for this tranche, and the Event 26 event inspect/render and probability workflows remain partial because the installed MCP cannot resolve the complete owner pools or full lifecycle helper graph.

No HOI4 session, save/reload, multiplayer, in-game tooltip, refund, or live achievement validation was performed by the agent.

The unadapted custom owners, native one-time decision costs, equipment-upgrade XP, guarantees, operation costs, flat license-purchase fields, factory commitments, special projects, flat leader/tactic costs, MIO assignment and policy costs, custom currencies, and other engine-inaccessible surfaces remain explicit blockers in the registry and Part 8 record. Dedicated audits rejected unsafe partial adapters for CBRN diplomacy, CBRN doctrine, CBRN occupation, and genocide crisis; their handoffs record the exact multi-component, delayed-payment, commitment, cross-owner, and refund boundaries.

Event 26 remains absent from the default enabled-event allowlist until every registry row and live acceptance gate is closed.

## Presentation follow-up

The shared Event Log predicates now show the actorless `Scope: Global` line for Event 26 history and the Event Details tertiary status row for an unfired Event 26 catalogue entry in `common/scripted_guis/chaosx_scripted_gui_events_log.txt`.

The Event Details premise, the biological blocked-cost selector, and the Japanese biological requirements, cost, and effect strings now consume the current dynamic sale wording, and the mirrored workbook cell was exported through the repository exporter.
