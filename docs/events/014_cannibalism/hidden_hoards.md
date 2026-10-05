# Event 014 hidden hoards

Status: implemented on 2026-10-04 (spec part 7, Larder integration: "hidden hoards can create warlord loyalty events").
Acceptance basis: the lead's delegated decision that hidden hoards are an accepted requirement, recorded with the design choices as agent decision D10 in `docs/plans/014_cannibalism_plans/agent_decisions_2026-10-04.md`.

## What it does

When a warlord answers the public reveal or a later absorption, its Larder ships to the unification host along the distance-scaled route described in [Larder logistics](larder_logistics.md).
A warlord with the hoarder personality, or one bargaining for autonomy, keeps part of that shipment back in a cache at its own capital.
The host notices the short count and must decide how to answer the warlord.
The CBL host can later investigate to locate the caches and, on the Break the Warlords route, send troops to seize a located cache.

## Step by step

1. Concealment. `cannibalism_prepare_current_warlord_concealment_share` sets the hidden share before the quote: 0.30 for a hoarder, 0.20 for an autonomy bargain, both together capped at 0.45 (`cannibalism_hoard` constants).
   `cannibalism_prepare_larder_transfer_quote` takes that share of the dispatch as `cannibalism_transfer_hoard_amount` when the donor's capital was captured, and only the rest travels and suffers the route loss.
   The donor still loses the full dispatch once; the host receives `(dispatch - hoard) x retention` once; the hoard is the third bucket.
   A cache below 20 Larder is not worth hiding and ships normally.
   The CBL and Wendigo constructors never set a share, so the opening host and the primary Wendigo donor conceal nothing.
   The absorbing and bargaining callers own the share and the cache amount before these helpers run, so both survive the helper return (`helper_output_ownership.md`).
2. Record. On a committed transfer, `cannibalism_conceal_current_warlord_hoard` writes the cache on the capital STATE: `cannibalism_hoard_amount`, `_owner` (the warlord country), `_owner_generation`, `_name` (the warlord's name index, kept for the event after the tag is annexed), `_host` and `_host_generation`.
   The host lists its cache states in the country array `cannibalism_hoard_states`.
   A second concealment by the same host's warlords at the same capital adds to the cache; a record from another host or an older host incarnation is replaced.
3. Review. `cannibalism_schedule_hoard_review` queues `chaosx.nr14.82` on the host one day later, one review at a time.
   The timed flag `cannibalism_hoard_review_pending` (30 days) prevents a second queue and expires if an event never fires.
   The event's immediate block (`cannibalism_select_next_hoard_review`) picks the first cache awaiting review and quotes the options.
4. Answer. The host chooses:
   - Confront: recovers 50 percent of the cache now (75 percent once the cache is located) and destroys the rest. A live autonomous governor gains 10 percent autonomy; otherwise the cache state, if the host owns it, gets Hoard Guard Unrest for 120 days, and the option says so only in that case. Unified authority +5.
   - Tolerate: the cache stays and is marked tolerated. A live governor loses 10 percent autonomy. Unified authority -3.
   - Bargain: pays Command Power equal to a tenth of the cache (5 to 40) and recovers 80 percent with no resistance. Hidden when the host cannot pay.
   - Write off: shown instead of the three answers when neither the host nor one of its subjects controls the cache state. The review says the stores are beyond reach, and the cache is closed with no recovery, no payment, no resistance and no authority change.
   Every answer checks control again when it is chosen, so a cache lost while the event was open is closed the same way and a bargain is never charged for it.
   Write off always closes a cache still on record, even one retaken while the event was open, because the host chose to write it off.
   After the answer the cache is marked reviewed and the next waiting cache is queued.
5. Investigation (CBL, after Audit the Submitted Hosts). `cannibalism_unified_investigate_hidden_hoards` costs 15 Command Power and 5 Army Experience (plus the hostility command surcharge) and needs an unlocated cache.
   It locates every unlocated cache and reopens its review, so each owner answers again with the higher located confront share.
6. Seizure (CBL, after Seize the Hidden Hoards). `cannibalism_unified_seize_hidden_hoard` targets a located, answered cache in a state controlled by the host or one of its subjects, costs 20 Command Power and 50 support equipment, and starts the 100-day mission `cannibalism_unified_hoard_seizure_mission`. One seizure runs at a time.
   - Success: two of the host's divisions stand in the state. The whole cache is recovered and unified authority +5. A tolerated cache still provokes mild resistance.
   - Partial: at the deadline at least one division is there. Half the cache is recovered and mild resistance follows.
   - Failure: no division. The cache is lost, severe resistance follows (20 percent autonomy for a governor, 240 days of unrest otherwise) and unified authority -10.
   - Cancellation: the cache record vanished, the host lost access to the state or the unified decisions closed. The cache stays located.
   Both decisions count as command operations and advance the command mission timetable.

## Interactions

- Larder: recoveries credit `cannibalism_larder` and finish with `cannibalism_clamp_and_publish_current_larder`, so capacity and the global mirror stay correct.
- Warlord dispositions: autonomy changes act on the governor's real HOI4 autonomy through `add_autonomy_ratio` with the reason "Hoard dispute"; the disposition itself is unchanged.
- Existing focus effects: the investigation flag still lowers the absorb Larder cost and adds a command contract point; the seizure flag still lowers the purge Larder cost and its risk flag raises purge hostility. The focus tooltips state both.
- Wendigo route: the transformed host records caches and answers reviews; authority lines are hidden because it has no unified authority meter, and the CBL-only investigation and seizure are not available to it.
- AI: review options use the unified decision AI levels (confront high, doubled on the break route or a located cache, halved against a governor at war; tolerate standard, doubled on the keep route or for a governor at war; bargain high, doubled on the chain route or with Larder under 60). The investigation scores high, doubled on the break route and with low Larder. The seizure scores high only where two of its divisions already stand, so the AI never starts a seizure it cannot finish.

## Cleanup

`cannibalism_clear_hidden_hoards` clears every cache record this host wrote, its array, the review context and any running seizure.
It runs from `cannibalism_reset_current_country_incarnation_state` and from the final cleanup's actor-registry loop, which also removes a running seizure mission.
`cannibalism_clear_all_current_country_mission_runtime` removes the seizure mission on an incarnation reset.
No daily, weekly or whole-world loop is used; all work happens at transfers, event answers, decisions and mission resolution.

## Constants and identifiers

- Constants: `cannibalism_hoard` and the four `hoard_*` keys in `cannibalism_unified_decision_cost` (`common/script_constants/014_cannibalism_constants.txt`). Autonomy amounts and the review delay are file constants at the top of the hidden-hoard section of `common/scripted_effects/014_cannibalism_effects.txt`, because `add_autonomy_ratio` and event delays take plain numbers.
- Effects: the "Hidden hoards" section of `common/scripted_effects/014_cannibalism_effects.txt`.
- Triggers: the "Hidden hoards" section of `common/scripted_triggers/014_cannibalism_triggers.txt`.
- Event: `chaosx.nr14.82` in `events/014_cannibalism.txt`.
- Decisions and mission: `common/decisions/014_cannibalism_decisions.txt`, unified command category.
- State modifier: `cannibalism_hoard_guard_unrest` (local supplies -15 percent, resistance target +10 percent) in `common/dynamic_modifiers/014_cannibalism_dynamic_modifiers.txt`.
- Localisation: `localisation/english/014_cannibalism_l_english.yml` and the `GetCannibalismHoard*` getters in `common/scripted_localisation/014_cannibalism_scripted_localisation.txt`.

## Icons

| Use | Sprite in `interface/014_cannibalism.gfx` | Texture |
| --- | --- | --- |
| Investigate Hidden Hoards | `GFX_decision_cannibalism_unified_investigate_hidden_hoards` | `gfx/interface/decisions/014_cannibalism/decision_cannibalism_unified_investigate_hidden_hoards.dds` |
| Seize a Hidden Hoard | `GFX_decision_cannibalism_unified_seize_hidden_hoard` | `gfx/interface/decisions/014_cannibalism/decision_cannibalism_unified_seize_hidden_hoard.dds` |
| Seize the Hidden Hoard mission | `GFX_decision_cannibalism_unified_hoard_seizure_mission` | `gfx/interface/decisions/014_cannibalism/decision_cannibalism_unified_hoard_seizure_mission.dds` |

The review event reuses `GFX_report_event_cannibalism_warlord_submission`, and the unrest modifier needs no icon.
Sources and processing are recorded in `docs/plans/014_cannibalism_plans/subagent_handoffs/2026-10-04_hidden_hoard_icons.md`.

## Validation limits

The AI weights were evaluated and compared through the HOI4 MCP probability route (`docs/plans/014_cannibalism_plans/subagent_handoffs/2026-10-04_hidden_hoards_probability.md`).
Engine behaviour of the meta-trigger force check, the autonomy changes and the native mission timer remains for live verification.

## Future plans

- The revealed command window could list located caches with their amount and owner on the Loyalty page.
- A hoarder governor could later draw on its own cache to resist absorption, turning a tolerated hoard into a military reserve.
- Enemy intelligence could learn of a located cache and raid it, giving the counterwar side a target inside the cult's territory.
