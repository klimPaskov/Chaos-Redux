# Event 006 IW-093/IW-098 player-facing wording cleanup

Date: 2026-08-28

## Scope

This bounded localization pass clarifies the Asante and Sokoto package focus, decision, and mission wording without changing gameplay, package admission, costs, AI, flags, triggers, or dynamic selectors.

## Changed file

- `localisation/english/006_independence_wave_iw093_iw098_l_english.yml`

The pass replaces implementation-facing uses of “receipt” and “decision receipt” with the corresponding completed project, settlement, reorganization, or arrangement. It also removes “route lane” wording, shortens the Sokoto category description, and keeps the in-world accounting use of “cocoa receipts” unchanged.

## Validation

- The file remains UTF-8 with BOM.
- A focused search confirms no technical “receipt” or “decision receipt” wording remains in the affected IW-093/IW-098 focus and mission strings; the accounting phrase “cocoa receipts” remains intentionally in-world.
- No localization keys were added, removed, or renamed.

## Boundary

This is a player-facing clarity-only change. The package remains subject to its existing identity, rights, setup, admission, and engine-evidence gates. No pre-event surface, decision cost, or Event 006 transaction behavior changed.
