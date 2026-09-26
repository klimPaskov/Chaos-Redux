# Event 016 Mengele CXT Provider Fixture Mode

Disposition: `implemented` for the CXT-only provider setup entry; the full provider scenario matrix remains `unresolved`.

## Acceptance basis

The accepted Event 016 closure plan requires the existing CXT package to expose provider decision stages for the fifteen families, native callbacks, both DLC states, six Singularity components, six biological agents, DHR receipt gates, and cleanup.
The existing provider gate already includes a bounded `mengele_clone_army_scenario_country` plus `mengele_clone_army_scenario_state` branch, and the existing CXT category accepts that scenario marker.
This tranche uses that test-only branch through a player-triggered CXT debug decision and does not create a second provider model or synthetic stage history.

## Implementation

`common/decisions/chaosx_test_country_debug_decisions.txt` adds `chaosx_test_country_event016_mengele_provider_fixture_decision`, visible only for initialized player-controlled CXT.
The decision calls `chaosx_cxt_event016_enable_mengele_provider_fixture` in `common/scripted_effects/016_alien_infantry_cxt_test_effects.txt`.
The setup effect sets the existing Mengele scenario marker and scenario idea, opens `mengele_clone_focus_directorate_project_registry`, initializes the private provider receipt arrays, and reconciles provider project availability.
It records a CXT readiness flag only if `brilliant_scientist_mengele_project_stage_provider_is_valid` succeeds after setup; the decision remains visible for retry if that gate is still false.
The setup does not write a family Theory, Prototype, Deployment, or Weaponization receipt, complete a native project, award an API package, charge resources, or add a periodic CXT grant.
The decision uses the existing debug category and generic research icon, and its new player-facing strings are in `localisation/english/chaosx_test_country_l_english.yml`.
`docs/testing/chaosx_test_country.md` documents the activation order and the distinction between real provider decisions and the broad project-completion shortcut.

## Evidence and limits

Source inspection confirms that `is_mengele_clone_directorate_country` accepts the scenario-country marker and the provider gate accepts the matching scenario idea while still requiring the project registry and valid world/provider state.
The existing Mengele stage decisions remain the transaction owners after setup, so the fixture reaches their real costs, timers, cancellation handlers, and outputs.
The test country’s `Complete Research and Projects` debug decision bypasses native project clocks and payments; it must not be used as transaction evidence.
The setup is available in either DLC state, but this tranche does not prove both DLC routes in a live campaign.
No HOI4 session was launched and no test suite was run; user-owned live acceptance remains required.
No model, 3D geometry, model asset, or model pipeline was created, inspected, or modified.

The accepted plan’s full CXT matrix is still open: this entry does not add separate executable cases for all fifteen family lifecycles, six component de-duplication, six biological raid outcomes, DHR five-receipt positives and negatives, provider loss, or exact native later-stage settlement.
The native later-stage callback identity question is separately queued for the user because the installed special-project documentation does not expose a supported current-`FROM` project-ID comparison; this CXT setup does not approximate that identity.
