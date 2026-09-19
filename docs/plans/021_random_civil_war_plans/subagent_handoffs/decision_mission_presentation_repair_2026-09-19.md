# Event 021 decision, mission, and exposure repair handoff

Date: 2026-09-19.

Status: implemented for the `Needs Testing` test-entry state; final acceptance remains unresolved.

## Scope

This owner-applied repair addresses the final decision and mission audit findings and the fresh completion-audit exposure findings without adding a custom GUI or changing the shared decision-category framework.

## Changed files

- `common/decisions/021_random_civil_war_decisions.txt`
- `common/scripted_effects/021_random_civil_war_decision_effects.txt`
- `common/scripted_effects/021_random_civil_war_effects.txt`
- `common/script_constants/021_random_civil_war_constants.txt`
- `common/scripted_localisation/021_random_civil_war_localisation.txt`
- `common/scripted_triggers/021_random_civil_war_parent_triggers.txt`
- `localisation/english/021_random_civil_war_l_english.yml`
- `docs/events/021_random_civil_war/acceptance_evidence.md`
- `docs/plans/021_random_civil_war_plans/source_of_truth_map.md`

## Implemented repairs

Consumed action flags and invalid target guards now affect decision visibility, so completed or unusable actions are removed from the category instead of remaining as greyed entries. Priority Front is one-use per crisis and records its action flag. Hold Capital uses the centralized 150-day duration, failed holds cannot reactivate, and its mission AI covers government, opposition, Event 006, and same-tag fronts. Secure Rail now covers reconstruction, opposition, and Event 006 contexts.

Evolution III prevention now presents two actions, Loyalty Review and Protect Communications, while Regional Administration stays available for reconstruction or settlement. The category description includes State Authority guidance with the next threshold and response. Capital and supply summaries are mapped separately, and support-target tooltips explain viability requirements.

Applying regional exposure now registers the neighbor in the existing bounded review registry. The exposure trigger rejects management while Evolution II is disabled, and cleanup clears the relief-use flag along with the other per-exposure action state.

## Evidence

The focused source checks found balanced blocks and no unsupported comparison operators in the patched files. The root `hoi4.event_inspect` lint returned `EVENT_INSPECTED_PARTIAL` with zero blocking diagnostics and zero skipped sources at revision `e6b5c2103a9a6912647172e8029907bdadf496f98234c85cb611a22359deeeb9`. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2780463794b9e80cc86de9fe00c11d344ab9cf249a980859c28dcab4db5a1316/6c7af5390c979ee04195362cead0059a57c1740793732e4ddf2fec16bfb2d9f1/event-lint-e6b5c2103a9.json`.

Mission probability source inspection passed with three candidates and zero unresolved source inputs at source revision `81006a9534710fec2cc9a555758f2ad98132a45f44232bb790a41b66c6a6f947`. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8739e8c00b47be7b445f443a0435ec4ae1a3026b5565e02fef76518829e8a3a6/7fdc2c22c881ca1f5010037b7fee3ee621478e494755b875a902c4080b7f6e66/probability-inspect-d942638f25e4.json`.

Decision probability source inspection returned `INTERNAL_ERROR` and no artifact. The event lint is partial because helper and lifecycle projections are deferred for the large workspace. No live GUI, mission cadence, exposure expiry, or full probability comparison is claimed.

## Remaining risks

Event 021 and SCN-018 remain `Needs Testing`. User-owned live gameplay, save/reload, full scenario and scheduler sequences, helper-expanded lifecycle evidence, the complete probability matrix and same-scenario comparison, the 32-package Event 006 runtime matrix and asset provenance, the shared fixed-target provider contract, and measured Maximum-scenario performance remain open.
