# Event 016 Mengele Strategic Singularity terminal adapter

## Purpose and scope

These COUNTRY-scope scripted effects let the registered Mengele Directorate submit its completed Strategic Singularity through the existing source-aware Fallout request, lock, and super-event queue.
They preserve Kruger's project, component, and terminal receipts while sharing the canonical world-end scenario and consequence values.

`brilliant_scientist_mengele_execute_singularity_terminal` is the public entry from the Directorate decision and the existing hidden retry event `chaosx.nr16.901`.
`brilliant_scientist_mengele_finalize_singularity_after_fallout_lock` is called only in the saved `fallout_request_actor` scope after the shared Fallout lock sets `world_end`.
The prelock gate requires the private Weaponization receipt, the DLC-appropriate component route, three controlled qualifying facilities, the private live two-node/two-link network, scenario settings, and a valid provider.

## Inputs, outputs, and defaults

The public entry accepts no caller-supplied selector.
The first authorized call records `mengele_event016_singularity_terminal_committed` and one-time private prelock Chaos and consequence receipts.
`mengele_event016_singularity_fallout_request_submitted` owns the queued request; rejection clears it, records a private rejection and retry count, and schedules one retry while the programme remains valid.
The persistent `mengele_event016_singularity_detonation_date` is recorded once at first submission.
The private `mengele_event016_singularity_terminal_fired` flag records the accepted lock once, while submitted, rejected, and pending retry flags are cleared.
The finalizer also records the shared `brilliant_scientist_singularity_terminal_fired` route lock without writing a Kruger country receipt.

The existing shared Fallout request receives `fallout_request_source.strategic_singularity`, `fallout_request_intensity.maximum`, and a regular actor target.
The shared coordinator revalidates the saved actor's provider, physical network, facilities, stage, scenario, and submitted receipt before locking the world-end state, then dispatches to the private finalizer for this actor or to the existing Kruger finalizer for its actor.
The private finalizer sets the shared Strategic Singularity world-end identity and queues the existing Strategic Singularity super-event with `THIS`, the saved provider actor, because a later coordinator callback need not retain that actor as `ROOT`.
The Kruger threat activation stores `brilliant_scientist_world_threat_actor` as a global event target; ordinary threat shutdown, defeat, and Kruger terminal paths clear it, while this provider terminal uses it to settle a separate active Kruger threat interval before clearing the shared source marker.

## Side effects and failure behavior

Prelock Chaos raises the shared meter above the final threshold once using the existing Event 016 Singularity history reason.
The one-time provider consequence uses the existing civilian and military death, air-contamination, condemnation, unconventional-weapon, and treaty values.
These are private one-time receipts, so request rejection and retry never repeat them.
An invalid provider or lost physical network prevents a new request and retry, while an already locked valid request finalizes through its saved actor after `world_end` makes ordinary prelock provider gates false.
The shared Fallout validation rejects a strategic request whose saved actor lacks the matching submitted receipts.
The actor finalizer calls provider receipt cleanup after recording the durable fired flag and queuing presentation.

Example: after private Weaponization and site construction, `brilliant_scientist_mengele_execute_singularity_terminal = yes` on the registered Directorate submits the existing Fallout request; the shared lock invokes `brilliant_scientist_mengele_finalize_singularity_after_fallout_lock = yes` in that same saved country scope.

## Presentation, assets, and future work

The terminal decision reuses `GFX_decision_brilliant_scientist_project_strategic_singularity_weaponization` from `interface/016_brilliant_scientist_project_icons.gfx` and its `gfx/interface/decisions/016_brilliant_scientist/projects/strategic_singularity_weaponization.dds` texture.
The shared super-event keeps its existing art and sound consumers; no new terminal icon, image, sound, or 3D geometry is introduced.
The private physical construction decisions and provider cleanup are documented in `016_mengele_singularity_construction_effects.md` and `docs/events/016_brilliant_scientist/systems/mengele_singularity_construction.md`.
Full CXT fixtures, catalog alignment, and final event/MCP audits remain outstanding before Event 016 can be presented for live acceptance.
