# Event 006 overlay localisation registry — 2026-08-25

## Scope and outcome

The thirteen adapter-only overlay families now share one UTF-8-BOM localisation file: `localisation/english/006_independence_wave_minor_overlay_l_english.yml`.

The former eight overlay localisation files are removed:

- IW-005 Flanders
- IW-022 Dalmatia
- IW-025 Vojvodina
- IW-035 Livonia
- IW-059 Mesopotamia
- IW-085 Cyrenaica
- IW-101/IW-102/IW-105 COG overlays
- IW-156/IW-196/IW-197/IW-204 final vanilla route overlays

Each source section is retained under a `# SOURCE` marker beneath one `l_english:` root. Existing player-facing wording, dynamic values, cost disclosures, icon tokens, and scripted-localisation references remain intact; the current IW-059 cost wording present in the worktree was carried into the registry rather than replaced by the older committed snapshot.

## Validation

- The registry has one `l_english:` root, a UTF-8 BOM, 468 localisation keys, and zero duplicate keys.
- All eight source sections are present under explicit source markers.
- The Flanders system note now points to the registry and identifies the IW-005 section.
- No decision, trigger, effect, category, on-action, package-admission, or pre-event surface changed.
- No live localisation parser, UI render, or save/load receipt is claimed.

## Boundary

This is a source-layout consolidation only. Overlay carriers remain adapter-only and fail-closed outside central Event 006 admission.
