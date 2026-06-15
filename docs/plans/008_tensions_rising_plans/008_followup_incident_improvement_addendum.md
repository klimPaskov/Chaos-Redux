# Event 008 Follow-Up Incident Improvement Addendum

## Goal

Repurpose the delayed Tensions Rising report popups into real gameplay incidents. They remain follow-ups to the repeatable Event 008 firing, but each visible popup must now apply a bounded mechanical aftershock instead of serving as flavour only.

## Accepted Design

- The delayed events `chaosx.nr8.2` through `chaosx.nr8.12` become follow-up incidents.
- Each incident recalculates the current Diplomatic Fever stage when it fires. If the world has dropped out of an evolved chaos tier before the delayed event arrives, the incident resolves as a Stage I aftershock.
- Every incident applies at least one real effect surface: additional distributed world tension, small chaos gain, extra timed opinion shocks, AI posture pressure, or a high-stage border-war attempt.
- Incidents do not recurse into `apply_tensions_rising_event_effect`. They use lighter helper bundles so one Event 008 firing cannot schedule another full Event 008 firing.
- Border-war incidents are limited to Stage III+ and use true `start_border_war` effects between adjacent owned-and-controlled states.
- Border wars must be non-transfer clashes: `change_state_after_war = no`.
- Border-war candidates must be independent, non-capitulated, non-zombie, not in civil war, not already at war, not already in a border war, not subjects, not faction partners, not recent border-war actors, and have a small fielded army.
- Border-war attempts are gated by global and per-country cooldowns. If no safe adjacent pair exists, the incident still applies its other pressure effects.
- Border-war callbacks add small political and war-support consequences so the result has state beyond the combat itself.

## Incident Roles

- Telegram Nobody Signed: light world-tension and opinion aftershock.
- Embassy Side Doors: opinion aftershock plus a small AI posture nudge.
- Calm Map Says Nothing: extra world-tension pressure and chaos while the cap no longer tells the whole story.
- Insurance Rates Jump in Neutral Ports: shipping panic pressure while preserving the Insurance Market achievement hook.
- Rumour That Arrived Twice: two extra opinion-pair shocks.
- Staff Cars After Midnight: staff posture pressure and additional diplomatic damage.
- Fleets Keep Radio Silence: posture pressure plus a diplomatic shock.
- Border Lamps: Stage III+ border-war attempt plus heavier opinion damage.
- One Denial Too Many: heavier opinion damage and a Stage IV border-war attempt.
- Last Normal Briefing: strongest incident bundle, with the highest high-stage border-war chance.

## Documentation Impact

The Event 008 event docs, event-log details, evolution text, and popup localisation should describe delayed incidents as real aftershocks. Boundary wording should stop saying the event never starts a direct conflict, because high-stage follow-ups can start non-transfer border wars.
