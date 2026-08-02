# Event 016 public-news milestones

Event 016 uses six minor news events to make already-recorded public milestones legible outside the active Directorate. They do not replace the event log, add a second character, advance a project, grant a unit, or create a new route.

| Event | Headline | One-time source receipt | Picture |
| --- | --- | --- | --- |
| `chaosx.nr16.304` | Public appointment | `brilliant_scientist_news_public_appointment_fired` | `GFX_news_event_016_brilliant_scientist_public_appointment` |
| `chaosx.nr16.305` | International recognition | `brilliant_scientist_news_international_recognition_fired` | `GFX_news_event_016_brilliant_scientist_international_recognition` |
| `chaosx.nr16.306` | First public breakthrough | `brilliant_scientist_news_public_breakthrough_fired` | `GFX_news_event_016_brilliant_scientist_public_breakthrough` |
| `chaosx.nr16.307` | Kruger State formation | `brilliant_scientist_news_kruger_state_formation_fired` | `GFX_news_event_016_brilliant_scientist_kruger_state_formation` |
| `chaosx.nr16.308` | First project-army deployment | `brilliant_scientist_news_project_army_deployment_fired` | `GFX_news_event_016_brilliant_scientist_project_army_deployment` |
| `chaosx.nr16.309` | Global containment coalition | `brilliant_scientist_news_global_containment_coalition_fired` | `GFX_news_event_016_brilliant_scientist_global_containment_coalition` |

The source effects dispatch each headline only after the corresponding state transaction commits. A two-day shared delay keeps a headline out of the same transaction frame while avoiding an autonomous scheduler. Public appointment is emitted only for the public compact posture; secret appointment remains local and intelligence-aware. International recognition, formation, and containment headlines reuse the exact thresholds and one-time super-event guards already owned by those systems. The breakthrough headline is emitted on the first resolved public Prototype, while the project-army headline is emitted after at least one historical project-force formation is materialized.

The six final news textures are event-owned black-and-white `397x153` DDS files under `gfx/event_pictures/016_brilliant_scientist/`. Their source masters, processed previews, contact sheet, checksums, and sprite handoff remain in the active `docs/assets/016_brilliant_scientist/report_news_expansion/` workspace until the parent completes runtime review. The six sprites are registered in `interface/016_brilliant_scientist.gfx`.

These are presentation-only news events, so they intentionally have no new Event Log or Event Details row. The existing log records the underlying appointment, breakthrough, recognition, formation, threat, and terminal state through their owning systems. No Event 016 model package is required by this surface; the project-army headline describes the existing causal formation ledger and does not substitute for the seven deferred generic unit-model packages.
