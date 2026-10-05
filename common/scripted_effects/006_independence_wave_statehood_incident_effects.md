# Event 006 statehood incident effects

Source: `006_independence_wave_statehood_incident_effects.txt`. Mechanic documentation: `docs/events/006_independence_wave/statehood_incidents.md`.

## independence_wave_start_statehood_incidents

Purpose: queue the first statehood incident pulse of a released country.

Scope: the active Event 006 country, called from the founding posture resolution effects in `006_independence_wave_opening_dispatch_effects.txt`.

Inputs: none. Reads `independence_wave_generation_id`.

Side effects: sets `independence_wave_statehood_incident_pulse_queued`, the generation and due-date variables, and schedules `chaosx.nr6.150` after `first_delay_days`. Does nothing while a pulse is already queued.

## independence_wave_queue_statehood_incident_pulse

Purpose: schedule the next pulse.

Scope: country.

Input: caller-set temporary `independence_wave_statehood_incident_delay`, in days.

Side effects: writes `independence_wave_statehood_incident_generation` and `independence_wave_statehood_incident_due_date` (the delay minus `due_margin_days`, converted with `chaosx_convert_days_to_date_offset`) and schedules `chaosx.nr6.150` after the delay.

## independence_wave_run_statehood_incident_pulse

Purpose: draw at most one incident and queue the next pulse.

Scope: country, from `chaosx.nr6.150`.

Gate: `can_run_independence_wave_statehood_incident_pulse` (active country, queued flag, current generation, due date reached).

Behaviour: computes the seven category weights and the quiet weight, gives each eligible incident its category weight, draws with `random_list` over temporary weights, marks the drawn incident done, sets `independence_wave_statehood_incident_open`, starts its category cooldown and fires the incident. It then queues the next pulse after a random interval. All temporary weights are created and consumed inside this one effect.

## independence_wave_statehood_incident_cool_<category>

Purpose: store the date from which a category may open another incident.

Scope: country. Categories: founding, recognition, security, government, league, formable, evolution.

Output: `independence_wave_statehood_<category>_ready_date`.

## independence_wave_statehood_incident_resolve

Purpose: close the open incident and zero every delta an option may write.

Scope: country, at the start of every option.

Side effects: clears `independence_wave_statehood_incident_open` and zeroes the Statehood, former-host, League and Network deltas.

## independence_wave_statehood_incident_apply_host_deltas

Purpose: apply the option's former-host deltas only while the former host lives.

Scope: country. Inputs: the `independence_wave_decision_*` host deltas.

## independence_wave_clear_statehood_incident_runtime

Purpose: generation-local cleanup.

Scope: country, called from `independence_wave_reset_current_generation` and `independence_wave_end_active_origin`.

Side effects: clears the queue flag, generation, due date, open incident, every category cooldown date and every done flag.
