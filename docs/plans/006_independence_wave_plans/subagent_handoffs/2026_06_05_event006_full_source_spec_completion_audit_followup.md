# Event 006 Full Source-Spec Completion Audit Follow-up

Audit date: 2026-06-05  
Subagent role: `chaosx_event_completion_auditor`  
Scope: read-only source audit plus this handoff only. No gameplay, localisation, asset, spreadsheet, or existing-doc edits were made.

## Basis Read

- Read `AGENTS.md` first.
- Consulted required offline wiki pages before opening Chaos files: Data structures, Triggers, Effect, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, National focus modding, Country creation, Graphical asset modding, Interface modding, Scripted GUI modding.
- Consulted vanilla docs under `~/projects/Hearts of Iron IV/documentation`, including `effects_documentation.md`, `triggers_documentation.md`, `script_concept_documentation.md`, `modifiers_documentation.md`, and `common/script_constants/documentation.md`.
- Used the required repo skills conceptually: `chaos-redux-events`, `chaos-redux-subagents`, `chaos-redux-improvement-loop`, `hoi4-focus-trees`, `hoi4-decisions-missions`, `chaos-redux-event-assets`, `chaos-redux-frame-animation`, and `chaos-redux-super-events`.

## Requirement Coverage Table

| Requirement | Evidence path/line | Status | Notes |
| --- | --- | --- | --- |
| Event root remains `chaosx.nr6.1` and auto path is hidden/triggered. | `events/006_independence_wave.txt:24-31` | PASS | Entry event exists as hidden triggered country event. |
| Waves release immediately after hidden scoring and host-survival validation. | `events/006_independence_wave.txt:31-92`, `events/006_independence_wave.txt:151-158` | PASS | Candidate pool is built in `immediate`, host is validated, `release = event_target:independence_wave_current_candidate` runs in the same event, then report/news fire. |
| Release count is dynamic and tier-based, with no hardcoded live tuning. | `common/script_constants/006_independence_wave_constants.txt:8-31`, `common/scripted_effects/006_independence_wave_effects.txt:80-115` | PASS | Release bands are script constants and selected by chaos tier. |
| Per-wave release slots are reset before each wave. | `common/scripted_effects/006_independence_wave_effects.txt:115-136` | PASS | Release count, current host count, 16 country slots, candidate pool, and current-wave release ledger are cleared. |
| Event 6 does not erase the host; host keeps at least one state, preferably capital. | `common/scripted_triggers/006_independence_wave_triggers.txt:659-686`, `common/scripted_effects/006_independence_wave_effects.txt:230-293`, `events/006_independence_wave.txt:83-92` | PASS | Host must have more than the survival floor, capital is preferred as protected state, reserved state is flagged before release. |
| Later recovery/claims do not consume protected host-survival state. | `common/scripted_triggers/006_independence_wave_triggers.txt:2789-2823` | PASS | Border Commission target, claim, and contested-state triggers reject `independence_wave_host_survival_reserved`. |
| Reduced release footprints preserve future recovery instead of giving all cores immediately. | `common/scripted_effects/006_independence_wave_effects.txt:295-406` | PASS | Non-anchor candidate cores are temporarily masked before release and restored as later claim/proof territory. |
| One-state or reduced starts receive a recovery path. | `common/scripted_effects/006_independence_wave_effects.txt:375-388`, `common/scripted_effects/006_independence_wave_effects.txt:2408-2415`, `common/scripted_effects/006_independence_wave_effects.txt:6052-6128` | PASS | Reduced starts receive `independence_wave_reduced_territory_start`, border survey, claim ambition, limited-territory flag, and Border Commission transfer/recovery effects. |
| Released countries get origin flag and do not enter Soviet Collapse systems. | `common/scripted_effects/006_independence_wave_effects.txt:2339-2350`, `common/scripted_triggers/006_independence_wave_triggers.txt:10-12`, `common/national_focus/006_independence_wave_focus.txt:5-24` | PASS | Releases get `chaosx_release_origin_independence_wave`, origin variable 6, and the Event 006 focus tree. Runtime search found no active Soviet Collapse helper calls in Event 006 files. |
| Current user correction: KUB and ALT are not active Event 6 candidates. | `common/scripted_triggers/006_independence_wave_triggers.txt:44-48`, `docs/plans/006_independence_wave_plans/source_of_truth_map.md:14` | PASS | Runtime KUB/ALT references are only candidate exclusions; older KUB/ALT package claims are superseded. |
| New niche Africa/South America generic countries exist with unique flags. | `common/country_tags/chaosx_countries.txt:40-47`, `common/countries/Asante Council.txt:1-5`, `localisation/english/chaosx_countries_l_english.yml:236-310`, `docs/assets/006_independence_wave/flags/manifest.md:5` | PASS | ASN/KBN/PLM/AYM are custom tag/country/loc entries and have documented unique flag assets. DFR/ZUL/MAP also have custom tag/loc/flag support. |
| Generic Event 6 releases share `independence_wave_liberation_provisional_tree`. | `common/scripted_effects/006_independence_wave_effects.txt:3232-3243`, `common/national_focus/006_independence_wave_focus.txt:13-24`, `docs/specs/006_independence_wave_specs/006_independence_wave_country_packages.md:11-13` | PASS | Releases load the shared provisional tree; current correction says niche generic releases must not become bespoke overlays. |
| Released countries have starting units, equipment, industry, and a way to build an army. | `common/scripted_effects/006_independence_wave_effects.txt:2339-2406`, `common/ai_strategy/006_independence_wave.txt:88-111` | PASS | Setup adds manpower, infantry/support equipment, division template, starting guard units, one arms factory, focus tree, and AI build/production strategies. |
| News event displays all released countries. | `events/_chaosx_news.txt:144-154`, `localisation/english/006_independence_wave_l_english.yml:46-65`, `common/scripted_localisation/006_independence_wave_scripted_localisation.txt:231-325`, `common/scripted_effects/006_independence_wave_effects.txt:6790-6886` | PASS | Successful releases store current-wave country slots 1-16; news loc selects a 1-16 country list. Max release constant is 16. |
| Evolution logs are only a few true chaos-tier stages; no Calm World spam. | `common/scripted_effects/006_independence_wave_effects.txt:6144-6200`, `localisation/english/chaosx_gui_l_english.yml:511-517` | PASS | Current runtime logs Gathering Storm, Rising Cascade, Old Names, and Impossible Statehood only once each. |
| Event log/details and docs remain aligned. | `docs/events/006_independence_wave.md:164`, `docs/plans/006_independence_wave_plans/source_of_truth_map.md:107-108` | PARTIAL | Docs say catalog row is aligned, but source map still says future catalog parity needs review after changes and final completion audit remains required. |
| Decision categories, costs, tooltips, and AI decisions exist. | `common/decisions/categories/006_independence_wave_categories.txt:8-84`, `common/decisions/006_independence_wave_decisions.txt:61-220`, `common/decisions/006_independence_wave_decisions.txt:541-684` | PASS | The decision layer is large and has many `custom_trigger_tooltip`, `custom_effect_tooltip`, costs, timers, and `ai_will_do` blocks. |
| Scripted GUI satisfies full source-spec interactive management layer. | `common/scripted_guis/006_independence_wave_scripted_guis.txt:1-58`, `interface/006_independence_wave_scripted_gui.gui:1-166`, `docs/specs/006_independence_wave_specs/006_independence_wave_spec.md:1212-1328` | PARTIAL | Five GUI boards exist, but they are display-only icon/text containers. The source spec asks for candidate/member/state/protected-state displays and possible buttons with costs, requirements, AI equivalents, cleanup, and feedback. |
| Focus tree is implemented and AI weighted. | `common/national_focus/006_independence_wave_focus.txt:13-140` plus counted `50` focus blocks and `50` `ai_will_do` blocks | PARTIAL | Shared tree exists and has AI weights, but full source-spec closure also expects all accepted package identity and route depth to be validated. |
| Achievements are guarded against wrong origin/debug completion. | `common/scripted_triggers/006_independence_wave_triggers.txt:24-42`, `common/achievements/chaos_redux_achievements.txt:637-920`, `common/achievements/chaos_redux_achievements.txt:1023-1047` | PASS | Achievement helper requires Event 006 origin and clean/no-debug flags. Event 006 achievement definitions are present. |
| Super-events have thresholds, text, images, audio, and repeat prevention. | `common/script_constants/006_independence_wave_constants.txt:57-70`, `common/scripted_effects/006_independence_wave_effects.txt:5588-5668`, `interface/chaosx_super_events.gfx:116-141`, `localisation/english/006_independence_wave_l_english.yml:1072-1099` | PARTIAL | Runtime packages exist. Full prompt also requires source notes and catalog alignment for quotes/audio/images; current audit verified assets exist but did not verify every quote/audio source note against the prompt. |
| Report and news images are wired and referenced assets exist. | `interface/006_independence_wave_report_event_images.gfx:3-56`, `interface/006_independence_wave_news_event_images.gfx:3-8`, `events/006_independence_wave.txt:167-349`, `events/_chaosx_news.txt:148` | PASS | Texture reference probe found zero missing Event 006 referenced textures among checked `.gfx` files. |
| Package-specific portraits, seals, route art, and animations are complete. | `docs/plans/006_independence_wave_plans/source_of_truth_map.md:106`, `docs/specs/006_independence_wave_specs/006_independence_wave_assets_prompt.md:369-455`, `docs/specs/006_independence_wave_specs/006_independence_wave_spec.md:1312-1328` | PARTIAL | Current docs explicitly queue these as future asset work; no animation/frame-sheet package was found in `docs/assets/006_independence_wave`. |
| Spreadsheet/catalog is readable and fully aligned. | `docs/spreadsheets/chaos_redux_events_catalog.xlsx`, `docs/specs/006_independence_wave_specs/006_independence_wave_catalog_update.md:68-86` | UNVERIFIED | Workbook zip opened and contains an Independence Wave row; `openpyxl` is unavailable, and XML shared strings did not show the newer super-event stage names. Needs parent review with spreadsheet tooling. |
| Localisation encoding and key style are compliant. | `localisation/english/006_independence_wave_l_english.yml:1`, BOM probe results below | PARTIAL | Audited loc files are UTF-8 BOM and `:0`-free. Two player-facing strings still mention Soviet Collapse/Event 005 framing directly. |
| No fallback or placeholder completion claim. | `docs/events/006_independence_wave.md:13`, `docs/plans/006_independence_wave_plans/source_of_truth_map.md:6`, `docs/plans/006_independence_wave_plans/source_of_truth_map.md:108` | PASS | Current docs say playable wrap-up, not full completion. |
| Final completion standards are met. | `docs/specs/006_independence_wave_specs/006_independence_wave_spec.md:1141-1155`, `docs/specs/006_independence_wave_specs/006_independence_wave_spec.md:1347-1359` | FAIL | Current state is playable and broad, but source-spec closure still has known partials: GUI, package-specific presentation/animation, catalog/spreadsheet verification, source-note verification, and final balance/completion audit gates. |

## Top 10 Blockers For Full Source-Spec Completion

1. **Full completion would be a false claim in the current source-of-truth docs.** `docs/events/006_independence_wave.md:13`, `docs/events/006_independence_wave.md:407-413`, and `docs/plans/006_independence_wave_plans/source_of_truth_map.md:108` explicitly say the current target is playable wrap-up, queued items remain, and final completion audit is still required.

2. **Scripted GUI is display-only relative to the full source spec.** Current scripted GUI definitions only gate visibility and point to simple text windows (`common/scripted_guis/006_independence_wave_scripted_guis.txt:1-58`, `interface/006_independence_wave_scripted_gui.gui:1-166`). The spec asks for candidate/member/state/protected-state views and possible buttons with costs, requirements, AI equivalents, cleanup, and feedback (`docs/specs/006_independence_wave_specs/006_independence_wave_spec.md:1212-1328`; `docs/specs/006_independence_wave_specs/006_independence_wave_decisions_ai.md:491-516`).

3. **Animation and frame-animation deliverables are not complete.** The source spec and asset prompt require real source frames, sheet PNG/DDS, static fallback, preview, manifest, and `.gfx` handoff for animated states (`docs/specs/006_independence_wave_specs/006_independence_wave_spec.md:1312-1328`; `docs/specs/006_independence_wave_specs/006_independence_wave_assets_prompt.md:360-367`). `find docs/assets/006_independence_wave -name '*animation*' -o -name '*frame*' ...` found no animation packages.

4. **Package-specific non-flag presentation remains future-scoped.** The current source map queues package portraits, seals, route art, and animations (`docs/plans/006_independence_wave_plans/source_of_truth_map.md:106`), while the country-package spec says generic route families currently reuse shared art and bespoke seals/portraits/animated route art remain follow-up (`docs/specs/006_independence_wave_specs/006_independence_wave_country_packages.md:453`).

5. **Spreadsheet/catalog parity is not fully verified.** `openpyxl` is not installed, so workbook semantic inspection could not be done. A zip/XML read proved the workbook opens and contains Event 006 text, but shared strings did not include `Great Partition Week`, `Old Names Return`, or `Impossible Statehood`. Source map still calls future catalog parity review out separately (`docs/plans/006_independence_wave_plans/source_of_truth_map.md:107`).

6. **Two player-facing localisation strings still mention Event 005/Soviet Collapse framing.** Runtime search found `localisation/english/006_independence_wave_l_english.yml:509` and `localisation/english/chaosx_achievements_l_english.yml:244` using "Soviet Collapse" in player-facing text. That conflicts with the current correction that Event 6 is independent and should not present itself through Event 5 system language.

7. **Super-event source-note and catalog proof is only partially audited.** Runtime super-event packages and assets exist, but the super-event prompt requires quote/audio source fields and catalog alignment (`docs/specs/006_independence_wave_specs/006_independence_wave_super_event_prompt.md:465-509`). This audit did not verify every quote/audio note against the prompt, and source-map/catalog docs still retain alignment follow-up.

8. **Final balance scenarios remain outside this read-only audit.** The current improvement addendum still says implemented decision/route layers need final balance scenarios and completion audits before closure (`docs/plans/006_independence_wave_plans/006_independence_wave_improvement_addendum_post_focus_formation_tranche.md:61`). Mechanical source checks passed, but no live or scenario simulation was run.

9. **The worktree is not in a completion-ready integration state.** `git status --short` shows core Event 006 runtime files such as `common/scripted_effects/006_independence_wave_effects.txt`, `common/scripted_triggers/006_independence_wave_triggers.txt`, `common/decisions/006_independence_wave_decisions.txt`, `common/national_focus/006_independence_wave_focus.txt`, and GUI/on-action files as untracked, with many source specs modified. This is not a gameplay blocker by itself, but it blocks any clean "fully implemented and committed" completion claim.

10. **Full source-spec package/formable closure still exceeds current accepted playable wrap-up scope.** The source spec allows only formables with valid states, tag support, asset support, and route logic, and requires skipped formables to be reported (`docs/specs/006_independence_wave_specs/006_independence_wave_spec.md:1200-1210`). Current docs explicitly state other package-specific countries and formables are not complete (`docs/events/006_independence_wave.md:61`).

## Highest-Value Patch For Parent

Make a **targeted closure-alignment patch**, not a broad expansion pass:

- Upgrade the current scripted GUI/value-board layer to show the highest-value missing state already produced by runtime systems: protected host state, current release list/count, coalition members/count, Border Commission/reduced-start recovery status, and formation package requirements where available.
- Keep actions as normal decisions unless a GUI button can call the same scripted trigger/effect family and has an AI-equivalent decision path.
- In the same patch, remove the two player-facing Soviet Collapse references and update/review the workbook/catalog row against current implementation facts.

This patch closes the largest visible source-spec mismatch without adding a new route family or reopening KUB/ALT/package expansion.

## Validation Commands Run

| Command | Result |
| --- | --- |
| `rg -n "<=|>=" events/006_independence_wave.txt common/...` | No matches. |
| `rg -n "(^|[^A-Za-z0-9_])-([A-Za-z_][A-Za-z0-9_]*|global\\.[A-Za-z_][A-Za-z0-9_]*)"` on Event 006 runtime files | No unary negative variable-token matches. |
| `rg -n "^[^#\\n]*:0" localisation/english/006_independence_wave_l_english.yml localisation/english/chaosx_gui_l_english.yml localisation/english/chaosx_countries_l_english.yml localisation/english/chaosx_achievements_l_english.yml` | No matches. |
| `xxd -p -l 3` on audited loc files | All four checked loc files start with `efbbbf` UTF-8 BOM. |
| Bracket-count `awk` over Event 006 event/effects/triggers/decisions/focus/gui/on_actions/ideas/AI/constants/scripted localisation | All checked files ended with bracket balance `0`. |
| `rg -n "\\b(KUB|ALT)\\b|Kuban|Altai|Oyrot|Soviet Collapse|soviet_collapse|chaosx_release_origin_soviet"` on Event 006 runtime/loc files | Runtime KUB/ALT only candidate exclusions. Found one focus comment and two player-facing Soviet Collapse loc references. |
| Texture-reference probe over `interface/006_independence_wave_icons.gfx`, `interface/chaosx_super_events.gfx`, `interface/chaosx_achievements.gfx`, `interface/006_independence_wave_report_event_images.gfx`, `interface/006_independence_wave_news_event_images.gfx` | Checked 89 relevant Event 006/achievement texture references; zero missing. |
| `find gfx/super_events ...` and `find sound music ...` for Event 006 super-event assets | Found seven Event 006 super-event DDS files plus matching `.ogg` music and `.wav` sound files. |
| Count probe for focus/decision/idea files | Focus file has 50 focus blocks and 50 `ai_will_do` blocks. Decision file has 183 Event 006 decision icon refs, 146 `ai_will_do`, 212 `custom_trigger_tooltip`, and 168 `custom_effect_tooltip`. |
| Read-only workbook probe with `openpyxl` | Workbook exists, but `openpyxl` is not installed. |
| Read-only workbook zip/XML probe | XLSX zip opened, `Independence Wave`/`Event 006` strings present, but `Great Partition Week`, `Old Names Return`, and `Impossible Statehood` not found in shared strings. |
| `git status --short -- <Event006 surfaces>` | Many core Event 006 runtime files are untracked and many specs/docs are modified. No changes were reverted. |

## Improvement-Loop Recommendation

Broad improvement-loop expansion is **not recommended** right now. `docs/plans/006_independence_wave_plans/006_independence_wave_improvement_loop_gate.md:37` says no broad expansion is recommended, and the current blockers are closure, validation, presentation, and catalog-alignment gaps rather than a need for another large design addendum.

Recommended direction: closure hardening and alignment. Do not claim completion until the partials above are resolved or explicitly accepted as deferred scope.

## Simplifications, Omissions, And Blockers

- No runtime files were patched.
- No localisation files were patched.
- No assets, spreadsheets, or existing docs were patched.
- This handoff does not claim Event 006 completion.
- Spreadsheet semantic parity remains unverified because spreadsheet tooling is unavailable in this environment.
- Live in-game validation was not run; this audit is source/mechanical only.
