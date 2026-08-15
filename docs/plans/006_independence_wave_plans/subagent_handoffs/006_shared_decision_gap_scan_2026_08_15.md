# Event 006 shared decision gap scan — 2026-08-15

> Superseded current-source note (2026-08-15): the former DM-62 threshold decision was resolved by `006_dm62_charter_war_mandate_factory_gate_2026_08_15.md` and commit `934405954`. The live DM-62 `available` and `custom_cost_trigger` now use `can_pay_independence_wave_diplomatic_standard_factory_cost`; the historical no-safe-gap wording below remains the pre-repair audit record.

## Disposition

`NO_SAFE_SOURCE_GAP_FOUND — read-only audit.`

This scan reviewed the current shared Event 006 decision source, accepted decision-cost localisation, lifecycle/cancellation guards, and the recent factory-bearing cost-selector repairs. No gameplay, localisation, central-admission, Join, workbook, or asset files were changed.

## Current source evidence

The mandatory probability discovery pass for `common/decisions/006_independence_wave_decisions.txt` with the `decision_ai_will_do` adapter returned `PROBABILITY_SOURCE_INSPECTED` with source revision `3a9d424d51cc295428f065c9bcac5891725e664cdabc2cbb984f5fa8c9f0e8de`, source hash `f3ca7964920cfba2aa2a560df782f65d0e9ff44e221fa0ffd4b28fce2de6b942`, ten candidates, zero available candidates, 79 required inputs, and zero inspect-unresolved inputs. The artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/21bdc79d0345a348772496be977abde788dd540adab9db0b9490846582160bfa/626ed6abd9834d2958260fe161aa2d863b9ea401a8d813a225a4fb4225cc76da/probability-inspect-f3ca7964920c.json`.

The previously identified factory-bearing disclosure gaps are already owner-applied: `independence_wave_coordinate_recognition_campaign` and `independence_wave_request_collective_recognition` select `independence_wave_cost_diplomatic_standard_factory` while reserving the light civilian-factory amount, and the HBX federal asset-ledger decision uses the matching factory-bearing diplomatic selector. Their shared localisation triplets are present in `006_independence_wave_decisions_l_english.yml`.

The remaining shared decisions use the established cost families whose visible text matches their modifiers: administration light/standard/major, strategic/strategic-major, security, integration, border ultimatum, corridor, rescue aid, safe reserve, and breakaway sponsorship. No additional selector-versus-modifier mismatch was proven by the current source scan.

## Lifecycle and design boundary

The shared mission and decision families retain their existing setup, active-project, generation, origin-ended, capital-control, and cleanup guards. The accepted DM-01 design conflict remains an owner decision between the accepted garrison-only/no-click interpretation and a material equipment/supply/train commitment model; this scan does not invent costs or convert the passive founding mission into a selectable decision. The typed probability pool is incomplete and has no available candidates, so no ranking, timing, balance, or AI behavior claim is made.

## Parent follow-up

The next meaningful Event 006 progress remains package admission and evidence work, not a mechanical central-list edit. IW-048 UDM, IW-051 YAK, IW-052 BYA, IW-053 ALT, and IW-054 KHA remain package-local or fail-closed on identity, portrait, flag, host/origin, map, or typed-probability gates. Preserve the current central authority boundary and do not widen attestation, preflight, scenario, or Join surfaces without a complete independent package packet.

## Re-audit addendum — factory affordability gate considered and rejected as unsafe

The scan checked one remaining source-level candidate rather than treating the recent selector repairs as a complete gate audit: DM-62 `independence_wave_request_charter_war_mandate` now displays the factory-aware triplet and applies a light factory burden, but its decision-level `available` and `custom_cost_trigger` still call the shared diplomatic-only helper.

Exact evidence is `common/decisions/006_independence_wave_decisions.txt:2923-2926`, where both predicates call `can_pay_independence_wave_diplomatic_standard_cost`, followed by `custom_cost_text = independence_wave_cost_diplomatic_standard_factory` and `civilian_factory_use = @CR_SC_INDEPENDENCE_WAVE_DECISION_COST_CIVILIAN_FACTORY_LIGHT`. The helper at `common/scripted_triggers/006_independence_wave_decision_triggers.txt:249-255` checks only Command Power and convoy-or-train stockpiles. It does not check `num_of_civilian_factories_available_for_projects`.

The player-facing triplet at `localisation/english/006_independence_wave_decisions_l_english.yml` says the action requires the light civilian-factory amount, and the accepted matrix explicitly requires “diplomatic-standard cost and one civilian factory” for DM-62 at `docs/specs/006_independence_wave_specs/matrices/006_decision_mission_map.csv:63`. The existing payment helper at `common/scripted_effects/006_independence_wave_decision_effects.txt:180-195` correctly spends only the Command Power and convoy-or-train part because `civilian_factory_use` is a timer burden, not a complete-effect subtraction.

Vanilla precedent confirms that a factory-bearing decision owns a matching capacity predicate: `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/decisions/CZE.txt:3939-3954` pairs `civilian_factory_use = 1` with a factory-count custom-cost trigger, and `AUS.txt:1887-1896` puts the factory-count condition in `available` before applying `civilian_factory_use = 2`. The offline Decision Modding page also states that custom cost text only controls the displayed cost state and that timer modifiers are applied during the decision timer (`paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md:299-327`).

This is not promoted to a safe patch in this bounded scan. A local DM-62 predicate would need an owner decision about the intended integer threshold: `> 0` matches the matrix’s exact one-factory availability, while `> constant:independence_wave_decision_cost.civilian_factory_light` matches the shared Event 006 strict-reserve convention but requires two available project factories for a one-factory modifier. Editing the shared diplomatic helper would incorrectly add a factory requirement to non-factory diplomatic decisions such as DM-29, DM-31, DM-32, DM-38, DM-40, and other callers. Choosing either threshold therefore changes availability and balance, so it is not a design-free patch under the current authority boundary.

Disposition remains `NO_SAFE_SOURCE_GAP_FOUND`. If the owner later confirms the exact threshold, the narrow implementation is to add that same factory predicate to DM-62’s `available` and `custom_cost_trigger` only, leaving the shared helper, payment effect, selector, modifier, lifecycle, cooldown, AI, localisation, matrix, and central admission unchanged. No source patch is recommended by this audit.

## Lifecycle, mission, and route review addendum

DM-62 has a complete targeted timed-decision lifecycle: `complete_effect` pays the diplomatic package and stores the active target, `remove_effect` publishes the authorization and applies the success ledger, and `cancel_trigger` plus `cancel_effect` clear the target and apply the bounded cancellation ledger at `common/decisions/006_independence_wave_decisions.txt:2929-2974`. No cancellation or stale-target asymmetry was proven. The shared DM-01 provisional-capital mission overlap remains the previously documented owner-review question and is not safe to alter from this audit.

The mission/decision surface is ordinary HOI4 decision UI rather than an Event 006-owned scripted GUI, so `hoi4.gui_inspect` and `hoi4.gui_render` were not applicable and no GUI source was touched. The current source has no newly introduced decision-owned GUI surface.

The direct MCP probability discovery passes both completed with `PROBABILITY_SOURCE_INSPECTED` against source revision `3a9d424d51cc295428f065c9bcac5891725e664cdabc2cbb984f5fa8c9f0e8de`: `decision_ai_will_do` reported ten candidates, 79 required inputs, zero available candidates, and zero inspect-unresolved inputs at `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/21bdc79d0345a348772496be977abde788dd540adab9db0b9490846582160bfa/626ed6abd9834d2958260fe161aa2d863b9ea401a8d813a225a4fb4225cc76da/probability-inspect-f3ca7964920c.json`; `mission_ai_will_do` reported 54 candidates, 42 required inputs, zero available candidates, and zero inspect-unresolved inputs at `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/351b89a50ae7f5a6f604e6155e7eb4364a540b030e21442f05126c9203aaab07/f93f0d7beeddc37da0e36b385c987021f0eeeb722e48bf8320300fc5f314fd9c/probability-inspect-f3ca7964920c.json`. These are structural receipts only because `poolComplete=false`; no balance or AI ranking claim is made.

No gameplay, localisation, scripted trigger/effect, decision, central-admission, Join, asset, workbook, or GUI file was changed. The only file touched by this resumed audit is this documentation handoff.
