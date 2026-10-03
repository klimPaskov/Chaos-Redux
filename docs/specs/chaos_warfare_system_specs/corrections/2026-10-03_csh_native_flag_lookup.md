# Scientific Office native flag lookup

Disposition: implemented in source and native asset files, with header, pixel, orientation, and parent visual review complete; fresh engine warning absence remains unverified.

Acceptance basis: the user's 2026-10-03 13:20 live-QA report confirms missing democratic and neutrality CSH flag lookups in all three native folders after `cab3acb5b`, both during loading and on 1 January 1936.
The user explicitly requests 32-bit uncompressed bottom-left TGA files, with a base filename and the required ideology variants, or a valid native flag path.
Parent implementation chooses direct native files and complete four-ideology coverage.

The Scientific Office retains its stateless history-holder role, country identity, roster, and transfer logic.
Its native assets are `CSH.tga`, `CSH_democratic.tga`, `CSH_neutrality.tga`, `CSH_fascism.tga`, and `CSH_communism.tga` under `gfx/flags/`, `gfx/flags/medium/`, and `gfx/flags/small/`.
Normal flags are 82×52, medium 41×26, and small 10×7, using one documented institutional design shared across all ideology lookup aliases.
The office is not an ideological polity, and the aliases do not introduce political or gameplay variants.
Native filename lookup supplies the consumer; no sprite registry, cosmetic route, or scripted UI workaround is introduced.

The previous country audit's latent flag gap is a confirmed load defect under the new live evidence.
It is caused by the incomplete CSH country asset package and must be repaired with native files, despite the holder having no territory or playable route.
The [asset manifest](../../../assets/cbrn_scientist_holder_flags/manifest.md) records the generated master, processing, runtime files, format checks, and visual review.

The [scientist source check](../../../testing/2026-10-03_csh_flag_load_repair/scientist_source_check.json) finds only history-time recruitment for Haldane, Fishman, and Velikanov and no runtime recruitment commands in the dated startup owner.
Their guarded CSH-origin transfers are unchanged by this asset correction.
The archived cycle1 log still has its original pre-holder hash and warnings; it does not certify the latest live run's warning absence.
No fresh clean full error log or newly observed character transfer is claimed by this correction.

The [format-validation record](../../../testing/2026-10-03_csh_flag_load_repair/flag_format_validation.json) verifies all fifteen required names, exact native sizes and payload lengths, uncompressed 32-bit bottom-left headers, opaque alpha, and decoded equality with processed previews.
The native TGA first pixel also matches the corresponding decoded bottom-left pixel for every file.
No country, history, roster, or transfer script is changed by this repair, and no new gameplay benefit is introduced.
