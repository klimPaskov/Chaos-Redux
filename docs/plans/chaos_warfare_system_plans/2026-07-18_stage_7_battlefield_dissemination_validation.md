# Stage 7 Battlefield Biological Dissemination Validation

Status: implementation, primary source validation, scripted-system audit, localisation audit, and main-agent tranche audit complete. One bounded completion-auditor attempt returned unavailable evidence and is not counted as a pass. Stage 7 and the overall Chaos Warfare goal remain incomplete.

## Accepted route correction

Battlefield deployment is implemented as four native land raids. It is not a decision click. The route covers Anthrax, Plague, Tularemia, and Smallpox with exact native target-state selection and preserves the ordinary biological lifecycle. Generated decision-icon drafts are excluded from wiring and are not completion evidence for this route.

## Current-version source evidence

The implementation was checked against:

- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/raids/_documentation.md`
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/raids/land_infiltration_custom.txt`
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/raids/land_infiltration_raids.txt`
- the required offline wiki core pages and the current Chaos Redux raid, headquarters, biological lifecycle, equipment, policy, AI, localisation, and GFX surfaces.

The current raid schema supports exact `var:target_state`, actor and victim country variables, land starting points and arrows, repeatable battalion requirements, assigned units, native essential-equipment reservation, success factors, and four result callbacks. The implementation uses those surfaces directly.

The installed raid documentation defines the predefined `enemy_units` success factor as province-target-only. Although one current vanilla state-target raid retains that factor, this route does not rely on the ambiguous precedent. Concentrated armies are checked with the exact supported `divisions_in_state` trigger for eligibility and AI weighting; `enemy_units` is absent from the native state-raid success formulas.

## Route evidence

| Requirement | Repository evidence | Result |
| --- | --- | --- |
| Native raid-only deployment | `common/raids/biological_battlefield_raids.txt` defines four land raid types; no decision references any battlefield route helper or icon. | implemented |
| Exact target | All target, availability, launch, tooltip, resolver, and lifecycle calls use native `var:target_state`. | implemented |
| Front and military target | The target must be enemy-controlled, passable, eligible, adjacent to an actor-controlled state with an actor division, and contain a supply node or at least three enemy divisions. | implemented |
| Theater authorization | A current valid Combined CBRN Overmatch command, full readiness, battlefield-use policy, Theater CBRN Headquarters technology, war, and matching project are required. | implemented |
| Assigned delivery force | One infantry, motorized, or mechanized formation with at least three matching battalions is required; the origin is a supply node and the path is land. | implemented |
| Exact payload | Native essential equipment reserves 50 Anthrax, 25 Plague, 25 Tularemia, or 10 Smallpox packages. Shared constants mirror those values for lifecycle and history records. | implemented |
| Equal delivery reliability | All four agent raids use the same 0.50 native base success factor; agent identity changes lifecycle potency, not delivery chance. | implemented |
| Shared lifecycle | Limited, success, and critical outcomes map to partial, success, and catastrophic `battlefield_dissemination` seeds through `bio_lifecycle_dispatch_seed`. | implemented |
| Failed attempt | Failure loses the native reservation, stores 50 exact-state attempt evidence, adds the eligible 12-base biological Condemnation source, and does not create completed-use history. | implemented |
| Friendly blowback | A successful primary dispatch may seed one exact eligible adjacent actor-controlled state through `connected_spread`; there is no second payload debit, alternate-state search, or periodic retry. | implemented |
| Occupied friendly territory | The player may target enemy-held friendly-related territory; exposed share rises by 25 percent. AI never selects actor-, faction-, or subject-related owned territory. | implemented |
| Doctrine boundary | Doctrine can raise potency and blowback and refund only bounded Command Power. Only Condemnation may be reduced. Payload, evidence, attribution, physical effects, history, and public-harm floors remain intact. | implemented |
| Route-aware AI | The AI uses the same readiness, policy, project, payload, HQ, front, and target gates, plus retaliation, safety, desperation, treaty, outbreak, and sanction-vulnerability weights. | implemented in source; final package scenarios remain open |
| Private architecture | Battlefield helpers live in biological subsystem files and do not enter shared dynamic effect/trigger registries. | implemented |

## Native reservation mirror

The raid parser's native fields use file-local `@` values because those fields do not accept shared script constants. The route adapter uses script constants for cross-file lifecycle and history work. The following values must stay equal:

| Agent | Raid reservation | Shared reservation | Raid Command Power | Shared Command Power |
| --- | ---: | ---: | ---: | ---: |
| Anthrax | 50 | 50 | 10 | 10 |
| Plague | 25 | 25 | 12 | 12 |
| Tularemia | 25 | 25 | 10 | 10 |
| Smallpox | 10 | 10 | 15 | 15 |

The AI minimum success chance is 0.35 in both parser surfaces.

## Source-derived balance scenarios

These are deterministic source calculations, not substitutes for the final Stage 14 live package scenarios. They verify that agent identity, native result, and doctrine produce differentiated route values before protection, target response, outbreak progression, and later containment are applied.

| Agent | Partial seed intensity | Success seed intensity | Critical-result seed intensity | Theater net Command Power | Terminal net Command Power |
| --- | ---: | ---: | ---: | ---: | ---: |
| Tularemia | 9.35 | 17.00 | 22.95 | 5 | 0 |
| Anthrax | 11.00 | 20.00 | 27.00 | 5 | 0 |
| Plague | 12.65 | 23.00 | 31.05 | 7 | 2 |
| Smallpox | 14.30 | 26.00 | 35.10 | 10 | 5 |

The intensity calculations are `20 route intensity × canonical agent strength × result multiplier`. The route multiplier is neutral for every agent. Theater Contamination then multiplies physical seed potency by 1.10 and Terminal Hazard by 1.15. The Command Power columns apply the 5- or 10-point post-resolution refund capped to the native cost. Every row still consumes the complete native payload reservation for failure, partial, success, and critical resolution; doctrine never changes that debit. Evidence remains 40 for partial, 50 for success, and 65 for the critical operational result before the shared evidence clamp, independent of doctrine.

The internal catastrophic result token names the critical operational multiplier. Only Smallpox belongs to the severe weapon tier; Tularemia, Anthrax, and Plague retain their low, moderate, and serious classifications even after a critical delivery.

## Existing asset reuse

No existing raid DDS was edited, deleted, resized, or replaced. The four raid types reuse these registered sprites and files:

| Sprite | File | SHA-256 |
| --- | --- | --- |
| `GFX_raid_type_icon_anthrax_strike` | `gfx/interface/military_raids/map_icons/raid_type_icon_anthrax_strike.dds` | `0B3782F0E035EE9A54F64719A666C47E88F9363E9875AB4F43056303B20A3C4E` |
| `GFX_raid_type_icon_plague_strike` | `gfx/interface/military_raids/map_icons/raid_type_icon_plague_strike.dds` | `345640F3E2BF329D4EBBC4DBBF21177224558CBC78EC8617EB5066386AE998C8` |
| `GFX_raid_type_icon_tularemia_strike` | `gfx/interface/military_raids/map_icons/raid_type_icon_tularemia_strike.dds` | `2B8F1A6B945A6DBC643D251958C6803F647520E9195094DD3B47A8D3A2D8F6FB` |
| `GFX_raid_type_icon_smallpox_strike` | `gfx/interface/military_raids/map_icons/raid_type_icon_smallpox_strike.dds` | `66D665A8301FA0D37CFBE59CFBF02D19BE3A0FE96D693148209534BC9C84FBDA` |
| Category/unit aliases | `gfx/interface/military_raids/map_icons/raid_unit_icon_biological_raids.dds` | `C700EE7DF963B54061FBD59B54DCF1292777597011797E467C89D3B6747D344F` |

## Engine limits and rejected substitutes

Current-version scripting exposes no exact link between a Combined CBRN Overmatch headquarters command and the raid's selected state, and no native raid launch callback. The accepted supported implementation therefore uses the active valid command as theater authorization and the native raid state/formation/equipment as release context. It does not infer a headquarters state or use a flag, decision, event, air activity, estimator, or proxy as a launch substitute.

If authorization or target context is no longer exact at resolution, the full native reservation remains lost and the resolver creates no release, evidence substitute, use history, or Command Power refund. This is disclosed fail-closed behavior, not a fallback.

The state-target raid also omits the province-only `enemy_units` success factor. Exact state division concentration still controls eligibility and AI scoring; no province estimator or assumed target province replaces the unsupported modifier.

## Specialist audits

- `docs/plans/chaos_warfare_system_plans/subagent_handoffs/2026-07-18_battlefield_biological_scripted_system_audit.md` records the scripted-system architect review. It confirmed the native raid grammar, exact scope stack, payload/HQ continuity, AI gates, lifecycle route, doctrine boundary, private helper ownership, regular event-target cleanup, and unchanged asset reuse. It raised the documented province-only `enemy_units` conflict; the main pass removed that modifier and its unused constants from all four state-raid formulas.
- `docs/plans/chaos_warfare_system_plans/subagent_handoffs/2026-07-18_battlefield_biological_localisation_audit.md` records complete 26-key coverage and the wording audit. The main pass accepted its exact-state, payload, headquarters, shared-lifecycle, blowback, occupied-friendly, doctrine, and fail-closed improvements, then restored non-numeric disclosure that a failed attempt leaves forensic evidence and may raise Condemnation.
- A bounded `chaosx_event_completion_auditor` run was interrupted before it inspected the implementation, specs, plan, validation, or handoffs. It confirmed only the installed documentation's province-only `enemy_units` limit. This is unavailable completion-audit evidence, not a pass. The full mapped Stage 13 completion audit remains open.
- The main-agent tranche audit compared the live implementation against Spec 06's battlefield route, the Stage 7 plan, current headquarters/equipment/lifecycle/AI/GFX/localisation surfaces, installed raid documentation, vanilla land/state raid precedents, and both returned handoffs. It found no unresolved blocker to committing this bounded route. This does not substitute for final Stage 7, Stage 13, or Stage 14 audits.
- HOI4 MCP inspection produced no artifact during the specialist audit and is not counted as validation. Source, installed documentation, vanilla precedent, exact key/call-site inventories, value mirrors, and asset hashes are the available evidence for this tranche.

## Remaining Stage 7 work

Food/water/medical-chain sabotage, laboratory and stockpile accidents, captured-facility and doomsday releases, complete agent-specific countermeasures and treatment, remaining assets and final localisation, legacy caller migration, package scenarios, improvement-loop review, and all remaining mapped audits are still open. This validation file does not establish Stage 7 or overall completion.
