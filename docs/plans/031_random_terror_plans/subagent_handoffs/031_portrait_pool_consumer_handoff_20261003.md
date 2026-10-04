# Event 31 portrait pool and consumer handoff

Status: current 45-portrait source archive and complete consumer map delivered; parent-owned history recruitment, active role selection, and terminal entity lifecycle remain open. No commit was made.

## Changed files and ownership

- `common/characters/031_random_terror_characters.txt`: added the 36 remaining roleless pool identities with one-person gender metadata and existing registered sprites. The parent-owned `JMX_random_terror_final_command_council` and `JMX_random_terror_unanswered_presence` blocks were left intact.
- `docs/assets/portraits/031_random_terror/`: archived 45 current full-resolution PNG masters, five prior masters for source lineage, the source/runtime contact sheets, prior production evidence, a prompt-evidence note, and a 45-row manifest with source and DDS hashes.
- `docs/plans/031_random_terror_plans/subagent_handoffs/031_portrait_pool_consumer_handoff_20261003.md`: this handoff.

No `.gfx`, history, event, scripted effect, country, localisation, focus, decision, advisor, GUI, or gameplay selection file was changed by this worker. The file `interface/031_random_terror.gfx` already registers the 45 static pool sprites and one separate `GFX_Portrait_Random_Terror_Entity_Animated` frame sprite for the entity sheet; none required portrait-pool rewiring.

Parent-owned changes now visible in the shared tree are the two JMX character blocks and the JMX history recruitment entries at lines 53–54; those edits are not attributed to this worker.

## Council 04 and entity review

Council 04 is the people-free symbolic command image in the accepted institutional pool. Its 1081x1455 source is a dark storeroom composition with a locked chest bound by several ropes and five keys laid in front; it contains no person, personal gender cue, readable text, real flag, extremist mark, or sacred symbol. At the current 156x210 DDS size the chest and keys remain legible as controlled institutional authority. This is compatible with the explicitly authorized preterminal human command institution, and I found no visual defect requiring replacement.

Council 04 source SHA-256 is `f7d7ce63ac2db77a2a52ff988a2b580d6c8cc611246654cd76ef41680a79dbd2`; its runtime DDS is 156x210, 131168 bytes, SHA-256 `6635740f85338b1e74965743ad2450d879e4d737241a6354befcefdb764847ac`, registered as `GFX_Portrait_Random_Terror_Council_04` at `gfx/leaders/031_random_terror/leader_random_terror_council_04.dds`.

The parent-owned character block currently uses the exact ID `JMX_random_terror_final_command_council`, the name `Final Command Council`, `ideology = despotism`, and no `gender` field. It uses the registered Council 04 sprite, and JMX history now recruits it before the terminal transaction. No second Council 04 character ID was added.

The current entity master and static DDS show an impossible, faceless luminous presence without a specific deity, demon, real-person identity, or sacred mark. The parent-owned `JMX_random_terror_unanswered_presence` block retains its name and sprite without an initial `country_leader` role. The JMX history recruits that roleless character at line 53 and the Final Command Council at line 54; only the gated terminal transaction may add and promote the entity's leader role. The parent should use `set_nationality` if the active terminal host is not JMX.

## 45-row fictional identity and consumer map

The full source path, source dimensions and SHA-256, runtime sprite, DDS SHA-256, and status for each row are in the [durable archive manifest](../../../assets/portraits/031_random_terror/manifest.md). `Existing` means a prior stable character ID was preserved, `Parent-owned` marks the two exact JMX blocks, and `New roleless` means this worker added the identity and portrait reference without an initial leader role.

| Portrait | Character ID | Identity | Visible gender or class | Role and consumer state |
| --- | --- | --- | --- | --- |
| `clandestine_01` | `JNX_random_terror_nera_vos` | Nera Vos | female | Network coordinator; existing ID |
| `clandestine_02` | `JQX_random_terror_clandestine_02` | Oren Kest | male | Communications relay coordinator; new roleless pool entry |
| `clandestine_03` | `JQX_random_terror_clandestine_03` | Vera Dain | female | Records and dispatch coordinator; new roleless pool entry |
| `clandestine_04` | `JQX_random_terror_clandestine_04` | Halen Rook | male | Safehouse network steward; new roleless pool entry |
| `clandestine_05` | `JQX_random_terror_clandestine_05` | Sera Vael | female | Cross-border liaison; new roleless pool entry |
| `clandestine_06` | `JQX_random_terror_clandestine_06` | Toren Marr | male | Route network coordinator; new roleless pool entry |
| `council_01` | `JHX_random_terror_shadow_council` | Shadow Council | institution; no personal gender | Collective command body; existing ID |
| `council_02` | `JIX_random_terror_war_directorate` | War Directorate | institution; no personal gender | Military command institution; existing ID |
| `council_03` | `JKX_random_terror_ideological_secretariat` | Ideological Secretariat | institution; no personal gender | Political institution; existing ID |
| `council_04` | `JMX_random_terror_final_command_council` | Final Command Council | institution; no personal gender | Preterminal human command institution; parent-owned |
| `council_05` | `JQX_random_terror_council_05` | Regional Continuity Council | institution; no personal gender | Regional institutional council; new roleless pool entry |
| `council_06` | `JQX_random_terror_council_06` | Civic Coordination Council | institution; no personal gender | Civic institutional council; new roleless pool entry |
| `criminal_01` | `JQX_random_terror_criminal_01` | Talia Sorn | female | Warehouse and transport broker; new roleless pool entry |
| `criminal_02` | `JQX_random_terror_criminal_02` | Daren Sol | male | Market finance negotiator; new roleless pool entry |
| `criminal_03` | `JQX_random_terror_criminal_03` | Elva Rinn | female | Supply and procurement broker; new roleless pool entry |
| `criminal_04` | `JQX_random_terror_criminal_04` | Brant Korr | male | Senior procurement broker; new roleless pool entry |
| `criminal_05` | `JQX_random_terror_criminal_05` | Taren Holt | male | Smuggling network manager; new roleless pool entry |
| `criminal_06` | `JQX_random_terror_criminal_06` | Mara Kern | female | Territorial patronage broker; new roleless pool entry |
| `entity` | `JMX_random_terror_unanswered_presence` | The Unanswered Presence | impossible; no personal gender | Terminal transformation only; parent-owned roleless character |
| `jihadist_01` | `JLX_random_terror_rasim_vey` | Rasim Vey | male | Route leader; existing ID |
| `jihadist_02` | `JQX_random_terror_jihadist_02` | Rina Cor | female | Network organizer; new roleless pool entry |
| `jihadist_03` | `JQX_random_terror_jihadist_03` | Sela Or | female | Regional coalition organizer; new roleless pool entry |
| `jihadist_04` | `JQX_random_terror_jihadist_04` | Kalen Rusk | male | Field organization leader; new roleless pool entry |
| `jihadist_05` | `JQX_random_terror_jihadist_05` | Darin Tal | male | Border corridor commander; new roleless pool entry |
| `jihadist_06` | `JQX_random_terror_jihadist_06` | Mira Pel | female | Foreign-network coordinator; new roleless pool entry |
| `jihadist_07` | `JQX_random_terror_jihadist_07` | Varek Noll | male | Movement operations chief; new roleless pool entry |
| `jihadist_08` | `JQX_random_terror_jihadist_08` | Lysa Cem | female | Regional network leader; new roleless pool entry |
| `military_01` | `JOX_random_terror_liora_vask` | Liora Vask | female | Military-command leader; existing ID |
| `military_02` | `JQX_random_terror_military_02` | Tavin Or | male | Rail-security commander; new roleless pool entry |
| `military_03` | `JQX_random_terror_military_03` | Maera Dren | female | Garrison coordination leader; new roleless pool entry |
| `military_04` | `JQX_random_terror_military_04` | Ilan Varo | male | Field operations chief; new roleless pool entry |
| `military_05` | `JQX_random_terror_military_05` | Vara Sen | female | Logistics commander; new roleless pool entry |
| `military_06` | `JQX_random_terror_military_06` | Ronan Kess | male | Territorial defense commander; new roleless pool entry |
| `millenarian_01` | `JQX_random_terror_millenarian_01` | Eda Varen | female | Movement organizer; new roleless pool entry |
| `millenarian_02` | `JQX_random_terror_millenarian_02` | Iven Rask | male | Movement convenor; new roleless pool entry |
| `millenarian_03` | `JQX_random_terror_millenarian_03` | Mira Kett | female | Communal assembly organizer; new roleless pool entry |
| `millenarian_04` | `JQX_random_terror_millenarian_04` | Soren Vale | male | Movement strategist; new roleless pool entry |
| `millenarian_05` | `JQX_random_terror_millenarian_05` | Nira Bex | female | Movement advocate; new roleless pool entry |
| `millenarian_06` | `JQX_random_terror_millenarian_06` | Daren Krell | male | Public movement speaker; new roleless pool entry |
| `revolutionary_01` | `JPX_random_terror_arel_venn` | Arel Venn | male | Revolutionary leader; existing ID |
| `revolutionary_02` | `JQX_random_terror_revolutionary_02` | Tesa Marr | female | Labor committee organizer; new roleless pool entry |
| `revolutionary_03` | `JQX_random_terror_revolutionary_03` | Lena Oris | female | Regional committee leader; new roleless pool entry |
| `revolutionary_04` | `JQX_random_terror_revolutionary_04` | Tovan Hark | male | Cadre operations organizer; new roleless pool entry |
| `revolutionary_05` | `JQX_random_terror_revolutionary_05` | Edda Nyra | female | Civic assembly organizer; new roleless pool entry |
| `revolutionary_06` | `JQX_random_terror_revolutionary_06` | Eran Dov | male | Regional movement commander; new roleless pool entry |

The original eight character IDs remain stable. The six councils use institutional names and no personal `gender`; the impossible entity also has no personal `gender`. The 36 new pool definitions have no initial `country_leader` role and do not create advisor or commander-card portraits.

## Image evidence, dimensions, and hashes

The source archive contains 45 current PNG masters and five previous PNG masters. Current master dimensions range from 1080x1452 to 1083x1457; each current source SHA-256 is recorded row by row in the archive manifest. Each installed DDS is 156x210, 131168 bytes, fully opaque, and uses the required one-level 32-bit BGRA header. Current DDS SHA-256 values in the 45-row manifest match the 444-row inventory 45/45, and a direct current header/alpha pass found 45/45 valid.

The source and runtime sheets are [current source masters](../../../assets/portraits/031_random_terror/review/current_source_masters_contact_sheet.png) and [current runtime DDS](../../../assets/portraits/031_random_terror/review/current_runtime_dds_contact_sheet.png). Both contain 45 labeled 156x210 tiles on an 860x2174 sheet. I inspected the full set for repeated faces, visible gender, crop/framing, modern props, readable text, real-person resemblance, extremist or sacred marks, and route fit; I found no defect requiring ImageGen replacement.

The original processed PNG directory `docs/assets/031_random_terror/processed_png/portraits/` and the prior per-portrait processing JSON are absent. The current runtime DDS contact sheet is decoded from installed DDS files and is review evidence, not a substitute for the missing source-processed PNGs or per-row equality evidence.

## Consumer and lifecycle contract for the parent

The local Character modding reference says `recruit_character` must be placed in country history and that characters without a role at start must receive it later with `add_country_leader_role` (`paradox_wiki/Character modding - Hearts of Iron 4 Wiki.md`, lines 50 and 58–59). Installed effects documentation lists `add_country_leader_role` at lines 985–1006, `recruit_character` at lines 5696–5705, and `set_nationality` at lines 7397–7414.

JMX history now recruits `JMX_random_terror_unanswered_presence` at line 53 and `JMX_random_terror_final_command_council` at line 54. The entity remains recruited but roleless until the actual gated transaction. Add and promote its leader role only in that transaction, and use `set_nationality` if it must move to a different human host.

The parent must recruit the 36 new roleless candidates through their appropriate country histories, then add and promote a `country_leader` role only when that candidate is selected. This handoff does not claim an identity is consumed merely because its definition or portrait exists. Histories for the remaining 36, actor selection/recycling, selected-candidate role creation, and the entity terminal gate remain parent-owned and unimplemented here.

The offline `hoi4.reference_context` call timed out after 600 seconds, and the bounded `hoi4.source_lookup` request did not return and was stopped after one minute. Local wiki and installed documentation sections were read directly as the AGENTS.md fallback; no Paradox wiki web access was used.

## Review limits and remaining blockers

- Independent visual review was not performed; the source and DDS sheet inspection in this handoff is my producer-side review. Parent visual review is still required.
- Exact per-image ImageGen prompt text and output-ID records are missing from the previously cited `docs/assets/031_random_terror/portraits/prompts/prompt_record.md`; the old source manifest and processing-evidence JSON paths cited by the prior handoff are also absent. The accepted prompt direction and present source hashes are preserved, but missing prompt text was not invented.
- `.gitignore` line 80 ignores `docs/assets/`, so the new archive is present on disk but hidden from ordinary `git status` and a normal `git add`. It was not force-added or staged, and the ignore rule was not changed; the parent must account for this when including the archive in a later commit.
- The 2026-09-01 decode index predates current `clandestine_06` and `jihadist_08` source/DDS revisions. Their current source hashes and current DDS hashes are in the archive manifest and match the current inventory, but no current processed PNG or per-row source-to-DDS equality record was present.
- No Internet source attribution or rights research was applicable because every subject is fictional, institutional, or impossible. No RunPod operation, new ImageGen call, or portrait regeneration occurred.
- No game launch or in-game validation was performed. The parent owns engine recruitment and role activation, and the user owns live-game validation.
