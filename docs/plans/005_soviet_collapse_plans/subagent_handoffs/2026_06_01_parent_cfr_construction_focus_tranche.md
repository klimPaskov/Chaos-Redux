# Event005 Parent Handoff - CFR Construction Focus Tranche

## Scope

Parent patch for the Civilian Factory of Russia focus tree and CFR construction helpers.

## Files Changed

- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `common/scripted_effects/005_soviet_collapse_effects.txt`

## Gameplay Changes

- Added visible reciprocal mutual-exclusion pairs to CFR governance and strategy choices while keeping the existing hidden four-route locks intact. This avoids long mutually exclusive path lines crossing unrelated focus icons.
- Removed several one-off random construction rewards from CFR focuses and replaced them with CFR-specific mandate, registry, contract-depth, and decision-unlock hooks.
- Strengthened the foreign-contract branch so it advances `cfr_contract_network_depth` through the branch instead of only giving political power or generic pressure.
- Made `CFR_rebuild_russia_without_moscow` call the high-chaos neighbor expansion logic through its CFR helper and directly call the breakaway neighbor conflict plan from the focus reward.
- Kept all flag assets untouched.

## Validation

- Brace balance clean:
  - `common/national_focus/005_soviet_collapse_factory_successors.txt`
  - `common/scripted_effects/005_soviet_collapse_effects.txt`
- No unsupported `<=` or `>=` in touched files.
- `git diff --check` clean for touched files.
- CFR focus blocks have no multi-stockpile direct reward spam.
- New visible mutual exclusions are reciprocal and have no missing target ids.
- `git diff --name-only -- gfx/flags interface/flags` produced no output.

## Remaining Risks

- This is only one focus-tree tranche. Other Event005 chaos and republic focus trees still need similar bespoke reward-depth passes before the full goal can be claimed complete.
- The CFR tree still has broad every-state construction rewards in late industrial focuses; these are intentional identity payoffs, not one-random-state filler, but should be reviewed in the final balance pass.
