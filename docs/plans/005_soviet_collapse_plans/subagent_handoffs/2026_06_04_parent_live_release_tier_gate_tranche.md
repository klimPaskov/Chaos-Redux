## Parent Tranche: Live Release Tier Gates

Scope:
- Keep triggerable Soviet Collapse scenarios immediate and exhaustive.
- Stop the live Union Unmade terminal path from using the scenario-style all-possible release pass at calm world.
- Keep flag image files untouched.

Changed files:
- `common/script_constants/005_soviet_collapse_constants.txt`
- `common/scripted_triggers/005_soviet_collapse_triggers.txt`
- `common/scripted_effects/005_soviet_collapse_effects.txt`

Implementation notes:
- Added `is_soviet_collapse_terminal_base_republic_candidate` for terminal base SSR releases.
- Changed `soviet_collapse_release_terminal_ordinary_republics` to collect only base republic candidates instead of every possible core country.
- Added `soviet_collapse_release_terminal_internal_republics` and `soviet_collapse_release_terminal_internal_republics_for_current_tier`.
- Live terminal collapse now releases base republics at all tiers, internal vanilla republics from chaos tier 2 upward, and the exhaustive all-possible release pass only at chaos tier 5.
- Standalone triggerable Soviet Collapse still calls the exhaustive release helper so that scenario remains an immediate sandbox collapse.
- Removed calm-tier internal follow-on pressure by setting `follow_on_chaos_tier_1_internal_releases = 0`.
- Removed old-movement-pressure-only access from high-chaos successor spawning; custom chaos successors now require chaos tier 3+ or the standalone chaos scenario include-chaos flag.

Validation:
- `git diff --check` on touched release files passed.
- Brace balance check passed for touched release files.
- Unsupported `<=` / `>=` scan on touched release files returned no matches.

Remaining work:
- Focus trees still need the requested branch cleanup and deeper mechanic integration.
- Existing dirty worktree contains many prior Event005 focus/release/doc changes that were not part of this tranche.
