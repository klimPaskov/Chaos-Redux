# Event 006 IW-095 Dahomey lifecycle serialization repair — 2026-09-12

## Disposition

Implemented a package-local lifecycle repair for IW-095 Dahomey. Ordinary paid projects now remain closed until the founding compact mission publishes `independence_wave_dah_compact_crisis_resolved`, and the active founding mission occupies the package project slot. The repair is fail-closed and does not admit IW-095 to the central allocator, attestation, SCN-008, Join, assets, or formable registry.

## Changed gameplay surface

Changed `common/scripted_triggers/006_independence_wave_first_footprint_package_triggers.txt`:

- `is_independence_wave_iw095_project_ready` now requires `has_country_flag = independence_wave_dah_compact_crisis_resolved` in addition to the existing setup, identity-rights, force-generation, origin, failure, and state-776 ownership gates.
- `has_independence_wave_dahomey_active_package_project` now includes `has_active_mission = independence_wave_iw095_reconcile_abomey_and_porto_novo` before the paid decision list.

This mirrors the accepted serialized-opening contract already present in the Bashkiria package: the founding mission is the sole opening action, and ordinary projects begin only after its success receipt. Existing cancellation, timeout, payment, AI, cleanup, and state-776 capital guards remain unchanged. No cost, weight, route, identity, asset, or pre-event surface changed.

The same file already contains the concurrent IW-095 government-settlement exposure trigger; that pre-existing working-tree change is preserved and is not part of this repair.

## Source evidence

- IW-095 founding mission `independence_wave_iw095_reconcile_abomey_and_porto_novo` is defined in `common/decisions/006_independence_wave_decisions.txt` and publishes `independence_wave_dah_compact_crisis_resolved` only after stable compact values, a route government, and state 776 as the controlled capital.
- The nine IW-095 paid decisions use `is_independence_wave_iw095_project_ready` and `NOT = { has_independence_wave_dahomey_active_package_project = yes }` for their visibility/availability and therefore inherit the serialization guard.
- The parallel Bashkiria trigger contract at `common/scripted_triggers/006_independence_wave_bashkiria_mari_package_triggers.txt` already requires its compact-crisis receipt and includes its active founding mission in the package-project predicate.

## Validation

Focused Event 006 validators passed after the edit:

- allocator `--strict`: 149 publishers; 126 automatic/high-chaos selectable; 138 SCN-ranked; 40 adapters; 32 attestations; 29 compatible groups; automatic ladder 3/4/5/7/10; no pre-event crisis surface.
- country API: 242 broad tags, 191 resolved carriers, zero missing or duplicate carriers.
- flags `--strict`: 102 registered tags, 102 complete flag families.
- FORM-16, Statehood Ledger semantic source matrix, and SCN-008 scenario matrix all passed.

The required read-only event MCP refresh for `chaosx.nr6.1` was also run with a bounded downstream `lint`/`overview` pair. `hoi4.event_inspect` returned `EVENT_INSPECTED_PARTIAL` at revision `4bccb6ec7fe1a73728780d86d162cce29175781f0177cb5975beec17f22caa3d`, graph hash `24f73f1a61d57d7a3c99c927d106bf7fd7fe21299898bf43d3d8eab152165819`, and one large-workspace blocking diagnostic because helper/lifecycle projections were deferred. `hoi4.event_render` returned `EVENT_RENDERED_PARTIAL` at the same revision and layout hash `3ba5f18a64912a9ece6fe76dde07333dd05321a92381135e629786aae491844d`. A compare attempt returned the exact blocker `EVENT_REVISION_NOT_CACHED`; no comparison claim is made. These event artifacts cover the root chain only and do not prove package-trigger semantics or live execution.

No live game, save/load, event-MCP execution, or central-admission claim is made. No file was staged or committed because concurrent Git processes and unrelated worktree edits remain active.

## Remaining blockers

IW-095 remains package-local and unadmitted. The accepted identity/rights receipt, sourced opening flag, portrait/roster consumer, FORM-24 identity and membership evidence, central attestation/preflight/Join, typed probability evidence, Event 012 state-776 collision handling, country-specific technology acceptance, and live release/save-load receipts remain open. No fallback or simplification was introduced.
