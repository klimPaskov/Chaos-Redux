# Event 016 Mengele D’Rhondan operational gate

Disposition: implemented in source within the accepted Event 016 closure plan; engine acceptance remains unresolved.

The independent completion audit found that the Mengele envoy-craft gate accepted three project-completion markers plus `rocket_engines` and `atomic_research` despite the accepted requirement for five learned operational packages.
`dhrondan_envoy_craft_has_operational_work` now requires `conventional_technology_computation_operational`, `conventional_technology_materials_operational`, `conventional_technology_rocketry_operational`, `conventional_technology_high_energy_operational`, and `chaosx_custom_technology_alien_infantry_operational` in its Mengele branch.
The Kruger and KRG branch remains unchanged, and `docs/events/016_brilliant_scientist/systems/dhrondan_contact.md` describes the two paths accurately.

Source review confirms that the five flags are written by the existing provider-neutral conventional and custom technology APIs; a Prototype marker or the two vanilla technologies alone no longer passes the Mengele branch.
The current event-specific craft description already names the five operational domains and needed no localisation change.
Focused read-only `hoi4.event_inspect` lint for `chaosx.nr16.40` after the source edit returned `EVENT_INSPECTED_PARTIAL`, source revision `0106e3d60ec54fc3aee99358e16e371c895ba21d24260b46ba2318536924e62f`, zero blocking diagnostics, and zero skipped sources, with artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f48b979846f5172839434012e266e2c9cfbfc1bff838c3e791306c4ba60e4cc3/520b0dc38b66c452c3f75b0473a854e5dc3f359f4aa41346cbd90ec5d1ca20d7/event-lint-0106e3d60ec5.json`.
The focused MCP graph did not expand scripted helpers and retained the earlier graph revision, so it does not prove this changed prerequisite or native project behavior.
Positive tests with all five receipts and negative tests for each missing receipt, prototype-only state, and vanilla-only technologies remain scenario acceptance work; no HOI4 process was launched.
