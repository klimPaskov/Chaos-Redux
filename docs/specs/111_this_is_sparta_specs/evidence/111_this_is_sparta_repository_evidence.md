# Targeted repository evidence for Event 111

## Scope and provenance

This is a read-only targeted pass after the full supplied-source gate. The repository is klimPaskov/Chaos-Redux. Every file observation below is pinned to commit a3ef485c5da7e2337122eca04ac65c175050f251, which was the revision returned by the connected GitHub search index. The parent identifies master as the repository's default branch. This pass did not determine an installed game revision or modify the repository.

The actual connected GitHub tools used were github_search, github_fetch_file, and github_fetch. The tool registry exposed no HOI4 MCP tools. No engine, map renderer, GUI renderer, event analyzer, probability analyzer, asset provider, or game launch ran. Historical MCP artifact URLs embedded in repository documentation are source claims from earlier work. They are not results obtained by this pass.

There are 27 successful bounded content reads across 19 paths. The complete text spans and Git blob SHA values are in source_reading/repository_read_receipts.json. Search results and directory inventories are separately classified there. Large index bytes were accessed to select exact needed records, with only the listed spans claimed as content reading. A truncated combined output was discarded and its ranges reread in untruncated calls.

## 1. Identity and registration

The user assigns This is SPARTA!!! to current Event 111 and explicitly preserves its original identity 116. The pinned repository export still uses the older numbering. Its physical CSV line 234 is ID 111 Resistance, with a lootbox-like description. Line 239 is ID 116 This is SPARTA!!!, with the short premise that Spartan warriors rise in Greece. Both are marked Unavailable. IMRO remains legacy 115 and Wrestling Tournament legacy 113 in this export. The user brief is the authority for current 110 and 108 respectively.

The full initialize_event_categories body was read inside common/scripted_effects/chaosx_logic_effects.txt lines 220–345. Neither 111 nor 116 is added to any of its major, fire-once, or repeatable arrays. Event 071 is explicitly fire-once. Event 019 uses the constant-backed repeatable entry.

The 162-entry events directory inventory contains neither an 111 nor a 116 filename and no Sparta or Resistance filename. Exact GitHub searches for chaosx.nr111.1 and chaosx.nr116.1 returned no matches. Together with the export and full category body, this supports an unimplemented and unregistered Sparta identity in the inspected snapshot. It is not an exhaustive installed-content audit of every dynamically generated root and every enabled mod.

Design consequence: create current identity 111 only after a documented migration reconciles the old occupied catalog row. Do not blindly overwrite CSV row 111, treat 116 as a second live event, globally subtract a guessed offset, or assign Resistance a guessed destination. Preserve affected legacy rows and acceptance history. An old save row containing only numeric 111 is ambiguous and cannot safely be relabeled Sparta without further identity evidence. The concrete implementation branch must either supply a proved migration or declare a new-campaign requirement for this map and identity change.

No Sparta country tag was established. The common/country_tags directory was inventoried and the shared chaosx and Event 006 reservation files were read. They contain no named Sparta package. The Event 006 file includes existing Epirus and Thrace reservations among many other regional carriers. This does not prove any arbitrary three-character tag is free across vanilla, Workshop, sibling mods, history, flags, cosmetic tags, and scripted dynamic construction. SPARTA_TAG remains a role placeholder until that complete audit.

## 2. Laconia and the state boundary

The repository has no history/states directory at this revision. The endpoint returned 404 and its history directory contains only countries, general, and units. The map directory contains buildings.txt, without the base map bitmap or province definition table.

The committed universal state registry is therefore the available geographic snapshot. Its metadata names 1,081 states, IDs 1 through 1,081, a 5,632 by 2,048 map, a source state-history bundle hash, and the MCP revision from its historical build. The exact source names and records were read for the relevant Greek region:

| Snapshot state | Recorded source filename | Recorded province membership |
| --- | --- | --- |
| 47 | history/states/47-Greece.txt | 863, 976, 1109, 3864, 3973, 3988, 4109, 6930, 7127 |
| 182 | history/states/182-Crete.txt | 1164, 4170, 9940, 12058 |
| 183 | history/states/183-Cyprus.txt | 7193, 11984 |
| 184 | history/states/184-Thrace.txt | 9791, 9930, 11774, 11905 |
| 185 | history/states/185-Epirus.txt | 841, 1106, 1205, 3914, 3980, 9805, 9837, 9916, 10203, 11786, 11895, 12001 |
| 186 | history/states/186-Peloponnese.txt | 1173, 4078, 4178, 4193, 7096, 7211, 11965 |
| 187 | history/states/187-Aegean Islands.txt | 3401, 6550, 8435 |
| 731 | history/states/731-Central Macedonia.txt | 895, 936, 966, 3526, 3844, 3936, 6990, 10163, 11818 |

A programmatic search of all registry records found no Laconia or Sparta name/source match. State 186 is explicitly the entire recorded Peloponnese unit. This pass has not identified which of its seven provinces exactly cover Laconia, which province should be the capital, or which port and rail connections exist in the actual current combined map. Those are installation-dependent mapping tasks. The snapshot state IDs above are evidence references and must not become final unverified route requirements.

The offline State Modding article states that province membership belongs to a state definition in history/states, that the state has a numeric ID, and that state history sets ownership, buildings, resources, and victory points. The offline Effects article defines transfer_state as ownership and control of a whole state. set_province_controller changes only control and can reset at peace or a peace conference. It does not provide lasting province-level country ownership.

The parent has now accepted a mandatory build-time Laconia state split as part of Event 111's implementation. This is a design decision responding to the user's location requirement. It is not a map patch already made. Do not transfer all state 186 as a hidden approximation and do not substitute temporary province control.

The map dependency must include:

1. Exact installed province geometry and historic Laconian placement, including a defensible boundary and a deployable province.
2. A fresh collision-audited state ID after evaluating the complete active map and load order, without guessing 1082 from the stored registry's maximum.
3. A deliberate split of province membership with no duplication, omission, or overlap, preserving the existing source path for the parent state override.
4. Source-to-destination conservation of bookmark population, resources, state building capacity and existing buildings, with explicit justified allocation. Runtime event grants remain separately recorded.
5. Province-specific victory points, buildings, ports, coastal forts, supply hubs, railways, connections, and state-level supply reconciliation.
6. Both supported base bookmarks and dated ownership/control history, with Greece's starting forces and capital assumptions reviewed against the split.
7. Every old Peloponnese requirement examined semantically. A historical whole-Peloponnese requirement must usually include both resulting states, while an exact Laconian action must use only the new state.
8. Rebuilt geometry registry, state index, universal triggers, all affected consumer manifests and textures, localisation, category attachments, and map/GUI evidence against the actual combined map.
9. An explicit compatibility and save-migration policy. A map-changing package cannot claim compatibility with arbitrary installed overlays merely because the old snapshot was valid.

## 3. State-puzzle framework dependency

docs/formables/state_registry/README.md is stronger implementation guidance than a casual instruction to run an old compiler. It says the geometry producer, registry builder, and consumer compiler are archived provenance under .tools/archive and are not supported routine tools. A map revision or new consumer requires deliberate restoration and fresh review of the complete chain or an accepted replacement. The runtime generator .tools/generate_formable_state_puzzle_runtime.mjs remains active for complete manifests. Merely invoking it cannot produce new Laconian province geometry or a missing consumer texture.

The framework already supports grouped consumer overlays. Each family supplies a group_id and activation_helper, with shared GUI/window identifiers that must agree. It emits one overlay window and scripted-GUI binding for the group. This is a source-backed way to plan one event-owned panel for the selected route. State pieces, summaries, ordinary formation decisions, and AI all need the same authoritative live territory helper.

Geometry and nodes are built in advance. Live play can change ownership, control, qualification, or which predeclared candidates are relevant. It cannot invent a missing positioned state node at runtime. A long imperial route therefore needs a reviewed predeclared regional or active-objective view whose visual scope remains legible, with every excluded or hidden piece represented accurately by the authoritative completion condition.

The actual state 186 wrappers were read in common/scripted_triggers/chaosx_universal_state_registry_triggers.txt lines 3927–3947. They delegate to controlled-by-root, owned-by-root, owned-and-controlled-by-root, and owner/control-by-root-or-subject primitive families. They are live predicates, not cached meters. Owner and controller are distinct. A vague alliance or military-access pact does not satisfy a subject predicate.

The older framework overview retains a static category picture beside some puzzles. The current supplied event/GUI rules and parent contract forbid a category picture beside the new rich Event 111 puzzle. Preserve this explicit precedence rather than copying that older presentation uncritically.

## 4. Event 019 and finite unit families

The actual Event 019 entry invokes infantry_spawn_fire_manifestation immediately. Its core helper initializes the system and performs one bounded event-wide generation pass across eligible countries. It then schedules human reports and records generation accounting. This is a source precedent, not permission to call Event 019's entire global manifestation from Sparta.

The exact generation helper was read around lines 2235–2355. It captures unit and obligation ledger counts, the prior division set and counts, allocates unique identities, creates a formation inside event_target:infantry_spawn_current_origin_state, records owner as infantry_spawn_generation_country, and checks the observed division delta and ledger structure. This supports a state-scoped spawn transaction with receipts. The offline Effects entry also describes create_unit in STATE scope. The supplied events skill's country-scope phrasing is not a sufficient implementation recipe. Installed native documentation and actual callback scope must be checked before coding.

The existing unit-family contract is version 4. A consumable land family supplies one idempotent owner-side registry row and thirteen callbacks for eligibility, template, spawn, sustainment, concrete equipment token, published equipment snapshots, presentation, management evaluation, payment, refund, derivative setup, public-package removal, and cleanup. Event 019's central family file is not extended for a future owner. Parent country identity and progression remain isolated from generic derivatives. Missing provider evidence fails closed.

The source's natural derivative transfer cannot preserve every native division property. Its approved workaround freezes a recorded set, recreates and proves replacements, then removes exact source formations. It explicitly cannot preserve all live equipment variants, organization, veterancy, officers, orders, and related state. Event 111 must not borrow that workaround and promise lossless warrior conversion or country transfer.

The parent's finite ancient host, ordinary modern recruits, unique Talos, air-family birds, and other approved mythic consumers need distinct consumer dispositions. This evidence does not authorize endlessly generating additional returned ancient people, duplicating Talos, or copying Sparta's government into an Event 019 derivative. Exact survivor conversion and uniqueness need event-owned receipts and a verified native materialization method.

## 5. Persia 071

The full 161-line event script was read. chaosx.nr71.1 is hidden and immediately sends chaosx.nr71.2 to PER. The acceptance option changes PER's cosmetic tag to PER_UNIFIED, adds listed cores, sets form_persian_empire_flag, and creates core war goals. The alternate option reduces stability and war support and starts a neutral civil war. It does not create a new independent Persia tag.

Design consequence: do not treat every existing Iran/PER as an already restored Persian Empire or assume that a restoration flag guarantees the same current actor after civil war, annexation, or tag transformation. Event 111's route connection needs an actual living actor, its current territory and controller context, and owner-source restoration evidence. The current legacy script is a reference that needs robust integration gates, not a complete playable country-package template.

## 6. Cost framework and receipts

The current universal-cost overview was read through its native-limit section. It quotes ordinary current payable costs, composes eligible source ratios, quantizes positive costs upward to the requested quantum, and preserves zero/reward values. A quote is not a reservation or a paid receipt. Confirmations quote again, check affordability, debit supported native components or a precise owner adapter, and record actual paid components under one transaction.

Actual-paid refunds use stored components once and retain duplicate-refund proof. Unsupported components remain pending for a precise owner adapter. Shared costs do not replace event eligibility, target authority, reserve floors, cooldowns, or AI policy. Event 111 must not invent a universal native resource-token effect or assert source inspection proves a live displayed/debited price.

The document itself contains stale nine-scalar cache wording beside its twelve-family list. Treat the public API's concrete current source and live output contracts as the implementation authority for any adapter rather than depending on prose counts.

## 7. Workbook and remaining access limits

The current catalog CSV header contains ID, Event Name, Details, Evo I through Evo V, World-End Scenario, Type, Chaos level, Cluster ID, and Status. The README says the workbook Legend owns dropdown and color semantics, Events stores distinct cluster IDs, Cluster Memberships retains repeated membership slots and severity, and evolution overflow remains complete in Evo V until a deliberate schema migration.

GitHub returned only a three-line Git LFS pointer for chaos_redux_events_catalog.xlsx. Its object is sha256:a0ac5c0efacd7169e183b0bd393ba223d596ac74cae5d6d1a51bacb3411b613a with declared size 95,115 bytes. No workbook sheet, formula, dropdown, fill, or hidden metadata was inspected. A future workbook editor must materialize the real binary and follow the spreadsheet preservation contract. No catalog row or export was changed here.

The installation-dependent blockers remaining are exact tag availability, actual combined state and province membership, capital and supply placement, native scopes and arithmetic, a working restored or replacement geometry compiler, runtime unit and model behavior, and native/MCP validation. These are explicit implementation gates. They do not block writing the authorized design.

## Read register

Every link below resolves to the pinned repository snapshot. Git blob SHA values identify file objects, not a fresh SHA-256 of engine content. Source spans are the portions actually processed. The full project source reading gate is recorded separately.

| Repository path | Actual line spans | Git blob SHA |
| --- | --- | --- |
| [events/071_persian_empire.txt](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/events/071_persian_empire.txt) | 1–161 | f1e951049e23f34f3a73a96d53c683f1e1b36e27 |
| [common/scripted_effects/chaosx_logic_effects.txt](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/common/scripted_effects/chaosx_logic_effects.txt) | 220–345 | d3bf007cd3b6ee792f17c30229ae9e23ca143c92 |
| [docs/spreadsheets/README.md](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/docs/spreadsheets/README.md) | 1–28 | 3e9e2520f6d993f95ae4295e3dc6715bcc2adc03 |
| [docs/formables/formable_state_puzzle_system.md](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/docs/formables/formable_state_puzzle_system.md) | 1–136 | 76fc80f42d9981056649b7c81b5b336b3ef4127c |
| [docs/formables/state_registry/generated/state_geometry_registry_qa.json](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/docs/formables/state_registry/generated/state_geometry_registry_qa.json) | 1–119 | 6d9af65a9a5250cd8d084469ff9de6f05cbd432a |
| [common/country_tags/chaosx_countries.txt](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/common/country_tags/chaosx_countries.txt) | 1–44 | fe872714f9abbc7cdd6358f0830307e7ca6de621 |
| [docs/spreadsheets/chaos_redux_events_catalog.xlsx](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/docs/spreadsheets/chaos_redux_events_catalog.xlsx) | 1–3 | d81768d5368a731b4bede069845f623ed1d324d2 |
| [paradox_wiki/State modding - Hearts of Iron 4 Wiki.md](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/paradox_wiki/State%20modding%20-%20Hearts%20of%20Iron%204%20Wiki.md) | 1–150 | b62424248542c83f1fa263d939fb0809443f0c8f |
| [events/019_infantry_spawn.txt](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/events/019_infantry_spawn.txt) | 1–180 | 0e58e56060de658bfcfa59c168296668ca8b5365 |
| [common/scripted_effects/019_infantry_spawn_core_effects.txt](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/common/scripted_effects/019_infantry_spawn_core_effects.txt) | 480–594 | 83721631eff8d14577e7fcad17e303ddff5d2c9b |
| [docs/systems/cbrn_warfare/chaos_unit_family_registry.md](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/docs/systems/cbrn_warfare/chaos_unit_family_registry.md) | 1–148 | 120e7569306ef83fa3fc583e25b99f72ce11ea1e |
| [paradox_wiki/Effects - Hearts of Iron 4 Wiki.md](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/paradox_wiki/Effects%20-%20Hearts%20of%20Iron%204%20Wiki.md) | 900–942, 1033–1077, 1225–1250, 3355–3390 | afc9255950157681d0202484f20d06cea9bd747c |
| [docs/formables/state_registry/state_registry_index.json](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/docs/formables/state_registry/state_registry_index.json) | 1–46, 8205–8284, 8043–8204, 2074–2117, 33590–33633 | 89b0ad980e67a302965d1b80671f81aa85ca9676 |
| [docs/spreadsheets/chaos_redux_events_catalog.csv](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/docs/spreadsheets/chaos_redux_events_catalog.csv) | 1–1, 228–242 | 4f7db06c535d5d323d1a8134787fb3dd4f3d17b2 |
| [common/scripted_effects/019_infantry_spawn_generation_effects.txt](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/common/scripted_effects/019_infantry_spawn_generation_effects.txt) | 2235–2355 | bc6c8ba28fc8337215e46443d5fd81751c294bcc |
| [docs/formables/state_registry/README.md](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/docs/formables/state_registry/README.md) | 1–67 | 2ea2b99428b4fdead8652326e56617f6e9f3a488 |
| [common/country_tags/006_independence_wave_countries.txt](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/common/country_tags/006_independence_wave_countries.txt) | 1–118 | 67bf59d7e7f05fee7fd6c5c50245883dca62addb |
| [common/scripted_triggers/chaosx_universal_state_registry_triggers.txt](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/common/scripted_triggers/chaosx_universal_state_registry_triggers.txt) | 3927–3947 | 339fe464db7ff0e2aec0661c7caed47f3576cbce |
| [docs/systems/universal_cost_modifier.md](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/docs/systems/universal_cost_modifier.md) | 1–139 | f053e8d76ef5d7232fd622a18b7ae7d9faa77e83 |

