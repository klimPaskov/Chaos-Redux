# Event 31 mission cleanup parser repair

The launch 09 log reports eight unsupported `cancel_mission` calls in `random_terror_clear_country_commitments`, repeated in two parser passes.
The parent changed those eight effect names to `remove_mission` and preserved every mission identifier and subsequent cleanup command.
All eight identifiers are defined in `common/decisions/031_random_terror_missions.txt`.
The helper's two callers perform country recovery and terminal country cleanup.

Installed `documentation/effects_documentation.md`, under `remove_mission`, explicitly specifies country scope and removal without running completion or timeout effects.
The offline Effects page documents the same mission-removal command.
Vanilla decision files including AST.txt use this effect.
This matches cleanup without issuing a success reward or timeout penalty.

The immediate original is preserved under `pre_patch_event31_mission_removal/common/scripted_effects/031_random_terror_effects.txt`.
Reversing the eight exact keyword substitutions reproduced the entire original file byte for byte.
Post-patch SHA-256: `2e096c1ab7ab6342d1647408e1852277467416a4f211ff315e05f4770f8d1be2`.
The narrow Event 31 MCP trace was partial, with helper expansion deferred; it does not establish mission runtime acceptance.
The next launch must confirm the original errors disappear, and live recovery/terminal cleanup must verify that active missions close without rewards or timeout effects.

Two similarly named Event 33 legacy-migration calls remain outside this repair because their caller scope needs separate review.
