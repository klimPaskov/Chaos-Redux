# Event 014 Siege Eaters v8 source record

Status: selected for `reference_only_user_authorized` use and parent-approved by exact checksum; provider generation is blocked by insufficient credits.

## Selected modern designed artwork

- Direct image: https://imgcdn.gamefound.com/richtextimage/richtext/320075a9-c6d1-4ff2-ac13-d99e6a875f59.jpg
- Official campaign page: https://gamefound.com/en/projects/chip-theory-games/the-elder-scrolls
- Publisher terms reviewed: https://chiptheorygames.com/policies/terms-of-service
- Title/description: horned-skull warrior holding a massive two-handed spiked mace, promotional artwork for Chip Theory Games' The Elder Scrolls campaign.
- Creator/publisher: individual artist not identified on the reviewed pages; publisher/project owner identified as Chip Theory Games.
- Retrieval date: 2026-08-24.
- Source archive: `chip_theory_elder_scrolls_horned_skull_mace_warrior.jpg`.
- Source SHA-256: `59342677E01A84D57A097FE464D5CC4A101569894B4DA7BF9FF2267363E09D7F`.
- Rights decision: no reuse license was stated and no explicit NoAI, no-derivatives, or equivalent prohibition was found on the reviewed official campaign and publisher terms. The individual artist remains unresolved. This artwork is therefore accepted only under the user's explicit reference-only authorization; source pixels are non-shipping evidence and are not runtime art.
- Association uncertainty: the static campaign HTML snapshot did not expose the CDN UUID. The campaign association rests on the parent-provided official lead and the official Gamefound/Chip Theory context.

## Source fit

The artwork depicts a living, fully colored, full-body humanoid siege warrior with a readable bone-and-leather silhouette, horned skull headdress, complete anatomy, a two-handed overhead grip, and one massive spiked mace. It does not depict modern equipment, plate-knight armor, a documentary or ethnographic subject, or an undead body.

## Source-informed refinement

Native ImageGen was instructed to preserve the sourced identity, anatomy, proportions, pose, horned skull headdress, bone-and-leather armor, clothing, footwear, spikes, exact mace, and two-handed grip. The only permitted changes were isolation, cleanup/upscaling, conspicuous culturally neutral charcoal-black and muted iron-red siege paint, and restrained dried blood, dust, and grime. Knights, plate armor, undead anatomy, Indigenous or sacred motifs, modern tactical equipment, firearms, extra people or limbs, changed grip, and text were prohibited.

ImageGen returned a baked checkerboard instead of native alpha twice. The required fallback was therefore applied locally. U2Net alpha matting, U2Net without matting, and ISNet were rejected for internal damage, white halos, or checker fringe. The selected deterministic extraction removes border-connected near-neutral checker pixels, retains one connected foreground component, applies a 0.65-pixel Gaussian alpha edge, and decontaminates fringe RGB from the nearest opaque subject color.

- Final Meshy input: `../../original/meshy_input.png`.
- Final SHA-256: `1AC18B9B008CCCC70BC0AF30605CA72ADCC9030A1C233732559400C9A6744F75`.
- Final dimensions/mode: 1055x1491 RGBA.
- Alpha evidence: range 0-255; all four corners transparent; one visible foreground component; bbox `[194, 17, 952, 1408]`.
- Comparison: `source_to_refinement_comparison.png`.
- Comparison SHA-256: `CDE376E9703D4A4E5DF993048F7BAD0F9CF339830BB8D5A7B5176C411600A25B`.
- Parent approval: approved exact SHA-256 on 2026-08-24. The subsequent locked Meshy 7 call returned HTTP 402 before task creation and consumed zero credits.
