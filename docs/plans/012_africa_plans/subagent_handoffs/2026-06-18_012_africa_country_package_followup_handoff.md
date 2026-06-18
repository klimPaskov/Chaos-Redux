# Event 012 Africa Country Package Follow-up Handoff

Date: 2026-06-18
Agent role: Chaos Redux country package subagent
Scope: Event 012 Africa country-package surfaces only. Focus and decision files were audited but not edited.

## Changed files

- `localisation/english/chaosx_countries_l_english.yml`

Changed localisation keys:

- Africa route/cosmetic keys: `AFR_democratic`, `AFR_FEDERAL_CHARTER*`, `AFR_PEOPLES_LIBERATION*`, `AFR_CONTINENTAL_COMMAND*`, `AFR_CROWN_CONGRESS*`, `AFR_PAN_ATLANTIC_democratic*`, `AFR_ARCHIVE_MANDATE*`, `AFR_CONGRESS_OF_CONTINENTS*`.
- Regional authority country keys: `WAC*`, `SAH*`, `NHR*`, `EAC*`, `GLK*`, `CBC*`, `SLC*`, `IOC*`.

Before behavior:

- Several public country/cosmetic names used generic institutional country names such as `West African Congress`, `East African Railway Congress`, `Great Lakes Council`, `Congo Basin Charter`, `Continental General Staff`, `African Crown Congress`, and `Congress of Continents`.

After behavior:

- Public country/cosmetic names use direct route, region, or state-form names such as `West Africa`, `Sahel`, `Nile-Horn`, `East Africa`, `Great Lakes`, `Congo Basin`, `South Africa`, `Indian Ocean`, `Federal Africa`, `People's Africa`, `Continental Africa`, `Crown Africa`, `Old-Seat Africa`, and `Union of Continents`.
- Party names, focus names, decision names, and internal ids were left untouched; those surfaces can still use offices, congresses, councils, charters, and staff terms as mechanics/institutions.

No files were staged or committed.

## Country Package Coverage Checklist

- Implemented Event 012 route/cosmetic identity surface: `AFR` plus cosmetic tags in `common/countries/cosmetic.txt` with localisation in `localisation/english/chaosx_countries_l_english.yml`.
- Implemented regional authority tags: `WAC`, `SAH`, `MAG`, `NHR`, `EAC`, `GLK`, `CBC`, `ZSC`, `SLC`, `IOC`.
- Implemented high-chaos actor tags: `GHP`, `BBS`, `TDM`, `ANW`, `OVN`, `CRR`, `CTL`, `OKP`, `TRM`, `HGD`, `GHC`.
- All 21 Event 012 created actor tags above have tag registration, common country file, history file, land OOB, capital, leader/council display, ideology setup, country localisation, party localisation, base flags, medium flags, small flags, and a shared setup hook.
- Expanded matrix tags such as `JLF`, `MOS`, `HSA`, `BOR`, `BGM/WAD`, `SNG`, `OYO`, `EDO`, `DAH`, `ASH`, `KNG`, `LUB`, `LND`, `KSH`, `AXM`, `AJU`, `SWA`, `BUG`, `LOZ`, `MER`, and `ZNG` are not implemented as country tags. They appear to remain dossier/authority design entries rather than country packages.
- `KBN` exists as `Kanem-Bornu Authority`, but its files identify it as an Event 006 Independence Wave generic release. It is not wired as an Event 012 regional authority in `africa_bind_regional_authority_subjects`.

## File Surface Checklist

- Tag registration checked: `common/country_tags/chaosx_countries.txt`.
- Country definition files checked: `common/countries/*.txt` for the 21 Event 012 tags.
- Country history checked: `history/countries/{WAC,SAH,MAG,NHR,EAC,GLK,CBC,ZSC,SLC,IOC,GHP,BBS,TDM,ANW,OVN,CRR,CTL,OKP,TRM,HGD,GHC} - *.txt`.
- OOB files checked: `history/units/{WAC,SAH,MAG,NHR,EAC,GLK,CBC,ZSC,SLC,IOC,GHP,BBS,TDM,ANW,OVN,CRR,CTL,OKP,TRM,HGD,GHC}_1936.txt`.
- Naval/air OOB surfaces checked: coastal/island/suitable actors have split naval and/or air OOBs where present, including `WAC`, `MAG`, `EAC`, `CBC`, `IOC`, `TDM`, `ANW`, `OVN`, `CRR`, plus air for `MAG`, `NHR`, `SLC`, `IOC`, `OVN`.
- Focus loading checked: `common/scripted_effects/012_africa_effects.txt` loads `africa_regional_authority_focus_tree` and `africa_high_chaos_actor_focus_tree`; `common/national_focus/012_africa_authority_focus.txt` has country scoring based on `africa_regional_authority_subject` and `africa_high_chaos_actor`.
- AI checked: `common/ai_strategy/012_africa.txt` has unifier, regional authority, and high-chaos actor strategies, with tag-specific postures for regional groups and Bestiary groups.
- Asset references checked: `interface/012_africa.gfx` portrait sprite references resolve to `gfx/leaders/012_africa/*.dds`; `GHP` intentionally uses the existing `GFX_portrait_independence_wave_gorilla_chair`.
- Country localisation checked and patched in `localisation/english/chaosx_countries_l_english.yml`.
- Event-local seat and idea text checked in `localisation/english/012_african_union_l_english.yml`; no patch made there because those are mechanic/seat labels rather than public country names.

## Missing Or Stale Country Package Surfaces

- The expanded historical/legacy authority matrix is not implemented as a full tag roster. Most priority A/B authorities from `docs/specs/012_africa_specs/matrices/012_africa_expanded_subject_matrix.md` and `012_africa_niche_country_matrix.md` have no tag, country file, history file, OOB, flag, portrait, or AI strategy.
- `KBN` is a stale adjacent surface for Event 012 purposes: public names still use `Authority`, it uses `GFX_portrait_generic_africa_male_03`, and it is not bound by Event 012 setup helpers. I did not patch it because its files identify it as Event 006 scope.
- `CTL`, `OKP`, `TRM`, `HGD`, and `GHC` have root/medium/small `.tga` flag files, but no root `.dds` alongside the `.tga` while the other Event 012 actor flags have both. If the project standard expects DDS parity, these five need asset follow-up.
- No per-tag production-line setup was found in the 21 static OOBs. Created-country setup grants stockpiles/buildings through `africa_apply_created_country_setup_package`, but production-line initialization remains a weaker surface.

## Map And State Setup Issues

- The 21 Event 012 created actors have capitals in history:
  - Regional: `WAC` 558, `SAH` 556, `MAG` 459, `NHR` 271, `EAC` 546, `GLK` 548, `CBC` 295, `ZSC` 771, `SLC` 275, `IOC` 543.
  - High-chaos: `GHP` 768, `BBS` 778, `TDM` 905, `ANW` 779, `OVN` 773, `CRR` 772, `CTL` 718, `OKP` 890, `TRM` 889, `HGD` 903, `GHC` 904.
- These tags do not own starting states in normal history; they are dynamically created by Event 012 through controlled seat-state transfer helpers in `common/scripted_effects/012_africa_effects.txt`.
- Dynamic creation requires ROOT to own/control the relevant seat state. If the unifier cannot hold a seat state, that actor does not spawn from that helper; that matches the staged-authority premise but leaves many matrix authorities absent as countries.
- I did not audit state buildings, railways, ports, supply hubs, victory points, resources, or strategic region balance state-by-state. The setup helper gives limited capital infrastructure and selected naval base/dockyard/factory/bunker additions by tag.

## Politics, Leaders, Portraits, Flags, Advisors, And Parties

- Human regional authority tags use ordinary ideologies and institutional council leader display names. Their portraits are generated/institutional Event 012 portraits, not personal random-name leaders, so no male/female name-pool mismatch was found.
- High-chaos actor tags use institutional/nonhuman/supernatural leader display names and generated/symbolic portraits. No human personal names were assigned to nonhuman actors.
- Event 012 separates high-chaos actors from human authorities via `africa_high_chaos_actor` and `africa_high_chaos_nonhuman` flags. Remaining precision risk: supernatural actors (`BBS`, `TDM`, `ANW`, `OVN`) share the same `africa_high_chaos_nonhuman` flag as actual nonhuman actors instead of having a separate supernatural classification flag.
- Party names still contain congress/council/charter/institution language. That is acceptable for party/mechanic surfaces under the direct-name rule, but the parent may want a localisation audit if party tone should become more region-specific.
- Advisor/staff pool was not deeply re-audited, but previous identifiers are referenced in repo handoffs; the current check focused on country package surfaces.

## Focus, Decision, Idea, And Asset Issues

- Shared focus loading exists for created regional authorities and Bestiary actors:
  - `africa_setup_regional_authority_subject` loads `africa_regional_authority_focus_tree`.
  - `africa_setup_high_chaos_actor` loads `africa_high_chaos_actor_focus_tree`.
- The shared authority/high-chaos focus trees have tag-specific branchlets for the 10 regional authorities and 11 high-chaos actors. They are not bespoke full country trees.
- Starting ideas exist for role separation: `africa_regional_authority_spirit` and `africa_high_chaos_actor_spirit`.
- Event 012 portrait sprite definitions in `interface/012_africa.gfx` resolve to existing DDS files for all 20 new generated portraits; `GHP` uses the existing Independence Wave gorilla chair portrait.
- Root country/route asset manifests are split across many `docs/assets/012_africa/*/manifest.md` files. There is no single compact country-package asset ledger for all 21 actor flags/portraits in the checked root folder.

## Starting Military, Technology, Industry, Supply, And Production

- All 21 implemented Event 012 actors have land OOBs with at least one division template and starting unit.
- Regional authorities receive 3 research slots except `SLC` with 4; high-chaos actors receive 2.
- Static histories assign relevant basic technologies: infantry weapons, support, and tag-specific additions such as logistics, trains, mountaineers, engineers, motorized, early fighter, or naval hull/transport tech.
- `africa_apply_created_country_setup_package` gives tag-specific equipment, manpower, limited infrastructure, naval bases, dockyards, factories, or bunkers using constants in `common/scripted_effects/012_africa_effects.txt`.
- Reinforcement hooks exist:
  - `africa_create_authority_guard_divisions`
  - `africa_create_authority_guard_reinforcement_divisions`
  - `africa_create_high_chaos_guard_divisions`
  - `africa_create_high_chaos_guard_reinforcement_divisions`
  - decision/focus reward paths also add equipment, manpower, convoys, trains, support equipment, and buildings.
- Static OOB files themselves do not define production lines. If these actors are expected to persist as independent fighting countries, production setup should be added or confirmed through a parent balance pass.

## AI And Playability Issues

- AI strategy exists for:
  - unifier consolidation, liberation route, People's Liberation, Continental General Staff, Crown Congress, diaspora return, world-order sponsor, RSA emergency;
  - generic regional authority survival and grouped regional specializations;
  - generic high-chaos actor survival and grouped Bestiary specializations.
- AI validity for the 21 implemented actor tags is present at posture level, but the expanded historical-authority matrix lacks country-level AI because most of those authorities are not tags.
- Playability is strongest for the selected unifier and 21 created actor tags. Expanded restored old-seat authorities remain mostly dossier/focus/decision content, not playable country packages.
- No generic/fallback package was found for the 21 implemented actors in the strict tag/portrait/OOB sense: each has its own tag, history, OOB name, portrait, flags, and localisation. The shared setup/focus trees are still a simplification relative to bespoke packages.

## Meaningful Validation Run

- Checked Event 012 tag registration, country definition paths, histories, OOBs, base flags, medium flags, and small flags for the 21 implemented actor tags.
- Checked `interface/012_africa.gfx` portrait texture paths; all Event 012 portrait DDS references exist.
- Checked direct country-name rule for Event 012 `AFR*`, regional authority, and `KBN` public country keys after patch. Remaining administrative-name hits are `KBN*`, which is scoped in files as Event 006, not Event 012.
- Checked localisation BOM for `localisation/english/chaosx_countries_l_english.yml`; BOM remains present after patch.
- Checked focus-tree loading hooks and role flags for regional authority versus high-chaos actor setup.

## Skipped Meaningful Validation

- No in-game launch was run.
- No focus/decision file edits were made, per prompt. Focus and decision surfaces were inspected only for country-package integration hooks.
- No binary asset conversion or flag/portrait visual QA was run.
- No state-by-state balance pass was run for ports, rails, supply hubs, resource values, or victory points.

## Remaining Blockers And Risks

- Expanded historical authority country package coverage is incomplete if the acceptance target requires tags for the full matrix rather than dossier-only representation.
- `KBN` remains a stale adjacent African package with direct-name violations and generic portrait use, but it is labelled Event 006 and was left untouched.
- Five high-chaos actor flags lack root `.dds` parity (`CTL`, `OKP`, `TRM`, `HGD`, `GHC`) despite having `.tga` flag sets.
- Supernatural actors share `africa_high_chaos_nonhuman` with actual nonhuman actors; this may be sufficient for broad exclusion from human systems, but not for precise supernatural-vs-nonhuman separation.
- Static OOBs lack production-line setup; long-lived actor survival depends on scripted stockpiles, setup-package buildings, focus rewards, decisions, and AI building strategy.
- Other dirty working-tree files were present and not staged or reverted. I only intentionally changed `localisation/english/chaosx_countries_l_english.yml`.
