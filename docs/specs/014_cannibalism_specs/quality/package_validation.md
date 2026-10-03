# Package Validation

Status date: 2026-10-03 receipt reconciliation; no full-package validation claim.

The [current continuation checkpoint](../../../plans/014_cannibalism_plans/2026-10-03_continuation_report.md) bounds implementation evidence. The current parent instruction preserves 56 distinct HOI4-style final portraits as accepted and unfinished, seven bespoke models across nine families, approved cavalry/infantry visual reuse and no animation toggle. All July zero audits and their aggregate inventory/structural results below remain historical frozen-tranche evidence, not fresh validation of the current full package.

## Structural and gameplay-definition evidence

- Focus IDs are unique and exact at 68 warlord, 108 unified, and 28 Wendigo focuses.
- Every focus has its AI block, focus-specific reward helper, localisation, and unique registered icon.
- Both target scorers and both decision-weight MTTH entries exist. Exactly six unified targeted decisions consume the shared unified weight.
- All eight maintained mission IDs and seven added action IDs exist once and retain their target, cost, progress, outcome, AI, and cleanup contracts.
- Incarnation reset begins with one idempotent cleanup covering exactly 14 timed missions: two baseline missions, six maintained objectives, compact vigilance, four unified receipt missions, and the Wendigo terminal hunt. Hunt global-target cleanup is owner-scoped.
- Four terminal-hunt surfaces exist and preserve the pulse-only final lock.
- The ordinary two-Pack and receipt-backed one-Pack paths use the same complete-batch capacity check before population consumption.
- Receipt epochs initialize without retroactive credit, prune inactive enemies through a bounded registry, reset on re-war, and clear on shutdown.
- The transformed original ZZZ country disables normal queue recruitment for `Wendigo Pack` before its first post-merge focus and retains only the two paid scripted muster paths.
- The staged achievement tracker has 18 permanently unavailable presentation entries, zero gameplay effects, zero costs, zero cooldowns, and zero AI blocks. Its 18 status selectors call the 18 real achievement completion triggers.
- Two Event Details world-end rows retain distinct IDs, toggles, terminal flags, and super-event mappings.
- `SCN-010` performs a mutation-free preflight for the exact selected type and intensity. It freezes actor and opening-state capacity, external Island/Siege/March state arrays, and reusable-slot arrays, requires exact manifest equality, and commits only after success. Failure changes only the launcher failure marker and clears temporary planning state.

## Asset and presentation evidence

- Runtime focus icons: 204 of 204.
- Runtime idea/modifier textures: 62 of 62.
- Runtime decision/category textures: 135 of 135, including 38 distinct unified decision icons.
- Live idea pictures: 37 of 37 registered. The eight repaired icons are unique 68x68 DDS files with independent image-generated sources.
- Regional warlord portraits: 64 warlord sprite aliases reference 56 distinct existing regional DDS textures. Exact archive recovery covers the 16 HATE packages; archive status for the remaining 40 is unknown pending the portrait audit. All 56 distinct HOI4-style finals remain unfinished; path coverage does not prove visual fitness or final acceptance.
- Achievement assets: 18 triplets, 54 DDS files.
- Closure package: 21 distinct assets with generated sources, processed finals, runtime DDS files, hashes, and contact sheets.
- Super-event action images: four distinct 457x328 DDS files.
- Revealed leader animations: the static sprites directly register the exact supplied `hannibal.dds` and `hannibal_wendigo.dds` files. One 12-frame ordinary sheet and one 16-frame transformed sheet use those exact portraits as frame `000` and separately image-generated source art for every later motion state. Both play at 12 fps with frame blending.
- Historical 2026-07-15 Event 014 texture scan across one dedicated registry plus `chaosx_pictures.gfx` and `chaosx_super_events.gfx`: 812 total references, 598 unique existing paths and 598 unique hashes. These are the frozen scan's counts, not a current scan receipt.
- Super-event audio IDs 49, 50, 52, and 53 have unique 44.1 kHz WAV files and a rights/source record. ID 51 is not used by Event 014.
- The frozen super-event runtime audio inventory is eight unique source/runtime files: four runtime WAVs plus four preserved source recordings. The downstream unit-audio amendment separately records 61 source-derived/runtime unit WAV files and its unresolved playback gates.
- Nine inactive custom irregular-infantry/cavalry subunits now have stable sprite-token consumers, locked Event 014 template mappings, localisation, and additive CXT registration. `cannibal_bone_riders` is horse-mounted and consumes real infantry equipment. The locked Scavenged Elephant Column uses installed vanilla `elephantry` with its real infantry- and artillery-equipment need. No equipment archetype was added. The 27 counter DDS/registry consumers are present. Feast Guard, Feast Cohort, Bone Guard, Siege Eaters, March Predation Column, Island Reavers, and Scavenger Warband also have parent-installed mesh, eight-action, entity/GFX, material-map, and runtime sound packages.

## Current downstream amendment

The [portrait receipt](../../../plans/014_cannibalism_plans/subagent_handoffs/2026-10-03_event014_portrait_receipt_repair.md), [exact archive recovery](../../../plans/014_cannibalism_plans/subagent_handoffs/2026-10-03_portrait_source_archive_recovery.md) and [parent review JSON](../../../plans/014_cannibalism_plans/evidence/2026-10-03_portrait_archive_parent_review.json) resolve missing worker/archive/reproducibility evidence for H01-H16. The parent accepted commit `f440c5329` only at the archive boundary: all historical original/crop/candidate hashes match, crops equal source rectangles, candidates equal installed DDS pixels, 121 archive file hashes and 62 protected runtime/definition hashes are verified. No current runtime portrait, static Hannibal file or animated sheet was changed. No claim is made that all 56 source packages or every source field are restored.

Rights remain reference-only/user-authorized. The 56 final-art requirement, visual/live acceptance, H06's opaque white field and external static Hannibal original/crop/creator/rights provenance remain unresolved. Preserve the selected direct-source branch without applying the default fictional ImageGen route as a retrospective rejection; final-production authority is separately advisory to the parent.

Feast Cohort's selected `11014` mesh and eight actions match installed bytes in [its current receipt](../../../plans/014_cannibalism_plans/evidence/2026-10-03_feast_cohort_runtime_source_receipt.json). Follow the current continuation checkpoint for changing Feast Guard export recovery and five missing model-manifest links; this patch records no new manifests or restored model source fields.

The current evidence records nine gameplay consumers, 27 counter DDS files with matching registry consumers, and seven parent-installed bespoke model/action/entity/audio packages. Bone Riders intentionally uses vanilla `sprite = cavalry`, and Network Cadre intentionally uses vanilla `sprite = infantry`; neither requires a custom model/action/entity/provider package, and their retained 3D records are historical lineage only. Island Reavers and Scavenger Warband now have source-approved Meshy/Blender export, reimport, runtime entity/GFX, material, and audio evidence in their v11 and v2 handoffs. Parent live consumer review remains open for the seven bespoke packages and the counter/audio surfaces. The four super-event audio packages are source-checked and fully registered with unique base sounds, settings-scaled wrappers, catalog rows, and guarded settings-aware dispatch; see `event014_super_event_audio_wiring_audit_2026-08-25.md`. The 2026-07-15 closure audit is historical evidence for the frozen scope and does not close these downstream items.

## Secrecy evidence

- Public Hannibal identity is written only after `cannibalism_reveal_complete` in ordinary and Wendigo transactions.
- Pre-reveal events, evolution rows, decisions, focuses, GUI, Event Details, achievement tracker rows, scenario text, reports, portraits, terminal rows, and audio presentation use neutral military, cell, network, commune, island, and Host language.
- Event Details world-end rows do not enter the dynamic list before reveal.
- The tracker does not expose late achievements before their corresponding exploitation, Island Host, Evolution II, convergence, reveal, merge, or aftermath stage.
- No actor likeness or borrowed living Indigenous ceremonial, sacred, tribal, or authenticity framing is accepted in the current package.

## Audit limitations

The evidence above is definition-level, filesystem, source-manifest and scoped audit evidence. This documentation reconciliation did not launch HOI4 or claim runtime scenario testing. The 2026-07-15 country-package, decision/mission, focus-tree, asset and documentation zero findings are historical frozen-scope results. The 2026-08-26 spreadsheet audit retained `Events!N15` and `Scenarios!F10` as `Needs Testing`; the current continuation preserves that status. `event014_final_completion_audit_2026-07-13.md` is only a historical pre-origin-removal checkpoint.

Current event/helper comparison, GUI state/resolution/hierarchy/click-region comparison, probability scenarios and user-owned live consumer acceptance remain incomplete. Current curator calls to `hoi4.event_inspect`, `hoi4.focus_inspect`, `hoi4.gui_inspect` and `hoi4.tech_inspect` returned `MCP tool hoi4_agent_tools/hoi4.<route> is not available to the model`; exposed names establish neither service health nor standalone Technology Tree Viewer availability. No source-only check substitutes for the missing MCP evidence. The [probability auditor's handoff](../../../plans/014_cannibalism_plans/subagent_handoffs/2026-10-03_event014_decision_probability_audit.md) preserves named scenario pools and unresolved eligibility/score traces; this curation makes no numeric AI or balance conclusion.

The post-remediation asset recheck found 18 exact not-eligible overlay composites with zero pixel mismatches, 54 package/live achievement triplet files with zero mismatches, 65 separate built-in ImageGen flag masters with 195 unique runtime TGAs, and 14 semantic animation packages with 142 source and 142 processed frames. The later unit/model amendment supersedes the old “zero stale claims” statement for custom-unit model, counter, source, and audio handoffs.

## Resolved first-band strategy design

The pre-lock Wendigo target-priority package is intentionally idempotent. Later calls can add newly valid targets, while an already recorded target keeps its first assigned band because the effects database provides `add_ai_strategy` without a scripted removal counterpart. The post-lock target profile is a separate one-time escalation and is not represented as a dynamic update of the pre-lock package. This fixed-assignment contract is resolved intentional design, not an open audit finding.

The current `interface/014_cannibalism.gfx` mapping has 64 warlord aliases referencing 56 distinct existing texture paths, confirmed by the curator and the parent's independent regex scan. Exact archive recovery covers the 16 HATE packages H01-H16 only; archive status for the remaining 40 regional textures is unknown pending the parent-owned portrait audit. Actual subject gender/human identity/framing, source approval and final-art acceptance remain unresolved. Neither path coverage nor the August source-gate `PASS` claim approves all 56 sources, finals or a new generation route.
