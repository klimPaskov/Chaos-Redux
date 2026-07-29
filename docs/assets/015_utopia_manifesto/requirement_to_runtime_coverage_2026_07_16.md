# Event 015 Accepted Asset Requirement-to-Runtime Coverage

Date: `2026-07-16`

Scope: all `24` accepted rows in `docs/specs/015_utopia_manifesto_specs/matrices/asset_manifest_plan.md`.

Verdict: **PASS - 24/24 rows pass; no fallback, simplification, omission, or open asset blocker.**

Each row was checked from source/provenance through processed or packaged output, runtime file, registration, live consumer, and state binding where the row requires one. Extra assets were not accepted as substitutes.

| # | Accepted row | Source and package proof | Runtime registration, consumer, and state | Result |
| ---: | --- | --- | --- | --- |
| 1 | Opening report | `final_non_icon_2026_07_14/asset_records.json`: `report_event_utopia_manifesto_found` | `GFX_report_event_utopia_manifesto_found` in `015_utopia_manifesto.gfx`; consumed by opening events in `events/015_utopia_manifesto.txt` | PASS |
| 2 | Common-store reports | Same immutable package: `ledger`, `calling`, and `store` records | Three registered report sprites; live Event 015 picture assignments | PASS |
| 3 | Settlement reports | Same package: `settlement` and `island` records | Two registered report sprites; live settlement/island event assignments | PASS |
| 4 | Need news | Same package: `league`, `necessary_ground_war`, and `colony_revolt` | Three registered `397x153` news sprites; live news-event consumers | PASS |
| 5 | Five-route final super-event | Same package: five independent `super_event_015_*` source/processed/runtime records | Five definitions in `015_utopia_manifesto_super_event.gfx`; slots `96`-`100` select exact art/text, and the route-gated proclamation effect selects the slot | PASS |
| 6 | Focus icons | Seven generated focus atlases, `74` exact `goal_utopia_*_source.png` masters, processed PNGs, and the two documented island-variant source records | `124` live focus uses resolve to `74` unique `94x86` sprites with shine registrations | PASS |
| 7 | Idea icons | Twelve named generated sources, including ten `final_icons` masters | `50` idea entries resolve to `12` unique `64x64` registrations | PASS |
| 8 | Decision icons | `decision_icon_mapping.csv` plus `55` named generated source assets | `121` decisions and `44` missions are covered. All `165` live assignments resolve to registered `32x32` files | PASS |
| 9 | Decision category icons | Same mapping and named sources | Nine category rows resolve to nine category consumers | PASS |
| 10 | Achievement icons | Fourteen generated masters plus processed base/grey/not-eligible packages | Fourteen IDs and `42` exact current registered variants; eligibility selects the variants | PASS |
| 11 | Route flags | `route_identity_2026_07_14`: `21` independent built-in ImageGen designs plus four documented canonical aliases | `25` stems at `82x52`, `41x26`, and `10x7` produce `75` bottom-left-origin 32-bit TGAs; route cosmetic-tag effects drive filename lookup | PASS |
| 12 | League emblems | Five independent generated emblem records in the route-identity package | Five `64x64` sprites share the Ledger header position and are selected by five exact identity-emblem flags | PASS |
| 13 | Institutional leader tableaux | Four independent built-in ImageGen symbolic masters with the strict people-free review | Four `156x210` sprites serve eight founder/successor character assignments | PASS |
| 14 | Advisor dossier cards | Sixteen independent built-in ImageGen fictional portrait masters plus separately generated frame and paper/seal overlays | Sixteen `65x67` registered sprites serve sixteen advisor character entries | PASS |
| 15 | Other fictional personal portraits, if implemented | Character-file audit found no additional Event 015 personal portrait assignment | Conditional row is satisfied: only the eight institutional assignments and sixteen separately covered advisors exist | PASS |
| 16 | Ledger panel | Generated background, header, and warning-panel sources; processed PNGs and byte-identical packaged/runtime DDS files | Live `700x500` background and `700x96` header; four tab buttons and exact scripted-GUI tab flags control Overview, Callings, Stores/Settlements, and Necessary Ground | PASS |
| 17 | Value icons | `value_calling_icon_repair_2026_07_16`: frozen ImageGen atlas, four extracted/processed/package/runtime records | Need, Plenty, Concord, and Choice/Assignment are four distinct `32x32` sprites at `(30,104)`, `(194,104)`, `(358,104)`, `(522,104)`; score text remains live and the two balance animations overlay direction changes | PASS |
| 18 | Six Calling icons | Same repair package: six distinct `48x48` finals | Six registered consumers live inside `utopia_ledger_callings_panel`; Callings-tab visibility is the panel state | PASS |
| 19 | Ten Case cards | `ledger_case_cards_2026_07_16`: ten independent built-in ImageGen masters, ten `300x96` finals, validator and contact sheets | Ten registered cards share `(8,4)` in Necessary Ground; mutually exclusive bindings cover no target, eligible, selected, pending, counteroffer, refusal, ultimatum, expired, stewardship, and associate | PASS |
| 20 | Seven District roles and six states | `ledger_district_cards_2026_07_16`: thirteen independent built-in ImageGen masters and validated finals | Seven `300x96` role cards at `(334,4)` and six `48x48` overlays at `(578,12)` are deliberately in the **Stores/Settlements tab** (`utopia_ledger_stores_panel`); durable role, phase, timed planned flag, dispute, debt, and state flags bind all states | PASS |
| 21 | Ledger seal | `animations/utopia_ledger_seal`: one generated animation sheet sliced to eight distinct source frames, eight processed frames, exact sheet/static/GIF/contact package | `GFX_utopia_ledger_seal_animated`, `8` frames at `12 fps`, looping; live at `(18,16)` until one of the five route emblems replaces it | PASS |
| 22 | Need warning | `animations/utopia_need_warning`: eight distinct source and processed frames, exact sheet/static/DDS/GIF/contact package | Live `64x64` footer animation at `(24,430)`, `5 fps`, looping; high Need, low Plenty, or constitutional crisis | PASS |
| 23 | Balance shift, both directions | Eight distinct built-in ImageGen source frames per direction, exact processed sheets/static fallbacks/DDS/GIF/contact packages | Choice and Assignment animations share `(516,70)`, run at `5 fps`, do not loop, and use route-resolved band crossing, three-day direction flags, first-refresh suppression, opposite-flag clearing, and terminal cleanup | PASS |
| 24 | Formation-ready seal | `animations/utopia_formation_ready_seal`: ten distinct source and processed frames plus exact delivery package | Live `96x96` animation at `(610,0)`, scaled `0.72`, `5 fps`, looping; visible only when the current route can form and the commonwealth is not formed | PASS |

## Frozen machine evidence

- `decision_icon_mapping.csv`: SHA-256 `757ec0c51edca25b5453899f28816a3d34e8a5b330be268bed6ff4d27e0abcc0`, current authority for 174 mapping rows and 165 live assignments.
- `final_icon_frame_audit.json`: SHA-256 `c85df258c4aaaf37e905fdc14883cda6b0f8a1f41840df745a3136c830a66d01`, status `pass`. Its animation, registry, GUI, and state-binding evidence remains current. Its frozen 173-row, 43-mission, 164-assignment decision-mapping subsection is historical.
- Registry: `459` unique base definitions plus `5` unique super-event definitions = `464`; duplicate names `0`.
- Ledger: `46` unique sprite references; unresolved references `0`.
- Repaired static families: Values `4`, Callings `6`, Case cards `10`, District roles `7`, District states `6`; every family has unique runtime hashes.
- Non-icon records: `22/22` source, processed, package, and runtime files match; processed/runtime pixels match; all `22` source, processed, and runtime hashes are distinct. `asset_records.json` SHA-256: `5f12ace1db8b1ee59dd0530694cfbfaeec4d54a578c0ca773361a98b72047d3a`.
- Value/Calling validator SHA-256: `aa9a249348fb5bd864bb8ffc2a46ba6a67fc595cb58a08261cf32e8e5e61e007`.
- Case-card validator SHA-256: `924f2fc5a164ce6756ff453922a3e75cea6b8c79639b5254cec59072e746e1c4`.
- District-card validator SHA-256: `cc20a3bf3d48aa2f873af421a5c07ccce8943ee19edbaf785c040200b25eae84`.
- Route-identity validators: flags `14026c95ca9d3b8b9355a770d49658b05be738f06319252722f6ebd3e7ec1e65`; institutional tableaux `0da653422920087a28794a577963860b0dd2fbe2252353de241bf256c02d655d`; advisors `9e261b1ccd51249bdaebcd4cc2335a45988014e8aa740b43fad7c7dc8e25b02f`; built-in source evidence `7f892568ced49d74eb0d7e9cdfe3a796aee4dce13200b3f7a16b3fb2b16b6e18`.

## Legacy Ledger-seal proof

The Ledger seal is intentionally audited outside the five standardized animation entries because its legacy package layout differs.

- Eight unique `443x443` source slices and eight unique `64x64` processed frames.
- Exact `512x64` horizontal PNG sheet, SHA-256 `9404dc2e8af552c24c6a6bbec35e736573e017b6f04c57e5e6dacc3a62d789a1`.
- Static PNG equals processed frame `000`.
- Sheet DDS: strict one-level uncompressed BGRA, `131200` bytes, SHA-256 `17a5c98dcdc3cf9ba5317ecfb61ba9811e77152b603929675d6ab4c027114bd4`, pixel-identical to the sheet PNG.
- Static DDS: strict one-level uncompressed BGRA, `16512` bytes, SHA-256 `9a423fcf63ac58fa63fa24b4c77b29fc6636b97a0f282dcb0a21254622ddef2c`, pixel-identical to the static PNG.
- Review GIF: eight frames, looping, `120 ms` per review frame, SHA-256 `f73bad0e1cbec016d2fe43063e75490553692446ce030aead805e5702485d37b`; runtime timing is independently and correctly defined at `12 fps` in GFX.
- Contact sheet SHA-256: `6780acdccb83eb308dcd3b6e03cffcdc3bb1ccc0aca1c4e065747e6db22f901d`.

## Final super-event art, text, audio, and rights

Slots `96`-`100` select five route-distinct `457x328` images and five matching route descriptions under the shared title `UTOPIA HAS NEIGHBORS`. The selected Thomas More quotation is public-domain text documented in `015_utopia_manifesto_super_event_text_research.md`.

Audio ID `57` is assigned before `play_current_super_event_audio`, which respects the configured volume. The WAV is PCM s16le, `44,100 Hz`, stereo, `116.000000 s`, SHA-256 `05da5a30ba49c6592e5295dd499e9ad3e97279586bb7e7d51228ad236ce58655`. Frozen source-page, metadata, CC0 deed, CC0 legal code, original recording, processing, and catalogue evidence match the hashes in `docs/super_events/015_utopia_manifesto/audio_research.md`.

## Visual review and tool limits

Original-resolution contact sheets were inspected for reports/news, five super-event routes, 21 flag designs and their size ladder, four institutional tableaux, sixteen advisor dossiers, repaired Values/Callings, ten Case cards, seven District roles, six District states, and all required animation sequences. The institutional tableaux contain none of the prohibited people, faces, bodies, hands, crowds, silhouettes, statues, busts, mannequins, portraits, photographs, or human shadows. Advisor faces are distinct and readable; flags preserve authored emblem construction; repaired cards remain distinct at native size.

This was a static filesystem, image, registration, script-binding, codec, and metadata audit. HOI4 was not launched; audio was not auditioned in-engine; GIF timing was inspected from file metadata and frame sheets rather than treated as runtime playback. These are audit-tool limits, not fallbacks or missing deliverables.

## Prior P2 findings and resolution

An earlier `2026-07-16` snapshot correctly found four P2 gaps: incomplete Value icons, missing Calling icons, missing Case cards, and missing District cards/bindings. The three dated repair packages, GFX/GUI registrations, exact state bindings, durable district-role mapping, and planned-state lifecycle resolve all four. The history is retained here so the former blockers are not silently erased.

## Simplifications, omissions, fallbacks, and blockers

- Simplifications: none.
- Omissions: none.
- Fallbacks: none.
- Open blockers: none.
