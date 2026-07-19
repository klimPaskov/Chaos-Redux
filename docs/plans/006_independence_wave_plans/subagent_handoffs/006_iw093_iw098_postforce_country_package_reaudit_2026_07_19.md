# Event 006 IW-093 / IW-098 post-force country package re-audit

Date: 2026-07-19
Mode: read-only source and asset audit
Scope: DOX Asante and SOK Sokoto after the commander-roster and generation-bound starting-force tranche

## Verdict

The new command and starting-force tranche is wired with the requested fail-closed proofs at source level. Four fictional male corps commanders have complete commander portrait coverage, exact prepared-scope recruitment, corps-role roster proofs, and package-specific force mappings. A second force application in the same Event 006 generation is blocked by the current-generation receipt.

Neither package is runtime-admitted. Both setup paths still require an external runtime-content-attestation flag, and no setter for either flag exists in the repository. Pre-cutover SOK remains fail-closed because its setup path requires the post-cutover Siddiq leadership proof. No gameplay, asset, or localisation files were changed during this audit. This handoff is the only new file.

## Evidence reviewed

- Offline Paradox wiki pages: Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, Country creation, Character modding, Division modding, Equipment modding, Technology modding, and State modding.
- Vanilla documentation: `documentation/effects_documentation.md`, `triggers_documentation.md`, `script_concept_documentation.md`, `modifiers_documentation.md`, and `dynamic_variables_documentation.md`, including `recruit_character`, corps-commander roles, retirement, and generation-safe effects.
- Existing Chaos Redux handoffs for the commander asset package, source re-audit, FORM-24/25 linkage, and the Event 006 resume packet.
- No in-game load, save, runtime console, or MCP render was run. The installed MCP package exposes no Technology Tree Viewer, so technology-tree rendering remains an unresolved validation limitation.

## Country package coverage checklist

| Surface | DOX Asante | SOK Sokoto |
| --- | --- | --- |
| Identity and origin | Custom `DOX` shell and exact `original_tag = DOX` preflight | Vanilla `SOK` identity, no duplicate mod tag, exact `original_tag = SOK` preflight |
| Dormant origin gate | `exists = no`, reserved-country proof, IW-093 package id, state 274 anchor | `exists = no`, reserved-country proof, IW-098 package id, state 902 anchor |
| Leadership | `DOX_prempeh_ii` is recruited and promoted only in the exact prepared scope | Vanilla `SOK_siddiq_abubakar` is reused only on or after 1938-06-17; the pre-cutover Hasan branch is intentionally absent and fail-closed |
| Four new commanders | `DOX_kwame_frimpong`, `DOX_kwaku_ntim` | `SOK_umaru_gwadabawa`, `SOK_bello_rabah` |
| Roster proof | Both characters present and `is_corps_commander = yes` | Both characters present and `is_corps_commander = yes` |
| Starting force | Mapping proves `river_jungle` and tradition `p93` | Mapping proves `mounted_mobile` and tradition `p98` |
| Event 012 safety | Not applicable to the DOX adapter | Required by leadership, roster, and setup gates; Event 012 receipts are never cleared or converted |
| Runtime admission | Blocked until `independence_wave_iw093_runtime_content_attested` is set by an audited owner | Blocked until `independence_wave_iw098_runtime_content_attested` is set by an audited owner |

## Commanders, portraits, and localisation

The four new characters are male, military-only corps commanders. They have no advisor role blocks:

- `common/characters/006_independence_wave_iw093_iw098_characters.txt:58` `DOX_kwame_frimpong`
- `common/characters/006_independence_wave_iw093_iw098_characters.txt:81` `DOX_kwaku_ntim`
- `common/characters/006_independence_wave_iw093_iw098_characters.txt:104` `SOK_umaru_gwadabawa`
- `common/characters/006_independence_wave_iw093_iw098_characters.txt:127` `SOK_bello_rabah`

Each has `gender = male`, an `army_commander` portrait pair, a `corps_commander` role, and no `advisor` block. `DOX_prempeh_ii` is a civilian country leader and is not counted among these four commanders. Vanilla owns `SOK_siddiq_abubakar`; the mod does not duplicate that character.

The sprite contracts are complete and registered in `interface/006_independence_wave_iw093_iw098_portraits.gfx:15-44`. Each commander has a full 156x210 DDS and a separate 65x67 army-small DDS. The asset metadata records exact dimensions, legacy one-level uncompressed BGRA headers, and byte-exact RGBA decode against the processed PNGs:

- `docs/assets/006_independence_wave/iw093_iw098_commanders_2026_07_19/metadata/portrait_metadata.json`
- `docs/assets/006_independence_wave/iw093_iw098_commanders_2026_07_19/metadata/hashes.json`
- `gfx/leaders/006_independence_wave/portrait_DOX_kwame_frimpong.dds` and `_small.dds`
- `gfx/leaders/006_independence_wave/portrait_DOX_kwaku_ntim.dds` and `_small.dds`
- `gfx/leaders/006_independence_wave/portrait_SOK_umaru_gwadabawa.dds` and `_small.dds`
- `gfx/leaders/006_independence_wave/portrait_SOK_bello_rabah.dds` and `_small.dds`

The processed directory contains all eight matching PNGs with the required full and small dimensions. Localisation is present for all four names and descriptions in `localisation/english/006_independence_wave_iw093_iw098_country_core_l_english.yml:4-27`. The commander package manifest and handoff explicitly record `no_advisor_assets`, `no_advisor_manifests_or_sprites`, and that the small textures are commander miniatures rather than advisor dossier cards.

## Roster setup and role attestation

`common/scripted_effects/006_independence_wave_iw093_iw098_package_effects.txt:20-42` dispatches by exact temporary package id. The only roster recruiters are:

- `independence_wave_prepare_iw093_command_roster`: each recruitment limit requires `is_independence_wave_iw093_prepared_scope = yes` and the character to be absent, then recruits only Frimpong and Ntim.
- `independence_wave_prepare_iw098_command_roster`: each recruitment limit requires `is_independence_wave_iw098_prepared_scope = yes`, `is_independence_wave_iw098_event012_state_safe = yes`, and the character to be absent, then recruits only Gwadabawa and Rabah.

The SOK command helper has no date predicate of its own, but a pre-cutover prepared scope cannot enter SOK setup because date-appropriate leadership is required before politics, mapping, force application, or setup completion. This is a dormant preparation path, not an admission path.

`common/scripted_triggers/006_independence_wave_iw093_iw098_package_triggers.txt:313-328` requires all four recruited characters and explicitly checks `is_corps_commander = yes`. The shared `independence_wave_command_roster_ready` flag is set only inside the corresponding DOX or SOK setup blocks after those roster triggers pass (`...package_effects.txt:420-429` and `481-490`). There are no other setters for this flag in the package.

## Force mapping and one-time proof

The setup blocks call `independence_wave_load_force_package_mapping` only after the command-roster proof. They then call `independence_wave_apply_dynamic_starting_force` only when the mapping is valid (`...package_effects.txt:430-446` and `491-507`). Final setup success requires the same exact mapping and a current-generation receipt (`...package_effects.txt:538-544` and `571-577`).

The exact constants are:

- `common/script_constants/006_independence_wave_force_constants.txt:21-23`: `mounted_mobile = 6`, `river_jungle = 8`.
- `common/script_constants/006_independence_wave_force_package_constants.txt:170,175`: package profile values `p93 = 8`, `p98 = 6`.
- `common/script_constants/006_independence_wave_force_package_constants.txt:384,389`: military tradition values `p93 = 64`, `p98 = 70`.
- `common/script_constants/006_independence_wave_force_package_constants.txt:598,603`: reinforcement masks `p93 = 535`, `p98 = 647`.

The current-generation guard is `has_independence_wave_force_package_for_current_generation` in `common/scripted_triggers/006_independence_wave_force_triggers.txt:55-61`. `can_apply_independence_wave_force_package` rejects a second application in the same generation at line 90. The apply effect writes `independence_wave_force_package_generation_id = independence_wave_generation_id` and `independence_wave_force_package_applied` in `common/scripted_effects/006_independence_wave_force_effects.txt:871-887`. The only reset of that receipt is the generation reset in `common/scripted_effects/006_independence_wave_effects.txt:155-265`, where package cleanup runs before the generation variables and force receipt are cleared. This closes the same-generation free-unit loop while permitting a deliberate new generation reset.

## Cleanup and vanilla Siddiq protection

The package cleanup dispatcher is constrained to `original_tag = DOX` plus IW-093 or `original_tag = SOK` plus IW-098 (`...package_effects.txt:58-88`). DOX cleanup retires the Event 006 civilian leader and its two fictional commanders. SOK cleanup retires only `SOK_umaru_gwadabawa` and `SOK_bello_rabah` (`...package_effects.txt:635-640` and `687-692`). A repository-wide search found no `retire_character = SOK_siddiq_abubakar`. Event 012 focus-tree and lifecycle flags are explicitly preserved by the SOK cleanup helper.

## SOK cutover and living-country protections

`is_independence_wave_iw098_pre_cutover` is `date < 1938.06.17`. `has_independence_wave_iw098_date_appropriate_leadership` requires a post-cutover role proof, the post-cutover Sultan selection flag, recruited vanilla Siddiq, and Siddiq as the ruling leader. The missing Hasan branch is documented as fail-closed. SOK setup also requires this leadership trigger after the date selection step, so pre-cutover SOK cannot set setup-complete or apply the starting force.

`is_independence_wave_iw098_event012_state_safe` rejects `independence_wave_iw098_event012_focus_tree_replaced`, `africa_priority_member_package_active`, and `africa_priority_member_focus_tree_loaded`. The fixed-origin preflight requires `exists = no`, `original_tag = SOK`, the reserved-country proof, and exclusion of Soviet or already-active Event 006 origins. The mod registers no second SOK tag and contains no SOK history override. These checks preserve the living vanilla SOK identity and prevent a live-country takeover.

## Runtime attestation and release blockers

`has_independence_wave_iw093_runtime_content_attestation` and `has_independence_wave_iw098_runtime_content_attestation` are trigger-only receipts in `...package_triggers.txt:236-241`. Searches found no setter for either flag. Setup therefore remains intentionally blocked until the complete country, identity, visual, route, diplomacy, and scenario audit is accepted.

The following blockers remain from the source and asset audits:

1. The pre-cutover Hasan branch needs a sourced, distributable, identity-preserving male portrait before it can be authored. It must not be replaced with a generic or fallback face.
2. Exact 1935 Asante flag geometry is not yet proven.
3. Exact 1936 Sokoto flag geometry is not yet proven.
4. Host-settlement work still lacks concrete bilateral diplomatic outcomes for the DOX and SOK routes.
5. FORM-24 and FORM-25 still lack accepted member sets, territory and anchor contracts, identity tags, method mapping, sovereignty or integration outcomes, and cleanup ownership. The existing family registry is not an executable admission contract.
6. Final route politics, country identity, localisation, asset, and scenario audits remain pending. Runtime attestation must stay unset until those reviews pass.

Resolved by the current tranche: the four commander records, exact full and small commander assets, no-advisor constraint, prepared-scope roster recruitment, corps-role roster proofs, p93/p98 force mappings, generation-bound force receipt, and fictional-only Event 006 commander cleanup. Prempeh's portrait was already resolved by the parent work and is not repeated as a blocker here.

No fallback, generic portrait, advisor substitution, live-country takeover, or fail-closed weakening was introduced.

## Protected portrait hashes

The protected unrelated portraits remain unchanged:

- `gfx/leaders/006_independence_wave/portrait_BAY_rupprecht_of_bavaria.dds`: SHA-256 `7f0af64fdf4fecd49df454d1198935bb3ce6a8f74afc1ac82f8223704eaaad2b`.
- `gfx/leaders/006_independence_wave/portrait_RHI_josef_friedrich_matthes.dds`: SHA-256 `aa61cc3a12fb6670b690c7685feb9383383ce58599c9e6d6e7c14f20fab3bce2`.

These match `docs/assets/006_independence_wave/portrait_refresh_male_hoi4_2026_07_18/hashes/protected_runtime_sha256.sha256`.

## Parent handoff

Keep both runtime attestation flags unset. Do not promote either package to runtime-ready until the remaining flag, Hasan portrait, host diplomacy, FORM-24/25, and final route and scenario audits are closed. This audit supplies source-level evidence only and does not claim live-game validation.
