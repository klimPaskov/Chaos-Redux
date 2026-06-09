# Event 006 Generic Authority Finishers Focus Audit

Verdict: PASS

## Scope

Read-only audit of the five generic infrastructure-authority route-family finisher focuses:

- `independence_wave_free_port_neutrality_statute`
- `independence_wave_municipal_home_rule_charter`
- `independence_wave_protectorate_public_guarantees`
- `independence_wave_oil_public_concession_statute`
- `independence_wave_canal_transit_statute`

No gameplay, localisation, asset, flag, or flag-asset files were edited. This handoff is the only file written.

## Files Inspected

Required references:

- `AGENTS.md`
- `.agents/skills/hoi4-focus-trees/SKILL.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`
- `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Triggers - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Effect - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Modifiers - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Localisation - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Scopes - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/On actions - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Event modding - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Idea modding - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/AI modding - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/National focus modding - Hearts of Iron 4 Wiki.md`
- `/home/klim/projects/Hearts of Iron IV/documentation/script_concept_documentation.md`
- `/home/klim/projects/Hearts of Iron IV/documentation/triggers_documentation.md`
- `/home/klim/projects/Hearts of Iron IV/documentation/effects_documentation.md`
- `/home/klim/projects/Hearts of Iron IV/common/national_focus/generic.txt`

Event 006 files:

- `common/national_focus/006_independence_wave_focus.txt`
- `common/script_constants/006_independence_wave_constants.txt`
- `common/scripted_effects/006_independence_wave_effects.txt`
- `common/on_actions/006_independence_wave_on_actions.txt`
- `interface/006_independence_wave_icons.gfx`
- `localisation/english/006_independence_wave_l_english.yml`
- `docs/events/006_independence_wave.md`
- `docs/specs/006_independence_wave_specs/006_independence_wave_focus_trees.md`
- `docs/assets/006_independence_wave/focus_icons/reuse_ledger.md`
- `docs/assets/006_independence_wave/focus_icons/manifest.md`

## Checks Performed

- Confirmed all five focus blocks exist in `common/national_focus/006_independence_wave_focus.txt`.
- Confirmed each focus is post-proclamation by prerequisite chain and availability gate.
- Confirmed each focus has package-specific availability plus a proclamation flag requirement.
- Confirmed each focus has a bypass flag and calls a same-named scripted effect through `completion_reward`.
- Confirmed each matching scripted effect exists and sets the matching bypass/completion flag.
- Confirmed each focus uses already registered Event 006 focus sprites.
- Confirmed no new art or flag/flag-asset references are required by this tranche.
- Confirmed title and description localisation exists for every focus in the tree.
- Confirmed docs and focus icon asset docs report 115 focuses.
- Confirmed the focus icon reuse ledger has 115 rows.
- Scanned the audited Event 006 files for unsupported less-than-or-equal and greater-than-or-equal operators.
- Checked Event 006 on-actions for whole-world daily/weekly/monthly polling additions.
- Scanned tranche-relevant focus/effect/localisation/icon/docs surfaces for Event005/PRA/Soviet/collapse runtime coupling.

## Findings

No blocking findings.

The five audited focus blocks have the expected structure:

- Free Port: `common/national_focus/006_independence_wave_focus.txt:2287` to `2304`; package gate and proclamation flag at `2294` to `2297`; bypass at `2298` to `2300`; scripted effect call at `2302` to `2304`.
- Municipal: `common/national_focus/006_independence_wave_focus.txt:2367` to `2384`; package gate and proclamation flag at `2374` to `2377`; bypass at `2378` to `2380`; scripted effect call at `2382` to `2384`.
- Protected Mandate: `common/national_focus/006_independence_wave_focus.txt:2447` to `2464`; package gate and proclamation flag at `2454` to `2457`; bypass at `2458` to `2460`; scripted effect call at `2462` to `2464`.
- Oil Protectorate: `common/national_focus/006_independence_wave_focus.txt:2527` to `2544`; package gate and proclamation flag at `2534` to `2537`; bypass at `2538` to `2540`; scripted effect call at `2542` to `2544`.
- Canal Authority: `common/national_focus/006_independence_wave_focus.txt:2607` to `2624`; package gate and proclamation flag at `2614` to `2617`; bypass at `2618` to `2620`; scripted effect call at `2622` to `2624`.

Matching scripted effects exist:

- `common/scripted_effects/006_independence_wave_effects.txt:3320`
- `common/scripted_effects/006_independence_wave_effects.txt:3398`
- `common/scripted_effects/006_independence_wave_effects.txt:3490`
- `common/scripted_effects/006_independence_wave_effects.txt:3558`
- `common/scripted_effects/006_independence_wave_effects.txt:3634`

Finisher tuning is centralized in script constants:

- `common/script_constants/006_independence_wave_constants.txt:1101` to `1109`

Focus sprite references are registered:

- `GFX_focus_independence_wave_sponsored_cabinet`: `interface/006_independence_wave_icons.gfx:203`
- `GFX_focus_independence_wave_municipal_workshops`: `interface/006_independence_wave_icons.gfx:219`
- `GFX_focus_independence_wave_free_city_board`: `interface/006_independence_wave_icons.gfx:255`

Focus localisation exists:

- `localisation/english/006_independence_wave_l_english.yml:314` to `339`

Docs and asset ledgers are aligned:

- Infrastructure-authority finisher narrative: `docs/events/006_independence_wave.md:130`
- Docs focus count: `docs/events/006_independence_wave.md:158`
- Ledger focus count statement: `docs/assets/006_independence_wave/focus_icons/reuse_ledger.md:5`
- Manifest focus count statement: `docs/assets/006_independence_wave/focus_icons/manifest.md:54`
- Five audited focus ledger rows: `docs/assets/006_independence_wave/focus_icons/reuse_ledger.md:106`, `109`, `112`, `115`, and `118`

Event005/PRA/Soviet/collapse scan note: broad Event 006 docs intentionally contain Event 005 separation language and a future PRA queue note, but the audited tranche does not introduce runtime Event005/PRA/Soviet/collapse dependencies in the five focus blocks, their matching scripted effects, localisation, or icon ledger rows.

## Validation Evidence

- Focus block count: 115 from `rg -n "^\\s*focus = \\{" common/national_focus/006_independence_wave_focus.txt | wc -l`.
- Focus IDs inside `focus = { ... }` blocks: 115.
- Missing focus localisation entries: 0, checking each focus ID for both `id:` and `id_desc:`.
- Unsupported operator scan: 0 hits for unsupported less-than-or-equal or greater-than-or-equal operators across the audited Event 006 focus/constants/effects/localisation/docs/icon/on-action files.
- Docs count: 115 in `docs/events/006_independence_wave.md:158`, `docs/assets/006_independence_wave/focus_icons/reuse_ledger.md:5`, and `docs/assets/006_independence_wave/focus_icons/manifest.md:54`.
- Focus icon ledger row count: 115 rows matching `| \`independence_wave_`.
- Event 006 on-action world-polling scan: 0 hits for `on_daily`, `on_weekly`, `on_monthly`, `every_country`, `every_possible_country`, or `every_other_country` in `common/on_actions/006_independence_wave_on_actions.txt`.
- Event 006 on-actions use event hooks only: `on_war_relation_added`, `on_capitulation`, `on_peaceconference_ended`, `on_puppet`, and `on_annex` at `common/on_actions/006_independence_wave_on_actions.txt:9` to `65`.

## Remaining Risks Or Omissions

- This was a read-only audit. I did not run the game or a full Clausewitz parser.
- The worktree contains many unrelated modified and untracked files. I ignored unrelated changes and audited only the bounded Event 006 surfaces named above.
- Existing global on-action files elsewhere in the repo contain daily/weekly/monthly and world-iteration logic, but the Event 006 on-action file audited here does not add such polling.
- Some surrounding Event 006 scripted-effect indentation is uneven, but the audited finisher effects are present, close their blocks, and are callable from the focus rewards. No patch was made because gameplay edits were out of scope.
