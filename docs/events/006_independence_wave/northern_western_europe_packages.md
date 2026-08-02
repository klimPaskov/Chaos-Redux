# Event 006: Independence Wave Northern and Western Europe Packages

This is the consolidated implementation reference for the Northern and Western Europe country packages. Accepted design authority remains in `docs/specs/006_independence_wave_specs/`; implementation handoffs remain in `docs/plans/006_independence_wave_plans/`; asset provenance remains in `docs/assets/006_independence_wave/`.

Package sections:

- Scotland and Wales (IW-001–IW-002)
- Brittany (IW-004)
- Wallonia and Frisia (IW-006–IW-007)
- Rhineland and Bavaria (IW-008–IW-009)
- Saar (IW-010)
- Iceland (IW-012; exact vanilla-path carrier)

Current portrait authority is the sourced-only gate in the accepted specification and event-asset skill.
The earlier twenty generated large portraits remain consumer/provenance evidence but no longer satisfy grounded country readiness.
IW-001 Scotland, IW-002 Wales, IW-004 Brittany, IW-006 Wallonia, IW-007 Frisia, IW-008 Rhineland, IW-009 Bavaria, and IW-010 Saar have complete sourced real-male portrait rosters, final runtime DDS wiring, and post-wiring country-package audits, so their exact package IDs are compile-time content-attested. IW-012 Iceland is also statically admitted through its registered vanilla `ICE` tag, exact vanilla-path `iceland_tree` carrier, four ICE route consumers, supported AI profile, and Nordic-precedence formable guard; its runtime release and host-survival evidence remain open.
IW-002 has independently approved and runtime-wired J. H. Thomas civic and Major George Frederick Myddleton Cornwallis-West commander portraits, so Wales is admitted. The earlier Lewis Pugh Evans retry still fails the non-compensable likeness gate, and the Saunders Lewis evidence remains rejected because the rights-clear 1973 source preserves the wrong 1936 age; reconstructing a younger face would violate the source-locked identity gate. IW-006 retains its approved Jules Destrée civic portrait and now has the independently approved, source-locked, byte-matched Louis Ruquoy/Rucquoy commander portrait wired to the stable AFX consumer; the retired Hainaut-born general is documented as an alternate-history reserve appointment rather than a 1936 office. IW-010 has independently approved, byte-matched Walter Simons and Friedrich von Rabenau full-size portraits, a passing post-portrait country-package audit, and exact compile-time content attestation.
Route-owned Rupprecht and Matthes remain protected and byte-identical.
Gameplay advisor offices remain active without custom Event 006 advisor cards, sprites, or runtime DDS files.
Any later section describing a closed package as promoted records an earlier gameplay audit and is superseded for current visual admission by this paragraph.

Current source-of-truth correction: IW-002 Wales is admitted. Its J. H. Thomas civic and Major George Frederick Myddleton Cornwallis-West commander portraits are independently approved, source-locked, and runtime-wired without changing the vanilla history, tag, or meaningful tree. The earlier Saunders Lewis and Lewis Pugh Evans trials remain rejected evidence.

The complete IW-012 package reference is [the dedicated Iceland package document](iw012_ice_package.md). It is kept outside the grounded real-portrait roster because it deliberately reuses Iceland's researched vanilla identity and portrait/flag/history surfaces rather than adding Event 006 art.

> Supersession note (2026-08-01): The older Wales paragraph above predates the J. H. Thomas and Cornwallis-West promotion. Use the current admission statement below; Wales is admitted and the earlier Lewis Pugh Evans/Saunders Lewis failures remain historical evidence only.

## Current regional admission snapshot (2026-08-01)

Any 63-row/68-file wording in the dated regional paragraph below is historical traceability only and does not override the current shelf authority recorded in the resume packet and source map.

The ASY Barsoum v93 independent audit now passes identity/likeness, HOI4 style/framing, provenance, and the PD-1923/1921 rights/date basis with a low-resolution group-photo caveat; parent release acceptance is required and no runtime promotion occurred.

The current portrait-shelf authority is 78 original-size PNG masters in one flat directory, with 73 indexed rows and five older physical files outside that index (four ARX masters and the CHU Mirsaid master). No normalized 156x210 shelf files, advisor portraits, dossier derivatives, or small consumers are authorized. CHU Karim Tinchurin v3 and ASY Haydo remain rights/date-gated evidence, and the alternate ASY Barsoum package remains pending independent audit.

The current Event 006 authority is `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md` together with the current resume packet and the post-ARX count audit. Nine Northern and Western Europe packages are statically content-attested: IW-001, IW-002, IW-004, IW-006, IW-007, IW-008, IW-009, IW-010, and IW-012, across their compatible reservation groups. Event-wide, the current allocator source audit records 149 publishers, 126 automatic/high-chaos selectable packages, 138 SCN-008 ranked packages, the doubled 6/8/10/14/20 ladder, and fourteen attested packages across thirteen compatible groups and fourteen distinct anchors, with IW-018 ARX Sardinia as the latest admitted package. IW-014 Catalonia, IW-043 CHU, IW-058 ASY, IW-093 DOX, IW-098 SOK, IW-179 FSM, IW-030 MNT, and IW-177 FIJ remain **HOLD / fail-closed** outside that set; the shared IW-046 CHU overlay row is also unadmitted. The IW-014 Catalonia package remains an implementation draft pending its formable or valid Mediterranean carrier adapter. The flat portrait shelf is documented as 63 original-size masters with no normalized, advisor, dossier, or small derivatives; its 63-row versus 68-file inventory discrepancy remains unresolved and is not reclassified here, while the two Montenegro masters remain rights-gated evidence only.

The IW-012 route-arbitration source closure is recorded after commits `3570ed8ff` and `72d8549e3` in `subagent_handoffs/006_iw012_decision_ai_reaudit_2026_07_28.md` and `subagent_handoffs/006_iw012_formal_route_ai_closure_implementation_2026_07_28.md`. These static findings do not close live allocator, host-survival, force, save/load, route-AI timing, shared-focus visibility, scenario, or synchronized transaction evidence. The regional package remains under the overall **HOLD / PARTIAL** runtime disposition, and the restored shared-focus baseline retains fourteen geometry blockers.

---

<!-- Consolidated section: Scotland and Wales. -->

## Event 006: Scotland and Wales Packages

This section documents the implemented gameplay contract for Independence Wave packages IW-001 Scotland (`SCO`) and IW-002 Wales (`WLS`). Both reuse their installed vanilla tags, country definitions, history, characters, cores, and ideology flag families. Event 006 does not replace a living Scotland or Wales, and neither package is part of the Soviet-collapse system.

### Runtime setup

The regional allocator retains the existing package geography:

| Package | Tag | Anchor and capital | Compact territory | Extended territory | Archetype | Depth |
|---|---|---|---|---|---|---|
| IW-001 Scotland | `SCO` | 121 Lothian | 133 Lanark | 120 Highlands, 136 Aberdeenshire, 933 Shetland | port or island | regional |
| IW-002 Wales | `WLS` | 122 Wales | none | none | mountain or frontier | regional |

The setup adapters run only after the shared origin transaction has published the exact package, anchor, and former-host scopes. Each adapter then:

1. verifies the original tag, package ID, region, depth, archetype, owned and controlled anchor, living former host, and exact capital;
2. creates its institutional council and territorial commander only when those tokens do not already exist, then reapplies the exact HOI4-painted portrait set;
3. ensures civilian economy, export focus, and volunteer-only laws without overwriting other history content;
4. initializes package politics and party names;
5. assigns the reviewed full Event 006 focus framework in place of the vanilla generic tree;
6. publishes constitutional, popular/labor, traditional/cultural, and emergency-military routes while explicitly withholding patron-client and radical-sovereignty routes;
7. publishes all four former-host policy routes, a distinct internal power struggle, league participation, and the accepted formable families;
8. loads and materializes the package's existing force mapping only after the guarded command-roster proof succeeds;
9. enables the origin-locked AI profile; and
10. recruits the package's three distinct institutional advisors; and
11. proves every package field again before the shared transaction may mark runtime setup successful.

IW-001 verifies the existing p1 territorial-defense package with military tradition 70, including its audited navy and air inheritance behavior. IW-002 verifies the existing p2 mountain-frontier package with military tradition 60.

### Institutional authority and command

Scotland uses the sourced R. B. Cunninghame Graham character token `SCO_independence_wave_civic_convention` for its civic routes and the sourced Victor Morven Fortune token `SCO_independence_wave_territorial_commandant` as its emergency head and corps commander. Wales uses the independently approved and runtime-wired J. H. Thomas token `WLS_independence_wave_national_council` as its civic leader. Its `WLS_independence_wave_mountain_commandant` remains source-blocked after the Evans trial-03 likeness failure.

These are guarded runtime Event 6 characters, not replacements for vanilla characters. Setup retains stable `156x210` sprite consumers with `set_portraits`; Event 6 defines no commander miniature, advisor-card, dossier, or `_small` portrait. Scotland's two sourced real-male treatments and Wales's J. H. Thomas civic treatment are approved and wired; the Lewis Pugh Evans commandant remains source-blocked after the trial-03 likeness failure. A package cannot pass content attestation while one of its required identities is source-blocked or its complete portrait set has not passed visual review.

Scotland also recruits a Shipping Authority Commissioner, Industrial Reconstruction Secretary, and Territorial Defense Planner. Wales recruits a Bilingual Civil Service Commissioner, Coal and Rail Organizer, and Mountain Defense Planner. These asset-neutral advisor offices carry no custom Event 006 portrait cards or sprite registrations. Each retains a substantial role-specific trait, a concrete hiring cost, and route-aware AI weighting.

The static advisor records are recruited by hidden setup event `chaosx.nr6.10` inside the frozen release chain. The calling package adapter then proves all three records exist before it can publish setup success; no scripted effect or on action contains `recruit_character`.

### Founding pressures and lifecycle ideas

All tuning lives in `common/script_constants/006_independence_wave_scotland_wales_constants.txt`.

Scotland exposes `independence_wave_sco_shipping_authority`, starting at 35 and stabilizing at 65. Below the threshold it carries `sco_divided_coastal_command`; at or above the threshold it carries `sco_north_atlantic_state_service`.

Wales exposes `independence_wave_wls_north_south_integration` and `independence_wave_wls_bilingual_service`, starting at 30 and 40. Both must reach 65 to replace `wls_divided_valleys_administration` with `wls_bilingual_coal_and_rail_compact`.

Each package can hold at most one lifecycle idea and one selected-government idea. Changes clamp between 0 and 100 and immediately refresh the lifecycle.

The decision-category descriptions show these package pressures beside the shared Event 006 Legitimacy, Recognition, Capacity, Security, and Instability values.

### Government settlements

The shared focus framework chooses one government route. A package-owned timed decision then installs the corresponding government, public party name, authority, popularities, and idea.

| Route | Scotland | Wales |
|---|---|---|
| constitutional | Constitutional Convention | Constitutional National Council |
| popular/labor | Workers' Commonwealth Charter | Workers' Valleys Charter |
| traditional/cultural | Crown and Convention Settlement | Cultural Guardians Settlement |
| emergency military | Emergency Territorial Directorate | Emergency Mountain Directorate |

Scotland registers `traditional_authority_vs_assembly` as its internal power struggle. Wales registers `labor_councils_vs_ministries`.

### Package projects

Projects use the shared Event 006 cost and duration tables. Civil work consumes command power, manpower, and a civilian factory; security work consumes command power, equipment, manpower, or army experience according to its tier; diplomacy consumes command power and convoys or trains; regional congresses pay the strategic bundle. Package projects serialize, occupy time, cancel if the exact package or capital proof fails, and apply explicit failure pressure where work can collapse.

Scotland reconnects the central belt, organizes Firth convoys, settles British asset ledgers, and unifies territorial command. Its regional choice can remain with the Celtic Cooperation State or pivot to the North Atlantic Compact before formable discovery. A later maritime conference prepares the selected-family transaction and leaves a successful congress ready for the final proclamation.

Wales reconnects north-south rail, establishes bilingual services, guards coalfield corridors, and settles the British property board. Its accepted family is the Celtic Cooperation State, followed by a Celtic council that prepares the shared transaction and leaves a successful congress ready for the final proclamation.

The conference effects publish a bounded shared formable operation through the selected-family registry. FORM-01 and FORM-02 have certified exact X-ending identity adapters, complete flag triplets, strict territory and consent policies, and reversible integration transactions. Their final proclamations remain governed by the shared readiness and commit gates; the package does not invent a fallback tag.

### Package focus branches

The full Event 006 tree contains five origin-gated focuses for each package.

Scotland's branch reconnects the central belt, charters North Atlantic shipping, settles crown and convention, convenes a Celtic maritime conference, and founds the North Atlantic State Service.

Wales's branch reconnects north and south, charters coal and rail, establishes the bilingual service, secures mountain corridors, and convenes the Celtic Council.

These branches supplement rather than replace the shared framework's government, economy, defense, diplomacy, former-host, league, formable, and high-chaos lanes. Their rewards change package pressures and shared values; they do not provide repeating free formations.

### AI behavior

Scotland prioritizes infantry, support equipment, artillery, trains, convoys, infrastructure, and dockyards, restrains early war declarations, and raises coastal defense and army priority under severe former-host threat.

Wales prioritizes infantry, support equipment, artillery, trains, infrastructure, and mountain defense, follows the same founding restraint, and raises army and fortification priority under severe former-host threat.

Both profiles are locked to the exact original tag, package ID, setup-complete flag, and package AI flag.

### Vanilla preservation

No country, history, character, flag, state-history, or portrait file is overridden. Scotland and Wales continue using their installed ideology flag triplets. The Welsh flag family carries the documented caveat that its familiar green-white layout was officially adopted in 1959; reuse here is the accepted registered-tag behavior, not a claim of 1936 authenticity.

The package files never activate, remove, duplicate, or rename vanilla `WLS_restore_y_wladfa_decision`. Its standalone vanilla decision category therefore coexists with the narrowly visible Event 006 Wales category.

### Visual assets and sprite wiring

The package reuses these already registered Event 006 interface sprites:

- ideas: `independence_wave_founding_identity`, `independence_wave_improvised_government`, and `independence_wave_fragmented_command` from the existing Event 006 idea interface definitions;
- decisions: `GFX_decision_independence_wave_government_actions`, `GFX_decision_independence_wave_depot_border_actions`, `GFX_decision_independence_wave_former_host_negotiations`, `GFX_decision_independence_wave_army_integration_actions`, and `GFX_decision_independence_wave_formable_proclamation`;
- focuses: `GFX_goal_independence_wave_founding_administration`, `GFX_goal_independence_wave_infrastructure_authority`, `GFX_goal_independence_wave_recognition_diplomacy`, `GFX_goal_independence_wave_constitutional_state`, `GFX_goal_independence_wave_army_integration`, and `GFX_goal_independence_wave_league_congress`.

The unique package portraits are registered in `interface/006_independence_wave_region_01_portraits.gfx` and installed under `gfx/leaders/006_independence_wave/`. The gameplay advisor offices deliberately carry no custom Event 006 portrait sprites. The authoritative user-directed HOI4 leader production package records source portraits, processed PNGs, DDS decodes, reference review sheets, hashes, and manifests under `docs/assets/006_independence_wave/`.

| Country | Real male identity | Runtime portrait | Source status |
| --- | --- | --- | --- |
| Scotland | R. B. Cunninghame Graham | `portrait_SCO_independence_wave_civic_convention.dds` | attributed archival master, source-locked HOI4 repaint, independent likeness/style/provenance pass, and runtime wiring complete |
| Scotland | Victor Morven Fortune | `portrait_SCO_independence_wave_territorial_commandant.dds` | IWM archival master, source-locked HOI4 commander repaint, independent likeness/style/provenance pass, and runtime wiring complete |
| Wales | J. H. Thomas | `portrait_WLS_independence_wave_national_council.dds` | Bain/Library of Congress archival source, source-locked HOI4 repaint, independent likeness/style/provenance PASS, and byte-matched runtime DDS; circa-1920 wording boundary retained |
| Wales | Lewis Pugh Evans | `portrait_WLS_independence_wave_mountain_commandant.dds` | IWM archival source retained; trials 01, 02, and 03 pass provenance/style/framing but fail the non-compensable likeness gate and remain unwired |

Scotland and Wales retain their installed vanilla flag triplets because these are reused vanilla countries, not newly created Event 006 tags. Any future royal Scottish cosmetic route must remain traditional-route-only. Wales receives no invented pre-1959 fallback.

### Readiness and future work

Gameplay adapters, projects, focus hooks, ideas, AI, localisation, exact setup validation, source-backed Scottish leaders, asset-neutral advisor boards, and FORM-01/02 integration are implemented. IW-001 Scotland and IW-002 Wales are admitted after their complete sourced rosters and post-wiring package audits. The earlier Lewis Pugh Evans commandant hold remains evidence-only; no portrait tranche alone admits a package. The runtime allocator still enforces host survival, unique anchors, reservations, Event 5 separation, and wave capacity. Wales's installed vanilla flag retains its 1959-layout caveat in the asset audit. No dormant vanilla history file receives a content-readiness flag.

Admission correction (2026-08-01): IW-002 Wales is admitted after the independently approved J. H. Thomas civic and Cornwallis-West commander promotions. The earlier Lewis Pugh Evans commandant hold remains evidence-only and does not reopen the package gate.

Future depth can add bilateral Scottish-Welsh conference events and route-specific cabinet succession without bypassing the package gate or replacing living countries.

---

<!-- Consolidated section: Brittany. -->

## Event 006 Brittany country package

### Package contract

`IW-004` is the complete Event 006 country package for `BRI`. It remains a Minor Repeatable candidate inside the northern and western European pool. The package is bounded to the accepted map binding and never changes the allocator or cluster definition.

| Field | Binding |
|---|---|
| Country | `BRI` |
| Package | `IW-004`, numeric package ID 4 |
| Anchor and capital | State 14 only |
| Accepted extensions | None on the installed map |
| Former host | Preserved through the Event 006 former-host event target and variable |
| Region | Northern and western Europe |
| Depth | Regional |
| Archetype | Port or island |
| Force profile | Coastal maritime |
| Formable family | FORM-01 only, Celtic Congress `KCX` |

The initializer requires the exact `BRI` origin, package ID, regional depth, archetype, state-14 anchor ownership and control, state-14 capital, and a living former host distinct from Brittany. A living or otherwise meaningful `BRI` is still protected by the parent allocator. The package does not overwrite a dormant tag's history until the Event 006 transaction has already established the exact origin.

### Founding state

The package begins under Maurice Duhamel's democratic political family and keeps the accepted vanilla Gwenn-ha-du identity. It does not install Olier Mordrel and does not expose the radical-sovereignty route.

Two visible values describe the founding settlement:

- Breton and Gallo Public Compact begins at 30.
- Coastal Command begins at 25.

Both must reach 60 to replace `Divided Ports and Language State` with `Bilingual Maritime Compact`. The 480-day founding mission fails if the state loses control of its capital or cannot stabilize both values. Project failure reduces both package values and damages the shared Event 006 legitimacy, capacity, security, recognition, and instability ledgers.

The public-service track distinguishes Breton from Gallo rather than treating Brittany as culturally uniform. The maritime track distinguishes port and fleet crews from inland territorial defense. These pressures meet in a mutually exclusive operational choice:

- Prioritize the inherited flotilla to strengthen the coastal command at a capacity and instability cost.
- Hold an inland mobile reserve to strengthen the interior at a small recognition cost.

Neither choice grants free divisions, equipment, or political power. All founding projects are costed and one-time.

### Government routes

The shared full Event 006 focus framework exposes five package-approved routes. Each route has a costed government-installation decision and one exclusive route spirit.

| Route | Breton settlement | Political identity |
|---|---|---|
| Constitutional | Federalist Civic Charter | Maurice Duhamel's democratic political family and an elected federal assembly |
| Popular council | Dock, Rail and Fisheries Councils | A labor administration rooted in maritime and transport councils |
| Traditional | Regionalist Cultural Compact | Cultural communities and municipalities led by Breton regionalist Régis de l'Estourbeillon |
| Emergency military | Joint Coastal Command | Henri-Léon Devin coordinates ports and inland approaches from the professional naval command at Brest |
| Patron client | Protected Ports Mandate | External guarantees traded for contractual limits on policy |

The traditional route is a civic regionalist settlement, not an extremist one. The package sets `independence_wave_radical_sovereignty_route_excluded` and never makes a fascist or Mordrel route available.

### Leadership and advisors

Vanilla provides the accepted historical Breton political figures and official HOI4 portraits. The package relies on those assets for Maurice Duhamel and the labor political family rather than creating duplicate historical characters.

The two package runtime characters are guarded against duplicate generation:

- `BRI_independence_wave_civic_delegate`, Régis de l'Estourbeillon, is the sourced real male founder and long-serving president of the Breton Regionalist Union and a former Morbihan deputy. His 1904 John Wickens portrait is retained with its public-domain evidence, repainted through an identity-preserving ImageGen edit, independently approved against the source, and wired at the full `156x210` leader size.
- `BRI_independence_wave_coastal_commandant`, Henri-Léon Devin, is the sourced real male naval officer who commanded the École navale at Brest from September 1930. He serves as the Joint Coastal Command leader and corps commander; the package does not call him maritime prefect before his September 1936 appointment.

The readiness proof also requires the existing vanilla `BRI_coi`, `BRI_stc`, `BRI_acd2`, `BRI_nccr`, and `BRI_mt` advisors. Their official vanilla dossier sprites remain unchanged.

François Debeauvais is deliberately absent. Available research did not establish a defensible United States public-domain basis for the sharper 1932 to 1933 photographs, and the cleared 1928 group source is too weak for an authentic individual portrait. This is a rights blocker, not a license to substitute another real person or a generated likeness.

### Forces and military progression

The package consumes the already frozen p4 force registry without changing it:

- force profile `coastal_maritime`
- military tradition 58
- reinforcement mask 1543
- inheritance mask 1
- navy inheritance enabled
- air inheritance disabled

The five exact reinforcement pathways are integrate militias, regional guards, secure depots, professional officers, and capital or border defense. The setup proof rejects every other reinforcement flag. The existing force framework supplies engineers and reconnaissance at opening strength, while artillery, logistics, and signals remain part of the later professionalization path. Package decisions add no free unit, equipment, manpower, political-power, or repeatable reward loop.

### Focus branch

Because dormant `BRI` owns only the generic vanilla tree, Event 006 assigns the full framework and adds a five-focus Breton branch:

1. Charter the Ports and Fisheries.
2. Establish Breton and Gallo Services.
3. Integrate Sailors and Guards.
4. Settle the French Accounts.
5. Convene the Celtic Delegation.

The branch advances the same visible package values as decisions and connects the cultural, maritime, former-host, and regional-ambition systems. It adds no replacement branch to a meaningful pre-existing national tree.

### Former-host and diplomacy systems

The package preserves the former host as a scoped relationship rather than assuming a hardcoded runtime country. Its French asset-ledger project addresses ships, depots, pensions, rail stock, property, border administration, and inherited obligations. It reduces claim, hostility, obligation, property, pressure, and reconquest-fear ledgers while improving the negotiated border position.

All four shared former-host policy lanes remain available. AI strategy reads the dynamic host-threat proof, builds army and coastal defenses when that proof is severe, and otherwise favors founding restraint. Constitutional and traditional AI emphasize infrastructure and dockyards, labor AI emphasizes civil industry and rail supply, emergency AI emphasizes defense, and patron AI emphasizes docks and convoys. Every route retains an avoid-starting-wars strategy.

### Regional ambition and FORM-01

Brittany registers the Celtic cooperation family and the `independence_wave_bri_form01_candidate` flag only. The package does not register FORM-02, FORM-03, FORM-04, a North Atlantic family, or any alternative formable.

The Celtic branch has two costed steps:

- Open a Celtic Port Corridor to improve network standing through port, mail, pilotage, and relief coordination.
- Convene the Breton Celtic Delegation after the package-specific focus, compact stabilization, regional-power threshold, formable readiness, and strategic cost are satisfied.

The custom congress replaces the shared preparation mission, not the final proclamation. It revalidates the selected FORM-01 transaction, builds the frozen invitation and member ledgers, resolves the shared congress vote, and grants the package-specific congress result only when `independence_wave_formable_transaction_ready` is present. A successful vote leaves the transaction in `formation_ready`; the separate shared proclamation action rechecks the ledger, charges the selected-method commitment costs, and atomically applies the `KCX` identity and integration. `KCX` is treated as a congress or league of consenting delegations, not a unitary annexation state. The only Event 006-created cosmetic tag used by this package is `KCX`, which follows the required `X` suffix.

### Cleanup and release admission

The cleanup adapter removes the founding mission, all package decisions, both lifecycle ideas, all route ideas, package values, package flags, focus handoff flags, AI profile, and FORM-01 candidate flags. Runtime characters are guarded for repeat initialization and remain harmless outside the exact active package gates.

The narrow runtime dispatch adapter recognizes package ID 4 for setup, final validation, and cleanup. Its immutable package/tag helper and runtime preflight branch prove the exact `IW-004`/`BRI` identity. The automatic and scenario gates require BRI to be absent, state 14 to be a valid unique anchor, `RG-14` to be free, the former host to retain a state, and the candidate to be clear of Event 5 reservations. The current sourced portrait and post-wiring package audits authorize IW-004's exact compile-time attestation; live host, anchor, reservation, Event 5, chaos-band, force, and transaction checks remain mandatory. No dormant-history or legacy content-ready flag grants readiness.

### Visual assets and icon wiring

New portrait sprites are registered in `interface/006_independence_wave_brittany_portraits.gfx`:

- `GFX_portrait_BRI_independence_wave_civic_commission` uses `gfx/leaders/006_independence_wave/portrait_BRI_independence_wave_civic_commission.dds`.
- `GFX_portrait_BRI_independence_wave_coastal_commandant` uses `gfx/leaders/006_independence_wave/portrait_BRI_independence_wave_coastal_commandant.dds`.

Event 006 defines no Brittany commander miniature, advisor card, dossier, or `_small` portrait. The coastal-commandant sprite is the admitted identity-preserving HOI4 repaint of the 1930 Gallica/Agence Rol portrait of Henri-Léon Devin. The civic-commission sprite is the admitted identity-preserving HOI4 repaint of John Wickens's 1904 portrait of Régis de l'Estourbeillon. Both real male subjects were independently reviewed at full and native scale before one-level BGRA DDS conversion; both runtime textures are `156x210`. The package uses de l'Estourbeillon as a researched role-compatible alternative to the rights-blocked Debeauvais material and uses no generated likeness as a substitute.

The package reuses these registered Event 006 icons:

- `GFX_goal_independence_wave_infrastructure_authority`
- `GFX_goal_independence_wave_founding_administration`
- `GFX_goal_independence_wave_army_integration`
- `GFX_goal_independence_wave_former_host_settlement`
- `GFX_goal_independence_wave_regional_formable`
- `GFX_decision_independence_wave_government_actions`
- `GFX_decision_independence_wave_army_integration_actions`
- `GFX_decision_independence_wave_former_host_negotiations`
- `GFX_decision_independence_wave_league_votes`
- `GFX_decision_independence_wave_formable_proclamation`

No new focus, decision, or flag DDS is required. The standard vanilla `BRI` flag family supplies the historically accepted Gwenn-ha-du design.

### Sources and precedents

Implementation follows the repository Event 006 package framework and the offline wiki pages for data structures, triggers, effects, modifiers, localisation, scopes, on actions, events, decisions, ideas, AI, country creation, and national focuses.

Vanilla references include:

- `history/countries/BRI - Brittany.txt` for capital 14, technologies, advisors, politics, and historical leaders.
- `common/countries/Brittany.txt` for the country identity and graphical culture.
- `common/characters/BRI.txt` for the official advisor roster.
- vanilla BRI localisation, leader portrait sprites, flag family, and generic focus assignment.
- vanilla script, effect, trigger, modifier, and script-constant documentation.

### Future plans

Potential later depth should remain within the accepted package boundary. Suitable additions include non-repeatable fisheries incidents, merchant-marine accidents, and cultural-service disputes whose outcomes feed the two visible values. A named François Debeauvais branch must not be attempted unless a defensible public-domain portrait source is found and reviewed. Any future formable expansion requires explicit design approval because this package is intentionally FORM-01 only.

---

<!-- Consolidated section: Wallonia and Frisia. -->

## Event 006 Wallonia and Frisia Packages

### Scope

This package layer implements the playable country content for two accepted Event 006 packages:

| Package | Tag | Anchor | Depth | Economy | Opening force |
| --- | --- | ---: | --- | --- | --- |
| IW-006 Wallonia | AFX | State 34 | Regional | Industrial breakaway | Industrial security, score 61 |
| IW-007 Frisia | AGX | State 36 | Standard | Port or island | Coastal maritime, score 45 |

The implementation is isolated from the shared allocator and executor. Regional setup, final-validation, and cleanup adapters are registered through the parent-owned generic dispatchers. Readiness is a static exact-ID/tag attestation rather than a mutable dormant-history flag. The Low Countries formable identity, flag, territory, member policy, integration adapter, and post-charter progression passed their independent audits; the AFX and AGX automatic/scenario release wrappers remain separate package-level preflight gates.

### Runtime setup sequence

Each exact package setup follows the same fail-closed order:

1. Verify the persistent package ID, the temporary executor package ID, the original tag, the former-host event target, and the exact anchor state.
2. Install the provisional political authority and party landscape.
3. Prove that the custom-tag history supplied the baseline civilian-economy, export-focus, and volunteer-only laws together with the civic authority and named commander.
4. Set `independence_wave_command_roster_ready` only after the commander is confirmed as a corps commander.
5. Initialize the package crisis value or values and install the appropriate starting national spirit.
6. Assign `independence_wave_focus_assignment.full_framework` and load the shared Event 006 focus tree.
7. Publish only the routes accepted for that package, then register former-host routes, the internal power struggle, regional ambition, network and league access, and the Low Countries formable family.
8. Load the researched package force mapping and call the dynamic starting-force transaction.
9. Enable the package AI profile.
10. Run the prepared package proof. Only a passing proof sets the package setup-complete flags and returns a successful setup-dispatcher result.

The prepared proof includes baseline laws, roster, focus mode, accepted and rejected routes, power struggle, formable family, force-mapping generation lock, force application, package AI flag, crisis idea, persistent anchor and former-host pointers, and the exact capital. After the shared activation pass publishes reversible registries, a separate live proof requires activation readiness, aligned active-country and network-member arrays, and exact membership in both registries before the shared transaction may commit durable history.

### Wallonia, IW-006

#### Political authority and command

Jules Destrée is the source-backed Walloon civic leader for the constitutional, labor, and patron settlements. The internal token retains its package-stable assembly name, but the player-facing identity and installed portrait are Destrée. Louis Hubert baron Ruquoy/Rucquoy is the source-backed reserve commander for the emergency-military settlement and opening formations; the alternate-history role is documented as a retired Hainaut-born general recalled to Walloon service, not as a documented 1936 office.

Accepted political routes:

- Constitutional Compact, led by Jules Destrée under centrism.
- Workers' Industrial Charter, led by Destrée under socialism.
- Emergency Works Command, reserved for a source-cleared Walloon commander under despotism.
- Patron Industrial Mandate, led by Destrée under oligarchism.

Traditional-restoration and radical-sovereignty routes remain unavailable. The internal power struggle is civilians against the army.

Accepted former-host routes are negotiation, guarded frontier, association, and reclamation. The former host is dynamic and normally resolves to Belgium through the executor's saved event target.

#### Industrial-continuity mechanic

`independence_wave_afx_industrial_continuity` measures whether the Sambre-Meuse mines, steelworks, rail junctions, and factory guards still function as a common system. Wallonia begins with `afx_disrupted_industrial_belt`. Securing the threshold swaps it for `afx_sambre_meuse_industrial_covenant`. The lifecycle can regress if a failed project pushes continuity below the threshold.

The timed `Prevent an Industrial Stoppage` crisis gives the country 360 days to stabilize the system. The player can commit shared Event 006 material packages to:

- keep mine pumps running,
- secure Sambre-Meuse rail junctions,
- settle industrial ledgers with the dynamic former host,
- unify factory guards under civilian warrants and professional officers.

Actions take 75 to 180 days. The emergency pump and rail projects sequentially commit the one spare civilian factory that a one-state opening can realistically provide, then pay the shared light-administration command-power and manpower package. The rail project still contributes security progress, but it does not compete with automatic division reinforcement for the opening equipment stockpile. The stronger factory-guard project consumes manpower, Army Experience, infantry equipment, and support equipment. The former-host settlement consumes command power plus trains or convoys. Capital loss, war during negotiations, or origin termination cancels the relevant work. Failed work reduces industrial continuity and statehood values while increasing founding instability. Completing the pumps and rail junctions supplies the baseline 150-day stabilization path; the guard and former-host projects provide stronger but more demanding alternatives.

After recognition and stabilization, the Meuse Industrial Conference raises network standing and opens the package's Meuse and Low Countries political identity. It uses the shared strategic cost and takes 300 days.

#### Level 2 Sambre-Meuse lane and incidents

Wallonia's package-specific eight-focus lane begins after the shared capital-administration opening. It charters the Sambre-Meuse authority, binds mines to rails and furnaces, codifies the selected government, integrates the industrial reserve, settles industrial succession, opens the Meuse network office, authorizes the paid conference, and prepares the Low Countries dossier. The lane never substitutes a checklist for the existing projects: the host settlement, network membership, conference payment, 300-day conference timer, and `FORM-03` consent transaction remain binding.

The lane applies concrete costs as well as gains. Constitutional and popular governments trade 5 percent War Support for their public settlement; emergency and patron governments trade 5 percent Stability for stronger command or diplomatic authority. A living-host succession compact requires the paid industrial-ledger project and costs 5 percent War Support. The defense node grants Army Experience and Command Power but creates no formation or stockpile. The industry node adds one anchor-state Infrastructure and a single Industry research bonus.

Three generation-local incidents make the package values and political choices visible:

- `chaosx.nr6.18`, scheduled with prepared founding setup, chooses between municipal review of industrial warrants and binding dispatch authority;
- `chaosx.nr6.19`, scheduled by any accepted government installation, chooses between published quotas and government quota command; and
- `chaosx.nr6.20`, scheduled only after the paid Meuse conference completes, chooses between a confederal mandate and a binding industrial directorate.

Every option changes Industrial Continuity plus legitimacy, recognition, capacity, security, and instability. The selected outcomes persist for the generation and cleanup clears every scheduled, resolved, outcome, focus, authorization, and delegation flag. No incident creates troops, grants free equipment, or bypasses route, host, network, league, or formable costs.

### Frisia, IW-007

#### Political authority and command

Douwe Kalma provides the sourced opening civic leadership for the Frisian municipalities, harbor administration, dike authorities, and coastal constabulary. Pieter Reenalda, a documented maritime officer represented by a sourced archival portrait, commands the coastal force before its mobilization package is applied.

Accepted political routes:

- Constitutional Water Board, led by the Council under centrism.
- Coastal Labor Councils, led by the Council under socialism.
- Patron Harbor Mandate, led by the Council under oligarchism.

Traditional-restoration, emergency-military, and radical-sovereignty routes remain unavailable. The internal power struggle is labor councils against permanent ministries.

Accepted former-host routes are negotiation, guarded frontier, and association. Reclamation is not published. The former host is dynamic and normally resolves to the Netherlands through the executor's saved event target.

#### Waterline mechanic

Frisia tracks two independent values:

- `independence_wave_agx_waterline_integrity` for dikes, pumps, sluices, and evacuation roads.
- `independence_wave_agx_coastal_security` for ports, harbor stores, maritime approaches, and guard readiness.

Both values must reach their thresholds to replace `agx_exposed_waterline` with `agx_dike_and_coast_authority`. Losing either threshold restores the exposed-waterline spirit.

The timed `Hold the Waterline` crisis gives the country 540 days to secure both systems. The player can commit shared Event 006 material packages to:

- inspect pump stations,
- organize a harbor watch,
- secure the inland rail link,
- train dike guards,
- reconcile water-board records with the dynamic former host.

Actions take 75 to 180 days and divide their gains between waterline integrity and coastal security. The pump survey uses the same one-factory emergency-administration predicate as Wallonia, while the harbor watch and inland rail link make two sequential light commitments from the opening coastal logistics reserve. Interrupted work reduces one or both values and worsens the shared founding settlement. Pump inspection, harbor watch, and inland rail security together reach both thresholds in 270 days. The design therefore prevents the country from solving coastal defense merely by buying equipment or solving flooding merely by raising troops, while avoiding dependence on Army Experience or a living former host.

After recognition and stabilization, the North Sea Coastal Conference raises network standing and connects the North Sea coastal hook to the negotiated Low Countries formable family. It uses the shared strategic cost and takes 300 days.

### Shared framework interactions

Both packages receive the full shared Event 006 focus framework. They register:

- a package-specific internal power struggle,
- the appropriate government-route subset,
- package-appropriate former-host route subsets,
- the regional ambition family,
- an Event 006 network membership and league route,
- `independence_wave_formable_family.low_countries_federation`,
- package hooks for the Meuse industrial corridor or North Sea coast.

The Low Countries family is negotiated rather than imposed. Constitutional and popular-council governments receive the strongest package AI preference for the regional conferences. Patron governments remain valid package routes but cannot use an independent conference while the shared client-route lock is active.

Route formalization is deliberately payable from each package's proven opening economy. Wallonia's four settlements and Frisia's constitutional and popular settlements use the one-factory light-administration commitment; the political outcomes still apply route-specific administrative, security, or diplomatic progress. Frisia's patron settlement uses one remaining light coastal-logistics commitment after its 270-day crisis baseline. Formalization shares the serialized package-project lane, requires control of the capital, and can be attempted again after an occupation cancels the timer. No route government depends on an unproven second spare civilian factory, starting Army Experience, or a landlocked opening train reserve.

All package missions, projects, formalizations, and conferences use generation-local state instead of engine-persistent `fire_only_once`. Package predicates, active-decision checks, and completion or failure flags prevent repetition during one live origin. Regional cleanup explicitly removes every active package mission and decision without applying its result, then clears those flags. An accepted Annexation and Return recreation can therefore receive fresh timers and costs and complete the full package decision layer in a later Event 006 generation, including when reset and preparation share one effect chain.

The force layer remains authoritative. IW-006 loads the researched industrial-security mapping. IW-007 loads the researched coastal-maritime mapping. The package code does not duplicate templates, unit counts, stockpiles, or inheritance rules.

### AI behavior and balance intent

Wallonia prioritizes infantry, support equipment, artillery, trains, arms factories, and infrastructure. Frisia prioritizes infantry, support equipment, trains, convoys, infrastructure, and coastal defenses. Both avoid initiating wars while they remain founding states and the dynamic former-host ledger shows no severe threat. A severe former-host threat activates a defensive buildup. Wallonia's emergency route adds a stronger army and artillery overlay. Frisia's AI defers the optional standard-convoy former-host settlement until both waterline thresholds are secure, preserving the two light logistics payments required by its baseline crisis path.

Important balance scenarios:

1. A fragile one-state Wallonia can stabilize through the complementary pump and rail projects in 150 days, but it must commit its spare factory, manpower, and command attention twice; automatic reinforcement cannot consume either project's decision reserve. Alternate projects remain valuable for statehood progress.
2. A hostile former host cannot be ignored. The dynamic threat ledger shifts AI behavior even when the former host is not the historical Belgian or Dutch tag.
3. Frisia must improve both dike administration and coastal security. Its 270-day baseline path combines pump, harbor, and rail work; completing only civil work or only guard work cannot end the crisis.
4. Capital loss during a package project produces a real setback instead of a free cancellation.
5. The regional conferences require recognition, a stable package mechanic, network membership, an unlocked independent diplomatic posture, and the strategic cost.
6. Opening formations cannot appear without a recruited commander, a valid researched mapping, the exact anchor event target, and the current-generation lock.
7. Every accepted government route can install its package leader and national spirit from the guaranteed post-crisis opening reserve: six settlements use one spare factory, and Frisia's patron route uses the sixth convoy remaining after its two baseline logistics commitments.
8. Route formalization cannot overlap recovery work or complete while the capital is occupied; a canceled timer remains available after the capital is recovered.

### Cleanup and lifecycle ownership

`independence_wave_dispatch_wallonia_frisia_package_cleanup` removes package ideas, crisis variables, route-government flags, decision outcome flags, AI profile flags, and regional hooks. It is registered in the generic cleanup dispatcher, which both the shared reset and successful origin-end path call before clearing the package identity needed by the regional adapter.

Character recruitment remains in the dormant custom-tag history files, following the character-system contract. Leaders and commanders are not recruited from on actions or scripted effects. They are not retired during origin cleanup because the tag continues to exist and may retain its post-origin government.

### Visual inventory and wiring

#### Required package portraits

| Character | Sprite | Final DDS | Registration |
| --- | --- | --- | --- |
| Jules Destrée | `GFX_portrait_AFX_walloon_provisional_assembly` | `gfx/leaders/006_independence_wave/portrait_AFX_walloon_provisional_assembly.dds` | sourced, processed, and wired; recorded in the 2026-07-22 treatment ledger |
| Walloon reserve commander | `GFX_portrait_AFX_walloon_reserve_commander` | `gfx/leaders/006_independence_wave/portrait_AFX_walloon_reserve_commander.dds` | Louis Hubert baron Ruquoy/Rucquoy Agence Rol/BnF Gallica source, exact crop, independent likeness/style/provenance PASS, deterministic `156x210` candidate, and byte-matched runtime DDS; retired-veteran alternate-history wording is wired |
| Douwe Kalma | `GFX_portrait_AGX_friesland_coastal_council` | `gfx/leaders/006_independence_wave/portrait_AGX_friesland_coastal_council.dds` | the previously approved source-locked runtime portrait remains authoritative; 2026-07-24 trial 01 passed style but failed the independent likeness gate and did not replace the DDS |
| Pieter Reenalda | `GFX_portrait_AGX_friesland_coastal_commander` | `gfx/leaders/006_independence_wave/portrait_AGX_friesland_coastal_commander.dds` | the previously approved retry-02 runtime portrait remains authoritative; 2026-07-24 trial 01 passed style but failed likeness and source-supported insignia control and did not replace the DDS |

#### Required flags

The package uses only the authorized unsuffixed tag flags:

- `gfx/flags/AFX.tga`, `gfx/flags/medium/AFX.tga`, and `gfx/flags/small/AFX.tga`.
- `gfx/flags/AGX.tga`, `gfx/flags/medium/AGX.tga`, and `gfx/flags/small/AGX.tga`.

No ideology or cosmetic flag variants are referenced.

#### Focus, report, idea, and decision icons

Wallonia's Level 2 lane uses eight package-specific `94x86` focus icons under `gfx/interface/goals/006_independence_wave/afx/`. Its three generation incidents use distinct `210x176` report cards under `gfx/event_pictures/006_independence_wave/afx/`. The nineteen base, shine, and report sprites are registered in `interface/006_independence_wave_wallonia_frisia_assets.gfx`; every focus and event consumes its exact registered sprite.

The full ImageGen sources, exact prompts, processed PNGs, contact sheets, decoded-equivalence proof, uniqueness results, hashes, manifest, and sprite handoff live under `docs/assets/006_independence_wave/afx_unique_assets_2026_07_16/`. The final package contains eleven separate source compositions and eleven validated runtime DDS files. No shared composition or placeholder substitutes for the country-specific art.

The package continues to reuse the established Event 006 idea and decision sprites registered in `interface/006_independence_wave.gfx`:

- Ideas: `GFX_idea_independence_wave_founding_identity`, `GFX_idea_independence_wave_improvised_government`, `GFX_idea_independence_wave_fragmented_command`, and `GFX_idea_independence_wave_patron_pressure`.
- Decisions: `GFX_decision_independence_wave_government_actions`, `GFX_decision_independence_wave_army_integration_actions`, `GFX_decision_independence_wave_depot_border_actions`, `GFX_decision_independence_wave_former_host_negotiations`, `GFX_decision_independence_wave_patron_aid`, `GFX_decision_independence_wave_league_votes`, and `GFX_decision_independence_wave_formable_proclamation`.

Reusing the established idea and decision language is the intended framework design; the country-specific focus and incident surfaces use their own completed art.

### Source references consulted

The implementation was checked against the offline Paradox wiki snapshot for Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, Country creation, Character modding, National focus modding, Division modding, and Portrait modding.

References consulted include vanilla `documentation/effects_documentation.md`, `documentation/triggers_documentation.md`, `documentation/modifiers_documentation.md`, `documentation/script_concept_documentation.md`, `common/ai_strategy/_documentation.md`, `common/script_constants/documentation.md`, `common/characters/_documentation.md`, the offline `paradox_wiki/On actions - Hearts of Iron 4 Wiki.md` snapshot, and the decision and country history documentation. Vanilla precedents included Belgian defense decisions, Dutch inundation and waterline content, institutional leaders, character promotion, and self-removing AI strategies.

### Future plans and extension ideas

- Add later package events that react to a failed industrial-stoppage or waterline mission without bypassing the shared Event 006 evolution system.
- Let a durable Low Countries league coordinate Meuse rail standards and North Sea flood-response stores through member-scoped decisions.
- Preserve Wallonia's Level 2 Sambre-Meuse lane when adding later incidents or regional diplomacy; any expansion must continue to consume the paid projects and shared FORM-03 consent transaction.
- Add additional commanders or advisors only after a researched roster and portrait plan replaces the current deliberate two-character package scope.

### Integration status and blockers

The isolated gameplay package files and LCX identity/integration adapters are
implemented. The shared transaction retains reversible preparation and
pre-commit rollback, while the post-commit FORM-03 consumer owns the language
and industrial state machine. AFX carrier work in state 34 feeds the existing
industrial-continuity value; AGX carrier work in state 36 feeds the existing
waterline and coastal-security values. An absorbed non-carrier package is not
reinitialized.

The package portrait and flag files remain registered. Wallonia has eight
package-specific focus icons and three incident report scenes with complete
source and runtime evidence. FORM-03 has a dedicated six-focus, six-idea,
six-decision icon set and a charter-convention report scene.
BEL, HOL, and LUX member work remains sovereign and never modifies the AFX/AGX
package identity contract. The audited FORM-03 base and progression
attestations are restored. Wallonia's post-Level-2 audit authorizes the exact
IW-006 compile-time content attestation and SCN-008 preflight branch. Its live
wrapper still requires the dormant AFX tag, unique anchor, surviving-host
remnant, reservation, Event 5 collision, chaos-band, and transaction-preflight
checks. No gameplay fallback, placeholder leader, generic commander, generic
route, or substitute flag is introduced.

---

<!-- Consolidated section: Rhineland and Bavaria. -->

## Event 006: Rhineland and Bavaria Gameplay Packages

### Overview

This document describes the package-owned gameplay implemented for Event 006 package `IW-008` (Rhineland, `RHI`) and package `IW-009` (Bavaria, `BAY`). Both packages use the shared full Independence Wave focus framework and add their own Level 2 focus groups, rosters, portraits, founding crises, political settlements, host negotiations, ambitions, network projects, high-chaos actions, AI profiles, and lifecycle ideas.

The implementation does not create tag history files, duplicate vanilla characters, override global portrait sprites, or spawn bespoke units. Existing dormant vanilla tags are configured only after the Event 006 transaction has prepared their origin. The shared dynamic force layer remains authoritative for starting formations and reinforcement packages.

### Runtime setup

The bounded dispatcher adapters are:

- `independence_wave_dispatch_rhineland_bavaria_package_setup`
- `independence_wave_dispatch_rhineland_bavaria_package_final_validation`
- `independence_wave_dispatch_rhineland_bavaria_package_cleanup`

The parent Event 006 transaction calls these adapters from its setup, final-validation, and cleanup dispatchers, and its immutable adapter registry recognizes the exact ID/tag pairs for package IDs 8 and 9. Readiness is not stored in dormant vanilla history. IW-008 and IW-009 carry exact static content attestation after their independent post-wiring package audits. Runtime admission still requires every dormant-tag, anchor, host-survival, reservation, Event 5 exclusion, chaos-band, and transaction-preflight gate. Rhineland additionally depends on the shared `FORM-04` identity transaction and flag package. Bavaria has a South German restoration ambition and no shared formable dependency.

Each prepared proof checks the exact tag, package ID, region, depth, archetype, anchor, former-host pointer, capital, laws, command roster, full focus assignment, allowed routes, power struggle, ambition policy, force mapping, applied starting force, lifecycle, and AI profile. Both proofs require `independence_wave_radical_sovereignty_route_excluded`, which keeps their accepted route matrices authoritative when Evolution 5 applies Open Sovereignty; other countries retain the shared evolution behavior. The frozen allocation planner owns the shared `RG-RHINE-SAAR` reservation and admits only the reciprocal RHI/AJX pair at capacity two, with distinct anchors 51 and 42; per-host protected-remnant checks still apply when both rows share GER.

### Characters and portraits

The package creates stable Event 6 character tokens with guarded `generate_character` calls and reapplies their exact portraits on every setup:

- `RHI_independence_wave_provisional_directorate` — Wilhelm Marx
- `RHI_independence_wave_river_commandant` — Gustav-Adolf von Zangen
- `BAY_independence_wave_state_council` — Heinrich Held
- `BAY_independence_wave_mountain_commandant` — Friedrich Dollmann

The two commandants have distinct corps-commander roles. Every grounded identity in these packages must use an attributed, role-accurate real male source and a reviewed identity-preserving `156x210` HOI4 treatment; generated officeholders and generic reuse of unrelated vanilla figures are prohibited. Event 006 defines no commander thumbnails.

`RHI_josef_friedrich_matthes` is used only when he remains recruited by Rhineland. Package setup applies protected `GFX_portrait_RHI_josef_friedrich_matthes` with `set_portraits`, while Wilhelm Marx leads the opening provisional directorate. Matthes becomes leader only for the labor settlement; when he is unavailable, the established directorate retains office as the designed institutional outcome. Gustav-Adolf von Zangen commands the armed river authority and may lead the emergency settlement through the same stable full-size consumer.

`BAY_rupprecht_of_bavaria` is used only when Bavaria still has the character and Germany does not. Package setup applies `GFX_portrait_independence_wave_BAY_rupprecht_of_bavaria` with `set_portraits`, while Heinrich Held provides the opening civic authority. Rupprecht becomes leader only for the traditional restoration settlement; Held's state administration retains the institutional regency if he is unavailable. Friedrich Dollmann commands the mountain-region emergency forces through the stable full-size consumer.

Cleanup restores both vanilla character portraits. No `.gfx` character sprite is globally replaced.

#### Advisor offices

Each package recruits three fictional specialist offices without custom Event 006 advisor portrait cards:

- Rhineland: Municipal Customs Administrator, Rail and Public Works Liaison, and River Defense Planner.
- Bavaria: District Finance Administrator, Estates' Constitutional Liaison, and Alpine Supply Inspector.

Their substantial traits affect customs and consumer burdens, rail and infrastructure construction, river defense and planning, district finance, constitutional stability, or alpine logistics. Hiring costs and route-aware AI weights are centralized in `common/script_constants/006_independence_wave_nwe_advisor_constants.txt`. The advisors are visible only for their exact active Event 006 package, use no custom portrait sprites, and never overwrite either tag's vanilla advisor content.

Hidden setup event `chaosx.nr6.10` recruits these static records within the frozen release chain. The package adapter will not publish success unless the exact three-advisor roster is present, and no scripted effect or on action contains `recruit_character`.

### Starting forces

Both packages call `independence_wave_load_force_package_mapping` and `independence_wave_apply_dynamic_starting_force` after their command rosters prove ready.

#### Rhineland (`IW-008`)

- Shared force profile: `regular_defectors`
- Military tradition: package constant `p8` = 70
- Reinforcement mask: `p8` = 1612
- Package features: secure depots, converted defectors, factory and rail guards, professional officers, capital defense, border defense, and inherited air support where the shared ledger permits it

#### Bavaria (`IW-009`)

- Shared force profile: `regular_defectors`
- Military tradition: package constant `p9` = 75
- Reinforcement mask: `p9` = 1676
- Package features: secure depots, converted defectors, terrain units, professional officers, capital defense, border defense, and inherited air support where the shared ledger permits it

No package-owned OOB or direct unit spawning is present.

### Rhineland gameplay

#### Founding crisis

`independence_wave_rhi_corridor_authority` begins at 25. The mission **Keep the Rhine Arteries Open** gives the country 420 days to reach 65. Bridge dispatch, factory and rail guard integration, host customs ledgers, and river crossing security supply distinct administrative, military, and diplomatic ways to reach the threshold. Cancellation after loss of the capital or timeout applies a concrete authority loss and shared legitimacy, recognition, capacity, security, and instability penalties.

The lifecycle swaps from `rhi_divided_river_authority` to `rhi_rhine_civic_industrial_compact` once the threshold is reached.

#### Government routes

The package publishes constitutional, labor, emergency military, and patron client routes. It deliberately does not publish traditional or radical-sovereignty routes.

- Constitutional: elected river assembly and civil administration
- Labor: industrial councils, with Matthes when available and the established directorate retaining office otherwise
- Emergency: the river commandant controls crossings and depots
- Patron: foreign credit and transit protection in exchange for political freedom

Each route installs one mutually exclusive route spirit. **Codify Durable Rhenish Independence** is a later capstone that requires a completed founding settlement and stable Corridor Authority.

#### Ambition, formable, league, and high chaos

Rhineland selects the shared `rhine_federation` family (`FORM04`), surveys the federation corridor, and can convene the Rhine Congress. This package congress settles the Rhenish municipal, industrial, customs, and security mandate even when no Saar delegation is yet available, so the country-specific incident sequence and Level 2 branch remain playable on every viable RHI release. It does not prepare or commit `FORM04`. The later shared formation congress independently rechecks the living RHI and AJX founders, connected capitals, territory, carrier delegation, invitation ledger, and consent before the selected-family registry can perform its synchronized formation commit.

The Event 006 package closes the vanilla German reunification decision only after its prepared proof succeeds, preventing the Rhenish FORM04 identity from competing with a second German path. Cleanup reactivates the vanilla decision as part of rollback.

The network project **Charter Network Transit** raises Independence Wave network standing. The regional high-chaos action **Seize the Corridor Authorities** requires regional-power status, the shared high-chaos action unlock, and Open Sovereignty. It does not replace the accepted government settlement and trades legitimacy, recognition, and stability for decisive security and Corridor Authority.

### Bavaria gameplay

#### Founding crisis

`independence_wave_bay_civic_settlement` begins at 25 and `independence_wave_bay_mountain_security` begins at 30. The mission **Hold the Bavarian State Together** gives the country 480 days to raise both values to 60. District treasury reconciliation advances civic authority; pass organization advances security; the host ledger advances civic legitimacy; integrating mountain companies advances both.

The lifecycle swaps from `bay_disputed_state_inheritance` to `bay_estates_and_districts_settlement` only when both thresholds are satisfied.

#### Government routes

The package publishes constitutional, labor, traditional, and emergency military routes. It deliberately does not publish patron-client or radical-sovereignty routes.

- Constitutional: a restored Landtag and district liberties
- Labor: strong civic mobilization at a cost to mountain security
- Traditional: restoration court led by Rupprecht when available, with the State Council retaining the institutional regency otherwise
- Emergency: mountain guardians gain security while weakening civic consent

The paired visible values make the court-versus-guardians power struggle mechanically relevant. Each government installs one mutually exclusive route spirit. **Codify Durable Bavarian Independence** is the later independence capstone.

#### South German ambition and Germany coexistence

Bavaria does not register a new Germany formable and does not select a shared formable family at setup. The prepared package begins with `independence_wave_bay_no_competing_german_claim`, closes the vanilla German reunification decision for the duration of the Event 006 origin, and proves that neither a preserved pan-German option nor a competing German-policy choice is active.

The regional ambition is limited to **Choose a South German Restoration**. That policy closes the vanilla German reunification decision and opens **Convene the South German Estates**, a timed diplomatic settlement that strengthens both Bavarian ledgers and network standing without creating a second German formable. The Level 2 branch can instead conclude a German host compact while no South German policy has been selected. That compact recognizes the living host and grants no claims, country identity, or reunification path.

The network project **Negotiate an Alpine Supply Accord** raises network standing. The regional high-chaos action **Seize South German Protectorates** requires regional-power status, the shared high-chaos action unlock, and Open Sovereignty. It leaves the accepted government settlement in force while sharply increasing mountain security and damaging civic settlement, legitimacy, recognition, and stability.

### Level 2 country focus groups

Both packages have a package-owned branch inside `independence_wave_focus_tree`. The branch roots are revealed only by the exact package triggers, and every child focus rechecks the same exact package identity before its guarded scripted reward can run. The focus helpers are repeat-safe, use the shared Event 006 tuning constants, and clear every package focus flag during generation cleanup.

#### Rhineland corridor branch

The Rhineland branch contains eight focuses and resolves seven in any one playthrough:

1. **Charter the Corridor Authority** opens the branch and raises Corridor Authority by 10.
2. **Unify Rhine Rail Dispatch** and **Arm the River Customs Guard** form parallel administrative and security projects. Together they add infrastructure, an Industry research bonus, Army Experience, Command Power, and 20 Corridor Authority.
3. **Secure the Rhine Industrial Belt** requires both parallel projects, adds one Civilian Factory and building slot to the anchor state, and supplies the final 10 Corridor Authority needed to move from the opening value of 25 to the stable threshold of 65 without a free unit package.
4. **Ratify the Former Host Transit Compact** and **Proclaim the Neutral Rhine Corridor** are mutually exclusive. The compact improves recognition and former-host ledgers at the cost of security and War Support. Neutrality improves domestic security and Stability while reducing recognition.
5. **Charter the Network Transit Office** requires either diplomatic settlement and active network membership.
6. **Authorize the Rhine Federation Delegation** requires the exact `FORM-04` family, the RHI carrier flag, and a completed package Rhine Congress. It sets `independence_wave_rhi_form04_delegation_ready` and opens formable discovery. The package congress does not stand in for Saar consent or a prepared formation transaction: the shared `FORM-04` strict mutation precondition still requires this marker for an RHI carrier or the corresponding AJX delegation marker for an AJX carrier, plus both valid founders and the complete shared ledger, before formation can commit.

#### Bavaria civic and mountain branch

The Bavaria branch contains eight focuses and resolves six in any one playthrough:

1. **Broker the Civic Settlement** opens the branch and raises Civic Settlement by 10 and Mountain Security by 5.
2. **Reconcile the Landesbank Accounts** and **Bind Rail and Pass Authorities** form parallel finance and security projects. They add one Civilian Factory and slot, one Infrastructure, an Industry research bonus, Army Experience, Command Power, 15 Civic Settlement, and 15 Mountain Security.
3. **Seat the Landtag and Court** and **Entrust the Mountain Guardians** are mutually exclusive. The civic compact trades 10 Mountain Security and 5 percent War Support for 15 Civic Settlement and 5 percent Stability. The guardians trade 10 Civic Settlement and 5 percent Stability for 15 Mountain Security and 5 percent War Support.
4. **Open the Alpine Network Office** requires either institutional settlement and active network membership. It raises both visible package values and advances network diplomacy.
5. **Convene the South German Settlement** requires the completed South German estates settlement and grants no German claims or competing identity. The mutually exclusive **Ratify the German Host Compact** instead requires a living former host and no selected competing German policy. It settles bilateral ledgers and records a negotiated host-preservation compact without changing country identity.

The branch creates no additional national spirit. The existing lifecycle and route-idea limit therefore remains unchanged.

### Country incident sequences

Each package receives three player-facing incidents in a normal playthrough. The setup adapter schedules the founding incident before evaluating the prepared package proof, and that proof requires the scheduled marker. The government incident follows the first successfully installed route government, and the ambition incident follows the relevant regional settlement. A one-day delay keeps these country choices outside the synchronized allocation and release transaction.

Rhineland resolves:

1. **Warrants at the River Gates**, choosing between temporarily preserving municipal customs seals and centralizing every gate under the Corridor Authority;
2. **The First Statute of the Corridor**, choosing published review or emergency decree authority for the installed government; and
3. **The Mandate Carried Downriver**, choosing municipal vetoes or binding transit powers after the Rhine Congress.

Bavaria resolves:

1. **Who Holds the District Seals?**, choosing district inventories or guardian-supervised treasury commissions;
2. **The Government Takes Possession**, choosing a published district compact or a centralized emergency apparatus; and
3. either **Terms Before the Southern Estates** after the South German settlement or **The Offices Left on Either Side** after the negotiated German host compact.

Every option changes Corridor Authority or Bavaria's paired Civic Settlement and Mountain Security values together with Legitimacy, Recognition, Capacity, Security, and Instability. The choices use symbolic Event 006 tuning constants, create explicit tradeoffs, set repeat-safe outcome flags, and clear all scheduling and outcome state during package cleanup. No incident grants units, equipment, political power, or a persistent store.

### Idea lifecycle and limits

Each package can hold at most two package spirits at once:

1. one founding or mature lifecycle spirit; and
2. one mutually exclusive government-route spirit.

The implementation therefore remains below the requested maximum of three tree-created spirits. No decision creates a third persistent package idea.

### AI behavior

Decision AI prioritizes the founding crisis, reacts to low values, and changes route or ambition preferences according to historical-character availability, former-host threat, regional-power status, and high-chaos access.

Macro AI strategies:

- prioritize infantry, support equipment, artillery, trains, infrastructure, and defensive construction;
- avoid early offensive wars until the country is settled or has become a regional power;
- increase army and fortification priority under severe former-host threat;
- favor civil industry under constitutional, labor, or Rhineland patron settlements;
- increase army production under emergency governments and completed high-chaos actions; and
- remove founding restraint from the decision layer only through the existing regional-power and threat conditions.

The AI uses the same costs, gates, route exclusions, and mission consequences as the player.

### Visual assets and icon wiring

No new decision icon files are required. The package reuses registered Event 006 sprites:

- `GFX_decision_independence_wave_government_actions` -> `gfx/interface/decisions/006_independence_wave/decision_independence_wave_government_actions.dds`
- `GFX_decision_independence_wave_former_host_negotiations` -> `gfx/interface/decisions/006_independence_wave/decision_independence_wave_former_host_negotiations.dds`
- `GFX_decision_independence_wave_depot_border_actions` -> `gfx/interface/decisions/006_independence_wave/decision_independence_wave_depot_border_actions.dds`
- `GFX_decision_independence_wave_army_integration_actions` -> `gfx/interface/decisions/006_independence_wave/decision_independence_wave_army_integration_actions.dds`
- `GFX_decision_independence_wave_integration_missions` -> `gfx/interface/decisions/006_independence_wave/decision_independence_wave_integration_missions.dds`
- `GFX_decision_independence_wave_formable_proclamation` -> `gfx/interface/decisions/006_independence_wave/decision_independence_wave_formable_proclamation.dds`
- `GFX_decision_independence_wave_league_votes` -> `gfx/interface/decisions/006_independence_wave/decision_independence_wave_league_votes.dds`

The Level 2 branches use a distinct installed visual package:

- sixteen `94x86` focus icons under `gfx/interface/goals/006_independence_wave/rhineland_bavaria/`, one for every RHI and BAY country focus;
- eight `64x64` route-institution idea icons under `gfx/interface/ideas/006_independence_wave/rhineland_bavaria/`, one for each accepted government route;
- `gfx/event_pictures/006_independence_wave/rhineland_bavaria/report_event_006_rhi_corridor_incidents.dds` and `report_event_006_bay_state_incidents.dds`, both `210x176`;
- normal and shine focus sprites, idea sprites, and report sprites in `interface/006_independence_wave_rhineland_bavaria_assets.gfx`; and
- source masters, processed PNGs, contact sheets, exact prompts, validation, and hashes under `docs/assets/006_independence_wave/rhi_bay_unique_assets_2026_07_16/`.

All sixteen country focuses consume their package-specific normal sprites, all eight route ideas consume their package-specific idea sprites, and the incident events consume `GFX_report_event_006_rhi_corridor_incidents` or `GFX_report_event_006_bay_state_incidents`. The generated source set contains twenty-six unique compositions. Its final DDS set contains sixteen `94x86` focus icons, eight `64x64` idea icons, and two `210x176` report scenes; all twenty-six files passed the package's legacy BGRA, exact-dimension, alpha, decoded-equivalence, and uniqueness checks. The current post-wiring audits authorize exact IW-008 and IW-009 compile-time attestation and SCN-008 preflight; live host, anchor, reservation, Event 5, chaos-band, force, and transaction checks remain mandatory.

The historical-character portraits are registered in `interface/006_independence_wave.gfx`:

- `GFX_portrait_RHI_josef_friedrich_matthes` -> `gfx/leaders/006_independence_wave/portrait_RHI_josef_friedrich_matthes.dds`
- `GFX_portrait_independence_wave_BAY_rupprecht_of_bavaria` -> `gfx/leaders/006_independence_wave/portrait_BAY_rupprecht_of_bavaria.dds`

The package effects reference those stable sprite names directly through `set_portraits`.

The additional package portrait sprites are registered in `interface/006_independence_wave_region_01_portraits.gfx`:

- `GFX_portrait_RHI_independence_wave_provisional_directorate`
- `GFX_portrait_RHI_independence_wave_river_commandant`
- `GFX_portrait_BAY_independence_wave_state_council`
- `GFX_portrait_BAY_independence_wave_mountain_commandant`

The six gameplay advisor offices carry no custom Event 006 advisor cards or portrait-sprite registrations, and Event 006 defines no commander miniatures or dossier portraits. The current grounded roster is Wilhelm Marx, Gustav-Adolf von Zangen, Heinrich Held, and Friedrich Dollmann, with Josef Friedrich Matthes and Rupprecht of Bavaria retained as the two protected approved portraits. All four package-specific treatments are sourced, independently reviewed, and wired; the protected portraits remain byte-identical. Source and replacement authority lives in `docs/assets/006_independence_wave/sourced_portrait_treatments_2026_07_22/` and `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/active_vanilla_conflict_retry/`.

### Readiness boundary

Gameplay, AI, localisation, asset-neutral advisor offices, package-specific focus art, route-idea art, incident scenes, and stable portrait consumers are wired. IW-008 and IW-009 are admitted after their complete sourced rosters, pixel-identical runtime DDS checks, and full post-wiring package audits. `FORM-04` has its separately promoted `RLX` identity, complete flag family, territory and consent transaction, and post-formation progression. Bavaria's South German ambition is package-owned and does not inherit a `FORM-01`, `FORM-02`, or `FORM-04` dependency. Neither package gains readiness through vanilla history.

### Future plans and suggestions

- Preserve the exact-package admission boundary when either package is expanded: new content must remain origin-gated, cleanup-complete, and compatible with the audited host-survival and Event 5 collision contracts.
- Give the South German restoration ambition a dedicated regional diplomacy module if a future accepted specification defines its member states and treaty outcomes.
- Consider dedicated decision art only if a later Event 006 asset pass replaces the current shared icon language across all regional packages.

---

<!-- Consolidated section: Saar. -->

## Event 006 IW-010 Saar country package

### Scope

IW-010 creates the Saar as `AJX` from state `42` in Northern and Western
Europe. It is a one-state industrial-security package built around coal, rail,
municipal administration, factory guards, and cross-border contracts. It uses
reservation group `RG-RHINE-SAAR`, which is the one documented two-package exception: IW-010 and IW-008 may be selected together only with distinct anchors 42 and 51 and after every ordinary host-survival, reservation, and transaction gate passes. A later repeatable wave may release either package again only when its tag, anchor, host, and generation checks pass, allowing living AJX and RHI countries to coexist.

The country uses two stable character consumers:

- Walter Simons, a sourced real Rhenish constitutional figure used as an alternate-history civic leader without claiming a historical Saar commission;
- Friedrich von Rabenau, a sourced real German Army officer used as an alternate-history corps commander without claiming a historical Saar posting.

The Municipal Neutral Commission is civilian.
Rabenau has no country-leader role, and neither script nor localisation describes the neutral route as military, traditional, restorationist, or emergency government.

### Runtime sequence

1. The release transaction transfers and controls state `42`, makes it the AJX
   capital, records the dynamic former host, and preserves that host's selected
   remnant state.
2. `can_initialize_independence_wave_iw_010_package` proves the exact package,
   region, standard depth, industrial-breakaway archetype, anchor, capital,
   living former host, and host-owned protected remnant. The shared
   `RG-RHINE-SAAR` plan admits only the reciprocal IW-010/IW-008 pair at
   capacity two with distinct anchors; in the installed map both anchors are
   GER-owned, so same-host cases may share GER's protected-remnant row. Every
   other reservation group retains the one-package rule.
3. The dormant history supplies the baseline laws and recruits Walter Simons and Friedrich von Rabenau.
   Runtime setup installs provisional politics, localized parties, the full shared focus framework, package routes, the power struggle, ambition family, AI profile, and lifecycle values.
4. The shared p10 force table supplies the `industrial_security` profile,
   military tradition `50`, no naval or air inheritance, and exactly five
   reinforcement pathways: integrated militias, secure depots, factory and rail
   guards, foreign arms, and capital/border defense.
5. The prepared proof checks every one of those opening facts, including the
   exact positive and negative pathway set. The final proof also checks live
   active-country and network registries.
6. Package cleanup removes its mission and decisions, ideas, route state,
   lifecycle variables, AI flag, ambition hooks, and AJX-local markers before
   the shared origin reset clears generation state.

No daily, weekly, monthly, or world-country iteration is used.

### Politics and permanent routes

The provisional state starts under Walter Simons with elections suspended until the founding settlement selects one of four accepted routes.

| Route | Permanent government | Ruling family | Identity idea |
| --- | --- | --- | --- |
| Constitutional | Saar Constitutional Charter Coalition | democratic | `ajx_constitutional_municipal_charter` |
| Popular / labor | Saar Congress of Mine, Rail, and Factory Councils | communism | `ajx_saar_labor_compact` |
| Patron-client | Saar Industrial Guarantee Board | neutrality | `ajx_patron_industrial_mandate` |
| Neutral commission | Saar Municipal Neutral Commission | neutrality | `ajx_municipal_neutral_commission` |

Traditional restoration, emergency military government, and Radical
Sovereignty are not exposed. The neutral route has its own enum value, route
flag, selection proof, focus settlement, government installer, idea, AI branch,
localisation, and durable-sovereignty closure flag. It is not an alias for any
of the rejected shared routes.

### Lifecycle and power struggle

Two player-visible values begin at `30` and stabilize at `60`:

- Industrial Continuity measures working mines, wagons, power, and contracts;
- Neutrality Credibility measures whether border, patron, and security policy
  is accepted as independent rather than improvised or externally dictated.

Until both values reach the stable threshold, AJX carries
`ajx_exposed_saar_industrial_compact`. Reaching the threshold swaps it for
`ajx_balanced_saar_industrial_compact` and safely resolves the `480`-day
founding mission. Timeout or loss of the capital applies the package failure
transaction and records failure.

The shared power-struggle lane uses the AJX-specific
`municipal_commission_vs_industrial_security` type. The player-visible balance
starts at `50`; lower values favor the Municipal Commission and higher values
favor the Industrial Security Companies. The generic focus outcomes retain
their normal one-shot closure, while scripted localisation supplies the two
Saar identities.

### Decisions and costs

The Saar Compact category shows both lifecycle values and the internal balance.
All player-started actions use shared Event 006 cost proofs and payment effects;
only the automatic founding mission has no player cost.

- Administration: restore mine and rail dispatch; seat constitutional, labor,
  or neutral-commission government.
- Security: register and subordinate the factory security companies.
- Diplomacy: open the cross-border trade desk, settle former-host ledgers,
  accept the patron mandate, balance registered patron contracts, survey the
  Rhenish corridor, and charter network coal transit.
- Strategic: codify durable independence and convene the Rhenish congress.

Timed actions serialize through
`has_independence_wave_ajx_active_package_project`. Cancellation on package
loss, capital loss, war with the former host, or network exit is explicit where
relevant and uses the package failure transaction.

Former-host settlement writes only through the dynamic bilateral ledger. It
does not assume that Germany, France, or any other fixed tag is the host.
Patron balancing iterates only the country's bounded aligned patron ledger.

### Focus integration

AJX receives the complete shared Event 006 tree plus ten package focuses.

The permanent neutral settlement contains:

- Appoint the Neutral Commission;
- Codify Municipal Neutrality;
- Bind Security to the Commission;
- Entrench the Neutral Commission.

The country branch contains:

- Keep the Mines Breathing: survival;
- Charter the Coal and Rail Authority: economy and infrastructure;
- Screen the Industrial Security Companies: security;
- Open the Cross-Border Trade Desk: diplomacy;
- Settle the Saar Accounts: former-host policy;
- Send the Rhenish League Delegation: network and FORM-04 ambition.

The branch adds no repeated dust grants, equipment loops, or unit-creation
loops. Its rewards use the lifecycle values, existing public-value effects, one
infrastructure improvement, and bounded flags. The neutral settlement's final
flag is part of the shared durable-sovereignty closure proof.

### FORM-04 hooks

AJX selects and registers `independence_wave_formable_family.rhine_federation`,
sets `independence_wave_ajx_form04_candidate` and the shared Rhine-corridor
ambition, exposes a corridor survey, readies a Rhenish League delegation, and
can run the shared FORM-04 preparation transaction through its custom congress.
The congress builds the frozen invitation/member ledgers and resolves the vote;
only a shared `transaction_ready` result grants the AJX congress reward. The
separate shared proclamation action then revalidates the vote, charges the
selected-method costs, and atomically applies the audited `RLX` identity and
integration adapters. It also has a network coal-transit project.

The shared reservation blocks AJX and RHI only inside one incident, so later
repeatable waves can establish both founders for the approved Rhenish League
direction. FORM-04 passed its post-transaction operational re-audit and exact
readiness promotion. IW-010 country-package admission is independently proven;
automatic waves and SCN-008 still require its live package preflight.

### AI behavior

Every strategy is locked to `original_tag = AJX` and the exact setup/package
flags. AJX prioritizes an infantry force with support equipment and artillery,
arms production, civilian industry, and infrastructure. It avoids starting wars
through the founding period and under constitutional, labor, patron, and neutral
settlements. Severe threat reads the dynamic former-host ledger and adds army
and bunker priority without assuming a fixed host tag.

### Visual assets and sprite wiring

#### Required and wired

| Surface | Runtime asset | Registration / consumer |
| --- | --- | --- |
| National flag | `gfx/flags/AJX.tga` | HOI4 flag path discovery |
| Medium flag | `gfx/flags/medium/AJX.tga` | HOI4 flag path discovery |
| Small flag | `gfx/flags/small/AJX.tga` | HOI4 flag path discovery |
| Walter Simons | `gfx/leaders/006_independence_wave/portrait_AJX_saar_municipal_neutral_commission.dds` | stable `GFX_portrait_AJX_friedrich_hoffmann` in `interface/006_independence_wave_region_01_portraits.gfx` |
| Friedrich von Rabenau | `gfx/leaders/006_independence_wave/portrait_AJX_saar_industrial_security_commissioner.dds` | stable `GFX_portrait_AJX_karl_becker` in the same `.gfx` file |
| Municipal Neutral Commission focus | `gfx/interface/goals/006_independence_wave/goal_independence_wave_ajx_neutral_commission.dds` | base and shine in `interface/006_independence_wave.gfx`; base consumed by `independence_wave_ajx_appoint_neutral_commission_focus` |

The character sprites are consumed by `common/characters/006_independence_wave_saar_characters.txt`.
Event 006 defines no Saar commander miniature, advisor card, dossier, or `_small` portrait.
Both Simons's civic portrait and Rabenau's commander portrait have passed the archival-source, exact-crop, ImageGen identity-preservation, HOI4-style, independent-audit, and DDS-equality gates.
Saar has exact `iw_010` compile-time content attestation after its fresh country-package audit. This admits the package to live preflight without claiming that any particular host, anchor, reservation, Event 5, chaos-band, force, or synchronized transaction will pass.
The flag hashes remain checked against `generated_nwe_hashes.sha256`.

#### Reused Event 006 icons

The decisions and focuses use already registered Event 006 sprites:

- `GFX_decision_independence_wave_government_actions`;
- `GFX_decision_independence_wave_integration_missions`;
- `GFX_decision_independence_wave_army_integration_actions`;
- `GFX_decision_independence_wave_former_host_negotiations`;
- `GFX_decision_independence_wave_formable_proclamation`;
- `GFX_decision_independence_wave_league_votes`;
- `GFX_goal_independence_wave_founding_administration`;
- `GFX_goal_independence_wave_infrastructure_authority`;
- `GFX_goal_independence_wave_army_integration`;
- `GFX_goal_independence_wave_recognition_diplomacy`;
- `GFX_goal_independence_wave_former_host_settlement`;
- `GFX_goal_independence_wave_regional_formable`.

No placeholder icon is counted as completed art. A distinct Municipal Neutral
Commission focus icon is installed as a runtime DDS file and documented in
`docs/assets/006_independence_wave/ajx_asset_completion_2026_07_15/manifest.md`.
The verified handle is:

- `GFX_goal_independence_wave_ajx_neutral_commission` at
  `gfx/interface/goals/006_independence_wave/goal_independence_wave_ajx_neutral_commission.dds`.

The three gameplay advisor records have role-title localisation and are
recruited by the Event 006 setup event, but they deliberately carry no custom
portrait handles. The focus base and shine handles are registered; the base
handle identifies the neutral-commission entry focus while its three follow-up
nodes retain their specific shared icons. Event 006 defines no Saar commander
miniature or dossier portrait. The full grounded character roster remains
fail-closed until its archival sources and treatments pass the current portrait
gate.

### Implementation files

- `common/script_constants/006_independence_wave_saar_constants.txt`
- `common/characters/006_independence_wave_saar_characters.txt`
- `common/ideas/006_independence_wave_saar_ideas.txt`
- `common/scripted_triggers/006_independence_wave_saar_package_triggers.txt`
- `common/scripted_effects/006_independence_wave_saar_package_effects.txt`
- `common/decisions/categories/006_independence_wave_saar_categories.txt`
- `common/decisions/006_independence_wave_saar_decisions.txt`
- `common/ai_strategy/006_independence_wave_saar.txt`
- `localisation/english/006_independence_wave_saar_l_english.yml`
- `history/countries/AJX - Event 006 Country Shell.txt`
- shared route, focus, dispatch, scripted-localisation, and portrait registries

### References used

The implementation was checked against the offline wiki pages for data
structures, scopes, triggers, effects, modifiers, localisation, events,
decisions, ideas, AI, country creation, divisions, portraits, and national
focuses. Official vanilla documentation was used for script constants,
effects, triggers, characters, decisions, AI, and localisation formatters.
Vanilla precedents include Assyria's history character recruitment,
Afghanistan's timed mission structure, Brazil's mutually exclusive focus
branches, and Argentina's origin-gated AI strategy.

### Readiness and future plans

- A fresh independent IW-010 package audit passed the complete Level 1 package, exact AJX identity, state-42 anchor, host-survival proof, Event 5 collision gates, shared focus and regional overlay, routes, decisions, forces, AI, assets, localisation, and FORM-04 dependency. The SCN-008 preflight, exact automatic wrapper, P10 capacity witness, region-one planner gate, and exact `iw_010` compile-time content attestation are registered. Every live preflight and synchronized transaction proof remains mandatory.
- IW-010 and IW-008 retain the shared `RG-RHINE-SAAR` reservation. They are the only pair allowed to coexist inside one frozen incident, using distinct anchors 42 and 51; same-host protected-remnant, both-order, Event 005 collision, rollback, save/load, and synchronized execution evidence remains mandatory. A later wave may admit either package again if its own readiness and host-survival checks pass.
- FORM-04 identity, consent, integration, rollback construction, and
  military-settlement adapters remain independently audited and ready. FORM-04
  still requires its living RHI partner and carrier-specific delegation proof;
  admitting AJX does not manufacture or overwrite that partner.
- The distinct neutral-commission focus art is produced, installed,
  hash-validated, registered, and consumed by the live parent-owned focus.
  AJX's three gameplay advisor offices deliberately carry no custom Event 006
  portrait sprites. No AJX focus-art integration blocker remains.

After those contracts are resolved, useful extensions would be patron-specific
coal contracts, former-host-dependent border prose, a negotiated Saar/Rhine
customs board, and event reactions to the commission-versus-security power
settlement. They are future depth, not substitutes for the implemented package.
