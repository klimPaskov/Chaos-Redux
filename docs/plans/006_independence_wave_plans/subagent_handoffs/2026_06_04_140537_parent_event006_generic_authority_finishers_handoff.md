# Event 006 Generic Authority Finishers Parent Handoff

## Scope

Implemented one bounded Event 006 focus-tree tranche: five post-proclamation route-family finishers for generic infrastructure-authority packages.

New focuses:

- `independence_wave_free_port_neutrality_statute`
- `independence_wave_municipal_home_rule_charter`
- `independence_wave_protectorate_public_guarantees`
- `independence_wave_oil_public_concession_statute`
- `independence_wave_canal_transit_statute`

No flags, flag art, country flags, or new visual assets were edited in this tranche. The focuses reuse registered Event 006 focus sprites.

## Files Changed

- `common/national_focus/006_independence_wave_focus.txt`
- `common/script_constants/006_independence_wave_constants.txt`
- `common/scripted_effects/006_independence_wave_effects.txt`
- `localisation/english/006_independence_wave_l_english.yml`
- `docs/events/006_independence_wave.md`
- `docs/specs/006_independence_wave_specs/006_independence_wave_focus_trees.md`
- `docs/assets/006_independence_wave/focus_icons/reuse_ledger.md`
- `docs/assets/006_independence_wave/focus_icons/manifest.md`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/2026_06_04_135926_event006_generic_authority_finishers_focus_audit.md`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/2026_06_04_140537_parent_event006_generic_authority_finishers_handoff.md`

## Implementation Notes

- Added centralized finisher tuning constants under `independence_wave_focus`.
- Added matching scripted effects for each finisher. Each effect sets the matching completion flag used by the focus bypass.
- Added focus localisation titles and descriptions.
- Updated Event 006 documentation and focus-tree source-spec notes to reflect that the generic Free Port, Canal Authority, Protected Mandate, Oil Protectorate, Municipal Authority, and railway package families now have route-family finishers.
- Updated the focus icon reuse ledger and manifest from 79 to 115 focus icon references, matching the live focus tree.

## Validation

- Brace balance passed with `balance=0 min=0` for the touched gameplay, localisation, and documentation files.
- Unsupported operator scan found no unsupported less-than-or-equal or greater-than-or-equal operators in the touched surface.
- Focus block count: 115.
- Focus localisation coverage: 0 missing title or description keys.
- Focus icon ledger rows: 115.
- Focus icon manifest count: 115.
- New focus coordinates:
  - `independence_wave_free_port_neutrality_statute`: `(38,8)`
  - `independence_wave_municipal_home_rule_charter`: `(38,9)`
  - `independence_wave_protectorate_public_guarantees`: `(38,10)`
  - `independence_wave_oil_public_concession_statute`: `(38,11)`
  - `independence_wave_canal_transit_statute`: `(38,12)`
- New focus coordinate duplicates: none.
- Reused sprites are registered in `interface/006_independence_wave_icons.gfx`.
- Matching scripted effects are top-level definitions by brace-depth check.
- New focus/effect/localisation/icon-doc surfaces do not introduce Event 005, PRA, Soviet, or collapse runtime coupling.

## Audit

Subagent audit: `docs/plans/006_independence_wave_plans/subagent_handoffs/2026_06_04_135926_event006_generic_authority_finishers_focus_audit.md`

Verdict: PASS.

The auditor confirmed the five focus blocks exist, are post-proclamation, have package-specific availability plus proclamation gates, have bypass flags and matching scripted effects, use registered Event 006 sprites, have localisation, and keep docs/icon ledgers aligned at 115 focuses.

## Remaining Risks And Omissions

- This tranche does not claim full Event 006 completion.
- No full game launch or complete Clausewitz parser pass was run.
- The worktree contains broad unrelated modified and untracked Event 005/Event 006 files, so no commit was created from this bounded tranche.
- The generic finishers are route-family finishers, not bespoke package-specific visual identities. Later package-specific variants and final visual support remain future work where the source specs require them.
