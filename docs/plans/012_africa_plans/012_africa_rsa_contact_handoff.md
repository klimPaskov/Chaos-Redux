# Event 12 South Africa Allied rupture handoff

Status: isolated RSA package complete and ready for parent integration. This handoff records the public API, owned files, identifiers, lifecycle contract, balance values, assets, validation evidence, and remaining integration work. The package does not edit Event 12 shared files.

## 1. Public integration API

The caller must be in COUNTRY scope on the original, player-led South African Event 12 host.

1. Test `africa_rsa_allied_branch_can_start = yes`.
2. If Britain is not in the same faction but the route still represents an accepted Allied framework, set the caller-owned marker `africa_rsa_allied_framework_confirmed` before the test.
3. Call `africa_rsa_start_allied_civil_war = yes`.

The start effect repeats the complete gate internally and does nothing when it fails. It never substitutes a different host, capital, patron, or country. Its gate requires:

- actual and original tag `SAF`;
- the committed Event 12 host contract through `africa_is_current_host`;
- no active civil war and no prior RSA branch or exile continuation;
- membership in a faction plus either Britain in that faction or `africa_rsa_allied_framework_confirmed`;
- an explicitly supported independence/autonomy state;
- control and ownership of Transvaal, Cape, and Natal, including a viable port in Cape and Natal;
- at least one independent African government already held in a bounded Event 12 relationship/selection array that can receive the mandate if the Coalition loses.

Useful completion triggers for shared content are:

- `africa_rsa_civil_war_first_proof_satisfied = yes`: the civil-war proof was completed and the shared first-proof state is satisfied or recovered.
- `africa_rsa_allied_settlement_is_complete = yes`: the RSA Allied-framework settlement has completed on the surviving country, regardless of which South African government won.
- `africa_rsa_exile_recovery_can_be_completed = yes`: the one saved exile custodian satisfies its recovery gate.

One-use global state is carried by `africa_rsa_branch_used` and `africa_rsa_recovery_used`. Active and completed settlement state uses `africa_rsa_civil_war_active`, `africa_rsa_settlement_pending`, and `africa_rsa_settlement_completed`.

## 2. Government and split contract

- The original `SAF` country remains player-led and becomes the `Continental Coalition`. It retains Pretoria/Transvaal and the Event 12 host ledger.
- `start_civil_war` creates the dynamic revolter and saves it as global `africa_rsa_allied_union_government`. It becomes the `Allied Union Government`, receives Cape and Natal plus owned Namibian states admitted by the fixed filter, and retains the pre-war party popularities and governing tradition.
- The Coalition receives explicit democratic-communist partner politics, with the primary party chosen opposite a democratic pre-war government so the two sides cannot collapse into the same political identity.
- Loyalist allocations are 44% of the stockpile, 46% of the army, 72% of the navy, and 56% of the air force.
- The pre-war capital, enemies, faction leader, overlord, and exact supported autonomy level are snapshotted. The loyalist inherits the old faction and old subject relationship. The Coalition becomes free without ending the civil war and exits inherited external wars pairwise.
- `africa_rsa_original_faction_leader` remains the historical pre-war snapshot. `africa_rsa_allied_faction_leader` records the actual post-split faction leader and is the only target used for faction traversal or a surviving Cape base lease.

## 3. Proof, support, and intervention ledgers

The wartime proof is physical and conjunctive:

- civilians protected through the relief decision;
- Transvaal held with at least one civilian or military factory;
- Cape or Natal held with a naval base;
- an allied-only railway connection from Transvaal to the controlled port;
- material support from two distinct African governments.

Regional requests are targeted decisions over the bounded `africa_selected_targets` array. Acceptance transfers 2% of current equipment and records the responding country once in both response and supporter arrays. Refusal is also recorded, so the same country cannot be asked repeatedly.

`on_war_relation_added` records only explicit Allied-side parties related to the loyalist/faction snapshot and coalition-side parties already present in the supporter ledger. A one-shot traversal of the saved Allied faction leader captures faction wars created inside `start_civil_war` before the saved loyalist target can be observed by the on action. No recurring country scan exists.

## 4. Civil-war lifecycle and settlements

The lifecycle uses four event-driven hooks:

1. `on_war_relation_added` maintains the two intervention arrays.
2. `on_capitulation` contains a bounded lifecycle bridge for the active Allied Union loser only. The gate requires the saved loyalist identity, the active RSA civil war, an uncapitulated Coalition still at war with it, faction membership, and an unused bridge flag. If the loyalist is faction leader, leadership first passes to the first recorded, existing, uncapitulated Allied intervener still in the faction. Any inherited subject tie is released with `end_wars = no` and `end_civil_wars = no`, then the defeated loyalist leaves its faction. This bridge performs no peace, annexation, host transfer, winner selection, or settlement; it only allows the engine's normal civil-war end callbacks to fire. There is no alternate fallback outcome.
3. `on_civil_war_end_before_annexation` snapshots the still-living loser. A Coalition victory supplements the Allied ledger from the saved faction. A loyalist victory copies the coalition-support ledger and transfers the Event 12 host mandate to the one bounded exile patron before the old host is annexed.
4. `on_civil_war_end` performs only recorded pairwise white peace where war still exists, then applies a two-year truce to every surviving recorded participant. It never invokes a faction-wide peace conference or broad peace effect.

Coalition victory restores an owned pre-war capital and opens `chaosx.nr12.1204` with three settlements:

- sovereign Cape convention;
- a two-year military-access lease to the surviving Allied faction leader, with an idempotent expiry and early termination decision;
- closure of foreign bases.

The post-war recovery proof requires both a citizenship-and-land settlement and a guarantee to an independent neighboring African state.

Loyalist victory suppresses the Coalition's public identity. Before the split, the system freezes every valid patron already present in the accepted relationship, selection, or first-contact stores. At defeat it may select only from that frozen ledger or from a government that explicitly supplied the Coalition during the war; the post-split roster refresh cannot add patron candidates. It then transfers the original host identity, opening profile, playbook, generation lineage, surviving relationships (excluding the custodian itself), constitutional variables and route-origin flags, and continental values, closes all in-flight actions, and opens one delayed exile-council recovery. Completed-focus and in-flight action state deliberately do not migrate. If every prequalified contact becomes invalid during the war, the route ends through the explicit `chaosx.nr12.1208` terminal event; no unrelated host is selected.

## 5. Identifiers

Events:

- `chaosx.nr12.1200` — Continental Coalition opening.
- `chaosx.nr12.1201` — Allied Union Government opening.
- `chaosx.nr12.1202` — targeted African material-support response.
- `chaosx.nr12.1204` — Cape settlement.
- `chaosx.nr12.1205` — loyalist suppression.
- `chaosx.nr12.1206` — exile custodian notice.
- `chaosx.nr12.1207` — hidden base-lease expiry.
- `chaosx.nr12.1208` — explicit no-patron terminal.
- `chaosx.nr12.1209` — pre-war Allied leader response.

Decision category and decisions:

- `africa_rsa_crisis_category`
- `africa_rsa_protect_civilian_corridor`
- `africa_rsa_seek_regional_support`
- `africa_rsa_first_proof_mission`
- `africa_rsa_enact_citizenship_land_milestone`
- `africa_rsa_guarantee_neighbor_sovereignty`
- `africa_rsa_terminate_base_lease_early`
- `africa_rsa_reconstitute_exile_council`

Public cosmetic identities:

- `AFRICA_RSA_CONTINENTAL_COALITION`
- `AFRICA_RSA_ALLIED_UNION_GOVERNMENT`

## 6. Owned files

- `common/script_constants/012_africa_rsa_constants.txt`
- `common/scripted_triggers/012_africa_rsa_triggers.txt`
- `common/scripted_effects/012_africa_rsa_effects.txt`
- `common/on_actions/012_africa_rsa_on_actions.txt`
- `events/012_africa_rsa.txt`
- `common/decisions/categories/012_africa_rsa_categories.txt`
- `common/decisions/012_africa_rsa_decisions.txt`
- `localisation/english/012_africa_rsa_l_english.yml`
- `docs/plans/012_africa_plans/012_africa_rsa_contact_handoff.md`

The localisation file is UTF-8 with BOM. Every visible event option and decision has direct player-facing text, a custom consequence/requirement tooltip, and an AI path using the same executable conditions.

## 7. Balance and cleanup

Central constants own the force ratios, 360-day wartime proof, two-supporter threshold, 730-day settlement truce/base lease, 30-day exile notice, resource costs, political distributions, effects, and AI weights. Fields that are not safe script-constant consumers receive scoped variables before use.

Both victory paths clear intervention arrays, regional response flags, proof mission state, temporary state flags, autonomy snapshots, split variables, saved targets, and response flags. Historical outcome, proof, settlement, one-use, and exile lineage flags remain deliberately. The base-lease path keeps only its actual Allied leader target and truce-duration variable until the idempotent expiry removes access and clears them.

## 8. Assets

No new raster or interface asset is required. The accepted package has no custom flag, portrait, or route-emblem requirement; those asset families are `not_needed`, not placeholders. The cosmetic identities are name-only and retain South Africa's underlying flag presentation. The package reuses verified vanilla sprites:

- event pictures: `GFX_report_event_generic_african_unity`, `GFX_report_event_generic_conference` from vanilla `interface/eventpictures.gfx`;
- decision-category icon: `GFX_decision_category_generic_crisis`; decision and mission icons: `GFX_decision_generic_industry`, `GFX_decision_generic_civil_support`, `GFX_decision_generic_political_discourse`, and `GFX_decision_generic_break_treaty`, all from vanilla `interface/decisions.gfx`.
- cost text also reuses vanilla's registered `GFX_train_texticon` plus the standard equipment/political/command/stability text icons.

No DDS, sprite definition, asset manifest, or new `.gfx` file is needed.

## 9. References and validation evidence

Implementation was checked against the mandatory offline wiki pages for data structures/event targets, triggers, effects, modifiers, localisation, scopes, on actions, event modding, decision modding, idea modding, AI modding, factions, and country creation. Vanilla documentation consulted includes script concepts/script constants, effects, triggers, and the script-constant schema. Structural precedents include AST civil-war settlement and union-control lifecycle code, TAOG war-relation on actions, WTT Germany, La Résistance Spain, Indian faction inheritance, and Afghanistan revolter targeting.

Repository skills used for this package were `chaos-redux-events`, `chaos-redux-decisions-missions`, and `chaos-redux-event-assets`. The asset workflow confirmed that the accepted design needs no new visual production and changed the category treatment to a category-sized vanilla crisis sprite.

Focused checks confirmed:

- all RSA helper calls and every external Event 12 helper resolve to definitions;
- all 68 referenced script constants resolve;
- the nine event definitions are unique;
- all eight referenced event, decision, category, and text-icon sprites exist in vanilla;
- the autonomy snapshot/restoration covers all 21 current vanilla autonomy states and all seven fixed package state IDs resolve;
- event/decision/cost/tooltip localisation coverage is complete and the file retains its BOM;
- only the nine new RSA-owned files listed above are in this package.

The HOI4 event inspector was invoked first for the namespace and then for the opening event, but its artifact store returned `ARTIFACT_STORAGE_LIMIT` before producing diagnostics. This is a tooling-capacity limitation, not a reported script diagnostic.

## 10. Parent integration and future extensions

The parent still owns the exact shared focus/event call site, Event 12 event-log/detail actor mapping, accepted-spec promotion, catalog workbook alignment/export, and final package-wide audit. Those shared surfaces were intentionally not edited under the isolated ownership boundary.

Future depth can add bespoke event art, named South African leaders, region-specific supporter responses, and additional post-settlement constitutional work. Those are extensions, not substitutes for any implemented route.

Remaining runtime risk: if a defeated Allied Union Government is the faction's sole viable leader and no recorded, living, uncapitulated Allied intervener can inherit leadership, the task's no-substitute and no-faction-teardown constraints leave no alternate bridge. The bounded hook still asks the defeated leader to leave its faction, so callback progression in that exact edge case depends on the engine accepting the leader departure. No hidden host or settlement fallback masks that condition.

Simplifications, omissions, and blockers: none inside the isolated RSA gameplay package. The shared call site and shared documentation/catalog surfaces remain parent-owned integration work. The only validation limitation is the event inspector's full artifact store described above.
