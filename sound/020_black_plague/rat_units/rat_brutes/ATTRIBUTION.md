# Rat-family recorded audio attribution

The current rat-brute package uses eleven retained WAV derivatives from three verified recordings.
No audio was generated, synthesized, recorded or hand-made by this repair job.
Original OGG bytes and the source receipt are under `docs/assets/020_black_plague/models_3d/rat_ground_unit_shared/audio/models_1018_sources/`.
Original and derivative hashes, format and waveform measurements are recorded in `evidence/models_1018_parent/manual_audio_verification.json` under that model package.
Historical derivative recipes are retained in `docs/plans/unit_fix_2026-10/wp5_wp6_audio_handoff.md` and its linked evidence.

| Recording creator / source | Licence | Source page | Original SHA-256 |
|---|---|---|---|
| British Library Board; recordist Richard Ranft, bamboo-rat calls | CC BY 4.0 | [Bamboo Rat](https://commons.wikimedia.org/wiki/File:Bamboo_Rat_(Dactylomys_dactylinus)_(W_DACTYLOMYS_DACTYLINUS_R1_C1).ogg) | `F3FE77A46115BECBC5761315D4A993DFBF5303D6285A8CACF998948A9C00D946` |
| admin_phpbb (recording metadata: Stephan), eating recording | Public domain | [Cat eating noisily](https://commons.wikimedia.org/wiki/File:Cat_eating_noisily.ogg) | `B96EE393ADAB3A45832B0BE54C3CB0726F7317EC52F203ED18AE2B1B30D4B955` |
| gregoryweir, recorded dull thud / creature-footstep foley | Public domain dedication | [Dull thud](https://commons.wikimedia.org/wiki/File:Dull_thud.ogg) | `5B91906D41BD57F1F6551E446D30FBFF06EC59A39D22725140293EF4AEC6CDB3` |

Bamboo-rat vocal adaptations are distributed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/); no endorsement is implied.
Adaptations include excerpt selection, transient trimming, short fades, DC/subsonic cleanup, pitch-preserving time stretching, peak adjustment, mono conversion and PCM16 44.1 kHz delivery.
The bite cues use the recorded eating source; impact and timed footfalls use the recorded public-domain thud.
The stable `rat_brutes_move_scurry` wrapper plays that thud once at each measured left/right foot plant rather than playing an unrelated gravel bed.

The former `Walking-on-gravel-38827` source is rejected: Commons lacks an original-author attribution, and the located Pixabay page identifies deffyme (Freesound) under a different licence without establishing a CC0, public-domain or CC BY grant.
The two rat-brute gravel WAVs and their owned current-package source/derivative copies were removed; preimage hashes are in `evidence/models_1018/final/runtime_install_receipt.json`.
This disposition does not rewrite historical receipts or authorize this rat job to modify legacy cues shared by other xenobiological models.
The provenance review is `evidence/models_1018/gravel_provenance_review.json`.

The session could inspect provenance, bytes and waveform measurements but could not audition audio; it makes no auditory or in-game acceptance claim.

| Runtime file | Verified input SHA-256 | Installed SHA-256 |
|---|---|---|
| `rat_brutes_attack_vocal_01.wav` | `92858AE35F4FECBF583728D5A995A1F57B50B917068628F49E2131B8B5A24E20` | `30D55375C0781243083DE7FC2583241297173FB31CD4FBF518246D1584A91332` |
| `rat_brutes_attack_vocal_02.wav` | `2FBCFAB45B458805F727CBABA4AFA525DADE7B011144106D7D1CAA5BB498AF07` | `95F7501DD5B25DDC2F7E6B7F8825139E26F6C60DB2FDC9754D93DBA2A1B9915C` |
| `rat_brutes_bite_01.wav` | `24FFCA89AFC65AD59335BB846F044AC0CB0324D95C3E48017F3395351C26AE10` | `A8FD4D20882D8505E488AA9AE8E120F5CB62BBCA2A1D6AAA1A99059791314BD2` |
| `rat_brutes_bite_02.wav` | `24FFCA89AFC65AD59335BB846F044AC0CB0324D95C3E48017F3395351C26AE10` | `7F4CFA7B5AD6C141AEA5F241E059BAA2D0101C3339A4FEC0B895840D5434FDD2` |
| `rat_brutes_idle_ambient.wav` | `5BD7166EC9E49AD27A078D8D3D7AE295BC0CAD238B9745136CD49BE84CB998BF` | `77ACA898BE13EF70F8EF97268970254D3F35B83CEF6FCDF983F234D5DFCFB8C2` |
| `rat_brutes_retreat_vocal_01.wav` | `2FBCFAB45B458805F727CBABA4AFA525DADE7B011144106D7D1CAA5BB498AF07` | `2519CF8E68EEAAC3092CF2EE8804D825E1C467DE02566BD486A6AAE94FC95138` |
| `rat_brutes_death_vocal_01.wav` | `61021F4138C68B656FC72B3CD6A44F8B8364209722C378825573A6B94DBCBEFC` | `9ECD10A2F03C1531A8D0098C626C0E67BCCB98BC0875228ED9D0368BAE03FF9B` |
| `rat_brutes_training_alert_01.wav` | `5B1FB78A344CB5B27FA1D6171CD23D7C91F48DD38ECDA097AF24B4BE1CA8C697` | `44E4554EBB39241861AC56FD88AD4084A547C4363B5C1C27C86A5B1CC3116782` |
| `rat_brutes_selection_voice_01.wav` | `9B8A61466E88991FE7EC5FF98BD85205756BDCE0129DFDF9F0FFC95730B14D89` | `2996ACAB15818AE12D134CEA6A7FD2B72F1E409C3BF2C69EC4304C3DFAF43083` |
| `rat_brutes_acknowledgement_voice_01.wav` | `13EC06C6A5E874687A900E09351944F56E55DF58319A04B84E09096D01A37405` | `5292AF4E974AFE8E608C42A6510B76CCC354E3063107BB3CED2C5277A0507D0E` |
| `rat_brutes_impact_01.wav` | `A84C6A2C745930A555D140C5616C28894A7FFEDA3AC8AFA88052CBA814347CFC` | `C178F5C0E631409DAB5C07C17410FFE2BA92A67FDAD2271BAE1A73C45547674A` |
