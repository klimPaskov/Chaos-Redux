# Event 014 Cannibalism Country Final Audit v4

Audit date: 2026-08-24.

Scope: the eight reusable warlord slots CBA-CBH, ordinary unified host CBL, CBL cosmetic identities, ZZZ Wendigo conversion, and their shared country, history, focus, decision, event, scripted, unit, technology, AI, localisation, map, and asset surfaces.

Disposition: the country and transformation source package is substantially wired, but this tranche is not a clean release claim because several required evidence routes remain blocked. Portrait wiring is intentionally complete through a retained-texture alias system. No gameplay or asset patch was safe or necessary during this audit. The only file changed by this tranche is this handoff.

## Executive findings

- Eight reusable slots are registered consistently as CBA-CBH in `common/country_tags/014_cannibalism_countries.txt`, with matching country and history files.
- The active origin set is exactly Island Host, Siege Commune, and March Host; no active `Prison Host` origin or tag is present.
- Warlord creation is state-driven and transfers an origin state plus at most two valid controlled neighbours, cores the transferred territory, sets the origin capital, and releases/reuses slots through explicit cleanup.
- Unified Hannibal and Wendigo host selection is human-first, deterministic on ties, and contains player-control preservation checks; reveal flags are set before the identity transform so downstream setup is gated consistently.
- The Wendigo package preserves the original ZZZ identity ledger, origin specialist/legion/bone-guard/elephantry flags and caps, recruitment state, pack templates, anchor state registry, countdown route, and terminal lock form in source logic.
- The focus package is loaded by source ID and has MCP-validated warlord, unified, and Wendigo trees with no blocking diagnostics. The unified tree has 18 layout warnings that are non-blocking but should be reviewed before a visual polish pass.
- The runtime flag matrix is complete at 13 families x 5 ideology variants x 3 sizes = 195 TGA files. Git revision `894037493` preserves the complete 204-file ImageGen source package for the current CBA-CBH tag set, and all 195 installed runtime TGAs are byte-identical to that provenance checkpoint.
- Warlord portrait wiring deliberately uses 16 retained warlord DDS files behind the complete CBA-CBH regional/default sprite-token set in `interface/014_cannibalism.gfx`; the aliases are intentional and all referenced files exist.
- No active source text exposes Hannibal before reveal through an ancient-general, Carthaginian, Punic, or disclaimer string. The histories recruit `CBL_hannibal` and `ZZZ_hannibal_wendigo` as roleless characters before promotion; this is an intentional hidden-character pattern in source comments but retains a low engine-semantic visibility risk requiring live validation.
- Quantitative AI/probability validation is incomplete because the required `chaosx_ai_probability_auditor` route is not callable and the generic probability adapter discovered no weighted surfaces for the AI source. No AI weight was changed.
- The GUI scenario route timed out, the technology tree viewer is not installed, and broad event/technology/map workspace analysis is deferred or contaminated by unrelated global diagnostics. These are evidence limitations, not claims that those systems are runtime-clean.

## Country package coverage checklist

| Surface | Result | Evidence and identifiers |
| --- | --- | --- |
| Tag registration | Pass | `common/country_tags/014_cannibalism_countries.txt`; CBA-CBH plus CBL. No AHX/AIX/AMX registration remains. |
| Country definitions | Pass with dormant-state caveat | `common/countries/Cannibal Warlord Slot CBA.txt` through `CBH.txt` and `Cannibal Unified Host CBL.txt`; neutral party setup, no public leader in dormant slots. |
| Country histories | Pass with hidden-character caveat | `history/countries/CBA - Cannibal Warlord Slot.txt` through `CBH - Cannibal Warlord Slot.txt`, `CBL - Cannibal Unified Host.txt`; dormant OOB and CBL roleless Hannibal attachment are intentional source patterns. |
| State ownership and capitals | Source pass; engine map evidence partial | Dynamic state selection and transfer use current owner/control, supported regions, origin capital, and valid neighbours; no Event 014 custom state IDs. |
| Cores and claims | Source pass | Warlord creation cores transferred territory; absorption, submission, resistance, and release helpers migrate or clear cores and runtime references. |
| Origins | Pass | `cannibalism_state_can_form_island_host`, `cannibalism_state_can_form_siege_commune`, `cannibalism_state_can_form_march_host`; `cannibalism_state_can_form_any_warlord_origin` is the three-way OR. |
| Region naming and identity | Pass | Region pool and scripted localisation cover Europe, Asia, Africa, Middle East, North America, South America, and Oceania; all current generated names are male-presenting and leaders have no female metadata. |
| Political setup | Source pass | Dynamic ritual-predation identity, origin party names, neutrality/stability/war-support setup, laws, and later public role promotion are wired. |
| Focus loading | MCP pass | `cannibalism_warlord_focus_tree`, `cannibalism_unified_focus_tree`, and `cannibalism_wendigo_focus_tree` load from `common/national_focus/014_cannibalism_focus.txt`. |
| Decisions and missions | Source/localisation pass | `common/decisions/014_cannibalism_decisions.txt` and `common/decisions/categories/014_cannibalism_categories.txt`; 140 decision IDs found with localisation coverage. |
| Ideas and national spirits | Source/localisation pass | `common/ideas/014_cannibalism_ideas.txt`; 37 direct `cannibalism_*` ideas checked for localisation, with broader icon set present. |
| Advisors and high command | Design warning | No dedicated Event 014 advisor/high-command/theorist definitions in `common/characters/014_cannibalism_characters.txt`; current source uses internal roleless characters and command ideas. |
| Flags | Pass | 13 families, five variants, three sizes; 195 files and unique per-size hashes. Git revision `894037493` contains 65 separate built-in ImageGen records, source masters, prompts, processing evidence, and validation for the current stems; the installed TGAs match it byte-for-byte. |
| Portraits | Pass with deliberate aliases | The 64 CBA-CBH warlord regional/default sprite tokens intentionally reuse the retained 16 warlord DDS files; the two mandated `hannibal.dds` and `hannibal_wendigo.dds` files are present. |
| Units and equipment | Source pass with activation risk | Nine custom irregular subunits and four vanilla equipment tokens are defined/registered; all custom units are `active = no` and templates are locked, so live recruitment/activation remains an engine-semantic risk. |
| Technology | Partial | Setup inherits donor technology and explicitly grants vanilla `elephantry`; no custom Event 014 technology tree exists. Required Technology Tree Viewer is unavailable. |
| AI | Source pass; quantitative evidence blocked | Four self-removing origin profiles are wired in `common/ai_strategy/014_cannibalism_warlords.txt`; required auditor and useful probability adapter are unavailable. |
| Formables and cosmetics | Pass for implemented scope | No `common/formable_countries` Event 014 suite; runtime transformations use dynamic country creation, `change_tag_from`, and cosmetic tags CBL_CENTRAL_COMMAND, CBL_HOST_CONFEDERATION, CBL_RITUAL_STATE, and ZZZ_CANNIBALISM_HANNIBAL. |
| Player-control safety | Source pass | Human candidates are selected first for unified and Wendigo host selection; dual-human displacement is refused and human donor control is preserved through achievement ledgers and `change_tag_from`. |
| Release and cleanup | Source pass | Warlord release clears slot flags, state/core/template/actor references, and reusable slot bookkeeping. |

## File surface checklist

- Tags: `common/country_tags/014_cannibalism_countries.txt`.
- Country definitions: `common/countries/Cannibal Warlord Slot CBA.txt` through `CBH.txt`, `common/countries/Cannibal Unified Host CBL.txt`, and `common/countries/cosmetic.txt`.
- Histories: `history/countries/CBA - Cannibal Warlord Slot.txt` through `CBH - Cannibal Warlord Slot.txt`, `history/countries/CBL - Cannibal Unified Host.txt`, and `history/countries/ZZZ - Zombie Outbreak.txt`.
- Characters: `common/characters/014_cannibalism_characters.txt` and `common/characters/ZZZ.txt`.
- Focus: `common/national_focus/014_cannibalism_focus.txt`.
- Events and scripted systems: `events/014_cannibalism.txt`, `common/scripted_effects/014_cannibalism_effects.txt`, `common/scripted_triggers/014_cannibalism_triggers.txt`, and `common/on_actions/014_cannibalism_on_actions.txt`.
- Decisions and ideas: `common/decisions/014_cannibalism_decisions.txt`, `common/decisions/categories/014_cannibalism_categories.txt`, `common/ideas/014_cannibalism_ideas.txt`, and `common/ideas/014_cannibalism_cxt_extension_ideas.txt`.
- Units and setup: `common/units/014_cannibalism_irregular_infantry.txt`, `history/units/014_cannibalism_dormant.txt`, and `common/scripted_effects/014_cannibalism_cxt_test_effects.txt`.
- AI and constants: `common/ai_strategy/014_cannibalism_warlords.txt`, `common/ai_strategy/ZZZ.txt`, and `common/script_constants/014_cannibalism_constants.txt`.
- Localisation and scripted localisation: `localisation/english/014_cannibalism_l_english.yml` and `common/scripted_localisation/014_cannibalism_scripted_localisation.txt`.
- GUI and sprite wiring: `interface/014_cannibalism.gfx` and `interface/014_cannibalism_frontline_hunger.gui`.

## Map, state, claims, and territory findings

Warlord state selection is dynamic rather than tied to a new Event 014 map region. `cannibalism_select_warlord_candidate_state` scores eligible state nodes, while `cannibalism_create_selected_warlord_country_from_current_state` validates the selected state, origin, slot, former owner control, and usable neighbours before transfer. `cannibalism_prepare_warlord_creation_context` maps supported continents to regional identity and scales population, units, experience, and frenzy.

The supported-region trigger covers Europe, Asia, Africa, Middle East, North America, South America, and Australia, with Australia mapped to Oceania identity. Formation preflight rejects unsupported regions, so the unknown-region fallback is not an ordinary formation path.

The transfer logic cores the origin and selected neighbouring territory, assigns the origin capital, avoids recovery/unusable states, and later clears runtime references on release. The main residual risk is engine iteration order for `every_neighbor_state`; this affects deterministic neighbour choice but was not safe to alter without a map-design request.

HOI4 MCP map inspection covered existing state ranges 1-10 and 219-226 and rendered the state/port/VP/building/supply/railway layers. Event 014 has no custom state definitions to inspect. Global map validation is contaminated by unrelated existing `map/buildings.txt` diagnostics (`MAP_BUILDING_POSITION_INVALID` and `MAP_PORT_ADJACENT_SEA_INVALID`), so map evidence is partial rather than a package-wide pass.

## Politics, leaders, portraits, parties, flags, and advisors

The eight slots begin dormant with neutral ruling parties, no public country leader, and no research slots. Warlord setup creates a dynamic leader with ritual-predation ideology, an origin trait for Island Reaver, Siege Butcher, or March Predator, a regional name pool, and a dynamic portrait key of the form `GFX_portrait_[slot]_warlord_[region]`. Current pools are male-presenting and no female leader metadata is set.

CBL history attaches `CBL_hannibal` without a public role, and ZZZ history attaches `ZZZ_hannibal_wendigo` without a public role. The role is promoted only after the reveal or Wendigo merge. This prevents source-level pre-reveal event text, but the roleless character attachment should be confirmed in live engine behavior because portrait/name visibility semantics are not proven by source review.

The active localisation has CBA-CBH dynamic country, adjective, party, origin, leader, idea, focus, decision, and cosmetic keys. A read-only key audit found zero missing keys for 140 decision IDs and the checked Event 014 idea IDs; MCP found all 68 warlord, 108 unified, and 28 Wendigo focus titles resolved.

The runtime flag inventory is:

| Family group | Families | Variants per family | Sizes | Files |
| --- | ---: | ---: | ---: | ---: |
| Reusable slots | CBA-CBH (8) | 5 | 3 | 120 |
| Unified base | CBL (1) | 5 | 3 | 15 |
| Unified cosmetics | CBL_CENTRAL_COMMAND, CBL_HOST_CONFEDERATION, CBL_RITUAL_STATE (3) | 5 | 3 | 45 |
| Wendigo cosmetic | ZZZ_CANNIBALISM_HANNIBAL (1) | 5 | 3 | 15 |
| Total | 13 | 5 | 3 | 195 |

The flag audit found 65 files in each of `gfx/flags`, `gfx/flags/medium`, and `gfx/flags/small`, with 65 unique SHA-256 hashes within each size. Representative files are uncompressed 32-bit alpha TGAs at 82x52, 41x26, and 10x7. Parent visual review of root-size CBA-CBH and CBL family designs found no immediate flat-vexillological rejection.

Flag provenance is repository-verifiable. The bulky `docs/assets/014_cannibalism/flags_refresh` source package was compacted out of the current worktree, but Git revision `894037493` preserves all 204 package files. Its `generation_evidence.json` contains 65 separate `built-in-imagegen` records for CBA-CBH, CBL, the three CBL cosmetics, and `ZZZ_CANNIBALISM_HANNIBAL`; its manifest, prompts, source PNGs, processed PNGs, contact sheets, and validation remain inspectable at that revision. A direct Git byte comparison reports zero differences across the 195 current runtime TGAs. The corrected handoffs use only the active CBA-CBH roots. The older regional-duplicate portrait lists are superseded by the explicit user deletion set described below; they are not a current portrait blocker.

No dedicated Event 014 advisors, high-command members, or theorists were found. This may be intentional because the design uses internal roleless characters and command ideas, but it remains a design confirmation item rather than a safe local patch.

## Portrait asset matrix

The deliberate contract in `interface/014_cannibalism.gfx` exposes eight stable sprite tokens per CBA-CBH slot: the default token, the Europe token, and Asia, Africa, Middle East, North America, South America, and Oceania tokens. Those 64 warlord tokens intentionally alias the retained 16 warlord DDS files in `gfx/leaders/014_cannibalism/` so existing dynamic leader keys remain stable without retaining regional duplicates.

The same interface file references `gfx/leaders/014_cannibalism/hannibal.dds` for `GFX_portrait_CBL_hannibal` and `gfx/leaders/014_cannibalism/hannibal_wendigo.dds` for `GFX_portrait_ZZZ_hannibal_wendigo`; both mandated files are present. The two sheet DDS files are also present for their existing sheet consumers.

The explicit user-requested deletion set is the literal 40-path list in `C:\Users\klimp\.codex\attachments\a7053e76-7615-4866-a805-459517d4d734\pasted-text.txt`. The set contains retired regional duplicates grouped as CBA=5, CBB=6, CBC=5, CBD=5, CBE=4, CBF=4, CBG=7, and CBH=4; the audit confirmed all 40 paths are absent from `gfx/leaders/014_cannibalism/`.

Every `texturefile` reference in `interface/014_cannibalism.gfx` was re-audited against the repository: 527 unique references, zero missing paths. The portrait subset contains 66 sprite definitions (64 CBA-CBH warlord tokens plus CBL and ZZZ Hannibal tokens), and every referenced texture exists. This is the intended alias design, not a missing-portrait defect, and no portrait production or gameplay patch is required for this correction.

## Focus, decision, idea, and asset findings

MCP focus inspection and rendering data found:

- `cannibalism_warlord_focus_tree`: 68 focuses, 68 resolved titles, 79 connectors, zero crossings, zero node intersections, and zero blocking diagnostics.
- `cannibalism_unified_focus_tree`: 108 focuses, 108 resolved titles, 103 connectors, zero crossings, zero node intersections, and 18 non-blocking layout warnings (`FOCUS_LAYOUT_LINEAR_DETOUR` and one `FOCUS_LAYOUT_ZIGZAG_CHAIN`).
- `cannibalism_wendigo_focus_tree`: 28 focuses, 28 resolved titles, 28 connectors, zero crossings, zero node intersections, and zero blocking diagnostics.

The unified tree is gated to CBL, `cannibalism_unified_country`, and `cannibalism_reveal_complete`; the Wendigo overlay is separately gated to the ZZZ Wendigo identity and reveal state. Four origin overlays are embedded in the warlord tree, matching the three active origins plus shared route content without introducing a Prison Host branch.

Decision IDs, ideas, icons, localisation, and the deliberate portrait alias coverage are present in source. No focus, decision, portrait, or gameplay patch was justified by the MCP/source audit.

## Starting military, technology, industry, supply, and production

`cannibalism_setup_current_warlord_country` inherits donor technologies, explicitly sets infantry weapons, support, engineers, recon, motorized, marines, military police, artillery, and vanilla `elephantry`, then creates scaled units, reinforcement, ideas, and locked starting templates. The setup also applies origin-specific supply/production behavior through the Island, Siege, and March AI profiles.

`common/units/014_cannibalism_irregular_infantry.txt` defines nine Event 014 irregular families: `scavenger_warband`, `feast_guard`, `feast_cohort`, `bone_guard`, `bone_riders`, `island_reavers`, `siege_eaters`, `march_predation_column`, and `network_cadre`. All are currently `active = no`, use the registered equipment contract, and carry low-org/high-supply irregular balancing. March templates gate motorized equipment.

`common/scripted_effects/014_cannibalism_cxt_test_effects.txt` registers the nine custom subunit tokens and four existing vanilla equipment tokens through the CXT extension contract. Startup and daily-CXT registration hooks are present. Templates are locked and `force_allow_recruiting = no` is used by the setup, so activation/recruitment behavior remains a live engine-semantic risk and was not altered without a focused military-design request.

The installed MCP technology route can inspect vanilla `elephantry` and the broad sub-unit scan, but the package exposes no Technology Tree Viewer. The `elephantry` trace/unlock/lint calls were partial with helper projections deferred, and the render timed out. No custom Event 014 technology file exists to repair.

## AI and playability

`common/ai_strategy/014_cannibalism_warlords.txt` defines self-removing common, Island, Siege, and March profiles. The profiles cover army/template/role selection, Island convoy/naval production and screening, Siege artillery/arms factories/bunkers, and March motorized/infrastructure/spare-unit priorities.

The required `chaosx_ai_probability_auditor` is not callable in this environment. The generic `hoi4_probability_inspect` call against `common/ai_strategy/014_cannibalism_warlords.txt` returned `PROBABILITY_SOURCE_DISCOVERED` with `no_weighted_surfaces`, zero candidates, and no available adapters; initial focus/decision/AI probability calls timed out. Therefore no quantitative AI balance, sweep, simulation, or before/after comparison is claimed, and no AI weight was patched.

## Unified Hannibal and outcome logic

`cannibalism_select_unification_host` scores viable candidates after selecting human countries first, then uses deterministic country ID tie-breaking. `cannibalism_is_viable_unification_host` requires a non-capitulated warlord with a controlled capital/core and valid logistics.

`cannibalism_create_unified_country_from_selected_host` preserves human control through the achievement ledger and `change_tag_from`, unions donor technology and `elephantry`, transfers capital/territory/troops/wars, applies CBL identity/politics/ideas/templates/recruitment, promotes `CBL_hannibal`, loads the unified focus tree, and rebuilds response references.

Submission, surrender, autonomy, resistance, and challenge outcomes have separate source paths. Submission keeps command, surrender creates a servant disposition, autonomy creates a subject, resistance fortifies and declares war, and challenge uses the personal-tyranny/division checks. Human donor control is not displaced by AI host selection.

## Wendigo preservation and transformation

Wendigo host selection also chooses human candidates first, scores divisions/states/population, and ties deterministically. It rejects capitulated, invalid, non-ZZZ, non-Wendigo, Hannibal, and world-end hosts.

`cannibalism_create_wendigo_unification_from_selected_hosts` refuses dual-human displacement, preserves ledgers, sets the reveal state before transform, and calls the identity-preservation contract. `cannibalism_prepare_wendigo_merge_identity` keeps the original ZZZ ledger, sets `ZZZ_CANNIBALISM_HANNIBAL`, retires the old ZZZ leader, promotes `ZZZ_hannibal_wendigo`, opens inherited recruitment, preserves origin specialist/legion/bone-guard/elephantry flags and caps, and locks the original Pack contract.

Anchor creation consumes exact population through the Deaths transaction, registers source/generation/strength flags, rebuilds runtime references, and respects anchor min/max and route/recovery conditions. Pack training checks anchor state, capacity, larder cost, and population cost before adding manpower/equipment and creating `Wendigo Pack` with start factors. The countdown requires the winter network, route, chaos/population, anchors, authority/larder, and victory/progress conditions; the lock path requires terminal progress and then clears runtime, applies the terminal idea, and locks anchor states. `cannibalism_process_wendigo_transformation_pulse` is the sole pulse path found.

## Event and GUI evidence

Narrow Event 014 MCP inspection/rendering was run for `chaosx.nr14.1`, `chaosx.nr14.70`, and `chaosx.nr14.72`. The result was `EVENT_INSPECTED_PARTIAL` with 9,513 events, 14,705 options, 1,071 entries, zero blocking diagnostics, and deferred large-workspace lifecycle/helper analysis. Narrow overview/options artifacts were emitted as event-trace, event-overview, and event-options JSON/SVG/PNG resources; global counts include unrelated workspace content and must not be read as an Event 014-only proof.

The dedicated GUI route was attempted for `cannibalism_network_window` and the frontline-hunger layout, but generic scenario inspection and rendering timed out after 180 seconds. No visual GUI pass is claimed. Source windows include `cannibalism_early_header_window`, `cannibalism_network_window`, `cannibalism_warlord_command_window`, `cannibalism_revealed_command_window`, and the Wendigo surface in `interface/014_cannibalism_frontline_hunger.gui`.

## Flag, portrait, and pre-reveal conclusions

The 195-file flag matrix is installed and dimension/format/hash-unique per size. Repository-backed ImageGen provenance and source-master evidence are preserved at Git revision `894037493`, and every installed runtime flag matches that checkpoint. No Meshy provider task or live `@meshy-ai/meshy-mcp-server` process is owned or used by this country audit.

The portrait matrix is intentionally consolidated: 64 CBA-CBH regional/default sprite tokens resolve to 16 retained warlord DDS files, and the mandated Hannibal/Wendigo DDS files are present. The 40 retired regional duplicates listed in the user attachment are absent by request, and all interface texture paths resolve.

Active source/localisation search found no `ancient general`, Carthaginian, Punic, or ancient-general disclaimer exposure. Reveal names and text in `localisation/english/014_cannibalism_l_english.yml` and events `.70/.72` are gated by the unified/Wendigo identity, reveal flag, and promoted character role. The roleless history attachments described above are the only remaining pre-reveal concern.

## MCP and validation record

- Focus MCP: validated all three trees; artifacts were emitted under `focus-inspect` resources for `cannibalism_warlord_focus_tree`, `cannibalism_unified_focus_tree`, and `cannibalism_wendigo_focus_tree`.
- Event MCP: narrow inspect and render completed partially for `.1`, `.70`, and `.72`; large-workspace helper/lifecycle analysis deferred with zero blocking diagnostics in the returned narrow result.
- Map MCP: state inspection for 1-10 and 219-226 plus state-layer render with coastlines, ports, victory points, buildings, supply nodes, and railways completed; global unrelated building/port diagnostics prevented a clean workspace-wide validation claim.
- Technology MCP: broad sub-unit scan and `elephantry` trace/unlocks/lint completed partially; technology render timed out, and the installed package has no Technology Tree Viewer.
- Probability MCP: AI source discovery completed but reported no weighted surfaces; required custom probability auditor unavailable, so no scenario-weight conclusion is claimed.
- Source checks: tag inventory, active-origin search, country/history pairing, dynamic state/claim/cleanup paths, leader/party/localisation references, unit/CXT registration, cosmetic tags, and event reveal gates were read-only audited.
- Asset checks: 13-family flag inventory, per-size file counts, SHA-256 uniqueness, ffprobe dimensions/pixel format, and representative TGA alpha headers were checked; all 527 interface texture references, 66 portrait sprite definitions, retained DDS files, and all 40 user-requested deletion paths were checked.
- Live HOI4 launch and in-game validation were not run by policy. The roleless-character visibility, custom-unit activation, GUI presentation, and final portrait identity remain live/runtime checks for the parent/user.

## Changed files and patch disposition

Changed files: `docs/plans/014_cannibalism_plans/subagent_handoffs/event014_country_final_audit_v4.md` only.

Changed tags, states, leaders, parties, focus IDs, localisation keys, formables, AI values, and assets: none.

Before/after gameplay and asset behavior: unchanged. No gameplay patch was required because the source tag, slot, origin, transfer, reveal, cleanup, focus, localisation, player-control, flag, and deliberate portrait-alias paths are already wired.

## Blockers, risks, and follow-up ownership

- P1 evidence blocker: run the required `chaosx_ai_probability_auditor` and named scenario comparison once the route is available; do not tune the four AI profiles from source-only weights.
- P1 evidence blocker: obtain a working GUI scenario and render route for the frontline-hunger windows.
- P1 evidence blocker: install/expose the Technology Tree Viewer or record that limitation in the parent release packet; validate custom-unit activation/recruitment in a live consumer pass.
- P2 design warning: confirm whether roleless CBL/Wendigo character attachments are invisible before promotion and whether the no-advisor design is accepted.
- P2 map warning: unrelated global `map/buildings.txt` diagnostics should be repaired by the map owner; they prevented a package-wide map validation claim but did not identify an Event 014 custom state defect.

No simplification was silently substituted for the requested country package. The remaining omissions are explicitly listed above.
