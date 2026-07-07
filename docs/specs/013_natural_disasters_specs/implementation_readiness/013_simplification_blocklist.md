# Event 013 Natural Disasters, simplification blocklist

This blocklist names shortcuts that would violate the expanded specs. If any of these shortcuts becomes necessary, the implementation report must mark the feature incomplete or explicitly list the deviation as a simplification.

## Logic shortcuts that are not allowed

| Shortcut | Why it is blocked | Required alternative |
| --- | --- | --- |
| Reusing old Natural Disasters logic | The event was deleted and must be rebuilt as a fresh system. | Implement the reusable controller from the source specs. |
| Reusing old Earth Earthquake logic | The old logic is broken and the whole-earth rupture belongs in Event 013 Evolution III. | Keep Event 046 inactive and build fresh rupture logic inside Event 013. |
| One generic disaster event with swapped family name | The user required unique disaster-specific news, reports, remarks, and mechanics. | Preserve family-specific warning, impact, aftermath, report, news, modifier, AI, and chain routes. |
| Only random disaster calls | Other events must be able to trigger specific families and targets. | Build a direct call contract with family, target, severity, policies, and scaling overrides. |
| Direct callers copying damage logic | Copied logic will become stale and inconsistent. | Every caller routes through shared helpers. |
| Extra history rows for subevents | One Event 013 firing must create one Event 013 history row. | Record the sequence once and treat delayed subevents as sequence internals. |
| Immediate burst of multiple subevents | The event should feel like a delayed disaster sequence. | Use queue delays and compression rules. |
| Tiny baseline deaths | Baseline disasters must matter to the Deaths system. | Use family and vulnerability scaling that produces visible losses. |
| Mild Evolution II scaling | Evolution II must be materially more destructive and regional. | Scale through density, infrastructure, supply, devastation, stability, recovery weakness, and follow-up chains. |
| Cosmetic Evolution III | Abnormal disasters must be campaign-shaping when severity fits. | Add abnormal controller behavior, real damage, reports, GUI state, and super-event eligibility. |

## UI and decision shortcuts that are not allowed

| Shortcut | Why it is blocked | Required alternative |
| --- | --- | --- |
| Silent aftermath category | The affected country must reliably see that recovery is available. | Fire or refresh a visible notification with the report and category state. |
| Flat political-power recovery buttons | Disaster recovery should use concrete resources and tradeoffs. | Use equipment, fuel, trains, convoys, manpower, XP, stability, local support, supply, foreign relief, and timed objectives. |
| All recovery decisions visible at once | The category would become a debug menu. | Stage early, middle, and late recovery with caps and priority. |
| Human-only recovery | AI countries would remain broken after disasters. | Add AI equivalents and scripted recovery behavior. |
| No partial success | Disaster recovery would lose pressure and nuance. | Add success, partial success, failure, and degraded follow-up logic where mapped. |
| Static-only abnormal moving disasters | Moving paths need visual state for readability. | Use frame-sheet animation with static fallback for path and warning states. |
| GIF as final asset | HOI4 final animation should use a frame sheet. | Produce source frames, sheet DDS, static DDS, preview GIF, manifest, and GFX handoff. |

## Presentation shortcuts that are not allowed

| Shortcut | Why it is blocked | Required alternative |
| --- | --- | --- |
| Generic institution framing | The player should see specific disasters in specific places, not a generic system speaker. | Write family-specific, place-specific reports and news from observed effects. |
| News for every small late disaster | Later evolutions would spam the player. | Use severity, family, rarity, chain, abnormal, and global thresholds for news. |
| Research-gate text pasted into localisation | Planning files are direction-only. | Write final text during implementation after source research and localisation audit. |
| Unresearched quotes or cultural remarks | Super-event text must be real, verified, and source-documented. | Run the super-event text researcher and document confidence. |
| Placeholder or default super-event audio | Completed super-events need unique documented audio. | Run audio research, license checks, conversion, sound wiring, and documentation. |
| Automatic achievements | Achievements must reward difficult mastery or rare outcomes. | Implement disqualifiers, route checks, hard conditions, and icon variants. |

## Related-event shortcuts that are not allowed

| Shortcut | Why it is blocked | Required alternative |
| --- | --- | --- |
| Keeping Event 099 as a separate sandstorm disaster system | It duplicates the Event 013 family system. | Make it a placeholder or a narrow bridge into Event 013 dust and sandstorm calls. |
| Letting Event 013 heat stack with Event 051 | Event 051 remains separate. | Add a non-stacking guard and clear player-facing result. |
| Turning Event 013 into a world-end scenario | The brief says no world-end scenario for this event. | Keep Evolution III catastrophic but non-terminal. |
| Adding disaster relief tags or focus trees | Natural Disasters should pressure existing countries. | Use decisions, missions, reports, modifiers, AI, and GUI instead. |
| Super-event for every family | This would dilute meaningful super-events. | Reserve super-events for abnormal or rare massive moments. |

## Reporting rule

If an implementation uses any blocked shortcut, the final report must place it under simplifications, omissions, and blockers. Do not bury it inside a validation note or present it as complete.
