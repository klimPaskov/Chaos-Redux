# Event 015 country-package post-Ledger re-audit

Date: `2026-07-16`  
Role: `chaosx_country_package_auditor`  
Mode: exact current-source, lifecycle, hash, localisation, provenance, and decoded-visual audit  

## Verdict

**PASS for the live Event 015 country package. No gameplay, identity, military-growth, diplomacy, district, achievement, runtime-asset, or provenance blocker was found.**

The late Ledger tranche does not regress the previously accepted country package. Safe recipient and rejection handling, original-tag and base-flag preservation, all five route identities, institutional leadership, succession, all sixteen advisors, the fifty staged ideas, paid military growth, League autonomy and failure handling, Necessary Ground, external-network and formation proof, seven durable district roles, fourteen achievements, reverse-link cleanup, annexation cleanup, and terminal teardown remain complete in the exact current source.

The three top-level Event 015 asset authority documents were still stale at the audit capture point: they described the four Ledger visual families as missing even though all thirty-three textures were present, registered, consumed, state-bound, and hash-valid. The dedicated asset-requirement auditor accepted ownership of that documentation reconciliation while this report was being written. It is an Event-wide documentation dependency, not a live country-package failure. The parent must still confirm that reconciliation before making a whole-Event completion claim.

No gameplay or asset fallback, simplification, or omission was accepted. This audit made no gameplay, localisation, GUI, GFX, or asset change.

## Authorities and references

The audit read `AGENTS.md` in full and applied these repository skills:

- `chaos-redux-subagents`
- `chaos-redux-events`
- `chaos-redux-event-assets`

All accepted Event 015 specifications under `docs/specs/015_utopia_manifesto_specs/` were read, including the package manifest and both focus-graph specifications. Current handoffs and evidence included:

- `ledger_state_architecture_reaudit_2026_07_16.md`
- `country_package_post_balance_reaudit_2026_07_16.md`
- the Event 015 asset requirement crosswalk, manifest, and GFX handoff
- the route-identity manifest, asset records, ImageGen evidence, and flag/advisor/institution validators
- the value-and-calling repair manifest and validator
- the case-card manifest, provenance, checksums, and validator
- the district-card manifest, provenance, checksums, and validator

The required offline Paradox wiki snapshot was consulted for Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, Country creation, Cosmetic tags, Autonomy, States, National focuses, Interface modding, and Scripted GUI modding. No web copy of the Paradox wiki was used.

Installed vanilla documentation was read for script concepts and constants, effects, triggers, modifiers, characters, decisions, on actions, AI strategies, and the relevant GUI concepts. Direct vanilla precedents included:

- `events/AAT_Iceland.txt` for `set_politics`, `set_cosmetic_tag`, `drop_cosmetic_tag`, and promoted character leadership;
- current Afghanistan and Australia focus files for conditional faction creation and membership;
- `common/scripted_guis/RAJ_tax_fraud_scripted_gui.txt` for variable-driven mutually exclusive GUI visibility;
- `common/scripted_guis/AST_cabinet_trust_scripted_gui.txt` and its interface file for decision-category scripted-GUI properties and registered icon consumers.

## Frozen current source snapshot

Hashes are SHA-256 over the exact bytes observed for this audit.

| Surface | Current SHA-256 | Post-balance relation |
| --- | --- | --- |
| `events/015_utopia_manifesto.txt` | `8e3e0c24ebb7c243761c4391965909b7f5d823878a07ec4798ac4f2f8ae688f4` | late Ledger role-binding delta |
| `common/decisions/015_utopia_manifesto_decisions.txt` | `5dcd41ef8669a4384fedb2efa9761e657fe8a5ff8ea686e45046005fd23d17fd` | exact match |
| `common/decisions/015_utopia_manifesto_evolution_consumption_decisions.txt` | `aa8c813015cacbf2b5d588b82c39d3b440ed9e83f0009a6a048f83e5d0f82ed4` | unaffected by Ledger tranche |
| `common/decisions/015_utopia_manifesto_prefire_evolution_decisions.txt` | `04c46f18ad0c23f70303d75d0d00bb45afcaaf9ab5d877ba01bfe1e9754e3347` | unaffected by Ledger tranche |
| `common/decisions/categories/015_utopia_manifesto_categories.txt` | `feb02d3e2af05804a30d2c6ef4a1ebb647b3ced2dfe96cb6c8afed2e035a91e8` | unaffected by Ledger tranche |
| `common/national_focus/015_utopia_manifesto_focus_tree.txt` | `8a905d4b1922ab88bfab97716ba79721fc5b42679863c9543fb04d2cd489fc05` | exact match |
| `common/characters/015_utopia_manifesto_characters.txt` | `5cdf2ea793216351b5a250bbb1bb0eea84103e7668791b30867216af436749cb` | exact match |
| `common/country_leader/015_utopia_manifesto_traits.txt` | `6cd9a84026b739030115c2a81d2303c5a94bd4a3b4b5178b10947897603230a2` | exact match |
| `common/ideas/015_utopia_manifesto_ideas.txt` | `84f1e322ef827edd4eedff68ba99e67ae61e6c4ed1172193cf77eb3f4d05326a` | exact match |
| `common/countries/cosmetic.txt` | `db7814f7dad4a1b27b95f6afa8d87713ebe7a630bb5b4743bbe76550c38b25e4` | exact match |
| `common/script_constants/015_utopia_manifesto_constants.txt` | `73e6986f6b36094694b311347f0bb39299156c4f9c1f4627e67e0306d323d9e0` | late Ledger presentation delta |
| `common/script_constants/015_utopia_manifesto_country_constants.txt` | `f53c2eade8230ac93c8af734e41b01b42fe861a3bdb2ec6944d048545af67326` | exact match |
| `common/script_constants/015_utopia_manifesto_decision_constants.txt` | `b54d543548255f116fe73aa055b274b845a4dbc7dba6fa0d8bcd083ea72df1d1` | late seven-role Ledger delta |
| `common/scripted_effects/015_utopia_manifesto_effects.txt` | `c174887733b31f8f84596826c5e6a7d511d9ef7db72410c0c34946b628e827d2` | late case-expiry/geography-role delta |
| `common/scripted_effects/015_utopia_manifesto_identity_effects.txt` | `da2b2c86a47979dde9b7cae022e4f1798bac6029955858ca90fddd8a9167fa75` | exact match |
| `common/scripted_effects/015_utopia_manifesto_country_effects.txt` | `078ccd44ef44d768e1954b3beb914726417fa742a0fe35f8bc5c5938977998aa` | exact match |
| `common/scripted_effects/015_utopia_manifesto_decision_effects.txt` | `c743be8d9a124710eb1f1e00b8c13b0197e50c0f2bb9d9b5e9bc55f5752e467c` | late durable-role/planned-state delta |
| `common/scripted_effects/015_utopia_manifesto_achievement_effects.txt` | `bab3fc080661918b35d88b0418a4067ca716e458a63e36a86aa37a5da6f886e2` | exact match |
| `common/scripted_effects/015_utopia_manifesto_aftermath_effects.txt` | `0e027f7512bdf07dd04123ef97802235cd18db5d6f46e6de909d8376df7cce4d` | exact match |
| `common/scripted_effects/015_utopia_manifesto_prefire_evolution_effects.txt` | `1d757540eab0082a09df425578e4208e09cb364832d7b170591ea763d50c60c4` | exact match |
| `common/scripted_triggers/015_utopia_manifesto_triggers.txt` | `d0c304d2b4cd5dccd72b40cff8e9ab4caa3beab58838ce68057eacf31bcfe9af` | exact match |
| `common/scripted_triggers/015_utopia_manifesto_prefire_evolution_triggers.txt` | `ba4ac12603651718c633a0b3c90b530097ceadcf16969fadcec69c77508a1c5e` | exact match |
| `common/on_actions/015_utopia_manifesto_on_actions.txt` | `c2b26e499078d0c7782e46db587d377d8d64cee02e372f2ae8e087c7cea7ea81` | exact match |
| `common/ai_strategy/015_utopia_manifesto_ai_strategy.txt` | `e6db306460f20b84cb452faafc300d062a318cbd5b48eb01bb8a24da30658cbb` | unaffected by Ledger tranche |
| `common/achievements/chaos_redux_achievements.txt` | `c1c729f4717129e8abb60303a79e6fe4318598e6ac0221c79c65faa1ffe4391c` | exact match |
| `common/scripted_guis/015_utopia_manifesto_scripted_gui.txt` | `70325293fc61422eb59d717f8c10a5fb9555e680d0207e2d7be9f3d7cd5fd128` | late card/role/state visibility delta |
| `common/scripted_localisation/015_utopia_manifesto_scripted_localisation.txt` | `6e44014672139189c53bedb4dd441b9d27900d934a42b6f1fb2166287b6701ed` | unaffected by Ledger tranche |
| `interface/015_utopia_manifesto.gfx` | `1f061f7bf04372777cc422831b4ff93ff808ec769c258b1457d212b02295fc53` | thirty-three late texture registrations |
| `interface/015_utopia_manifesto_ledger.gui` | `82c07b4ac7dde3dbee92745ddb7a64e515682e813133904dc31df026d9669593` | thirty-three late GUI consumers |
| `interface/015_utopia_manifesto_super_event.gfx` | `e74e0b5ec1f7ea653f575fafd26d1be0abb553519ba35c58cb3d216b180748df` | unaffected by Ledger tranche |

### Exact late-Ledger hash disposition

Eight country-package files differ from the preceding post-balance country audit, and each difference belongs to the accepted Ledger tranche:

| File | Previous SHA-256 | Current SHA-256 | Disposition |
| --- | --- | --- | --- |
| `events/015_utopia_manifesto.txt` | `a7d27155c463424f19fb1d661356a42ccb90cc4b29f8e42a03ea78ba86b9b164` | `8e3e0c24ebb7c243761c4391965909b7f5d823878a07ec4798ac4f2f8ae688f4` | Event `.40` records the research-town presentation role; no identity or formation event changed. |
| `common/script_constants/015_utopia_manifesto_constants.txt` | `75abb0707e63730e871d7582ed6aaa6b275d3a0bc0a37ab5b7e4e5bfeb5ff700` | `73e6986f6b36094694b311347f0bb39299156c4f9c1f4627e67e0306d323d9e0` | Bounded district planned-card duration joins the existing presentation constants. |
| `common/script_constants/015_utopia_manifesto_decision_constants.txt` | `870516531db2a480be8c2f0626997e7b1a65c6fd4c35e796bb6049b93d84d8c9` | `b54d543548255f116fe73aa055b274b845a4dbc7dba6fa0d8bcd083ea72df1d1` | District presentation roles expand from four to seven exact values. |
| `common/scripted_effects/015_utopia_manifesto_effects.txt` | `fd7b62671d1f49eb00363316914c6893463c08f4ea24a2c972d37093a8c87cd7` | `c174887733b31f8f84596826c5e6a7d511d9ef7db72410c0c34946b628e827d2` | Successful case opening clears stale `utopia_manifesto_case_expired`; coastal and inland island preparation set exact visual roles. |
| `common/scripted_effects/015_utopia_manifesto_decision_effects.txt` | `0eeedf55b22818d4452e18adbe75bb106bf45ffcd33cbf6d3573cab6125bc33a` | `c743be8d9a124710eb1f1e00b8c13b0197e50c0f2bb9d9b5e9bc55f5752e467c` | Ordinary district selectors preserve a durable role, the registrar emits the bounded planned state, and teardown clears both. |
| `common/scripted_guis/015_utopia_manifesto_scripted_gui.txt` | `de37ba78051436a69abdc4a79799749210b9e208b9d3a5396ea012206fde8dbd` | `70325293fc61422eb59d717f8c10a5fb9555e680d0207e2d7be9f3d7cd5fd128` | Ten case cards, seven durable roles, and six exclusive district overlays gain exact visibility triggers. |
| `interface/015_utopia_manifesto.gfx` | `8d7bb8d4889ac2a08cdefa95fe49c591d775a973c43a8e706c5032e7d9f9a6e2` | `1f061f7bf04372777cc422831b4ff93ff808ec769c258b1457d212b02295fc53` | Registers the thirty-three accepted Ledger textures. |
| `interface/015_utopia_manifesto_ledger.gui` | `93dc265e487d72424a3c9143c61615a32da41fca1634af75f762adc67c8df51e` | `82c07b4ac7dde3dbee92745ddb7a64e515682e813133904dc31df026d9669593` | Consumes the thirty-three textures at the value, calling, case, and district surfaces. |

Every identity, character, trait, idea, focus, main decision, cosmetic-tag definition, country lifecycle, achievement, aftermath, prefire, trigger, on-action, and achievement-registration hash in the preceding table remains exact or is outside the Ledger delta. The delta therefore has no unexplained country-package source drift.

## Exact inventory

| Content | Current count | Result |
| --- | ---: | --- |
| Event IDs | `99` total, `99` unique, range `.1` through `.214` | PASS |
| National focuses | `124` focus blocks | PASS |
| Decisions | `121` unique: `105` main, `15` evolution-consumption, `1` prefire-evolution | PASS |
| Missions | `43` unique: `39` main, `1` evolution-consumption, `3` prefire-evolution | PASS |
| Decision categories | `9` | PASS |
| Ideas | `50` unique across the accepted `12` lifecycle families | PASS |
| Characters | `24`: `8` institutional founder/successor entries plus `16` advisors | PASS |
| AI strategy plans | `12` | PASS |
| Route cosmetic identities | `5` | PASS |
| Event 015 achievements | `14` | PASS |
| Achievement sprite registrations | `42`: base, grey, and not-eligible for all `14` | PASS |
| Route flag files | `75`: `25` stems at three engine sizes | PASS |
| Late Ledger textures | `33`: `4` values, `6` callings, `10` cases, `7` roles, `6` district states | PASS |

## Country-package findings

| Required surface | Result | Exact current evidence |
| --- | --- | --- |
| Safe recipient | PASS | The entry event calls `utopia_manifesto_manual_event_is_available`; the acceptance helper rechecks the same absolute gate before mutation. Eligible actors must use normal civilian systems, be a minor with generic or approved light tree, have a secure capital, and avoid dominant-faction leadership, capitulation, civil war, offensive war, terminal or protected packages, mature-tree conflicts, excessive factories, subjects, occupation, surrender, and unsafe subject status. |
| Rejection | PASS | Rejection sets its durable flag, clears acceptance, invokes the idempotent whole-runtime clearer, and clears all country-idea lifecycles. It never loads the tree, commits a route, installs a leader, or applies a cosmetic tag. |
| Original tag and base flag | PASS | Event 015 contains no `change_tag`. The only identity mutations are five formation-gated `set_cosmetic_tag` calls and one teardown `drop_cosmetic_tag`. Before formation the no-suffix recipient flag remains active, and teardown returns to it automatically. |
| Original political state | PASS | Acceptance records the exact ruling ideology group, country-leader character token, leader ideology subtype, and election permission. The subtype list covers every current vanilla ideology and both mod-added ordinary ideology types. Teardown restores the ideology, exact surviving eligible leader, and original election permission without inventing a fallback leader. |
| Five identities and formations | PASS | Voluntary Commonwealth, Union of Common Tables, Commonwealth of Measure, Closed Island, and Practical Commonwealth are the only five final cosmetics. Each is installed only after a second live formation-proof refresh. Formation itself adds no core, state, unit, equipment, or reserve. |
| Institutions and parties | PASS | Route commitment sets one of five institution identities and advances its staged route idea. Existing recipient party names are deliberately preserved; route party identity is expressed through institution, cabinet, ideology, route flags, ideas, decisions, and localisation. The Humanist Reform Coalition is represented by its cabinet and declaration flag without overwriting native party labels. |
| Founder leadership | PASS | Four institutional routes promote the Household Assembly, Council of Callings, Board of Measure, or Stewardship Council only at formation. The Practical Commonwealth keeps the recipient's current constitutional leader and ruling ideology while pausing native elections for package-owned succession. |
| Succession | PASS | Four institutional successors replace only their matching founder role: Commonwealth Council, Rotating Congress, College of Measure, and Directorate of Service. Practical succession records the constitutional-election proof. All five are guarded by `utopia_manifesto_identity_successor_installed`. |
| Advisors | PASS | Sixteen character entries have sixteen distinct small portrait handles, role-specific traits, availability gates, political-power cost, AI weight, and on-add/on-remove active flags. Route-general and route-specific advisors remain separated. |
| Staged ideas | PASS | Fifty ideas remain distributed across the accepted twelve concept families. Central lifecycle helpers remove the prior stage before installing founding, mitigated, failure, final, property-route, auxiliary, or stewardship state; terminal cleanup removes all package stages. |
| AI behavior | PASS | Twelve current country-generic plans cover foundation, five routes, route crisis/war posture, and post-formation behavior with explicit enable and abort gates. Every decision and mission family retains current AI weights or disabled behavior where player ownership is required. |
| Paid military growth | PASS | Eight `create_unit` variants exist only inside `utopia_manifesto_deploy_paid_formation`. The sole execution path checks current affordability, negates dynamic manpower, infantry-equipment, support-equipment, and army-XP costs, pays them, creates the matching template, and only then deploys the batch. Formation and identity helpers never call it. |
| League autonomy and cohesion | PASS | Initialization resets cohesion and all counters. Candidate entry requires adequate Concord and Plenty and no constitutional crisis. Members, observers, reserve contributors, sponsors, aid recipients, and defense partners receive distinct flags and arrays; refusal, exit, expulsion, failure, and collapse apply cohesion consequences and exact cleanup. Major powers use sponsor/observer paths rather than ordinary membership. |
| League defense | PASS | Formal defense additionally requires a passed vote, stable cohesion, minimum member/shared-action/defense counts, an independent unfactioned founder, and every member unfactioned. Only then is the faction created and members added. Cleanup dismantles only an Event 015 formal-defense faction still led by its founder; the aftermath path can transfer viable leadership first. |
| External network | PASS | The live network rebuild starts from League members and adds recognized compacts/associates/partners only when absent, producing a deduplicated count. Reverse founder links are reconciled after relation changes. |
| Formation gates | PASS | Common proof requires an island project or proven capital ring, the first resolved external case, a real external network, resolved external conduct, minimum Plenty, no constitutional crisis, and no stewardship failure. Each route adds its own capstone and Concord, Plenty, Assignment, reserve, defense, city, autonomy, or humanist proof. |
| Necessary Ground | PASS | Deficit preparation, domestic review, exact target/state selection, response mission, peaceful offer ladder, counteroffer, refusal, ultimatum, renunciation, expiry, stewardship, return, and authorized long integration remain live. A successful new case now explicitly clears the previous `utopia_manifesto_case_expired` flag. |
| No free territorial expansion | PASS | There is no `add_state_core`, `annex_country`, or `load_oob` occurrence. The three ownership transfers are the accepted purchase settlement, exact return to the recorded target, and authorized long-stewardship integration. Controller changes belong to leases, joint administration, and reversible Assigned Colony conduct. None occurs at formation or without its corresponding case outcome. |
| Seven durable district roles | PASS | Constants `1` through `7` are market garden, industrial housing, rail junction, refugee municipality, port town, research town, and Inland Island ring. Four ordinary selectors write both project type and durable visual role; event `.40` writes the research role; coastal and inland geography preparation write port and ring roles. |
| District phase cleanup | PASS | The registrar alone creates the seven-day planned-card flag. Six state overlays are exclusive by exact phase/conduct logic. State loss clears the state package and arrays; full teardown clears every state modifier/flag, project variable, planned flag, and durable visual role. |
| Achievements | PASS | Fourteen definitions require human play and acceptance plus durable positive proofs. Conduct disqualifiers cover offensive war, coercive or unrelated annexation, reserve reset, League coercion/member annexation, early coast, repeated status vote, regime collapse, auxiliary use/abuse, forced relocation/households, colonial repression, and stale claims. All `42` registered sprite paths exist. |
| Reverse links and annexation | PASS | Case targets, case states, League partners, and association states retain founder-side and partner/state-side reverse arrays. `on_annex` deduplicates exact founder callbacks into `.163`; `.164` puts an annexed Event 015 founder into terminal safe state; one-shot state-controller changes use `.165` and the exact state ID/founder proof. |
| Terminal cleanup | PASS | Rejection, disable, annexation, regime collapse, total repeal, target loss, case expiry, state-control loss, stewardship failure, League collapse, association withdrawal, district loss, and island-lease expiry have explicit cleanup. Identity teardown retires all twenty-four Event 015 characters, restores the original political state when possible, drops the cosmetic tag, and clears route, successor, advisor, and achievement identity state. |
| Recurring scans | PASS | Event 015 defines no daily, weekly, or monthly on-action. Recipient selection, case candidate preparation, League candidate refresh, and super-event playback use only explicit one-shot invocations; reverse indexes handle annexation and state changes without a recurring world scan. |

## Visual and provenance evidence

### Institutional leaders

The four active institutional portrait files are distinct `156x210` OpenAI built-in ImageGen tableaux and are explicitly people-free. Decoded visual inspection found empty institutional chambers rather than personal portraits:

| Runtime tableau | Character consumers | Visual identity |
| --- | --- | --- |
| `leader_household_assembly.dds` | Household Assembly; Commonwealth Council | empty municipal chamber, common table, open household ledger, assembly seal |
| `leader_council_of_callings.dds` | Council of Callings; Rotating Congress | empty congress-workshop with six calling stations and tool-wheel seal |
| `leader_board_of_measure.dds` | Board of Measure; College of Measure | empty standards chamber with balances, gauges, compass work, and network plan |
| `leader_stewardship_council.dds` | Stewardship Council; Directorate of Service | empty reserve chamber with sealed ledger, vacant chairs, and fortified stewardship seal |

The four source hashes and ImageGen handles are independent. The four DDS files are unique, correctly registered, and intentionally serve eight founder/successor entries in four pairs. The practical route needs no fifth institutional portrait because it preserves the recipient's existing leader.

### Advisor dossiers

All sixteen advisors remain separate fictional-person HOI4 dossier cards at `65x67`: Public Interpreter, General Provisioner, Secretary of Callings, Surveyor of Shores, Civic Engineer, Keeper of Stores, League Envoy, Advocate of Limits, Public Auditor, Constitutional Jurist, Council Organizer, Social Workshop Planner, Chief Surveyor, Standards Engineer, Steward of Service, and Contract Broker.

Decoded inspection found sixteen visibly distinct people in a consistent paper-dossier treatment. The validator records sixteen distinct built-in ImageGen masters; generated-frame and paper-overlay sources are exact copies, the final DDS hashes are all unique, and no drawing fallback was used. Each of the sixteen registered small handles is consumed by exactly its matching character entry.

### Route flags

The route package has `25` filename stems at all three engine sizes: `82x52`, `41x26`, and `10x7`, for `75` TGA files. Header, uncompressed 32-bit format, bottom-left origin, exact byte length, decoded-pixel parity, and source/runtime hash checks pass.

There are `21` independent ImageGen compositions and exactly four intentional base-to-route-ideology aliases:

- Voluntary Commonwealth base to democratic
- Council Union base to communism
- Planned Utopia base to neutrality
- Closed Island base to fascism

The Practical Commonwealth base is independently designed. Each route has four distinct ideology-specific variants, there are `21` unique hashes at every size, all four aliases are byte-identical at every size, and no unexpected duplicate exists. Decoded size-ladder inspection confirmed five distinct route families with legible silhouettes at the small engine size.

### Late Ledger package

The thirty-three live Ledger textures resolve as follows:

- `4` value icons at `32x32`;
- `6` calling icons at `48x48`;
- `10` case cards at `300x96`;
- `7` district-role cards at `300x96`;
- `6` district-state overlays at `48x48`.

All thirty-three GFX paths exist. Every DDS is a valid one-level uncompressed BGRA surface with the expected dimensions and exact payload length. GFX registration and GUI consumer stems match `33/33`; all ten case states and all thirteen district role/state elements match scripted visibility bindings `23/23`. Live hashes match the package validation records `33/33`.

The value/calling atlas produces ten unique cells with a recorded minimum perceptual Hamming distance of `55`. The case package has ten unique ImageGen cards, three retained rejected sources, C2PA assertions, uniform geometry, and exact processed/runtime parity. The district package has seven unique role scenes and six unique overlay badges; it retains one rejected research-town draft before the corrected source. Decoded review found every case pictogram, district scene, and state badge visually separable at native size.

### Evidence hashes

| Evidence | SHA-256 |
| --- | --- |
| Route identity `asset_records.json` | `828f18554094f6b214a07dde11f4fa61df290b881d8261cc3b6eeb3677f54ea7` |
| Route ImageGen source evidence | `7f892568ced49d74eb0d7e9cdfe3a796aee4dce13200b3f7a16b3fb2b16b6e18` |
| Flag identity validator | `14026c95ca9d3b8b9355a770d49658b05be738f06319252722f6ebd3e7ec1e65` |
| Advisor validator | `9e261b1ccd51249bdaebcd4cc2335a45988014e8aa740b43fad7c7dc8e25b02f` |
| Institutional portrait validator | `0da653422920087a28794a577963860b0dd2fbe2252353de241bf256c02d655d` |
| Value/calling validator | `aa9a249348fb5bd864bb8ffc2a46ba6a67fc595cb58a08261cf32e8e5e61e007` |
| Case-card manifest | `de90ebf5f3ca2e6b4a61f9e28cbbe93cdd312ca392fc640eca72e8734eec83a5` |
| Case-card validator | `924f2fc5a164ce6756ff453922a3e75cea6b8c79639b5254cec59072e746e1c4` |
| Case-card binary checksum ledger | `94ba79942b3834ee1b8658f5b6bf51dde5dda71f30d60f15953fa0c229bf1ff8` |
| District-card manifest | `bf3badf129ee842c9da86ace05e56b7f659497034dbd412a2d538f4ad8c65511` |
| District-card validator | `cc20a3bf3d48aa2f873af421a5c07ccce8943ee19edbaf785c040200b25eae84` |
| District-card checksum ledger | `5faa3e064311454afac22accd0ee2bdb2abd62a29347c7a048509fbf8815a491` |
| Ledger state-architecture re-audit | `c4f20170c7362a618da4128cecd608c0f090f98fb8e7b1a7276e766f451884ec` |

## Scenario traces

1. **Eligible recipient rejects.** `.1` passes the absolute safety gate; the reject option sets only the rejection state, clears ideas and all runtime, and never loads the focus tree or installs a route, leader, cosmetic, district, League, or case state.

2. **Eligible recipient accepts and later forms the Voluntary Commonwealth.** Acceptance records the original politics and leader, recruits but does not promote the package roster, loads the tree, and initializes staged ideas. Route commitment installs the Household Assembly institution but no cosmetic tag. Only after center, external-case, network, conduct, Plenty, Concord, low Assignment, partner-autonomy, and route-capstone proofs pass does formation promote the assembly and apply the voluntary cosmetic. No core, state, equipment, or unit is granted by formation.

3. **Practical route preserves the person in office.** Route commitment records the humanist cabinet. Formation changes only election scheduling and the cosmetic identity; it does not promote an institutional character or replace the ruling ideology. Second-generation proof records constitutional succession. Terminal teardown restores the original election permission and preserves/restores the exact eligible original character.

4. **Military growth cannot fire for free.** A calling/focus/decision prepares its formation type and tier, refreshes all dynamic costs, and checks stockpiles, manpower, and XP. Failure sets the payment-failed flag and creates nothing. Success negates and deducts every prepared cost before creating the template and deploying the matching batch.

5. **League member enters, contributes, and formalizes defense.** The candidate must be an independent unfactioned minor without war or package conflict; the founder must meet Concord/Plenty and crisis gates. Membership records autonomy and reverse links. Aid, reserve, and defense actions each update exact arrays and cohesion. Formal faction creation remains impossible until vote, stable cohesion, member/shared-action/defense thresholds, and every-member faction checks all pass.

6. **League refusal, exit, and collapse.** Refusal and exit are durable, decrease cohesion, and are not silently converted into membership. A formal-defense exit below threshold records failure. At the failure/cohesion limit, collapse removes only package-created relations, arrays, flags, and founder-led faction state; terminal aftermath can first transfer a viable defense-league leadership.

7. **Expired Necessary Ground case followed by a new case.** Expiry records `utopia_manifesto_case_expired`, clears the exact target/state reverse links, and reopens candidate preparation. The next successful case opening clears the old expiry flag before installing the new case header, target, state, response, and timeout. The expired card therefore cannot mask an active new case.

8. **Case target or case state changes hands.** `on_annex` snapshots only the target's registered founders and fires `.163` once per exact founder; the handler adopts a valid annexer as successor or closes the relationship. A controller change reads state-side founder arrays and fires `.165` after one hour; the event rechecks the exact state ID and founder membership before invalidation. No recurring scan is required.

9. **District role survives phase changes and then cleans up.** Ordinary selectors, event `.40`, or geography preparation write one of seven durable visual-role values. The registrar emits the seven-day planned card; building, disputed, surveyed, blocked, and complete overlays replace it through exclusive trigger logic without rewriting the role. State loss clears that state's package; terminal cleanup clears all district arrays, state flags/modifiers, phase variables, the recent-plan flag, and the durable visual role.

10. **Annexed Event 015 founder.** `on_annex` first notifies every exact case/League founder relation, then fires `.164` for the annexed actor. The annexation-safe path cancels pending aftermath state, marks dissolution, retires package characters, drops the cosmetic, clears ideas, cases, districts, League and reverse arrays, and disables the kernel.

## Validation performed

- Parsed and deduplicated all `99` event IDs, `124` focuses, `121` decisions, `43` missions, `9` categories, `50` ideas, `24` characters, `12` AI plans, and `14` achievements.
- Confirmed the only five `set_cosmetic_tag` calls are formation helpers; confirmed one teardown `drop_cosmetic_tag` and zero `change_tag` calls.
- Confirmed zero Event 015 `add_state_core`, `annex_country`, and `load_oob` occurrences and traced every `create_unit`, equipment addition, manpower change, ownership transfer, and controller transfer to its payment or reversible case contract.
- Compared all current vanilla and mod ideology subtype definitions to the exact original-leader recording branches; no subtype is uncovered.
- Verified all `24` character name/description pairs, all `14` achievement name/description/tooltip triples, and all `75` cosmetic name/DEF/ADJ keys exist across Event 015 localisation.
- Verified all nine Event 015 localisation files retain UTF-8 BOM encoding.
- Verified all `42` achievement GFX registrations point to existing files.
- Compared `100/100` route-identity asset records to runtime paths and hashes: zero missing file and zero mismatch.
- Validated all `75` TGA headers, dimensions, origins, lengths, duplicate groups, and decoded pixels.
- Validated the four institutional and sixteen advisor DDS files, registrations, dimensions, uniqueness, consumer counts, and decoded visuals.
- Validated all thirty-three late Ledger DDS files, package hashes, GFX registrations, GUI consumers, and twenty-three case/district state bindings.
- Reconciled every hash changed since the post-balance country audit to the accepted late Ledger implementation surface; no unexplained source delta remains.

## Limitations, simplifications, omissions, fallbacks, and dependencies

- This is a static exact-source, decoded-visual, provenance, and scenario audit. It does not claim an interactive engine trace or live scripted-GUI render.
- Exact original-leader restoration is deliberately conditional on the saved character still existing and still being eligible for country leadership. No substitute leader is fabricated.
- The value/calling repair retains the generated ImageGen atlas and exact source/cell/runtime hashes, but its package records that the original verbatim generation prompt was not retained. This is a provenance-detail limitation, not a missing or fallback asset.
- The four flag aliases are the explicitly accepted base-to-route-ideology aliases, not substitutes for independent ideology variants. All twenty-one required independent compositions exist.
- No gameplay content, route, identity, formation, institution, party representation, leader, successor, advisor, idea family, military payment, League path, case path, district role, achievement, AI plan, localisation key, or runtime visual was simplified or omitted.
- No fallback asset or gameplay fallback was used.
- At audit capture, `docs/assets/015_utopia_manifesto/requirement_to_runtime_coverage_2026_07_16.md`, `manifest.md`, and `gfx_handoff.md` still carried the superseded four-family FAIL. The dedicated asset auditor is reconciling those top-level authority documents. Whole-Event completion remains dependent on that documentation update and its own fresh asset report; the live country-package PASS does not override that separate requirement.

## Files changed by this audit

- `docs/plans/015_utopia_manifesto_plans/subagent_handoffs/country_package_post_ledger_reaudit_2026_07_16.md`

No gameplay, localisation, GUI, GFX, asset, spreadsheet, skill, top-level authority document, or other handoff was edited. No commit was created.
