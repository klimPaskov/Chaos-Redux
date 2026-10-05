# Event 008 Follow-Up Incident Improvement Addendum

Disposition: unresolved acceptance, with partial implementation evidence documented below.
The former `Accepted Design` heading supplied no independent user decision or parent acceptance record, so it is not an acceptance basis.
This reconciliation does not promote the addendum into accepted source design.
The parent owns design decisions and records them separately in `agent_decisions_2026-10-05.md`.

## Goal

Define bounded gameplay aftershocks for the delayed Tensions Rising report popups following repeatable Event 008 firings.

## Retained design claims with unresolved acceptance

- The ten delayed events `chaosx.nr8.2` through `.10` and `.12` are follow-up incidents, with `.11` deliberately unused.
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
- Unease Along the Frontier: extra world-tension pressure and chaos, retaining the `apply_tensions_rising_incident_calm_map` helper name and historical Calm Map Says Nothing design title.
- Insurance Rates Jump in Neutral Ports: shipping panic pressure while preserving the Insurance Market achievement hook.
- Rumour That Arrived Twice: two extra opinion-pair shocks.
- Staff Cars After Midnight: staff posture pressure and additional diplomatic damage.
- Fleets Keep Radio Silence: posture pressure plus a diplomatic shock.
- Border Lamps: Stage III+ border-war attempt plus heavier opinion damage.
- One Denial Too Many: heavier opinion damage and a Stage IV border-war attempt.
- Last Normal Briefing: strongest incident bundle, with the highest high-stage border-war chance.

## Documentation Impact

The Event 008 overview records real delayed pressure bundles and high-stage non-transfer border clashes.
The 2026-10-05 localisation handoff records concrete report/detail prose and qualitative consequence tooltips, pending parent review and rendered validation.

## Implementation evidence and remaining disposition

| Claim group | Disposition | Evidence and limitation |
| --- | --- | --- |
| Ten real incident bundles and no root recursion | implemented | `events/008_tensions_rising.txt:58` and `common/scripted_effects/008_tensions_rising_effects.txt:963`, reviewed in the release audit. This proves source behavior, without design acceptance or runtime delivery proof. |
| One selected follow-up per root | implemented | Scheduler dispatch is mutually exclusive in `common/scripted_effects/008_tensions_rising_effects.txt:776`. Each firing has one root report and at most one selected follow-up report, with no live `news_event`. |
| Adjacent safe state selection, non-transfer clashes, cooldowns, result callbacks | implemented | Source declarations and callbacks reviewed at effects lines 1124-1282 and event lines 254-292. Successful clash start/result behavior remains unobserved. |
| Delayed-stage enablement and terminal cleanup | unresolved | Release findings F1-F2 identify disabled gameplay and queued terminal-delivery gaps. Acceptance and reviewed owner fixes remain pending. |
| Broad incident reachability | blocked | Release finding F7 identifies branch shadowing. Probability owner's named scenarios and required MCP delivery are absent from the supplied evidence. |
| Source-design acceptance | unresolved | Historical heading and implementation existence do not establish approval. Parent/owner decision evidence is required. |

The [release audit](subagent_handoffs/event_completion_audit_2026-10-05.md) and [current source map](documentation_state_2026-10-05.md) retain the evidence boundary and unresolved findings.
No asset, gameplay, localisation, workbook, CSV, or other agent handoff was changed by this addendum reconciliation.
