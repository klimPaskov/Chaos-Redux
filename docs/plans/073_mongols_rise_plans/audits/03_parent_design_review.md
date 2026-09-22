# Parent design review

## Review identity

This review was performed by the same assistant that wrote the planning package. It is not an independent subagent audit. No game implementation, native render, or live test was available. Findings below concern the written design and internal consistency.

## Findings addressed in the written baseline

| Finding | Change made | Remaining proof |
|---|---|---|
| A huge opening army could destroy itself through supply congestion | Separate total entitlement from safe immediate deployment, preserve a visible reserve and require actual reception testing | Live map and supply calibration |
| Upgrades could replace casualties for free | Use cumulative claimed entitlement, not surviving division count | Actual grant and reload tests |
| Changing scale factors could make an upgrade shrink or duplicate its grant | Freeze the occurrence's division scale basis at acceptance | All scaled tier transitions |
| Formation equipment and spare equipment could be counted twice | Separate formation requirements, spare reserve, and later transfers | Actual template-derived ledgers |
| Cavalry normal-army wording could be expanded into an unsupported universal designer ban | Define required recruitment, rewards, modifiers, AI and qualification precisely, require truth about any stronger restriction | Supported category and control bindings |
| Late support branches could remove the event's defensive weakness | Keep the defensive budget persistent and test combined effects after all routes | Measured full-stack stats |
| A focus tree could delay the first war for years | Keep the two short opening anchors and let development proceed alongside conquest | Actual early campaign timing |
| Regional routes could become identical annexation ladders | Give China industry, Central Asia connection, the Rus a western military partner, Persia administration, Europe industrial resistance, and southern routes different terrain problems | Regional playtests |
| Succession could become random punishment | Tie it to a real vacancy and prior commitments, provide caretaker and negotiated outcomes | Character lifecycle and crisis tests |
| Collapse could erase the player's campaign | Preserve meaningful successors, surviving forces, and a recovery route | Actual release and army allocation tests |
| More systems could create a crowded interface | Keep two public meters, four spendable click-cost types, at most six primary actions and three missions | Native UI fixtures |
| Repeated peace, release, or recapture could farm rewards | One-time settlement records, distinct anti-farming history and sustained containment conditions | Adversarial tests |
| Generic war and annexation Chaos could be charged again | Separate generic sources from event milestones and coalesce overlapping power milestones | Actual Chaos ledger |
| A historical site could be replaced with an arbitrary capital state | Make exact Karakorum relocation an explicit map capability gate | Local map and capital-effect proof |
| Media directions could be copied into final localisation | Keep all labels provisional and require research before final super-event text and audio | Source and rights review |

## Coverage assessment

The written baseline includes the opening, cavalry identity, offensive and defensive profile, three political paths, shared development routes, all requested expansion directions, four regional packages, tribute, Karakorum, connected routes, three Evolutions, succession, collapse, recovery, AI, multiplayer, presentation, achievements, and production requirements.

Path-level focus planning is intentional. Final IDs, coordinates, and a fixed focus count would be premature without native layout and source binding. The broad regional state sets remain semantic targets until mapped.

## Open design and implementation risks

The army-size anchors could be too large for the actual supply map. Category-specific modifiers may not support every desired distinction. A precise capital move may require approved map work. Some tribute types may need a narrower supported agreement. Character and tag identities need local inventory and research. Custom mounted model source eligibility may be difficult to satisfy under the supplied rules.

These risks are not marked resolved by writing a handoff. They are assigned to implementation-stage gates and the relevant role prompts.

## Mandatory remaining review

The actual `chaosx_improvement_loop_planner` review remains blocked by unavailable collaboration tooling in this conversation. Focus, decision, AI, country, localisation, asset, and completion roles also remain unexecuted. The package contains their tasks and expected evidence, not fabricated findings from those roles.
