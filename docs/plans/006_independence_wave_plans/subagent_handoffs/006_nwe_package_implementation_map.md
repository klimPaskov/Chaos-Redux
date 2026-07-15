# Event 006 Northern and Western Europe Package Implementation Map

Date: 2026-07-14
Scope: IW-001, IW-002, IW-003, IW-004, IW-005, IW-006, IW-007, IW-008, IW-009, IW-010, and IW-012
Mode: read-only repository/vanilla exploration; this handoff is the only file changed
Parent objective: provide the exact implementation and preservation map for Scotland, Wales, Cornwall, Brittany, Flanders, Wallonia, Frisia, Rhineland, Bavaria, Saar, and Iceland.

## 1. Executive decision

The current package allocator and force framework are reusable, but none of the scoped tags can be made selectable merely by setting `independence_wave_package_content_ready`. The current initialization path records generic Event 006 provenance only. It does not dispatch country-package politics, a valid command roster, package identity ideas, route availability, focus assignment, AI, formable/league registration, or package-specific assets.

The complete implementation should use these assignments:

| Package | Tag | Focus treatment | Can become content-ready after the proposed integration? | Current blocker |
|---|---:|---|---|---|
| IW-001 Scotland | `SCO` | Full Event 006 framework | Yes, after all package surfaces and audit pass | No dedicated vanilla tree; needs a complete release cabinet/command roster and package assets |
| IW-002 Wales | `WLS` | Full Event 006 framework | Yes, after all package surfaces and audit pass | No dedicated vanilla tree; preserve the vanilla Y Wladfa decision |
| IW-003 Cornwall | `ACX` | Full framework only after a valid release geography exists | **No** | State 123 is South-West England, not a unique Cornwall state; the accepted binding deliberately omits IW-003 |
| IW-004 Brittany | `BRI` | Full Event 006 framework | Yes, after all package surfaces and audit pass | Reuse leaders selectively; sensitive extremist identity must not become the neutral/default authority |
| IW-005 Flanders | `AEX` | Full Event 006 framework | **No under the installed standard map binding** | Anchor state 6 contains Belgium's capital and is protected; changing the anchor/territory contract requires an accepted design update |
| IW-006 Wallonia | `AFX` | Full Event 006 framework | Yes, after all package surfaces and audit pass | New shell needs complete identity, government, command, AI, assets, and localisation |
| IW-007 Frisia | `AGX` | Full Event 006 framework | Yes, after all package surfaces and audit pass | State 36 is a usable distinct anchor, but the new shell is otherwise empty |
| IW-008 Rhineland | `RHI` | Full Event 006 framework | Yes, after all package surfaces and audit pass | Must preserve/reuse the verified registered character conditionally; conflicts with vanilla German reunification content require an explicit policy |
| IW-009 Bavaria | `BAY` | Full Event 006 framework | Yes, after all package surfaces and audit pass | Rupprecht may already have been transferred to Germany by vanilla content; requires a conditional institutional authority; German formable overlap must be resolved |
| IW-010 Saar | `AJX` | Full Event 006 framework | Yes, after all package surfaces and audit pass | Mutually exclusive with Rhineland in `RG-RHINE-SAAR`; new shell needs full content |
| IW-012 Iceland | `ICE` | **Safe additive Event 006 mechanics/decision layer only; preserve `iceland_tree`** | Yes, but only for an absent `ICE` and only after the additive adapter is complete | The installed shared-focus definitions are not included in Iceland's tree; standard-start Iceland is alive and owns its sole state |

“Additive” has a precise limitation in this audit: it can safely publish Event 006 decisions, missions, ideas, variables, route/formable/league hooks, and AI weights without replacing Iceland's tree. It is **not currently a visible focus overlay**. No focus tree in the repository includes the Event 006 `shared_focus` root. A visible Iceland focus branch would require a deliberate static integration into the vanilla/DLC tree and must not be represented as already working.

## 2. Required reference set consulted

The audit used the offline snapshot only for Paradox wiki material. No live Paradox wiki page was opened.

Core offline pages consulted under `paradox_wiki/`:

- Data structures
- Triggers
- Effects
- Modifiers
- Localisation
- Scopes
- On actions
- Event modding
- Decision modding
- Idea modding
- AI modding

System-specific offline pages also consulted:

- Country creation
- National focus modding
- State modding
- Unit modding
- Division modding
- Equipment modding
- Technology modding

Official vanilla documentation consulted under `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/` and adjacent documented systems:

- `script_concept_documentation.md`, including script constants and focus-tree behavior
- `effects_documentation.md`, including country/state transfer, character, event-target, OOB, focus-tree, and technology effects
- `triggers_documentation.md`, including country, character, focus, state, and event-target predicates
- character documentation
- on-action documentation
- decision documentation
- AI strategy, AI strategy-plan, AI template, and AI equipment documentation
- `common/script_constants/documentation.md`

Vanilla examples were inspected for each registered tag's country definition, history, character file, flag set, localisation, OOB, focus assignment, AI plans, and relevant decision/formable collisions. The current Chaos Redux Event 006 specs, matrices, research resolutions, package bindings, source-of-truth map, resume packet, allocator files, force framework, focus framework, decisions, ideas, localisation, country shells, and asset handoffs were reviewed in parallel.

## 3. Current runtime contract and missing link

### 3.1 What already exists

- Region 01 eligibility: `common/scripted_triggers/006_independence_wave_packages_region_01_triggers.txt`.
- Region 01 publishers/reservations: `common/scripted_effects/006_independence_wave_packages_region_01_effects.txt`.
- Stable package constants: `common/script_constants/006_independence_wave_package_constants.txt`.
- Generic origin initialization: `independence_wave_initialize_country_origin` in `common/scripted_effects/006_independence_wave_effects.txt`.
- Frozen-plan release initialization: `independence_wave_initialize_frozen_countries` in `common/scripted_effects/006_independence_wave_execution_effects.txt`.
- Package-to-force mapping: `common/scripted_effects/006_independence_wave_force_package_effects.txt`.
- Dynamic force materialization: `common/scripted_effects/006_independence_wave_force_effects.txt`.
- Full Event 006 focus tree plus detached shared-focus definitions: `common/national_focus/006_independence_wave_focus.txt`.
- Assignment helper and route/ambition/formable flags: `common/scripted_effects/006_independence_wave_focus_effects.txt`.
- Generic Event 006 decision, idea, and localisation layers.

### 3.2 Why every scoped package is presently allocator-locked

`is_independence_wave_candidate_tag_available` requires both:

- `exists = no`; and
- `has_country_flag = independence_wave_package_content_ready`.

No current effect grants that flag to the scoped tags. This is correct fail-closed behavior. The execution validator checks the flag again before releasing the frozen plan.

The current release sequence sets the new capital, then calls `independence_wave_initialize_country_origin`, increments the initialized counter, and clears pending metadata. It never calls a package adapter. Consequently, granting the flag today would permit a release that lacks the package contract required by the trigger comment itself.

### 3.3 Required dispatcher and call sites

Add one bounded region-01 package setup layer, with names following the existing Event 006 convention:

- `common/scripted_effects/006_independence_wave_packages_region_01_setup_effects.txt`
  - `independence_wave_refresh_region_01_content_readiness`
  - `independence_wave_apply_region_01_package_setup`
  - `independence_wave_apply_package_iw_001_setup`
  - `independence_wave_apply_package_iw_002_setup`
  - `independence_wave_apply_package_iw_004_setup`
  - `independence_wave_apply_package_iw_005_setup`
  - `independence_wave_apply_package_iw_006_setup`
  - `independence_wave_apply_package_iw_007_setup`
  - `independence_wave_apply_package_iw_008_setup`
  - `independence_wave_apply_package_iw_009_setup`
  - `independence_wave_apply_package_iw_010_setup`
  - `independence_wave_apply_package_iw_012_setup`
- `common/scripted_triggers/006_independence_wave_packages_region_01_content_triggers.txt`
  - package-specific completeness predicates used by readiness registration and post-setup proof.

The refresh must run in the shared Event 006 allocation path before candidate weights are prepared, not solely in `chaosx.nr6.1`. That keeps standalone and joint Event 5/Event 6 allocation behavior identical. The setup dispatcher must run inside the released country scope in `independence_wave_initialize_frozen_countries`, after `independence_wave_initialize_country_origin` has written `independence_wave_package_id` and the setup event targets are still live, and before the initialized counter is incremented and pending metadata is cleared.

The dispatch must branch on the numeric `independence_wave_package_id`, not on the current cosmetic tag. This preserves package identity through cosmetic-tag transitions and formables.

### 3.4 Required setup order

Within each package adapter:

1. Validate `independence_wave_package_id`, `independence_wave_setup_former_host`, and `independence_wave_setup_anchor_state`.
2. Establish the provisional politics and recruit/reuse the release authority.
3. Recruit or create the package command roster; grant `independence_wave_command_roster_ready` only after the roster exists.
4. Publish package identity ideas and their lifecycle inputs.
5. Publish focus assignment, available government routes, former-host routes, power-struggle inputs, regional ambition, league signatures, and formable signatures.
6. Dispatch the existing force-package mapping, then materialize the force only after the command roster flag is valid. The existing force effect inherits technology from `event_target:independence_wave_setup_former_host`, enforces minimum research slots, creates templates/units, and handles approved air/naval transfer.
7. Publish origin-aware AI behavior.
8. Run a package-specific setup proof and set a setup-complete flag. A failed proof must fail the initialization counter rather than silently accepting a partial country.

No whole-world daily/weekly/monthly on action is needed. Readiness can be registered from the allocator call path and package setup occurs only for countries in the frozen plan.

## 4. Existing map bindings and release geography

| Package | Anchor | Compact states | Extended states | Reservation group | Installed-map finding |
|---|---:|---|---|---|---|
| IW-001 `SCO` | 121 Lothian | 133 Lanark | 120 Highlands, 136 Aberdeenshire, 933 Shetland | `RG-121-120-133` | All listed states are England-owned/core at start and carry `SCO` cores |
| IW-002 `WLS` | 122 Wales | none | none | `RG-122` | England-owned/core and carries a `WLS` core |
| IW-003 `ACX` | unresolved | unresolved | unresolved | unresolved | Registry's state 123 is South-West England, including Plymouth and Exeter; not a distinct Cornwall package |
| IW-004 `BRI` | 14 Brittany | none | none | `RG-14` | France-owned/core and carries a `BRI` core; Brest is the principal port/VP |
| IW-005 `AEX` | 6 Vlaanderen | 977 Antwerp | none | `RG-6` | Both are Belgian core territory; state 6 includes Brussels and Belgium's capital |
| IW-006 `AFX` | 34 Wallonie | none | none | `RG-34` | Belgian core territory; Namur/Liège/Charleroi urban-industrial anchor; no pre-existing `AFX` core |
| IW-007 `AGX` | 36 Friesland | none | none | `RG-36` | Dutch core territory; distinct coastal state; no pre-existing `AGX` core |
| IW-008 `RHI` | 51 Rhineland | none | 42 Moselland/Saar | `RG-RHINE-SAAR` | Germany-owned/core; both states carry `RHI` cores; state 51 contains the Rhine industrial cities |
| IW-009 `BAY` | 52 Oberbayern | 53 Niederbayern, 54 Franken | none | `RG-52-53-54` | Germany-owned/core and all three carry `BAY` cores; Munich is in state 52 |
| IW-010 `AJX` | 42 Moselland/Saar | none | none | `RG-RHINE-SAAR` | Germany-owned/core; carries `RHI`, not `AJX`, core; Saarbrücken is the compact's VP |
| IW-012 `ICE` | 100 Iceland | none | none | `RG-100` | `ICE` owns and cores its sole state in the standard start |

The anchor becomes the released country's capital in the current executor. Therefore the intended capitals are Edinburgh/Lothian (121), Wales/Cardiff (122), Brest/Brittany (14), Brussels/Flanders (6), Wallonia (34), Friesland (36), Rhineland (51), Munich/Oberbayern (52), Saarbrücken/Moselland (42), and Reykjavík/Iceland (100).

Do not edit state history simply to manufacture readiness. The release executor already transfers ownership/control and cores released territory as part of its contract. A state-history edit would change the base scenario and is not justified for these event-origin packages.

## 5. Package dossiers

### 5.1 IW-001 Scotland — `SCO`

**Existing vanilla definition and history**

- Tag: `common/country_tags/00_countries.txt`.
- Country definition: vanilla `common/countries/Scotland.txt`; Commonwealth graphical culture; RGB approximately `232 232 0`.
- History: `history/countries/SCO - Scotland.txt`; capital 121; early infantry/truck technology; 20 convoys; democratic-leaning politics; generic advisor roster; no country leader and no OOB.
- Characters: `common/characters/SCO.txt`; generic advisors with generic small portraits, not a release head of government or field command roster.
- Flags: vanilla ideology variants exist in all three flag sizes; there is no separate base file, so route use must follow the actual ideology filenames.
- Focus tree: no dedicated tree assignment; the tag falls through to the 56-focus `generic_focus` tree. Its 1939 history marks generic focuses complete.
- AI: no Scotland-specific strategy plan or strategy file found.
- Localisation: country names exist; tag-specific party names and Event 006 cabinet/route text do not.

**Implementation decision**

- Assign `constant:independence_wave_focus_assignment.full_framework` and call `independence_wave_assign_focus_framework`.
- This is a reviewed replacement of the generic tree, not a replacement of bespoke national content.
- Publish constitutional, popular/labor, traditional/cultural, and emergency-military route availability from the accepted registry. Do not publish patron-client or radical sovereignty unless the source-of-truth route matrix is explicitly amended.
- Register Celtic and North Atlantic league/formable participation as defined by the accepted formable/league registries.
- Use a sourced institutional provisional authority or a verified historical person. Do not invent a famous leader. If a fictional individual is approved, it needs the accepted regional name-pool and generated-portrait process.
- Add a real command roster or an explicitly institutionalized commander character before setting `independence_wave_command_roster_ready`.
- Preserve the existing core geography and vanilla flags unless a route specifically needs a sourced variant.

**Readiness result**: can be marked content-ready when the adapter, cabinet/command characters, package ideas, AI, localisation, route/formable wiring, and required assets all exist and pass package audit.

### 5.2 IW-002 Wales — `WLS`

**Existing vanilla definition and history**

- Tag and country definition are vanilla; Commonwealth graphical culture; RGB approximately `255 0 0`.
- `history/countries/WLS - Wales.txt`: capital 122; early infantry/truck/fuel-silo technology; 20 convoys; democratic-leaning politics; generic advisors; no country leader and no OOB.
- `common/characters/WLS.txt`: generic advisor roster only, with generic small portraits.
- Vanilla flags provide ideology variants in all sizes, without a separate base file.
- No dedicated focus tree; the tag receives `generic_focus` and has generic 1939 completions.
- No Wales-specific AI plan found.
- Vanilla `common/decisions/WLS.txt` provides `WLS_restore_y_wladfa_decision`; Event 006 must not hide or duplicate it.
- Country names exist; party/cabinet/package localisation is absent.

**Implementation decision**

- Use the full Event 006 framework after explicit generic-tree review.
- Publish constitutional, popular/labor, traditional/cultural, and emergency-military routes.
- Register Celtic participation and any accepted Celtic/North Atlantic cross-links without duplicating `WLS_restore_y_wladfa_decision`.
- Provide a sourced institutional authority and command roster; vanilla advisor definitions are not sufficient proof of command readiness.
- Retain Wales's standalone vanilla decision file and make Event 006 decision categories coexist through narrow visibility triggers.

**Readiness result**: can be marked content-ready after the complete adapter and preservation checks; Y Wladfa coexistence belongs in its audit scenario.

### 5.3 IW-003 Cornwall — `ACX`

**Existing Chaos Redux shell**

- `ACX` is reserved in `common/country_tags/006_independence_wave_countries.txt`.
- `common/countries/006_independence_wave_ACX.txt` and `history/countries/ACX - Event 006 Country Shell.txt` are shells only.
- Basic country-name localisation exists in `localisation/english/006_independence_wave_countries_l_english.yml`.
- No vanilla tag/history/characters/flags/tree/OOB/AI exist for `ACX`.

**Hard map blocker**

The candidate registry's old state 123 binding is not a unique Cornish state on the installed map. It is South-West England and includes Plymouth and Exeter. The accepted current-map audit therefore deliberately omits `can_plan_independence_wave_package_iw_003` and its publisher. Creating the country on all of state 123 would violate the package identity and the no-fallback rule.

**Implementation decision**

- Do not add the package to region-01 automatic allocation.
- Do not set `independence_wave_package_content_ready` on `ACX`.
- Do not create a substitute anchor, claim-only release, or South-West England fallback.
- Once an installed map/spec supplies a unique Cornish anchor and an accepted host-survival contract, use the full Event 006 framework because `ACX` has no tree to preserve.

**Readiness result**: cannot be content-ready in this tranche.

### 5.4 IW-004 Brittany — `BRI`

**Existing vanilla definition and history**

- Registered vanilla tag with western graphical culture; RGB approximately `118 99 151`.
- `history/countries/BRI - Brittany.txt`: capital 14; three research slots; broad starting technology/doctrine; 20 convoys; neutrality is ruling; no OOB.
- The history creates four country leaders:
  - Yann-Morvan Gefflot, Stalinist route, generic Europe portrait 1.
  - Morvan Marchal, socialist route, generic Europe portrait 2.
  - Olier Mordrel, fascist/Nazi route, generic Europe portrait 6.
  - Maurice Duhamel, centrist route, generic Europe portrait 4.
- `common/characters/BRI.txt` otherwise supplies generic advisors, not a complete command roster.
- Flags: a base flag plus communism, fascism, and neutrality variants exist in every size; the base supplies democratic display.
- No dedicated focus tree or Brittany AI plan; it receives `generic_focus`.
- Party localisation exists for NPB, URB, FLB, and PCB.

**Implementation decision**

- Use the full Event 006 framework.
- Reuse an existing leader only when the release route and date make that leader valid and the character is not active elsewhere. A neutral/default release should use Maurice Duhamel or an accurately localized institutional cabinet, not Olier Mordrel.
- Olier Mordrel is collaboration/extremism-sensitive. Vanilla inclusion proves the engine identifier, not design endorsement. His use must be route-specific, accurately named, and consistent with the accepted sensitivity research.
- Publish constitutional, popular/labor, traditional, emergency-military, and patron-client routes as accepted for Brittany.
- Register Celtic and North Atlantic participation.
- Add a separate valid command roster; country-leader entries and generic advisors do not satisfy force readiness.

**Readiness result**: can be marked content-ready after leader-route validation, command assets, AI, ideas, focus assignment, and package audit.

### 5.5 IW-005 Flanders — `AEX`

**Existing Chaos Redux shell**

- Reserved tag/country/history/localisation shell already exists.
- No vanilla `AEX` definition, characters, flags, OOB, focus, AI, party localisation, or core history exists.
- The tag collision audit found no current country-tag or cosmetic-tag collision.

**Hard map blocker**

The accepted binding uses state 6 as anchor and 977 Antwerp as compact territory. State 6 contains Brussels and is Belgium's current capital. The release planner protects host capitals. Consequently, in the standard 1936 map state, Flanders cannot pass anchor availability while Belgium's capital remains protected. Marking the content shell complete would not make the package selectable and would misrepresent the installed binding.

Changing the anchor to Antwerp alone is not a safe implementation detail: the source-of-truth binding says state 6 is the anchor and 977 is compact territory. Such a change affects capital, territorial identity, release viability, and Belgium/Wallonia interaction and needs an accepted design revision.

**Implementation decision**

- The eventual package should use the full Event 006 framework.
- Planned route mapping: constitutional, popular/labor, radical-sovereignty/nationalist, and patron-client.
- Register Low Countries formable/league participation.
- Build a sourced civic provisional authority, command roster, route flags, party names, identity ideas, and industrial/port AI.
- Keep `independence_wave_package_content_ready` absent until the capital/anchor contract is explicitly resolved, even if all content surfaces are authored.

**Readiness result**: cannot be marked content-ready under the installed standard-map contract.

### 5.6 IW-006 Wallonia — `AFX`

**Existing Chaos Redux shell**

- Reserved tag/country/history/name-localisation shell exists.
- No vanilla characters, flags, OOB, focus, AI, party localisation, or state core exists for `AFX`.
- State 34 is distinct Belgian territory and does not contain Belgium's protected capital.

**Implementation decision**

- Use the full Event 006 framework.
- Publish constitutional, popular/labor, emergency-military, and patron-client routes.
- Register Low Countries participation and the accepted Meuse/industrial regional ambition without inventing a second unsupported formable.
- Use a sourced civic/institutional provisional cabinet. Any fictional individual requires a regional name pool and generated portrait; do not present invented leadership as historical.
- Build industrial militia/regular-defector command characters before force materialization.
- Add final civic and route flags in all three sizes; a country flag does not require a `.gfx` sprite definition, while leader portraits do.

**Readiness result**: can be marked content-ready after the full package and asset/audit checklist is complete.

### 5.7 IW-007 Frisia — `AGX`

**Existing Chaos Redux shell**

- Reserved tag/country/history/name-localisation shell exists.
- No vanilla characters, flags, OOB, focus, AI, party localisation, or `AGX` state core exists.
- State 36 Friesland is a distinct Dutch coastal state and is a valid current-map anchor, subject to ordinary host-survival checks.

**Implementation decision**

- Use the full Event 006 framework.
- Publish constitutional, cultural-council, labor/popular, and patron-client routes. Map cultural council into the popular-council framework unless the source-of-truth focus architecture is amended; do not imply a dynastic/traditional route that is not accepted for the package.
- Register the North Sea coastal league/ambition and accepted Low Countries connections.
- Provide a sourced municipal/coastal authority and coastal-defense command roster.
- Add civic and route flags, parties, ideas, AI, localisation, and portrait sprites.

**Readiness result**: can be marked content-ready after complete implementation and a state-36/host-survival scenario audit.

### 5.8 IW-008 Rhineland — `RHI`

**Existing vanilla definition and history**

- Registered vanilla tag with western graphical culture; RGB approximately `0 153 51`.
- `history/countries/RHI - Rhineland.txt`: capital 51; three research slots; substantial German regional technology/doctrine; 50 convoys; 0.75 stability; democratic plurality; no OOB.
- `common/characters/RHI.txt` defines and the history recruits `RHI_josef_friedrich_matthes` as a socialist country leader.
- Portrait asset: `gfx/leaders/RHI/portrait_RHI_josef_matthes.dds` with its vanilla sprite definition.
- Ideology flags exist in all three sizes, without a separate base flag.
- No dedicated focus tree or RHI-specific AI plan; receives `generic_focus`.
- No complete tag-specific party/package localisation was found.

**Implementation decision**

- Use the full Event 006 framework.
- Reuse `RHI_josef_friedrich_matthes` only when he remains a valid `RHI` character and the chosen release politics match. Otherwise use a provisional institutional cabinet until a sourced leader is assigned; do not duplicate the character.
- Publish constitutional, popular/labor, emergency-military, and patron-client routes; register neutral-corridor/Rhine ambition and `FORM-04` Rhine participation.
- Add a real command roster, since the country leader does not satisfy force readiness.
- The extension state 42 must be trimmed whenever IW-010 Saar owns the same reservation group. The existing reservation group already enforces at most one automatic member in the wave.

**Vanilla content collision**

`RHI` can see vanilla German reunification/formable content. The complete tranche must explicitly decide whether an Event 006-origin Rhineland keeps that path, has it hidden while the origin is active, or routes into an Event 006 settlement. Do not leave two overlapping Rhine/Germany identity progressions available by accident.

**Readiness result**: can be marked content-ready only after the German-formable interaction is deliberately resolved and the package surfaces pass audit.

### 5.9 IW-009 Bavaria — `BAY`

**Existing vanilla definition and history**

- Registered vanilla tag with western graphical culture; RGB approximately `233 231 246`.
- `history/countries/BAY - Bavaria.txt`: capital 52; three research slots; German regional technology/doctrine; 50 convoys; 0.75 stability; neutrality dominant; no OOB.
- `common/characters/BAY.txt` defines `BAY_rupprecht_of_bavaria` with a despotic country-leader role and a skill-4 field-marshal role.
- Portraits: `gfx/leaders/BAY/portrait_BAY_rupprecht_of_bavaria.dds` plus the vanilla small idea portrait/sprite.
- Ideology flags exist in all sizes, without a separate base flag.
- No dedicated focus tree or BAY-specific AI plan; receives `generic_focus`.

**Character ownership collision**

Vanilla Germany's `GER_fan_prussian_militarism` branch can transfer Rupprecht to Germany when Bavaria does not exist. A later Event 006 release must not create or recruit a duplicate. The adapter must check that the character is still valid for/recruitable by Bavaria. If not, use a provisional institutional authority and command structure until a sourced replacement is available.

**Implementation decision**

- Use the full Event 006 framework.
- Publish constitutional, popular/labor, traditional/restoration, and emergency-military routes.
- The power struggle should cover the accepted court/assembly or court/guardianship tension rather than assume Rupprecht is always available.
- Register the South German/restored-kingdom regional ambition. The current formable registry does not provide a clear Event 006 formable row for this identity; if the design intends a true formable rather than an ambition, the spec must be amended before implementation.

**Vanilla content collision**

`BAY` participates in vanilla Germany formable/reunification decisions. Resolve coexistence with the Event 006 ambition deliberately, as for `RHI`.

**Readiness result**: can be marked content-ready after character-transfer handling, command roster, full package content, and formable-policy audit.

### 5.10 IW-010 Saar — `AJX`

**Existing Chaos Redux shell**

- Reserved tag/country/history/name-localisation shell exists.
- No vanilla definition, characters, flags, OOB, focus, AI, parties, or `AJX` core exists.
- No present country-tag or cosmetic-tag collision was found.

**Implementation decision**

- Use the full Event 006 framework.
- Publish constitutional, popular/labor, patron-client, and neutral-commission routes. The neutral commission should be a distinct package authority/route expression; do not silently relabel it as military rule.
- Register `FORM-04` Rhine Compact participation.
- Provide a municipal/industrial provisional authority and industrial-security command roster, with sourced civic symbols and route variants.
- Preserve the `RG-RHINE-SAAR` mutual exclusion. IW-008 and IW-010 must never be released in the same automatic wave. Rhineland's extended state 42 must not survive reservation when Saar owns the group.

**Readiness result**: can be marked content-ready after full package implementation; mutual exclusion is expected behavior, not a blocker.

### 5.11 IW-012 Iceland — `ICE`

**Existing vanilla definition and history**

- Registered vanilla tag, western graphical culture, RGB approximately `100 125 175`, and `use_legacy_ai_pp_spend = yes`.
- `history/countries/ICE - Iceland.txt`: capital/sole state 100; `set_oob = ICE_1936`; two research slots; 30 convoys; democratic start; substantial DLC-conditional ideas, technology, variables, and character setup; uses `ICE_personal_union` in the relevant path.
- `history/units/ICE_1936.txt`: Ríkislögreglan template plus production lines, but no fielded division. The Event 006 dynamic force package remains necessary after a release.
- With Arms Against Tyranny, `common/characters/ICE.txt` recruits a large bespoke roster, including Hermann Jónasson, Gísli Sigurbjörnsson, Brynjólfur Bjarnason, Sveinn Björnsson, Ólafur Thors, advisors, and Björn Sveinsson Björnsson as a commander. DLC portrait assets/sprites exist.
- Without that DLC, history creates a smaller fallback leader roster including Sveinn Björnsson, Johannes Valurson, Haraldur Gudmunsson, and Einar Olgeirsson; base portrait coverage is narrower.
- Base plus communism/fascism/neutrality flags exist in all sizes; the base is the democratic flag.
- Dedicated `iceland_tree` contains about 89 focuses and includes Nordic shared content. This is meaningful national content.
- Iceland has dedicated AI strategy and historical/alternate strategy plans.
- Party localisation exists for Framsóknarflokkurinn, Kommúnistaflokkur, Þjóðernissinna, and Heimastjórnarflokkurinn.

**Implementation decision**

- Never call `load_focus_tree = independence_wave_focus_tree` for `ICE`.
- Assign the additive mode only to publish Event 006 mechanics and decisions while retaining `iceland_tree` and existing AI plans.
- The current Event 006 shared-focus blocks are detached definitions. No existing tree contains `shared_focus = independence_wave_overlay_take_stock_of_independence`. Therefore do not claim that ICE receives a visible Event 006 focus branch.
- If visible focus integration is required, prepare an explicit, version-sensitive static integration proposal for `iceland_tree`; do not override/copy the DLC tree without approval.
- Reuse the correct DLC/non-DLC vanilla leader and command roster where it is still valid. Add only the missing Event 006 setup proof and avoid duplicate recruitment.
- Preserve `ICE_personal_union` unless an Iceland route itself legitimately changes the cosmetic identity.
- Preserve dedicated Iceland AI strategies/plans; add Event 006 origin-aware strategy/decision weights rather than replacing them.
- Reconcile Event 006 North Atlantic formable/league content with vanilla Nordic League/Scandinavia content and Iceland's Nordic shared focus.
- Audit vanilla Iceland decisions that can produce Scottish/Welsh communist uprisings in states 121/122 so a returned Event 006 Iceland does not duplicate or corrupt active SCO/WLS origins.

**Availability reality**

In the standard start, `ICE` exists and owns its sole state. The candidate-tag trigger therefore rejects it. If Iceland has ceased to exist later, the host-survival/protected-capital logic must still reject any release that would consume a living host's sole state.

**Readiness result**: can be marked content-ready after the additive non-focus adapter, DLC-safe character/command checks, preserved-tree/AI audit, Nordic-content collision policy, localisation, ideas, and assets are complete. The tag will still be unavailable while it exists, by design.

## 6. Full implementation file map

The following is the minimum complete tranche surface. Exact names may be folded into existing Event 006 files where that is cleaner, but every responsibility must remain identifiable and documented.

### 6.1 Runtime and package adapters

- Add `common/scripted_effects/006_independence_wave_packages_region_01_setup_effects.txt` with the refresh, dispatcher, and package effects listed in section 3.
- Add `common/scripted_triggers/006_independence_wave_packages_region_01_content_triggers.txt` with readiness and post-setup proof predicates.
- Update `common/scripted_effects/006_independence_wave_package_allocator_effects.txt` at the shared allocation entry so region readiness is refreshed before weights in standalone and joint flows.
- Update `common/scripted_effects/006_independence_wave_execution_effects.txt` so released countries call the package dispatcher before pending metadata is cleared.
- Reuse, do not duplicate, `independence_wave_initialize_country_origin`, `independence_wave_dispatch_force_package_mapping`, force materialization helpers, `independence_wave_assign_focus_framework`, route helpers, ambition/formable/league helpers, and cleanup hooks.
- If new reusable dynamic effects are required, add them to `common/scripted_effects/chaosx_dynamic_effects.txt` and document purpose/scope/inputs/defaults/side effects/example in `common/scripted_effects/chaosx_dynamic_effects.md` in the same change.

### 6.2 Country definitions and history

- Preserve vanilla country definitions/history for `SCO`, `WLS`, `BRI`, `RHI`, `BAY`, and `ICE`; use runtime Event 006 adapters rather than wholesale overrides.
- Complete the existing country/history shells for `AEX`, `AFX`, `AGX`, and `AJX` only to the degree required for stable load-time identity. Runtime politics, characters, and force setup should remain in package adapters.
- Leave the `ACX` shell reserved but disabled until geography is accepted.
- Do not add base OOB files for Event 006 releases unless a package truly requires a history-start OOB. The existing runtime force system is the correct release-time mechanism.
- Do not add static state cores/ownership for new tags solely for Event 006. The execution layer owns runtime transfer/core behavior.

### 6.3 Characters and command rosters

- Add `common/characters/006_independence_wave_region_01_characters.txt` for new institutional/civic leaders and commanders needed by `SCO`, `WLS`, `AEX`, `AFX`, `AGX`, and `AJX`, plus any audited institutional alternatives for `BRI`, `RHI`, and `BAY`.
- Reuse vanilla identifiers for `RHI_josef_friedrich_matthes`, `BAY_rupprecht_of_bavaria`, Brittany's existing leaders, and the DLC-appropriate Iceland roster; never duplicate them.
- Add portrait sprite definitions to `interface/006_independence_wave_region_01_portraits.gfx` and final DDS portraits under a stable Event 006 leader asset directory.
- Each adapter must prove a command character exists before granting `independence_wave_command_roster_ready`.

### 6.4 Ideas and package identity

- Add package-specific founding/identity ideas in `common/ideas/006_independence_wave_region_01_ideas.txt`, using the accepted idea lifecycle matrix.
- Add corresponding localisation in `localisation/english/006_independence_wave_region_01_ideas_l_english.yml`.
- Keep shared Event 006 ideas in `common/ideas/006_independence_wave_ideas.txt`; do not duplicate the shared instability/recognition/command concepts per country.
- Package ideas should express industrial, coastal, agrarian/restoration, island, or regional institutional character and feed the shared mechanics rather than provide disconnected flat bonuses.

### 6.5 Focus, decisions, formables, and leagues

- Full-framework packages: `SCO`, `WLS`, `BRI`, `AEX`, `AFX`, `AGX`, `RHI`, `BAY`, `AJX`.
- Preserved-tree additive package: `ICE`.
- Disabled: `ACX`.
- Publish only the route flags accepted for each package. Use existing focus helpers instead of cloning focus blocks.
- Add package-specific regional ambition/league/formable decision wiring to the existing Event 006 decision framework, or to a bounded `common/decisions/006_independence_wave_region_01_decisions.txt` if separation is clearer.
- Reconcile rather than duplicate vanilla `WLS_restore_y_wladfa_decision`, German formables for `RHI`/`BAY`, and Nordic/Scandinavian content for `ICE`.
- Do not expose detached Event 006 shared focuses as if they were installed in Iceland's tree.

### 6.6 AI

- Add package AI in `common/ai_strategy/006_independence_wave_region_01.txt` and, only where needed, `common/ai_strategy_plans/006_independence_wave_region_01.txt`.
- For runtime-created tags, static `allowed` must use stable tag/original-tag conditions. Vanilla documentation makes strategy-plan `allowed` a startup evaluation; do not put `has_country_flag = independence_wave_active_origin` there and expect a newly released country to acquire the plan.
- Use runtime `enable`/`abort`, decision `ai_will_do`, focus `ai_will_do`, and package flags/variables for origin-sensitive behavior.
- Focus priorities belong only to full-framework packages. Iceland retains its dedicated vanilla AI plans and receives narrow Event 006 decision/strategy modifiers.
- AI must account for former-host diplomacy, route identity, formable/league competition, force profile, industry/port/island character, and the RHI/AJX mutual exclusion.

### 6.7 Localisation and assets

- Complete country-party, provisional-authority, commander, biography, route, idea, decision, mission, ambition, formable, tooltip, and AI-visible text in UTF-8 BOM localisation files without `:0`.
- Keep `localisation/english/006_independence_wave_countries_l_english.yml` for stable country identities and add a bounded region-01 file for package text.
- Add final flag files for `ACX`, `AFX`, `AGX`, and `AJX` under `gfx/flags/`, `gfx/flags/medium/`, and `gfx/flags/small/`; add route/cosmetic variants only when actually used and sourced. Do not add AEX: Flanders remains the vanilla `BEL_flanders` cosmetic overlay.
- Preserve vanilla flags for the registered tags unless the route explicitly changes identity.
- Register portrait, idea, decision, and focus sprites in `.gfx` files before final asset production. Country flags themselves are selected by filename and do not need `.gfx` registration.
- Update `docs/assets/006_independence_wave/gfx_handoff.md`, package asset coverage, provenance/source register, contact sheets, and manifests through `chaos-redux-event-assets` before readiness.

### 6.8 Documentation and data alignment

- Update `docs/events/006_independence_wave.md` with the region-01 runtime adapter and focus-preservation behavior.
- Add/update the mechanic/package documentation required by AGENTS.md, including step-by-step behavior, interactions, icon paths/names, future plans, and extension suggestions.
- Fold accepted binding changes into the Event 006 specs rather than leaving them only in a plan handoff.
- Keep package registry, AI matrix, regional overlay matrix, idea lifecycle matrix, formable registry, force mapping CSV, event details/evolution details, and spreadsheet/presentation wording aligned with exact in-game localisation.

## 7. Adapter field contract by package

Every package adapter should explicitly publish or preserve these fields. An unset field must be an intentional “not available,” not an accidental omission.

| Field | SCO | WLS | BRI | AEX | AFX | AGX | RHI | BAY | AJX | ICE |
|---|---|---|---|---|---|---|---|---|---|---|
| Focus assignment | full | full | full | full | full | full | full | full | full | additive mechanics only |
| Constitutional | yes | yes | yes | yes | yes | yes | yes | yes | yes | preserve vanilla + Event 006 adapter if accepted |
| Popular/labor | yes | yes | yes | yes | yes | yes | yes | yes | yes | preserve vanilla + Event 006 adapter if accepted |
| Traditional | yes | yes | yes | no | no | no unless matrix says cultural=traditional | no | yes | no | do not publish blindly |
| Emergency military | yes | yes | yes | no unless accepted nationalist route requires it | yes | no | yes | yes | no | do not publish blindly |
| Patron client | no unless matrix amended | no unless matrix amended | yes | yes | yes | yes | yes | no unless matrix amended | yes | only when accepted by Iceland adapter |
| Radical sovereignty | no unless matrix amended | no unless matrix amended | no unless matrix amended | yes (nationalist) | no | no | no | no | no | do not publish blindly |
| Regional/formable family | Celtic + North Atlantic | Celtic | Celtic + North Atlantic | Low Countries | Low Countries/Meuse ambition | North Sea/Low Countries link | Rhine | South German/restoration ambition | Rhine | North Atlantic, reconciled with Nordic content |
| Force roster source | new/sourced | new/sourced | conditional vanilla leader + new command | new | new | new | conditional vanilla leader + new command | conditional Rupprecht + institutional alternative | new | DLC-safe vanilla roster plus Event 006 proof |

This table is an implementation map, not authority to override a contradictory accepted matrix. If the source-of-truth route matrix differs, update the specs and this table together before code.

## 8. Content-ready gate

`independence_wave_package_content_ready` is a publishable build gate, not a “tag exists” marker. The readiness refresh should set it only when all compile-time assets/files for that package are installed. Runtime setup proof remains separate.

For each tag, readiness requires:

- stable tag/country definition and non-colliding identity;
- accepted current-map anchor and host-survival contract;
- complete package setup effect and numeric package-ID dispatch;
- provisional politics and valid head of government/authority;
- valid command roster and command-ready proof;
- force mapping and materialization compatibility;
- full framework or explicitly preserved-tree additive assignment;
- route, former-host, power-struggle, ambition, league, and formable fields;
- package identity idea and lifecycle behavior;
- origin-aware AI behavior;
- complete player-facing localisation;
- required flags, portraits, icons, sprite definitions, provenance, and manifests;
- collision policy for vanilla decisions/formables/characters/AI;
- package-specific audit evidence.

Per-package readiness publication after the proposed integration:

- Settable: `SCO`, `WLS`, `BRI`, `AFX`, `AGX`, `RHI`, `BAY`, `AJX`, and `ICE` after their full checklists pass.
- Not settable in this tranche: `ACX` (invalid geography) and `AEX` (protected-capital anchor conflict).
- `ICE` being ready does not make it eligible while it exists; `exists = no` remains a separate availability guard.
- `RHI` and `AJX` may both be ready, but `RG-RHINE-SAAR` permits at most one selected package in a wave.

Do not set readiness unconditionally for every reserved Event 006 shell. Register only explicitly completed packages. The executor's second readiness check should remain intact.

## 9. Preservation and collision checklist

### Focus trees

- `SCO`, `WLS`, `BRI`, `RHI`, and `BAY`: reviewed generic-tree replacement is safe once package content is complete.
- `AEX`, `AFX`, `AGX`, and `AJX`: no existing tree; full Event 006 framework is correct.
- `ICE`: preserve `iceland_tree`; additive Event 006 mechanics only.
- `ACX`: no assignment until geography is resolved.

### Characters and portraits

- Never duplicate `RHI_josef_friedrich_matthes`.
- Never duplicate `BAY_rupprecht_of_bavaria`; handle his possible transfer to Germany.
- Reuse Brittany's leaders only on compatible routes; do not make Olier Mordrel the route-neutral authority.
- Select Iceland characters according to installed DLC/history behavior and do not recruit the same person twice.
- Generic advisor portraits are not evidence of a complete release cabinet or command roster.

### Decisions/formables

- Preserve `WLS_restore_y_wladfa_decision`.
- Resolve `RHI`/`BAY` overlap with vanilla German reunification/formable decisions.
- Resolve `ICE` overlap with Nordic League, Scandinavia, Nordic shared focuses, and its SCO/WLS uprising decisions.
- Preserve Event 006 `RG-RHINE-SAAR` exclusion.
- Clarify whether Bavaria's accepted identity is an ambition or a true formable before adding a formable decision.

### Flags and cosmetic tags

- Use `original_tag` and Event 006 package variables/flags for identity logic so cosmetic tags do not break adapters.
- Preserve `ICE_personal_union` until a legitimate Iceland route changes it.
- New tags `ACX`, `AEX`, `AFX`, `AGX`, and `AJX` were collision-free in the 2026-07-14 repository audit, but the collision audit must be rerun if registries change.
- Final route flags must be sourced/generated as distinct, documented designs; recoloring one still is not evidence of a researched route identity.

### State/host safety

- Do not release Cornwall from all of state 123.
- Do not bypass Belgium's protected capital to force Flanders through.
- Do not consume a living host's sole state for Iceland.
- Do not release both Rhineland and Saar in one wave.

## 10. Meaningful validation scenarios for the completion tranche

These scenarios are specific enough to catch package integration failures and should be part of the eventual completion evidence:

1. A Scotland release with compact and extended territory receives the full Event 006 tree, correct authority/commander, dynamic force, Celtic/North Atlantic hooks, and no generic-tree remnants presented as active package content.
2. A Wales release keeps `WLS_restore_y_wladfa_decision` while receiving its Event 006 routes and force package.
3. Brittany selects a neutral/constitutional authority without assigning Olier Mordrel; an explicitly extremist route can use him only under its route gate.
4. Standard-start Belgium keeps state 6 protected, so Flanders is not selected; Wallonia can still be evaluated independently.
5. Wallonia and Frisia receive valid new-tag flags, parties, leaders, commanders, ideas, AI, and full focus framework.
6. A Rhineland/Saar allocation selects no more than one package; Rhineland cannot also take state 42 when Saar owns the reservation.
7. Bavaria released before and after Germany's Rupprecht-transfer content never duplicates Rupprecht and always has a valid authority/command path.
8. A returned Iceland retains `iceland_tree`, its dedicated AI, valid DLC-specific roster, and cosmetic identity while gaining Event 006 decisions/mechanics; it does not show a nonexistent Event 006 focus branch.
9. Iceland remains ineligible while alive in the standard start, and no sole-state host is erased to create it.
10. The frozen executor rejects a country whose readiness flag or post-setup proof is missing rather than incrementing the initialized count.

## 11. Blockers requiring parent/user design authority

1. **Cornwall geography**: a unique installed-map Cornwall state or an explicit map change is required. No fallback release is acceptable.
2. **Flanders anchor**: state 6 is Belgium's capital. The accepted binding must either stay blocked or be revised with explicit capital/territory/host-survival design authority. Antwerp-only substitution is not an implementation assumption.
3. **Visible Iceland focus integration**: the current shared focuses are detached. Preserving Iceland means a non-focus additive layer unless a static DLC-tree integration is explicitly approved.
4. **German formable coexistence**: `RHI` and `BAY` need a deliberate policy for vanilla Germany reunification content.
5. **Bavarian formable scope**: clarify whether South German/restored-kingdom content is a regional ambition or a formal Event 006 formable.
6. **Final real-person/symbol sourcing**: Scotland, Wales, and the new tags still require approved institutional/historical leadership and final civic/route asset provenance. Do not substitute unsourced famous people or invented “historical” flags.

## 12. Exact installed reference inventory

This inventory records the concrete files and identifiers behind the decisions above so implementation does not need to rediscover them.

### 12.1 Vanilla registered-country files

All six registered tags are declared in:

- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/country_tags/00_countries.txt`

| Tag | Country definition | Country history | Character source |
|---|---|---|---|
| `SCO` | `common/countries/Scotland.txt` | `history/countries/SCO - Scotland.txt` | `common/characters/SCO.txt` |
| `WLS` | `common/countries/Wales.txt` | `history/countries/WLS - Wales.txt` | `common/characters/WLS.txt` |
| `BRI` | `common/countries/Brittany.txt` | `history/countries/BRI - Brittany.txt` | `common/characters/BRI.txt` plus leaders created in history |
| `RHI` | `common/countries/Rhineland.txt` | `history/countries/RHI - Rhineland.txt` | `common/characters/RHI.txt` |
| `BAY` | `common/countries/Bavaria.txt` | `history/countries/BAY - Bavaria.txt` | `common/characters/BAY.txt` |
| `ICE` | `common/countries/Iceland.txt` | `history/countries/ICE - Iceland.txt` | `common/characters/ICE.txt` plus non-AAT history-created leaders |

Relevant focus/AI files:

- Generic tree: `common/national_focus/generic.txt`, tree ID `generic_focus`.
- Iceland tree: `common/national_focus/iceland.txt`, tree ID `iceland_tree`, `original_tag = ICE`, and `shared_focus = NORDIC_form_joint_alliance`.
- Iceland AI strategy: `common/ai_strategy/ICE.txt`.
- Iceland historical plan: `common/ai_strategy_plans/ICE_historical_strategy_plan.txt`.
- Iceland alternate plans: `common/ai_strategy_plans/ICE_alternate_strategy_plan.txt`, containing `ICE_alt_democratic_strategy_plan`, `ICE_fascist_strategy_plan`, and `ICE_communist_strategy_plan`.
- No tag-specific focus or AI file was found for `SCO`, `WLS`, `BRI`, `RHI`, or `BAY`.

Relevant exact portrait identifiers:

- `RHI_josef_friedrich_matthes` uses `GFX_portrait_RHI_josef_matthes`, defined in `interface/_leader_portraits.gfx`, texture `gfx/leaders/RHI/portrait_RHI_josef_matthes.dds`.
- `BAY_rupprecht_of_bavaria` uses `GFX_portrait_BAY_rupprecht_of_bavaria`, defined in `interface/_leader_portraits.gfx`, texture `gfx/leaders/BAY/portrait_BAY_rupprecht_of_bavaria.dds`; its small portrait is `GFX_portrait_BAY_rupprecht_of_bavaria_small` in `interface/ideas.gfx`, texture `gfx/interface/ideas/portrait_BAY_rupprecht_of_bavaria_small.dds`.
- Base-game Sveinn Björnsson uses `GFX_portrait_ICE_sveinn_bjornsson`/the corresponding lower-case asset path `gfx/leaders/ICE/portrait_ice_sveinn_bjornsson.dds`. AAT `common/characters/ICE.txt` references the broader `GFX_portrait_ICE_*` roster, including Hermann Jónasson, Gísli Sigurbjörnsson, Brynjólfur Bjarnason, Sveinn Björnsson, Ólafur Thors, and Björn Sveinsson Björnsson.
- Brittany's four history-created leaders use generic European portrait slots, not dedicated Breton portrait textures.
- Scotland/Wales character files provide generic advisor portraits only.

### 12.2 Chaos Redux new-tag shells

All five tags are declared in `common/country_tags/006_independence_wave_countries.txt` and point to the following definitions. Their dormant history files intentionally contain no setup.

| Tag | Definition | Dormant history | Existing shell identity |
|---|---|---|---|
| `ACX` | `common/countries/006_independence_wave_ACX.txt` | `history/countries/ACX - Event 006 Country Shell.txt` | `commonwealth_gfx`, RGB `54 73 92` |
| `AEX` | `common/countries/006_independence_wave_AEX.txt` | `history/countries/AEX - Event 006 Country Shell.txt` | `western_european_gfx`, RGB `235 196 54` |
| `AFX` | `common/countries/006_independence_wave_AFX.txt` | `history/countries/AFX - Event 006 Country Shell.txt` | `western_european_gfx`, RGB `145 37 56` |
| `AGX` | `common/countries/006_independence_wave_AGX.txt` | `history/countries/AGX - Event 006 Country Shell.txt` | `western_european_gfx`, RGB `48 116 170` |
| `AJX` | `common/countries/006_independence_wave_AJX.txt` | `history/countries/AJX - Event 006 Country Shell.txt` | `western_european_gfx`, RGB `83 109 131` |

Existing new-tag localisation is limited to the base/ideology country-name and adjective set in `localisation/english/006_independence_wave_countries_l_english.yml`. No party, authority, character, biography, AI, route, or package identity localisation is provided by these shells.

### 12.3 Exact state-history sources

The installed vanilla state filenames are important because several filenames and displayed state names are historically stale or counterintuitive:

- `history/states/6-Belgium.txt` — displayed Vlaanderen; contains Brussels and Belgium's capital.
- `history/states/977 - Antwerp.txt` — Antwerp compact state.
- `history/states/14-Brittany.txt`.
- `history/states/34-Wallonie.txt`.
- `history/states/36-Friesland.txt`.
- `history/states/42-Rhineland.txt` — displayed Moselland in the current localisation; Saarbrücken is here.
- `history/states/51-Moselland.txt` — displayed Rhineland in the current localisation; Rhine urban-industrial anchor.
- `history/states/52-Wuttemberg.txt` — displayed Oberbayern; Munich is here.
- `history/states/53-Oberbayern.txt` — displayed Niederbayern in the current localisation.
- `history/states/54-Bayreuth.txt` — displayed Franken in the current localisation.
- `history/states/100-Iceland.txt`.
- `history/states/120-Scottish Highlands.txt`.
- `history/states/121-Scottish Lowlands.txt` — displayed Lothian.
- `history/states/122-Wales.txt`.
- `history/states/123-Cornwall.txt` — displayed South-West England; this filename is not proof of a unique Cornwall release.
- `history/states/133-Strathclyde.txt` — displayed Lanark.
- `history/states/136-Aberdeenshire.txt`.
- `history/states/933-Shetland.txt`.

No Chaos Redux override was found for these target state histories, and the mod does not use a `replace_path` that substitutes them.

### 12.4 Starting technology, slots, convoys, and OOB evidence

| Tag | 1936 history evidence | OOB consequence |
|---|---|---|
| `SCO` | `infantry_weapons`, `tech_trucks`, 20 convoys; later dated history adds electronics/industry/fuel technology | No `set_oob`; Event 006 must materialize forces |
| `WLS` | `infantry_weapons`, `tech_trucks`, `fuel_silos`, 20 convoys; later dated history adds electronics/industry technology | No `set_oob`; Event 006 must materialize forces |
| `BRI` | 3 slots, 20 convoys, infantry/support/motorization/artillery/AA, fuel/train, aircraft, armor, naval hull/weapons, transport technology, with later dated additions | No `set_oob`; Event 006 must materialize forces |
| `RHI` | 3 slots, 50 convoys, German-regional infantry/support/motorization/artillery/AA/fuel/air/armor/transport technology, with later dated industry/electronics additions | No `set_oob`; Event 006 must materialize forces |
| `BAY` | Same broad German-regional technology/slots/convoys structure as `RHI` | No `set_oob`; Event 006 must materialize forces |
| `ICE` | 2 slots, 30 convoys; infantry/support/recon, early air/naval/transport and DLC-conditioned technology | `set_oob = ICE_1936`; `history/units/ICE_1936.txt` defines Ríkislögreglan and production lines but fields no starting division |
| `ACX/AEX/AFX/AGX/AJX` | No dormant-history technology, slots, or convoys | No OOB; Event 006 host inheritance and dynamic forces are mandatory |

Do not duplicate these lists in package adapters. `independence_wave_inherit_opening_technology_and_slots` already uses `inherit_technology = event_target:independence_wave_setup_former_host`, then enforces Event 006 minimum slot/reinforcement pathways. Package adapters only need to ensure the force preconditions and special country-preservation rules are correct.

### 12.5 Exact localisation and flag sources

- Vanilla country identities: `localisation/english/countries_l_english.yml`.
- Vanilla parties: `localisation/english/parties_l_english.yml`; exact complete package-specific party sets exist for `BRI_*_party` and `ICE_*_party`, while `SCO`, `WLS`, `RHI`, and `BAY` have no equivalent tag-specific set there.
- State display names: `localisation/english/state_names_l_english.yml`.
- Iceland national focus/localised content: primarily `localisation/english/aat_focus_l_english.yml`, `aat_events_l_english.yml`, `aat_decisions_l_english.yml`, and `aat_ideas_l_english.yml`, with shared/base entries elsewhere.

Flag files under vanilla `gfx/flags/`, `gfx/flags/medium/`, and `gfx/flags/small/`:

- `SCO`, `WLS`, `RHI`, and `BAY`: `_democratic`, `_communism`, `_fascism`, and `_neutrality` variants; no unsuffixed base flag.
- `BRI` and `ICE`: unsuffixed base flag plus `_communism`, `_fascism`, and `_neutrality`; the base file supplies the democratic display.
- `ACX`, `AFX`, `AGX`, and `AJX`: the later live-flag repair supplies complete Chaos Redux historical flag triplets. AEX is deliberately absent because Flanders remains the vanilla `BEL_flanders` cosmetic overlay.

### 12.6 Exact cosmetic and cross-content references

- Iceland history uses `set_cosmetic_tag = ICE_personal_union` on the relevant vanilla path; package logic must not clear it generically.
- `common/decisions/WLS.txt` owns `WLS_restore_y_wladfa_decision`.
- `common/decisions/formable_nation_decisions.txt` owns `form_nordic_league` and `declare_germany_reunified_decision` plus their associated formable category logic.
- `common/decisions/categories/00_formable_categories.txt` owns `form_nordic_league_category` visibility/category behavior.
- `common/national_focus/germany.txt` owns `GER_fan_prussian_militarism`; its effects interact with `BAY_rupprecht_of_bavaria` when Bavaria is absent.
- The Event 006 new-tag collision audit dated 2026-07-14 found no tag or cosmetic-key collision for `ACX`, `AEX`, `AFX`, `AGX`, or `AJX` in the then-current registries.
- The only unrelated Chaos Redux use of scoped tag `ICE` found in this pass is an Event 001 Nordic communist rebel-name pool reference; it is not a package definition but should remain untouched.

## 13. Simplifications, omissions, and completion status

This handoff does not implement gameplay, assets, localisation, or readiness flags. It makes no completion claim for the package tranche. No fallback geography, replacement tree, invented leader, placeholder flag, generic OOB, or unconditional content-ready flag is proposed.

The implementation path is complete enough to begin bounded coding for `SCO`, `WLS`, `BRI`, `AFX`, `AGX`, `RHI`, `BAY`, `AJX`, and the preserved-tree `ICE` adapter. `ACX` and `AEX` remain intentionally blocked for the reasons above.

Skills used for this exploration: `chaos-redux-subagents`, `chaos-redux-events`, and `hoi4-focus-trees`. No skill was created or modified.
