# Event005 Soviet Collapse Focus/Release Cleanup Tranche

## Scope

Parent implementation tranche after the full read-only focus audit.

Touched files:

- `common/script_constants/005_soviet_collapse_constants.txt`
- `common/scripted_triggers/005_soviet_collapse_triggers.txt`
- `common/scripted_effects/005_soviet_collapse_effects.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`

Flag assets were not touched.

## Implemented

- Slowed Soviet Collapse follow-on release pacing so the union does not dump every possible successor immediately.
- Kept first-year/base backlog releases restricted to the base republic pool.
- Gated wider internal/vanilla republic dynamic releases behind chaos-tier checks, with full dynamic candidate expansion only at higher chaos tiers.
- Added visible mutual exclusivity to the MFR ownership route split and merged a duplicate bunker construction reward.
- Replaced several exposed random anti-air focus/helper rewards with logistics, rail, infrastructure, factory, bunker, supply, or port rewards that fit the relevant successor.
- Removed copied UDC tooltip and command-network payload usage from the TNC early branch.
- Strengthened Far Eastern/Pacific focuses with Japan-facing opinion, support strategy, decryption, convoy/fuel, dockyard, and port-city rewards.

## Validation

- Brace balance checked on all touched script files: all balanced at zero.
- `rg "<=|>="` on all touched files: no unsupported operators found.
- `git diff --check` on all touched files: clean.
- `git status --short -- gfx/flags interface/flags`: no flag or flag-interface changes.

## Remaining Work

- The full Soviet Collapse focus-tree suite still needs a deeper route-layout pass: clean three-branch industry/political/expansion structures, fewer decorative mutual exclusions, and better pathline spacing across all republics.
- Some older anti-air rewards remain outside this tranche and should be reviewed country-by-country rather than blindly replaced.
- The broad focus reward system still has older generic helper calls in some trees; those should be replaced with country-specific mechanics where the branch identity is currently weak.
- This tranche was not committed because the larger focus-tree cleanup goal is not complete.
