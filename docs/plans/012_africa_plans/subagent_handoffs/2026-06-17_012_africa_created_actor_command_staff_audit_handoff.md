# Event 012 Africa Created-Actor Command Staff Audit Handoff

Date: 2026-06-17

Scope: bounded country-package command/staff tranche for the 21 Event 012 created, restored, sponsored, transformed, and high-chaos actors:

`WAC`, `SAH`, `MAG`, `NHR`, `EAC`, `GLK`, `CBC`, `ZSC`, `SLC`, `IOC`, `GHP`, `BBS`, `TDM`, `ANW`, `OVN`, `CRR`, `CTL`, `OKP`, `TRM`, `HGD`, `GHC`.

## Summary

No gameplay patch was made by this audit. The current parent worktree already contains the narrow command-staff implementation surface that was likely missing after the two-advisor tranche:

- `africa_generate_created_country_role_staff` gives every created actor two generated advisors: one role advisor and one support advisor.
- `africa_generate_created_country_command_staff` gives every created actor one generated corps commander.
- The same command helper gives generated naval commanders to the nine actors that already have matching static naval OOBs: `WAC`, `MAG`, `EAC`, `CBC`, `IOC`, `TDM`, `ANW`, `OVN`, and `CRR`.
- No generated field marshals exist. This looks intentional and safe for a bounded setup pass; adding field marshals to 21 small actors would become a broad balance and identity change rather than a local command-staff fix.
- No extra minister layer beyond the existing two generated advisors exists. That remains a full country-package depth item, not a safe small patch.

The implemented command names are institutional or office-like command bodies, not invented historical personal leaders. This fits the constraint that supernatural and nonhuman actors stay explicit fictional/nonhuman entities and avoids opposite-gender portrait/name-pool risk because the helper does not draw from personal random-name pools.

## Changed Files

- Added this handoff:
  - `docs/plans/012_africa_plans/subagent_handoffs/2026-06-17_012_africa_created_actor_command_staff_audit_handoff.md`

No gameplay, localisation, focus, decision, history, country, AI, or asset files were changed by this audit.

## Country Package Coverage Checklist

- Tags covered: all 21 expected Event 012 created actors.
- Generated advisors: present from `africa_generate_created_country_role_staff`; 42 total generated advisor blocks, two per tag, per the prior advisor-pool audit.
- Generated corps commanders: present from `africa_generate_created_country_command_staff`; 21 total, one per tag.
- Generated naval commanders: present for the nine tags with static naval OOB support.
- Generated field marshals: absent.
- Additional ministers/advisors beyond the two generated advisors per actor: absent.
- Idempotence: command helper gates on `africa_created_country_command_staff_generated`; setup helper calls it from `africa_apply_created_country_setup_package`.

## File Surface Checklist

- `common/scripted_effects/012_africa_effects.txt`
  - `africa_generate_created_country_role_staff`
  - `africa_generate_created_country_command_staff`
  - `africa_apply_created_country_setup_package`
- `history/countries/TAG - *.txt` for all 21 actors
  - Static land OOB references checked.
  - Naval and air OOB references checked where present.
  - No static `recruit_character`, `create_corps_commander`, `create_navy_leader`, or `create_field_marshal` blocks found in those history files.
- `interface/012_africa.gfx` and `interface/chaosx_characters.gfx`
  - Event-specific fictional/nonhuman portrait sprites used by command staff resolve.
- Vanilla `~/projects/Hearts of Iron IV/interface/_random_portraits.gfx`
  - Generic African land/naval commander portrait sprites used by command staff resolve.
- Vanilla `~/projects/Hearts of Iron IV/common/unit_leader/00_traits.txt`
  - All unit-leader traits used by command staff resolve.
- `docs/events/012_africa_foundation.md`
  - Current doc already mentions `africa_generate_created_country_command_staff`.

## Missing Or Stale Country Package Surfaces

- No missing narrow command-staff helper was found in the current worktree.
- Older handoffs still say full minister or commander rosters remain future work. That remains accurate for full bespoke rosters, but this handoff supersedes the narrower "no generated commanders at all" concern.
- Full bespoke minister rosters, named personal commanders, field marshals, deeper naval/air branches, and per-tag decision/focus identities remain broader country-package work.

## Map And State Setup Issues

No map or state setup issue was found for the command-staff surface.

The history-file pass confirmed all 21 actors have static land OOB references. The nine actors with generated naval commanders match the same nine actors with static naval OOB references:

`WAC`, `MAG`, `EAC`, `CBC`, `IOC`, `TDM`, `ANW`, `OVN`, `CRR`.

## Politics, Leader, Portrait, Flag, Advisor, And Party Issues

- Country leaders, party names, flags, and cosmetic names were not changed.
- Command staff use institutional display names such as "Lagos Port Column Captains", "Grove Boundary Wardens", and "Migration Corridor Wardens"; they are not joke names, translated leader/court names, or personal random-name pool draws.
- Nonhuman/supernatural actors use their fictional/nonhuman leader portrait sprites where available, preserving explicit nonhuman presentation.
- Human regional-authority actors use vanilla generic African land/naval commander portraits.
- No opposite-gender portrait/name-pool defect was found because these generated characters do not use gendered personal names.

## Focus, Decision, Idea, And Asset Issues

- Focus loading exists through `load_focus_tree = { tree = africa_regional_authority_focus_tree keep_completed = no }` or `load_focus_tree = { tree = africa_high_chaos_actor_focus_tree keep_completed = no }` in the selected created-actor package paths.
- No focus or decision patch was needed for this command-staff tranche.
- Generated command characters do not create advisor idea tokens, so no new advisor idea localisation keys or idea icons are required for them.
- All portrait sprite names referenced by the command helper resolve either in Event 012/Chaos Redux interface files or vanilla portrait sprite files.

## Starting Military, Technology, Industry, Supply, And Production Issues

No new starting military issue was found inside this command-staff surface.

The command helper lines up with the existing bounded military setup:

- Every actor has a static land OOB reference.
- Naval commanders are only generated for actors that already have a static naval OOB.
- Air OOB actors do not receive air commanders here, which is expected because HOI4 country characters do not use an equivalent generated air-commander role.

## AI And Playability Issues

The command-staff layer improves basic playability for created actors without creating full bespoke military establishments. The absence of field marshals is acceptable for this bounded pass because these are small created actors with small static OOBs, not full major-country packages.

Remaining AI/playability risks are broader:

- no full bespoke commander rosters;
- no field marshal progression route;
- limited naval/air behavior beyond the small OOB and role-specific AI posture;
- no per-tag command decisions or focus branches beyond the shared companion tree and tag capstones.

## Validation

Meaningful checks run:

- Counted generated command characters in `africa_generate_created_country_command_staff`: 30 total.
- Counted generated corps commanders: 21 total.
- Counted generated naval commanders: 9 total.
- Checked all 21 expected tags appear exactly once as command-helper tag gates.
- Checked generated command token bases for duplicates; none found.
- Checked command-helper portrait sprite names against Event 012/Chaos Redux interface files and vanilla interface files; no missing sprites found.
- Checked command-helper unit-leader traits against vanilla/mod unit-leader trait definitions; no missing traits found.
- Checked all 21 actor history files for static land OOB references and for static naval/air OOB references.

Skipped meaningful validation:

- No live game load was run. This audit did not change gameplay files and was scoped to static implementation inspection.
- No broad country-package balance validation was run because this is only the command/staff tranche and not a full country-package completion pass.

## Patch Status

Patch status: handoff-only. No gameplay patch was needed because the current worktree already has the bounded generated command-staff helper and setup call.

## Residual Risks

- This does not complete the full country-package requirement for Event 012.
- The 21 actors still need broader review for fully bespoke ministers, route-specific commanders, deeper naval/air branches, country-specific decision chains, full focus-tree identities, and richer AI behavior.
- The generated command names are institutional by design. If the parent later wants personal commanders, that must go through a separate portrait/name-pool and sourcing/generation pass, especially for female-presenting portraits and supernatural/nonhuman actors.
