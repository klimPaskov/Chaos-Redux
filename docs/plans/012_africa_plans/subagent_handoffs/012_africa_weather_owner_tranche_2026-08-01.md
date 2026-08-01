# Event 012 weather-owner tranche — 2026-08-01

## Scope

This tranche closes only the owner-system gap around the existing Event 013 natural-disaster weapon actions 69 and 70. It does not add a tag, country, model, unit archetype, Event 013 source edit, or new persistent store.

## Runtime changes

- `common/scripted_effects/012_africa_achievement_effects.txt` now owns weather-war success, member-target disqualification, neutral-African-target disqualification, and ecological-wrath collapse.
- `common/scripted_effects/012_africa_action_effects.txt` calls the target classifiers only after Event 013 accepts the exact selected-country call. It checks the canonical wrath threshold after every weather backfire/rejection and after a high-chaos action failure.
- `common/on_actions/012_africa_world_order_on_actions.txt` records one distinct weather-marked hostile target and the weather-war milestone only when that target capitulates directly to the current host. Ordinary peace and third-party victories do not count.
- `common/scripted_triggers/012_africa_achievement_triggers.txt` documents that the owner gate opens from this exact host-capitulation receipt, while the completion trigger remains fail-closed until the live three-target proof exists.

## Acceptance and evidence

The target flag and host-generation receipt are written by the accepted Event 013 selected-country wrapper. Member classification uses current-generation membership or a cooperative Charter relationship. Neutral-African classification uses an African capital plus the outside relationship state. Wrath collapse uses `africa_achievement_ratio.ecological_rampage_threshold` after `africa_clamp_host_values`. The capitulation owner rejects stale target receipts after a host transfer by comparing the target generation with the winner's current `africa_host_generation`.

Static brace/quote scans report depth 0 and closed quotes for all touched scripts. Focused `hoi4.event_inspect` lint reports status `ok`, no blocking diagnostics, and a deferred workspace-wide analysis note. No in-game test was run.

## Remaining gate

The row remains `ACTIVE/BLOCKED`: a campaign must produce three distinct weather-marked hostile targets that each capitulate to the current host, without member/neutral-target/wrath/backfire disqualifiers or the existing high-chaos eligibility failures. The weather action and Event 013 public contract remain otherwise unchanged.
