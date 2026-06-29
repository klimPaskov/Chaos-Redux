# Event 013 focused addendum resolution

## Scope

This handoff resolves the P0 blocker list from `2026-06-29_event013_focused_improvement_addendum.md` for the final Event 013 implementation pass.

## P0 status

1. Scored target pool: implemented in `natural_disasters_score_current_target_candidate`, `natural_disasters_consider_target_candidate`, and `natural_disasters_select_target_state_for_current_family`.
2. Warning variance by family and capacity: implemented through `natural_disasters_prepare_warning_score_for_current_target`, `natural_disasters_roll_warning_for_current_target`, and the missed-warning direct impact path. The score reads family band, state control, infrastructure, radar, airbase, coastal facilities, war state, stability, preparedness actions, evolution stage, active aftermath, and maximum barrage pressure.
3. Family objective packets: implemented through `natural_disasters_objective_type`, mission success and failure assignments in `013_natural_disasters_decisions.txt`, and the shared objective success and failure helpers. The final decision handoff verifies all 21 selectable missions assign objective types on success and failure.
4. Evolution II and III chain controllers: implemented through hidden events `chaosx.nr13.40` through `.45` and helpers for delayed tsunami, moving storm corridor, meteor cluster, massive rupture wave, and massive eruption ashfall or lahar follow-up behavior.
5. Animated gameplay surface: implemented through the Event 013 scripted GUI decision-category strip, which displays registered animated warning, tsunami, corridor, eruption, and skyfall sprites with static fallbacks.
6. Achievement predicates: tightened in achievement definitions and wired through impact, warning, objective success, objective failure, and cleanup flags for capital preparation, no-deaths cleanup, maximum barrage aftermath closure, firebreak control, aftershock control, skyfall crater cleanup, global relief variety, and abnormal no-world-end resolution.
7. Family news throttling: implemented through family-routed news events, global news cooldown, family-specific global cooldown flags, and severity or death-aware report eligibility using the last affected state context.

## Manual scenario override

Disaster Barrage is intentionally forceable from the manual scenario UI. It is not blocked by active world-end state, an existing Event 13 sequence, or a valid-state precheck. The launch helper clears active Event 13 sequence and chain context before queuing the manual barrage so scenario flags do not leak into later automatic events. Existing aftermath ledgers are not deleted by that force launch. Manual Disaster Barrage uses a hidden state-scoped controller token for the scheduler, finish report, generic chain controller, and delayed tsunami warning. The token stores the launching country pointer and exact sequence id, while manual target states are stamped with the active manual sequence id and slot. Stale manual delayed events therefore self-cancel if a later force launch has replaced their context. Normal delayed Event 13 controllers and state impacts are guarded by active-sequence checks and a temporary post-launch flush flag, so pre-barrage automatic deliveries cannot wake up after the manual season ends.

## Remaining risks

No P0 addendum item is intentionally skipped, queued, or rejected. The remaining risk is live-session pacing across high-intensity chained sequences, especially no-valid-neighbor outcomes and player timing between warning events and recovery decisions.
