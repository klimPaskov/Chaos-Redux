# Fallout Seed Vault Custody chain proof

Status: implemented as a dormant reviewed-candidate tranche. It is not
countable toward the 660 block release floor and has no activation setter.

## Ownership and identity

- Namespace: `chaosx.fallout`
- Event suffixes: `188` through `200`
- Candidate id: `188`
- Transaction key: `710007`
- Candidate route: `7107`
- Event Log history id: `9112`
- Gameplay effect file: `common/scripted_effects/fallout_world_end_seed_vault_event_effects.txt`
- Trigger file: `common/scripted_triggers/fallout_world_end_seed_vault_event_triggers.txt`
- Event picture sprite: `GFX_fallout_seed_vault_report`

The chain is Fallout-owned. It does not reference zombie events, zombie assets,
zombie audio, zombie sprites, or zombie paths.

## Trigger contract

The candidate selects the lowest valid owned state with a current Fallout state
identity and durable resource row. The state must retain one of the reviewed Air
Winter seed-memory flags, a produced Air Winter snapshot, reclamation above the
minimum band, adaptation above the minimum band, and a current transition
generation. The country must be able to pay the selected policy cost. A state
registry flag prevents a second selection while the chain is open.

The opening, result, callback, and cleanup triggers revalidate the exact state,
owner, generation, ordinary receipt, delayed receipt, branch, and event token.
Missing state identity or stale ownership fails closed.

## Chain surface

1. Event `188` presents four policies. The state reserve can be nationalized,
   entrusted to field cooperatives, shared with a proven ally, or sold through a
   licensed auction.
2. Event `189` selects a deterministic hidden AI policy using the same target
   values and cost gates.
3. Events `190` through `193` present the human delayed result for each policy.
4. Events `194` through `197` resolve the same four result lanes for AI.
5. Events `198` and `199` run the agronomist callback for human and AI.
6. Event `200` releases both delayed rows through the authenticated cleanup path.

The score uses Air Winter food, reclamation, adaptation, and water values with
current country recognition where the bilateral policy needs it. Every branch
has success, partial, and failure outcomes. Failure uses the Deaths-backed exact
state population loss helper with a small reviewed percentage. Results change
food, reclamation, adaptation, clean water, recognition, cohesion, stability,
and timed institutional modifiers. State memory distinguishes each policy and
outcome. The callback records a living agronomist charter, a contested review,
or a failed harvest memory.

## Event Log and localisation

History `9112` has fifteen explicit payloads, four policy bands with three
outcomes each, and three callback outcomes. The detail selector lives in
`common/scripted_localisation/fallout_world_end_seed_vault_event_log_scripted_localisation.txt`.
The Event Log name and detail mapping is registered in
`common/scripted_localisation/chaosx_scripted_localisation_events_log.txt` and
the history id is accepted by the event detail routing effect.

Player-facing text names the rail-cut archive, field cooperatives, clean-water
convoys, and the first protected plots. It contains no em dash or semicolon and
does not describe implementation history.

## Asset proof

The dedicated report package is under `docs/assets/fallout_seed_vault/` with a
retained generated source, processed 210 by 176 preview, prompt provenance,
manifest, and final legacy BGRA DDS at
`gfx/event_pictures/fallout/seed_vault_report.dds`. The sprite is
registered in `interface/fallout_world_end.gfx` and human events `188`, `190`,
`191`, `192`, `193`, and `198` reference it. The scene is fictional, contains
no readable text, and uses no existing Fallout or zombie art.

## Review boundary

Static review covers unique ids, balanced blocks, event token alignment,
parallel candidate arrays, localization keys, BOM encoding, history payloads,
dynamic modifier consumers, and DDS header facts. No HOI4 process was launched.
The scheduler activation flags remain unset, so no runtime event count is
claimed. Save recovery, host authority, multiplayer synchronization, delayed
timing, dynamic modifier presentation, and the normal map result remain
unobserved until a permitted runtime pass.
