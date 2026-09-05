# Event 012 Gods of Africa runtime lifecycle and negotiation handoff

Date: 2026-09-05

Disposition: implemented

## Scope

This handoff records the bounded runtime repair for the Event 012 Gods of Africa participant contract, negotiation, substitute, and reconciliation surfaces. It does not change Event 070, the shared event log, or the separate strange-force model packages.

## Implemented source surfaces

- `common/scripted_effects/012_africa_gods_effects.txt` now builds and freezes up to three deterministic substitute slots when a demand contract is created, validates live capacity before submission, exposes explicit host acceptance and rejection effects, restores the original demand after rejection, records the rejected offer, and clears substitute state idempotently during archive, settlement, cancellation, and participant cleanup.
- `common/scripted_effects/012_africa_gods_effects.txt` now cancels an ordinary demand once when its participant enters a war with Africa, records the treaty break, applies the bounded `gods_of_africa_wrath.war_magnitude` increment, and waits for the post-war dispatch gates before issuing another demand.
- `common/decisions/012_africa_gods_decisions.txt` now exposes `gods_of_africa_accept_substitute` and `gods_of_africa_reject_substitute` to the current host over the bounded participant array, with current-contract and pending-offer guards.
- `common/scripted_triggers/012_africa_gods_triggers.txt` now exposes `gods_of_africa_substitute_offer_is_pending` and keeps reconciliation eligibility inside the review window with a retry-cooldown guard.
- `common/decisions/012_africa_gods_decisions.txt` and `common/scripted_effects/012_africa_gods_effects.txt` now use `gods_of_africa_reconciliation_mission` as a real 60-day review window; timeout calls `gods_of_africa_fail_reconciliation`, records the failure, raises Wrath, and schedules the next attempt, while completion removes the mission and clears the pending state.
- `events/012_africa_gods_of_africa.txt` and `localisation/english/012_africa_gods_l_english.yml` now provide the rejected-substitute report event `chaosx.nr12.612`, the wartime cancellation report event `chaosx.nr12.613`, and their decision/effect text. Participant cleanup clears the wartime report receipt alongside the other terminal report flags.
- `common/script_constants/012_africa_gods_constants.txt` adds the unique `substitute_rejected` history kind and a central `war_magnitude` Wrath value.

## Model boundary

The elephant formation remains on the normal vanilla Elephantry runtime. `common/units/012_africa_elephant_forces.txt` uses `sprite = elephantry`, and no custom elephant entity, Meshy model, or replacement action set is required. This is the accepted source disposition documented in `docs/events/012_africa/gods_of_africa.md` and `docs/systems/3d_model_pipeline/chaosx_africa_elephant_model.md`.

## Evidence

Focused `hoi4.event_inspect` lint and `hoi4.event_render` options were run for `chaosx.nr12.613` with helper expansion; both returned `status = ok`, no blockers, and zero blocking diagnostics in the focused response. Lint revision `b21215aa484b34e2e808a18e534ffb74072b27ebe8a9f4994cfa673400443ef2` produced `event-lint-b21215aa484b.json`; the options render produced `event-options-b21215aa484b-manifest.json` plus JSON/SVG/PNG resources. The remaining validation-false state is the documented large-workspace/deferred-helper boundary, not a source parse error. Structural brace and unsupported-operator checks were run on the touched script surfaces, and the localisation file remains UTF-8 with BOM.

## Remaining risks and evidence limits

The host acceptance/rejection flow and reconciliation timeout are source-present but still require the user's live-save validation. The decision probability route remains aggregate/incomplete and has no immutable before/after pair for a probability comparison; this handoff therefore makes no normalized AI-balance claim. The separate Africa model manifests, live visual promotion, and other Event 012 package gates remain governed by their own handoffs and are not completed by this runtime tranche.
