# Event 012 Africa Country Package Surface Audit Handoff

Date: 2026-06-17
Agent role: country package subagent

## Scope

Audited Event 012 Africa country-package surfaces for the countries and identities created, transformed, sponsored, or restored by the Africa event chain.

Primary tags audited:

- Regional authority actors: `WAC`, `SAH`, `MAG`, `NHR`, `EAC`, `GLK`, `CBC`, `ZSC`, `SLC`, `IOC`
- High-chaos actors: `GHP`, `BBS`, `TDM`, `ANW`, `OVN`, `CRR`, `CTL`, `OKP`, `TRM`, `HGD`, `GHC`
- Africa cosmetic identities: `AFR`, `AFR_FEDERAL_CHARTER`, `AFR_SOVEREIGN_SEATS`, `AFR_PEOPLES_LIBERATION`, `AFR_CONTINENTAL_COMMAND`, `AFR_CROWN_CONGRESS`, `AFR_PAN_ATLANTIC`, `AFR_ARCHIVE_MANDATE`, `AFR_WORLD_ROOT`, `AFR_AFRICAN_MIDDLE_EASTERN_UNION`, `AFR_AFRO_ASIAN_UNION`, `AFR_AFRO_EURASIAN_UNION`, `AFR_AFRO_ATLANTIC_UNION`, `AFR_CONGRESS_OF_CONTINENTS`

Rules and references applied:

- `AGENTS.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`
- `.agents/skills/chaos-redux-events/SKILL.md`
- `.agents/skills/hoi4-focus-trees/SKILL.md`
- `.agents/skills/chaos-redux-event-assets/SKILL.md`
- Offline Paradox wiki pages for data structures, triggers, effects, modifiers, localisation, scopes, on actions, event modding, decision modding, idea modding, AI modding, country creation, state modding, national focus modding, ideology modding, unit/division/technology modding, portrait modding, graphical assets, and cosmetic tags
- Vanilla documentation and examples in `~/projects/Hearts of Iron IV/documentation/` and vanilla country/history/state/interface files

No web access was used.

## Country Package Coverage Checklist

- Tag registration: complete for all 21 created actors in `common/country_tags/chaosx_countries.txt`.
- Country definition files: complete for all 21 actors under `common/countries/`.
- Country history files: complete for all 21 actors under `history/countries/`.
- Static capitals: all 21 history capitals resolve to valid state IDs when both mod and vanilla `history/states/` are considered.
- State package handling: Event 012 transfer/setup code references all 21 actors and calls the matching regional or high-chaos setup effects from `common/scripted_effects/012_africa_effects.txt`.
- Politics and popularities: all 21 actors have `set_politics`, `set_popularities`, and leader setup in country history.
- Country localisation: all 21 actors have base, `DEF`, `ADJ`, ideology-name, ideology `DEF`, ideology `ADJ`, ideology party, and ideology party-long keys in `localisation/english/chaosx_countries_l_english.yml`.
- Cosmetic localisation: audited Africa base, route, and dynamic union cosmetic identities have base and ideology-name variants in `localisation/english/chaosx_countries_l_english.yml`.
- Portraits: high-chaos leader sprites resolve through `interface/012_africa.gfx` and `interface/chaosx_characters.gfx`; regional authority generic African portrait sprite names resolve through vanilla `_scientists_portraits.gfx` and copied generic portrait textures in the mod.
- Flags: all 21 created actor tags have base and ideology flag families in `gfx/flags/`, `gfx/flags/medium/`, and `gfx/flags/small/`.
- Land OOBs: all 21 created actors load `TAG_1936` land OOBs from `history/units/`.
- Naval OOBs: present for `WAC`, `MAG`, `EAC`, `CBC`, `IOC`, `TDM`, `ANW`, `OVN`, and `CRR`, matching coastal/port actor coverage.
- Air OOBs: present for `MAG`, `NHR`, `SLC`, `IOC`, and `OVN`, matching prior country-package reinforcement coverage.
- Focus loading: `africa_setup_regional_authority_subject` loads `africa_regional_authority_focus_tree`; `africa_setup_high_chaos_actor` loads `africa_high_chaos_actor_focus_tree`; both set the focus-tree guard flags used by `common/national_focus/012_africa_authority_focus.txt`.
- AI strategy linkage: every created actor has a tag-specific AI strategy block in `common/ai_strategy/012_africa.txt`, layered under the regional or high-chaos role strategy families.

## File Surface Checklist

Audited country-package files and surfaces:

- `common/country_tags/chaosx_countries.txt`
- `common/countries/West African Congress.txt`
- `common/countries/Sahel Caravan.txt`
- `common/countries/Maghreb Coast.txt`
- `common/countries/Nile-Horn League.txt`
- `common/countries/East African Railway Congress.txt`
- `common/countries/Great Lakes Council.txt`
- `common/countries/Congo Basin Charter.txt`
- `common/countries/Zambezi-Stone Cities.txt`
- `common/countries/South African Liberation Congress.txt`
- `common/countries/Indian Ocean Congress.txt`
- `common/countries/Gorilla Highlands.txt`
- `common/countries/Baobab Senate.txt`
- `common/countries/Tidemark Dominion.txt`
- `common/countries/Ananse Web.txt`
- `common/countries/Orisha Vodun Nature Courts.txt`
- `common/countries/Crocodile Rivers.txt`
- `common/countries/Chimpanzee Telegraph League.txt`
- `common/countries/Okapi Court.txt`
- `common/countries/Termite Citadel Engineers.txt`
- `common/countries/Honeyguide Commons.txt`
- `common/countries/Great Herds.txt`
- `common/countries/cosmetic.txt`
- Matching `history/countries/<TAG> - <country>.txt` files for all 21 actors
- Matching `history/units/TAG_1936.txt` files for all 21 actors
- Matching naval OOB files for `WAC`, `MAG`, `EAC`, `CBC`, `IOC`, `TDM`, `ANW`, `OVN`, and `CRR`
- Matching air OOB files for `MAG`, `NHR`, `SLC`, `IOC`, and `OVN`
- `common/scripted_effects/012_africa_effects.txt`
- `common/national_focus/012_africa_authority_focus.txt`
- `common/ai_strategy/012_africa.txt`
- `localisation/english/chaosx_countries_l_english.yml`
- `interface/012_africa.gfx`
- `interface/chaosx_characters.gfx`
- `docs/assets/012_africa/generated_flags/manifest.md`
- `docs/assets/012_africa/implementation_asset_manifest.md`

## Patches Made

No gameplay, localisation, country-history, focus, AI, or asset patch was made.

Reason: the audit did not find a narrow safe issue in the requested writable surfaces. The remaining blocker is an asset package gap for Africa cosmetic flags, and creating or copying cosmetic flag families would exceed the requested narrow country-package patch scope.

Changed files:

- `docs/plans/012_africa_plans/subagent_handoffs/2026-06-17_012_africa_country_package_surface_audit_handoff.md`

Changed tags, state IDs, leaders, parties, focus tree IDs, localisation keys, or formable IDs:

- None.

Before and after behavior:

- Before: Event 012 country-package surfaces had no current audit handoff tying together created-country setup, focus loading, AI, portraits, flags, and remaining cosmetic flag risks.
- After: the audit state and remaining blocker are documented for parent review. Runtime behavior is unchanged.

## Missing Or Stale Country Package Surfaces

### Cosmetic flag families are incomplete

Affected identities:

- `AFR`
- `AFR_FEDERAL_CHARTER`
- `AFR_SOVEREIGN_SEATS`
- `AFR_PEOPLES_LIBERATION`
- `AFR_CONTINENTAL_COMMAND`
- `AFR_CROWN_CONGRESS`
- `AFR_PAN_ATLANTIC`
- `AFR_ARCHIVE_MANDATE`
- `AFR_WORLD_ROOT`
- `AFR_AFRICAN_MIDDLE_EASTERN_UNION`
- `AFR_AFRO_ASIAN_UNION`
- `AFR_AFRO_EURASIAN_UNION`
- `AFR_AFRO_ATLANTIC_UNION`
- `AFR_CONGRESS_OF_CONTINENTS`

Concrete missing flag stems:

- In `gfx/flags/`, `gfx/flags/medium/`, and `gfx/flags/small/`, `AFR` is missing ideology variants: `AFR_communism`, `AFR_democratic`, `AFR_fascism`, `AFR_neutrality`.
- In `gfx/flags/`, `gfx/flags/medium/`, and `gfx/flags/small/`, these route cosmetics are missing base and ideology variants: `AFR_FEDERAL_CHARTER`, `AFR_SOVEREIGN_SEATS`, `AFR_PEOPLES_LIBERATION`, `AFR_CONTINENTAL_COMMAND`, `AFR_CROWN_CONGRESS`, `AFR_PAN_ATLANTIC`, `AFR_ARCHIVE_MANDATE`, `AFR_WORLD_ROOT`.
- In `gfx/flags/`, `gfx/flags/medium/`, and `gfx/flags/small/`, these dynamic union cosmetics have base flags but are missing ideology variants: `AFR_AFRICAN_MIDDLE_EASTERN_UNION`, `AFR_AFRO_ASIAN_UNION`, `AFR_AFRO_EURASIAN_UNION`, `AFR_AFRO_ATLANTIC_UNION`, `AFR_CONGRESS_OF_CONTINENTS`.

Why this matters:

- The offline cosmetic tag wiki notes that ideology-specific base-country flags can override a cosmetic tag fallback unless the cosmetic identity also has ideology-specific flag files.
- Event 012 applies these cosmetic tags to existing African unifier countries, so ideology flag fallback behavior can make the visible flag remain the underlying country ideology flag instead of the Africa route or dynamic union flag.

Relevant references:

- `common/countries/cosmetic.txt`
- `common/scripted_effects/012_africa_effects.txt` (`AFR_AFRICAN_MIDDLE_EASTERN_UNION`, `AFR_AFRO_ASIAN_UNION`, `AFR_AFRO_EURASIAN_UNION`, `AFR_AFRO_ATLANTIC_UNION`, `AFR_CONGRESS_OF_CONTINENTS`)
- `localisation/english/chaosx_countries_l_english.yml`
- `docs/assets/012_africa/generated_flags/manifest.md`
- `docs/assets/012_africa/implementation_asset_manifest.md`
- `gfx/flags/`, `gfx/flags/medium/`, `gfx/flags/small/`

Suggested follow-up:

- Asset pass should provide base plus ideology flag files in all three flag sizes for every Africa cosmetic identity above.
- If one visual should be shared across ideologies, copy the same final flag to the ideology-specific filenames rather than relying on fallback behavior.

## Map And State Setup Issues

No narrow state setup defect was found in this audit.

Validated capitals:

- `WAC`: capital `558`
- `SAH`: capital `556`
- `MAG`: capital `459`
- `NHR`: capital `271`
- `EAC`: capital `546`
- `GLK`: capital `548`
- `CBC`: capital `295`
- `ZSC`: capital `771`
- `SLC`: capital `275`
- `IOC`: capital `543`
- `GHP`: capital `768`
- `BBS`: capital `778`
- `TDM`: capital `905`
- `ANW`: capital `779`
- `OVN`: capital `773`
- `CRR`: capital `772`
- `CTL`: capital `718`
- `OKP`: capital `890`
- `TRM`: capital `889`
- `HGD`: capital `903`
- `GHC`: capital `904`

Remaining uncertainty:

- This audit checked static package and scripted references, not live in-game post-transfer ownership/controller outcomes for every event branch.

## Politics, Leader, Portrait, Flag, Advisor, And Party Issues

No narrow politics, party, leader, portrait, or advisor setup defect was found for the 21 created actors.

Notes:

- High-chaos leaders use institutional names and symbolic-body portraits, which fits the project rule for council, committee, symbolic-body, and non-personal leaders.
- Regional authority leaders use institutional names with generic African portraits; no personal random-name gender pool issue was found.
- Party localisation exists for all four ideologies per created actor, using ideology-scoped keys like `WAC_democratic_party` and `WAC_democratic_party_long`.
- Advisor and command staff package references for the 21 actors are present in `common/scripted_effects/012_africa_effects.txt`; the audit did not identify missing character or portrait references inside the current country-package scope.
- The unresolved issue in this category is the Africa cosmetic flag family gap described above.

## Focus, Decision, Idea, And Asset Issues

Focus loading:

- `africa_setup_regional_authority_subject` sets `africa_regional_authority_subject`, adds `africa_regional_authority_spirit`, and loads `africa_regional_authority_focus_tree`.
- `africa_setup_high_chaos_actor` sets `africa_high_chaos_actor`, adds `africa_high_chaos_actor_spirit`, and loads `africa_high_chaos_actor_focus_tree`.
- `common/national_focus/012_africa_authority_focus.txt` allows those two trees through the same guard flags.
- No missing event-created focus loading guard was patched. The created actor tags are Event 012 custom tags and the setup effects are idempotent behind package flags.

Decisions:

- Decision and mission files were intentionally out of scope per the task.

Ideas:

- Starting/package ideas referenced by setup effects are present at the country-package level. No missing idea hook was found in the audited surfaces.

Assets:

- High-chaos portrait sprite definitions are registered in `interface/012_africa.gfx`.
- `GFX_portrait_independence_wave_gorilla_chair` is registered in `interface/chaosx_characters.gfx`.
- Generic African portrait sprites used by regional authorities resolve via vanilla interface definitions and available texture paths.
- The unresolved asset blocker is the missing Africa cosmetic flag families listed above.

## Starting Military, Technology, Industry, Supply, And Production Issues

No narrow starting-military package defect was found.

Confirmed OOB coverage:

- Land OOBs: `WAC_1936`, `SAH_1936`, `MAG_1936`, `NHR_1936`, `EAC_1936`, `GLK_1936`, `CBC_1936`, `ZSC_1936`, `SLC_1936`, `IOC_1936`, `GHP_1936`, `BBS_1936`, `TDM_1936`, `ANW_1936`, `OVN_1936`, `CRR_1936`, `CTL_1936`, `OKP_1936`, `TRM_1936`, `HGD_1936`, `GHC_1936`
- Naval OOBs: `WAC_1936_naval_mtg`, `WAC_1936_naval_legacy`, `MAG_1936_naval_mtg`, `MAG_1936_naval_legacy`, `EAC_1936_naval_mtg`, `EAC_1936_naval_legacy`, `CBC_1936_naval_mtg`, `CBC_1936_naval_legacy`, `IOC_1936_naval_mtg`, `IOC_1936_naval_legacy`, `TDM_1936_naval_mtg`, `TDM_1936_naval_legacy`, `ANW_1936_naval_mtg`, `ANW_1936_naval_legacy`, `OVN_1936_naval_mtg`, `OVN_1936_naval_legacy`, `CRR_1936_naval_mtg`, `CRR_1936_naval_legacy`
- Air OOBs: `MAG_1936_air_bba`, `MAG_1936_air_legacy`, `NHR_1936_air_bba`, `NHR_1936_air_legacy`, `SLC_1936_air_bba`, `SLC_1936_air_legacy`, `IOC_1936_air_bba`, `IOC_1936_air_legacy`, `OVN_1936_air_bba`, `OVN_1936_air_legacy`

Remaining uncertainty:

- This audit did not rebalance force sizes, equipment stockpiles, state industry, supply, or role reinforcement values. Those would be a balance/design pass rather than a narrow country-package safety patch.

## AI And Playability Issues

No missing AI strategy linkage was found for the 21 created actors.

Confirmed AI surface:

- Regional role strategies are gated by `africa_regional_authority_subject`.
- High-chaos role strategies are gated by `africa_high_chaos_actor`.
- Per-tag AI strategy blocks exist for all 21 actors in `common/ai_strategy/012_africa.txt`.

Remaining playability risk:

- The shared companion focus trees are broad role-family trees with tag-specific capstones, not fully bespoke country trees. This is an accepted depth limitation from the current implementation, not a country-package wiring defect found in this audit.

## Validation

Meaningful validation performed:

- Parsed `common/country_tags/chaosx_countries.txt` and confirmed all 21 Event 012 actor tags resolve to existing country definition files.
- Parsed the 21 matching `history/countries/` files and confirmed valid capitals against combined mod and vanilla state IDs.
- Parsed country history OOB references and confirmed referenced land, naval, and air OOB files exist.
- Parsed country leader portrait sprite references and checked them against mod and vanilla interface sprite definitions.
- Parsed `localisation/english/chaosx_countries_l_english.yml` and confirmed created actor country, ideology, adjective, and party localisation coverage.
- Checked setup/focus/AI linkage across `common/scripted_effects/012_africa_effects.txt`, `common/national_focus/012_africa_authority_focus.txt`, and `common/ai_strategy/012_africa.txt`.
- Checked flag file presence for created actor tags and Africa cosmetic identities in `gfx/flags/`, `gfx/flags/medium/`, and `gfx/flags/small/`.

Skipped validation:

- No in-game launch or branch simulation was performed.
- No decision, achievement, spreadsheet, super-event, or audio validation was performed because the task explicitly scoped those surfaces out.
- No asset generation or flag placeholder copying was performed because the remaining flag-family issue is an asset package gap outside the narrow patch scope.

## Simplifications, Omissions, And Blockers

Simplifications:

- None in code, because no gameplay or localisation patch was made.

Omissions by requested scope:

- Decisions, missions, achievements, spreadsheets, super-event/audio files, and full focus-tree content review were not edited or deeply audited.

Blockers:

- Africa cosmetic flag families are incomplete. This is the only blocker identified in this country-package pass.

Uncertainty:

- Runtime state-transfer outcomes and AI military performance still need live or scenario-level validation if the parent wants balance/playability proof beyond static package integrity.
