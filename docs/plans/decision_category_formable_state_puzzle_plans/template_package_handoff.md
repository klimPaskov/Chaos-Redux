# Formable state-puzzle template package handoff

## Scope

The reusable package under `.agents/skills/hoi4-decisions-missions/templates/formable_state_puzzle/` is now populated as documentation scaffolding only.

## Files added

- `state_manifest.schema.json` defines map revision, counting policy, projection, exact geometry provenance, sprite names, state entries, and alternate groups.
- `state_manifest.example.json` is a three-state installed-map example using states 121, 122, and 123, one fixed state, one two-member alternate group, source hashes, row-run hashes, mask hashes, pixel counts, and projected positions.
- `formable_state_puzzle.gui` defines a compact clipped decision-category container, summary line, status badge, and one generated icon entry per state.
- `formable_state_puzzle.gfx` registers static unresolved, hatch, border, qualifying, check, keyline, status, generic dynamic-list aliases, and gated category-picture sprites.
- `formable_state_puzzle_scripted_gui.txt` binds the decision-category context, optional dirty refresh variable, dynamic state-piece images, summary state properties, and presentation-only AI contract.
- `formable_state_puzzle_scripted_triggers.txt` defines one state qualification helper, generated state wrappers, an explicit alternate-group helper, territory eligibility, and decision availability scaffolding.
- `formable_state_puzzle_scripted_effects.txt` defines bounded count refresh and cleanup with owner constants and no periodic world iterator.
- `formable_state_puzzle_scripted_localisation.txt` defines dynamic sprites, a direct live qualifying count through descending `count_triggers` checks, summary/status selection, state-scope hover helpers, owner/controller fallback helpers, and fixed generated state helpers.
- `formable_state_puzzle_localisation.example.yml` contains the category, summary, requirement, hover, owner/controller fallback, control, core, and status examples and is UTF-8 with BOM.
- `static_category_picture_option.md` records the explicit one-state or indivisible-adjacent-shape gate and static category snippets.
- `validation_checklist.md` records geometry, piece, shared-helper, refresh, AI, lifecycle, asset, localisation, and GUI evidence checks.

## Validation performed

The JSON example was parsed successfully as JSON, and the schema and example were checked for matching required fields and SHA-256 shape with the repository's JSON tooling.

The installed vanilla map was read directly to obtain the example's 5632 by 2048 dimensions, state-history province memberships, source bounding boxes, row-run counts and hashes, mask hashes, and pixel counts.

The package file list matches every missing file named by the template README.

The localisation example begins with the UTF-8 BOM byte sequence.

The Clausewitz templates use tabs for script blocks, no periodic world iterator, no event-target syntax, no animation declarations, no button controls, and a shared territory helper for the summary and decision contract.

## Limitations and owner follow-up

The package is not runtime wiring and contains deliberate angle-bracket placeholders for owner ids, state ids, manifest-generated coordinates, constants, sprite paths, and GUI entry names.

The owner must generate one concrete icon and sprite family per manifest state, replace the example helper names, archive the geometry extraction artifact beside the owner implementation, and attach the GUI inspect/render evidence required by the checklist.

The generic dynamic-list path requires the owner to verify state-scope array support in the installed engine; the fixed generated icon path is supplied for owners that cannot use a verified state-scope dynamic list.

The parent integration pass updated the README and localisation examples to prefer the same non-mutating `count_triggers` contract used by the runtime generator; the bounded refresh effect remains an optional scaffold for owners with proven event-driven coverage.

No runtime `common/`, `interface/`, `gfx/`, or localisation files were changed.
