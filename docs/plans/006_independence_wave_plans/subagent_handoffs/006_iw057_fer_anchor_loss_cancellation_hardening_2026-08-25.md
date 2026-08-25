# IW-057 Far Eastern Republic anchor-loss cancellation hardening

Date: 2026-08-25

## Scope and outcome

The ten FER project decisions now cancel when the Event 006 ordered anchor contract is lost. Each `cancel_trigger` adds `NOT = { has_independence_wave_fer_anchor_owned = yes }` alongside the existing package, generation, crisis, and capital-control cancellation gates.

The founding mission already carried the same anchor-loss cancellation branch. The shared `is_independence_wave_fer_project_ready` trigger already requires an owned-and-controlled state 408 or 409 anchor, so project visibility and availability were already fail-closed; this patch aligns active-project cancellation with that same contract.

When an anchor is lost, existing decision `cancel_effect` branches still execute the package's existing failure or host-loss cleanup. No new effects, central adapter, attestation, scenario preflight, deterministic Join entry, map rebind, identity receipt, flag, portrait, leader, or probability claim was added.

## Validation

- FER project decisions: 10 anchor-loss cancellation branches added.
- FER founding mission: existing anchor-loss cancellation preserved.
- `is_independence_wave_fer_project_ready`: existing anchor gate preserved.
- Decision file braces remain balanced.
- No central admission or package count changed.
- Existing allocator, country API, scenario, flag, FORM-16, and Statehood Ledger static audits remain passing.
- This handoff provides source evidence only; no live cancellation receipt is claimed.
