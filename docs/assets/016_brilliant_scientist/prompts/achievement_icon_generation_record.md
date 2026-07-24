# Event 016 achievement icon generation record

Source mode: built-in `$imagegen` using the official image-generation skill (`gpt-image-2` path). One generation call was used for each of the seventeen identities. The generated masters are retained under `docs/assets/016_brilliant_scientist/source_png/` at 1254x1254 RGB and are the editable source evidence for this package.

Shared prompt constraints applied to every call: compact nearly square dark steel-and-bronze achievement plaque; aged 1930s-1940s grand-strategy finish; integrated laurel or riveted edge; crisp high-contrast silhouette that remains legible at 64x64; plaque fills about 88% of a square canvas; perfectly flat solid `#00ff00` chroma-key background; no shadows, gradients, texture, reflections, floor plane, vignette, cast shadow, text, letters, numbers, watermark, logo, checkerboard, white halo, sticker rim, modern UI, generic Kruger portrait, or tiny-detail-dependent identity. The chroma-key background was removed with `remove_chroma_key.py` using border auto-key, soft matte, despill, and the documented thresholds.

The identity-specific prompts are preserved in [`achievement_icon_prompts.md`](achievement_icon_prompts.md). The generated source-to-output mapping is:

| Achievement id | Source master | Completed composition |
| --- | --- | --- |
| `016_brilliant_scientist_borrowed_century` | `source_png/016_brilliant_scientist_borrowed_century.png` | Period calendar overtaken by vacuum tube, rocket arc, atom orbit, industrial gear, and medical lens. |
| `016_brilliant_scientist_every_door` | `source_png/016_brilliant_scientist_every_door.png` | Six different laboratory doors around an impossible white-violet central light. |
| `016_brilliant_scientist_public_method` | `source_png/016_brilliant_scientist_public_method.png` | Open technical folio and precision instrument supported by different ordinary hands. |
| `016_brilliant_scientist_the_one_who_left` | `source_png/016_brilliant_scientist_the_one_who_left.png` | Lone scientist crossing a hard border between contrasting laboratory skylines with a sealed prototype case. |
| `016_brilliant_scientist_clean_break` | `source_png/016_brilliant_scientist_clean_break.png` | Laboratory key beside an intact national academy and open gate in calm daylight. |
| `016_brilliant_scientist_approve_everything` | `source_png/016_brilliant_scientist_approve_everything.png` | Government fountain pen signing beneath incompatible project diagrams. |
| `016_brilliant_scientist_the_former_host` | `source_png/016_brilliant_scientist_the_former_host.png` | Conventional soldiers entering a reclaimed laboratory past clone, machine, and beast silhouettes. |
| `016_brilliant_scientist_combined_arms_redefined` | `source_png/016_brilliant_scientist_combined_arms_redefined.png` | Clone infantry, heavy robots, and paleogenetic beast beneath one command-and-supply emblem. |
| `016_brilliant_scientist_clever_girl` | `source_png/016_brilliant_scientist_clever_girl.png` | Predatory dinosaur entering a monumental period great-power capital skyline. |
| `016_brilliant_scientist_the_machine_continues` | `source_png/016_brilliant_scientist_the_machine_continues.png` | Empty high-backed chair before branching command network, robot nodes, and government core. |
| `016_brilliant_scientist_population_one` | `source_png/016_brilliant_scientist_population_one.png` | Repeated human profiles resolving into distinct individuals within a civic register. |
| `016_brilliant_scientist_yesterday_sent_help` | `source_png/016_brilliant_scientist_yesterday_sent_help.png` | Two defensive-line versions joined by broken clock and phase ring. |
| `016_brilliant_scientist_not_from_here` | `source_png/016_brilliant_scientist_not_from_here.png` | Human laboratory silhouette split with nonhuman anatomy, alien interface, and stellar vector. |
| `016_brilliant_scientist_no_second_sun` | `source_png/016_brilliant_scientist_no_second_sun.png` | Dark singularity core safely opened beneath an ordinary unbroken sky. |
| `016_brilliant_scientist_the_last_calculation` | `source_png/016_brilliant_scientist_the_last_calculation.png` | Calculation grid and surrender gauge collapsing toward a destructive global core. |
| `016_brilliant_scientist_the_world_is_the_laboratory` | `source_png/016_brilliant_scientist_the_world_is_the_laboratory.png` | Globe transformed into integrated laboratory nodes, power lines, rails, and command emblem. |
| `016_brilliant_scientist_ordinary_people_won` | `source_png/016_brilliant_scientist_ordinary_people_won.png` | Human, clone, and mechanical hands rebuilding one damaged laboratory around a civic flame. |

The grey state is a mechanical grayscale conversion of the completed 64x64 RGBA PNG. The not-eligible state is a mechanical alpha composite of that grey PNG with the canonical overlay at `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/achievements/overlay.png`; no identity art is redrawn or substituted.
