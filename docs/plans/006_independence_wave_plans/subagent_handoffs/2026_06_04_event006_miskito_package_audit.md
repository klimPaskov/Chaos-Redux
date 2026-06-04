# Event006 Miskito Package Audit

Read-only audit of `iw_pkg_miskito` for the Event006 Independence Wave country-package tranche.

## Findings

### Medium: Miskito candidate seeding leaves cores behind when MIS is not selected

- `common/scripted_effects/006_independence_wave_effects.txt:742` seeds `MIS` when `can_independence_wave_seed_miskito_package = yes`.
- `common/scripted_effects/006_independence_wave_effects.txt:744` and `common/scripted_effects/006_independence_wave_effects.txt:745` add `MIS` cores to states `312` and `317` immediately during candidate-pool construction.
- `events/006_independence_wave.txt:33` calls `independence_wave_seed_verified_package_candidates = yes` before random candidate selection.
- `events/006_independence_wave.txt:75` through `events/006_independence_wave.txt:113` releases only selected candidates, and `events/006_independence_wave.txt:115` only restores the Sokoto temporary masking handled by `independence_wave_restore_temporary_package_cores`.
- `common/scripted_effects/006_independence_wave_effects.txt:787` through `common/scripted_effects/006_independence_wave_effects.txt:802` only restores temporary Sokoto cores; there is no Miskito cleanup or candidate-selected guard.

Impact: if the Miskito gate passes but the release target count is reached before `MIS` is selected, states `312` and `317` still retain `MIS` cores for the rest of the campaign. That violates the parent handoff's explicit verification target that dynamic core seeding should not leave unwanted persistent cores when `MIS` enters the pool but is not selected in a reduced wave. It can also make vanilla `MIS` releasable through other systems after an Event006 wave that did not actually create Miskito.

Suggested fix: defer the two `add_core_of = MIS` effects until the selected-candidate release path, or mark the added cores with temporary state flags and remove them after the loop when `MIS` was not released by the wave. If cleanup is chosen, keep selected-release behavior intact so reduced release still starts from `317` and restores `312` as the later proof/core territory.

## Verified Surfaces

- Vanilla evidence matches the parent handoff: `MIS` is registered in vanilla `common/country_tags/00_countries.txt`, vanilla `history/countries/MIS - Miskito.txt` sets capital `317` and comments cores `312, 317`, vanilla `common/characters/MIS.txt` defines `MIS_miskito_council`, vanilla Chile decisions dynamically core/release `312` and `317`, and vanilla ideology flag assets exist.
- Candidate gate `can_independence_wave_seed_miskito_package` is tier IV/V, requires `MIS = { exists = no }`, requires state `317` to be non-capital, requires the owner to control `317`, preserves a host survival floor, and gates on host weakness.
- Reduced-release anchor cluster is sequential for BAR, DAH, and MIS and the audited files are brace-balanced.
- Startup identity sets `independence_wave_package_miskito`, local-polity package candidate/type, package id constant, shore-council formation family, local-polity gain, and `independence_wave_miskito_shore_council_spirit`.
- Focus route contains `independence_wave_miskito_shore_records` and `independence_wave_miskito_coastal_petitions`, both with icons, localisation, rewards, bypasses, and AI weights.
- Decision route contains `independence_wave_open_miskito_shore_records`, `independence_wave_map_miskito_coastal_petitions`, `independence_wave_proclaim_miskito_shore_council`, and mission `independence_wave_integrate_miskito_shore_council`.
- Event-log constants, record effects, scripted localisation mappings, and GUI localisation cover Miskito package and formation rows in list/detail/selected-detail contexts.
- AI strategy includes `independence_wave_package_miskito`, shore-records opened, and shore-council proclaimed in the local-polity package posture.
- No `common/country_tags`, `history/countries`, or `gfx/flags` file changes were present in the worktree diff/status for this package audit.

## Validation Commands

- `sed -n '1,220p' .agents/skills/chaos-redux-events/SKILL.md`
- `sed -n '1,220p' .agents/skills/chaos-redux-subagents/SKILL.md`
- `for f in "paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md" "paradox_wiki/Triggers - Hearts of Iron 4 Wiki.md" "paradox_wiki/Effect - Hearts of Iron 4 Wiki.md" "paradox_wiki/Modifiers - Hearts of Iron 4 Wiki.md" "paradox_wiki/Localisation - Hearts of Iron 4 Wiki.md" "paradox_wiki/Scopes - Hearts of Iron 4 Wiki.md" "paradox_wiki/On actions - Hearts of Iron 4 Wiki.md" "paradox_wiki/Event modding - Hearts of Iron 4 Wiki.md" "paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md" "paradox_wiki/Idea modding - Hearts of Iron 4 Wiki.md" "paradox_wiki/AI modding - Hearts of Iron 4 Wiki.md" "paradox_wiki/National focus modding - Hearts of Iron 4 Wiki.md" "paradox_wiki/Country creation - Hearts of Iron 4 Wiki.md"; do sed -n '1,32p' "$f" >/tmp/chaosx_wiki_read.tmp; wc -l "$f"; done`
- `rg -n "MIS|Miskito|miskito|312|317|add_core_of|release|load_focus_tree" "/home/klim/projects/Hearts of Iron IV/common/country_tags/00_countries.txt" "/home/klim/projects/Hearts of Iron IV/history/countries/MIS - Miskito.txt" "/home/klim/projects/Hearts of Iron IV/common/characters/MIS.txt" "/home/klim/projects/Hearts of Iron IV/common/decisions"`
- `rg -n "miskito|Miskito|MIS|iw_pkg_miskito|independence_wave_package_miskito|shore_council|317|312|BAR|barotseland|DAH|dahomey" <task files>`
- `rg -n "independence_wave_candidate_pool|remove_core_of = MIS|312 = { add_core_of = MIS|317 = { add_core_of = MIS" common/scripted_effects/006_independence_wave_effects.txt common/scripted_triggers/006_independence_wave_triggers.txt events/006_independence_wave.txt`
- `python3 - <<'PY' ... brace-balance check for audited script files ... PY`
- `python3 - <<'PY' ... UTF-8 BOM check for localisation/english/006_independence_wave_l_english.yml and localisation/english/chaosx_gui_l_english.yml ... PY`
- `git status --short`

## Residual Risks

- I did not run the HOI4 executable or an external Clausewitz parser. This was a static audit against local wiki, vanilla documentation/evidence, and repository files.
- Several Event006 files are currently untracked in the worktree, so this audit treats the parent implementation as the source to inspect rather than a clean committed baseline.
