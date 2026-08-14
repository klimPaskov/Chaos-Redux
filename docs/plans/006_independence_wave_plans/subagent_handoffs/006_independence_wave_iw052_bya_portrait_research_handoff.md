# IW-052 BYA portrait identity and source research handoff

Date: 2026-08-15

Status: `blocked` / fail-closed for the exact vanilla 1936 opening consumer.

This was a bounded read-only identity and source audit. No source image, crop, processed derivative, `156x210` PNG, DDS, `.gfx`, character file, history file, gameplay file, or runtime wiring was created, staged, or committed.

## Decision

The installed vanilla BYA carrier does not define a named democratic country leader for the 1936 start. It recruits two named characters, but one is Stalinist and the other is despotist. The engine's unnamed or generic democratic fallback is not acceptable evidence for a grounded Buryat portrait.

A strong conditional historical source was found for the actual 1936 Buryat-Mongol officeholder Mikhei (Michei) Nikolayevich Erbanov. It is not a vanilla character token, and the source is a group photograph whose crop and parent-approved identity assignment remain unresolved. It therefore cannot be archived or wired under this bounded audit.

The package remains blocked until the parent explicitly chooses the exact Event 006 opening identity: either a newly approved Erbanov provisional-institution identity backed by the source below, or another exact 1936 Buryat officeholder/institution source. Do not silently relabel a vanilla generic texture as that subject.

## Installed vanilla identity evidence

- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/characters/BYA.txt:2-14` defines `BYA_seymon_ignatyev`, display name `Seymon Ignatyev`, civilian `large = GFX_portrait_Seymon_Ignatyev`, Stalinist country-leader ideology, and expiry `1943.1.1.1`.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/characters/BYA.txt:15-27` defines `BYA_bidia_dandaron`, display name `Chakravartin Bidia Dandarovitch Dandaron`, civilian `large = GFX_portrait_Chakravartin_Bidia_Dandarovitch_Dandaron`, despotism ideology, and expiry `1960.1.1.1`.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/history/countries/BYA - Buryatia.txt:1` sets capital state `564` (Ulan Ude).
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/history/countries/BYA - Buryatia.txt:89-104` sets the 1936 start to `ruling_party = democratic`, `last_election = "1936.1.1"`, democratic popularity `50`, neutrality popularity `50`, and recruits only the two characters above. There is no named democratic BYA character in this history file.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/interface/_leader_portraits.gfx:3458-3465` maps the two named tokens to `gfx/leaders/Asia/Portrait_Asia_Generic_2.dds` and `gfx/leaders/Asia/Portrait_Asia_Generic_3.dds`. These are generic Paradox textures, not identity-bearing source photographs.
- Those installed generic textures are `156x210`, 87,368 bytes, with SHA-256 `75ea54febbfb76011e9827d0c30feb82bd4747bcb0c976c9bb3e1792ab1d360c` and `7931b57e900ca175b0fd1c297584f8f755ebbc887655ef5670f967157d6feb7d`, respectively. They were not copied or archived.
- The project has no mod-local `common/characters/BYA.txt` or BYA country-history override. The only project BYA portrait consumer found is the unrelated Soviet Collapse token at `interface/005_soviet_collapse.gfx:1963`, `GFX_portrait_BYA_baikal_relay_council`, backed by the existing `gfx/leaders/005_soviet_collapse/BYA_leader.dds` (`156x210`, SHA-256 `8459cd38b25501b058e49789a2d4c2bdeec6101ad2e453ac941c72bf50e487f4`). It is not an Event 006 opening identity and must not be relabelled.
- Search across project `common/characters`, `history/countries`, `gfx/leaders`, `interface`, and localisation found no Event 006 BYA character, portrait manifest, or opening portrait consumer. The mod-local `common/scripted_effects/005_soviet_collapse_effects.txt:14927` reference is also unrelated.

The vanilla `Seymon Ignatyev` name is not a safe 1936 opening assignment even though the real Semyon Denisovich Ignatyev later served as first secretary of the Buryat-Mongol regional committee in 1937-1943. That date window starts after the 1936 opening, and the vanilla GFX is generic.

The vanilla Dandaron token is not a safe officeholder assignment. Bidia Dandarovich Dandaron is documented as a Buryat Buddhist lama, Tibetologist, and translator, not a 1936 Buryat state officeholder; he was born in 1914 and was 22 at the opening.

## Event 006 acceptance evidence

- `docs/specs/006_independence_wave_specs/research/006_package_research_resolution.csv:53` requires a sourced real male period leader valid for the release date and not already active elsewhere, or authentic archival material for the actual provisional institution, and explicitly says to block until a defensible sourced leader or institution is assigned.
- `docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv:53` identifies IW-052 as Buryatia, tag `BYA`, state `564`, Ulan Ude, reservation group `RG-564`, with a Buryat anchor and sourced historical symbols and leaders.
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_current_registry_gap_map_2026_08_15.md:73` records IW-052 as `HOLD` pending a sourced Buryat institution/leader, identity-matched symbols, and complete package evidence.
- `docs/plans/006_independence_wave_plans/asset_research/006_package_asset_coverage.md:76-78` permits existing character art only after a real male subject is period-valid, identity-correct, and not actively owned elsewhere. Vanilla generic art does not satisfy that gate.

## Conditional period source found

The best exact-date candidate is [Mikhei Nikolayevich Erbanov](https://ru.wikipedia.org/wiki/%D0%95%D1%80%D0%B1%D0%B0%D0%BD%D0%BE%D0%B2,_%D0%9C%D0%B8%D1%85%D0%B5%D0%B9_%D0%9D%D0%B8%D0%BA%D0%BE%D0%BB%D0%B0%D0%B5%D0%B2%D0%B8%D1%87), a Buryat-born Soviet party and state official who served as first secretary of the Buryat-Mongol regional committee from 1929 through October 1937. The biography also places him at the 27 January 1936 Kremlin reception as head of the Buryat-Mongol delegation, which directly fits the requested opening date and regional identity.

The attributable archival image is [Erbanov Markizova.JPG](https://commons.wikimedia.org/wiki/File:Erbanov_Markizova.JPG). The Wikimedia Commons API record checked on 2026-08-15 reports:

- depiction date `1936-01-27`;
- original dimensions `473x640` and source-file size `41,073` bytes;
- description `I. Stalin, M. Erbanov and E. Markizova`;
- original publication credit `Газета "Цемент" №1 от 1 января 1938 года`;
- artist `Mikhail Mikhailovich Kalashnikov`;
- Commons status `Public domain` under `PD-Russia` metadata with `AttributionRequired=false`.

The photograph shows Erbanov as the right-hand adult in a three-person scene. The image is period-fitting and attributable, but it is not a solo head-and-shoulders source; the crop must be reviewed for identity and framing before any archive or processed derivative is accepted. The Commons category also notes United States copyright caveat material, so final distribution-rights sign-off must retain the exact Commons record and not broaden the public-domain claim beyond its stated jurisdiction.

No copy of this image was retained in `docs/assets/portraits/006_independence_wave/` or its existing `processed/` directory during this audit.

## Rejected or insufficient alternatives

- `Seymon Ignatyev`: real person and later Buryat-Mongol officeholder, but office begins in 1937, after the requested opening; installed portrait is generic and no attributable source image was found in the Commons name searches.
- `Chakravartin Bidia Dandarovitch Dandaron`: Buryat cultural/religious figure rather than a 1936 state officeholder; the Commons `Dandaron.jpg` is a 2013 `300x399` self-published-work upload sourced to `dandaron.ru`, licensed `CC BY-SA 3.0`, and does not establish a 1936 office role.
- `GFX_portrait_BYA_baikal_relay_council` and `BYA_leader.dds`: existing Soviet Collapse institutional art, not Event 006 opening evidence.
- `Portrait_Asia_Generic_2.dds` and `Portrait_Asia_Generic_3.dds`: vanilla generic faces, not identity evidence.

## Review state and parent action

| Gate | Result |
| --- | --- |
| Exact vanilla named 1936 democratic leader | `FAIL` — no named democratic character is recruited by the 1936 BYA history. |
| Regional/office identity candidate | `CONDITIONAL PASS` — Mikhei Erbanov is a documented Buryat-Mongol officeholder active on 1936-01-27. |
| Source attribution and date | `PASS for candidate` — Commons identifies the people, date, publication credit, and photographer. |
| Rights | `CONDITIONAL` — Commons records Public Domain/PD-Russia; preserve the jurisdiction caveat and exact record. |
| Solo portrait framing | `HOLD` — three-person scene; crop and identity review not performed. |
| Package/runtime assignment | `FAIL / blocked` — Erbanov is not a vanilla BYA character token and parent approval is required. |

If the parent approves Erbanov as the authentic provisional institution identity, archive the untouched `473x640` original directly under `docs/assets/portraits/006_independence_wave/`, keep any crop/review derivative flat under the existing `processed/` directory, retain no `156x210` archive file, and require parent review before character/GFX/runtime wiring. If exact vanilla identity is mandatory, keep IW-052 blocked and research another 1936-valid source rather than assigning Erbanov to a generic vanilla token.

No RunPod operation, native ImageGen, crop processor, DDS conversion, MCP/in-game validation, character edit, history edit, gameplay edit, or runtime portrait wiring was performed.
