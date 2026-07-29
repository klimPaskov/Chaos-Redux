# Event 016 Idea and National-Spirit Icon GFX Handoff

Parent agent owns the `.gfx` edit, gameplay references, localisation alignment, visual review, and final commit. This tranche edits no `.gfx`, `.gui`, idea, event, localisation, focus, decision, or spreadsheet file.

## Wiring contract

Add the thirteen `spriteType` entries below to the existing Event 016 idea-icon `.gfx` surface chosen by the parent, following that file's established formatting. Do not create duplicate sprite names if a pre-registered Event 016 surface already exists. Each `name` is the recommended picture token expected by the manifest and each `texturefile` is the runtime path relative to the mod root.

```text
spriteType = {
	name = "GFX_idea_brilliant_scientist_kruger_appointment"
	texturefile = "gfx/interface/ideas/016_brilliant_scientist/idea_brilliant_scientist_kruger_appointment.dds"
}
spriteType = {
	name = "GFX_idea_brilliant_scientist_kruger_method"
	texturefile = "gfx/interface/ideas/016_brilliant_scientist/idea_brilliant_scientist_kruger_method.dds"
}
spriteType = {
	name = "GFX_idea_brilliant_scientist_national_scientific_dependence"
	texturefile = "gfx/interface/ideas/016_brilliant_scientist/idea_brilliant_scientist_national_scientific_dependence.dds"
}
spriteType = {
	name = "GFX_idea_brilliant_scientist_public_scientific_renaissance"
	texturefile = "gfx/interface/ideas/016_brilliant_scientist/idea_brilliant_scientist_public_scientific_renaissance.dds"
}
spriteType = {
	name = "GFX_idea_brilliant_scientist_controlled_secret_compact"
	texturefile = "gfx/interface/ideas/016_brilliant_scientist/idea_brilliant_scientist_controlled_secret_compact.dds"
}
spriteType = {
	name = "GFX_idea_brilliant_scientist_unrestricted_laboratory_state"
	texturefile = "gfx/interface/ideas/016_brilliant_scientist/idea_brilliant_scientist_unrestricted_laboratory_state.dds"
}
spriteType = {
	name = "GFX_idea_brilliant_scientist_scientific_vacuum"
	texturefile = "gfx/interface/ideas/016_brilliant_scientist/idea_brilliant_scientist_scientific_vacuum.dds"
}
spriteType = {
	name = "GFX_idea_brilliant_scientist_improvised_laboratory_state"
	texturefile = "gfx/interface/ideas/016_brilliant_scientist/idea_brilliant_scientist_improvised_laboratory_state.dds"
}
spriteType = {
	name = "GFX_idea_brilliant_scientist_inherited_project_portfolio"
	texturefile = "gfx/interface/ideas/016_brilliant_scientist/idea_brilliant_scientist_inherited_project_portfolio.dds"
}
spriteType = {
	name = "GFX_idea_brilliant_scientist_fragmented_command"
	texturefile = "gfx/interface/ideas/016_brilliant_scientist/idea_brilliant_scientist_fragmented_command.dds"
}
spriteType = {
	name = "GFX_idea_brilliant_scientist_experimental_supply_chain"
	texturefile = "gfx/interface/ideas/016_brilliant_scientist/idea_brilliant_scientist_experimental_supply_chain.dds"
}
spriteType = {
	name = "GFX_idea_brilliant_scientist_scientific_exodus"
	texturefile = "gfx/interface/ideas/016_brilliant_scientist/idea_brilliant_scientist_scientific_exodus.dds"
}
spriteType = {
	name = "GFX_idea_brilliant_scientist_world_threat_project_state"
	texturefile = "gfx/interface/ideas/016_brilliant_scientist/idea_brilliant_scientist_world_threat_project_state.dds"
}
```

## Parent wiring checklist

1. Visually review `contact_sheets/processed_decoded_contact_sheet.png` at native-size intent and enlarged scale, checking that the symbols remain readable over the in-game idea surface.
2. Register the thirteen sprite names in the existing Event 016 idea or national-spirit `.gfx` file and keep the texture paths exactly as shown.
3. Replace only the Event 016 idea or national-spirit picture tokens that correspond to these concepts with the matching `GFX_idea_brilliant_scientist_<stem>` names.
4. Keep any existing Kruger portrait or advisor DDS files untouched. These files are separate idea icons and are not replacements for portrait or dossier art.
5. Do not use the contact sheets as runtime assets. Runtime references must point to `gfx/interface/ideas/016_brilliant_scientist/*.dds`.
6. Preserve the `validation.tsv` evidence and record the parent visual-review outcome in the Event 016 plan or spec before the final commit.

## Asset-by-asset handoff

| Stable stem | Sprite name | Runtime DDS | Intended spirit use |
|---|---|---|---|
| `idea_brilliant_scientist_kruger_appointment` | `GFX_idea_brilliant_scientist_kruger_appointment` | `gfx/interface/ideas/016_brilliant_scientist/idea_brilliant_scientist_kruger_appointment.dds` | Appointment and first institutional acceptance |
| `idea_brilliant_scientist_kruger_method` | `GFX_idea_brilliant_scientist_kruger_method` | `gfx/interface/ideas/016_brilliant_scientist/idea_brilliant_scientist_kruger_method.dds` | Method adoption and scientific discipline |
| `idea_brilliant_scientist_national_scientific_dependence` | `GFX_idea_brilliant_scientist_national_scientific_dependence` | `gfx/interface/ideas/016_brilliant_scientist/idea_brilliant_scientist_national_scientific_dependence.dds` | National dependence on Kruger institutions |
| `idea_brilliant_scientist_public_scientific_renaissance` | `GFX_idea_brilliant_scientist_public_scientific_renaissance` | `gfx/interface/ideas/016_brilliant_scientist/idea_brilliant_scientist_public_scientific_renaissance.dds` | Public scientific renewal |
| `idea_brilliant_scientist_controlled_secret_compact` | `GFX_idea_brilliant_scientist_controlled_secret_compact` | `gfx/interface/ideas/016_brilliant_scientist/idea_brilliant_scientist_controlled_secret_compact.dds` | Controlled confidential cooperation |
| `idea_brilliant_scientist_unrestricted_laboratory_state` | `GFX_idea_brilliant_scientist_unrestricted_laboratory_state` | `gfx/interface/ideas/016_brilliant_scientist/idea_brilliant_scientist_unrestricted_laboratory_state.dds` | Unrestricted laboratory governance |
| `idea_brilliant_scientist_scientific_vacuum` | `GFX_idea_brilliant_scientist_scientific_vacuum` | `gfx/interface/ideas/016_brilliant_scientist/idea_brilliant_scientist_scientific_vacuum.dds` | Scientific collapse or absence |
| `idea_brilliant_scientist_improvised_laboratory_state` | `GFX_idea_brilliant_scientist_improvised_laboratory_state` | `gfx/interface/ideas/016_brilliant_scientist/idea_brilliant_scientist_improvised_laboratory_state.dds` | Salvaged improvised laboratory governance |
| `idea_brilliant_scientist_inherited_project_portfolio` | `GFX_idea_brilliant_scientist_inherited_project_portfolio` | `gfx/interface/ideas/016_brilliant_scientist/idea_brilliant_scientist_inherited_project_portfolio.dds` | Inherited projects after transfer or recovery |
| `idea_brilliant_scientist_fragmented_command` | `GFX_idea_brilliant_scientist_fragmented_command` | `gfx/interface/ideas/016_brilliant_scientist/idea_brilliant_scientist_fragmented_command.dds` | Fragmented command state |
| `idea_brilliant_scientist_experimental_supply_chain` | `GFX_idea_brilliant_scientist_experimental_supply_chain` | `gfx/interface/ideas/016_brilliant_scientist/idea_brilliant_scientist_experimental_supply_chain.dds` | Experimental supply and procurement network |
| `idea_brilliant_scientist_scientific_exodus` | `GFX_idea_brilliant_scientist_scientific_exodus` | `gfx/interface/ideas/016_brilliant_scientist/idea_brilliant_scientist_scientific_exodus.dds` | Researcher and knowledge exodus |
| `idea_brilliant_scientist_world_threat_project_state` | `GFX_idea_brilliant_scientist_world_threat_project_state` | `gfx/interface/ideas/016_brilliant_scientist/idea_brilliant_scientist_world_threat_project_state.dds` | World-threat project governance |

## Validation evidence

`validation.tsv` contains thirteen rows. All rows report 64x64 processed and decoded dimensions, DDS dimensions 64x64, DDS header size 124, pixel format size 32, flags 65, 32-bit pixels, BGRA masks, texture caps `0x1000`, file length 16512 bytes, transparent corners, and `pixel_equal_processed_decoded=True`. All thirteen rows are marked `complete`.

## Simplifications, placeholders, and blockers

No simplifications or placeholders were used. No icon is a resize, recolor, or crop of a focus icon. No animation was requested for this family. There are no known blockers. Parent visual review and `.gfx` wiring remain intentionally outstanding because those actions are outside this subagent's granted scope.
