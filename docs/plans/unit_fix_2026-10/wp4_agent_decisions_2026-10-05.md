# WP4 shared-unit repair decisions

Acceptance basis: the user assigned all nine WP4 models and every ticket in the supplied unit-fix plan.
The Event 039 decisions are recorded in `docs/plans/039_murder_mystery_plans/agent_decisions_2026-10-05.md`.

## Clone rifle firing

Use the ticket's discharge times in the existing attack, defend and support-attack actions.
Emit one rifle flash at 0.75 seconds in attack and at 1.0 seconds in defend/support attack.
Emit the bolt-action cartridge at 1.5833 seconds in attack and at 1.8333 seconds in defend/support attack.
The installed mesh already contains separate `muzzle` and `cartridge` locators.
Use the ticket's permitted `defend` successor for attack and support attack, and mark the opening shout `trigger_once`.
The installed attack and support actions fail the loop-seam gate; repeating those actions would retain their discontinuity.
The already registered defend action passes its loop gate and receives the matching rifle discharge events.
Actual attack recovery, entry and grip repair remain separate acceptance requirements; event wiring does not prove them.

## Robot firing

Emit the vanilla flash and smoke systems only at the first existing discharge for each gun/burst.
Attack uses left 0.6667 seconds and right 0.7917 seconds; support attack uses left 1.0 seconds and right 1.125 seconds; defend uses left 0.75 seconds and right 2.75 seconds.
Remove the repeated impulse systems and their `keep_particle` flags.
The desired recorded audio has a long burst for attack/support attack and a short burst for defend, with one sound event per gun/burst.
Audio is promoted only when its source provenance and mastering gates pass.

## Energy weapons

Remove `keep_particle` from the Portal Raider and Alien Infantry laser discharge events while retaining their existing weapon nodes and times.
Energy weapons do not eject brass cartridges.
A pistol-up scan is a non-firing defend action unless an actual discharge is authored and measured.

## Dependency handling

The connected session exposes no HOI4 reference or validation MCP tools; relevant local wiki and installed entity/particle/sound sources are read directly and hash-bound in the package evidence.
The requested `unit_s3_report.md` is absent; the section 3 owner's `pipeline_report.md` and per-model delivery reports provide the existing delivery baseline.
An occupied live Blender scene belongs to its active worker and is never replaced by WP4.
No synthetic motion, automated weights, invented texture detail or generated sounds may hide an unresolved authoring or source gap.
