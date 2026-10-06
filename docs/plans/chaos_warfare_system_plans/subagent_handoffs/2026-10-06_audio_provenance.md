# Chaos Assault Battalion audio provenance audit

Audit date: 2026-10-06. Scope: read-only review of the nine shipped chaos_assault_battalion runtime WAVs, the archived 2026-09-12 recovery evidence, the exact idle-breath source page, and installed vanilla infantry voice consumers.

Status: The idle-breath WAV has an exact sample-for-sample source match to the archived primbal recording under CC0. The other eight shipped WAVs remain blocked for provenance: the preserved repository/job evidence does not identify exact sources, and the recorded source-matching pass found no plain crop/gain match against its archived candidates. The per-subunit selection-voice claim in the older model note needs parent correction: vanilla also exposes country/original-tag infantry voice groups, but they apply to the tag’s infantry family rather than an individual subunit.

## Scope and disposition

This is a completed provenance audit, not runtime acceptance. The overall shipped sound package remains blocked while eight runtime cues lack exact source lineage and CBRN-specific selection voice cannot be bound separately where ordinary and CBRN infantry share a country/original tag.

Only this handoff and its adjacent JSON crosswalk were created. No runtime WAV, sound definition, entity asset, model file, or source candidate changed. No Meshy, Blender, paid, download, audio-processing, or game-launch operation occurred; cost was $0. The Meshy key gate was not applicable because this was a read-only audit with no Meshy work.

## Proven idle-breath lineage

The archived source page is [OpenGameArt: horror breathing](https://opengameart.org/content/horror-breathing), by primbal, published 2023-02-09. The page lists CC0 and says attribution is not required, with optional credit to primbal. It links https://opengameart.org/sites/default/files/horrorbreathing.zip; the archived receipt dates retrieval 2026-09-12. I rechecked the live page on 2026-10-06. Its archived HTML SHA-256 is 7501A5035D4DF8BA321C359FF2F027CE17816F554AE747C23540712EC700E4A6.

The downloaded ZIP SHA-256 is 5984AA9D197885AB110C31EA0BA382D3F47D12B93449F8942E1CF96B0449462C. The archived extracted horrorbreathing.wav SHA-256 is C6BA78F40B9F5A1C9A3BDDCEB580FEC137DAE12861C95B82688D1DCFB13FC45A. It is stereo, signed PCM16, 44,100 Hz, with 275,796 frames. The shipped chaos_assault_battalion_idle_breath.wav SHA-256 is 222DEBCB8972EDAED5B4B34A620714065CB003836C3FA9FCFCE935FB18746B9F; it is mono IEEE float32, 44,100 Hz, with the same 275,796 frames.

Independent comparison decoded the source PCM16 to normalized float32, multiplied each channel by float32 1/sqrt(2), summed in float32, and compared every resulting frame to the shipped float32 samples. All 275,796 frames match exactly: maximum absolute residual 0.0, mean residual 0.0, no offset, trim, or resampling. This proves the idle recording’s source and its channel-conversion lineage; it does not attribute any other runtime cue.

## Eight unresolved shipped cues

The existing sound-definition header says every runtime WAV is mechanically derived from an immutable CC0 source. Exact evidence now supports that statement for the idle file only. The 2026-09-12 derived candidates have status needs_user_review and runtime_wiring parent-owned; not copied; the prior handoff and manifest do not bind those candidates to these eight shipped files.

The pre-existing read-only match report at .git/cbrn_takeover_20261006/audio_source_matching.json reports no plain crop/gain waveform match for the remaining files. Its highest candidate scores are all below 0.35. This is bounded negative evidence: it does not exclude tempo or pitch changes, other processing, layering, a source absent from the recovery archive, or an earlier source retained elsewhere. Do not promote the candidate sources to runtime attribution without a matching source receipt or a defensible transformation lineage.

| Runtime cue | Current runtime SHA-256 | Best archived-candidate score | Provenance status |
| --- | --- | ---: | --- |
| Attack gas | 979C4D512D7E17A79A3A3451613ADF5CD801402E89DA56098E7E1DBB31CF4741 | 0.0673 | Blocked: exact source unproven |
| Death 01 | 885BBE5F4CA50E1AE68942792F7B4CA1BAB4CA3970110DAD1045FF4832C513FF | 0.1995 | Blocked: exact source unproven |
| Death 02 | 892EDDA65D26FE7D9E48493CD4DF0FFC43B956D47649FA90255B6EA2B0F81CA2 | 0.2408 | Blocked: exact source unproven |
| Death 03 | 188D02CDE5ED11E3DDBD92B959A608826D90A57BA409E4136B5100C01E40959B | 0.1733 | Blocked: exact source unproven |
| Move step 01 | B47341232E4D9EA281D6BD896567A45D3DBE655D1C2BF97FAEA3ACF64C9159D2 | 0.3368 | Blocked: exact source unproven |
| Move step 02 | 9771CA8D3E5936B79D1C76020FCC757B2DCC2FDE333B2A64A26287E6E91DDBD7 | 0.2346 | Blocked: exact source unproven |
| Move step 03 | 913169A436EF7D6AB4EDB3F8E335AECA716259B1F9B8CA672D8D757FE8D65F34 | 0.2872 | Blocked: exact source unproven |
| Move step 04 | 389A2A1C2E2C300DAC1EC69AC68B46A9EC7A1A2DA94AB08FD4336B5F9C8A0742 | 0.3416 | Blocked: exact source unproven |

Git history confirms the nine runtime paths were added in a48e000bf on 2026-08-15. A path-following query appeared to connect the idle WAV to an unrelated DDS because both Git LFS pointer files have similar boilerplate; their actual pointer OIDs differ (222debcb… for the WAV and 6a378db4… for the DDS), and their recorded object sizes differ (1,103,276 bytes versus 35,328 bytes). That apparent path history is not audio provenance. No source attribution for the other eight was recovered from the examined job evidence or Git history.

## Vanilla selection and infantry voice findings

The previous model note describes selection as only the global select_army family. The installed data shows two distinct surfaces that the note should distinguish. sound/soundeffects.asset defines the generic select_army, select_vehicle, and select_tank effects at lines 1001, 1014, and 1024; these are also listed in sound/category.asset at lines 112–114. A separate installed Voices category in integrated_dlc/dlc018_together_for_victory/sound/vo.asset registers country-prefixed infantry groups such as GER_infantry_idle, GER_infantry_move_out, GER_infantry_neutral_combat, GER_infantry_positive_combat, and GER_infantry_retreat (lines 1–10 and definitions at 175, 208, 240, 272, and 304); SOV_infantry_idle is defined at line 1061. The generic global groups and the tag-prefixed infantry voice family should not be collapsed into one claim.

chaos_battalion is declared with type = { infantry } and group = infantry in common/units/cbrn_regimental_support.txt lines 703–714. The installed voice identifiers are country/original-tag keyed, not subunit keyed. A tag-level infantry idle voice can serve a tag’s infantry, but when ordinary infantry and chaos_battalion coexist under the same tag it cannot provide a distinct CBRN-only selection line. The current model entity’s audio events are attached to idle, move, attack/support attack, and death animation states in gfx/entities/chaos_assault_battalion.asset; those events do not act as selection or order-acknowledgement bindings. The recovered chaos_assault_battalion_selection_breath.wav is only a reviewed candidate and is not registered by the active sound definition.

Parent-owned reconciliation should update the model-system note and manifest: preserve the proven idle attribution, mark the other eight runtime cues blocked pending exact provenance, qualify the blanket CC0 header claim in sound/chaos_assault_battalion_sound.asset, and replace the selection paragraph with the two-route vanilla description above. No runtime replacement is recommended from the 2026-09-12 candidate set on this evidence.

## Evidence and remaining work

Primary local evidence reviewed: docs/systems/3d_model_pipeline/chaosx_chaos_assault_battalion_model.md; sound/chaos_assault_battalion_sound.asset; gfx/entities/chaos_assault_battalion.asset; docs/assets/chaos_warfare_system/models_3d/chaos_assault_battalion/manifest.json; docs/assets/chaos_warfare_system/models_3d/chaos_assault_battalion/audio/recovery_20260912/approved_downloads.json; source_file_receipts.json; runtime_attribution.txt; runtime_attribution_receipt.json; the archived source pages and source bytes; derived_manifest.json; sound_handoff.md; the 2026-09-12 model finalization handoff; and the parent-provided .git/cbrn_takeover_20261006/idle_audio_match.json and audio_source_matching.json measurements.

The adjacent JSON crosswalk contains the exact cue paths, hashes, match scores, source status, voice-consumer evidence, and audit limits. This handoff establishes an idle source match and records blockers; it does not establish that the complete custom-unit audio package is legally or operationally complete. Parent-owned wiring, documentation reconciliation, and live consumer validation remain outstanding.
