# Event 31 Random Terror asset prompt

## Task

Close the remaining Event 31 visual asset work.
The full asset package is produced and wired.
Its families, counts and consumers are listed in the [Part 11 Implementation status](031_random_terror_spec_part_11_assets_presentation_and_localisation.md#implementation-status), and the row-level record is the [visual asset inventory](../../plans/031_random_terror_plans/031_random_terror_visual_asset_inventory.md).

Read `CLAUDE.md` sections 2 and 8, the `chaos-redux-event-assets` skill, Part 11, and the [visual asset audit](../../plans/031_random_terror_plans/031_random_terror_visual_asset_audit.md).
Route work through the [routing table](031_random_terror_subagent_routing_prompts.md): portraits to `chaosx_portrait_creator`, icons to `chaosx_icon_artist`, scene and flag art to `chaosx_generated_event_art`.
The parent owns `.gfx`, localisation and gameplay wiring.

## Open work

1. Entity portrait binding: Event Details shows the animated entity for Evolution V before the revelation. Bind the animation to the terminal state and show `GFX_Portrait_Random_Terror_Entity_Static_Fallback` before it (Part 8). This is a shared-window selector change for the parent, not an Event 31 GUI.
2. Supply Collapse idea icon: the actor economy failure form is renamed from Famine (Part 5). Reuse `idea_random_terror_famine.dds` only if its art reads as broken supply rather than hunger. Otherwise commission one replacement idea icon and keep the sprite name stable after registration.
3. Deaths tab: check whether the three new Event 31 Deaths reasons (Part 10) need a cause icon in the shared Deaths tab, and register any icon before requesting art.
4. Inventory refresh: update the 36 stale achievement hashes and add the two map-mode buttons.
5. Flag cycle: record a disposition for the asset plan's distinct ordinary actor flags versus the implemented 16 active and 8 dormant identities.
6. Provenance gaps: the submitted portrait image prompts and two source-to-DDS equality records are missing. Recover them or record the exact gap. Do not reconstruct prompts after the fact.

No other new art is needed for the audit revisions: the hostage approach is an event option, and the aftermath accounting event reuses the defeat and reconstruction report art.

## Rules that stay fixed

- No real extremist name, flag, emblem, uniform or propaganda, no sacred Islamic calligraphy as hostile branding, no depiction of Allah, and no ethnic, religious or national caricature.
- Period-authentic 1936 to 1945 treatment, no generated readable text, no gore.
- Native transparency for icons and overlays, and the background treatment of the real consumer for scenes, flags and portraits.
- Every replaced or added file gets an inventory row with source, processing, final path, sprite, consumer and hash.
