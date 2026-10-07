# Riches Found railhead connection contract

Open the Railhead's land route uses a concrete connection between the mine and its current controller's capital.
An infrastructure spur or a previous controller's `riches_found_railway_laid` marker is not proof of that connection.
This bounded repair addresses the old mission result that awarded full success before its railway helper could reject an unbuildable route.
The acceptance basis is Part 3's objective to complete the valid transport connection while retaining control and supply.
It does not waive the remaining supply and sea-route proof requirements.

## Land-route transaction

The new STATE predicates use CONTROLLER as the country network scope, PREV as the mine endpoint and `THIS.capital` as the destination inside that country scope.
The same `build_only_on_allied = yes` restriction is used for buildability, construction and connection verification.
Only state endpoints are supplied, so no native fallback-to-another-path-option field is needed.
If the mine is itself the capital state, it is already at the delivery destination and needs no artificial zero-length railway.
An existing connection is reused instead of increasing it repeatedly.
A missing controller or an impossible land connection fails preflight.

At resolution, `riches_found_lay_mine_railway` builds only if no current connection exists and the native `can_build_railway` predicate permits those exact endpoints.
It records the historical laid marker only after `has_railway_connection` confirms the result.
The native mission then checks the connection again before calling `riches_found_complete_mission`, awarding full development/order results or marking railhead success.
Only a currently active railhead-kind subject is resolved.
The post-build success branch also rechecks progress, route capacity, damage and development rather than trusting the earlier availability frame.
If those checks fail, the resolution records partial state and the existing partial development/pressure consequence without incrementing the success/achievement counter.
The partial branch releases the live mission target and active/cleanup markers while retaining its explicit result.
The ordinary cooldown and subject cleanup still occur in the original controller's bounded mission consumer.

The existing port branch is retained as a separate planned route, not substituted for an impossible railway.
Its current port/route checks do not prove convoy delivery, blockade conditions or uninterrupted supply.
Those are open acceptance requirements and this repair does not claim the complete mission package is verified.

## Evidence and limits

Installed `documentation/triggers_documentation.md:4603-4627`, revision `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29`, documents actual railway connections and endpoint parameters.
The revision-bound MCP detailed read completed for that section.
Installed `documentation/effects_documentation.md:2535-2577`, revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`, documents native building and allied-ground pathing.
Offline `Triggers - Hearts of Iron 4 Wiki.md:1867-1868,1961-1985`, revision `abc51ad18a2c46e46d47baa795c5a840ebaf7c4ae3e777426c64a9f4c0c0ce06`, supplies state endpoint examples.
Installed `common/decisions/PHI.txt:2019-2027` provides a native country-perspective connection check from nested state scopes using PREV and PREV.PREV.

The main agent's explicit STATE-to-CONTROLLER validation snippet returned `SCRIPT_CHECK_PARTIAL`, `valid = null`, with command-kind/scope support and two unchecked native argument blocks.
It is not a parameter or engine validation pass.
The bounded map lookup inspected state 64 under revision `cac07d131e687e71d6d640989d18ab7d5fc342fae7cf83196badd0fc066fdbbb` and returned `MAP_LOOKUP_COMPLETED`.
Its artifact SHA-256 is `0b97172f00bf8aff033b8551d1c5f7cb5dacfb274f3049bda42a3fefb33d9f46`, with lookup-only coverage, one inspected state and no full map validation.
That is map/source inventory evidence, not a successful campaign railway or supply test.
The dedicated decision/mission audit verified the owner fixes for timeout identity/result cleanup, conditional partial text and the three-value inline rows in its follow-up dispositions.
Timeout partial/failure results now clear the live mission markers before orphan recount, preserving their matching generic result instead of turning them into cancellations.
The audit retains the sea-supply, current decision-AI and native visual-fit evidence gaps.

## Files, presentation and remaining work

The predicates live in `029_riches_found_rail_triggers.txt`, construction in `029_riches_found_works_effects.txt`, and the native mission in `029_riches_found_decisions.txt`.
The mission tooltip is conditional and does not announce success before construction verification.
It retains the existing mission icon and category; no new asset or GUI is introduced.
Frozen sources and byte-verified atomic-write backups are under `docs/plans/029_riches_found_plans/evidence/2026_10_07_rail_connection_before/`.
Future accepted integration must prove actual supply and sea-route delivery using a documented narrow predicate or report the missing hook, not turn route flags into claimed physical evidence.
No agent launched HOI4 and no Event029 completion is claimed.
