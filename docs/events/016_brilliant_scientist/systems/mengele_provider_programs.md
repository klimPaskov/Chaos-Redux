# Mengele provider programs

The fifteen Event 016 provider families are available through three native decision categories after the Directorate project registry and valid program-owner gates.
The user approved this category split on 2026-09-26.
The grouping is a parent implementation choice within that approval.

| Category | Families |
| --- | --- |
| Conventional Programs | Computation, Electronics, Materials, Rocketry, High Energy |
| Biological Programs | Biomedical, Cloning, Paleogenetics, Xenobiological Synthesis, Biological Weapons |
| Advanced Programs | Teleportation, Robotics, Alien Arms, Temporal, Singularity |

## Stage flow

Each family follows Theory, Prototype, Deployment, and Weaponization through its existing private receipt logic.
A family shows its running or next eligible stage; the exact predecessor and empty-receipt gates prevent another stage from starting concurrently in that family.
Each category contains five family chains and twenty stage definitions.
The category regrouping preserves the decision bodies, costs, timers, cancellation, rewards, and AI formulas.
The existing Clone Directorate category retains its campaign, incident-recovery, construction, and terminal decisions.

Six primary actions is the repository's content and interaction budget, not a documented HOI4 engine row limit.
The three-category grouping makes the fifteen independent family choices easier to navigate.
The legacy category's action density is a separate usability review; it must not be described as a proven engine clipping defect from decision counts alone.

## Costs and native completion

The custom cost rows for Cloning, Paleogenetics, Xenobiological Synthesis, Alien Arms, and Temporal have base, blocked, and hover strings for all twenty stage actions.
The blocked variant preserves the quoted amounts and icons and displays them in red when the combined affordability gate fails.
The full cost-row hover lists every dynamic payment amount and the factory assignment, and explains when they are paid or released.
The ordinary cost detail keeps the reservation and payment timing concise without duplicating the inline amounts.
Cancellation and unsuccessful settlement continue to refund only the exact recorded direct payment.

The user directed on 2026-09-26 that a matching native completion must leave an already active paid provider timer unchanged.
The native settlement helper therefore rejects that provider transition while its family receipt is active.
The existing decision lifecycle remains responsible for finishing or cancelling that receipt.

## Category artwork and wiring

| Category ID | Existing sprite | Texture and owning registry |
| --- | --- | --- |
| mengele_conventional_programs_category | GFX_decision_category_brilliant_scientist_directorate | gfx/interface/016_brilliant_scientist/directorate/decision_category_directorate.dds, interface/016_brilliant_scientist_directorate.gfx |
| mengele_biological_programs_category | GFX_decision_category_brilliant_scientist_krg_exotic_biological | gfx/interface/decisions/016_brilliant_scientist/categories/decision_category_exotic_biological.dds, interface/016_brilliant_scientist_kruger_state_decisions.gfx |
| mengele_advanced_programs_category | GFX_decision_category_brilliant_scientist_krg_portal_temporal | gfx/interface/decisions/016_brilliant_scientist/categories/decision_category_portal_temporal.dds, interface/016_brilliant_scientist_kruger_state_decisions.gfx |

Category visibility and priority are registered in common/decisions/categories/germany_mengele_categories.txt.
Titles and descriptions are in localisation/english/016_mengele_provider_program_categories_l_english.yml.
The source decision wrappers remain in their existing common/decisions/016_mengele_* files.
The three category images are reused; no artwork or model asset is produced by this navigation change.

## Reference evidence

The connected reference routes returned both available required source kinds with no omitted sources.
The script-documentation source kind was unavailable; installed markdown documentation and the offline wiki were available.

| Source | Read span | Revision |
| --- | --- | --- |
| Offline paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md, Basic creation | 44-78 | 7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162 |
| Same page, Decision cost | 284-336 | 7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162 |
| Installed common/decisions/_documentation.md, Country Decisions | 1-46 | 5e7e686b5582f32c38d898d805e17171e88f3bfeee4a030deb1884f9726de019 |
| Vanilla common/decisions/AFG.txt, political_actions category grouping | 1768-1787 | Source-lookup revision e60db9131a086f16cf4fa878089e27c22d7067ca02c67337c4960429ba9550ec |
| Repository .agents/skills/chaos-redux-scripted-gui/SKILL.md, content and interaction budget | 34-40 | Read directly from current worktree |
| Offline paradox_wiki/Localisation - Hearts of Iron 4 Wiki.md, key syntax and texticons | 61-96, 221-247 | SHA-256 1A8F72362A34B4BB653186746B9FAE0B98E463205CB02F12CCF2C3D9CCD3A064 |
| Installed localisation/english/decisions_l_english.yml, custom cost suffix precedent | 49-54 | SHA-256 ED305836A44B0CE34CBB361F7EA5FF08C84DB51795F99C3EEB91A4606ECBF4A4 |

## Validation and remaining work

Source review verifies sixty unique stage decisions, twenty in each category, with five complete stage chains per group.
The current localisation audit re-read all twenty full cost hovers after the parent corrected missing direct-payment amounts, and found no remaining wording or token defect.
The dedicated decision inventory resolves sixty provider decisions, twenty per category, with no in-scope unresolved definition or override.
The complete returned artifact was read from the configured local storage and its SHA-256 verified.
The overall inventory is partial because 218 unrelated definitions remain unresolved.
The independent navigation review accepts the bounded source regrouping and verifies family membership, retained legacy operations, and titles and icons.
It retains explicit limits for exhaustive visibility equivalence, hidden-category callback evaluation, and cost-count certification.
Source equality and inventory evidence are in 016_provider_navigation_source_review_2026-10-03.json.
Declared visibility scenario evidence and rendered text fit remain unverified.
Their source/scenario projections do not establish live-game behavior.
No focus, event-log, event-details, evolution, or catalog-facing wording is changed by this navigation and cost-text tranche.

Event 016 remains incomplete beyond this tranche.
Next work includes native Prototype ownership receipts, the legacy cloning-route guard, the CXT lifecycle matrix, current AI scenario evidence, and the broader completion contract.
Future improvements should connect portfolio progress to the existing program status and clarify available native Prototype routes through their current tooltips, without introducing another public meter or scripted GUI.
