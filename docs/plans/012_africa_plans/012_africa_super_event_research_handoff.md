# Event 012 Africa super-event research handoff

Date of research: 2026-07-16

## Disposition

This note supplies one researched package for each of the four roles required by the Event 012 source package. It does not create a fifth role or a host-by-host variant grid. The final title recommendations are deliberately different from the working role labels, as required by the Event 012 prompt.

No media was downloaded. No image was generated. No audio derivative, DDS, GFX entry, GUI entry, sound definition, gameplay script, localisation, workbook, or catalog row was created or edited. The four packages below are therefore **research-complete candidates, not wire-ready super-events**.

The governing Event 012 sources are:

- [`africa_super_event_prompt.md`](../../specs/012_africa_specs/prompts/africa_super_event_prompt.md), especially the four-role rule and the text, audio, image, and research gates.
- [`012_africa_spec_part_6_presentation_achievements_assets.md`](../../specs/012_africa_specs/specs/012_africa_spec_part_6_presentation_achievements_assets.md), especially the four super-event roles at lines 253-354.
- [`012_africa_asset_animation_matrix.csv`](../../specs/012_africa_specs/matrices/012_africa_asset_animation_matrix.csv), whose four rows require one generated `457x328` image for each role and already fix the final DDS filenames and sprite names.

## Decision summary

| Working role | Final title recommendation | Quote source | Track candidate | Display slot | Audio ID | Research status |
| --- | --- | --- | --- | ---: | ---: | --- |
| Africa is one | **THE CONTINENT TAKES ITS SEAT** | Marcus Garvey, 1922 | `Nkosi Sikelel' iAfrika`, White House performance, 1994 | `101` | `58` | Needs user review because one liberation anthem must also accompany coercive and high-chaos constitutional outcomes |
| Scramble response | **THE MAPMAKERS RETURN** | General Act of Berlin, Article 34, 1885 | Beethoven, *Eroica*, II. *Marcia funebre*, Musopen/Czech National Symphony | `102` | `59` | Ready for asset/audio production; final cue still requires audition and source freezing |
| Continental wars | **CONTINENTS UNDER ARMS** | Clausewitz, *On War* | Brahms, Symphony No. 4, IV, Musopen | `103` | `60` | Performer-credit discrepancy must be reconciled before the attribution ledger is frozen |
| The World | **ONE WORLD REMAINS** | Shelley, `Ozymandias` | Schubert, *Unfinished* Symphony, II, Fulda Symphonic Orchestra | `104` | `61` | Needs user/legal-production review of the EFF Open Audio License metadata-retention obligation |

The four exact proposed titles and four exact track labels returned no matches in the repository-wide title/path search performed on 2026-07-16. That is a catalogue check, not acoustic uniqueness proof. Final audio production must compare source and derivative Chromaprint fingerprints and hashes against every live super-event recording.

## Numeric collision audit

### Live presentation slots

The authoritative live getter is `common/scripted_localisation/chaosx_scripted_localisation_super_events.txt`. Its unique `super_event_visible` values are:

`1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 49, 50, 51, 52, 53, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 82, 83, 84, 96, 97, 98, 99, 100`.

Additional reserved presentation ranges were also inspected:

- Event 020 reserves `85`, `86`, and `87` in `common/script_constants/020_black_plague_constants.txt:21-23`.
- Event 016 reserves `90` through `95` in `common/script_constants/016_brilliant_scientist_constants.txt:928-933`; six matching WAV filenames already exist under `sound/016_brilliant_scientist/`.
- `docs/plans/018_resources_found_plans/018_live_registry_reservations.md:3-11` retains a historical reservation note for `78` through `81`. Those gaps were not reclaimed here.

A namespace-specific search found no getter, localisation key, sprite, constant, event call, or plan allocation using presentation slots `101`, `102`, `103`, or `104`. They are the safest contiguous maximum-plus-one block at the time of this audit.

### Live audio IDs

The unique IDs registered in both `sound/chaosx_sound.asset` and `sound/chaosx_sound.asset` are:

`1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 17, 18, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 52, 53, 54, 55, 56, 57, 6002`.

Event 016's six source OGG filenames additionally reserve the `90` through `95` audio namespace even though their wrapper registration is not yet present in the shared live asset files. A namespace-specific search found no sound wrapper, sound wrapper, raw sound, or `current_super_event_audio_id` assignment for `58`, `59`, `60`, or `61`.

Display and audio identifiers are separate namespaces. Consequently, audio IDs `59`, `60`, and `61` are free even though presentation slots `59`, `60`, and `61` are occupied.

### Proposed allocation

| Role | Presentation slot | Audio ID | Proposed final WAV | Stable raw sound name |
| --- | ---: | ---: | --- | --- |
| Africa is one | `101` | `58` | `sound/012_africa/super_event_58_africa_is_one.wav` | `chaosx_super_event_africa_is_one_track` |
| Scramble response | `102` | `59` | `sound/012_africa/super_event_59_scramble_response.wav` | `chaosx_super_event_scramble_response_track` |
| Continental wars | `103` | `60` | `sound/012_africa/super_event_60_continental_wars.wav` | `chaosx_super_event_continental_wars_track` |
| The World | `104` | `61` | `sound/012_africa/super_event_61_the_world.wav` | `chaosx_super_event_the_world_track` |

Future registration should create all six established settings-scaled sound wrappers `chaosx_super_event_<ID>_sound_0_5` through `chaosx_super_event_<ID>_sound_3_0`. This document does **not** reserve those identifiers in engine-readable code. The implementation agent must repeat the shared-registry scan immediately before registering all four roles atomically.

## Rights and wording policy

The recommended button remarks below are original Chaos Redux wording, not attributed quotations. They should be treated as authored localisation and must never be displayed with a speaker attribution.

The 1963 OAU summit speeches are historically excellent alternatives but are not cleared here. The [African Union archive record](https://archives.au.int/handle/123456789/10452) names the African Union as rights holder, and the [AU legal notice](https://au.int/en/legal_notice) states that website material cannot be reproduced without written permission except under stated conditions. The following short candidates remain **permission-blocked alternatives only**:

- Kwame Nkrumah, page 48: "Unite we must."
- Ahmadou Ahidjo, page 23: "Africa at last takes her place at the family table."
- Sékou Touré, page 54: "African unity has its convinced adherents and its determined adversaries."

The wording is verified in the [African Union's 1963 summit PDF](https://archives.au.int/bitstream/handle/123456789/10452/OAU_Sum_Spe_1963_E.pdf?isAllowed=y&sequence=3), but none should ship unless the project records permission or a legal review reaches a different documented conclusion.

## Role 1: Africa is one

### Final text direction

- **Recommended title:** `THE CONTINENT TAKES ITS SEAT`.
- **Why it fits:** it announces political standing and an institution entering world affairs, rather than merely repeating the working label's word `unity`. It can describe a republic, federation, council of crowns, people's congress, command order, confederation, or revealed Covenant.
- **Selected quote:** "building up... a great nation in Africa."
- **Attribution:** Marcus Garvey, `Africa for the Africans`, *Negro World*, 22 April 1922.
- **Evidence:** the [PBS American Experience primary-source transcription](https://www.pbs.org/wgbh/americanexperience/features/garvey-his-own-words/) supplies the wording and identifies the original article and date. Attribution confidence is high for the excerpt as transcribed; the lower-case opening and ellipses should be preserved because this is a fragment of the source sentence.
- **Rights assessment:** the underlying article was published in 1922, making it a strong U.S. public-domain candidate by publication date. The linked PBS page is evidence and a transcription trail, not the source of a new licence. The release ledger should still record the project's target jurisdictions and the exact original edition used for final transcription.
- **Selected button remark:** `The continent will answer for itself.` Original Chaos Redux wording; no external copyright or attribution dependency.
- **Backup original remark:** `The empty chair is filled.`
- **Permission-blocked historical backups:** Nkrumah's and Ahidjo's short OAU lines listed in the rights section above.
- **Cultural review:** Garvey's wider programme is politically specific, and the PBS page itself describes his separatist and inflammatory reputation. The selected fragment avoids the source's racial-imperial wording, but the project should approve the association before using it for every constitutional route.

### Dynamic description fields

The final description needs semantic fields for:

- final continent actor name and adjective;
- completed constitutional settlement and its public institution;
- seat/capital only when the original host or diplomatic legacy remains central;
- settlement method for the final required regions;
- unresolved integration burden, confederal autonomy, or coercive residue;
- high-chaos identity only when it is already public.

Description direction, not final localisation: identify the final actor, name the institution that has opened, state how all required regions crossed the accepted political threshold, and retain one visible unresolved cost. Do not imply that a confederation is a unitary state or that military control alone equals settled integration.

### Image handoff

- **Source mode:** one generated symbolic alternate-history scene, matching matrix row `africa_is_one_super`.
- **Final DDS:** `gfx/super_events/012_africa/super_event_012_africa_is_one.dds`.
- **Sprite:** `GFX_super_event_012_africa_is_one`.
- **Brief:** an Africa Hall-inspired continental assembly seen from a human eye line. Delegates and observers from several regions converge on a newly opened central dais; rail, port, telegraph, and road lines appear as physical relief-work behind them rather than a flat political map. No single leader dominates. Banners use invented, non-readable devices so the interface can carry the real actor and route identity dynamically. The image must show confidence and institutional weight while retaining one sign of unfinished burden, such as empty benches, petitions, or guarded doors.
- **Avoid:** an AU emblem, copied national flags, readable text, a lone heroic strongman, a generic crowd montage, a flat map, ethnic costume collage, or triumph without political residue.
- **Historical reference only:** the [1963 OAU summit photograph of Haile Selassie and Gamal Abdel Nasser](https://commons.wikimedia.org/wiki/File:Selassie_and_Nasser,_1963.jpg) is useful for diplomatic dress, room scale, and period posture. Commons identifies it as a 1963 Addis Ababa OAU image, `455x430`, uncredited, and public domain under its Egyptian-work analysis. The generated image must not reproduce either leader's likeness or the photograph's exact arrangement.
- **Variant decision:** one final image, as the accepted matrix requires. If a high-chaos route later proves impossible to represent without falsifying the base composition, the parent must amend the matrix and approve a specifically triggered second state before production; no second variant is preapproved here.

### Audio handoff

- **Candidate:** Enoch Sontonga, `Nkosi Sikelel' iAfrika`, performed by a United States military band and recorded by White House Television in October 1994.
- **Frozen evidence page:** [Wikimedia Commons revision 999959845](https://commons.wikimedia.org/w/index.php?title=File:%22Nkosi_Sikelel%27_iAfrika%22_performed_at_the_White_House_in_1994.oga&oldid=999959845).
- **Source evidence:** duration `104.06848072562359 s`; published SHA-1 `0759a8aac2fea38a839cc3b88784712fc1ff8a53`. The page dates the composition to 1897, names Sontonga, identifies the military-band performance and White House recording, and separately labels the composition, performance, and recording public domain on the stated old-work and U.S.-federal-work bases.
- **Licence confidence:** medium-high as source-page evidence. The page separately supplies the public-domain rationale for composition, performance, and recording, but its acquisition trail points through a YouTube copy of the White House programme rather than a direct federal archive download. It is also a U.S.-federal public-domain basis for the 1994 performance/recording rather than a CC0 dedication. Production should locate the matching White House/Clinton-era federal master or archive record if possible, then preserve the exact source revision and downloaded-file hash.
- **Courtesy attribution:** `Enoch Sontonga, "Nkosi Sikelel' iAfrika"; United States military band; recorded by White House Television, October 1994; source via Wikimedia Commons. Chaos Redux excerpted/processed the source; no endorsement is implied.`
- **Proposed preserved source:** `docs/assets/012_africa/source_audio/africa_is_one_nkosi_white_house_1994_source.oga`.
- **Editing plan:** first audition the whole `1:44` file for spoken introduction, applause, silence, clipping, vocal content, and a complete ending. Prefer the complete performance if it is clean and ends musically; otherwise retain one `75-104 s` continuous arc with only necessary head/tail trims, a short fade-in, and a phrase-respecting fade-out. Produce a stereo `44,100 Hz` OGG and signed 16-bit PCM WAV at the project's super-event loudness target.
- **Why it fits:** the work is historically associated with African liberation and continental aspiration, and its full source already fits the two-minute ceiling.
- **Unresolved blockers:** one liberation anthem may sanctify coercive, command, or high-chaos completions and has strong South African associations. User review must decide whether that tension is acceptable for the single shared role. Production must also close the Commons-to-YouTube provenance gap with an official federal archive match or a documented decision that the frozen Commons evidence is sufficient. No alternate route track is authorized by the four-role matrix.

## Role 2: Scramble response

### Final text direction

- **Recommended title:** `THE MAPMAKERS RETURN`.
- **Why it fits:** it recalls colonial partition without presenting the old Scramble as adventure, and makes the outside response feel like an attempted return to a discredited political practice.
- **Selected quote:** "to enable them, if need be, to make good any claims of their own."
- **Attribution:** *General Act of the Conference at Berlin*, Article 34, 26 February 1885.
- **Evidence:** the linked [English transcription of the General Act](https://www.internationalwaterlaw.org/documents/regionaldocs/1885GeneralActBerlinConference.pdf) gives this exact Article 34 wording on PDF page 13. The [German Federal Foreign Office archival overview](https://archiv.diplo.de/arc-en/the-political-archive/general-act-2684414) independently explains that Articles 34 and 35 established the effective-occupation framework and that no African representative was consulted.
- **Rights assessment:** the underlying 1885 treaty text is a strong public-domain candidate by age and official-document character. Attribution confidence is high for the Article and substance, but the final ledger should compare this English wording with a contemporaneous official English printing before shipping because the linked transcription does not identify its translator.
- **Selected button remark:** `This time, Africa answers.` Original Chaos Redux wording; no external attribution dependency.
- **Backup original remark:** `The old capitals have found their voice.`
- **Permission-blocked historical backup:** Touré's OAU line listed in the rights section above.

### Dynamic description fields

The final description needs semantic fields for:

- unified African actor and completed constitutional form;
- named response leader or coalition when one exists;
- visible response class: recognition crisis, sanctions, ultimatum, expedition planning, or open war;
- stated demand, concession, or containment objective;
- Africa's public answer or mobilization posture;
- threshold that made the crisis globally visible.

Description direction: name the outside actor and concrete response without exposing AI calculations, then state the African actor's answer as a sovereign subject. Do not describe Africa as territory being divided, and do not imply armed intervention when the actual state is recognition or sanctions.

### Image handoff

- **Source mode:** one generated alternate-history scene, matching matrix row `scramble_super`.
- **Final DDS:** `gfx/super_events/012_africa/super_event_012_africa_scramble_response.dds`.
- **Sprite:** `GFX_super_event_012_africa_scramble_response`.
- **Brief:** reverse the visual grammar of the Berlin Conference. A central African diplomatic and logistical command receives simultaneous sealed notes, port closures, naval schedules, and foreign ultimatums from the frame edges. African ministers, dockworkers, soldiers, and demonstrators occupy the compositional centre; outside fleets and chancelleries are secondary pressures. A relief map may appear as an object under African hands, never as a board being partitioned by foreigners.
- **Avoid:** copying real delegates, heroic colonial portraiture, caricatured Europeans, partition lines drawn across passive people, readable ultimatums, or a neutral-adventure tone.
- **Historical reference only:** Adalbert von Roessler's [1884 Berlin Conference drawing](https://commons.wikimedia.org/wiki/File:Kongokonferenz.jpg) is a clear period reference for table geometry, dress, and crowded diplomacy. Commons identifies the 1884 publication, Roessler's 1922 death, a `3631x2790` scan, and public-domain status by age. Use it to reverse the power relationship, not to copy faces or reproduce the colonial scene.
- **Variant decision:** one final image. Recognition, sanctions, and expedition differences belong in dynamic text and actor fields unless production proves a materially different composition is essential and the matrix is amended first.

### Audio handoff

- **Candidate:** Ludwig van Beethoven, Symphony No. 3 in E-flat major, Op. 55 `Eroica`, II. `Marcia funebre. Adagio assai`; Czech National Symphony Orchestra, listed as Musopen Symphony; 2012.
- **Frozen evidence page:** [Wikimedia Commons revision 1030946911](https://commons.wikimedia.org/w/index.php?title=File:Beethoven_-_Symphony_No._3_in_E_flat_major,_Op._55_%27Eroica%27_-_II._Marcia_funebre._Adagio_assai_(Musopen_Symphony).flac&oldid=1030946911).
- **Source evidence:** duration `928.508645833333 s`; published SHA-1 `e8bcbc56a4d293a4dc4271f3a5e4c5dffd9a78c7`. The page names the Czech National Symphony Orchestra, dates the recording to 2012, states that Musopen released the recording into the public domain worldwide with unconditional fallback permission, and separately identifies Beethoven's composition as public domain.
- **Licence confidence:** high as source-page evidence. Freeze the exact FLAC and verify its hash before processing.
- **Courtesy attribution:** `Ludwig van Beethoven, Symphony No. 3 "Eroica", II. "Marcia funebre"; Czech National Symphony Orchestra (Musopen Symphony); source via Wikimedia Commons/Musopen. Recording released to the public domain. Chaos Redux excerpted and processed the source.`
- **Proposed preserved source:** `docs/assets/012_africa/source_audio/scramble_response_beethoven_eroica_ii_musopen_source.flac`.
- **Editing plan:** audition the full movement and select a continuous `80-115 s` passage that begins with legible funeral-march gravity and reaches a clear rise in pressure. Avoid a cue that remains only mournful or ends mid-phrase. Apply phrase-safe fades, the project loudness target, and `44,100 Hz` stereo WAV delivery.
- **Why it fits:** the funeral march treats the old order's reaction as grave and destabilizing rather than adventurous, while its internal escalation can carry a shift from diplomatic panic to containment or war.
- **Unresolved blocker:** the cue point is not selected. No derivative may be made until a human audition confirms that the retained arc supports both non-war and war reaction states.

## Role 3: Continental wars

### Final text direction

- **Recommended title:** `CONTINENTS UNDER ARMS`.
- **Why it fits:** it names the unprecedented political scale without using vague apocalypse language or declaring the terminal victor before the war begins.
- **Selected quote:** "War is a mere continuation of policy by other means."
- **Attribution:** Carl von Clausewitz, *On War*, Book I, Chapter I; J. J. Graham translation.
- **Evidence and rights:** [Project Gutenberg's 1909 reprint of the 1874 translation](https://www.gutenberg.org/files/1946/1946-h/1946-h.htm) contains the exact heading and identifies the translator and publication history. Project Gutenberg states that the ebook may be reused under its terms and advises users outside the United States to check local law. The translation and source edition are strong public-domain candidates by age.
- **Backup quote:** "the political view is the object, War is the means" from the same passage and edition.
- **Selected button remark:** `The arguments have reached the front.` Original Chaos Redux wording; no external attribution dependency.
- **Backup original remark:** `No border can contain this front.`

### Dynamic description fields

The final description needs semantic fields for:

- both continent-scale actors and their public names/adjectives;
- the continents or union identities actually involved;
- initiator and defender only where the gameplay state establishes them;
- each side's alliance method and constitutional war aim;
- deliberate terminal-path decision that opened the war;
- immediate human stakes: mobilization, ports, supply corridors, or threatened member polities.

Description direction: identify both rival systems and the concrete political dispute that crossed into war. The text must not announce The World, assume total conquest, or flatten distinct peaceful unions, federations, command orders, and high-chaos actors into generic blocs.

### Image handoff

- **Source mode:** one generated high-scale alternate-history scene, matching matrix row `continental_wars_super`.
- **Final DDS:** `gfx/super_events/012_africa/super_event_012_africa_continental_wars.dds`.
- **Sprite:** `GFX_super_event_012_africa_continental_wars`.
- **Brief:** two continent-scale military and political systems meet across a real logistics corridor: railheads, troop columns, convoy silhouettes, field radios, and civilian evacuation routes converge on a central rupture. The opposing masses must feel equivalent in scale while retaining human figures in the foreground. Use fictional, non-readable standards and period-appropriate 1930s-1940s material. The interface supplies the actual actor names, flags, and war aims.
- **Avoid:** a burning globe, modern missiles, holograms, science-fiction armour, one ethnically coded side, colonial-force insignia, gore, or a generic battle painting with no logistics or institutions.
- **Historical reference only:** [Ethiopian Patriots crossing the Omo River](https://commons.wikimedia.org/wiki/File:Ethiopian_Patriots_in_1941_crossing_the_Omo.jpg) is useful for African troop movement, terrain, load, and human scale. Commons identifies the image as Ethiopian Patriots in the 1941 East African Campaign, sourced from a 1956 HMSO history, and marks the UK-government work public domain with worldwide Crown-copyright expiry evidence. Do not copy identifiable people, turn Ethiopian resistance into a generic continent identity, or retain colonial insignia.
- **Variant decision:** one final image. Actual opponents and war aims must remain dynamic. A second route image would require a matrix amendment and a named trigger role.

### Audio handoff

- **Candidate:** Johannes Brahms, Symphony No. 4 in E minor, Op. 98, IV. `Allegro energico e passionato`; Musopen recording.
- **Frozen evidence page:** [Wikimedia Commons revision 956374187](https://commons.wikimedia.org/w/index.php?title=File:Brahms,_Symphony_No._4_in_E_Minor,_Op._98_-_IV._Allegro_Energico_e_Passionato.ogg&oldid=956374187).
- **Source evidence:** duration `667.728 s`; published SHA-1 `6090286916a8981cad1f5edcf129f4442001d11c`. The file page applies CC0 1.0 to the recording and states that the waiver covers copyright and neighbouring rights worldwide to the extent allowed by law. Brahms's nineteenth-century composition is public domain by age.
- **Attribution discrepancy:** the page's author field says `Musopen Symphony Orchestra`, while embedded metadata says `Czech National Symphony Orchestra`. The same discrepancy is visible on the frozen page and must not be silently resolved by assumption.
- **Licence confidence:** high for the file-specific CC0 grant; medium for performer attribution until the source package or Musopen record is checked.
- **Provisional courtesy attribution:** `Johannes Brahms, Symphony No. 4 in E minor, IV. "Allegro energico e passionato"; Musopen recording; source via Wikimedia Commons; recording dedicated under CC0 1.0. Performer credit pending source reconciliation.`
- **Proposed preserved source:** `docs/assets/012_africa/source_audio/continental_wars_brahms_symphony_4_iv_musopen_source.ogg`.
- **Editing plan:** after resolving performer credit, audition for a continuous `75-115 s` arc with an immediate pulse, sustained middle escalation, and a complete cadence or controlled phrase-safe fade. Deliver `44,100 Hz` stereo WAV at project loudness; do not manufacture intensity with tempo or pitch changes.
- **Why it fits:** the passacaglia-like drive and severe orchestral escalation communicate campaign-defining war without modern or cinematic associations.
- **Unresolved blocker:** exact performer attribution must be reconciled before the rights ledger, embedded metadata, catalogue row, or final derivative is approved.

## Role 4: The World

### Final text direction

- **Recommended title:** `ONE WORLD REMAINS`.
- **Why it fits:** it supports union, federation, submission, victory, or a public high-chaos resolution while emphasizing irreversible finality rather than a planet explosion or ordinary conquest celebration.
- **Selected quote:** "Nothing beside remains."
- **Attribution:** Percy Bysshe Shelley, `Ozymandias`, first published in 1818; wording taken from the 1914 Hutchinson edition.
- **Evidence and rights:** the [Wikisource transcription of the 1914 edition](https://en.wikisource.org/wiki/The_Complete_Poetical_Works_of_Percy_Bysshe_Shelley_%28ed._Hutchinson%2C_1914%29/Ozymandias) provides the exact line, identifies the 1818 first publication, and links the source edition. The poem and 1914 edition are strong public-domain candidates by age.
- **Backup quote:** "The lone and level sands stretch far away."
- **Selected button remark:** `The last border is an archive.` Original Chaos Redux wording; no external attribution dependency.
- **Backup original remark:** `There is no second signature.`
- **Tone guard:** Shelley's line supplies cost and exhaustion, but the description must not imply that the population is extinct. What has ended is the plurality of eligible continent-scale sovereign identities.

### Dynamic description fields

The final description needs semantic fields for:

- final actor name, adjective, and surviving public institution;
- surviving constitutional route or public high-chaos identity;
- resolution method for the last rival: union, federation, submission, negotiated settlement, or victory;
- identities incorporated, federated, subordinated, or defeated;
- final capital/seat only if it remains meaningful;
- shutdown of incompatible world-end competition and the cost carried into the terminal order.

Description direction: name the surviving institution, state how the final rival identity was resolved, and describe what the resulting order inherits. Do not write a universal military victory when the actual path was consensual union, and do not erase the continental wars' political and human cost.

### Image handoff

- **Source mode:** one generated terminal symbolic scene, matching matrix row `the_world_super`.
- **Final DDS:** `gfx/super_events/012_africa/super_event_012_africa_the_world.dds`.
- **Sprite:** `GFX_super_event_012_africa_the_world`.
- **Brief:** a silent terminal chamber after the final settlement. One route-neutral institution remains active at a central table; the surrounding seats are empty but intact, and bound treaties, surrendered standards, federation instruments, and archived borders show several possible methods of resolution. A world horizon or reflected Earth curve may appear only as a secondary light source. Human clerks, guards, delegates, or survivors prevent the image from becoming an empty emblem.
- **Avoid:** a triumphant lone dictator, a globe as the sole subject, planet explosion, futuristic command centre, readable text, piles of bodies, or route-specific symbolism that misstates peaceful union.
- **Reference only:** NASA's [Apollo 17 Blue Marble page](https://eol.jsc.nasa.gov/Collections/EarthObservatory/articles/The_Blue_Marble_from_Apollo_17.htm) records that the 7 December 1972 photograph shows almost the entire coastline of Africa. NASA's current [Images and Media Usage Guidelines](https://www.nasa.gov/nasa-brand-center/images-and-media/) say NASA content is generally not subject to U.S. copyright but impose source-credit, no-endorsement, logo, third-party, and identifiable-person conditions. Use the image only for world-horizon and Africa-orientation reference unless the final asset ledger separately clears direct pixel use; never include NASA branding.
- **Variant decision:** one final image. A high-chaos alternative is not preapproved; it requires a matrix amendment and a named public trigger before production.

### Audio handoff

- **Candidate:** Franz Schubert, Symphony No. 8 in B minor `Unfinished`, II. `Andante con moto`; Fulda Symphonic Orchestra; conductor Simon Schindler; source metadata also credits Johannes Volker Schmidt; recorded 9 April 2000.
- **Frozen evidence page:** [Wikimedia Commons revision 1189797410](https://commons.wikimedia.org/w/index.php?title=File:Schubert%27s_8th_Symphony,_2nd_movement_Andante_con_moto_in_E_major.ogg&oldid=1189797410).
- **Source evidence:** duration `645.08 s`; published SHA-1 `ad07c6d7eaad79d06bc68c7e9e058bc04bfa0ef8`. The page identifies the orchestra and conductor, dates the recording, and applies the EFF Open Audio License version 1.
- **Licence terms:** the source page states that copying, redistribution, performance, and modification are allowed, but original author attribution, Vorbis audio tags, and licence terms may not be removed or modified. The composition is public domain by Schubert's 1828 death; the recording remains governed by the EFF licence rather than CC0.
- **Licence confidence:** high for the grant stated on the frozen page; production/legal review is still required because the mod must distribute an edited derivative while preserving the required attribution, tags, and terms.
- **Required attribution direction:** retain the original source tags intact, add separate derivative/edit tags without overwriting them, identify the Fulda Symphonic Orchestra and Simon Schindler, preserve Johannes Volker Schmidt exactly as present in the source metadata, name the EFF Open Audio License v1, link its terms, state the retained interval and processing, and avoid any endorsement implication.
- **Proposed preserved source:** `docs/assets/012_africa/source_audio/the_world_schubert_unfinished_ii_fulda_source.ogg`.
- **Editing plan:** select a continuous `85-115 s` passage whose restrained opening develops toward a complete, exhausted cadence. Modification is allowed, but processing must copy every original Vorbis attribution/licence field into the final WAV and retain a sidecar rights record for the WAV, which cannot carry the same Vorbis comments. Apply phrase-safe fades and `44,100 Hz` stereo delivery at project loudness.
- **Why it fits:** the `Unfinished` work's measured, unresolved character supports terminal political exhaustion without turning the moment into a coronation or conventional victory march.
- **Unresolved blocker:** the project must explicitly accept the EFF Open Audio License obligations and prove that its final WAV and distribution documentation preserve them. If not, replace this recording with a file-specific CC0/public-domain recording before production.

## Production and final-wiring gates

None of the four roles may be wired until all of the following are complete:

1. User or parent approval of the four final titles, four quotations, four original remarks, and the two flagged cultural/licence judgements.
2. A repeated live collision scan followed by atomic registration of presentation slots `101-104` and audio IDs `58-61`.
3. Download of each exact frozen source revision into `docs/assets/012_africa/source_audio/`, verification of the published SHA-1, calculation of SHA-256, and preservation of the source file without transcoding.
4. Human audition and exact cue-time selection for every track.
5. Chromaprint and binary-hash comparison against all existing super-event sources and derivatives; title/path uniqueness alone is insufficient.
6. Production of unique stereo `44,100 Hz` OGG and signed 16-bit PCM WAV files no longer than two minutes, with task-specific loudness, peak, duration, and decode checks.
7. Complete composition and recording rights ledger, frozen URL/revision, attribution, licence terms, edit notice, and jurisdiction note for every cue.
8. Generated-art production through the Event 012 asset worker: source PNG, processed PNG, final `457x328` DDS, contact sheet, prompt record, manifest, and sprite handoff for the exact four matrix rows.
9. Visual review at UI size for central subject, contrast, crop safety, route neutrality, historical dignity, absence of readable text, and absence of copied real-person likenesses.
10. Parent-owned wiring of the four sprites, all title/quote/description/remark getters, dynamic actor/route fields, settings-aware audio playback, zero-random-play music entries, sound wrappers, event triggers, documentation, event catalog, and workbook alignment.

## Simplifications, omissions, and blockers

- No final media exists; all four roles remain unwired.
- No image variant beyond the one image per accepted matrix row is approved. Any high-chaos image variant needs a matrix amendment and explicit trigger role.
- `Nkosi Sikelel' iAfrika` has clear source-page rights evidence but requires both a cultural judgement for coercive/high-chaos routes and closure of the Commons-to-YouTube provenance gap.
- The Brahms recording has a performer-credit discrepancy between the file page and embedded metadata.
- The Schubert recording is clearly licensed rather than public domain/CC0 and carries mandatory metadata and licence-retention obligations.
- The Garvey excerpt is a strong public-domain candidate, but its political context requires user review and the final ledger should identify the exact original edition rather than relying only on the modern PBS transcription.
- The Berlin Act quote's substance and Article are verified, but the final ledger should confirm the exact English wording against a contemporaneous official English print.
- Slot and audio-ID findings are valid for the 2026-07-16 working tree only; this markdown note does not make an engine-readable reservation.
