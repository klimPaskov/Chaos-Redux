# Event 006 IW-093 / IW-098 country-package audit handoff — 2026-07-18

**Scope:** Asante (`DOX`, IW-093, state 274/Kumasi, high-chaos-only) and Sokoto (`SOK`, IW-098, state 902, dormant/automatic-if-not-living). This audit covers the current foundational package tranche, the accepted signature-package addendum, the region-09 reservation/dispatch layer, and the Event-012 separation contract.

**Verdict:** Both packages remain **fail-closed and not runtime-admitted**. The tranche has bounded package triggers/effects, focus branches, paid decisions, staged ideas, localisation, and AI strategy profiles, but it does not set either runtime content-attestation flag. Neither package is in the normal release/scenario attested set. No fallback identity, portrait, flag, advisor, force, or succession surface was invented.

## Package coverage checklist

| Surface | IW-093 Asante / `DOX` | IW-098 Sokoto / `SOK` |
|---|---|---|
| Tag and shell | New `DOX` registration and African graphical shell in `common/country_tags/006_independence_wave_countries.txt` and `common/countries/006_independence_wave_DOX.txt`; dormant history shell has no fixed setup. | Vanilla `SOK` is deliberately reused; no mod country-tag or duplicate history file. Vanilla shell is `common/countries/Sokoto.txt`. |
| Origin and admission | Exact `DOX` origin proof, Soviet/Event-006-origin exclusion, high-chaos-only region weight, and RG-GHANA-ASANTE-FANTE reservation. Planner still requires the legacy `independence_wave_package_content_ready`; runtime attestation remains absent. | Exact `SOK` dormant/not-living proof, Soviet/Event-006-origin exclusion, RG-NIGERIA-COARSE reservation, and Event-012 safety gate. Planner still requires the legacy content-ready flag; runtime attestation remains absent. |
| Anchor and capital | Fixed state `274`; Kumasi VP `12787` is recorded in constants. Setup/final validation require the frozen anchor to be owned/controlled and capital. | Fixed state `902`; vanilla Sokoto VP `1891` and SOK core are present in the installed map. Setup/final validation require the frozen anchor to be owned/controlled and capital. |
| Host survival | Former host must exist, not be `ROOT`, and retain an owned capital. | Same host-survival proof. |
| Focus | 21 package focuses, imported by `common/national_focus/006_independence_wave_focus.txt`; constitutional/royal/veterans branches and FORM-24 preparation are route-gated. | 22 package focuses, imported by the same tree; sultanic/northern/frontier branches and FORM-25 preparation are route-gated. Full framework assignment excludes Event 012. |
| Decisions | 8 paid/timed actions in the Asante category; receipts and state-control checks are present. | 8 paid/timed actions in the Sokoto category; receipts and state-control checks are present. |
| Ideas | Two staged ideas, added by package setup/decision helpers and removed by cleanup. | Two staged ideas, added by package setup/decision helpers and removed by cleanup. |
| AI | Five package strategy profiles, enabled only after active package setup. | Five package strategy profiles, enabled only after active package setup. |
| Identity/forces/assets | No country leader, commander, OOB, production, portrait, or flag is shipped; focus/decision/category/idea icon registrations and DDS files are present. | Vanilla Siddiq is the only existing country character; no Event-006 Hasan pre-cutover role, package force setup, new production, exact period flag, or portrait is shipped. Focus/decision/category/idea icon registrations and DDS files are present. No advisor content is in scope. |
| Formable | FORM-24 profile can load and the focus unlocks a preparation decision; no FORM-24 family readiness/identity/integration adapter or commit path exists. | FORM-25 profile can load and the focus unlocks a preparation decision; no FORM-25 family readiness/identity/integration adapter or commit path exists. |
| Runtime status | `independence_wave_iw093_runtime_content_attested` is not set anywhere in this tranche. | `independence_wave_iw098_runtime_content_attested` is not set anywhere in this tranche. |

## File-surface checklist

The reviewed package surface is present and internally connected:

- `common/country_tags/006_independence_wave_countries.txt` (`DOX` only; `SOK` remains vanilla).
- `common/countries/006_independence_wave_DOX.txt` and `history/countries/DOX - Event 006 Country Shell.txt` (dormant Asante shell).
- Vanilla `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\countries\Sokoto.txt` and `history\countries\SOK - Sokoto.txt` (vanilla Sokoto shell/history).
- `common/script_constants/006_independence_wave_iw093_iw098_constants.txt` (anchors, values, thresholds, costs, timing, AI weights, idea modifiers).
- `common/scripted_triggers/006_independence_wave_iw093_iw098_package_triggers.txt` (candidate/origin/anchor/capital/host/values/formable/Event-012/date gates).
- `common/scripted_effects/006_independence_wave_iw093_iw098_package_effects.txt` (central setup/final-validation/cleanup, date hook, focus configuration).
- `common/national_focus/006_independence_wave_iw093_iw098_focus.txt` and `common/national_focus/006_independence_wave_focus.txt` (package focuses and two import roots).
- `common/scripted_effects/006_independence_wave_iw093_iw098_focus_effects.txt` (focus rewards, route receipts, cleanup).
- `common/decisions/categories/006_independence_wave_iw093_iw098_categories.txt`, `common/decisions/006_independence_wave_iw093_iw098_decisions.txt`, and `common/scripted_effects/006_independence_wave_iw093_iw098_decision_effects.txt` (categories, 16 actions, paid ledgers).
- `common/ideas/006_independence_wave_iw093_iw098_ideas.txt` (four staged ideas).
- `common/ai_strategy/006_independence_wave_iw093_iw098_ai_strategy.txt` (ten package profiles).
- `interface/006_independence_wave_iw093_iw098_{focus,decisions,categories,ideas}.gfx` and `gfx/interface/{goals,decisions,ideas}/006_independence_wave/iw093_iw098/` (package icon registrations and DDS files).
- `docs/assets/006_independence_wave/iw093_iw098_icons_2026_07_18/gfx_handoff.md` (57-row icon manifest, dimensions, runtime paths, hashes, and no-flag/no-character scope).
- `localisation/english/006_independence_wave_iw093_iw098_{focus,decisions,categories,ideas}_l_english.yml` (player-facing package text).
- `common/scripted_effects/006_independence_wave_package_dispatch_effects.txt` and `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt` (central dispatch and runtime admission list).
- `common/scripted_effects/006_independence_wave_packages_region_09_effects.txt` and `common/scripted_triggers/006_independence_wave_packages_region_09_triggers.txt` (region loaders, automatic weights, reservations, fixed anchors).

## Tag, origin, and lifecycle findings

1. `DOX` is a new X-ending Event-006 tag and is registered only once. Its exact package helper requires `original_tag = DOX`, `exists = no`, the current reserved-country proof, Event-006 origin, and exclusion of Soviet-collapse and other Event-006 origins.
2. `SOK` is not registered by the mod, which is correct for the accepted dormant-vanilla reuse. Its exact helper requires the living tag to be absent and the same origin exclusions. A living vanilla SOK is never overwritten by this path.
3. `is_independence_wave_iw093_candidate_preflight` and `is_independence_wave_iw098_candidate_preflight` require both the exact tag proof and the legacy `independence_wave_package_content_ready` flag. No current IW-093/IW-098 file grants that flag.
4. `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt` lists runtime adapters for package IDs 93/98, but its compile-time attestation OR deliberately excludes both IDs. The scenario preflight therefore also excludes them. This is the intended fail-closed result.
5. Setup is dispatched after the shared frozen release ledger transfers the anchor and sets the country capital. Final validation requires active provenance, setup, focus framework, signature module, formable profile registration, capital/host survival, values, ideas, and package runtime attestation. Cleanup removes package decisions/focus receipts, staged ideas, values, route/formable selection flags, and reloads `generic_focus` only when the Event-006 tree is actually loaded.

## Map and state setup

- Vanilla state `274-British Africa.txt` is owned by `ENG`, contains Kumasi VP `12787`, and is the accepted Asante anchor. The package constants and region-09 reservation publisher use `274`; the Kumasi capital proof also requires `is_capital = yes` after frozen setup.
- Vanilla state `902-Sokoto.txt` is owned by `ENG`, has Sokoto VP `1891`, and contains a vanilla `SOK` core. The live package loaders, triggers, reservation publisher, and setup/final validation all use `902`.
- The public candidate registry still records IW-098's old baseline anchor as `558`. The installed-map binding/audit, accepted addendum, region-09 scripts, constants, and live package all override that stale public row to dedicated state `902`. Do not reintroduce `558` into the current package.
- `RG-NIGERIA-COARSE` and current-map collision records correctly prevent IW-098 and IW-100 from reserving state 902 in the same automatic wave. `RG-GHANA-ASANTE-FANTE` prevents the coarse Asante/Fante collision.
- The former-host proof requires an existing non-`ROOT` host with at least one owned capital. This prevents a release from silently destroying the host's country state.
- **Patch applied:** `independence_wave_iw098_secure_caravan_approaches` in `common/national_focus/006_independence_wave_iw093_iw098_focus.txt` now requires `902 = { is_owned_by = ROOT is_controlled_by = ROOT }` in `available`. Its reward helper in `common/scripted_effects/006_independence_wave_iw093_iw098_focus_effects.txt` has the same state gate before adding infrastructure. Before the patch a focus could be started/rewarded against a lost anchor; after it, the focus is unavailable and the reward is inert unless Sokoto still owns and controls state 902.

## Politics, leaders, portraits, flags, advisors, and parties

- `DOX` has only graphical culture, colour, and country-name localisation (`DOX`, `DOX_DEF`, `DOX_ADJ`, ideology variants). It has no `set_politics`, party names, country leader, commander, character, ideology-popularity, law, or starting production surface. The accepted identity requires Prempeh II and a researched 1935 Asante Confederacy bridge; that leader surface remains absent.
- Vanilla SOK history starts neutral with 75% neutrality, `capital = 902`, `infantry_weapons = 1`, no SOK-specific OOB, and `recruit_character = SOK_siddiq_abubakar`. Vanilla SOK localisation/party names and `SOK_siddiq_abubakar` are available, but this is not sufficient for the accepted Event-006 date contract.
- The accepted IW-098 contract requires Hasan dan Mu'azu Ahmadu before 17 June 1938 and Siddiq Abubakar III on/after 17 June 1938. The current `independence_wave_iw098_select_sultan_by_date` helper clears/sets only Event-006 role-selection flags and requires the matching external role-attestation flag; it does not author, replace, or activate either character. A missing pre-cutover leader package is therefore still a hard blocker.
- No `common/characters` or `common/country_leader` file for IW-093/IW-098 exists. There are no package leader portrait paths or `.gfx` registrations. The source/rights handoffs explicitly block Hasan/Siddiq visual completion and the exact period flags. No custom advisor icons, portraits, sprites, dossiers, or advisor mechanics are present or added here, per the accepted scope.

## Focus, decisions, ideas, and assets

- The focus file contains 43 unique package focus IDs (21 IW-093, 22 IW-098); both roots are imported into `006_independence_wave_focus.txt`. Focus prerequisites and route mutual exclusions are present. The FORM-25 focus uses one prerequisite block containing the Sultanic and Northern terminal focuses, which is the intended OR semantics; the frontier route is intentionally excluded by `can_prepare_independence_wave_form25_from_iw098`.
- Localisation coverage is complete at source level for 43/43 focuses, 16/16 decisions, 4/4 ideas, and 2/2 decision categories. The current workspace also contains 35 focus DDS bases plus shine registrations, 16 decision DDS/sprite registrations, 2 category DDS/sprite registrations, and 4 idea DDS/sprite registrations under the package icon directories. The remaining visual blockers are leader portraits and exact period flags, not a missing generic fallback icon.
- The two decision categories expose only when their exact active package predicate is true. All 16 decisions use paid/timed receipts, command/equipment/factory ledgers, state-control checks, cancellation/failure cleanup, and package-local values. They do not create units, grant free equipment, set runtime attestation, or commit FORM-24/25.
- Four ideas represent the opening and completed project states. Their `allowed` blocks accept the exact prepared or active package scopes, matching the setup-time initializer and active lifecycle; cleanup removes both staged variants. Their four package picture sprites are registered and have matching DDS files.
- Focus and decision cleanup removes package flags/receipts and reloads `generic_focus` only for an Event-006 focus tree. Sokoto cleanup intentionally does not clear Event-012's own flags or tree.

## Starting military, technology, industry, supply, and production

- Asante's dormant history shell intentionally has no fixed setup. The current tranche does not provide the required starting leader, army/OOB, templates, stockpiles, manpower, technology, research slots, factories, production lines, trains, convoys, fuel, or supply setup.
- Vanilla SOK provides only `infantry_weapons = 1`, zero convoys, and the vanilla Siddiq recruit; no country OOB or IW-098 package military/economic setup is present. The accepted force mapping calls for a grounded cavalry/veteran/local-infantry core and an emirate-civic defence staff, but no such runtime surface is implemented.
- Decisions and focus effects can improve existing state buildings/values only after package setup and state control. They do not substitute for the missing starting force, technology, industry, or command-roster readiness.

## AI and playability

- The AI file contains ten exact profiles (five per package), all gated by `original_tag` plus the active package predicate. Foundation/host-crisis profiles prioritise infantry/support, infrastructure, army construction, bunkers, and war-restraint; route profiles select recovery/construction or emergency defence.
- These weights are structurally connected to focuses/decisions, but they cannot make either package playable while leader, force, politics, industry, and visual attestation are absent. No command-roster readiness or scenario admission is set.
- The package has no periodic world scan or broad on-action requirement. Balance values and paid costs are centralised in the IW093/IW098 constants file; no free-unit loop was introduced.

## FORM-24 / FORM-25 boundaries

- `common/scripted_effects/006_independence_wave_formable_registry_effects.txt` loads profile rows for `west_african_federation` (FORM-24) and `sahel_confederation` (FORM-25), so package selection can record a profile and minimum member/consent/anchor metadata.
- `independence_wave_formable_register_selected_family_readiness` in `common/scripted_effects/006_independence_wave_form01_02_04_effects.txt` has readiness branches only for FORM-01/02/03/04/05/48. It has no FORM-24 or FORM-25 branch. The generic `has_independence_wave_formable_commit_readiness` and commit triggers likewise have no 24/25 adapter path.
- IW-093 and IW-098 focus effects therefore unlock only package-local preparation/congress decisions. They do not attest family readiness, write identity/flag/integration receipts, freeze members, or commit a formable. This is correctly fail-closed; do not add a formable fallback or a readiness flag in the country package.

## Event-012 separation

`is_independence_wave_iw098_event012_state_safe` excludes `africa_priority_member_package_active`, `africa_priority_member_focus_tree_loaded`, and the Event-012 replacement receipt. Full IW-098 focus assignment requires a generic or existing Event-006 tree and those Event-012 flags absent. Cleanup leaves Event-012's own tree and lifecycle flags untouched and only removes Event-006 generation state. No Event-012 transfer, flag clear, or tree replacement was found in the IW-093/IW-098 tranche.

## Changes made in this audit

1. `common/national_focus/006_independence_wave_iw093_iw098_focus.txt`
   - Identifier: `independence_wave_iw098_secure_caravan_approaches`.
   - Added the state-902 ownership/control proof to focus `available`.
2. `common/scripted_effects/006_independence_wave_iw093_iw098_focus_effects.txt`
   - Helper: `independence_wave_iw098_focus_secure_caravan_approaches`.
   - Added the same state-902 ownership/control proof before the infrastructure reward and receipt flags.
3. `common/ideas/006_independence_wave_iw093_iw098_ideas.txt`
   - Updated the file header so it no longer describes the now-wired picture sprites as unresolved; leader portraits, flags, and advisors remain separate country-package surfaces.
4. Created this handoff; no source-of-truth map, spreadsheet, advisor surface, binary asset file, runtime attestation, succession attestation, command-roster readiness, scenario admission, or formable commit surface was changed.

## Validation and limitations

- Source checks found balanced braces in both touched scripts (`445/445` in the focus file; `194/194` in the focus-effect file), the state-902 gate in both intended locations, no runtime-attestation setter in package focus/decision/idea/AI surfaces, and no missing texture paths in the four package `.gfx` files.
- Cross-file coverage checks found 43/43 focus localisations, 16/16 decision localisations, 4/4 idea localisations, and 2/2 category localisations. The FORM-25 Sultanic/Northern prerequisite remains one OR block.
- Read-only vanilla checks confirmed state 274/Kumasi VP 12787, state 902/Sokoto VP 1891 and SOK core, vanilla SOK neutral history, and the vanilla Siddiq character. Read-only asset checks confirmed all package focus/decision/category/idea sprite registrations resolve to existing DDS files.
- No HOI4 MCP technology-tree viewer is exposed in the installed package, so no technology-tree render/audit was possible. No in-game load, release/save scenario, map rewrite, or runtime formable transaction was run in this subagent scope.

## Remaining blockers / next handoff

Both packages are incomplete for runtime admission. The next implementation tranche must provide, with source/rights evidence and without fallbacks: Prempeh II and date-aware Hasan/Siddiq character/leader surfaces; exact flags and portrait registrations; package politics/parties/laws; starting OOB, templates, stockpiles, technology, industry, production, supply, and command-roster surfaces; FORM-24/25 readiness/identity/integration adapters; and the final country/content audit before setting either runtime attestation flag. Focus/decision/category/idea icon files are present and should be kept wired. Advisor content remains intentionally absent and should not be added as a shortcut.

No simplification or fallback was used. The only gameplay code change is the narrow state-control safety gate described above; the idea-header edit is documentation-only. Both packages remain fail-closed by design.
