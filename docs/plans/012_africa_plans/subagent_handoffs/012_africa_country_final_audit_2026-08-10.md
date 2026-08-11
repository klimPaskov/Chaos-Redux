# Event 012 Africa country-package final audit

Date: 2026-08-10

Scope: final read/write country-package certification for Event 012 (Africa), limited to the existing Independence Wave tags and current shared tree. This audit preserves concurrent work and does not add tags, states, or broad identity content.

## Result

The country package surfaces are structurally covered: the host playbook contains 22 full and 29 compact bindings, the HZX/EUX/ELX niche receipts are guarded, all 16 priority packages have carrier, identity, council, force, decision, idea, focus, localisation, and asset surfaces, the six Tier A promoted packages use the required fixed carriers/states, and the RSA Allied civil-war branch preserves the original South African host. No country gameplay file was patched in this pass. The only file written by this subagent is this handoff.

No new country tag, state, capital, owner/controller rule, or fallback package was invented. No simplification was introduced. The remaining limitations are certification limits recorded below, not substitutions in source.

## Required references and source review

Before the audit, I read `AGENTS.md`, the Chaos Redux event and subagent skills, the focus-tree, event-assets, and portrait skills, the required offline Paradox wiki pages in `paradox_wiki/`, and the applicable vanilla HOI4 documentation under `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\`. Vanilla country, map, event, focus, character, portrait, and flag precedents were also consulted where the package surface required them.

## Country-package coverage checklist

| Surface | Evidence | Result |
| --- | --- | --- |
| Host registration | `common/script_constants/012_africa_constants.txt:337-395` lists 22 full and 29 compact host IDs; `common/scripted_effects/012_africa_effects.txt:316-375` contains 51 mapped branches | Covered; counts match the Event 012 contract |
| HZX/EUX/ELX receipts | Direct `HZX`, `EUX`, and `ELX` branches in `common/scripted_effects/012_africa_effects.txt:367-371` are guarded by `africa_is_valid_independence_wave_niche_host_binding`; trigger is in `common/scripted_triggers/012_africa_triggers.txt:50` | Covered and fail-closed |
| Host eligibility | `africa_is_eligible_host` in `common/scripted_triggers/012_africa_triggers.txt:359` checks existence, mapping, niche receipt, pre-fire contact, generic-focus loading, non-capitulation, African capital/core control, no civil war, and terminal/global flags | Covered |
| Original host preservation | `africa_initialize_selected_host` in `common/scripted_effects/012_africa_effects.txt:424` saves the host, keeps its tag/government/leaders/territory/armies/public identity, applies only the playbook and focus handoff, and suppresses the generic popup only for the dedicated RSA branch | Covered |
| Priority members | 16 package IDs in `common/script_constants/012_africa_priority_member_constants.txt:9-31`; predicates and registration are in `common/scripted_triggers/012_africa_priority_member_triggers.txt` | All 16 covered |
| Promoted Tier A | Fixed carriers and states in `common/script_constants/012_africa_promoted_tiera_constants.txt:8-35`; eligibility and reveal effects in `common/scripted_triggers/012_africa_promoted_tiera_triggers.txt` and `common/scripted_effects/012_africa_promoted_tiera_effects.txt` | All six covered |
| RSA Allied settlement | `common/scripted_triggers/012_africa_rsa_triggers.txt`, `common/scripted_effects/012_africa_rsa_effects.txt`, `events/012_african_union.txt`, and `common/on_actions/012_africa_rsa_on_actions.txt` | Covered; dedicated civil-war and settlement cleanup present |
| Tag collision safety | `.tools/audit_chaosx_country_tags.py --surface-scan` reported `external country-definition collisions: 0; external identity-surface collisions: 0` | No collision found |

## Priority 16 package matrix

The matrix below records the current carrier and map binding. Dormant packages intentionally have no unique state binding and are not assigned an invented state.

| Package | Existing carrier | State/map binding | Legitimacy or council identity | Force profile |
| --- | --- | --- | --- | --- |
| Asante | `DOX` | 274 | Stool-council legitimacy | Royal guard |
| Oyo | `DSX` | 558 | Corridor-city compact | Mobile guard |
| Sokoto | `SOK` | 902 (current split) | Emirate reform | Mobile guard |
| Kanem-Bornu | `DUX` | 901 | Lake/caravan covenant | Mobile guard |
| Manden | `MLI` | 556, 782, 898, 899 | Assembly legitimacy | Mobile guard |
| Kongo | `COG` | 295, 538, 718, 768, 769, 888-890 | Cross-border consent | River guard |
| Buganda | `UGA` | 548 | Kingdom federal balance | Royal guard |
| Aksum | `TIG` | 842 | Heritage consent | Highland guard |
| Harar | `HAR` | 835 | Corridor guarantees | Mobile guard |
| Kilwa | `EMX` | Dormant by design; no unique state | Common customs | Coastal guard |
| Nubia | `SUD` | 549, 551, 883-887 | River rights | Mobile guard |
| Luba | `DYX` | Dormant by design; no unique state | Mining/local consent | River guard |
| Lunda | `DZX` | Dormant by design; no unique state | Cross-border access | Mobile guard |
| Great Zimbabwe | `ZIM` | 545 | Restoration mandate | Highland guard |
| Merina | `MAD` | 543, 706, 708 | Island federalism | Coastal guard |
| Zulu | `EQX` | 719 | Crown/land/labour | Mobile guard |

The five force profiles in `common/scripted_effects/012_africa_priority_member_force_effects.txt:12-164` cover all 16 packages. The idempotent initializer at `:259` requires the package plus owned-and-controlled territory, avoids duplicate divisions, and adds primary/reserve formations only below the two-formation threshold.

All 16 package predicates, origin gates, package registration, and portrait approval are present in `common/scripted_triggers/012_africa_priority_member_triggers.txt`. The registration trigger is fail-closed at `africa_priority_member_can_register_package` (`:545`). The one repeated `NOT = { is_independence_wave_registry_soviet_origin = yes }` in the Kanem-Bornu origin branch is harmless duplication, not a behavior change.

## Promoted Tier A fixed mappings

| Package | Required carrier | Required state(s) | Capital/control requirement | Cosmetic/public identity |
| --- | --- | --- | --- | --- |
| Pan Toolmaker Compact | `EBX` | 900 | Own and control 900; capital in 900 | `AFRICA_PROMOTED_PAN`; direct name localisation |
| Gorilla Kingdom | `EHX` | 768 | Own and control 768; capital in 768 | `AFRICA_PROMOTED_GORILLA`; direct name localisation |
| The Green | `DPX` | 298 | Own and control 298; capital in 298 | `AFRICA_PROMOTED_GREEN`; direct name localisation |
| Living Rivers | `EEX` | 548 | Own and control 548; capital in 548 | `AFRICA_PROMOTED_RIVERS`; direct name localisation |
| Stoneborn | `DFX` | 460 | Own and control 460; capital in 460 | `AFRICA_PROMOTED_STONEBORN`; direct name localisation |
| Ancient Hosts | `DHX` | 448 and 661 | Own and control both; capital in 448 | `AFRICA_PROMOTED_ANCIENT`; direct name localisation |

The carrier trigger uses exact `original_tag` or `tag` checks for `EBX`, `EHX`, `DPX`, `EEX`, `DFX`, and `DHX`. Eligibility rejects already-claimed global flags and requires the fixed state ownership/control checks. Reveal effects transfer only the specified existing states, set the corresponding cosmetic/lifecycle flags, install the fictional leader and starting idea, and fire the package event. The `DHX` branch transfers both 448 and 661 and keeps 448 as capital.

Promoted public names are direct, player-facing localisation in `localisation/english/012_africa_promoted_tiera_l_english.yml:2-19`; there is no generic or fallback country name. `common/countries/012_africa_cosmetic.txt` supplies the cosmetic definitions.

## File-surface checklist

| Surface | Current files and finding |
| --- | --- |
| Country tags and shells | Existing Event 006 registration in `common/country_tags/006_independence_wave_countries.txt` and shells in `common/countries/006_independence_wave_{DOX,DSX,DUX,DYX,DZX,EMX,EQX}.txt`; Event 012 adds no country-tag file. Vanilla carriers are not redefined. |
| Host effects/triggers | `common/scripted_effects/012_africa_effects.txt`, `common/scripted_triggers/012_africa_triggers.txt`, and `common/script_constants/012_africa_constants.txt` contain mapping, eligibility, preservation, focus loading, and 22/29 registration surfaces. |
| Priority effects/triggers | `common/scripted_effects/012_africa_priority_member_effects.txt`, `common/scripted_triggers/012_africa_priority_member_triggers.txt`, `common/scripted_effects/012_africa_priority_member_character_effects.txt`, and `common/scripted_effects/012_africa_priority_member_force_effects.txt` cover package lifecycle, identity, councils, and forces. |
| Priority country identities | `common/characters/012_africa_priority_member_characters.txt` defines all 16 sovereign characters with `gender = male` and package portrait paths. Character localisation is in `localisation/english/012_africa_priority_member_characters_l_english.yml`; names are direct public names. |
| Priority gameplay | `common/ideas/012_africa_priority_member_ideas.txt`, `common/decisions/012_africa_priority_member_decisions.txt`, `events/012_africa_priority_member_events.txt`, and `common/national_focus/012_africa_priority_member_focus.txt` exist and contain all 16 package identifiers. |
| Priority focus loading | `africa_load_continental_focus_tree` in `common/scripted_effects/012_africa_effects.txt:541` and the priority loader in `common/scripted_effects/012_africa_priority_member_effects.txt:245` preserve Event 006/Soviet/active trees and load the shared priority tree only on safe generic/direct surfaces. |
| Promoted package | `common/scripted_effects/012_africa_promoted_tiera_effects.txt`, `common/scripted_effects/012_africa_promoted_tiera_settlement_effects.txt`, `common/scripted_triggers/012_africa_promoted_tiera_triggers.txt`, `common/ideas/012_africa_promoted_tiera_ideas.txt`, `common/decisions/012_africa_promoted_tiera_decisions.txt`, `events/012_africa_promoted_tiera_events.txt`, `common/ai_strategy/012_africa_promoted_tiera.txt`, and `common/on_actions/012_africa_promoted_tiera_on_actions.txt` are present. |
| Promoted leaders/assets | `common/characters/012_africa_fictional_characters.txt` and `interface/012_africa_leaders_fictional.gfx` cover six symbolic fictional leaders; `interface/012_africa_promoted_tiera_assets.gfx` registers promoted icons/report assets. |
| RSA | `common/scripted_triggers/012_africa_rsa_triggers.txt`, `common/scripted_effects/012_africa_rsa_effects.txt`, `events/012_african_union.txt`, and `common/on_actions/012_africa_rsa_on_actions.txt` cover gate, civil-war start, Allied inheritance, victory, settlement, and cleanup. |
| Localisation/assets | Priority assets are registered in `interface/012_africa_priority_member_assets.gfx`; all 16 runtime/source-locked portrait DDS paths exist under `gfx/leaders/012_africa/priority_members`. Event 012 focus, idea, decision, and report icons resolve in the registered asset surface. |

## Politics, leaders, portraits, flags, advisors, and parties

Host initialization preserves the selected host's original tag, government, leaders, territory, armies, and public identity. Priority package character effects provide council/civic/producer sovereign roles for all 16 packages, while `common/characters/012_africa_priority_member_characters.txt` keeps every package sovereign explicitly male. Character localisation uses direct regional or institutional names such as Asantehene, Alaafin, Sultan, Shehu Sanda Kura, Pedro VII Afonso, Ezana, Taharqa, and Radama II.

The six promoted leaders are fictional symbolic or institutional bodies in `common/characters/012_africa_fictional_characters.txt`; their runtime leader assignment uses the existing Event 006 `DJX` character pool and does not create a country tag. All six are male metadata, and the portrait/GFX paths point to generated runtime DDS outputs. Promoted cosmetic names are direct public names rather than implementation labels.

No package-specific advisor or high-command roster is required by the current design; the package uses sovereign/council/party focus surfaces. No opposite-gender portrait/name pairing was found in the inspected package character definitions. The source-locked portraits are present, but their grounded provenance and final HOI4-style acceptance remain an explicit portrait-worker/user certification item, especially for the ancient or date-misaligned Aksum, Nubia, and Merina actors. No substitute portrait was introduced.

Existing Event 006 cosmetic names and flags remain the carrier identity layer. Event 012 promoted cosmetics are separate and are cleaned up on defeat. No new flag or tag family was invented.

## Focus, decisions, ideas, and assets

The package focus tree at `common/national_focus/012_africa_priority_member_focus.txt` contains eight focuses with nine connectors and no package-tree diagnostics in the MCP inspection. It is a shared priority tree; package differentiation is supplied by scripted package effects, decisions, ideas, and identity routes rather than copied country trees. The continental tree remains the shared 276-focus tree and was inspected separately; its layout warnings are recorded under MCP limitations below and were not altered in this country audit.

All 16 package identifiers occur in the priority effect, trigger, character, force, idea, decision, event, focus, and localisation surfaces. Visible package events `.1200`, `.1210`, `.1220`, and `.1230` contain all 16 package descriptions; hidden `.1240` recruits existing vanilla sovereigns. Focus and decision icon registrations resolve through the existing Event 012 asset GFX. No missing package icon was found in static path checks.

## Starting military, technology, industry, supply, and production

The package force initializer is deliberately conditional and idempotent: it requires an eligible package and owned/controlled territory, then supplies the package's primary and reserve guard profile without duplicating divisions. Host initialization does not replace the original host's equipment, manpower, technology, production, ports, railways, or supply identity. No broad army, stockpile, industry, or technology rebalance was introduced in this audit.

The MCP technology scan was run, but the installed package exposed no dedicated Technology Tree Viewer render/compare route for a country-specific technology tree. Therefore technology-tree visual/compare certification remains unresolved rather than being represented by a fallback. Live save/session validation of starting stockpiles, production lines, manpower, fuel, and supply belongs to parent/user verification; this subagent did not launch HOI4.

## AI and playability

Promoted AI strategy blocks exist in `common/ai_strategy/012_africa_promoted_tiera.txt` for all six packages with bounded package-specific priorities: Pan build-army 65/avoid-war 20, Gorilla 95/70, Green 35/130, Rivers 55/force-defend-ally-borders 90, Stoneborn 85/40, and Ancient 75/65. Priority packages use the shared focus/decision/effect route and host-preserving setup; no package-specific AI strategy file exists for the 16-member set beyond those shared decision/focus surfaces.

No probability-bearing patch was made here. The required probability baseline and compare pass for AI strategy factors, focus/decision scores, random selection, or MTTH must be completed and reported by the parent through `chaosx_ai_probability_auditor`; this handoff does not claim that pass.

## RSA Allied civil-war settlement

The RSA gate in `common/scripted_triggers/012_africa_rsa_triggers.txt` requires current/original SAF, no active civil war/global Event 012 state, Allied faction evidence, and control of Pretoria, Cape, and Natal. The release gate for `ESX` additionally requires anti-war support of at least 60, no existing `ESX`, and a dynamically eligible SAF core state that excludes `EQX` and the promoted principals.

`common/scripted_effects/012_africa_rsa_effects.txt` snapshots pre-war context, starts the deterministic civil war, preserves original SAF as coalition host, and gives the Allied Union Government inherited faction/autonomy, pre-war government, equipment ratios, and ports. The optional `ESX` branch is gate-bound and does not consume `EQX`. RSA on-actions record intervention, victory, and settlement. Cleanup restores the original capital, clears runtime targets and branch flags, drops branch cosmetic/leader state, and preserves `ESX` tag/core where applicable. The dedicated RSA success path suppresses the generic delayed first-contact popup; ordinary delayed handling remains for other hosts.

## Mandatory MCP evidence

The following read-only routes were run against workspace `mod_chaos_redux_ea3b2d67c2c0` before this report.

| Surface | Route and result | Artifact |
| --- | --- | --- |
| Event state flow | `hoi4_event_inspect` for `chaosx.nr12.1`, `mode=state_flow`, both directions, helpers expanded; `EVENT_INSPECTED_PARTIAL`, no blocking diagnostics. Counts: 9,499 events, 14,687 options, 1,060 entries, 37,052 edges; helper/lifecycle projections deferred and inline files truncated. | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b2905d5636d74e10f3713acad11d11fa93f2b00daefd66e10592f4c1c6690265/53df677d29b268523bfcb231550045bd68bc8f282bf1c65b0c8c72c24cf6d5d3/event-state_flow-c11a255294fb.json` |
| Event render | `hoi4_event_render` state view for `chaosx.nr12.1`; `EVENT_RENDERED_PARTIAL`, no blocking diagnostics. | Manifest `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/577218031d513e984c64e189cc2780c49a57407c778e53fd8a2cd44ae6ebc679/e66bf0a83761bdc50dc9d1e85567c82292433d227b925cc13867db72c5985080/event-state-c11a255294fb-manifest.json`; JSON `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/577218031d513e984c64e189cc2780c49a57407c778e53fd8a2cd44ae6ebc679/e66bf0a83761bdc50dc9d1e85567c82292433d227b925cc13867db72c5985080/event-state-c11a255294fb.json`, SVG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/577218031d513e984c64e189cc2780c49a57407c778e53fd8a2cd44ae6ebc679/e66bf0a83761bdc50dc9d1e85567c82292433d227b925cc13867db72c5985080/event-state-c11a255294fb.svg`, and PNG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/577218031d513e984c64e189cc2780c49a57407c778e53fd8a2cd44ae6ebc679/e66bf0a83761bdc50dc9d1e85567c82292433d227b925cc13867db72c5985080/event-state-c11a255294fb.png` |
| Map inspection | `hoi4_map_inspect` on the 17-state Event 012 priority/promoted/RSA set; `MAP_INSPECTED`, unknown province IDs and missing geometry IDs empty, map/state-region/network checks true. A preceding broad inspect covered 27 distinct priority, promoted, and RSA states including the Sokoto, Aksum, Harar, Great Zimbabwe, and Merina bindings. | Narrow artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/82b67ba2ca08977d9b00f565e7b92df9ea20f95a45b23279809e8b0f5604d077/35a0156985db93c81e0ba0572f6e70de5bcb3c1c3725a9413de3748e2417a95e/map-inspect.b00cb7b1afbebbfa.json`; broad artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4c92382116fde99a42b29bc085d6cf8f8a3babd91434d8cc75e9d368dda362c5/2f1c37e074a21d98f284e1694dec324ce53cd4aaaa03b278f6c9597c059175b4/map-inspect.00ef22e5d9803968.json` |
| Map render | `hoi4_map_render` state layer with coastlines, ports, victory points, resources, state buildings, railways, and adjacencies; validation true. | PNG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/26e7f75d45704b50a303b13c42fac34b941172051ff4a51726fe51714ab8c4df/fd84323267a53baec6426f149c15817ca0ec2f20cae71ef16fd8a28ebcd7bc94/map-state.png`; JSON `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/26e7f75d45704b50a303b13c42fac34b941172051ff4a51726fe51714ab8c4df/fd84323267a53baec6426f149c15817ca0ec2f20cae71ef16fd8a28ebcd7bc94/map-state.json`; HTML `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/26e7f75d45704b50a303b13c42fac34b941172051ff4a51726fe51714ab8c4df/fd84323267a53baec6426f149c15817ca0ec2f20cae71ef16fd8a28ebcd7bc94/map-state.html` |
| Priority focus | `hoi4_focus_inspect` and `hoi4_focus_render` for `africa_priority_member_focus_tree`; eight focuses, nine connectors, zero crossings/intersections/long connectors, zero package-tree diagnostics. | Inspect JSON `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/98a0c8ceff8a2ba4f4ec0fe4c9a786fba66ce920d50bb8d98efe1fa97500ac3e/aac55b6dc005ee8ac758b13564438749cc36ae5f1a5d16587e36fae123a9e108/focus-inspect.00d440afb80ffee0.json`; HTML `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c7b5e8be08120d936ab079c3ca5727aa1477707782b4d7c409837ec7f18a812b/391639c8e069fe01286f2348470996794e0b1c8de99103b9ab01fe684e1a16df/africa_priority_member_focus_tree.focus.html`; SVG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c7b5e8be08120d936ab079c3ca5727aa1477707782b4d7c409837ec7f18a812b/391639c8e069fe01286f2348470996794e0b1c8de99103b9ab01fe684e1a16df/africa_priority_member_focus_tree.focus.svg`; JSON `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c7b5e8be08120d936ab079c3ca5727aa1477707782b4d7c409837ec7f18a812b/391639c8e069fe01286f2348470996794e0b1c8de99103b9ab01fe684e1a16df/africa_priority_member_focus_tree.focus.json`; source map `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c7b5e8be08120d936ab079c3ca5727aa1477707782b4d7c409837ec7f18a812b/391639c8e069fe01286f2348470996794e0b1c8de99103b9ab01fe684e1a16df/africa_priority_member_focus_tree.focus.source-map.json`; plan `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c7b5e8be08120d936ab079c3ca5727aa1477707782b4d7c409837ec7f18a812b/391639c8e069fe01286f2348470996794e0b1c8de99103b9ab01fe684e1a16df/africa_priority_member_focus_tree.focus.plan.json` |
| Continental focus | `hoi4_focus_inspect` and `hoi4_focus_render` for `africa_continental_focus_tree`; 276 focuses, 348 connectors, 58 crossings, 58 node intersections, 36 long connectors. | Inspect `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5d2a91e0778e4c270ac74bd6b1f77fe5d29174218787ba79ba2535e7729a230e/c0a466216a020453da17c427527a6375eb368bc57671ba47ac1ed569833e5085/focus-inspect.a7951710978ea1dc.json`; HTML `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/92540d488f6cac11a77bdfd846fa328bd62ea195d6324009bd4dd630be09ee70/6ca776b4689b26e1750ef37524c628c98de7d1aefb7c777ef0f791f938469d47/africa_continental_focus_tree.focus.html`; SVG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/92540d488f6cac11a77bdfd846fa328bd62ea195d6324009bd4dd630be09ee70/6ca776b4689b26e1750ef37524c628c98de7d1aefb7c777ef0f791f938469d47/africa_continental_focus_tree.focus.svg`; JSON `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/92540d488f6cac11a77bdfd846fa328bd62ea195d6324009bd4dd630be09ee70/6ca776b4689b26e1750ef37524c628c98de7d1aefb7c777ef0f791f938469d47/africa_continental_focus_tree.focus.json`; source map `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/92540d488f6cac11a77bdfd846fa328bd62ea195d6324009bd4dd630be09ee70/6ca776b4689b26e1750ef37524c628c98de7d1aefb7c777ef0f791f938469d47/africa_continental_focus_tree.focus.source-map.json`; plan `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/92540d488f6cac11a77bdfd846fa328bd62ea195d6324009bd4dd630be09ee70/6ca776b4689b26e1750ef37524c628c98de7d1aefb7c777ef0f791f938469d47/africa_continental_focus_tree.focus.plan.json` |
| Technology scan | `hoi4_tech_inspect mode=scan` completed `TECH_INSPECTED_PARTIAL`; 663 technologies, 18 folders, 475 placements, 457 edges, 838 unlocks, 19,746 references, 1,690 issues, three unresolved; helper projections deferred. No dedicated Technology Tree Viewer render/compare route was exposed. | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3f4e32834012e3d8c98f63bf7daad7369566fcc5a82e6359bda0d25be607257a/1ce1e791aac9cdd0ad184d5fcab67b917b82002609b2d4d1305233c47f32105a/technology-scan-1332a472ba53.json` |

The broad map inspection also found empty unknown/missing geometry sets. Global map diagnostics are dominated by 1,323 `MAP_BUILDING_POSITION_INVALID` and 1,331 `MAP_PORT_ADJACENT_SEA_INVALID` records in `mod:map/buildings.txt`, outside the Event 012 country package. Focus diagnostics include 14 generic continuous-focus icon blockers from vanilla `game:common/continuous_focus/generic.txt`; the continental layout metrics above are pre-existing/shared-tree findings. These MCP diagnostics were not patched because they are not narrow Event 012 country-package defects.

## Missing, stale, or unresolved surfaces

1. Sixteen source-locked priority portrait DDS files exist and are wired, but grounded provenance and final HOI4-style acceptance are not certified here. The Aksum/Ezana, Nubia/Taharqa, and Merina/Radama II identities need the portrait-worker/user evidence path; no fallback was silently substituted.
2. The installed MCP exposes technology scan but no dedicated Technology Tree Viewer render/compare route, so country technology visual/compare completion remains unresolved.
3. Live HOI4 save/session checks for starting manpower, stockpiles, production, fuel, supply, and post-settlement behavior were not run by this agent and remain parent/user validation.
4. Dormant `DYX`, `DZX`, and `EMX` packages intentionally have no unique state binding. Assigning states would violate the no-invented-state constraint.
5. Priority differentiation uses the shared eight-focus tree plus scripted package routes rather than 16 separate trees. This is the established package design, not a fallback introduced by this audit. A bespoke branch expansion would be a design decision and is outside a narrow country-package patch.
6. The Zulu sovereign description includes “awaits an eligible sovereign” wording despite the runtime sovereign install path; this is a minor localisation review item, not patched without parent design direction.

## Changed files and validation

Changed files: `docs/plans/012_africa_plans/subagent_handoffs/012_africa_country_final_audit_2026-08-10.md` only. No gameplay, country, state, map, focus, event, AI, portrait, flag, or localisation source was changed.

Meaningful validation used in this audit: the exact read-only Event 012 event inspect/render, map inspect/render, priority and continental focus inspect/render, technology scan, and country-tag collision surface scan listed above; static package-token/path review across the 16 package surfaces; fixed-state and carrier review for all six promoted packages; and RSA gate/settlement source review. No HOI4 process was launched.

## Parent review actions

1. Run the required `chaosx_ai_probability_auditor` baseline and `hoi4.probability_compare` pass for promoted AI strategies and any weighted focus/decision/MTTH surfaces using named Event 012 scenarios.
2. Route the 16 source-locked portraits through the portrait-worker provenance and final HOI4-style acceptance workflow before treating the asset package as final.
3. Record the technology-tree viewer limitation in the parent completion report; do not treat the scan artifact as a substitute for a missing Viewer render/compare route.
4. Perform parent-owned live/new-session checks for host preservation, package refusal, promoted fixed-state reveal, RSA Allied civil-war settlement, force initialization, and cleanup.
