# Event 014 country-package final re-audit — 2026-07-12

Audit performed: 2026-07-13

## Verdict

**Completion-ready for the frozen Event 014 country-package scope.**

- P0: 0
- P1: 0
- P2: 0
- P3: 0

The two P1 findings from `event014_country_package_postclosure_reaudit_2026-07-12.md` are closed. A normal-queue Wendigo Pack recruitment window found during this final pass was also closed before this report was written and was re-audited against the updated files. No unresolved country-package finding remains.

This was a read-only gameplay audit. The only file written by this auditor is this report. No gameplay, localisation, asset, spreadsheet, spec, or skill file was edited, and no commit was created.

## Audit authority and scope

The audit re-read:

- `docs/plans/014_cannibalism_plans/subagent_handoffs/event014_country_package_postclosure_reaudit_2026-07-12.md`;
- `docs/plans/014_cannibalism_plans/subagent_handoffs/event014_country_package_postclosure_remediation_2026-07-12.md`;
- the final Event 014 country, unification, Wendigo, focus-closure, decision, scorer, on-action, AI, unit-history, focus, event, localisation, interface, and lifecycle files relevant to the findings and acceptance gates.

Required repository guidance was read first: `AGENTS.md`, `chaos-redux-subagents`, `chaos-redux-events`, `chaos-redux-focus-trees`, and `chaos-redux-decisions-missions`.

The offline `paradox_wiki/` snapshot was used instead of the online Paradox wiki. The required core pages were consulted together with the country, division, unit, national-focus, technology, and equipment pages. Vanilla script-constant, effects, triggers, and script-concept documentation was consulted. Vanilla scorer definitions, `change_tag_from`, template-support, and on-action implementations were used as precedents.

## Closed findings

### Mixed one-Pack/two-Pack capacity

Pass.

- `common/scripted_triggers/014_cannibalism_wendigo_decision_triggers.txt:48-62` defines one shared requested-batch capacity check.
- The ordinary two-Pack gate sets its two-Pack batch and calls that helper at `:74-85`.
- The one-Pack receipt gate uses the same helper in `common/scripted_triggers/014_cannibalism_focus_closure_triggers.txt`.
- Both click-time effects repeat the batch check before any population transaction: `common/scripted_effects/014_cannibalism_wendigo_decision_effects.txt:155-189` and `common/scripted_effects/014_cannibalism_focus_closure_effects.txt:389-427`.

At a live capacity of 12, count 11 accepts the one-Pack receipt batch and rejects the ordinary two-Pack batch. A rejected batch reaches neither population consumption nor Larder payment. This holds for every even capacity tier because both paths compare the complete requested post-batch count with the same live capacity.

### Active-enemy receipt epochs

Pass.

- `common/scripted_effects/014_cannibalism_focus_closure_effects.txt:194-231` clears and initializes a target epoch from its current casualty counter, granting no first-sample receipt.
- `:233-266` prunes the actor-owned tracked-country registry, clears inactive target epochs, rebuilds only the still-active set, and fully clears all registered epochs on shutdown.
- `:279-330` records only positive casualty growth, resets the snapshot and remainder on a counter decrease, preserves the same-war issued count, and enforces the per-enemy and actor-pool caps.
- `:333-353` prunes before each bounded `every_enemy_country` sample and initializes a fresh epoch for newly encountered enemies.
- `:364-382`, called from `common/on_actions/014_cannibalism_on_actions.txt:15-17`, resets the epoch immediately when a new war relation is added. The offline wiki and vanilla both define ROOT as the attacker and FROM as the defender; the helper handles either side being the Wendigo actor.
- `:356-362` and `:616-627` clear the registry, target epochs, actor pool, cooldowns, and receipt/muster flags on shutdown, route break, terminal lock, capitulation, annexation, and Event 014 cleanup.

Continuous war, newly encountered enemy, peace followed by re-war before the next pulse, ordinary inactive-enemy pruning, casualty-counter decrease, route break, and terminal lock all retain a non-retroactive bounded result. No recurring whole-world country scan was introduced.

### Immediate paid-only Wendigo Pack contract

Pass after final closure.

The original Event 2 profile deliberately sets `force_allow_recruiting = yes` for the locked `Wendigo Pack` in `common/scripted_effects/zombie_special_project_effects.txt:2646-2660`. The offline Division Modding reference confirms that this permits normal recruitment from a locked template.

The final transformation now closes that permission before player interaction:

1. `common/scripted_effects/014_cannibalism_wendigo_effects.txt:257-288` transforms the selected existing original-ZZZ host in place, creates or preserves the inherited template package, then immediately calls `cannibalism_wendigo_focus_preserve_pack_contract`.
2. `common/scripted_effects/014_cannibalism_wendigo_focus_effects.txt:80-99` locks the template package and sets `Wendigo Pack` to `force_allow_recruiting = no` when the template exists.
3. Only after that call does the transformation open inherited paid contracts, install the public leader, build anchors, and load the focus overlay (`014_cannibalism_wendigo_effects.txt:289-307` and `:471-485`).

The contract helper is idempotent: its AI strategy writes are guarded by `cannibalism_wendigo_pack_contract_ai_applied`. Later focus calls preserve the same queue lock without duplicate AI additions.

All other live calls to `weaponized_zombie_unlock_profiled_template` are inside Event 2 effects that create and initialize new outbreak countries. Event 2 recurring country handling explicitly excludes the Event 014 Hannibal country, so the transformed host has no later recurring path that re-enables normal Pack recruitment.

The closure changes only template lock/recruitment permission and guarded AI preferences. It does not load an OOB, replace the country, recreate existing units, remove technology, remove ideas, clear equipment, or reset zombie-profile state. Original-ZZZ identity, territory, units, templates, technologies, ideas, equipment, and Event 2 profile state are preserved.

The authored paid Pack paths remain available after their intended focus unlocks:

- `cannibalism_wendigo_focus_open_the_pack_musters` sets both ordinary Pack training and receipt-muster unlock flags in `common/scripted_effects/014_cannibalism_wendigo_focus_effects.txt:292-298`;
- the ordinary two-Pack decision remains wired through `common/decisions/014_cannibalism_wendigo_decisions.txt:88-115`;
- the one-Pack receipt decision remains wired through `:275-303`;
- neither scripted spawn depends on normal queue permission.

## Country-package acceptance evidence

### Original ZZZ and player control

- Wendigo unification selects the live original-ZZZ survivor and mutates it in place. It does not release a substitute country or reload its OOB.
- A human primary donor transfers control with `change_tag_from` before donor annexation when the selected ZZZ is AI. A human ZZZ remains controlled by that player. If both countries are human, the donor is not silently annexed at reveal and retains an explicit response route.
- Ordinary CBL creation and later human absorption likewise transfer player control before annexation.
- Public reveal state is written before public cosmetic, leader, focus, decision, report, news, or audio-facing identity changes.

### Population, Deaths, Larder, equipment, and Pack output

- Ordinary and receipt Pack gates validate actor resources, exact state validity, and the complete requested batch before population consumption.
- The canonical Event 014 exact-population transaction records the state loss through the shared Deaths-aware path and requires the applied loss to equal the exact request before any Larder/equipment payment or unit creation succeeds.
- The receipt sampler reads enemy military `casualties` only. It does not call the population/Deaths transaction and cannot double-count military losses as Event 014 Deaths.
- The receipt muster still consumes one receipt, 100K controlled-state population, 200 Larder, 500 infantry equipment, and 100 support equipment; it credits the configured 50 percent manpower share and creates one Pack only after exact payment succeeds.
- `common/scripted_effects/014_cannibalism_wendigo_decision_effects.txt:135-152` creates every paid Pack with the configured zero starting equipment and zero starting manpower factors. The ordinary and receipt paths pass batches of two and one respectively.
- Both original ZZZ OOB variants retain exactly sixteen `wendigo_zombies` battalions and no support company in the base `Wendigo Pack`. Focus stages add recon, engineer, and logistics once without changing the battalion count.

### Route-aware AI and targeting

- The four origin AI profiles remain distinct and terminate when their route conditions no longer apply.
- The shared scorer contract matches the offline wiki: scorer `target_trigger` uses actor ROOT/default and candidate FROM; scorer `score` uses candidate THIS/default and actor FROM. `common/scorers/country/014_cannibalism_target_scorers.txt:4-11` now documents that split correctly.
- Both scorer target triggers use explicit actor-ROOT/candidate-FROM aliases; the six unified and two Wendigo targeted decisions retain their decision-scope wrappers.
- Ordinary Pack, receipt Pack, inherited-cell, terminal-hunt launch, and terminal-hunt press AI paths require the relevant payment plus the countdown Larder reserve. Duplicate Pack-contract and pre-lock target-priority AI writes are guarded.
- Scorer work remains bounded and one-shot. Receipt work uses the existing Event 014 pulse and a narrow relation-added hook; no new daily, weekly, or monthly world iteration exists.

### Submission, resistance, and absorption

- Absorption preserves compatible technology additively, migrates route/origin knowledge, Larder, commanders, bound servants, wars, troops, and destination cores before source cleanup.
- Human-country safeguards prevent one human from silently displacing another. Submission is available only when control can be preserved; resistance and challenge retain an independent country and enter the authored conflict path.
- Reusable CBA-CBH slot cleanup remains generation-safe and does not release a slot until stale country/state references have been cleared.

### Terminal transition and cleanup

- Final Wendigo lock remains pulse-owned. A focus cannot directly set the terminal world-end state.
- Terminal lock calls `cannibalism_clear_wendigo_prelock_operation_runtime` before setting the locked/world-end state. Route break, capitulation, annexation, and global cleanup call the same bounded runtime cleanup.
- Cleanup removes hunt, cell, receipt, cooldown, and pre-lock decision runtime while preserving original ZZZ, its identity and territory, paid formations, inherited templates, structural Pack/support stages, commander traits, technology, ideas, equipment, and retained Event 2 state.

## Findings by priority

### P0

None.

### P1

None.

### P2

None.

### P3

None.

## Simplifications, omissions, and blockers

No fallback, placeholder, generic replacement country, skipped origin, skipped response route, free normal-recruitment substitute, hardcoded replacement for the constant-backed payment model, missing route AI package, or weaker cleanup substitute was found in the audited country-package scope.

There are no remaining country-package blockers. This report is a definition-level re-audit of the frozen files requested by the parent; it does not claim an in-game runtime session was performed.

## Skills used

- `chaos-redux-subagents`
- `chaos-redux-events`
- `chaos-redux-focus-trees`
- `chaos-redux-decisions-missions`

No skill was created or updated.
