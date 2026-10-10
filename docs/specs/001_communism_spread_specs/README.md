# Event 001 Communism Spread specifications

The design source is [`001_communism_spread_spec.md`](001_communism_spread_spec.md), the original rework brief with the 10 October 2026 World Revolution integration.
Its Document status section lists where the source differs from the brief, and its Open questions section holds the unaccepted proposals.
Current implementation documentation is in [`docs/events/001_communism_spread/overview.md`](../../events/001_communism_spread/overview.md).
The [2026-10-06 release reconciliation](../../plans/001_communism_spread_plans/release_qa_completion_20261006.md) records acceptance for the bounded QA repairs and leaves broader historical design differences unresolved where their user or parent acceptance basis is missing.

On 10 October 2026 the user selected the [new Event 091 package](../091_the_great_revolution_specs/README.md) to govern the shared Revolution handoff.
The [World Revolution State Integration](001_communism_spread_spec.md#world-revolution-state-integration) section preserves inherited territory first, adds Event 091's proportional nominations and rebel political choices, and keeps targeted local-cell activity after the opening.
This design is accepted and queued for gameplay implementation.
The [current import review](../../plans/091_the_great_revolution_plans/subagent_handoffs/091_import_review_2026-10-09.md) records that decision and the documentation alignment.

## Changelog

- 2026-10-10, spec audit.
  - Added a Document status section to the spec that marks the brief as implemented and lists the points where the source differs from it (drift cap, conversion model, warning gate), each with its disposition.
  - Marked the Cleanup Requirements as completed and the conversion chances as superseded by the source budget, without removing either.
  - Replaced the duplicated World Revolution entry paragraph in Evolution 3 with a pointer to the Major Event Hook section.
  - Added open questions 1 to 5 as proposals: conversion model, drift cap, warning gate, Famine escalation factor and Deaths from the emergency crackdown.
  - No historical date gate exists in Event 001, so the 10 October date-gate rule required no change.
  - No package manifest exists for this package.
