# Event 021 Decision and Mission Parent Refresh — 2026-09-19

Status: implemented source repair recorded; final acceptance remains open.

Scope: reconcile the bounded decision/mission audit output with the current Event 021 source after the test-entry rework marker was opened.

The bounded specialist audit was interrupted after it returned its findings and did not write the requested specialist handoff.

No Event 023 files were edited, no gameplay process was launched, and no live decision, mission, save/reload, or performance result is claimed.

## Evidence and repairs

`common/decisions/021_random_civil_war_decisions.txt` contains 18 action decisions and three selectable missions under `event021_civil_war_crisis_category`.

The action cost audit found no action spending more than four resource types, with `event021_offer_emergency_settlement` at the four-type ceiling and all other actions below it.

The State Authority guidance strings had referenced the nonexistent `event021_authority` constant namespace.

The owner repaired those three references to `constant:random_civil_war_authority.*` in `localisation/english/021_random_civil_war_l_english.yml` and committed the repair as `125b48227`.

The repository-wide localisation audit completed after the repair with zero parse errors, duplicate keys, missing BOMs, or encoding artifacts.

The mission source uses `complete_effect` to set a mission-active receipt and `timeout_effect` to call a resolver that checks the objective and dispatches the distinct success or timeout helper.

This matches the installed vanilla mission contract: selecting a selectable mission runs its `complete_effect`, while `timeout_effect` is the expiry boundary; the installed effects documentation also exposes `remove_mission` as the path that intentionally removes a mission without running either completion or timeout effects.

The three Event 021 mission resolvers are therefore source-consistent, but their activation, expiry, cancellation, and cleanup behavior still require the user-owned live test pass.

## Remaining gates

The interrupted specialist did not produce a current independent decision/mission probability artifact or before/after comparison.

The current parent probability evidence remains structural and does not certify the full named weighted matrix.

The current Event 021 status remains `Needs Testing`; this handoff does not promote it to final acceptance.

