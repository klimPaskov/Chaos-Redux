# Event 039 Opening Host and Succession Safety Audit: ENG

Disposition: `blocked` for engine-verified host approval. Local source review identifies ENG as the bounded historical candidate `ENG_stanley_baldwin` to `ENG_neville_chamberlain`, but the connected HOI4 event, focus, map, reference, and probability routes were unavailable, and the installed history source contains a contradictory 1936 comment that prevents me from certifying the live ruling character from source alone.

Acceptance basis: the user explicitly directed this audit to treat Part 3 and Part 18 as accepted design. This handoff treats their opening-leader gate and verified-succession requirement as binding.

Scope: read-only review of Event 039 opening host eligibility, ENG 1936 leader and successor sources, the relevant vanilla UK focus and event dependencies, the Event 039 emergency portrait record, and exact Chaos Redux ownership references. No gameplay, localisation, workbook, asset, staging, commit, map write, or HOI4 launch was performed.

## Finding

The only country examined was vanilla ENG, with country tag `ENG`, history file `ENG - Britain.txt`, vanilla country mapping `countries/United Kingdom.txt`, and player-facing country name `Britain`. The exact static identities are `ENG_stanley_baldwin` and `ENG_neville_chamberlain`; no alternate country or roster was proposed.

The source files support a grounded succession route: both characters have the `liberalism` country-leader ideology, Chamberlain has a native vanilla portrait, and the 1939 history block explicitly recruits and promotes Chamberlain before retiring Baldwin. This is a history-date precedent, not evidence of a 1936 runtime succession event.

The 1936 current-ruler claim remains unresolved. The ENG history sets `ruling_party = democratic`, recruits Baldwin in the initial character sequence, and sets democratic popularity to 97 percent. The same block contains the comment “here Chamberlain becomes starting leader,” even though Chamberlain is not recruited in that root sequence and appears in the dated 1939 block. `ENG_stanley_baldwin` is also defined with `expire = "1938.1.1.1"`. A live country roster inspection is required to establish the actual active leader for the selected date and route.

Event 039 currently does not implement the static ENG row. Host eligibility admits a major or human-controlled country with a country leader, then the opening package selects a random character satisfying `is_country_leader = yes` without a ruling-leader test or a country-specific succession disposition. Its democratic successor branch creates the shared name `The Emergency Successor` with `GFX_portrait_039_emergency_constitutional_successor`, then retires the selected character. This remains incompatible with the accepted grounded-country and pre-prepared-successor gates.

Therefore ENG is a source-supported candidate for parent follow-up, not a currently verified pass. The accepted candidate row is `ENG_stanley_baldwin` → `ENG_neville_chamberlain`, gated to a live ruling Baldwin and an uncommitted baseline route. ENG should fail closed when another leader or a committed political route is active unless that route has its own verified successor row.

## Country package coverage checklist

| Surface | Finding | Evidence or limit |
| --- | --- | --- |
| Tag and country aliases | `ENG` is an existing vanilla tag, mapped to `countries/United Kingdom.txt`; vanilla English localisation displays `Britain`. Event 039 does not add an ENG alias or country package. | Vanilla `common/country_tags/00_countries.txt`; `localisation/english/countries_l_english.yml`; history `ENG - Britain.txt`. |
| Opening eligibility | The trigger accepts a major or a human-controlled country and requires a country-leader character, but does not require the current ruling leader to be the registered opening target. | `common/scripted_triggers/039_murder_mystery_integration_triggers.txt:12-35`. |
| Politics and party | The vanilla history sets democratic government and 97 percent democratic popularity. Baldwin and Chamberlain both have `liberalism` leader roles. Actual ruling-leader state remains unresolved because of the history-order/comment conflict and missing live inspection. | `ENG - Britain.txt:592-604,628-633,354-356`; `ENG.txt:79-92,184-198`. |
| Leader disposition and succession | Event 039 marks whichever random country leader it captured as `eligible_opening_leader`; it does not use an ENG-specific disposition or a pre-prepared static successor. | `common/scripted_effects/039_murder_mystery_integration_effects.txt:318-535`. |
| Portrait and identity | ENG has native Baldwin and Chamberlain portrait sprites and DDS files. The current Event 039 portrait is a generated fictional individual used by the generic successor effect across host countries. | Vanilla `interface/_leader_portraits.gfx:3819-3835`; `interface/039_murder_mystery_portraits.gfx:10-13`; portrait manifest cited below. |
| Focus route | Vanilla focus `ENG_motion_of_no_confidence` requires ruling Chamberlain and bypasses for Churchill, Lord Edward Halifax, or unavailable Churchill. Promoting Chamberlain preserves that focus gate; killing or replacing another committed route leader needs separate route-aware handling. | `common/national_focus/uk.txt:9608-9637`. No direct Baldwin token reference was found in the focused ENG focus search. |
| Vanilla event succession | The 1939 history block performs `recruit_character = ENG_neville_chamberlain`, `promote_character = ENG_neville_chamberlain`, then `retire_character = ENG_stanley_baldwin`. Later `britain.9` transfers Chamberlain to Churchill under wartime conditions. No 1936 Baldwin-to-Chamberlain runtime event was found in the exact-token search of vanilla events, focuses, on-actions, scripted effects, and decisions. | `ENG - Britain.txt:354-356`; `events/Britain.txt:249-278`; exact-token search result. |
| Chaos ownership | No Chaos Redux gameplay source directly references either static ENG character token. A later ENG Easter Egg creates a separate “Chamberlain The Immortal” leader and can replace the country leader; it does not use `ENG_neville_chamberlain` or coordinate with the Event 039 registry. This is a future leader-slot interaction, not a direct owner claim on the static token. | `events/_chaosx_easter_eggs.txt:3-45`; `interface/chaosx_characters.gfx:1-6`; `common/country_leader/chaosx_leader_traits.txt:3-...`. |
| State and map setup | Opening eligibility checks controlled-state counts and the package sets a coarse host-state-viable flag. This review did not inspect exact state connectivity, capital retention, split candidates, supply, or rail data. | `common/scripted_triggers/039_murder_mystery_integration_triggers.txt:12-35`; `common/scripted_effects/039_murder_mystery_integration_effects.txt:318-535`; map MCP route unavailable. |
| Flags, advisors, decisions, ideas | No ENG flag, advisor, or party-name edit was found in the opening transaction. Broader decision, idea, and asset coverage was outside this bounded audit. | No source changes; no package-wide completeness claim. |
| Military, technology, industry, supply, production | Outside this opening-leader audit; no related setup changes were made or validated. | No country-package readiness claim. |
| AI and host playability | ENG qualifies by its vanilla major status and would also satisfy the player branch when human-controlled. The host pool is shared and weighted; the source does not guarantee ENG or a player host. No normalized probability is claimed. | Event source plus the Part 13 scenario contract; probability MCP route unavailable, and the specialist returned no scenario evidence before shutdown. |

## File surface checklist

| File | Identifiers or line spans | Audit result |
| --- | --- | --- |
| `common/scripted_triggers/039_murder_mystery_integration_triggers.txt` | `murder_mystery_prefire_host_is_valid`, lines 12-35 | Coarse host gate accepts a major or player and any country leader; no ruling-leader or succession row check. |
| `common/scripted_effects/039_murder_mystery_integration_effects.txt` | `murder_mystery_select_weighted_prefire_host`, lines 19-43; `murder_mystery_prepare_opening_package` and `murder_mystery_install_verified_successor`, lines 318-470; opening commit, lines 472-535 | Shared weighted pool, random character capture, generic emergency successor, and opening transaction reviewed. Current parent diff does not overlap these lines. |
| `common/scripted_effects/individual_crisis_targeting_effects.txt` and `common/script_constants/individual_crisis_targeting_constants.txt` | `adjust_individual_crisis_candidate_ticket_weight`, lines 9-70; ticket constants, lines 8-22 | Load dependent ticket curve found; numeric campaign probability unresolved. |
| Vanilla `common/characters/ENG.txt` | `ENG_stanley_baldwin`, lines 79-92; `ENG_neville_chamberlain`, lines 184-198 | Static identities, leader ideologies, traits, expiry dates, and portrait keys reviewed. |
| Vanilla `history/countries/ENG - Britain.txt` | politics and party popularity, lines 592-604; initial recruitment and conflicting comment, lines 628-633; 1939 succession, lines 354-356 | Baldwin is recruited in the root sequence; Chamberlain is recruited and promoted in the 1939 dated block. The 1936 live ruler remains unresolved. |
| Vanilla `common/national_focus/uk.txt` | `ENG_motion_of_no_confidence`, lines 9608-9637 | Chamberlain gate and Churchill/Halifax bypass reviewed. |
| Vanilla `events/Britain.txt` | Chamberlain wartime succession, lines 249-278; death branch, lines 282-324 | Later Chamberlain-to-Churchill handling reviewed; no 1936 Baldwin-to-Chamberlain runtime event found in the focused search. |
| Vanilla `interface/_leader_portraits.gfx` and portrait DDS files | Baldwin sprite lines 3819-3821; Chamberlain sprite lines 3834-3836 | Native sprite and texture paths exist. |
| `interface/039_murder_mystery_portraits.gfx`, `localisation/english/039_murder_mystery_l_english.yml`, and `docs/assets/039_murder_mystery/portraits/manifest.md` | `GFX_portrait_039_emergency_constitutional_successor`, loc keys 159-160, manifest rows 7, 23-25, 40, 48, 67 | Generic female fictional portrait source and runtime wiring documented; source mode is invalid for a grounded ENG successor. |
| `events/_chaosx_easter_eggs.txt` and `common/country_leader/chaosx_leader_traits.txt` | `chaosx.easter_egg.1`, lines 3-45; `chamberlain_the_immortal`, lines 3-13 | Future ENG leader-slot interaction identified; no direct static Baldwin or Chamberlain token ownership. |
| Part 3, Part 13, and Part 18 accepted specs | Part 3 lines 31-65 and 183-185; Part 13 lines 9-18, 25-45, 265-280; Part 18 lines 11-19, 82, 89, 195, 270 | Opening succession, weighted audit, named scenario, and hard-blocker requirements applied. |

## Missing or stale surfaces

- Event 039 has no ENG-specific `eligible_opening_leader` row that binds the current ruling token to a named successor.
- The opening selector does not verify Baldwin as the active ruler, the ENG route state, the successor's recruitment and ownership, or that the successor is not active elsewhere.
- The current successor uses a generated individual portrait and shared office label in a grounded polity; the static Chamberlain token and native portrait are not used.
- No live evidence confirms whether ENG begins with Baldwin as the ruling leader in the selected start context, whether Chamberlain is available to recruit at the event date, or whether the opening transaction preserves all committed UK focus and event routes.
- No map inspection established the host capital, split-state candidates, connectivity, supply, or capital retention. The opening count checks alone do not establish those later Part 18 cases.

## Portrait and identity evidence

`docs/assets/039_murder_mystery/portraits/manifest.md:7,23-25,40,48,67` records the emergency successor as the fictional female individual Mara Vey, produced through the native ImageGen branch owned by `chaosx_portrait_creator`. The manifest gives prompt and source dimensions, SHA-256, processed PNG and runtime DDS, and states that the concurrent Event 039 character file has no matching static token. It reports visual review as PASS and parent review as pending; I read the evidence record but did not independently inspect the image pixels.

The effect instead displays the localisation key `MURDER_MYSTERY_EMERGENCY_SUCCESSOR_NAME` as “The Emergency Successor,” and the dynamic `create_country_leader` block does not set a gender field. The event asset is a completed fictional portrait, not an unchanged grounded source placeholder or an authentic ENG institution portrait. Applying it to Baldwin’s grounded UK succession fails Part 3 and the portrait source-mode gate. No portrait was generated or edited during this audit, and RunPod was not used.

The vanilla successor assets are available at `GFX_portrait_ENG_neville_chamberlain` → `gfx/leaders/ENG/Portrait_Britain_Neville_Chamberlain.dds` and `GFX_portrait_ENG_stanley_baldwin` → `gfx/leaders/ENG/Portrait_Britain_Stanley_Baldwin.dds`. Both source files exist in the installed game. They are appropriate static references for the bounded ENG route; this audit does not authorize new portrait production.

The Event 039 runtime GFX points to `gfx/leaders/039_murder_mystery/leader_039_emergency_constitutional_successor.dds`. A focused runtime-source search found no references from `common`, `interface`, or `events` into the portrait source workspace under `docs/assets/039_murder_mystery/portraits/`.

## Weighted host selection

Event 039 sets `individual_crisis_candidate_base_weight = 1`, calls `adjust_individual_crisis_candidate_ticket_weight`, repeats the country scope in a temporary array by the resulting integer ticket count, then selects one scope with `random_scope_in_array`. The shared helper returns 4 tickets at active load 0, 2 tickets when active load is below 2, and 1 ticket at load 2 or more, provided the individual-crisis load cap still passes; otherwise it returns 0. These are source facts, not ENG selection odds.

The complete candidate pool, each eligible country's active load, external factors, normalized ENG share, and the Part 13 "Stable major with strong agency" scenario result remain unresolved. The mandatory audit was routed to `chaosx_ai_probability_auditor`, but the agent stayed running after the interrupt request and was shut down without returning a probability result. No numeric claim is supported without the live `hoi4.probability_inspect` workflow.

The reviewed vanilla focus `ENG_motion_of_no_confidence` also has `ai_will_do = { factor = 1 }`. This focus score was included in the auditor's interrupt request, but no focus selection result was returned. No focus selection probability claim is made without a complete available-focus pool and route inputs.

## MCP and source-reference evidence

The connected tool inventory exposed no `mcp__hoi4_agent_tools__hoi4_*` routes and no callable HOI4 reference, event, focus, map, or probability tools. It exposed unrelated `mcp__blender_hoi4__chaosx_blender_hoi4_*` tools only.

The initial combined resource discovery failed. Separate retries of `list_mcp_resource_templates({server: "hoi4_agent_tools"})` and `list_mcp_resources({server: "hoi4_agent_tools"})` also failed with `MCP startup failed: timed out handshaking with MCP server after 119.9999999s`. No connected server version, health, live schemas, or client task negotiation was available.

The mandatory `hoi4.event_inspect`, `hoi4.event_render`, `hoi4.event_compare`, focus inspect/render/lint, map inspect/render, `hoi4.reference_context`, `hoi4.reference_search`, `hoi4.reference_read`, `hoi4.source_lookup`, and probability routes therefore could not be called. Local file review below is fallback evidence only, not engine or MCP validation. Technology is not a dependency in this bounded audit; standalone Technology Tree Viewer availability was not assessed.

Local fallback references read: offline `Character modding`, `Effects`, and `Triggers` wiki sections, plus installed `effects_documentation.md` and `triggers_documentation.md`. The installed effects documentation describes `recruit_character` as a COUNTRY-scope attach effect and `promote_character` as promotion to the head of the political party; the wiki describes character recruitment and succession semantics. Those references support the source interpretation but do not prove live ENG roster state or runtime execution.

The read fallback spans were `Character modding - Hearts of Iron 4 Wiki.md:48-50,417-503`, `Effects - Hearts of Iron 4 Wiki.md:137,2736,2930,3252`, `Triggers - Hearts of Iron 4 Wiki.md:1757-1763,2033-2036`, installed `effects_documentation.md:3010-3029,5149-5170,5343-5348,5696-5705,6436-6453`, and installed `triggers_documentation.md:3640-3652,5408-5414`. MCP reference paths and live revisions were unavailable.

## Parent follow-up

1. Keep the candidate set explicit: `ENG_stanley_baldwin` as the only opening target for the 1936 baseline row and `ENG_neville_chamberlain` as its grounded same-ideology successor.
2. Require a live ruling-character check and a route-state check before registering the row. Reject ENG when its actual leader or committed route is not covered by this row.
3. Prepare Chamberlain before retiring Baldwin, using the native token and vanilla 1939 sequence as the source precedent. Require proof the successor is recruited, available to ENG, the ruling leader after promotion, and not simultaneously active elsewhere; use the vanilla portraits and preserve the leader’s identity.
4. Coordinate the later Chaos Easter Egg leader-slot transaction with the Event 039 character registry if the ENG branch can overlap. Do not substitute a new country or generic invented successor for this bounded candidate.
5. When the HOI4 service is available, run the narrow Event 039 inspect/render/compare, the relevant focus inspect/render/lint, and the probability audit for the complete host pool and the ENG focus surface using named scenarios. Keep any missing route or unresolved live-state input visible.

## Validation and limitations

Completed: local source review of the specified Event 039 effect and trigger spans; exact vanilla ENG character, history, focus, event, and portrait-path checks; repository exact-token search for Chaos ownership; local wiki and installed-documentation fallback; and source-path existence checks for the cited portraits.

Skipped: all mandatory HOI4 MCP event, focus, map, reference, and probability inspections/renders/comparisons because their routes were not exposed and the server resource handshake timed out on the separate retries. No live roster UUID, current country alias payload, scenario hash, or engine artifact URI was returned. No in-game launch or testing was performed.

No gameplay before/after behavior changed. No candidate is certified as passing every opening gate until the ruling character, current route, successor transaction, and complete weighted pool have live evidence.

## Source snapshot

Repository HEAD at audit snapshot: `2cfa6c01e5ce85d83672415b08910f7bae003a2b`. The shared working tree has an existing parent-owned modification in `common/scripted_effects/039_murder_mystery_integration_effects.txt`. I rechecked the current diff and confirmed that it changes later target-selection, safe-target, and cleanup functions, not opening lines 318-535. This audit did not modify or stage that file.

Key SHA-256 fingerprints at audit snapshot:

| Source | SHA-256 |
| --- | --- |
| `common/scripted_effects/039_murder_mystery_integration_effects.txt` working copy at final recheck | `D48AEEC6EE032F110B6588E5CAA20AEAAED57EC9A482068330B566C303D11254` |
| `common/scripted_triggers/039_murder_mystery_integration_triggers.txt` | `16F2972DD0085000611BBFC5530458F6C7AE80BAE6BD80B4409860765861C2B7` |
| `common/characters/ENG.txt` installed vanilla | `01DE51F84D9C584A25A178ECF0CF4E6FBB423F3D85E28AEB4D2F7506FED38680` |
| `history/countries/ENG - Britain.txt` installed vanilla | `5D8A15AE229D98AB7DA18C85A3E1CED673D8B1A29AF0644B8125B76E2570AA49` |
| `common/national_focus/uk.txt` installed vanilla | `053A43E77EB5152ABAF638CC72EA019B44301397F50C16C9D75D77F42A668F77` |
| `events/Britain.txt` installed vanilla | `83741F44F61F18C1BB2731612042878866093E8BA8E701C8EF0AB7A769494F28` |
| `interface/_leader_portraits.gfx` installed vanilla | `38154EB1B7EBB6CFFFAD0F4A8E457C4291006BA015AD04FF060CC1CBE1A92A22` |
| `interface/039_murder_mystery_portraits.gfx` | `8FAB9491A0CAD9A0D743751784029D664FFC874ACA6905B8AA029CDCF6A600E7` |
| `localisation/english/039_murder_mystery_l_english.yml` | `8814F80B2646D5D202AFA98F85AB5C768EC700DB445DEC6D093457BB1D9C2CAD` |
| `docs/assets/039_murder_mystery/portraits/manifest.md` | `F0D66DEE605FF9E25B83AE77440778E2F5AB464FCE8F0B7E2966BF7854E0B0C4` |
| `events/_chaosx_easter_eggs.txt` | `7A3B21384CF82BBDAAD1A1C52386A9733214CB18A0697DE1EC82A21F8DFC5627` |
| `docs/specs/039_murder_mystery_specs/039_murder_mystery_spec_part_3_character_safety.md` | `509B1F07EE03EF995DA804E42E272899A0FCA43CC8D704E54F844BAB790E862B` |
| `docs/specs/039_murder_mystery_specs/039_murder_mystery_spec_part_18_acceptance.md` | `916C0B169F69EF10A081E3FDE0704A8AC7DC1E7D319310298A79533A556E3428` |
| `docs/specs/039_murder_mystery_specs/039_murder_mystery_spec_part_13_ai_probability.md` | `145EABCF4FF40D4643B97E1D4CBD309613D03548510A46F4513F181A59AD7A09` |
| `common/scripted_effects/individual_crisis_targeting_effects.txt` | `903562C1DC27BF9367E5A8AB8A807047A798FB16DE0BD8E1DF2841B6A2C40B16` |
| `common/script_constants/individual_crisis_targeting_constants.txt` | `8B4471A8412E3A883570743E0EE17037129DCEAA889D63781AC8FC2C3529E002` |

The offline wiki fingerprints are `Character modding - Hearts of Iron 4 Wiki.md` `8EF3D5F9923026DD81F239944710B7331A8D06AD42E4345B32FCE4E86DD95D98`, `Effects - Hearts of Iron 4 Wiki.md` `997DDB09BFD63EFB41A425149C46BD812D5F8953217A403386B2F6C85196AA0C`, and `Triggers - Hearts of Iron 4 Wiki.md` `ABC51AD18A2C46E46D47BAA795C5A840EBAF7C4AE3E777426C64A9F4C0C0CE06`. The installed documentation fingerprints are `effects_documentation.md` `2CDC93D26775990468EED167442F7A416B13059FB8FE07D139B54250B79209AF` and `triggers_documentation.md` `7D27ED77DADAF3A213A4B3E2C624BF9C02DAE495317ABE8EEE833B27C2D1DE29`. These hashes identify the local reference bytes only; no live source revision was returned.

Changed files by this sidecar: only `docs/plans/039_murder_mystery_plans/subagent_handoffs/opening_eng_succession_safety_2026_10_03.md`. No tags, state ids, leaders, parties, focus ids, localisation keys, formables, flags, gameplay, assets, or source files were changed. No files were staged or committed.
