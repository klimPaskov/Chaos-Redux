# IW-043 / IW-058 vanilla formable guard handoff — 2026-07-18

Owner: `chaosx_decision_mission_auditor`

## Documentation reconciliation note (2026-07-18)

The compatibility guard remains current: ordinary and Event 005 CHU/ASY
behavior is preserved, while exact Event 006 carriers cannot use the vanilla
shortcuts. The later exact-carrier transaction audit supersedes this
handoff’s statement that no Event 006 formable is enabled and that all
attestations are unwritten. FORM-12/13/18 now operate only for the admitted
CHU/ASY carriers under their consent, anchor, paid-congress, and staged
integration contracts; historical guard validation below is unchanged.

## Scope and changed files

- `common/scripted_triggers/006_independence_wave_vanilla_formable_compatibility_triggers.txt`
- `common/decisions/zz_006_independence_wave_vanilla_formable_compatibility_decisions.txt`

The new trigger file centralizes two negative compatibility predicates:

- `can_access_vanilla_chu_formable_shortcuts`
- `can_access_vanilla_asy_formable_shortcuts`

They negate the existing exact predicates `is_independence_wave_iw043_country` and `is_independence_wave_iw058_country`. Those existing predicates prove the carrier tag, Event 006 active origin, exact package id, exact package flag, and exclusion of every Soviet Collapse origin marker.

The decision adapter re-declares the current vanilla decision baseline for exactly these IDs:

- `form_idel_uralic_republic` in `form_idel_ural_category`
- `neo_assyrian_empire_decision` in `neo_assyrian_empire_category`
- `neo_mesopotamia_decision` in `neo_mesopotamia_category`

## Before and after behavior

Before this patch, an active Event 006 IW-043 `CHU` could use vanilla `form_idel_uralic_republic`, while an active Event 006 IW-058 `ASY` could use vanilla `neo_assyrian_empire_decision` or `neo_mesopotamia_decision`. Each shortcut applies its vanilla cosmetic, broad core, and global-formation effects without the Event 006 FORM-12, FORM-13, or FORM-18 settlement contracts.

After this patch, the three decisions retain the current vanilla baseline but add one exact `visible` guard:

- IW-043 `CHU` cannot see `form_idel_uralic_republic`.
- IW-058 `ASY` cannot see `neo_assyrian_empire_decision` or `neo_mesopotamia_decision`.
- A normal vanilla `CHU` or `ASY`, including the separate Soviet Collapse flow, passes the negative guard and retains the unmodified vanilla behavior.

At handoff time no Event 006 formable was enabled. The later exact-carrier
transaction pass enables FORM-12/13/18 only for CHU/ASY under their admitted
readiness, consent, anchor, and staged-integration contracts; ordinary and
Event 005 behavior remains guarded as described above.

## Compatibility and override surface

The adapter uses the existing vanilla category and decision IDs, with a `zz_` filename so it loads after the source formable file in the common decision set. `descriptor.mod` replaces only `gfx/loadingscreens`, not `common/decisions`, so the full vanilla formable surface remains loaded. Each affected decision has exactly one source definition in vanilla and exactly one compatibility definition in the mod. The categories also retain their vanilla category metadata from `common/decisions/categories/`; this patch only replaces the three decision records inside their existing categories.

The full current vanilla decision bodies were copied intentionally rather than reconstructing their core grants, map highlights, cosmetic changes, global flags, or AI weights. This makes the guard the only semantic delta and preserves ordinary carrier behavior when the exact Event 006 predicate is absent.

## Decision category lifecycle and mission notes

`independence_wave_iw043_middle_volga_congress_category` and `independence_wave_iw058_council_of_communities_category` keep their existing exact package visibility and their existing paid-action cleanup. This patch creates no category, mission, target, GUI action, AI branch, cost, timer, or cleanup state. It only prevents conflicting vanilla decisions from becoming visible during the active Event 006 package lifecycle.

There is no new mission quality, cost, tooltip, localisation, or AI surface. The three hidden shortcuts have no new player-facing text, so no localisation key was required.

## Meaningful validation

- Normalized comparison of each adapter decision against the current vanilla `formable_nation_decisions.txt` body passed after removal of only its new guard line: all three baselines matched exactly.
- Confirmed `is_independence_wave_iw043_country` and `is_independence_wave_iw058_country` include exact tag, Event 006 active origin, package ID, package flag, and Soviet Collapse exclusions.
- Confirmed one vanilla source definition and one mod compatibility definition for each affected decision ID, and confirmed the descriptor has no `common/decisions` replacement path.
- Reviewed vanilla decision documentation: `visible` is the continuously evaluated country-scope UI gate, which hides an otherwise allowed decision without altering its availability or completion effects.

## Skipped validation and remaining risks

- No live game session was launched. The static check cannot prove the engine's final duplicate-key resolution beyond the standard common-decision override structure, so load-order behavior should be included in the parent’s next task-specific runtime pass.
- The adapter intentionally mirrors the installed vanilla baseline. If a future HOI4 update changes any of these three vanilla decision definitions, this file must be re-compared and refreshed before claiming unchanged vanilla behavior.
- At handoff time FORM-12, FORM-13, and FORM-18 adapter attestations were
  unwritten and fail-closed. The later exact-carrier pass supersedes that
  status for CHU/ASY; wider family promotion remains outside this handoff.

## Simplifications, omissions, and blockers

No fallback, formable enablement, tag change, broad decision removal, or Soviet Collapse alteration was used. The requested compatibility guard is complete, but the wider FORM-12, FORM-13, and FORM-18 implementation remains intentionally blocked by its existing attestation contract.
