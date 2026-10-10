# Package Validation

Status date: 2026-10-10 spec audit; no full-package validation claim.

Authority, current implementation scope, provenance and open gates are recorded once in [package status](package_status.md).
This file lists definition-level, filesystem and secrecy evidence; all July zero audits and aggregate inventory or structural results below remain historical frozen-tranche evidence.

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
- Runtime decision/category textures: 138, including the 41 unified decision and mission icons (the three hidden-hoard icons were added on 2026-10-04).
- Live idea pictures: 37 of 37 registered. The eight repaired icons are unique 68x68 DDS files with independent image-generated sources.
- Regional warlord portraits: all 56 native fictional candidates are produced, regionally parent-approved and installed, eight per region. Every runtime DDS equals its selected candidate bytes, including South America CBD v02, and the unchanged 64 aliases resolve to the same 56 paths. Parent regional receipts record 156x210 opaque BGRA32 single-level DDS and exact PNG/DDS pixels. Distinct file/pixel hashes do not prove global face/composition distinctness; the independent visual audit is accepted and live acceptance remains pending.
- Achievement assets: 18 triplets, 54 DDS files.
- Closure package: 21 distinct assets with generated sources, processed finals, runtime DDS files, hashes, and contact sheets.
- Super-event action images: four distinct 457x328 DDS files.
- Revealed leader animations: the static sprites directly register the exact supplied `hannibal.dds` and `hannibal_wendigo.dds` files. One 12-frame ordinary sheet and one 16-frame transformed sheet use those exact portraits as frame `000` and separately image-generated source art for every later motion state. Both play at 12 fps with frame blending.
- Historical 2026-07-15 Event 014 texture scan across one dedicated registry plus `chaosx_pictures.gfx` and `chaosx_super_events.gfx`: 812 total references, 598 unique existing paths and 598 unique hashes. These are the frozen scan's counts, not a current scan receipt.
- Super-event audio IDs 49, 50, 52, and 53 have unique 44.1 kHz WAV files and a rights/source record. ID 51 is not used by Event 014.
- The frozen super-event runtime audio inventory is eight unique source/runtime files: four runtime WAVs plus four preserved source recordings. The downstream unit-audio amendment separately records 61 source-derived/runtime unit WAV files and its unresolved playback gates.
- Nine inactive custom irregular-infantry/cavalry subunits now have stable sprite-token consumers, locked Event 014 template mappings, localisation, and additive CXT registration. `cannibal_bone_riders` is horse-mounted and consumes real infantry equipment. The locked Scavenged Elephant Column uses installed vanilla `elephantry` with its real infantry- and artillery-equipment need. No equipment archetype was added. The 27 counter DDS/registry consumers are present. Feast Guard, Feast Cohort, Bone Guard, Siege Eaters, March Predation Column, Island Reavers, and Scavenger Warband also have parent-installed mesh, eight-action, entity/GFX, material-map, and runtime sound packages.

## Secrecy evidence

- Public Hannibal identity is written only after `cannibalism_reveal_complete` in ordinary and Wendigo transactions.
- Pre-reveal events, evolution rows, decisions, focuses, GUI, Event Details, achievement tracker rows, scenario text, reports, portraits, terminal rows, and audio presentation use neutral military, cell, network, commune, island, and Host language.
- Event Details world-end rows do not enter the dynamic list before reveal.
- The tracker does not expose late achievements before their corresponding exploitation, Island Host, Evolution II, convergence, reveal, merge, or aftermath stage.
- No actor likeness or borrowed living Indigenous ceremonial, sacred, tribal, or authenticity framing is accepted in the current package.

## Audit limitations

The evidence above is definition-level, filesystem, source-manifest and scoped audit evidence. This documentation reconciliation did not launch HOI4 or claim runtime scenario testing. The 2026-07-15 country-package, decision/mission, focus-tree, asset and documentation zero findings are historical frozen-scope results. The 2026-08-26 spreadsheet audit retained `Events!M15` and `Scenarios!F10` as `Needs Testing`; the current continuation preserves that status. `event014_final_completion_audit_2026-07-13.md` is only a historical pre-origin-removal checkpoint.

Current event/helper comparison, GUI state/resolution/hierarchy/click-region comparison, probability scenarios and user-owned live consumer acceptance remain incomplete, including the parent's narrower 600-second retry gaps. Earlier curator calls returned unavailable-route errors; these historical responses and exposed route names do not establish current service health or standalone Technology Tree Viewer availability. Preserve the [probability auditor's handoff](../../../plans/014_cannibalism_plans/subagent_handoffs/2026-10-03_event014_decision_probability_audit.md), named scenario pools and unresolved eligibility/score traces. No numeric AI or balance conclusion, live `error.log` acceptance or full sign-off is supplied by this curation.

The post-remediation asset recheck found 18 exact not-eligible overlay composites with zero pixel mismatches, 54 package/live achievement triplet files with zero mismatches, 65 separate built-in ImageGen flag masters with 195 unique runtime TGAs, and 14 semantic animation packages with 142 source and 142 processed frames. The later unit/model amendment supersedes the old “zero stale claims” statement for custom-unit model, counter, source, and audio handoffs.

## Resolved first-band strategy design

The fixed first-assignment pre-lock Wendigo target package is resolved intentional design; Part 9, Resolved pre-lock first-band strategy behavior, is its authoritative description.
