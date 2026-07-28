# Event 006 IW-012 formal-route AI closure addendum

Date: 2026-07-28

Status: **IMPLEMENTED / STATIC REVIEW PENDING**

The plan-only design below remains the rationale and acceptance matrix. Gameplay is now wired in the two ICE decision/focus surfaces and the ICE-local trigger file; runtime probability, shared-focus visibility, and whole-event completion remain open.

Event: `006`, Independence Wave

Package: `IW-012`, registered vanilla carrier `ICE`, anchor state `100`

## Disposition and improvement-loop cadence

This document is not a new broad Event 006 expansion pass.

It elaborates one finite closure workstream exposed by the IW-012 implementation after the dynamic former-host AI repair and the decision/mission timing repairs.

The v27 improvement-loop closure remains authoritative: do not add another country package, focus family, formable, decision family, scripted GUI, scenario family, achievement, super-event, visual layer, or technology layer while its finite closure gates remain unresolved.

The new IW-012 source-design gap is narrower:

- all four formal IW-012 route focuses use the same unconditional `high` AI weight;
- `independence_wave_ice_declare_armed_neutrality` independently locks the Emergency Military route and uses an unconditional `urgent` base weight;
- the resulting AI does not perform the accepted two-stage founding-posture and formal-route re-evaluation;
- in an otherwise peaceful package, the armed-neutrality project can pre-empt Constitutional, Traditional, or Patron-Client selection before those focus weights can express a preference;
- route probability is therefore not merely missing runtime evidence; the current source lacks the package-aware comparison promised by the accepted specification.

This addendum should be implemented once, audited, folded into the accepted IW-012 and AI specifications, and closed.

Do not run another IW-012 improvement-loop pass while this addendum remains unresolved.

## Evidence for the gap

### Accepted design contract

`docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_4_focus_tree_architecture.md` requires the AI to choose routes in two stages.

The founding posture reads government archetype, starting institution, host hostility, military strength, legitimacy, regional tradition, patron offers, League presence, and chaos.

The formal route decision then re-evaluates current conditions and avoids constitutional government during collapse, military expansion without the means to sustain it, invalid patron or formable routes, and suicidal confrontations.

`docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_7_ai_balance_assets_and_acceptance.md` additionally states that a single generic AI weight table is insufficient.

### Current IW-012 source

The four formal route consumers in `common/national_focus/006_independence_wave_focus.txt` are:

- `independence_wave_ice_choose_constitutional_route`;
- `independence_wave_ice_restore_traditional_authority`;
- `independence_wave_ice_establish_emergency_command`;
- `independence_wave_ice_accept_patron_mandate`.

Each currently uses:

```txt
ai_will_do = { base = constant:independence_wave_focus_ai.high }
```

Their validity triggers are package-aware, but their relative AI preferences are not.

`common/decisions/006_independence_wave_ice_decisions.txt` defines `independence_wave_ice_declare_armed_neutrality` as a serialized 180-day project with:

```txt
ai_will_do = {
	base = constant:independence_wave_decision_ai.urgent
	modifier = {
		factor = constant:independence_wave_decision_ai.modifier_double
		has_independence_wave_severe_host_threat = yes
	}
}
```

On completion it calls `independence_wave_select_government_route` with `emergency_military`.

That project is therefore both a material security project and an alternate formal route selector.

Its urgent peaceful weight is higher than the other ICE project weights and is not conditioned on war, severe host threat, institutional collapse, or the relative maturity of the other three route ledgers.

### Post-repair distinction

The static Denmark targeting defect is no longer current.

`independence_wave_ice_apply_host_ai` and `independence_wave_ice_clear_host_ai` in `common/scripted_effects/006_independence_wave_ice_package_effects.txt` now add and reverse supported `befriend` and `prepare_for_war` strategies against `event_target:independence_wave_setup_former_host`.

Do not reintroduce a literal `DEN` target, do not redesign that repaired helper, and do not describe the stale fixed-target implementation handoff as current source.

The harbour mission and DM-01 serialization defect are also repaired.

`independence_wave_ice_hold_the_harbour` remains outside `has_independence_wave_ice_active_package_project`, the deadline is 1,440 days, and the audited six-project path is 1,230 project-days.

This addendum does not reopen either repair.

## Research and vanilla precedent

The installed vanilla Iceland content provides the relevant precedent without requiring a new lore layer.

### Institutional choice

`common/ai_strategy_plans/ICE_historical_strategy_plan.txt` prioritizes `ICE_the_kingdom_of_iceland` followed by `ICE_declare_absolute_neutrality`.

`common/ai_strategy_plans/ICE_alternate_strategy_plan.txt` instead gives the cooperative democratic plan `ICE_united_we_stand`, `ICE_joint_shipbuilding_programme`, `ICE_patrolling_the_atlantic`, `ICE_not_standing_idly_by`, and `ICE_industrial_cooperation`, while setting `ICE_declare_absolute_neutrality = 0`.

The vanilla precedent is therefore not a four-way equal roll.

It distinguishes a neutral institutional posture from a Denmark-cooperative maritime posture and suppresses an incompatible alternative.

### Maritime survival

The installed vanilla `common/national_focus/iceland.txt` connects:

- `ICE_expand_the_harbour` to local port capacity;
- `ICE_expand_the_fishing_industry` to the island economy;
- `ICE_the_merchant_fleet` to convoy capacity;
- `ICE_patrolling_the_atlantic` to naval readiness;
- `ICE_joint_military_training` and `ICE_not_standing_idly_by` to a threat-responsive defense posture;
- `ICE_united_we_stand` and `ICE_industrial_cooperation` to cooperation with Denmark;
- `ICE_declare_absolute_neutrality` to a mutually exclusive independent posture.

These are gameplay precedents, not authority to copy vanilla rewards or overwrite the preserved tree.

They support using port, shipping, host relationship, and threat variables to choose among the existing Event 006 routes.

### Historical use boundary

The vanilla event chain represents equal standing with Denmark, a possible Danish king, a republican outcome, and a break with the Crown.

Those themes justify the existing Constitutional and Traditional routes.

They do not justify inventing a new royal claimant, a new Danish-only host rule, a second Nordic formable, or a generic North Atlantic empire.

The Event 006 former host remains dynamic.

## Proposed bounded implementation

### Principle

Keep the four existing route focuses as the only formal IW-012 government selectors.

Convert Armed Neutrality into an emergency security project that materially enables and favors Emergency Military but does not itself write the government route.

This restores a single formal route arbitration point and allows the AI focus weights to compare all currently valid routes.

No new focus, decision, mission, idea, variable, flag, country, formable, event, GUI, asset, or super-event is required.

### Change 1: remove the duplicate route write from Armed Neutrality

In `independence_wave_ice_declare_armed_neutrality`:

- retain the existing security-major cost;
- retain the 180-day duration;
- retain `fire_only_once = yes`;
- retain `independence_wave_ice_armed_neutrality_declared`;
- retain the existing value changes, Coastwatch idea, and shared security progress;
- remove only the temporary `independence_wave_government_route_input` assignment and the call to `independence_wave_select_government_route`;
- keep the project unavailable after any government route is formally locked.

The decision remains a visible material commitment.

It no longer bypasses the formal route focus layer.

The Emergency Military focus should use the declaration as a strong maturity signal, not as an additional hard prerequisite.

Keeping it as a signal avoids making the 180-day project mandatory when a severe war requires the AI to lock Emergency Military immediately.

### Change 2: make project AI establish a founding posture

Update only the six existing `ai_will_do` blocks in `common/decisions/006_independence_wave_ice_decisions.txt`.

Use the existing shared constants from `independence_wave_decision_ai`; do not add duplicate numerical constants.

| Project | Base | Positive modifiers | Avoidance modifiers | Intended behavior |
| --- | ---: | --- | --- | --- |
| `independence_wave_ice_reconcile_shipping_registers` | `high` = 25 | `modifier_double` when Shipping Security is below `secure_threshold`; `modifier_double` when Port Authority is below `traditional_route_threshold` | `modifier_half` at war | Establish the common maritime and administrative trunk before prestige diplomacy. |
| `independence_wave_ice_charter_municipal_council` | `high` = 25 | `modifier_double` while Civic Cohesion is below `constitutional_route_threshold`; `modifier_double` under severe instability | `modifier_half` at war | Favor civilian settlement in recoverable peace without outranking immediate survival. |
| `independence_wave_ice_expand_coastwatch` | `high` = 25 | `modifier_major` under severe host threat; `modifier_double` at war | none | Make Coastwatch urgent because of a real threat, not by unconditional package identity. |
| `independence_wave_ice_negotiate_north_atlantic_compact` | `standard` = 10 | `modifier_major` when the family is registered, Compact Support is at least `compact_negotiation_threshold`, Network Standing is at least `observed`, and there is no severe host threat; `modifier_double` when League membership already exists | `modifier_half` at war | Pursue the existing compact only when its diplomatic surface is materially open. |
| `independence_wave_ice_settle_former_host_charter` | `standard` = 10 | `modifier_major` when the former host lives, is not at war with ICE, and either host hostility or reconquest fear meets the existing conflict gate; `modifier_double` when no severe host threat remains | `modifier_half` when ROOT is at war | Use the charter as risk reduction, without preserving a Denmark-only assumption. |
| `independence_wave_ice_declare_armed_neutrality` | `very_low` = 2 | `modifier_major` under severe host threat; `modifier_double` at war | factor `blocked` when there is no severe host threat and ROOT is not at war | Keep the emergency security commitment dormant in ordinary peace and available to a threatened AI. |

The parent may express repeated compound tests through narrowly named ICE scripted triggers if that is clearer.

If new scripted triggers are introduced, place them in `common/scripted_triggers/006_independence_wave_ice_package_triggers.txt`; do not create a generic cross-package helper for this one package.

Do not introduce an on-action poll.

### Change 3: perform formal route re-evaluation in focus weights

Replace the four equal `high` focus weights with the following exact matrix.

Use the existing shared constants from `independence_wave_focus_ai`.

Every focus retains its current `allow_branch`, `available`, prerequisite, mutual exclusions, 70-day cost (`@independence_wave_focus_standard = 7`), completion reward, icon, and localisation.

#### Constitutional Republic

Base: `standard` = 10.

Apply:

- `strong_preference_factor` = 4 when Civic Cohesion is at least `stable_threshold`, there is no severe host threat, and ICE is not at war;
- `preferred_factor` = 2 when `independence_wave_ice_former_host_charter_settled` exists;
- `war_avoid_factor` = 0.25 when ICE is at war or a severe host threat exists;
- `avoid_factor` = 0.1 under severe instability.

#### Traditional Authority

Base: `standard` = 10.

Apply:

- `strong_preference_factor` = 4 when Port Authority is at least `stable_threshold`, Shipping Security is at least `secure_threshold`, and Shipping Registers are reconciled;
- `preferred_factor` = 2 when the former-host charter is settled and the former host still lives;
- `war_avoid_factor` = 0.25 under severe host threat.

The Traditional route represents an internally grounded authority settlement.

Do not make it require Denmark, a Danish monarch, or subject status.

#### Emergency Military

Base: `standard` = 10.

Apply:

- `strong_preference_factor` = 4 under severe host threat;
- `strong_preference_factor` = 4 at war;
- `preferred_factor` = 2 when Armed Neutrality has been declared or Coastwatch Readiness is at least `secure_threshold`;
- `avoid_factor` = 0.1 when `has_stable_independence_wave_ice_state = yes`, ICE is at peace, and no severe host threat exists.

#### Patron-Client

Base: `standard` = 10.

Apply:

- `strong_preference_factor` = 4 when Compact Support is at least `compact_threshold` and Network Standing is at least `treaty_backed`;
- `preferred_factor` = 2 when a severe host threat exists and ICE is not at war;
- `preferred_factor` = 2 when ICE is already a League member;
- `war_avoid_factor` = 0.25 at war.

The existing `can_lock_independence_wave_ice_patron_client_route` remains the hard validity gate.

Do not infer a patron when the shared patron system has not supplied one.

### Expected all-routes-valid weights

These are design checks, not claims about live engine behavior.

They assume no additional modifier outside the row.

| Scenario | Constitutional | Traditional | Emergency | Patron | Expected leader |
| --- | ---: | ---: | ---: | ---: | --- |
| Stable civic peace; charter settled | 80 | 10 | 1 | 10 | Constitutional |
| Stable port authority and shipping; charter settled | 10 | 80 | 1 | 10 | Traditional |
| War plus severe host threat and mature Coastwatch | 0.625 | 2.5 | 320 | 2.5 | Emergency |
| Mature Compact, treaty-backed network, peaceful severe host pressure | 2.5 | 2.5 | 40 | 80 | Patron |
| No route has a mature distinguishing signal | 10 | 10 | 10 | 10 | Controlled replayable tie |

An equal weight is acceptable only when the world state genuinely supplies no distinguishing evidence.

### Costs and pacing

No costs or durations change.

The existing project prices remain:

- administration light for Shipping Registers;
- administration standard for Municipal Council;
- security standard for Coastwatch;
- diplomatic standard for the Compact;
- diplomatic standard for the former-host charter;
- security major for Armed Neutrality.

The existing durations remain `120/180/180/300/270/180` days.

The harbour deadline remains 1,440 days.

The formal route focuses remain 70 days.

Do not compensate for AI behavior by granting political power, free equipment, free convoys, units, factories, or shortened timers.

## Localisation, assets, and documentation

### Localisation

No new player-facing key is required because the project names, descriptions, effect tooltips, focus names, and route outcomes do not change.

The parent must still compare `independence_wave_ice_armed_neutrality_effect_tt` with the revised effect.

If that tooltip explicitly says Armed Neutrality immediately selects Emergency Military, revise the existing key in `localisation/english/006_independence_wave_ice_l_english.yml` so it describes the security commitment and its support for the emergency route.

Do not add implementation-history language.

### Assets

No visual asset is required.

Reuse the current registered Event 006 focus and decision sprites.

No animated sprite, portrait, flag, advisor icon, report image, news image, achievement icon, 3D model, or super-event art is authorized.

### Documentation promotion

While queued, this file remains in `docs/plans/006_independence_wave_plans/`.

If accepted and implemented:

- merge the route arbitration rule and exact matrix into the IW-012 section of `006_independence_wave_spec_part_5_country_packages_and_regional_overlays.md`;
- merge the two-stage AI acceptance cases into `006_independence_wave_spec_part_7_ai_balance_assets_and_acceptance.md`;
- update `docs/events/006_independence_wave_iw012_ice_package.md`;
- update `006_source_of_truth_map.md` and `006_independence_wave_resume_packet.md`;
- reconcile stale IW-012 handoffs that still describe a fixed Denmark target or unconditional route behavior.

Do not promote this document into the specs before the parent accepts the design.

## Exact implementation surfaces

Required:

- `common/decisions/006_independence_wave_ice_decisions.txt`;
- `common/national_focus/006_independence_wave_focus.txt`;
- `docs/events/006_independence_wave_iw012_ice_package.md`;
- `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md`;
- `docs/plans/006_independence_wave_plans/006_independence_wave_resume_packet.md`;
- `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_5_country_packages_and_regional_overlays.md` after acceptance;
- `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_7_ai_balance_assets_and_acceptance.md` after acceptance.

Conditional:

- `common/scripted_triggers/006_independence_wave_ice_package_triggers.txt` if compound AI conditions are factored into ICE-local helpers;
- `localisation/english/006_independence_wave_ice_l_english.yml` only if the existing Armed Neutrality tooltip promises an immediate route lock;
- the latest IW-012 audit and implementation handoffs when their stale target or route wording is reconciled.

Not authorized:

- `common/ai_strategy/006_independence_wave_ice.txt`, except if an implementation audit finds a concrete regression in the already repaired dynamic-host helper;
- FORM-02 implementation files;
- package registry or allocator files;
- event scripts;
- GUI or GFX files;
- achievements;
- super-events;
- technology or doctrine files.

## AI and validation matrix

### Static source checks

The implementation audit must prove:

- Armed Neutrality no longer calls `independence_wave_select_government_route`;
- each of the four formal route focuses remains mutually exclusive and is the only IW-012 formal route writer;
- all six project weights read current package state rather than a single unconditional urgency tier;
- the four focus weights are materially different under the four named scenarios;
- every new compound trigger, if any, is ICE-local and used;
- no literal `DEN` is added to Event 006 ICE AI targeting;
- no project becomes a zero-cost or repeatable reward path;
- the exact vanilla `iceland_tree` carrier body remains preserved apart from the existing Event 006 shared-focus imports.

### Probability evidence

Use the read-only HOI4 probability inspector against the six ICE decision weights and four ICE formal-route focus weights.

Run at least these declared scenarios:

1. stable civic peace with a settled former-host charter;
2. stable port and shipping administration with a settled charter;
3. severe host threat while at war with mature Coastwatch;
4. treaty-backed Compact with peaceful host pressure;
5. stable neutral peace with no distinguishing route signal;
6. patron route invalid;
7. former host dead;
8. route already locked.

Acceptance:

- an invalid route receives zero selectable probability through its existing availability gate;
- the named route holds at least 55 percent of the four-route weight in scenarios 1, 2, and 4;
- Emergency Military holds at least 75 percent in scenario 3;
- Armed Neutrality has zero AI willingness in stable peace without war or severe host threat;
- no valid all-route scenario produces an accidental 100 percent route unless only one route is valid;
- repeated seeded runs preserve some replayability in the undifferentiated tie case;
- decision sequencing never makes the 1,440-day harbour survival path impossible when all required resources remain available.

`hoi4.focus_inspect` and `hoi4.focus_render` currently omit imported `shared_focus` nodes from their useful metrics.

Record that limitation and use source-level carrier/import evidence alongside the probability inspection.

The installed package has no Technology Tree Viewer.

No technology work is proposed, and the absence of that viewer does not block this addendum.

### Parent-owned runtime evidence

Repository agents must not launch HOI4.

The parent must retain the current HOLD for:

- live dormant-tag allocation and synchronized release;
- date/DLC-safe ICE leader and commander consumption;
- former-host survival and host-death cleanup;
- save/load persistence;
- force materialization;
- live shared-focus visibility;
- AI project start/cancel behavior;
- formal route selection;
- scenario transaction behavior;
- GUI/Event Details;
- achievements and super-events;
- whole-event completion reconciliation.

No static probability result is a substitute for those consumer checks.

## Separate FORM-02 blocker

IW-012 registers the North Atlantic Compact family, but FORM-02 completion is not established by this addendum.

`has_independence_wave_form02_strict_mutation_preconditions` requires a valid `GZX` Newfoundland founder and one valid pair among ICE, AKX, and SCO.

The current compile-time attestation set admits ICE and SCO but does not admit IW-182/GZX, while IW-011/AKX remains scenario-variant-only.

Therefore:

- do not advertise FORM-02 as reachable from the current automatic attestation set;
- do not weaken the strict founder matrix;
- do not substitute ICE or SCO for the required Newfoundland founder;
- do not create a fallback tag or generic Newfoundland package;
- do not seed FORM-02 post-formation values from ICE until strict reachability and transaction evidence exist;
- keep FORM-02 reachability as a separate plan-only HOLD boundary.

Adding IW-182 is a country-package expansion and is expressly outside this closure addendum.

## What should not be added

Do not add:

- a fifth Iceland government route;
- a second armed-neutrality decision or focus;
- a new Iceland civil war;
- a Danish-only scripted branch;
- a new monarch or generated leader;
- a new North Atlantic currency, Parliament GUI, or League sub-system;
- a second Nordic identity;
- a new package solely to make FORM-02 compile;
- passive daily, weekly, or monthly polling;
- a super-event for an ordinary IW-012 route lock;
- new art for AI-only behavior;
- technology or doctrine bonuses as compensation.

Those additions would bloat a package whose remaining problem is arbitration, not content volume.

## Acceptance and closure criteria

This addendum closes when:

- the duplicate Armed Neutrality route write is removed;
- the six existing project weights implement the founding-posture table;
- the four existing focus weights implement the formal re-evaluation table;
- existing costs, durations, route rewards, carrier imports, and preserved vanilla content remain unchanged;
- any directly stale Armed Neutrality tooltip is corrected;
- source and probability audits satisfy the matrix above;
- the accepted design is promoted into Parts 5 and 7;
- the IW-012 event documentation, source map, resume packet, and current handoffs agree;
- no fallback, generic bulk content, or live-game completion claim is used.

Event 006 must remain **HOLD / PARTIAL** after this bounded implementation until the separate allocator, transaction, runtime, FORM-02, GUI, achievement, super-event, and whole-event closure gates are resolved.

## Parent handoff

Design problem: IW-012 has four valid formal route consumers but equal focus weights, while an urgent decision independently locks Emergency Military.

Proposed closure work: make Armed Neutrality an emergency security signal rather than a second formal selector, then make the six existing decisions establish a state-aware founding posture and the four existing route focuses re-evaluate civic, maritime, threat, host, network, and League conditions.

Research basis: the accepted two-stage Event 006 AI contract and installed vanilla Iceland strategy/focus precedents distinguish neutrality, host cooperation, maritime capacity, and threat response rather than using a four-way equal roll.

Implementation surfaces: two gameplay files are required, one ICE trigger file is conditional, and the listed docs/specs/localisation surfaces must be reconciled after acceptance.

Open questions: none are required to implement the bounded arbitration table.

Separate blocker: FORM-02 still requires a valid GZX/Newfoundland founder and runtime transaction evidence; this addendum does not solve or weaken that gate.

Prior addendum state: v27 remains unresolved and authoritative.

This file is a finite v27 closure workstream made necessary by the subsequent IW-012 tranche, not a new broad expansion layer.
