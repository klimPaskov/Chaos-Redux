# Event 012 Africa final completion audit — 2026-08-01

## Verdict

Event 012 is load-safe by static evidence, but the requested complete package is not complete and must not be represented as complete.

The implemented core is suitable for an in-game consumer pass without known missing Event 012 event ids, focus load targets, custom GFX definitions, GFX texture paths, or localisation keys. Functional gates remain deliberately closed where the repository lacks an exact owner, approved Independence Wave binding, reviewed asset, model, audio right, or atomic world-package receipt.

## Load-safety evidence

- All nine final-tranche commits are ancestors of HEAD and the Event 012 scoped files matched HEAD during the audit.
- 493 Event 012 custom GFX uses were checked against 10,010 mod definitions and 25,078 vanilla definitions; no missing custom GFX id was found.
- No missing texture path was found in the Event 012 GFX definitions.
- All 32 referenced `chaosx.nr12.*` event ids are defined.
- All eight Event 012 focus-tree load targets are defined.
- The final localisation audit reconciled 1,390 source references and 598 event references with zero missing keys and zero duplicate Event 012 keys.
- The HOI4 event inspector resolved the Event 012 namespace and returned a partial bounded graph without a blocking diagnostic. The HOI4 focus inspector resolved `common/national_focus/012_africa_continental_focus_tree.txt` successfully.

This is static evidence, not a live-game acceptance result. The project rule reserves live-game consumer validation for the user.

## Acceptance coverage

- Actions: 102/102 concepts have a registered contract, selector, dispatch path, duration profile, outcome record, AI surface, localisation, and disposition. Ninety are implemented and twelve remain explicitly gated.
- Focuses: 405 unique focus ids are present. The seven constitutional routes and nine overlays reconcile to 77 implemented payoff rows and one queued external world-order row in the 78-row ledger.
- Priority members: thirteen packages are conditionally reachable on existing Independence Wave tags. DYX/Luba, DZX/Lunda, and EMX/Kilwa remain dormant because no approved exact Event 006 state binding exists. No new tag or fallback state was introduced.
- AI: all 64 profile predicates, loaders, and registry calls exist. Scramble material-readiness classification and executable probability evidence remain unresolved.
- Assets: all 239 matrix rows have a disposition: 50 installed runtime, 21 installed dormant, 133 deferred controlled-pool, 16 deferred model-required, 12 deferred runtime-gated, and 7 deferred unique-package-required.
- Achievements: exact owners were added for the rival-confederation and measured diaspora cases, and disaster backfire evidence was corrected. The full 44-achievement requirement is not satisfied because several exact lifetime and ownership proofs remain unavailable.
- Documentation and catalog: the Event 012 overview, world-order notes, ledgers, handoffs, asset matrix, workbook Event 12 status cells, and exported Event 12 CSV row were reconciled.

## Definition-only and ownership findings

The static reachability scan found 51 Event 012 helpers with no non-definition text reference. This does not create a parser or load error, but it prevents a completion claim until each helper is either connected to an exact owner or formally retired.

High-risk functional examples are:

- `africa_priority_member_record_rival_bloc_victory` now has a bounded `on_capitulation` caller for a rival priority member defeating the current host; ordinary peace remains intentionally non-qualifying.
- `africa_world_terminal_protocol_cleanup_after_identity`, which awaits the atomic terminal identity consumer.
- `africa_priority_member_cleanup_runtime` now has a bounded `on_annex` caller after achievement and world-package loss evaluation; it clears only transient package mission/relationship state while preserving lifetime proof flags. Live annexation-consumer acceptance remains open.
- `africa_rsa_allied_settlement_is_complete` and `africa_rsa_civil_war_first_proof_satisfied`, which are currently consumer-facing proof APIs without a static caller.
- `africa_select_mapped_first_proof_action`, `africa_confirm_all_required_first_proof_regions`, `africa_confirm_first_proof_domestic_settlement`, and `africa_confirm_first_proof_reform`, whose orchestration ownership is not proven.
- Thirteen achievement recorders without an exact caller, covering development and diaspora projects, civilian disaster weaponisation, disease containment, model-based elephant proofs, forced-relocation/scenario proof, other-world-end proof, socialised projects, and the terminal super-event. The common-reserve deployment recorder now has an exact Action 80 and protection-war caller, but its six-war live acceptance is still open. Weather-army defeat and weather-war ownership now have an exact accepted-target plus direct-host-capitulation caller, while row 38's three-target live proof remains open.
- Remaining definition-only helpers are bounded host/contact convenience APIs, five Scramble-interest subpredicates, world counterterm/refusal/completion predicates, reset/breach helpers, and an unused protection-first AI predicate. They are dormant or API-like scaffolding, not evidence that their gameplay is reachable.

Achievement rows 30, 32, and 37 remain fail-closed because exact concession-share, exploitation-scandal, and civilian-damage owners are not available. Row 38 has source owners for target defeat, direct-host campaign victory, member/neutral-target DQs, wrath collapse, and backfire; it remains blocked until three distinct hostile-target capitulations and the remaining live eligibility proof are accepted. Row 33 now has the reserve-war lifecycle owner; it remains fail-closed until six distinct defensive-war scenarios and the deadline/capital/offensive disqualifier paths are accepted.

## Simplifications, omissions, and blockers

- World package W5 is not certified because the six required route, protocol, AI/focus, identity/localisation, asset, and documentation receipts do not exist as authoritative pre-install evidence. No readiness setter or fallback was invented.
- Terminal `The World`, achievement 44, and its four-role atomic super-event remain gated.
- Super-event roles 1 and 4 still require original lossless masters and rights evidence; roles 2 and 3 remain dormant and unwired.
- Action 73 remains gated by fictional-pathogen review and the Event 13 API contract. Actions 74–76 remain model-gated. Other gated rows retain their recorded route or package conditions.
- The target-scoped `days_mission_timeout = FROM.africa_active_action_duration_days` contract has analogous scoped vanilla evidence but no exact vanilla `FROM.` precedent, so runtime parser confirmation remains required.
- DYX, DZX, and EMX require exact approved Event 006 map bindings. HZX, EUX, and ELX remain host-only shells until Event 006 or scenario setup supplies real ownership.
- The focus implementation now has route-aware pressure modifiers on all 107 route-body blocks; static overlay-layout diagnostics and the absence of live branch/world-order acceptance evidence remain.
- The AI audit could not prove Scramble material readiness intrinsically and returned `PROBABILITY_SURFACE_EMPTY` for strategy-plan probability analysis.
- The two requested Afaan Oromoo strings remain absent until complete-string verification and native-speaker review supplies approved text and placement.
- Some portrait, icon, and source-asset provenance remains incomplete. No unreviewed source-language names were added.
- Six episodic families remain intentionally list-only instead of being duplicated into the Charter GUI: Scramble, world order, constitutional crises, post-unification governance, host opening, and regional restorations.
- Partial and failure outcomes remain less bespoke than the successful paths for some shared actions, and the natural-disaster weapon path retains a war-ending edge case.

## Models required later

No model was created in this tranche.

Country visual packages are required for Pan, Gorilla Kingdom, The Green, Living Rivers, Stoneborn, and Ancient Hosts.

Unit or entity models are required for elephant logistics, elephant shock, gorilla heavy infantry, Pan sappers, stone cohorts, riverborn, forest giants, oracle recon, disaster wardens, and plague carriers.

Actions 74–76 and achievements 18, 35, 36, and 40 remain model-gated, with related AI and asset rows gated alongside them.

## Final classification

No hard Event 012 missing-reference or asset-path load blocker was found. The package is intentionally incomplete at the functional and content layers listed above. Continue with exact owners, approved Event 006 bindings, W5 receipts, super-event rights/audio, native-language review, scenario acceptance, and later model production; do not replace those dependencies with fabricated tags, states, receipts, or fallbacks.
