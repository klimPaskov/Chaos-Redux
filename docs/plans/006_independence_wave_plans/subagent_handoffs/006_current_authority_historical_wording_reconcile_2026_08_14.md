# Event 006 historical-authority wording reconciliation

Date: 2026-08-14.

## Scope

This docs-only patch is limited to the historical sections of the Event 006 source-of-truth map and resume packet.

## Changes

The dated 2026-08-09 source-map snapshot now says “then-current” for its 27/25/166 boundary and historical attested IDs.

The dated 2026-08-06 resume snapshot now describes its 21/20/172 arithmetic as historical and routes current authority only through the post-IW-045 override above it.

No current authority counts, Join order, admission gate, package source, asset, localization, workbook, or runtime file was changed.

## Validation

Targeted searches confirm the edited historical sections no longer describe 27/25/166 or 21/20/172 as current routing authority.

`git diff --check` was run on both edited docs and this handoff.

The current authority remains 32 content-attested packages, 29 compatible groups, 161 unattested rows, and 40 runtime adapters, with Event 006 HOLD / PARTIAL.
