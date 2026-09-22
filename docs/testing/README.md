# Testing and live-QA evidence

This directory contains test-country guidance and dated evidence from live-QA runs.

## Navigation

- [`chaosx_test_country.md`](chaosx_test_country.md) describes the reusable test-country setup and related test hooks.
- [`live_qa/`](live_qa/) contains dated run manifests, reports, coverage records, and retained diagnostic evidence.
- [`hoi4_agent_tools_profiles/visual_surfaces.md`](hoi4_agent_tools_profiles/visual_surfaces.md) records the focus and technology visual QA selectors, screenshot references, and review limits; [`visual_surfaces_suite.json`](hoi4_agent_tools_profiles/visual_surfaces_suite.json) checks their source inventories and renders with `hoi4.scenario_test` when that route is available.
- [`hoi4_agent_tools_profiles/scripted_gui.md`](hoi4_agent_tools_profiles/scripted_gui.md) records the meter, settings, scenarios, and insurgency window states; [`scripted_gui_suite.json`](hoi4_agent_tools_profiles/scripted_gui_suite.json) checks representative inspect and render scenarios.
- [`hoi4_agent_tools_profiles/transfer_and_event.md`](hoi4_agent_tools_profiles/transfer_and_event.md) records civilian transfer invariants and Event 001 integration; [`transfer_and_event_suite.json`](hoi4_agent_tools_profiles/transfer_and_event_suite.json) checks source declarations, an invalid preflight, and a bounded event chain.

Each dated QA package is evidence for the run it records and does not replace the accepted design in `docs/specs/`, the current implementation record in `docs/events/`, or the working status in `docs/plans/`.

Preserve dated reports and provenance when they explain a prior validation result or unresolved limitation.
Do not infer current gameplay status from an old run without checking its package date and current source references.
