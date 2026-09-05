# Event 012 Gods of Africa runtime lifecycle and negotiation handoff

Date: 2026-09-05

Disposition: implemented

## Scope

This handoff records the bounded runtime repair for the Event 012 Gods of Africa participant contract, negotiation, substitute, and reconciliation surfaces. It does not change Event 070, the shared event log, or the separate strange-force model packages.

## Implemented source surfaces

- `common/scripted_effects/012_africa_gods_effects.txt` now builds and freezes up to three deterministic substitute slots when a demand contract is created, validates live capacity before submission, exposes explicit host acceptance and rejection effects, restores the original demand after rejection, records the rejected offer, and clears substitute state idempotently during archive, settlement, cancellation, and participant cleanup.
- `common/scripted_effects/012_africa_gods_effects.txt` now cancels an ordinary demand once when its participant enters a war with Africa, records the treaty break, applies the bounded `gods_of_africa_wrath.war_magnitude` increment, and waits for the post-war dispatch gates before issuing another demand.
- `common/scripted_effects/012_africa_gods_effects.txt` now keeps priority-offender marks in a centralized host counter capped by `gods_of_africa_timing.priority_offender_cap`, releases the slot when a stale marked participant is archived, and resets the counter on unifier loss or final cleanup.
- `common/decisions/012_africa_gods_decisions.txt` now exposes `gods_of_africa_accept_substitute` and `gods_of_africa_reject_substitute` to the current host over the bounded participant array, with current-contract and pending-offer guards.
- `common/scripted_triggers/012_africa_gods_triggers.txt` now exposes `gods_of_africa_substitute_offer_is_pending` and keeps reconciliation eligibility inside the review window with a retry-cooldown guard.
- `common/decisions/012_africa_gods_decisions.txt` and `common/scripted_effects/012_africa_gods_effects.txt` now use `gods_of_africa_reconciliation_mission` as a real 60-day review window; timeout calls `gods_of_africa_fail_reconciliation`, records the failure, raises Wrath, and schedules the next attempt, while completion removes the mission and clears the pending state.
- `events/012_africa_gods_of_africa.txt` and `localisation/english/012_africa_gods_l_english.yml` now provide the rejected-substitute report event `chaosx.nr12.612`, the wartime cancellation report event `chaosx.nr12.613`, and their decision/effect text. Participant cleanup clears the wartime report receipt alongside the other terminal report flags.
- `common/script_constants/012_africa_gods_constants.txt` adds the unique `substitute_rejected` history kind and a central `war_magnitude` Wrath value.

## Model boundary

The elephant formation remains on the normal vanilla Elephantry runtime. `common/units/012_africa_elephant_forces.txt` uses `sprite = elephantry`, and no custom elephant entity, Meshy model, or replacement action set is required. This is the accepted source disposition documented in `docs/events/012_africa/gods_of_africa.md` and `docs/systems/3d_model_pipeline/chaosx_africa_elephant_model.md`.

## Evidence

Focused `hoi4.event_inspect` lint and `hoi4.event_render` options were run for `chaosx.nr12.608` with helper expansion; both returned `status = ok`, no blockers, and zero blocking diagnostics in the focused response. Lint revision `b21215aa484b34e2e808a18e534ffb74072b27ebe8a9f4994cfa673400443ef2` produced `event-lint-b21215aa484b.json`; the options render produced `event-options-b21215aa484b-manifest.json` plus JSON/SVG/PNG resources. The remaining validation-false state is the documented large-workspace/deferred-helper boundary, not a source parse error. Structural brace and unsupported-operator checks were run on the touched script surfaces, and the localisation file remains UTF-8 with BOM.

The post-cap `hoi4.probability_inspect` for `decision_ai_will_do` found the ten declared Event 012 host decisions with a complete source candidate pool, zero unresolved inputs, and no parser diagnostics at source hash `d1987cc6697fa1d90a358731a120ab38b4e3fbe0addc0a2e8ff4be9e287bff7c`; artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0850969f8cfed451fef0f78460aecee66c21e326f4fee6e48bd4a89b3eacad44/ce71bb5cc3b23f257dc7d87b3840834e9fbb439f1f175fe994bc33659b95887f/probability-inspect-d1987cc6697f.json`.

The same ten-candidate pool was compared with the repository `HEAD` decision source under the named scenarios `OFFENDER-CAP-AVAILABLE` and `OFFENDER-CAP-EXHAUSTED`. `hoi4.probability_compare` returned `PROBABILITY_ANALYZED_PARTIAL` with six comparison changes, twenty-one unresolved runtime-dependent items, and one expected fixture warning that the mark action is never eligible without a participant target state; artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0874558a4230de9b4e337d3578e8c613c835dd11559ebde6a8702da3d4a88a5f/39c8874dfc3f0d3fe663410c94db5da77f03f72489481d5e67479ebbd120ebea/probability-2ec727de92bfa7d18cdea211.json`. This is score-only, bounded comparison evidence and does not claim normalized live AI odds.

## Remaining risks and evidence limits

The host acceptance/rejection flow and reconciliation timeout are source-present but still require the user's live-save validation. The decision probability route remains aggregate/incomplete and the compact compare fixture does not represent the full participant-target matrix, so this handoff makes no normalized AI-balance claim. The separate Africa model manifests, live visual promotion, and other Event 012 package gates remain governed by their own handoffs and are not completed by this runtime tranche.
