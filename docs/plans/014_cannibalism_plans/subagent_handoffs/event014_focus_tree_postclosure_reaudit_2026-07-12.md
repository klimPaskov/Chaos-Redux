# Event 014 Focus-Tree Post-Closure Re-Audit

> **Historical snapshot.** The closure facts below were later promoted into
> the consolidated Event 014 focus audit and package status. Refer to those
> current authorities for counts, assets, and completion state.

> The former fourth-origin and Lockhouse references in this historical snapshot are superseded by the three-origin correction. Prison and detention remain ordinary mechanics, not a Prison Host route.

Date: 2026-07-13
Requested audit-series date: 2026-07-12
Mode: independent read-only gameplay, AI, localisation, and asset audit

## Verdict

**The Event 014 focus gameplay and asset closure passes this re-audit.**

No P0 or P1 gameplay finding remains. The three tree families are structurally complete at 72 warlord, 108 unified, and 28 Wendigo focuses. The frozen scorer, Pack, receipt, terminal-hunt, AI-reserve, localisation, and asset remediations resolve the defects found during the audit.

Repository-wide Event 014 completion was still **incomplete at this audit snapshot** because the accepted closure facts had not yet been promoted into the source-of-truth documentation and matrices. That reconciliation was queued to the documentation curator. One P3 engine-limited AI behavior is recorded openly below; it is bounded and does not fail the focus gameplay closure.

| Severity | Count | Result |
| --- | ---: | --- |
| P0 | 0 | No load-, data-, or terminal-path blocker found |
| P1 | 0 | No remaining gameplay, AI-completion, localisation, or asset blocker found |
| P2 | 1 | Closure facts still required documentation reconciliation at audit time |
| P3 | 1 | A pre-lock target keeps its first assigned score band until the separate post-lock rescore |

## Structural proof

| Tree | Focuses | AI blocks | Focus-specific helper calls/definitions | Result |
| --- | ---: | ---: | ---: | --- |
| Regional warlord | 72 | 72/72 | 72/72 | Pass |
| Unified command | 108 | 108/108 | 108/108 | Pass |
| Wendigo overlay | 28 | 28/28 | 28/28 | Pass |

Across all three files there are 208 unique IDs. The graph audit found no duplicate IDs, missing prerequisite or mutual-exclusion targets, cycles, asymmetric exclusions, coordinate collisions, orphaned nodes, or invalid relative-position chains. The files use absolute positions. Every unified focus calls `cannibalism_unified_focus_finalize_reward` exactly once.

The route depth remains distinct rather than copied:

- Warlord: six-node survival trunk, three hierarchy routes, three Larder methods, military convergence, four four-focus origin overlays, regional expansion, and three Evolution II end routes.
- Unified: opening convergence, three disposition routes, three hierarchy routes, four Larder methods, army/navy/air, cells, continental expansion, counterwar, and the ordinary terminal chain.
- Wendigo: five-node merge, winter, recruitment, inheritance, and countdown groups plus the three-focus alternate terminal.

Tree loading is explicit and correctly gated: the warlord tree loads after paid country creation, the unified tree after public unification, and the Wendigo tree only for the revealed original-ZZZ merged actor. No generic fallback tree is used.

## Target scoring and AI proof

The scorer contract is corrected and matches the offline wiki/vanilla contract:

- scorer `target_trigger`: actor in ROOT/default, candidate in FROM;
- scorer `score`: candidate in THIS/default, actor in FROM;
- targeted decisions: actor in ROOT/default, candidate in FROM.

`cannibalism_unified_target_scorer` and `cannibalism_wendigo_target_scorer` now call the explicit actor-ROOT aliases `cannibalism_unified_scorer_target_is_valid` and `cannibalism_wendigo_scorer_target_is_valid`. Hard-invalid candidates are excluded for self, alliance/faction/subject relations, capitulation/nonexistence, Event 014 cannibal or actual-nonhuman identity, unusable population, target locks, and lack of a proved war/adjacency/cell/rail/naval/post-lock route.

The shared score represents population, supply, cells, prisons, ports, stability, rail/naval access, coalition command, current war, adjacency, contamination, distance, and overextension. Wendigo adds cold-front preference before lock and population/coalition-capital preference after lock. Pre-lock strategy bands are 150/250/400; post-lock bands are 1000/2000/3000.

Exactly six unified targeted decisions consume `mtth:cannibalism_unified_target_decision_weight`:

1. `cannibalism_unified_collapse_enemy_front`
2. `cannibalism_unified_seed_major_enemy_army`
3. `cannibalism_unified_prepare_global_campaign`
4. `cannibalism_unified_issue_terror_ultimatum`
5. `cannibalism_unified_provoke_border_incident`
6. `cannibalism_unified_destroy_coalition_hub`

`CBL_read_the_continental_weakness` calls `cannibalism_unified_apply_scored_campaign_priorities`, so the focus changes target selection rather than only planning speed. The parent-owned terminal global-war effect calls `cannibalism_wendigo_apply_scored_terminal_priorities` only for the Wendigo branch; it no longer gives that branch blanket equal strategies.

All 208 focuses retain AI weights. The five audited closure/Pack AI spending paths preserve the 800-Larder countdown floor after payment: launch requires 1200, press 1000, ordinary two-Pack training 1040, receipt muster 1000, and inherited cell 950. The Pack-contract AI strategies are guarded by `cannibalism_wendigo_pack_contract_ai_applied`, and the pre-lock target registry prevents repeated focus milestones from stacking the same strategy package.

## Wendigo progression and terminal proof

The Pack remains a locked sixteen-battalion template. `cannibalism_wendigo_focus_preserve_pack_contract` sets `force_allow_recruiting = no`; normal queue recruitment cannot bypass the paid decisions.

- Pack stages add recon, engineer, and logistics support idempotently.
- Island Reavers, Siege Eaters, March Predation Columns, and Lockhouse Columns receive only their inherited, template-specific support upgrade.
- Bound Captain and Winter-Hunt Captain apply only to inherited host commanders/bound servants, exclude Hannibal, and do not coexist.
- The inherited winter-cell operation pays Larder, Command Power, and support equipment, uses a real inherited enemy cell, applies a timed target effect/lock, and has a one-time active-hunt pressure interaction.
- Enemy-death receipts initialize non-retroactively, use 50,000 new casualties, cap at two per continuous enemy epoch and five held receipts, and grant no population, manpower, equipment, Larder, or Deaths entry by themselves.
- Peace/re-war epochs are bounded through the actor-owned tracked-enemy registry plus `on_war_relation_added`; a first or renewed war sample grants no retrospective receipt.
- Receipt muster removes exactly 100,000 state population through the canonical transaction, pays one receipt, 200 Larder, 500 infantry equipment, and 100 support equipment, credits 50,000 manpower, and creates one empty Pack.
- The ordinary trainer creates two empty Packs. Both gates and both click-time effects verify `current count + requested batch <= capacity`, so a mixed one/two-Pack sequence cannot overflow capacity.

The overlay grants +125 Authority before clamping, +15 percentage points of direct Stability, +25 percentage points of direct War Support, and +16 Pack capacity. At the minimum three live anchors the capacity formula is `12 base + 12 anchors + 16 focuses = 40`. The focus route therefore clears the 80-Authority gate while the countdown still requires three anchors, five winter victories, Network Reach, controlled territory, consumed population, 800 Larder, and Chaos strictly greater than 1000.

H-03 normalization passes. Warlord and Wendigo authored percentage/meter ladders use five-point increments. Retained non-five values have exact inline semantic, formula, engine-count, or encoded-factor comments.

Exactly four terminal-hunt surfaces are live: launch, 120-day mission, press, and defender break. Launch plus three presses costs 1000 Larder, 125 Command Power, 1500 infantry equipment, 300 support equipment, and 1500 fuel. Four defender breaks require 40,000 manpower, 120 Command Power, 2000 infantry equipment, and 400 support equipment. Success grants only five transformation progress; failure removes ten. Defender counterpressure, capital control, war end, target invalidation, timeout, route break, capitulation, annexation, terminal lock, and global cleanup all have real resolution/cleanup paths.

`cannibalism_complete_wendigo_terminal_lock` has one live call site, inside `cannibalism_process_wendigo_transformation_pulse`. No focus or hunt effect sets the lock or world end directly. The final lock remains pulse-only.

## Presentation proof

- Focus localisation: 624/624 required title/description/tooltip keys resolve.
- Cross-file Event 014 localisation duplicates: 0 after consolidation.
- All audited English files retain UTF-8 BOM.
- Pre-reveal warlord focus title/description/tooltip leaks for Hannibal, Lecter, or Wendigo: 0.
- Focus icons: 208/208 sprites resolve to 208 existing, SHA-distinct DDS files.
- Closure icons: all six registered hunt/receipt/cell sprites resolve to six existing, SHA-distinct DDS files.
- The closure asset package contains generated sources, processed PNGs, final DDS files, manifest, hashes, validation report, and contact sheets. Manual contact-sheet review found the six closure compositions distinct and readable.

The earlier six-DDS dependency is therefore resolved and is not a blocker in this verdict.

## Findings

### P2 — Source-of-truth documentation reconciliation was pending

At the frozen audit snapshot, the implemented terminal hunt, enemy-death receipt muster, inherited winter cell, structural Pack/origin/commander stages, and exact scorer consumers were not yet reconciled into `docs/events/014_cannibalism/overview.md`, the focus/decision/AI/asset/idea matrices, package status/validation, package manifest, and the live asset ledgers required by the accepted closure addendum.

For example, `decision_mission_matrix.md` still ended with generic Wendigo training and acceleration rows, while `focus_route_matrix.md` described the Wendigo branches only at the pre-closure level. This does not invalidate the verified gameplay, but AGENTS.md forbids a repository completion claim while source-of-truth documentation is stale. The documentation curator owns the queued reconciliation.

### P3 — Pre-lock score bands are intentionally assigned once per target

`cannibalism_wendigo_apply_new_scored_enemy_priority` records every prioritized target in `cannibalism_wendigo_prelock_scored_priority_targets`. Later focus milestones can discover newly valid enemies but do not stack another package or dynamically replace an existing target's low/medium/high pre-lock band if its score changes.

This is a bounded, documented engine limitation rather than a hidden omission: the official effects database exposes `add_ai_strategy` but no scripted removal effect. The separate terminal-lock consumer rescans and applies the correct post-lock 1000/2000/3000 band, so the required pre-lock/post-lock distinction and terminal target scoring remain live.

## Simplifications, omissions, and blockers

No gameplay, AI, localisation, or asset simplification or fallback was accepted. No requested tree, focus, closure decision, target consumer, reward family, or icon is omitted.

The only completion blocker at audit time was the P2 documentation reconciliation. The P3 behavior is recorded above and does not block the gameplay/asset focus closure.

This audit wrote only this handoff. It did not edit gameplay, localisation, assets, specifications, matrices, spreadsheets, or commits.

## Skills used

- `chaos-redux-focus-trees`
- `chaos-redux-events`
- `chaos-redux-decisions-missions`
- `chaos-redux-mtth`
- `chaos-redux-event-assets`
- `chaos-redux-subagents`

No skill was created or updated during this bounded audit.
