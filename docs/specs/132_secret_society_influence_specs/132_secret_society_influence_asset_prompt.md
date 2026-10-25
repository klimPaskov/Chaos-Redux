# Asset production prompt

This prompt requests future Event 132 art after owners freeze consumers and reconcile inventory. It reports no generated, accepted, registered or tested artwork. New names are working identifiers.

## Authority, inventory and ownership

Read the current `chaos-redux-event-assets` skill and its reference-library, family and manifest references. Canonical references live under `.claude/skills/chaos-redux-event-assets/assets/gfx_references/`. Inspect the library README, catalog, each matching contact sheet and the exact installed vanilla or current mod consumer. A nominal size below is the planned consumer contract, not evidence that a runtime sprite already exists. Resolve any consumer discrepancy before generation and record the accepted size.

Extend the owning semantic inventory before requesting new art. Search prior sources, prompts, alternative candidates, retries, manifests, aliases and actual registered textures. Missing wiring or a different filename does not establish a source gap. Each row needs its accepted consumer, source-gap or alternative reason, source classification, dimensions, path, sprite and reviewer. Reuse complete matching receipts.

Preserve existing runtime textures found in either the mod or installed vanilla. New alternatives stay uniquely named and unbound. A dedicated icon replacing a shared stand-in receives a new sprite and changes only its authorized consumer. The parent owns final GFX and gameplay wiring. Portrait production owns its expressly authorized portrait-specific references. No artist may redesign gameplay to create a consumer for surplus art.

Use `chaosx_icon_artist` for icons and `chaosx_generated_event_art` for fictional documentary scenes and the static picture when those configured roles are actually available. Otherwise report the real production route without claiming those roles ran. Grounded-source research and portraits retain their specialist ownership.

## Naming and family contract

Expand each key below into its stated filename and sprite. Before production, map every actual consumer ID to its row. Same-family consumers may share the specified art when their meaning matches. Never resize one asset type into another.

| Family | Planned size and source | Runtime path and sprite family | Canonical references |
| --- | --- | --- | --- |
| Idea/spirit | 64×64, original generated symbolic subject with native alpha | `gfx/interface/ideas/132_secret_society_influence/idea_132_<key>.dds`, `GFX_idea_132_<key>` | `icons/ideas/` |
| Decision | 32×32, original generated subject with native alpha | `gfx/interface/decisions/132_secret_society_influence/decision_132_<key>.dds`, `GFX_decision_132_<key>` | `icons/decisions/` |
| Mission | 32×32, separately composed generated subject with native alpha | `gfx/interface/decisions/132_secret_society_influence/mission_132_<key>.dds`, `GFX_mission_132_<key>` | `icons/missions/` |
| Category icon | 32×32 planned, generated subject with native alpha | `gfx/interface/decisions/132_secret_society_influence/decision_category_132_case.dds`, `GFX_decision_category_132_case` | `icons/decision_categories/` |
| Static category picture | 114×101 planned, fictional institutional still life, consumer-opaque canvas | `gfx/interface/decisions/132_secret_society_influence/category_picture_132_case.dds`, `GFX_category_picture_132_case` | `icons/decision_categories/pictures/` |
| Report | 210×176 finished RGBA card from an opaque fictional documentary source | `gfx/event_pictures/132_secret_society_influence/report_event_132_<key>.dds`, `GFX_report_event_132_<key>` | `event_art/report/` |
| News | 397×153 opaque black-and-white documentary scene | `gfx/event_pictures/132_secret_society_influence/news_event_132_<key>.dds`, `GFX_news_event_132_<key>` | `event_art/news/` |
| Focus | 94×86, original generated full focus composition with native alpha | `gfx/interface/goals/132_secret_society_influence/goal_132_<key>.dds`, `GFX_goal_132_<key>` | `icons/national_focus/` |
| Achievement | 64×64 subject and three final states | `gfx/achievements/<full_achievement_id>{,_grey,_not_eligible}.dds`, exact achievement lookup | `icons/achievements/` plus supplied templates |

Use single forward slashes and the appropriate existing GFX registry, or an owner-approved `interface/132_secret_society_influence_icons.gfx` and picture registry. Achievement files remain root-level.

## Spirit and action coverage

The eight spirit subjects cover three visible slots. `network_low`, `network_entrenched` and `network_dominant` depict a private folio, a folio bound into an office network, and records controlling an institutional keyring. Distinguish stages by silhouette and construction, not colour alone. Each band serves both normal and accommodated modifier variants. Text conveys the contract, so accommodation does not require a fourth spirit slot or unrelated icon.

`response_inquiry`, `response_command` and `response_combined` depict examination tools, protected military orders and a deliberate combined composition. They cover the one consolidated response-burden slot. `aftermath_recovery` and `aftermath_settlement` depict repaired public records and a provisional institutional settlement. Map every finite aftermath variant to its actual meaning. Do not keep recovery art displayed after the modifier has cleared.

Create these decision families with original 32×32 compositions:

| Key | Required semantic consumers |
| --- | --- |
| `examine_records` | First lead, independent corroboration and coordination-link examination |
| `protect_source` | Protect or turn a real insider, preserve testimony, or shelter an identified organizer |
| `secure_command` | Officer protection, verified command separation and wartime coordination |
| `remove_leadership_access` | Close the proven organizing authority |
| `close_funding` | End the identified payment or procurement route |
| `close_institutional_access` | Replace proven appointment/access channels and seal recorded residual contacts |
| `negotiate_obligation` | Choose or renew one administrative, procurement or command contract |
| `exit_obligation` | Settle the actual contract and leave accommodation |
| `finance_interference` | Voluntarily finance a traceable operation through a known foreign connection |
| `partner_inquiry` | Consented bilateral inquiry, evidence exchange and foreign closure support |
| `public_exposure` | Publish corroborated institutional evidence during a prepared challenge |
| `emergency_response` | Costly emergency intervention, including the visibly distinct blind-purge warning |
| `restore_institutions` | Consolidation, post-capture recovery and verified restoration |

Use four mission subjects: `case_project`, `protected_action`, `bilateral_case` and `consolidation`. The last replaces a finished commitment rather than adding a fourth active row. The category icon combines a dossier and institutional key. The static picture shows a ministry desk with linked appointment records and sealed correspondence, without fake buttons, values, meters or readable generated text. It may serve another eligible Event 132 category only when the same subject still fits.

## Reports and public outcomes

Create six distinct period documentary source scenes. `opening_irregularities` shows obstructed administrative work through misplaced orders and linked files. `corroborated_records` shows secured records and independent examination. `negotiated_obligation` shows an official agreement and the material burden behind it. `rival_circles` contrasts two human patronage circles through separate correspondence and access routes. `foreign_chapter` shows a proven liaison and financial or diplomatic connection. `cabinet_preparation` shows civilian authority and military orders being coordinated for a challenge.

Use objects, rooms and non-identifying activity rather than invented portraits of real ministers. Avoid occult symbols, ritual costume and historical society emblems. Any clearly identifiable real building, document, uniform or person requires research and an appropriate source route.

Generate or source the photograph first. Apply `.claude/skills/chaos-redux-event-assets/tools/process_report_event_image.py` for cover crop, monochrome/sepia, grain, paper border, deterministic tilt, transparent margins and soft shadow. Do not ask generation to fake the finished tilted card. Retain the untouched photograph and exact 210×176 processed RGBA preview.

The two news keys are `government_contested` and `institutions_restored`. The first supports an actual public takeover or military split, with composition broad enough that text distinguishes them truthfully. The second supports verified restoration after a public crisis. Both use 397×153 black-and-white press composition with no modern overlays or generated lettering.

## Twelve claimant focus subjects

Every listed focus receives a distinct 94×86 composition. For this family, `<key>` is the exact focus ID with only `e132_` removed, producing names such as `goal_132_claimant_assert_continuity.dds` and `GFX_goal_132_claimant_assert_continuity`. Match the normal/shine declarations of the actual focus consumer without generating extra glow artwork.

| Exact focus ID | Symbol direction |
| --- | --- |
| `e132_claimant_assert_continuity` | Public registry and an intact administrative seal |
| `e132_claimant_reconcile_officer_lists` | Matched service rolls and officer insignia |
| `e132_claimant_keep_depots_open` | An existing depot, supply crate and open route |
| `e132_claimant_conditional_amnesty` | A released restraint beside a formal undertaking |
| `e132_claimant_binding_appointments` | Office keys bound to an appointment record |
| `e132_claimant_joint_operational_staff` | Coordinated command instruments and shared orders |
| `e132_claimant_replacement_drafts` | Muster papers and ordinary national service equipment |
| `e132_claimant_priority_repairs` | Repair tools beside damaged existing machinery |
| `e132_claimant_provincial_guarantees` | A protected civic record and local administrative seal |
| `e132_claimant_central_allocation` | A distribution ledger controlling several supply routes |
| `e132_claimant_capital_settlement` | A capital administration document and reconciled keys |
| `e132_claimant_restore_administration` | Reopened public offices and a restored registry |

These icons serve only the compact claimant crisis tree and its specified rewards.

## Portrait and flag treatment

Reuse safely owned existing national actors and their established portraits. Only an actual missing portrait consumer goes to `chaosx_portrait_creator`. For a grounded person or institution, that worker needs attributed exact-identity or authentic institutional source material and independent likeness, framing and provenance review. Freeze the existing runtime basename, path and sprite before producing the 156×210 texture. Preserve original bytes, lossless crop, equality JSON and provenance under `docs/assets/portraits/132_secret_society_influence/`. An accepted unchanged source placeholder is a valid selected mode. A styled final exists only when the user explicitly requests it, and only the user operates RunPod. Do not invent a historical person's face or produce advisor cards merely because an advisor exists.

The temporary claimant inherits the host nation's proper flag family and receives a distinct temporary governmental name and verified country identity through Part 4. No base flag replacement is requested here. If an accepted claimant identity later explicitly requires a new flag, open a separate authorized row with exact cosmetic/tag consumer, researched national motifs and original flat generated design. Deliver `<accepted_flag_key>.tga` at 82×52 under `gfx/flags/`, 41×26 under `gfx/flags/medium/` and 10×7 under `gfx/flags/small/`, with vanilla-compatible bottom-origin encoding. Preserve the host base flag. No waving scene, palette-swap substitute, arbitrary religious emblem or DDS flag workaround is acceptable.

## Production evidence and completion

Save every exact generation request before the call, including references, their roles and native transparency. Preserve immutable candidate and parent versions, source hashes, dimensions, alpha evidence, focused edit delta and explicit final selection. Alpha-backed icons require true transparent generation, then preserved alpha through resizing and conversion. Background removal is a documented fallback after native-alpha failure, never the normal method. Inspect against dark, light and checker backgrounds at source and actual consumer size.

Convert ordinary 2D PNGs with `.claude/skills/chaos-redux-event-assets/tools/convert_to_dds.py`. Require the canonical one-level BGRA layout: 128-byte header, header size 124, pixel-format block at byte 76 with size 32 and flags 65, fourCC 0, and 32-bit masks `0x00FF0000`, `0x0000FF00`, `0x000000FF`, `0xFF000000`. Require texture cap `0x1000` at byte 108 and exact length `128 + width × height × 4`. Verify alpha and decode the final DDS for native-size visual comparison. PNG-only delivery is incomplete.

The six achievement subjects and exact state workflow are specified in the achievement prompt. Use its dedicated triplet processor instead of independently converting three generated variants.

Maintain `docs/assets/132_secret_society_influence/manifest.md` and `gfx_handoff.md` with every requirement, actual consumer, source route, prompt, preview, runtime path, sprite, review and status. Record unavailable evidence honestly. Before temporary workspace cleanup, promote durable lineage, licensing, selection and consumer facts into the surviving event documentation. Parent acceptance and actual runtime linkage remain distinct from artwork production.
