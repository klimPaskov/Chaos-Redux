# Event 013 inbound-relief route gate re-audit

Disposition: The latest parent patch resolves both conditional gate risks from the first pass. The bounded source audit passes; this is not engine validation.

## Scope and files

Re-audited parent changes to `natural_disaster_route_inbound_relief` in `common/decisions/013_natural_disasters_decisions.txt` and `natural_disaster_can_route_inbound_relief` in `common/scripted_triggers/013_natural_disasters_triggers.txt`. The parent patch changes these two gate call sites/definitions; this audit changed only this handoff. Existing unrelated worktree changes were not attributed to this audit or reverted. No gameplay edits or commit were made.

## Findings

- Availability and the custom-cost trigger require `natural_disaster_can_route_inbound_relief = yes`. Availability and the completion guard also require the recorded state to pass `natural_disaster_state_has_recovery_card = yes`; completion rechecks both recovery-card validity and affordability before any debit or success receipt.
- The two conditional risks from the first pass are removed in source. The affordability trigger’s convoy branch requires the convoy flag and explicitly forbids the rail flag; its rail branch requires the rail flag and forbids convoy. Each branch checks the matching equipment, so zero route flags or both flags fail closed, while exactly one flag with adequate matching equipment passes and matches the completion effect’s debit. The route setup helper also clears both flags before setting the selected route.
- `natural_disaster_state_has_recovery_card` composes the open-card check (active aftermath flag, family/severity variables, and card state below `closed`) with exclusion of `natural_disaster_chain_only_card`. Thus a missing, inactive, closed/terminal, or chain-only recorded card blocks both availability and completion; the earlier open-but-chain-only classification caveat is resolved.
- The five charges and their values remain: manpower 2,500; one route transport (3 `train_equipment` or 8 `convoy_1`); fuel 1,200; stability −0.005; war support −0.010. The shared trigger uses strict-`>` floors of 2,499 manpower, 2 trains, 7 convoys, 1,199 fuel, 0.004 stability, and 0.009 war support, admitting exactly sufficient amounts and rejecting inadequate inventory/support. The debit expressions still reference the same price constants; the constants file is unchanged in the worktree.
- The route-success country flag, temporary route-status value, and state-scoped status update remain inside the same guarded completion branch, after the debits. No success receipt is written when the recheck fails.
- The player explicitly authorizes the five-spendable-type Event 013 price as an exception to the generic four-type cap. Treat it as accepted for this bounded audit, not as a redesign request; no cost or penalty adjustment is recommended.
- The decision’s AI block is unchanged by the scoped gate patch. No AI-weight or balance comparison was requested or performed.

## Issue list and bounded notes

No remaining gate defect was found in the reviewed source. The previously noted dual-route-flag and open-chain-only-card risks are resolved by the mutually exclusive route branches and recovery-card rechecks.

Lifecycle: the decision remains visible while inbound relief is active; selection requires a recorded recovery card, the exact single route, and affordability; completion repeats those checks. The related `natural_disaster_inbound_relief_mission` was not changed or fully quality-audited, so mission owner/category/region, duration, outcome, and duplicate risk remain outside this gate-only pass.

Cost and cognitive-load note: each route consumes five spendable types, with exactly one of trains/convoys; this is the user-authorized Event 013 exception stated above. No broader category action-density or displayed-cost texticon review was performed. The decision’s player-facing localization was not changed or re-audited. Cleanup and exploit review was limited to confirming that failed route/card rechecks produce neither charges nor route-success receipts; no unrelated lifecycle audit was performed.

AI and route-lock note: the exact route flag/inventory pairing blocks missing, conflicting, or underfunded route states. The decision AI block is unchanged; no AI validity or probability pass beyond this route gate was performed. No gameplay fix is recommended within the requested scope.

## Evidence and validation limits

Source review covered the focused current decision/trigger hunks, the recovery-card predicate, route-setup helper, and relevant constants. The decision gate and completion guard are around lines 4549–4594; `natural_disaster_can_route_inbound_relief` is around trigger lines 1535–1554; `natural_disaster_state_has_recovery_card` is around lines 460–463 and its open-card dependency around 605–610; route flag setup is around `common/scripted_effects/013_natural_disasters_effects.txt:6841`. Prices/floors are in `common/script_constants/013_natural_disasters_constants.txt` around lines 1028–1138. Offline wiki references consulted: `Decision modding`, `Triggers`, and `Effects` (alongside the repository-required core pages). Vanilla precedent: Afghanistan decision in `common/decisions/AFG.txt` around lines 1714–1745 pairs an equipment requirement, matching custom-cost trigger, and manual completion debit. Official vanilla trigger/effect documentation was also consulted.

The available HOI4 MCP tool inventory exposes no decision/mission-specific inspect or render route (zero decision/mission route matches), so no decision scenario evidence is available. The category has no scripted-GUI attachment; GUI inspect/render is inapplicable to this logic-only gate. Probability MCP routes exist, but no probability comparison was run because the AI weight is unchanged and this review is gate-bounded. The game was not launched and no logs were requested or searched; source review is not presented as engine validation. No additional gate hardening is recommended within scope.
