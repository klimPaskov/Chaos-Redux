# Chaos Warfare achievements

Thirteen achievements have active gameplay definitions.
Two accepted achievements remain blocked rather than using weaker substitutes.
The shared registry is `common/achievements/chaos_redux_achievements.txt`, with CBRN condition predicates, tuning and tracking in `common/scripted_triggers/cbrn_achievement_triggers.txt`, `common/script_constants/cbrn_achievement_constants.txt` and `common/scripted_effects/cbrn_achievement_effects.txt`.

## The Air Is Still Breathable

A confirmed chemical attack during a war marks the victim's current major opponents through targeted war flags.
A new war relation clears both pair-specific flags, so an earlier conflict cannot qualify another war.
A major opponent's capitulation credits its eligible surviving enemies and the eligible winning country only when they carry that current-war flag.
Existing protection refreshes and received-attack checks disqualify military protection below 75% during the chemical war.
Completion requires military protection still at least 75%, less than three contamination points from the country's own accepted chemical releases, no offensive first use, no strategic civilian attack and no doomsday use.
The major-capitulation milestone follows the package's established major-war victory contract, and does not claim that every remaining participant has signed a peace treaty.

## The Antidote Arrived

An eligible victim opens a state-owned episode on its first nerve-agent release with at least 75% effective protection for soldiers and civilians, researched advanced masks, and actual advanced or sealed masks issued to both groups.
The episode must reach Severe or Catastrophic contamination during nerve-agent exposure, receive medical care and decontamination, then reach zero chemical contamination without losing control of the state.
Protected hospitals and utilities or a real active Mass Antidote Response satisfy medical care.
Real field decontamination coverage of at least 50% or a completed state cleanup satisfies decontamination.
Every chemical release while the episode is open adds its initial civilian deaths and military loss fraction, including releases of other agents.
Continuing chemical deaths also count, using the shared death helper's caller-initialized output.
One thousand civilian deaths or one percent summed military loss fails the episode.
A later underprotected nerve attack also fails it.
A failed episode cannot restart while the contamination remains, preventing repeated attacks from resetting its loss total.
A controller change invalidates it.
Cleanup credit lives inside the exact state contamination-delta owner, avoiding reliance on helper-local outputs after return.
Natural expiry closes the episode only if the other response conditions were met.
Disabled civilian death accounting cannot open a qualifying episode.

## Clean Hands, Dirty Work

The achievement requires covert biological operations over a long period without disclosure, a cover-up, strategic civilian release or doomsday release.
`cbrn_achievement_covert_discovered_history` is set when a covert route is probably or certainly attributed.
`cbrn_achievement_covert_coverup_history` is set when a cover-up is discovered.
`cbrn_convention_expose_covert_program` sets it when a covert convention program is exposed, and `cbrn_occupation_publish_coverup_discovery` sets it on the responsible country when an occupation cover-up is published.
Both flags are permanent campaign history and are never cleared.

## Blocked accepted achievements

No Wind Is Friendly requires an actual forecast failure and recovery of the affected army followed by a battle or campaign win without another chemical use.
The inherited candidate measured deterministic proportional friendly damage and later state capture, so it was rejected and preserved as review evidence in the plans handoff.
Unbroken Supply Corridor requires current supply for the exact assigned army and its completed offensive objective.
The installed unit-leader getters do not expose those facts, and national stocks, railways, supply modifiers and commander service are not substitutes.
Both remain accepted design with unresolved implementation, without an inferred exception.

## Presentation and hooks

The Air and Antidote achievement icons reuse their existing 64x64 completed, grey and not-eligible triplets under `gfx/achievements/`, registered as `GFX_achievement_chaos_warfare_air_still_breathable*` and `GFX_achievement_chaos_warfare_antidote_arrived*` in `interface/chaosx_achievements.gfx`.
Localisation lives in `localisation/english/cbrn_achievements_l_english.yml`.
All tracking uses existing exact chemical actions, protection refreshes, paid medical care, state cleanup, headquarters activation and narrow native callbacks.
Tracking adds zero report or news popups and no periodic world scan.

## Validation limits and further work

Source predicates and explicit state/country scope checks do not prove native damage counts, temporary-variable lifetime or event ordering.
The takeover status and specialist handoffs record the actual MCP coverage and the live acceptance cases.
Further work should expose genuine forecast-failure and assigned-army outcomes before completing the two blocked achievements.
