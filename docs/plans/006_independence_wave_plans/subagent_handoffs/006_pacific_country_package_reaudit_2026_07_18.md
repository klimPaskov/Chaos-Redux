# Event 006 Pacific Country-Package Re-audit

Date: 2026-07-18
Auditor: `chaosx_country_package_auditor`
Scope: IW-173 / HAW, IW-179 / FSM, IW-184 / HBX, and their SCN-008 admission bridge
Overall result: **CONDITIONAL FAIL — keep all three packages fail-closed**

## Executive verdict

No P0 country-package defect was found. IW-179's inert government-route pool
and both island packages' route-contract drift were P1 findings. This lane
corrected both published route pools and implemented a complete four-choice
additive government settlement for Level-1 Micronesia.

The accepted main-agent design resolution assigns Level-2 Hawai'i the full
Event 006 focus framework plus a bespoke Hawaiian shared focus group. The
Pacific package must not add a parallel decision fallback. That exact tree
gate, load, shared group, and guarded cleanup restoration are still pending,
so IW-173 remains a P1 admission blocker. FORM-48's human invitation replies
and complete postformation package also remain outside this country lane and
unattested.

Keep IW-173, IW-179, and IW-184 absent from
`has_independence_wave_runtime_package_content_attestation_for_execution_id`.
Do not set `independence_wave_form48_readiness_attested`.

## Required references and workflow

The audit used `chaos-redux-subagents`, `chaos-redux-events`,
`hoi4-focus-trees`, `hoi4-decisions-missions`, and
`chaos-redux-event-assets`. The required offline wiki pages were consulted,
including the core scripting pages and the national-focus, country-creation,
division/unit, and portrait pages. Official vanilla effects, triggers, script
constants, modifiers, and AI-strategy documentation were also consulted.

Vanilla HAW/FSM histories, generic/shared-focus precedents, and registered tag
ownership were checked directly. The HOI4 MCP domain tools were unavailable in
this subagent session, so no MCP render or rewrite is claimed.

## Route-contract repair

| Package | Accepted routes | Published after repair | Playable selection surface |
| --- | --- | --- | --- |
| IW-173 HAW | traditional monarchy, constitutional, labor, patron client | traditional, constitutional, popular council as labor, patron client; emergency and radical explicitly excluded | pending full Event 006 tree and bespoke HAW shared focus group; no duplicate decision fallback |
| IW-179 FSM | federal council, traditional, constitutional, patron client | popular council as federal council, traditional, constitutional, patron client; emergency and radical explicitly excluded | four mutually exclusive timed package decisions |
| IW-184 HBX | constitutional, labor, emergency, patron client, radical | unchanged and aligned | full Event 006 framework |

The HAW/FSM setup proofs now require the exact positive and negative route
markers. Cleanup clears the emergency/radical exclusions plus the former stale
popular/patron exclusion markers. Shared focus cleanup subsequently clears all
positive availability markers; both generation reset and origin termination
call package cleanup before that shared cleanup.

## FSM additive government settlement

The four Level-1 choices are:

- `independence_wave_fsm_ratify_federal_council_compact`: 50-day light
  diplomatic project; selects popular-council/federal-council, applies a major
  five-value settlement, and is the preferred AI route.
- `independence_wave_fsm_confirm_traditional_leaders_council`: 65-day light
  security project; selects the traditional route and improves legitimacy,
  security, and instability.
- `independence_wave_fsm_adopt_inter_island_constitution`: 50-day light
  diplomatic project; selects the constitutional route and improves
  legitimacy, administration, and instability.
- `independence_wave_fsm_accept_protected_ocean_mandate`: 90-day island-
  strategic project; selects patron client, improves recognition and
  administration, and accepts the shared league-leadership exclusion. AI
  normally avoids it unless severe host threat or patron dependency raises its
  weight.

All four require stable Inter-Island Authority, capital control, an undecided
and unlocked shared government route, their exact published route flag, and no
other FSM package project. Each calls
`independence_wave_select_government_route`, publishes the matching shared
durable-state flag, records
`independence_wave_fsm_government_settlement_complete`, and uses player-facing
outcome localisation. The shared route lock plus the package project
serializer makes them one-shot and mutually exclusive for the current Event
006 generation. Cleanup removes all four decisions and the exact settlement
proof; shared focus cleanup removes route state.

## Country, force, and asset findings

- HAW and FSM remain vanilla registered tags; the package does not re-register
  or overwrite their country/history/flag definitions. HBX remains the custom
  Event 006 tag. PFX remains a cosmetic identity applied only to the HBX
  carrier.
- HAW preserves David Kalakaua Kawananakoa and the complete vanilla Hawaiian
  political roster. No Pacific package effect recruits, promotes, retires, or
  replaces a Hawaiian leader.
- FSM's vanilla history has no usable named leader. Exact IW-179 setup alone
  recruits and promotes `FSM_independence_wave_inter_island_congress_chair`;
  cleanup retires that Event 006 character.
- Force mappings remain aligned with the accepted registry: HAW coastal
  maritime / tradition 62 / navy and air; FSM coastal maritime / 46 / navy
  only; HBX regular defectors / 76 / navy and air.
- All 30 HBX/PFX flag files exist. FORM-48's final DDS SHA-256 is
  `6cfa...d222`.
- Accepted portrait files remain intact: HBX PNG
  `40fc48...c0242`, HBX DDS `7cd867...145e`, FSM PNG
  `0ab238...68310`, FSM DDS `64db23...ae29`. Protected BAY/RHI portrait hashes
  remain `7f0af64f...aad2b` and `aa61cc3...bce2`.
- The FSM route decisions reuse registered government-actions and patron-
  balancing decision sprites. No new portrait, adviser, flag, or icon fallback
  was introduced.

## SCN-008 bridge evidence

The scenario route now shares the normal compile-time content authority:

1. `independence_wave_scenario_attempt_ranked_packages` mirrors
   `independence_wave_scenario_dispatch_package_id` into temporary
   `independence_wave_execution_package_id` before loading the package mapping.
2. The candidate-country scope calls
   `is_independence_wave_scenario_package_preflight_ready` before the shared
   reservation effect.
3. That trigger first requires
   `has_independence_wave_runtime_package_content_attestation_for_execution_id`
   and then checks the exact scenario ID/tag availability branch.
4. Unattested content records the existing `package_unready` rejection rather
   than reserving territory.

The adapter registry contains IW-173, IW-179, and IW-184, but the compile-time
attestation OR contains none of them. SCN-008 therefore sees the mappings and
still rejects all three safely until a later coordinated promotion.

`.tools/audit_event6_allocator.py` passed with 149 publishers, 126
automatic/high-chaos selectable packages, and 138 SCN-ranked selectable
packages. The inspected order is ID mirror -> mapping load -> preflight ->
reservation, with `package_unready` on failed preflight.

## Changed files

- `common/scripted_effects/006_independence_wave_pacific_package_effects.txt`
- `common/scripted_triggers/006_independence_wave_pacific_package_triggers.txt`
- `common/decisions/006_independence_wave_pacific_decisions.txt`
- `localisation/english/006_independence_wave_pacific_l_english.yml`
- `docs/events/006_independence_wave/pacific_country_packages.md`
- this handoff

## Meaningful validation

- FSM's four decision IDs each resolve through decision definition, active-
  project serialization, cleanup, name/description localisation, and package
  documentation.
- All four result effects resolve to an exact route availability check, the
  shared route selector, the corresponding selected-route proof, a matching
  durable-state flag, and a visible country-value transaction.
- No provisional HAW government-decision adapter remains after the full-tree
  design resolution.
- The three touched Clausewitz files have balanced braces; Pacific localisation
  retains UTF-8 BOM encoding.
- The Event 006 allocator audit passed unchanged after the route work.

## Remaining P1 work and readiness recommendation

1. Implement exact dormant IW-173 HAW full-tree loading, the bespoke Hawaiian
   shared focus group, prepared/final tree proofs, and guarded restoration to
   `generic_focus`. Preserve all living/non-Event-006 HAW and every vanilla
   Hawaiian leader.
2. Re-run the focus audit, including the already reported HBX focus/project
   concurrency and bespoke Pacific focus-icon findings, after the HAW focus
   tranche lands.
3. Complete and audit FORM-48 human invitation replies and postformation
   systems before any FORM-48 readiness promotion.
4. Re-run the decision/mission, localisation, country-package, focus, and final
   completion audits as a coordinated admission review.

There is no authorized partial promotion. IW-179's country decision surface is
ready for re-audit, but IW-173, IW-179, and IW-184 must remain absent from both
automatic runtime attestation and SCN-008 admission until all coordinated
Pacific dependencies pass. No fallback or unapproved simplification was used
in this lane.
