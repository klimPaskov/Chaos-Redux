# Numeric scripted-localisation skill handoff

Disposition: implemented for the authorized documentation scope, pending parent review and commit.
Acceptance basis: the parent explicitly requested one generic numeric-display rule in the events skill and this handoff.
Repository: `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux`.

## Files and owned hunks

- Updated `.agents\skills\chaos-redux-events\SKILL.md` under `Detail text, immediate effects, and value formatting`, directly after the existing integer-formatting paragraph.
- Owned Git hunk: `@@ -155,6 +155,11 @@`, adding four instruction lines at current lines 158–161 and one separating blank line.
- Added `docs\plans\026_black_friday_plans\subagent_handoffs\2026-10-03_numeric_localisation_skill_handoff.md` as a new handoff file.

Existing-equivalent check: read the current events skill and searched its localisation, numeric, and formatting guidance.
The existing paragraph specified integer formatting with `|0`, but did not explain the distinction between a localisation value and a dynamic key.
The insertion places `numeric_value_display: "[?temp_value|0]"` in a real `.yml` value and selects it through `defined_text.text.localization_key = numeric_value_display`.
It explains the dynamic-token failure risk of putting the formatted output in the key field, preserves temporary calculations in the same `text.trigger`, retains documented constant-backed temporary getters, and avoids persistent globals solely for formatting.
The example identifiers are generic and introduce no runtime definitions.

Shared-file preservation: before editing, the skill already had a separate two-line insertion for event-option probability audits near original line 347.
That pre-existing hunk remains intact, appearing at `@@ -347,6 +352,8 @@` after this insertion.
Parent should review and select this task's numeric-display hunk independently of that unrelated work.

## Reference basis

References were read directly from the offline snapshot and installed game files.
The parent reported absent HOI4 reference tools in its connected tool list.
This subagent's `ALL_TOOLS` instead exposes reference-context, reference-search, and reference-read names, but no calls or service-health claims were made.
The authorized change is skill documentation only, and local reads provide the requested reference basis without claiming MCP or engine validation.

- Offline `paradox_wiki\Localisation - Hearts of Iron 4 Wiki.md`, lines 190–214: decimal formatter rules and `.yml` numeric examples.
- Same wiki, lines 680–681: temporary variables set in a scripted-localisation trigger remain available when displaying the selected key, whose field uses the American spelling `localization_key`.
- Same wiki, lines 706–726: dynamic text in `localization_key` constructs and evaluates a key name.
- Same wiki, lines 729–791: numeric unit-display example computes temporary values in `text.trigger`, selects literal named keys, and formats those values in `.yml` strings.
- Installed `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\scripted_localisation\WUW_GER_scripted_loc.txt`, lines 689–697: temporary array-length and iterator calculations precede literal `localization_key = oppositional_monroe_list`.
- Installed `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\localisation\english\WUW_decisions_l_english.yml`, line 566: the selected named key consumes the temporary iterator in its localisation value.
- Installed `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\script_concept_documentation.md`, lines 216–244: constants require supported fields and fixed-point access uses `constant:`.
- Installed `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\effects_documentation.md`, lines 7820–7839: `set_temp_variable` supports value, variable, and math-expression assignments.

Read-source SHA-256 revisions: wiki `1A8F72362A34B4BB653186746B9FAE0B98E463205CB02F12CCF2C3D9CCD3A064`, vanilla scripted localisation `82233D7BB8362D933182C7DA345606089A67B92ADEDB764C37A942E1E2F67683`, concept documentation `884BFE9F9207EA4B25B36B5129D0F77D11D4B2F7EB0592587767EC58D24930C7`, effects documentation `2CDC93D26775990468EED167442F7A416B13059FB8FE07D139B54250B79209AF`.

## Validation and handoff limits

The official `skill-creator\scripts\quick_validate.py` accepted the updated skill with `Skill is valid!`.
Reviewed the diff against the existing guidance and local examples, confirming one generic insertion and preservation of the unrelated existing hunk.
The startup dynamic-token defect is parent-reported evidence, not independently reproduced in this documentation task.
Local references support the named-key pattern and temporary-value visibility, but do not themselves reproduce the reported error or prove every constant assignment is accepted.
The constant-getter rule therefore remains conditional on installed documentation support.

Skills used: `skill-creator` and `chaos-redux-events`.
Skills updated: `chaos-redux-events` only.
No skills created, no other skills changed, and no routing or `AGENTS.md` update is needed.
No gameplay, localisation, catalog, or asset files were edited.
No live-game work was performed or awaited.
No simplifications or documentation blockers remain.
Parent owns final review and commit, including exclusion of unrelated shared-file changes.
