# Event 006 formable registry

## Purpose and status

The Event 006 formable registry is the shared discovery and transaction framework for FORM-01 through FORM-48. It replaces family-by-family copied decisions with one profile table, one method and consent surface, and one bounded member and anchor ledger.

All 48 accepted family rows have stable discovery metadata, but the shared
framework does not declare a family operational by metadata alone. FORM-01
through FORM-05 remain promoted from their owning adapters. FORM-48 has a
framework-readiness attestation and a complete carrier/member contract, but it
remains operationally unreachable until an admitted HBX/HAW/FSM member set
exists. FORM-07 now
has a bounded Iberian adapter surface for CAT/NAV/GLC, but remains fail-closed
until its researched X identity, flag package, and identity contract are
approved. FORM-06, FORM-10 through FORM-15, and FORM-17 through FORM-47 remain fail-closed, including FORM-42. FORM-08 now has a reviewed Danubian adapter and framework readiness, but the current geography guard exposes only the TRA 84/76 and AXX 82 selectable anchors. Vojvodina remains the vanilla HUN-origin dynamic overlay, Slavonia remains unbound without an installed-map anchor, and MAC state 106 is a separate Event 006 package anchor rather than a current FORM-08 member. The family therefore remains runtime-inadmissible until a third in-scope member and anchor are explicitly researched and admitted in one generation. FORM-09 is operational for a researched BBX or BAX carrier through the BLX cosmetic identity and exact Balkan member ledger. FORM-16 has its separately documented Transcaucasian adapter. No formable or cosmetic tag is assigned by registry metadata alone; a family still requires its owning package's audited territory, collision-safe X-ending identity, complete flag package, identity adapter, and reviewed integration policy.

The design authority remains docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_6_formables_league_and_scenario.md and docs/specs/006_independence_wave_specs/matrices/006_formable_family_registry.csv.

## Registry profile

common/script_constants/006_independence_wave_constants_registry.txt assigns FORM-01 through FORM-48 stable numeric family IDs and stores one profile row for every CSV entry.

Each row contains:

- Event 006 region;
- supported formation-method bit mask;
- discovery class;
- minimum registered members;
- minimum consenting members;
- minimum territorial anchors;
- AI willingness tier;
- congress risk tier.

independence_wave_focus_register_formable_family calls independence_wave_formable_load_selected_family_profile after the owning package selects its stable ID. The profile is therefore available to the discovery trigger without a copied family decision. Discovery loads it again before opening the transaction, and the profile-family snapshot prevents a later package choice from mutating an open transaction. Method-support flags are derived from the profile mask after loading.

The stored discovery class is enforced by the shared gate. Mature-tree and route families use the common discovery focus; map-state families require independence_wave_formable_map_reveal_ready; league-state families require a league membership, an open league route, or independence_wave_formable_league_reveal_ready; hidden families require independence_wave_formable_hidden_reveal_ready; hidden high-chaos families additionally require the Event 006 high-chaos action gate. These reveal flags are adapter evidence, not substitutes for the final territory and identity attestations.

The working family names are resolved through GetIndependenceWaveSelectedFormableName. These names are presentation labels for the accepted registry rows and do not create country identities.

## Gameplay flow

1. An owning Event 006 package selects one stable family ID and registers the family focus surface.
2. independence_wave_discover_regional_identity verifies the discovery gate, loads the profile, and builds the first member and anchor ledger.
3. The player chooses one supported formation method in the Formation Covenant category.
4. The player chooses a compatible consent rule.
5. A promoted family carrier dispatches one founding proposal. Each invitation stores the carrier country, carrier and invited-member Event 006 generations, family, and proposal sequence; only a reply to that exact live proposal can count. The non-Event-006 BEL delegation uses the documented zero-generation sentinel. A country already bound to another valid live invitation cannot issue or receive a competing proposal.
6. The shared preparation trigger verifies that the territory, identity, flags, and integration adapters are ready before allowing a congress to open.
7. independence_wave_convene_formation_congress is a selectable 360-day congress window. Ratifying it pays the strategic congress cost, rebuilds the ledger, freezes the exact proposal-bound consent rows, calculates the profile and member risk, and resolves the congress.
8. A successful congress opens the final ratification decision. Failure ends the transaction, invalidates its invitations, and applies the recorded political consequences.
9. independence_wave_proclaim_military_union, retained as a stable legacy decision ID, presents a dynamic Ratify title and pays the method-specific commit cost.
10. Identity and integration adapters run only after readiness and family-specific mutation preconditions pass in the same effect chain.
11. A successful integration adapter marks the transaction committed and may publish a bounded state array for independence_wave_integrate_member_region.

No on-action, daily pulse, all-country scan, or all-state scan is used. Ledger passes run only when discovery or preparation is explicitly taken and iterate global.independence_wave_active_countries.

## Formation methods and consent rules

The shared methods are:

- negotiated federation;
- dynastic or traditional union;
- revolutionary union;
- military settlement;
- league transformation;
- hidden high-chaos proclamation.

A family can expose more than one method without receiving copied decisions. The family profile mask determines which generic choice appears.

The shared consent rules are:

- voluntary membership, which requires the family minimum and rejects an openly opposed registered member;
- unanimous compact, which requires every registered member to consent;
- controlled settlement, which is restricted to military and hidden methods and requires controlled territorial anchors.

For FORM-01 through FORM-04, even the proposer counts only after its self-invitation is paired to the live proposal. Non-proposers remain observers until they answer that carrier's exact invitation. independence_wave_formable_declare_consent_for_selected_family and independence_wave_formable_withhold_consent_for_selected_family accept only a pending invitation whose carrier, generation, family, and sequence still match. The binding cannot be overwritten while that proposal remains valid. The congress rebuild freezes those exact accepted rows before commitment; a family-only declaration, a stale reply, or a reply to a competing carrier never authorizes mutation. AI response decisions use the same pending-invitation gate.

FORM-09 uses the same paid full-integration, autonomous-membership, and refusal decisions. Its AI resolver records one of those exact responses immediately after the proposal snapshot is stored. The congress treats all other FORM-09 candidates as observers, and the integration adapter rechecks the frozen accepted invitation before touching a member.

The conservative generic willingness model remains available only to registry families that have not adopted an exact invitation contract. It never substitutes for an explicit response in those operational adapters.

This generic willingness is intentionally conservative. An owning family may add a more exact consent declaration, but it must not erase the player-observer safeguard.

## Member and anchor ledger

The proposer owns four aligned arrays:

- independence_wave_formable_member_country_entries;
- independence_wave_formable_member_generation_entries;
- independence_wave_formable_member_anchor_entries;
- independence_wave_formable_member_consent_entries.

A candidate row is admitted only when the country is a valid current Event 006 generation, selected the same formable family, and has a persisted Event 006 anchor. Counts and the bounded integration-state array are rebuilt from those rows.

During proposal dispatch the carrier also owns aligned invited-country and invited-generation arrays. They are the bounded cleanup list if a member leaves the active registry before the proposal closes. Accepted congress rows receive a second carrier, generation, family, and proposal-sequence snapshot; the strict mutation triggers require this frozen snapshot as well as the aligned consent ledger.

The generic ledger is evidence of active Event 006 membership, not a substitute for the family's territorial specification. The family territory adapter must still validate the exact required states, capital alternatives, exclusions, and ownership or control rule before setting independence_wave_formable_territory_adapter_ready.

independence_wave_integrate_member_region targets only independence_wave_formable_integration_state_entries. It no longer searches every state while the decision category is open.

## FORM-01 through FORM-04 founding proofs

- FORM-01 requires living SCO, WLS, and BRI founders. Every non-carrier founder needs an actual faction, non-aggression, access, or guarantee relation with the carrier. The carrier and every fully integrating founder prevalidate its full compact: SCO states 121 and 133, WLS 122, and BRI 14.
- FORM-02 requires GZX and any two of ICE, scenario-created AKX, and SCO. Every accepted member must control its certified port anchor and have a verified treaty relation with the carrier; the carrier must also possess nonzero convoy capacity. The accepted sources do not define a larger safe-reserve threshold or an engine-computable pairwise sea-route formula, so none is invented. AKX is admitted only with independence_wave_scenario_origin and package IW-011. The carrier and every fully integrating founder prevalidate its full compact: SCO states 121 and 133 and the other compact states 100, 337, and 331.
- FORM-03 requires an AFX or AGX carrier and at least one connected, exact invited consent from the other core carrier or BEL_flanders. Only the second AFX or AGX core anchor can integrate. BEL remains sovereign at founding, and HOL/LUX remain post-charter sovereign associates; states 6, 7, 8, 35, 977, and 980 are outside the transfer contract.
- FORM-04 requires living RHI and AJX, capitals in states 51 and 42, direct capital-state adjacency, national adjacency, peace between the founders, and German non-control of both states. A stronger living Germany is not a player-facing prohibition. AI carriers avoid the proposal when carrier-to-Germany strength is below 0.67, meaning Germany is roughly one-and-a-half times stronger, unless the accepted Rhenish/Bavarian high-chaos action gate is open.
- FORM-08 currently admits only the researched selectable Danube anchors TRA state 84 (with optional state 76) and AXX state 82. MAC state 106 remains a separate Event 006 package anchor and is not a current FORM-08 member under the geography guard. Vojvodina remains the HUN-origin dynamic overlay, Slavonia remains unbound without a unique installed-map anchor, and the family requires three in-scope members, three anchors, and three consents before commit. It reuses the existing vanilla HUN_EMPIRE cosmetic identity and integrates only explicit full-integration rows; non-integrating consenting members retain sovereign Event 006 origins with directional access and guarantees.
- FORM-09 requires a researched BBX or BAX carrier plus two additional consenting reviewed anchors from the Balkan member set. The exact anchors are BBX 185, BAX 184, BOS 104, MAC 106, and MNT 105. All five anchors have admitted package contracts, while each invitation still requires its package, generation, territory, identity, consent, and frozen-snapshot proofs. The carrier adopts BLX, full-integration members transfer only certified compact territory and military assets, and autonomous members retain their country, package, tree, territory, and forces. A paid Federal Border Board project closes the post-formation settlement.

## Costs, time, and risk

The congress uses the existing strategic cost palette and a 360-day ratification window.

Commit costs depend on the selected method:

- negotiated, dynastic, and league methods pay strategic and standard administrative costs;
- revolutionary union pays strategic and standard security costs;
- military and hidden proclamations pay strategic and major security costs.

Congress failure risk begins with the family tier, then responds to opposed members, observers, controlled anchors, surplus consents, and the more coercive formation methods. Tuning is centralized in independence_wave_formable_risk. The random list uses an explicit success weight and failure weight whose sum is 100.

## Transaction lock and cleanup

has_independence_wave_formable_transaction_lock covers congress preparation, formation-ready state, and commit state. has_independence_wave_active_formable_operation also recognizes:

- independence_wave_sco_convene_maritime_conference;
- independence_wave_wls_convene_celtic_council;
- independence_wave_afx_convene_meuse_industrial_conference;
- independence_wave_agx_convene_north_sea_coastal_conference;
- independence_wave_rhi_convene_rhine_congress;
- independence_wave_bay_convene_south_german_estates;
- the bounded member-region integration decision.

Failure clears ready and commit state, removes the generic congress, records the failure state, invalidates every invitation in the bounded proposal list, and applies the congress failure consequence. Generation cleanup removes the method, consent, profile, proposal, ledger, adapter attestations, and transaction flags.

FORM-01, FORM-02, and FORM-04 autonomous settlements record the exact carrier, carrier Event 006 generation, and four directional ownership flags for military access and guarantees. Cleanup walks the frozen founding ledger before clearing it, accepts only the exact carrier-generation-family pairing, removes only relations whose Event 006 ownership flag is present, and then clears the member idea and pairing. Pre-existing access or guarantees are never claimed by this system and therefore survive cleanup. FORM-03 sovereign associates use their separate charter lifecycle and are not traversed by this cleanup.

FORM-48 uses the same directional-ownership rule through its private `has_independence_wave_form48_current_autonomous_binding` trigger. The trigger runs in HAW/FSM member scope, takes no caller-supplied inputs, and requires the saved carrier pointer, saved carrier generation, autonomous FORM-48 family, the member's live Event 006 generation, and the carrier's live Event 006 generation/family to match. It has no outputs or side effects. `independence_wave_form48_remove_event6_autonomous_relations` is its only relation-mutation call site: a stale or cross-generation binding still has its local markers cleared, but cannot remove access or guarantees from another transaction.

### FORM-07 Iberian adapter (current, fail-closed)

FORM-07 binds only the researched CAT/NAV/GLC corridor: CAT state 165, NAV state 792 (the installed-map País Vasco compact anchor), and GLC state 171. Navarra state 172 and French Basque state 806 remain optional NAV extension objectives rather than the compact release/readiness anchor. The adapter requires each package's exact original tag, package ID, Event 006 setup marker, anchor ownership/control, regional-power proof, compatible constitutional or popular-council route, bilateral connection, frozen invitation consent, and the negotiated or revolutionary method/consent policy. It stages autonomous-member relations with directional ownership markers and provides generation-checked integration, rollback, and cleanup effects over the frozen member ledger.

The adapter deliberately does not invent an Iberian X-ending identity or flag. Its readiness registration, identity adapter, commit proof, and integration adapter therefore remain false until a source-approved identity, flag triplet, and identity review set the explicit FORM-07 flags. The all-three corridor proof now has source-level NAV/IW-013 and GLC/IW-015 adapter surfaces, but their independent source/identity/flag/portrait audits and central content attestation remain open. CAT stays outside content attestation and cannot enter automatic or scenario release capacity through this source surface. The implementation files are `common/scripted_triggers/006_independence_wave_form07_triggers.txt` and `common/scripted_effects/006_independence_wave_form07_effects.txt`.

## Family adapter contract

A family adapter must bind its attestations by setting independence_wave_formable_readiness_family to the same stable family ID loaded in independence_wave_formable_profile_family. It must then complete all of the following before a congress can open:

1. Verify the exact territorial proof and set independence_wave_formable_territory_adapter_ready.
2. Reserve and re-audit an unused X-ending country or cosmetic identity and set independence_wave_formable_x_tag_reserved.
3. Provide every required flag size and ideology variant, then set independence_wave_formable_flag_package_ready.
4. Define independence_wave_formable_identity_adapter_<family id> and set independence_wave_formable_identity_adapter_ready.
5. Define independence_wave_formable_integration_adapter_<family id> and set independence_wave_formable_integration_adapter_ready.
6. Review how living members, subjects, controlled territory, and focus trees survive the settlement, then set independence_wave_formable_member_policy_audited.

The identity adapter must perform its identity mutation atomically and set independence_wave_formable_identity_committed only after success. FORM-01 through FORM-04 additionally require independence_wave_formable_mutation_prevalidated. Their exact country, territory, consent-snapshot, connection, and integration-policy proofs run before the flag is set, leaving the ensuing bounded integration pass deterministic and non-failable. The integration adapter must integrate only registered frozen rows under the selected consent rule and set independence_wave_formable_integration_committed only after success.

The shared readiness trigger rejects attestations bound to any other family. There is no fallback adapter. Setting a readiness flag without the corresponding audited content violates the contract and can dispatch an undefined family helper.

FORM-01 through FORM-04 passed the independent operational re-audit. Each
registration effect clears any prior family bundle first, binds the readiness
variable to its exact family, and then restores only the six generic adapter
attestations and its family-specific proof. FORM-03 additionally restores its
separately audited progression attestation. FORM-05 is promoted through its
own audited adapter. FORM-48 follows the same framework contract: its
registration binds family 48, sets the six shared adapter flags, sets
`independence_wave_form48_registry_surface_registered`, and sets
`independence_wave_form48_readiness_attested` only after the coordinated Pacific
PASS audits. The live commit gate still requires the exact active HBX/HAW/FSM
member set, so the family is not currently operational. FORM-07 remains fail-closed under its identity, flag, and NAV/GLC package contract. FORM-08 has a reviewed identity, territory, member-policy, and dynamic post-formation adapter through the Transylvania carrier, but its minimum three-member proof intentionally remains fail-closed because the current geography guard exposes only TRA/AXX and does not count separate MAC package readiness; Vojvodina is an overlay and Slavonia is unbound. FORM-09 is promoted through BLX with an exact frozen-consent adapter. FORM-16 is promoted through its Transcaucasian adapter. FORM-06, FORM-10 through FORM-15, and FORM-17 through FORM-47 remain fail-closed, including FORM-42.
Earlier FORM-48 handoffs that recorded unset flags are preserved as historical
evidence, not current status.

### FORM-48 Pacific adapter (framework-ready, operationally unreachable)

FORM-48 uses HBX as the carrier and HAW/FSM as sovereign autonomous members.
The family-48 identity adapter applies cosmetic identity `PFX` to the committed
HBX carrier; it does not annex, subject, or replace either member's country
identity or focus tree. The post-formation adapter requires the exact committed
carrier/member generations and uses the dedicated current-generation binding
trigger for relation cleanup. Its hidden-high-chaos presentation path remains
conditional on the live league and action predicates. FORM-42 and all other
unpromoted families remain fail-closed. Current evidence is the 2026-07-18
Pacific architecture, country-package, focus/icon, decision/mission,
localisation, flag/portrait, and postformation handoff chain under
`docs/plans/006_independence_wave_plans/subagent_handoffs/`; the earlier
fail-closed admission wording in those handoffs is historical and preserved.

The current FSM research boundary is `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_fsm_petrus_mailo_source_research_current_2026_08_03.md`: `independence_wave_fsm_sourced_identity_ready` remains unset, so framework readiness is not runtime reachability or package admission. HAW and HBX admission alone does not satisfy the exact HBX/HAW/FSM member contract, and no FORM-48 promotion follows.

## Origin separation and living countries

The shared core never annexes a country, creates a subject, changes a tag, assigns a cosmetic tag, or replaces a focus tree.

When an owning integration adapter is ready to absorb a consenting active Event 006 member, it may call independence_wave_formable_end_consenting_member_origin in that member's scope. The helper rechecks both the consenting ledger row and the frozen invitation-to-carrier snapshot, records formable_absorption, and uses the canonical Event 006 end path. The durable Event 006 origin row remains available. Event 005 active and historical origin state is not modified.

An adapter must not call this helper for an observer or an opposed country. Any annexation, subject arrangement, or institutional preservation beyond that point belongs to the reviewed family policy.

## Localisation and visual assets

The 48 family labels copied into the internal scripted-localisation map come
from the registry column explicitly marked `working_name_not_final_localisation`.
They are not approved player-facing names. Discovery also requires the complete
family-bound readiness proof, so no working label can appear until the owning
family supplies researched final identity text and replaces or explicitly
certifies its mapping.

The shared decisions reuse registered Event 006 sprites:

- GFX_decision_independence_wave_formable_proclamation;
- GFX_decision_independence_wave_league_votes;
- GFX_decision_independence_wave_border_arbitration;
- GFX_decision_independence_wave_integration_missions.

No new decision icon is required by the registry framework.

Every approved family identity still requires a complete flag package before its adapter can be marked ready:

- gfx/flags/<APPROVED_X_TAG>.tga;
- gfx/flags/medium/<APPROVED_X_TAG>.tga;
- gfx/flags/small/<APPROVED_X_TAG>.tga;
- every ideology-specific variant required by that identity.

The owning identity audit must record the approved X-ending tag, collision evidence, localisation keys, flag manifest, identity adapter ID, and integration adapter ID. No placeholder flag or borrowed fallback identity is accepted.

## Future depth

After individual family packages and identities are audited, useful extensions include negotiated capital ballots, subject-federation autonomy policies, congress concessions, and post-formation institutions. Narrative invitation events can decorate the proposal state, but must consume the existing carrier, generation, family, and sequence binding rather than create a parallel consent channel.

The registry should receive new tuning fields only when more than one family can use them. Exact territory and identity evidence remains in the owning family adapter and audit.

## FORM-03 post-charter consumer

The LCX Confederation of Low Countries is carried only by a committed AFX or
AGX FORM-03 transaction. Its post-charter consumer starts after the shared
transaction sets active and committed state and applies the ordinary commit
outcome. It owns two public values, a six-focus branch, sovereign-member votes,
bounded carrier and member works, a ratification mission, exact compromise and
rupture outcomes, and guarded cleanup. It never calls transactional rollback
after LCX has formed and never transfers BEL, HOL, or LUX territory.

The complete state-machine reference is
`docs/events/006_independence_wave/systems/form03_progression.md`. Static progression
attestation is restored after the independent audit. Automatic and scenario
release-package readiness remain separate package-level gates; restoring the
FORM-03 adapter does not bypass them. The runtime completion flag is not a
readiness certificate.

## Event 006 state-puzzle consumers

The Event 006 state-puzzle group is declared by fourteen consumer specs in `docs/formables/state_registry/consumers/006_form*_state_puzzle.json`. Each spec uses `group_id = independence_wave_formables`, the shared scripted GUI `independence_wave_formable_state_puzzle_scripted_gui`, the shared window `chaosx_independence_wave_formable_state_puzzle_window`, a family activation helper, and a finite `summary_required_count`. The compiled runtime contains fourteen manifests, 50 candidate-state rows, and 100 DDS state pieces. The family territory helper shown by the window is also required by the player and AI formation gate.

| Family | Candidate states | Summary count | Territory helper |
| --- | --- | ---: | --- |
| FORM-01 | 121, 133, 122, 14 | 4 | `independence_wave_formable_state_puzzle_form01_territory` |
| FORM-02 | 100, 337, 331, 121, 133 | 3 members, with both Scottish compact states | `independence_wave_formable_state_puzzle_form02_territory` |
| FORM-03 | 34, 36, 6 | 2 | `independence_wave_formable_state_puzzle_form03_territory` |
| FORM-04 | 51, 42 | 2 | `independence_wave_formable_state_puzzle_form04_territory` |
| FORM-05 | 1, 114, 115 | 2 | `independence_wave_formable_state_puzzle_form05_territory` |
| FORM-07 | 165, 792, 171 | 3 | `independence_wave_formable_state_puzzle_form07_territory` |
| FORM-08 | 84, 82 | 3 | `independence_wave_formable_state_puzzle_form08_territory` |
| FORM-09 | 185, 184, 104, 106, 105, 802 | 3 | `independence_wave_formable_state_puzzle_form09_territory` |
| FORM-12 | 249, 651, 833, 399, 397 | carrier plus 3 members | `independence_wave_formable_state_puzzle_form12_territory` |
| FORM-13 | 249, 651, 833, 399, 397 | carrier plus 3 members | `independence_wave_formable_state_puzzle_form13_territory` |
| FORM-16 | 230, 231, 229 | 3 | `independence_wave_formable_state_puzzle_form16_territory` |
| FORM-18 | 676, 421, 413 | carrier plus 2 members | `independence_wave_formable_state_puzzle_form18_territory` |
| FORM-39 | 636, 523, 669 | 3 | `independence_wave_formable_state_puzzle_form39_territory` |
| FORM-48 | 378, 629, 684 | 3 | `independence_wave_formable_state_puzzle_form48_territory` |

The qualification wrappers delegate to the package, tag, anchor, invitation, and frozen-consent contracts in the owning FORM trigger files. FORM-03 accepts either the second Event 006 carrier anchor or the sovereign `BEL_flanders` delegation at state 6. FORM-09 enumerates the finite twenty triplets needed for three of six candidates. FORM-12 and FORM-13 require the state 249 carrier plus three distinct consenting member anchors. FORM-18 requires the state 676 carrier plus both consenting member anchors. FORM-08 deliberately returns false because only states 84 and 82 are researched while its registry minimum is three; no third state is fabricated. No helper performs an all-country or geography scan, and the integration does not use GUI event targets.

The shared GUI is attached to all seventeen current Event 006 formable decision categories: the discovery category, shared transaction and membership, FORM-01 congress, FORM-02 union, FORM-03 low countries, FORM-04 league, FORM-05 charter, FORM-08 Danube, FORM-09 Balkan, the Middle Volga Congress for FORM-12 and FORM-13, the Council of Communities for FORM-18, FORM-16 integration, FORM-39 invitation and federal compact, and FORM-48 invitation and federal compact.

The exact activation helpers are in `common/scripted_triggers/006_independence_wave_formable_state_puzzle_triggers.txt`. Their pending-invitation branch is evaluated before selected/profile and post-formation branches; later branches explicitly reject a pending invitation so a category cannot expose two family overlays at once.

Build handoff requirements are recorded in `docs/plans/006_independence_wave_plans/subagent_handoffs/006_formable_state_puzzle_gameplay_integration_2026_08_09.md`.

## Current grouped-consumer authority (2026-08-09)

The settled grouped workflow is current implementation evidence for fourteen runtime-authored families, seventeen category attachments, 50 candidate-state rows, and 100 DDS pieces.

The complete category crosswalk is `docs/plans/006_independence_wave_plans/subagent_handoffs/006_formable_state_puzzle_category_attachment_audit_2026_08_09.md`, and the filesystem/asset authority is `docs/plans/006_independence_wave_plans/subagent_handoffs/006_formable_state_puzzle_settled_filesystem_audit_2026_08_09.md`.

The grouped scripted GUI is presentation-only and uses `context_type = decision_category`; the shared player and AI formation gates remain the gameplay authority. Pending founding invitations take precedence over selected/profile and post-formation projections, keeping overlays mutually exclusive in live helper state.

FORM-07 and FORM-48 are visible in the grouped architecture but remain readiness-controlled and fail closed under their identity, package, member, and integration gates. FORM-08 intentionally shows only states 84 and 82 with required summary count three while `independence_wave_formable_state_puzzle_form08_territory` remains false; no third state is fabricated.

The current read-only GUI inspection is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6f38780e05ee78efa5d9a7408288d4052bbf8b00f4901651df1412c86034a231/29c916409a6e614d0b7a161658e670d296fa1b53e75d14a06fd1b810c652c56f/gui-inspect.fdf2c34d03def14e.json` at shared revision `fdf2c34d03def14e0624f6dd33e6f1ac84e4167c618d8cf12ab6fcb4cd51666d`.

That MCP inspection preserves the current grouped source and 93 inspected elements but reports aggregate workspace graph, overlap, and unresolved-context diagnostics; it does not prove family-isolated visual acceptance. The shared registry remains source-aligned and the visual evidence remains bounded.

The 2026-08-13 family-isolated retry used scenario `E6_FORMABLE_STATE_PUZZLE_GUI_SETTLED_2026_08_09` against `chaosx_independence_wave_formable_state_puzzle_window` and returned `GUI_INSPECTED` with 93 inspected elements at shared revision `7ad8f26ec4fa5f8a6627743b402b28eb49949d638fc1ebdb2223e63202226903`; its linked artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/322a492e1d4c0ef00f4752f00e50619688d679f0cd0d09eaa6228ddbd4d4cec2/5ed7229c9248a8428339b27e7dbb5a5f21b6ea4c6272d8aced607657ad566309/gui-inspect.7ad8f26ec4fa5f8a.json`. The paired render returned `GUI_RENDERED` with linked SVG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e5cf4a0e6908e754ba9e1bae29b05ae013092399118afcfe42cedf62d2833fe9/82b305239eb8d8fd2979998fe492bd4f9f5bbaf7b5fc2d4b8aab087fbcf8a710/chaosx_independence_wave_formable_state_puzzle_w-full.svg`. The inspection remains bounded because workspace-wide symbol, overlap, and validation diagnostics are truncated; it is evidence of source/window reachability, not family-isolated visual acceptance.

The current state-833 rebind for FORM-12 and FORM-13 was rebuilt from the canonical state registry. The required state sets are `249, 397, 399, 651, 833`; state 256 remains only in the separate Idel-Uralic formable. A current map inspection of states 833, 256, 249, 397, 399, and 651 returned `MAP_INSPECTED` with valid state membership and networks, while unrelated workspace locator diagnostics kept aggregate validation false. The paired state render returned `MAP_RENDERED` and passed its render validation. The current grouped GUI retry used scenario `E6_FORMABLE_STATE_PUZZLE_GUI_REBOUND_2026_08_14`, returned `GUI_INSPECTED` with 93 elements, and rendered the updated window; the linked artifacts and aggregate-diagnostic limitation are recorded in `subagent_handoffs/006_iw047_mel_package_admission_audit_current_2026_08_14.md`.
