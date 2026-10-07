# Event 006 Regional Focus Integration Review

**Disposition:** bounded read-only integration audit of the accepted 44 Level 2 shared-focus groups. The review did not modify gameplay source or commit files. The A/B worker handoffs remain partial worker records, not whole-event completion claims.

**Scope:** `common/national_focus/006_independence_wave_regional_focus_a.txt` and `common/national_focus/006_independence_wave_regional_focus_b.txt`, their 220 focus references in `common/national_focus/006_independence_wave_focus.txt`, the nine regional decision files, the narrow framework identity/cleanup helpers, and the paired focus localization/icon wiring. Signature modules and formables were excluded as directed.

## Route coverage

| Tranche | Groups | Tags | Required route | Source coverage |
| --- | ---: | --- | --- | --- |
| A, three-project groups | 18 | CUX, PAL, DUX, UGA, RWA, BRD, HAR, SOM, TIG, BAR, MAD, FDX, SIN, BLC, PSH, KAS, HYD, MYS | Opener, two compatible projects, paid host support, regional congress cap | 90/90 foci present |
| A, four-project groups | 4 | IMO, LEB, RIF, DSX | Four paid project nodes with the accepted local fork/convergence, then regional congress cap | 20/20 foci present |
| B, three-project groups | 22 | RAS, FOX, MPU, ATJ, FUX, BLI, GCX, IAX, IBX, LAO, GMX, MEN, OKN, SAM, QUE, GZX, HCX, YUC, ATX, CLX, CIN, DAG | Opener, two sibling projects, paid host reinforcement, regional congress cap | 110/110 foci present |

The two source files contain 220 unique `shared_focus` IDs, exactly five for each of 44 tags. The owning `independence_wave_focus_tree` references all 220 IDs exactly once, from line 57 through line 307 of `common/national_focus/006_independence_wave_focus.txt`. No direct-focus fallback duplicates were found.

The A alternatives use OR prerequisites for the IMO Treaty of Seeb/coast-road choice and the LEB National Pact/Civic Charter choice. Their downstream convergence is reachable after either option. The other convergence focuses use separate prerequisite blocks for both compatible project branches, so those paths are AND gates. B host reinforcement convergences also require both sibling projects.

## Integration findings

All 136 project focus/paid-decision pairs resolve to one decision definition in the nine regional decision files. Each focus blocks while its paired decision is active, calls the same completion helper as that decision’s `remove_effect`, bypasses on the helper’s project receipt, and guards completion against a second payment. The helper sets the focus bypass receipt in every audited pair; no missing decision, helper, or result receipt was found.

The two intentional alternative pairs have symmetric `mutually_exclusive` links and decision-side locks against starting the opposing focus while it is in progress or complete: `independence_wave_imo_focus_renew_the_treaty_of_seeb` / `independence_wave_imo_focus_close_the_coast_road`, and `independence_wave_leb_focus_apportion_the_great_offices` / `independence_wave_leb_focus_open_offices_to_every_citizen`. The checks are in the focus source around lines 322–405 and 521–606, with decision interlocks in `common/decisions/006_independence_wave_levant_arabia_decisions.txt`.

A’s groups use `is_independence_wave_regional_framework_live`, which requires the exact admitted carrier, current framework generation, setup receipt, Event 006 origin, and a non-ended origin; each focus also checks its expected `original_tag`. The carrier list pairs each package ID with its original tag in `common/scripted_triggers/006_independence_wave_regional_framework_triggers.txt:19-94`, and generation matching is in `:97-110,217-229`. B’s shared gate is in `common/scripted_triggers/006_independence_wave_regional_focus_b_triggers.txt:7-11`; each of the 22 package predicates checks its exact package variable and original tag in the region-specific package trigger file.

The A host-support helper selects one package-specific delta set for each of its 18 supported tags and has a domestic fallback when the former host is gone. The B host-reinforcement effect branches across all 22 B package predicates. Cleanup is wired through `independence_wave_clear_focus_runtime` at `common/scripted_effects/006_independence_wave_focus_effects.txt:104-108`; the generic cleanup calls that helper from `common/scripted_effects/006_independence_wave_effects.txt:477,3139`. A’s support receipt and B’s support flag/generation variable are cleared there.

The regional congress caps and generic route are idempotent. `independence_wave_survey_regional_ambition` bypasses after ambition is opened, `independence_wave_call_regional_congress` bypasses after the shared congress flag, and its reward is guarded at `common/national_focus/006_independence_wave_focus.txt:1980-2033`. The regional caps set the same congress flag only when it is absent and open ambition only when needed. No second diplomatic-step reward is granted by the country-specific cap.

## Definite fixes, ordered by priority

1. **Resolve the duplicate global congress localization key.** `independence_wave_regional_congress_called` is defined as “The regional congress has been called” in `localisation/english/006_independence_wave_regional_focus_a_l_english.yml:7` and “A regional congress has been called.” in `localisation/english/006_independence_wave_regional_focus_b_l_english.yml:17`. Keep one canonical value or make both definitions identical.

2. **Remove conflicting generic copies of existing B receipt labels.** The B localization file defines 66 receipt-flag keys as “The matching project is already complete.” Twenty-one of those keys already have country-specific text in the regional decision localization files. Examples are `independence_wave_fox_assembly_seated` (B file line 39 versus `006_independence_wave_south_asia_l_english.yml:185`), `independence_wave_atj_notables_convened` (B line 75 versus `006_independence_wave_east_asia_oceania_l_english.yml:34`), and `independence_wave_hcx_legislature_seated` (B line 309 versus `006_independence_wave_americas_l_english.yml:72`). The conflicting keys are `independence_wave_fox_assembly_seated`, `independence_wave_mpu_durbar_convened`, `independence_wave_atj_notables_convened`, `independence_wave_fux_council_joined`, `independence_wave_bli_paruman_convened`, `independence_wave_gcx_council_bound`, `independence_wave_iax_council_seated`, `independence_wave_ibx_duwas_convened`, `independence_wave_lao_provinces_united`, `independence_wave_gmx_delegates_convened`, `independence_wave_men_council_convened`, `independence_wave_okn_assembly_seated`, `independence_wave_sam_fono_convened`, `independence_wave_que_assembly_seated`, `independence_wave_gzx_assembly_restored`, `independence_wave_hcx_legislature_seated`, `independence_wave_yuc_congress_seated`, `independence_wave_atx_assembly_convened`, `independence_wave_clx_khase_convened`, `independence_wave_cin_mekhk_khel_convened`, and `independence_wave_dag_assembly_seated`. Keep the existing country-specific text as the sole definition for those keys; retain a generic label only where no prior label exists.

3. **Differentiate the two DSX congress icons.** `independence_wave_dsx_focus_convene_the_yoruba_towns` at `common/national_focus/006_independence_wave_regional_focus_a.txt:1393` and `independence_wave_dsx_focus_prepare_regional_integration_authority` at `:1439` both use `GFX_goal_independence_wave_league_congress`. The town-council project is visually indistinguishable from the capstone; use another existing civic icon for the project. Other within-group repeats are BRD’s two settlement focuses, FUX’s two civic focuses, GCX’s railway/mining projects, and ATX’s two industrial projects; these are noted for review but their shared theme makes them lower priority.

## Icon coverage

All eight referenced GFX IDs are defined in `interface/006_independence_wave.gfx`, and each referenced DDS exists. No new art or sprite wiring is required.

| GFX ID | A uses | B uses | Coverage |
| --- | ---: | ---: | --- |
| `GFX_goal_independence_wave_founding_administration` | 22 | 21 | Registered DDS |
| `GFX_goal_independence_wave_popular_councils` | 13 | 15 | Registered DDS |
| `GFX_goal_independence_wave_infrastructure_authority` | 19 | 12 | Registered DDS |
| `GFX_goal_independence_wave_army_integration` | 8 | 6 | Registered DDS |
| `GFX_goal_independence_wave_military_emergency` | 2 | 0 | Registered DDS |
| `GFX_goal_independence_wave_former_host_settlement` | 21 | 22 | Registered DDS |
| `GFX_goal_independence_wave_recognition_diplomacy` | 2 | 12 | Registered DDS |
| `GFX_goal_independence_wave_league_congress` | 23 | 22 | Registered DDS |

All focus definitions have an icon, search filters, and `ai_will_do`. The six filters used—Political, Stability, Industry, Manpower, War Support, and Research—are base-game filters and match the main civic, industry, military, and research roles observed in the groups.

## Localisation and reward mapping

All 220 focus title keys, 220 description keys, and 220 completion-tooltip keys exist. The audit checked 1,159 focus-localization and tooltip references and found no missing English key or broken effect-tooltip alias. All 136 project focus rewards call the same completion helper as their paired paid decision, and the helper sets the corresponding focus bypass receipt. No additional title-to-helper mismatch was found in that crosswalk.

The 21 duplicate B receipt labels and the duplicate congress key above are the confirmed localization mismatches. The remaining B receipt labels have no competing English definition in the current localization scan.

## AI behavior

All 220 foci have a base `ai_will_do`; the source uses 43 `urgent`, 137 `high`, and 40 `standard` constants. The two LEB policy roots are both `high` because they are equal mutually exclusive choices. These are role-level weights without focus-local campaign-state modifiers; branch eligibility and completion gates still constrain the candidates.

The required read-only analysis has been delegated to `chaosx_ai_probability_auditor` for all 44 country groups. Its scenario-specific MCP result is still pending, so this report makes no balance or selection-probability conclusion. No AI weights were changed.

## MCP and validation evidence

The live MCP workspace is `mod_chaos_redux_ea3b2d67c2c0`. `hoi4.focus_inspect` and `hoi4.focus_render` on `common/national_focus/006_independence_wave_focus.txt` returned `FOCUS_INSPECTED` and `FOCUS_RENDERED`, each with a passing focus-diagnostics check and no blocking diagnostics. The inspect artifact is `focus-inspect.11aee1edfb4121cb.json` (1,003,233 bytes; SHA-256 `826c1a3f5b06f45330971b43ddce7d88805f7078006ab4b9464e167ceda20d00`). The render returned HTML, SVG, JSON, source-map, and plan artifacts; the source-map is `independence_wave_focus_tree.focus.source-map.json` (98,699 bytes; SHA-256 `908f83dd4c2481acf2e0889f52d0b091e42c3ec51778ed54ee5612a4ee96ca77`). Both inline inventories were truncated to 64 paths (93 for inspect, 92 for render).

Inspecting either regional file alone returned `FOCUS_TREE_NOT_FOUND`, as both contain `shared_focus` blocks rather than a `focus_tree`. The required owner-tree inspect/render succeeded. Attempts to read the linked inspect/source-map artifacts by byte range, including a manifest read, returned the exact resource error `Artifact provenance manifest is unavailable`; therefore the generated graph and rendered layout could not be reviewed visually in this task. This leaves imported-node layout evidence unresolved; the accepted shared-focus architecture was preserved.

Whole-file `hoi4.script_validate` returned `SCRIPT_CHECKED`, `valid: true`, and zero findings for both regional focus files. A checked 2,912 commands and reported 131 argument blocks unchecked; B checked 2,330 commands and reported 218 argument blocks unchecked. Both results state `parametersChecked: false`, so this is syntax/command-kind/scope evidence, not full argument-semantic proof.

The offline wiki references read were `National focus modding - Hearts of Iron 4 Wiki.md:818-838` (shared-focus definition and import behavior), `:455-512` (search filters), and `:604-626` (focus AI), all at revision `bd989a13237c464f140a0aa671cc42c30a48e84a27dae791b8914654fb9c6203`; plus `Triggers - Hearts of Iron 4 Wiki.md:704` (`focus_progress`) at revision `abc51ad18a2c46e46d47baa795c5a840ebaf7c4ae3e777426c64a9f4c0c0ce06`. Installed documentation read `triggers_documentation.md:2882-2891` (`focus_progress`) and `:3501-3509` (`has_completed_focus`) at revision `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29`. The installed documentation has no dedicated national-focus syntax section in the targeted search. Vanilla precedent `game:common/national_focus/baltic_shared.txt:44-93` (`BALTIC_rejoin_the_railways`) was read directly; `hoi4.source_lookup` located its shared-focus source block at revision `781ade82eec9e976ad0f5a81205a992f97ec4b019842e98a05caeff1716013a9`. `hoi4.source_lookup` resolved the framework exact-carrier trigger at `mod:common/scripted_triggers/006_independence_wave_regional_framework_triggers.txt:19-94`, revision `847f24b929a6f616621fe36bbbeaf082903cffc837f160f0696abb3dd612473a`; it did not return a workspace-index definition for a shared-focus symbol.

## Missing content, simplifications, and limits

No required A/B package, focus node, paid-project helper, decision lock, congress hook, focus localization key, GFX definition, or icon DDS was missing in the bounded 220-focus scope. No direct-focus fallback was present. The five-node shared architecture uses existing country-specific paid decisions and effects rather than generic substitute rewards.

The parent integration bullets in `regional_focus_a_20261006.md` are stale for the root imports, decision interlocks, and focus-runtime cleanup, all of which are present in current source. The remaining parent-level evidence gates are the probability auditor result and review of the rendered imported layout artifact. The B handoff’s later parent-review section already records the imported IDs and decision integration.

No focus source was changed, no game executable was launched, no logs were searched, and no Git mutation was made. No improvement-loop plan was written because the bounded routes use country-specific paid projects and the audit found no need to add a route family or expand the accepted design.

## Skills used

Read and applied `chaos-redux-focus-trees`, `chaos-redux-events`, `chaos-redux-decisions-missions`, `chaos-redux-event-assets`, `chaos-redux-improvement-loop` (not triggered for plan output), and `chaos-redux-subagents`. No skills were created or modified.

### Focus artifact resource URIs

- Inspect JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/826c1a3f5b06f45330971b43ddce7d88805f7078006ab4b9464e167ceda20d00/12e7a0565a0ea39f936231177c3de6d3813e42b891af4d57184b1e35e6672338/focus-inspect.11aee1edfb4121cb.json`.
- Render HTML: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/56f860f05545991122d48512d0de3f260d73ec730cfc0f9272ea9bc1fa697477/e07097d8ee1ef17475816e8ed8a66d5a7e003ee4d1db52d956012261fa21deed/independence_wave_focus_tree.focus.html`.
- Render SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a0a85cff2d86e55b30bc8bd1f269dc0778467a568331ce2f0cf773eac62fe149/0ca40fe80f34f56735cb40336c643663100fe1fc984b25e0b6df13eb98a783d0/independence_wave_focus_tree.focus.svg`.
- Render JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a7b31572b86a2c18135766e0be6410a4c4e39fb23781a6243153d176900cc47b/4cc9225f83bce8c1e716f9e849f1061fc34894a84a6602611831b8295ae0397f/independence_wave_focus_tree.focus.json`.
- Source map: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/908f83dd4c2481acf2e0889f52d0b091e42c3ec51778ed54ee5612a4ee96ca77/b25ef5643f641b2e1fdf3e7d643b1bfa6c5855f2b2a86ee5e90c9e1a9f541d81/independence_wave_focus_tree.focus.source-map.json`.
- Planning metadata: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bbb5250ec8f32a55d9657e23fdf8025681d7f0c095273e52b597113166a9a115/8e3e0b959e41ec10e84b32b222debba5c102adb21fafeecf8e9d34691c696f6f/independence_wave_focus_tree.focus.plan.json`.

Both the offset/length reads and the manifest query returned `Artifact provenance manifest is unavailable`.
