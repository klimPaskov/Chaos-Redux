# Camp Repression Scenario Contract Validation Report

Feature id: `system_camp_repression_rework`

Date: 2026-07-11

Validation mode: static script, localisation, GUI, GFX, and asset readback after the final Ledger and decision-cooldown corrections.

Result: **PASS — `ScenarioContracts=15 Failed=0`**.

This result covers the 13 scenarios in Part 7 plus `SCN-ABSTRACT-CHEM-BIO` and `SCN-FULL-LEDGER`. A pass means the required identifiers, gates, dispatch paths, state ownership or responsibility paths, cleanup calls, UI bindings, and presentation consumers were traceable with no static contract failure.

It does **not** mean these scenarios were executed in the HOI4 engine. No engine-runtime scenario execution occurred in this environment. Numeric deltas, timed mission behavior, AI choices, rendered GUI state, sound playback, and save-state transitions were not observed in a running game.

## Reconciled inventory used by the trace

- 84 player actions: 29 major, 43 colonial, and 12 generic.
- 41 missions: 17 major, 19 colonial, and 5 generic.
- Four separate Ledger controls: show, hide, open, and close.
- All 32 Ledger country action slots use the same native decision cooldown gates as their corresponding normal decisions.
- Connected active-country and active-state arrays feed the host-owned monthly runtime.
- Population damage reduces real state population through the Chaos Meter Deaths path.
- Stored responsible-country and accumulated-evidence state control discovery and condemnation.

## Static scenario results

| Scenario | Static contract evidence traced | Result |
| --- | --- | --- |
| `SCN-GER-AUSCHWITZ` | State `88`, Auschwitz registration, Deaths and population bridge, Mengele permission/autonomy pressure, and cloning unlock gates connect across the Germany decisions, shared effects, and Mengele chain. | PASS (static) |
| `SCN-GER-CORE-FALLBACK` | Germany's occupied/non-core preference and penalized core-fallback output, stability, and backlash paths are present. | PASS (static) |
| `SCN-JAP-OCCUPIED-CHINA` | Occupied China/Manchuria pools, owner-linked population loss, Japan responsibility, Ishii gates, and Pingfang program paths connect. | PASS (static) |
| `SCN-SOV-HIGH-PARANOIA` | Gulag expansion, projected paranoia, famine pressure, Union Crisis memory/relief, and high-crisis cap paths connect. | PASS (static) |
| `SCN-UK-RAJ` | Raj and subject-controlled selection, British output, Raj burden, autonomy pressure, mission outcomes, and reform routes connect through the colonial action bus. | PASS (static) |
| `SCN-USA-PACIFIC` | Threat-gated relocation authority, court review, termination, redress, and conservative AI conditions are present. | PASS (static) |
| `SCN-VICHY-NORTH-AFRICA` | Vichy/French route gates, North Africa pools, labor route, refugee-aid action, and later democratic/Free French reform paths connect. | PASS (static) |
| `SCN-ITA-LIBYA` | Libya/East Africa project pools, roads, forts, security, transport guard, closure, compensation, and exclusion of Italian cores from colonial projects connect. | PASS (static) |
| `SCN-BEL-CONGO` | Congo/subject pools, quota, corridor, resource, burden, accountability, strike settlement, inspection, and reform paths connect. | PASS (static) |
| `SCN-GENERIC-OCCUPATION` | Authoritarian activation, high-resistance non-core selection, labor route, inspection, AI caps, and territorial rather than protected-class selection connect. | PASS (static) |
| `SCN-DISCOVERY-CONTROL` | Enemy-control discovery reads stored responsibility, condemns the responsible authority, preserves state-linked Deaths, and does not blame the discoverer. | PASS (static) |
| `SCN-DISMANTLEMENT-CLEANUP` | Current-control eligibility, mission resolution, active-array removal, idea conversion, stale-decision hiding, category cleanup, and selected-state clearing connect. | PASS (static) |
| `SCN-NO-MONTHLY-SPAM` | Registered monthly processing updates Deaths and state/country pressure without a recurring minor leak-report call path. | PASS (static) |
| `SCN-ABSTRACT-CHEM-BIO` | Capability and stockpile gates connect to abstract Deaths, short-term resistance, logistics, contamination/outbreak, evidence, discovery, instability, and tribunal results. Chemical tiers are chlorine, phosgene, mustard, lewisite, tabun, sarin, and soman; biological tiers are anthrax, tularemia, plague, and smallpox. No operational recipe or protected-class selector is present. | PASS (static) |
| `SCN-FULL-LEDGER` | Five tabs, bounded pool/site/country arrays, country-panel header, phase and discovery display, 32 cooldown-parity action slots, cleanup, and all 24 generated sprite consumers connect. Evidence and reform seals have scripted visibility. | PASS (static) |

## Presentation and focus readback

The Ledger's 24 DDS sprites derive from frozen ImageGen sources in `docs/assets/system_camp_repression_rework/source/ui_imagegen/`. The prompts are recorded in `docs/assets/system_camp_repression_rework/prompts/repression_ledger_imagegen_prompts.md`, and `docs/assets/system_camp_repression_rework/tools/build_ledger_ui_assets.py` is the deterministic processor. The maintained static presentation is neither a header-only implementation nor a simple-shape fallback. Optional authored frame animation remains queued as an enhancement.

Super-event slots `12`, `74`, `75`, `76`, and `77`, audio IDs `45`, `44`, `46`, `47`, and `48`, and achievements `60` through `69` were included in the presentation readback. Germany's focus reward lifecycle is consolidated to a maximum of three stable lane spirits before convergence and exactly one final capstone spirit. The core variant preserves exact science-and-force totals; stage-specific variants preserve the exact highest completed optional territorial stage through reclamation, continental dominance, the command spine, or full world dominance. The trace found no new command prerequisite.

## Engine-runtime validation gap

The following observations require a running HOI4 session and were not made in this environment:

- actual monthly and immediate population/Deaths deltas;
- timer completion, cancellation, and failure behavior over elapsed game time;
- AI selection frequency and target choice under live campaign state;
- rendered Ledger layout, click behavior, state refresh, and scripted seal visibility;
- super-event audio playback and settings interaction;
- cross-save or reload persistence during long scenario transitions.

If engine-runtime execution becomes available, append observed results by scenario without replacing this static trace record. Until then, completion reporting must describe the scenario result as static/readback evidence only.

## Simplifications, omissions, and blockers

No fallback or unapproved simplification was used. Optional Ledger frame animation is explicitly queued and is not a missing current-scope dependency. The only validation gap is the absence of engine-runtime scenario execution in this environment; the parent owns the final completion disposition.
