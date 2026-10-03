# Native custom-cost key contract skill handoff

Disposition: implemented for the bounded skill-maintenance assignment.
Acceptance basis: the parent explicitly authorized one reusable paragraph in the decisions-and-missions skill and this handoff path on 2026-10-03, with no staging, commits, or gameplay changes.

## Exact owned change

Updated `.agents\skills\chaos-redux-decisions-missions\SKILL.md` immediately below `Custom-cost affordability and payment`, at working-file lines 232-235.
Only this paragraph and its separating blank line belong to this subagent:

```text
Every native `custom_cost_text = <base>` needs localisation for `<base>`, `<base>_blocked`, and `<base>_tooltip`; the engine selects the row key through `custom_cost_trigger` and the tooltip key on hover (offline Decision modding, lines 311-329).
Per-resource scripted colour selectors do not replace these parent native keys.
When the base already renders each resource's ready or blocked colour independently, exact `$base$` aliases for the suffixed keys can reuse that quote without duplicating amounts or adding fees.
Trace actual decision consumers, scripted getters, and texticon definitions; missing source-key coverage establishes a contract gap, not proof that a native row displayed a raw key.
```

The existing section covered affordability, payment, fractional quotes, emergency quotes, and release receipts but omitted the engine-selected native key family.
The addition states only that missing contract and its alias/evidence boundaries.
No new skill, routing change, UI metadata, gameplay edit, workbook edit, or other skill edit was needed.
No feature-specific identifiers, counts, commit identities, or historical context entered the skill.

## Sources read directly

- `paradox_wiki\Decision modding - Hearts of Iron 4 Wiki.md`, lines 311-329, especially line 314: `custom_cost_trigger` selects the base or `_blocked` row key; `_tooltip` is selected on cost hover.
  SHA-256: `7713B9BCEE5F3818D63AAFBD45D18E812A9173A7C59AB238384B57DB60DB6162`.
- `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\decisions\AFG.txt`, lines 490-496: native precedent pairs `custom_cost_trigger` with `custom_cost_text = BRA_decision_cost_cangaceiro`.
  SHA-256: `DABC91C3F7FB1810D64D91D07147E827068D42540326CE10554A0752EE48D7A7`.
- `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\localisation\english\toa_decisions_l_english.yml`, lines 340-341: the corresponding base and `_blocked` strings confirm the native suffix naming.
  This two-line precedent does not by itself establish tooltip coverage; that requirement comes from the offline Decision modding section.
  SHA-256: `AF37CB46F7D6C13E07FF4B0A6934239B8093132CC47780E05BC1B8A0E01DA152`.

Read the complete current decisions-and-missions skill before editing.
The official skill-creator skill and project subagent skill were already read completely in this subagent session and their narrow-edit and handoff guidance was followed.

## Actual consumer and getter evidence

Read-only inspection found `common\decisions\migration_decisions.txt`, lines 1260-1261, consuming `migration_cost_open_reception` beside its custom affordability predicate.
`localisation\english\migration_l_english.yml`, lines 78-86, supplies the base, exact base aliases for both native suffixes, and separate ready/blocked resource strings.
`common\scripted_localisation\migration_reception_preparation_cost_scripted_localisation.txt`, lines 5-30, maps each resource getter to its own ready or blocked localisation key.
The texticon names resolve to `GFX_support_equipment_text_icon` in `interface\chaosx_texticons.gfx`, lines 89-93, and installed `interface\texticons.gfx`, lines 122-126 and 261-265, for `GFX_fuel_texticon` and `GFX_pol_power`.
These reads establish the current source chain and a reusable alias pattern; they do not establish native rendering or a player's observed raw key.
All inspected consumer, getter, localisation, and sprite sources were left unchanged.

## MCP boundary

The parent reports that correctly formed reference context and narrow custom-cost context/search calls each reached an actual 600-second timeout.
This is a connected-route timeout, not tool absence.
The parent explicitly instructed this subagent not to duplicate those heavy calls.
No reference MCP call was attempted by this subagent, and this handoff claims direct local source review only.
No service-health, engine execution, visual rendering, or runtime evaluation is claimed.

## Preservation, validation, and parent commit

Captured the pre-edit working skill and reviewed its existing mixed diff before patching.
The preexisting fractional-quote paragraph and paid finite-registry release-receipt section remain intact.
Comparison after removing only the owned addition and normalizing line endings found every preexisting text line unchanged.
The official `quick_validate.py` accepted the updated skill when invoked with `python -X utf8`; this validates skill packaging, not engine behavior or the quality of runtime cost rendering.
Content review confirmed that the paragraph neither duplicates affordability/payment rules nor claims raw-key observations from missing source coverage.

The working diff combines this paragraph with nearby other-owner changes in one displayed hunk.
The parent must construct and review a patch containing only the four added sentence lines and separating blank line against its chosen index/base, rather than staging the whole displayed hunk or whole skill.
Keep the previously staged or unstaged work intact under the shared Git workflow.
This subagent did not change the index or create a commit.

No blocker, omission, or simplification remains for this bounded skill edit.
Parent review and the parent-owned mixed-hunk commit remain pending.
