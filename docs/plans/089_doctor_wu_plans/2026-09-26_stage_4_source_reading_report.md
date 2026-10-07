# Doctor Wu Stage 4 source-reading report

Date: 26 September 2026. Stage: DW-089-S4.

## Supplied-source gate

The fresh source-reading gate passed before repository research and Part 8 authoring. The pass covered all current supplied Project Sources, the original Doctor Wu brief, the cumulative Stage 3 package, and the distinct earlier package versions still present in this conversation. Previous reading reports were read as historical records, not used as a substitute for reading their source files again.

There were **82 distinct text identities totaling 1,992,408 bytes**. Every identity was displayed and processed in bounded reads. The archive contributed 42 text sources, including all twenty specialist definitions from its nested archive. The protocol and all current standalone Project Source files were included. Thirty-six additional mounted paths were byte-compared with the completed identities. Identical aliases did not require a second interpretation of identical bytes.

The [machine-readable inventory](2026-09-26_stage_4_source_inventory.json) records source paths, archive aliases, SHA-256 values, sizes, line counts, and complete read ranges. Extraction, inventory, and hashes established what needed reading and which aliases were identical. They did not replace content reading. Truncated displays were continued through smaller ranges. No supplied source remains unavailable, truncated, or partially read in this task.

The original brief remains unchanged at [source_inputs/2026-09-24_doctor_wu_user_brief.txt](source_inputs/2026-09-24_doctor_wu_user_brief.txt). The extracted source and role files are inventoried rather than copied into the specification package. Source locations in the inventory describe the working environment of this reading pass, not paths the later coding environment is expected to possess.

## Repository snapshot

The GitHub connector returned `master` at `5212636eef9f9607691ddc1348bddade1bafe0dd`. Repository reads below were pinned to that revision. This is the same revision recorded by Stage 3. Branch metadata is a snapshot of the connected repository, not evidence of a working-tree checkout or a later commit.

There were ten complete owner-file reads, three bounded owner-file reads, and fourteen bounded offline wiki consultations. Searches and directory listings served navigation only and are not counted as completed reads. In particular, the oversized first Black Plague overview response was truncated. The complete file was subsequently read through the three smaller ranges listed below.

### Complete owner reads

| Repository path | Requested coverage | Returned blob identity |
| --- | --- | --- |
| `docs/systems/famine_system.md` | 1-150, returned EOF | `f4efdba47cf34566b4b2a7710955758c423be2ee` |
| `docs/systems/migration_system.md` | 1-160, returned EOF | `0d2bfdb3994cab5f446495727a02e3fc38cfeec3` |
| `docs/events/016_brilliant_scientist/systems/projects.md` | 1-80, 81-165, 166-265, 266-400, returned EOF | `b0f3a86dc95f409d2aba69e2c76526c485155414` |
| `docs/events/020_black_plague/overview.md` | 1-55, 56-90, 91-150, returned EOF. Initial 1-135 truncated request excluded | `42188d3bd33d8dec50a33dc9bd70b55a8f078b6a` |
| `docs/systems/cbrn_warfare/biological_warfare/zombie_prevention_disease_integration.md` | 1-160, returned EOF | `a59898f29efefc798f45cd563de8bf7b3d748781` |
| `docs/events/002_zombie_outbreak/overview.md` | 1-110, 111-275, 276-450, 451-630, 631-820, 821-1010, 1011-1160, returned EOF | `24fbfdc1ef4030b4344cb2775b8abb7ed2845224` |
| `docs/events/016_brilliant_scientist/systems/biological_operations.md` | 1-100, returned EOF | `38b23417fad1998492509a13b2fd4a29f6587d79` |
| `common/scripted_triggers/chaosx_dynamic_triggers.txt` | 1-190, returned EOF | `965f7f83d133ab1e616299adf422c16325db9ffb` |
| `common/scripted_effects/016_brilliant_scientist_custom_technology_api_effects.md` | 1-125, 126-210, returned EOF | `7e75fbec80558ea00ced2e21626fcdc3738ff53d` |
| `docs/systems/cbrn_warfare/chaos_unit_family_registry.md` | 1-70, 71-155, returned EOF | `120e7569306ef83fa3fc583e25b99f72ce11ea1e` |

The project portfolio, public technology API, biological operations guide, and shared unit-family contract establish the current medical, paleogenetic, xenobiological, native-operation, and nonhuman integration boundaries used by this part. The complete Black Plague and Zombie Outbreak guides include their reconstruction and defeat endpoints. Their historical implementation assertions remain owner documentation, not fresh tests run by this task.

### Bounded owner reads

| Repository path | Requested coverage | Returned blob identity |
| --- | --- | --- |
| `common/scripted_effects/biological_countermeasure_effects.txt` | 1-145 | `b7cd6b9b3d9f3021b9fd271d04b1ad6949e5c804` |
| `docs/testing/chaosx_test_country.md` | 1-95, 96-150 | `e1b10f9f5630d83d76f36319d75183fb263da6c3` |
| `docs/events/014_cannibalism/overview.md` | 1-85 | `be139005189182212c4aeb07e476e4f776a9108e` |

These bounded reads cover medical investment and reservation entry points, the current CXT extension contract, and the Cannibalism medical, material, and reconstruction boundary. They do not establish full-file review or complete call-chain validation. The Cannibalism connection remains limited to a proposed owner-exposed biological condition. No medical adapter for its political or material values is presumed to exist.

### Offline wiki consultations

| Repository snapshot page | Lines consulted |
| --- | --- |
| `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md` | 72–109 |
| `paradox_wiki/Triggers - Hearts of Iron 4 Wiki.md` | 64–95 |
| `paradox_wiki/Effects - Hearts of Iron 4 Wiki.md` | 83–108 |
| `paradox_wiki/Modifiers - Hearts of Iron 4 Wiki.md` | 37–69 |
| `paradox_wiki/Localisation - Hearts of Iron 4 Wiki.md` | 48–73 |
| `paradox_wiki/Scopes - Hearts of Iron 4 Wiki.md` | 28–65 |
| `paradox_wiki/On actions - Hearts of Iron 4 Wiki.md` | 15–54 |
| `paradox_wiki/Event modding - Hearts of Iron 4 Wiki.md` | 30–62 |
| `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md` | 65–103 |
| `paradox_wiki/Idea modding - Hearts of Iron 4 Wiki.md` | 21–55 |
| `paradox_wiki/AI modding - Hearts of Iron 4 Wiki.md` | 1–43 |
| `paradox_wiki/Unit modding - Hearts of Iron 4 Wiki.md` | 47–125 |
| `paradox_wiki/Equipment modding - Hearts of Iron 4 Wiki.md` | 29–67 |
| `paradox_wiki/Technology modding - Hearts of Iron 4 Wiki.md` | 81–125 |

These pages were consulted through the repository's offline snapshot. They are bounded reference reads, not full-page reads. No web copy of the Paradox wiki replaced a supplied source. The ordinary decision, effect, scope, unit, and technology references inform proposed implementation boundaries but do not prove native behavior.

## Capability and reference limits

The installed vanilla locations `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV` and `/mnt/c/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV` were not available in this runtime. The required installed documentation, exact game consumers, model scales, counter palettes, and audio bindings were not inspected. These remain implementation prerequisites.

GitHub tools were used for actual reads. Codex Native discovery exposed an inventory action requiring an outer-turn token that was not supplied. Plugin discovery for HOI4 and collaboration returned no usable project-specialist spawning or HOI4 inspection route. No token was invented and no substitute generic agent was presented as a named specialist.

No specialist subagent, HOI4 MCP call, live-game test, image generation, 3D provider, Blender authoring, audio production, or workbook change ran. The [usage maps](2026-09-26_stage_4_mcp_and_subagent_usage_maps.md) are future assignments. They are not execution receipts.

## What this pass establishes

The supplied-source gate is complete. Part 8 is grounded in the original requested designed-life family, earlier authored projects, and the inspected owner boundaries. Repository evidence distinguishes existing behavior from new proposals. The local checks establish document preservation and symbolic accounting consistency only. They do not establish engine feasibility, approved balance, accepted owner amendments, or completion of Event 089.
