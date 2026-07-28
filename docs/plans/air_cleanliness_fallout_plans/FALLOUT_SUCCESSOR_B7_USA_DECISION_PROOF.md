# Fallout successor B7 USA continuity project proof

Status: dormant static implementation added on 2026-07-28. This tranche is a bounded successor proof and is not release-floor credit.

## Scope

The project category is visible only while the current USA B7 package receipt, the current generation receipts, and the controlled continuity capital are valid. It is not called by the Fallout consequence, blackout, Event Log, evolution catalog, or ordinary Fallout scenario registry.

The category exposes five actions.

| Decision | Route gate | Commitment | Visible result | Memory receipt |
| --- | --- | --- | --- | --- |
| `fallout_usa_repair_inland_depot` | Inland Corridors | 900 infantry equipment, 6 trains, 1 civilian factory for 70 days | Two infrastructure levels and one railway level in the frozen capital | `fallout_usa_logistics_memory = 2` |
| `fallout_usa_muster_guard_compacts` | Guard Compacts | 12,000 manpower, 1,600 infantry equipment, 350 support equipment, 15 Command Power | 25 Army Experience and 6 percent War Support | `fallout_usa_security_memory = 2` |
| `fallout_usa_ratify_lakes_charter` | Regional Partners | 10 convoys and 20 Command Power for 84 days | 8 percent Stability and 75 Political Power | `fallout_usa_diplomacy_memory = 2` |
| `fallout_usa_sweep_radio_dead_zones` | Continental Radio Net | 240 support equipment and 15 Command Power | 10 Air Experience with 10 net Command Power after the survey reserve | `fallout_usa_information_memory = 2` |
| `fallout_usa_launch_federal_reconstruction_drive` | Federal Reconstruction | 12 trains and 1 civilian factory for 105 days | One industrial complex and one infrastructure level in the frozen capital | `fallout_usa_reconstruction_memory = 3` |

Every action is one-shot for the current generation because successful completion writes a route flag. The current project trigger also rejects a stale package, a continuity error, a lost capital, and insufficient real resources. Cancellation records a current-generation failure receipt and removes 4 percent Stability and 4 percent War Support.

## AI and cleanup

The five decisions use route-specific AI factors from `fallout_successor_b7_project_ai`. War increases willingness for each action through one shared crisis multiplier. The additive `fallout_usa_b7_continuity_plan` keeps the AI focus order on the seven authored B7 focuses and is enabled only for an AI USA with current package receipts.

`fallout_successor_b7_cleanup_usa_project_memory` is called by the existing successor-ledger reset. It removes any active project decisions and the four B7 ideas, clears focus and project flags, and clears every project generation and memory variable. It does not replace or modify the ordinary USA focus tree.

## Engine-sensitive boundary

The implementation mirrors the documented decision category, custom cost, timed removal, capital scope, equipment, manpower, Command Power, building, and focus-plan surfaces. Runtime visibility, cost consumption, capital mutation, AI selection frequency, save recovery, multiplayer host behavior, and cleanup timing remain unobserved because HOI4 was not launched.

## Remaining gaps

This tranche does not provide the general successor allocator, a complete USA focus tree, a dedicated USA leader or advisor package, a full diplomatic target registry, a unit package, or final independent visual approval. Those remain explicit B7 and global Fallout blockers.
