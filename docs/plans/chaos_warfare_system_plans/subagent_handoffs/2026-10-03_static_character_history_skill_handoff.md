# Static character history skill handoff

Disposition: implemented for the bounded skill correction; native execution proof remains pending.

Acceptance basis: the parent delegation records the user's explicit direction to correct load-time recruitment warnings through history-time recruitment on a dedicated dormant holder while preserving approved static identities.
This basis authorizes the reusable skill correction and does not establish that the gameplay implementation has passed native execution validation.

## Changed paths and ownership

- `.agents/skills/chaos-redux-events/SKILL.md`: only the character-recruitment sentences within the country-package audit paragraph, currently line 473.
- `docs/plans/chaos_warfare_system_plans/subagent_handoffs/2026-10-03_static_character_history_skill_handoff.md`: this handoff.

The existing skill already owns this workflow, so no skill was created.
Other skills, gameplay files, AGENTS.md, staging, and commits are outside this delegation.
The unrelated pre-existing probability-audit addition around line 355 is preserved.
No subagent routing or AGENTS.md change is needed.
The parent owns final review and the isolated-index commit of only this paragraph hunk and this handoff.

## Exact paragraph hunk

```diff
@@ character-recruitment paragraph @@
-When auditing event-created country packages, verify the whole playable-country surface, not only the release effect. Check country files, custom-tag history files, additive startup grants for existing countries, generated startup scientists when needed, tag registration, base localisation, ideology-specific cosmetic localisation (`TAG_democratic`, `TAG_communism`, `TAG_fascism`, `TAG_neutrality` plus `_DEF` and `_ADJ`), flags, decision/focus/idea icons, focus loading, AI strategy, docs, and manifests together. For existing-country variants, verify the event-created flag is set only on the release path and every `load_focus_tree` path is gated by that flag. Do not copy vanilla country, state, or unit history only to add Chaos Redux technologies, equipment, facilities, traits, or other additive setup. Put that setup in `common/scripted_effects/chaosx_startup_history_effects.txt` and call it from `on_startup`. Do not put `recruit_character` in scripted effects or on_actions. Do not use `history/general` for country-specific Chaos Redux scientists. It is for generic character pools. For named existing-country startup scientists, call `generate_scientist_character` from the country startup grant with explicit portrait, gender, skills, and traits when any, mark/select the newly generated scientist with the startup helper flags, apply `set_character_name` and the intended portrait if needed, and set a persistent identity flag for later scripted references.
+When auditing event-created country packages, verify the whole playable-country surface, not only the release effect. Check country files, custom-tag history files, additive startup grants for existing countries, generated startup scientists when needed, tag registration, base localisation, ideology-specific cosmetic localisation (`TAG_democratic`, `TAG_communism`, `TAG_fascism`, `TAG_neutrality` plus `_DEF` and `_ADJ`), flags, decision/focus/idea icons, focus loading, AI strategy, docs, and manifests together. For existing-country variants, verify the event-created flag is set only on the release path and every `load_focus_tree` path is gated by that flag. Do not copy vanilla country, state, or unit history only to add Chaos Redux technologies, equipment, facilities, traits, or other additive setup. Put that setup in `common/scripted_effects/chaosx_startup_history_effects.txt` and call it from `on_startup`. Static named characters requiring persistent script tokens must be recruited in history. Do not use runtime `recruit_character` or attempt a character-scope transfer of an unrecruited identity. For dated identities, a bounded `history/general` recruitment pool on a dedicated dormant holder is valid; the holder must have no owned states or gameplay route and must not reuse an event-owned playable holder or test harness. Check date eligibility and original ownership before transferring from the original owner's country scope with `set_nationality = { target_country = <destination> character = <static_token> }`. Preserve availability dates, roles, identity flags, and retirement gates. Use `generate_scientist_character` only when a generated unnamed identity without a persistent character token is intended; never silently replace approved static identities with generated substitutes. Validate native execution separately from source proof.
```

## Source basis

The connected tool list exposes `hoi4.reference_context`, `hoi4.reference_search`, `hoi4.reference_read`, and `hoi4.source_lookup`.
The live context call and two search calls did not return during this correction and their orchestration was terminated after several minutes; the cited local source sections below were read directly.
The unreturned calls do not establish MCP reference coverage or engine evidence.

- Installed `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\effects_documentation.md`, lines 7397–7420: `set_nationality` supports COUNTRY and CHARACTER scopes; the documented country-scoped block takes `target_country` and `character`.
- The same installed file, lines 5696–5707: `recruit_character` attaches a character to a country and requires country scope.
- The same installed file, lines 4458–4481: `generate_scientist_character` creates a new character with a scientist role and recruits it into the country in scope; generation is distinct from recruiting an approved database token.
- Offline `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\paradox_wiki\Character modding - Hearts of Iron 4 Wiki.md`, lines 50–58: character recruitment belongs in history and unrecruited characters never appear; the checklist describes any history file, usually the country's corresponding file.
- Installed vanilla `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\history\countries\USA - USA.txt`, lines 441–448: existing-country history directly recruits persistent named database tokens.

Source revisions, SHA-256:

- `effects_documentation.md`: `2CDC93D26775990468EED167442F7A416B13059FB8FE07D139B54250B79209AF`.
- Offline Character modding page: `8EF3D5F9923026DD81F239944710B7331A8D06AD42E4345B32FCE4E86DD95D98`.
- Vanilla USA history: `73A96E416BE9B14D696AF8094A1505AF7616521CC991F291E716D85ABAB9BEC4`.

The dedicated dormant-holder convention is the parent-supplied user-approved design, constrained by the history recruitment and country-scoped transfer rules above.
The vanilla precedent proves ordinary history recruitment, not native execution of this dormant-holder arrangement.

## Validation and limits

Reviewed the rule against two intended cases: an approved static identity retains its database token and receives history recruitment plus a guarded country-scoped transfer; an intentionally generated token-free scientist remains eligible for `generate_scientist_character`.
The surrounding additive setup rule remains intact, and the change adds no event-specific identity, country token, or implementation history to the skill.
The holder rule excludes owned states, gameplay routes, playable event holders, and the test harness.
Date eligibility, original ownership, roles, identity flags, and retirement remain explicit preservation obligations.

Native execution proof remains pending with the parent and user.
Source review does not prove load-time warning removal, dated transfer behavior, role preservation in engine, or retirement behavior.
No game was launched and no gameplay patch, fallback substitution, staging, or commit was performed by this worker.
No simplifications were made within the delegated skill correction.

## Parent integration

Parent review retained the unrelated probability-audit paragraph in the working tree and isolated only the character-recruitment hunk for this commit.
The first extracted patch retained a new-side line offset from an omitted earlier hunk and did not apply to the temporary index; correcting that offset made the isolated patch apply without taking the unrelated paragraph.
The parent captured this reusable rule in `.agents/skills/chaos-redux-shared-git-commit/SKILL.md`, step 2.
No shared-index or source changes were made by the failed patch attempt.
The country-package audit also records the completed installed Workshop and local-mod CSH collision scan, whose only match was the new package registration.
