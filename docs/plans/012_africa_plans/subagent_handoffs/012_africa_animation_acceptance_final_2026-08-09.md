# Event 012 Africa animation acceptance handoff

Date: 2026-08-09. Scope is limited to the 18 accepted animation rows and their runtime sprite registrations. No gameplay, localisation, scripted GUI, decision, focus, event, or shared GFX files were changed.

## Acceptance result

All 18 rows pass the bounded visual and file audit. Every row has separately authored source frames, exact processed frames, a horizontal sheet PNG, a static fallback PNG, runtime sheet DDS, runtime static DDS, review GIF, row contact sheet, brief, frame plan, and manifest evidence. Source and processed frame hashes are unique within each row; no empty alpha tiles, repeated tiles, drifted silhouettes, or broken contact-sheet tiles were found. No repair or ImageGen regeneration was needed.

The overall review sheet is [animation_acceptance_contact.png](../../../assets/012_africa/animations/animation_acceptance_contact.png), with one labeled row per accepted key on transparency checkerboards.

Accepted rows:

- `colonial_pressure_border` — 96x96, 8 frames, 6 FPS, looping.
- `selected_member_confidence` — 64x64, 8 frames, 8 FPS, looping.
- `congress_ready_emblem` — 72x72, 8 frames, 6 FPS, looping.
- `member_departure_warning` — 72x72, 10 frames, 8 FPS, looping.
- `rival_bloc_alert` — 72x72, 8 frames, 6 FPS, looping.
- `africa_is_one_completion` — 128x128, 12 frames, 8 FPS, non-looping.
- `ecological_wrath_active` — 96x96, 10 frames, 6 FPS, looping.
- `continent_war_terminal` — 128x128, 12 frames, 8 FPS, looping.
- `host_overlay_federal_amalgamation` — 64x64, 3 frames, 4 FPS, non-looping.
- `covenant_obligation_review_states` — 64x64, 8 frames, 6 FPS, looping.
- `priority_member_promotion_card` — 64x64, 8 frames, 6 FPS, looping.
- `route_capstone_seal_family` — 64x64, 8 frames, 8 FPS, non-looping.
- `host_first_proof_state_kit` — 64x64, 6 frames, 6 FPS, non-looping.
- `federal_deadlock_warning` — 64x64, 3 frames, 5 FPS, non-looping.
- `republic_first_election_states` — 64x64, 8 frames, 8 FPS, looping.
- `military_commander_loyalty_states` — 64x64, 8 frames, 6 FPS, looping.
- `confederal_emergency_ratification_states` — 64x64, 8 frames, 6 FPS, looping.
- `postwar_constitutional_review_states` — 64x64, 8 frames, 6 FPS, looping.

## Runtime registration

[interface/012_africa_animations.gfx](../../../interface/012_africa_animations.gfx) registers one `frameAnimatedSpriteType` plus one static fallback `spriteType` for each of the 18 rows (36 unique sprite IDs total). Animated entries use the exact runtime sheet DDS, `noOfFrames`, `animation_rate_fps`, `looping`, `play_on_show = yes`, `loadType = "INGAME"`, `transparencecheck = yes`, `alwaystransparent = yes`, and vanilla-proven `effectFile = "gfx/FX/buttonstate_blendframes.lua"`. Static entries point to the matching runtime DDS pair; no registration points into `docs/assets/`.

The row manifests under `docs/assets/012_africa/animations/*/manifest.md` record actual source/processed/sheet/static/GIF/contact hashes and runtime paths. Runtime DDS checks covered all 18 sheets and all 18 static files: legacy one-level uncompressed BGRA 32-bit headers, one mip, declared canvas dimensions, exact payload lengths, and alpha-bearing output.

## Ownership boundary

This handoff claims asset production, visual QA, DDS integrity, and GFX registration. Parent integration bound `host_first_proof_state_kit`, `priority_member_promotion_card`, `federal_deadlock_warning`, `republic_first_election_states`, `military_commander_loyalty_states`, `confederal_emergency_ratification_states`, `covenant_obligation_review_states`, and `postwar_constitutional_review_states` to their exact decision selectors in `common/decisions/012_africa_decisions.txt`. The remaining state animations are reserved for the Event 012 Charter League GUI and route-capstone consumer pass. Live runtime validation remains user-owned.

No simplifications, substitutions, or unapproved fallbacks were made. No commit was created per parent instruction; the parent should stage only the bounded asset, registration, and handoff files listed above.
