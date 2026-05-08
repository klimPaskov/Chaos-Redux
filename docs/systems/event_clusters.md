# Event Clusters

## Overview

Event clusters are a layer above the normal random-event picker. The picker still selects an individual event first. If that event belongs to a cluster, the cluster system can roll to fire a linked sequence instead of only the selected event.

The current registered cluster is **Wars** (`constant:event_cluster_id.wars = 1`). Its theme is sudden wars and armed conflicts between countries, where local disputes, opportunistic attacks, and border shocks can turn into a wider chain of fighting.

## Runtime Flow

1. The daily event timer selects a normal event through existing weighted selection.
2. `fire_event_by_temp_id` checks whether the selected event belongs to a cluster.
3. If the selected event has a cluster, the system checks cluster type, unlock tier, cooldown, member availability, and the chaos-scaled cluster roll.
4. If the cluster fires, valid members are ordered by danger and placed into a country-scoped pending queue.
5. The first queued member fires immediately through `fire_event_by_temp_id_no_cluster`, so normal event accounting, history logging, weight reduction, and cooldown behavior still apply.
6. Later queued members fire from `chaosx.event_clusters.2` after tier-scaled random cooldowns.
7. If the cluster does not fire, the selected event fires normally.

Manual event triggering uses `fire_event_by_temp_id_no_cluster` directly. Cluster triggering has its own settings UI path through `trigger_selected_event_cluster`, which force-fires a known cluster instead of using automatic availability checks.

## Tuning

Cluster tuning lives in:

- `common/script_constants/event_cluster_constants.txt`

Important constants:

- `event_cluster_id.wars = 1`
- `event_cluster_wars.unlock_tier = 1`
- `event_cluster_wars.cooldown_days = 120`
- `event_cluster_roll.minimum` and `event_cluster_roll.maximum` define the shared percentile roll range
- `event_cluster_roll_chance_default.*` defines tier-based cluster roll chance
- `event_cluster_member_participation.*` defines member participation chance
- `event_cluster_member_order.*` defines random order scoring between danger bands
- `event_cluster_member_cooldown_min.*` and `event_cluster_member_cooldown_max.*` define delay ranges between queued members

The default tier roll chances are 5% at Calm World, 10% at Gathering Storm, 15% at Rising Chaos, 25% at Chaos Tier, 35% at Totalen Chaos, and 50% at World Collapse. A cluster that is still locked by chaos tier displays `N/A` for its roll chance.

The cluster roll and member participation roll are separate. A selected member can cause the cluster roll, while each optional member still rolls its own participation chance. Required members fire when valid.

## Member Order And Cooldown

Member events do not all fire at once. A cluster stores fired members in a pending queue and processes them one at a time.

Danger controls the queue order:

- Low and medium danger members are mixed with weighted random scores. Low danger normally sorts before medium danger, but the order is not fixed.
- High danger members are queued after low and medium members.
- Severe danger members are queued after high danger members.
- Members with the same danger level use random scores, so the exact order can vary between cluster firings.

Cooldown between queued members shortens as chaos increases:

- Calm World: 5-10 days
- Gathering Storm: 5-8 days
- Rising Chaos: 4-7 days
- Chaos Tier: 3-6 days
- Totalen Chaos: 2-5 days
- World Collapse: 2-3 days

## Event Log Integration

Cluster history is stored separately from normal event history:

- `global.events_log_cluster_*` arrays store cluster rows.
- `global.events_log_cluster_member_*` arrays store member event status and danger.
- The event log has a **Clusters** tab with the registered cluster catalogue.
- The catalogue supports filter, sort mode, and sort order controls. Cluster filters are `All`, `Available`, `Unavailable`, `Enabled`, and `Disabled`.
- Opening a catalogue row shows the current cluster details, readiness, roll chance, enabled state, and member availability.
- Fired cluster rows appear in the **History** tab and open the same cluster details window with the historical member results.
- Clicking a member row opens that member's normal event details.
- The cluster details window sorts member rows by danger level from lower danger to higher danger.
- Cluster rows and details include a checkbox that enables or disables automatic cluster firing. The trigger button in cluster details force-fires the selected cluster.

The cluster log records the cluster even though member events still appear in normal history. This lets the player see both the broad incident and each event's normal accounting.

## Settings Integration

The settings window has an Event Clusters view under Trigger Events. It lets the player:

- select a cluster ID
- inspect name, type, unlock tier, current tier, roll chance, member count, and status
- manually trigger the selected cluster

The manual trigger button is always clickable in the Event Clusters view. Manual triggering bypasses tier, cooldown, disabled-state, and member availability checks. The result line reports whether the selected cluster fired, is unknown, or failed because runtime setup could not build the required scopes.

## Icons And Assets

No new final art assets are required for the current implementation.

Existing assets used:

- Settings controls: existing `GFX_chaosx_add_one`, `GFX_chaosx_subtract_one`, `GFX_chaosx_text_bg_60`, and `GFX_chaosx_button_123x34`
- Event log buttons and flags: existing Chaos Redux event-log UI sprites

If a future cluster needs a dedicated icon, define the sprite in an `interface/...gfx` file first, then place the DDS under the matching `gfx/interface/...` folder.

## Files

- `common/script_constants/event_cluster_constants.txt`
- `common/scripted_effects/chaosx_event_cluster_effects.txt`
- `common/scripted_effects/chaosx_settings_effects.txt`
- `common/scripted_guis/chaosx_scripted_gui_settings.txt`
- `common/scripted_guis/chaosx_scripted_gui_events_log.txt`
- `common/scripted_localisation/chaosx_scripted_localisation_settings.txt`
- `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`
- `events/chaosx_event_clusters.txt`
- `interface/chaosx.gui`
- `interface/chaosx_events_log_popup.gui`
- `localisation/english/chaosx_gui_l_english.yml`

## Future Plans

- Add more Wars members, such as border incidents, faction breakups, and regional war chains.
- Add non-war clusters for economy, disasters, and anomalies.
