# Event 006 host-facing crisis mission audit — 2026-07-28

## Status: HOLD

The host-facing crisis has a sound controller, queue, timeout, ownership, and coordinator architecture, but two player-facing mission defects must be resolved before static PASS.

No gameplay files were changed by this read-only audit.

## Blocking findings

### High — selecting the mission hides its own category and timer

`independence_wave_crisis_category.visible` is only `can_independence_wave_open_crisis` in [common\\decisions\\categories\\006_independence_wave_crisis_categories.txt](C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\common\decisions\categories\006_independence_wave_crisis_categories.txt:8).

The selected mission immediately sets `independence_wave_crisis_active` in [common\\scripted_effects\\006_independence_wave_crisis_effects.txt](C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\common\scripted_effects\006_independence_wave_crisis_effects.txt:11), while `can_independence_wave_open_crisis` explicitly requires that flag to be absent in [common\\scripted_triggers\\006_independence_wave_crisis_triggers.txt](C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\common\scripted_triggers\006_independence_wave_crisis_triggers.txt:28).

Category `visible` is continuously evaluated, so the category becomes hidden as soon as its selectable 120-day mission begins.

The mission continues and can still queue a synchronized wave, but the player cannot see its timer or cancellation state.

The offline decision reference says category visibility gates the whole selection surface, and vanilla categories retain visibility through active-mission branches, for example `CHI_avoid_another_crisis_cat` in `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\decisions\categories\CHI_decision_categories.txt:492`.

Recommended local patch: make category visibility an `OR` of `can_independence_wave_open_crisis = yes` and `has_active_mission = independence_wave_open_host_crisis`.

### Medium — the available cost gate omits command power that the mission deducts

`independence_wave_open_host_crisis` advertises and deducts standard command power alongside manpower, Army Experience, infantry equipment, and support equipment in [common\\decisions\\006_independence_wave_crisis_decisions.txt](C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\common\decisions\006_independence_wave_crisis_decisions.txt:17) and [common\\scripted_effects\\006_independence_wave_crisis_effects.txt](C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\common\scripted_effects\006_independence_wave_crisis_effects.txt:11).

Its `can_pay_independence_wave_crisis_cost` delegates to the shared security-standard payment trigger, which checks manpower, Army Experience, infantry equipment, and support equipment but not command power in [common\\scripted_triggers\\006_independence_wave_decision_triggers.txt](C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\common\scripted_triggers\006_independence_wave_decision_triggers.txt:253).

The player and AI can therefore select the mission without the command power represented in its custom cost text.

Recommended narrow patch: add `command_power > constant:independence_wave_decision_cost.command_power_standard` to the crisis-specific payment trigger rather than broadening this audit into a shared security-cost redesign.

## Verified mission lifecycle

| Field | Evidence | Result |
| --- | --- | --- |
| Owner and category | Any host country, `independence_wave_crisis_category` | Correctly host-facing and not limited to existing Event 006 countries |
| Pressure trigger | Stability below 35% or a controlled state not owned by ROOT above 50 resistance | Correct country and state scope |
| Mission type | `activation`, `selectable_mission = yes`, custom cost, `days_mission_timeout`, `complete_effect`, `cancel_trigger`, `timeout_effect` | Valid vanilla mission structure |
| Duration | 120 days through `independence_wave_crisis_timing.mission_days` | Centralized and unchanged |
| Timeout success | Still-pressured, resettable coordinator sets one global queue flag, sets requester receipt, applies cooldown, clears runtime flags, and calls `chaosx.nr6.3` after one day | Correct normal-planner handoff |
| Cancel and blocked timeout | Missing pressure or a busy/invalid coordinator applies visible stability pressure and cooldown, then clears active/origin flags | Defined and no silent cleanup loss |
| Queue cleanup | `chaosx.nr6.3` clears the global queue and requester receipt on both the planner attempt and the reset-gate failure branch | Correctly bounded |
| Ownership | Crisis trigger/effect/decision sources contain no ownership transfer, annexation, release, or country creation effect | Correctly delegates all release work to the normal synchronized planner |
| Coordinator reset | Checked when category opens, at timeout queueing, and again in `chaosx.nr6.3` | Correctly fails closed |

## AI, localisation, and exploit notes

The mission has pressure-sensitive AI weighting, with separate occupation and low-stability multipliers.

The AI numbers are raw `base = 1` and `factor = 2` values in [common\\decisions\\006_independence_wave_crisis_decisions.txt](C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\common\decisions\006_independence_wave_crisis_decisions.txt:28), which should be moved to the existing crisis constants file during the cost/visibility repair to preserve central tuning.

The category, mission, description, and custom cost localisation keys all resolve in [localisation\\english\\006_independence_wave_decisions_l_english.yml](C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\localisation\english\006_independence_wave_decisions_l_english.yml:230).

The queue is global and is guarded before selection, before timeout scheduling, and in the event consumer, preventing duplicate crisis releases.

No direct ownership, free-unit, equipment-farming, war-goal, or repeated-release exploit was found.

## Validation and uncertainty

Reviewed the accepted pre-wave crisis specification and source-of-truth map, offline decision-mission documentation, the vanilla category active-mission precedent, the shared coordinator reset trigger, all named crisis sources, `chaosx.nr6.3`, and the crisis localisation.

Read-only Event MCP evidence: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c05dcdf6b3651ea37d9b056020bc51f512c42119ee3eaab50ad328fb8a48c407/17c629aa94e08966150fd19db5b8668dbd6b5e670ecdf98cca11df601beb9e5a/event-impact-dbe4d677c869.json`.

The MCP report is partial because workspace-wide helper and lifecycle projections were deferred, so direct source traces above are the completion evidence.

Live mission timing, queue cleanup after save/load, AI selection, and allocator execution remain runtime HOLD items, as already recorded in the Event 006 source-of-truth map.

No decision-owned GUI change was in scope.
