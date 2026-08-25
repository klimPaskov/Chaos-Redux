# Package Validation

Status date: 2026-08-25 parent runtime-wiring amendment to the 2026-07-15 frozen closure

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
- Regional warlord portraits: 56 of 56.
- Achievement assets: 18 triplets, 54 DDS files.
- Closure package: 21 distinct assets with generated sources, processed finals, runtime DDS files, hashes, and contact sheets.
- Super-event action images: four distinct 457x328 DDS files.
- Revealed leader animations: the static sprites directly register the exact supplied `hannibal.dds` and `hannibal_wendigo.dds` files. One 12-frame ordinary sheet and one 16-frame transformed sheet use those exact portraits as frame `000` and separately image-generated source art for every later motion state. Both play at 12 fps with frame blending.
- Event 014 texture references across exactly three GFX files, one dedicated registry plus `chaosx_pictures.gfx` and `chaosx_super_events.gfx`: 812 total references, 598 unique existing paths, and 598 unique hashes.
- Super-event audio IDs 49, 50, 52, and 53 have unique 44.1 kHz WAV files and a rights/source record. ID 51 is not used by Event 014.
- The runtime audio inventory is eight files: four WAV.
- Nine inactive custom irregular-infantry/cavalry subunits now have stable sprite-token consumers, locked Event 014 template mappings, localisation, and additive CXT registration. `cannibal_bone_riders` is horse-mounted and consumes real infantry equipment. The locked Scavenged Elephant Column uses installed vanilla `elephantry` with its real infantry- and artillery-equipment need. No equipment archetype was added. The 27 counter DDS/registry consumers are present. Feast Guard, Feast Cohort, Bone Guard, Siege Eaters, and March Predation Column also have parent-installed mesh, eight-action, entity/GFX, material-map, and seven-role 44.1 kHz runtime sound packages.

## Current downstream amendment

The current evidence records nine gameplay consumers, 27 counter DDS files with matching registry consumers, five parent-installed model/action/entity/audio packages, and four remaining model families with explicit blockers: Bone Riders has no supported compound horse/rider action route, Island Reavers is stopped by Meshy HTTP 402 before accepted v8 generation, Scavenger Warband needs the remaining user-review/source gate, and Network Cadre has no accepted provider-sourced action lease. The five installed packages contain 35 converted 44.1 kHz WAV files. The four super-event audio packages are source-checked and fully registered with unique base sounds, settings-scaled wrappers, catalog rows, and guarded settings-aware dispatch; see `event014_super_event_audio_wiring_audit_2026-08-25.md`. The 2026-07-15 closure audit is historical evidence for the frozen scope and does not close these downstream items.

## Secrecy evidence

- Public Hannibal identity is written only after `cannibalism_reveal_complete` in ordinary and Wendigo transactions.
- Pre-reveal events, evolution rows, decisions, focuses, GUI, Event Details, achievement tracker rows, scenario text, reports, portraits, terminal rows, and audio presentation use neutral military, cell, network, commune, island, and Host language.
- Event Details world-end rows do not enter the dynamic list before reveal.
- The tracker does not expose late achievements before their corresponding exploitation, Island Host, Evolution II, convergence, reveal, merge, or aftermath stage.
- No actor likeness or borrowed living Indigenous ceremonial, sacred, tribal, or authenticity framing is accepted in the current package.

## Audit limitations

The evidence above is definition-level, filesystem, source-manifest, and audit evidence. This documentation reconciliation did not launch an in-game runtime session and does not claim runtime scenario testing. The current 2026-07-15 country-package, decision/mission, focus-tree, asset, and documentation evidence reports P0/P1/P2/P3 all zero for its frozen scope. The authoritative workbook and update helper record `Events!N15` and `Scenarios!F10` as `Fully Functional`; this documentation audit does not alter or re-audit the workbook. `event014_final_completion_audit_2026-07-13.md` is preserved only as a historical pre-origin-removal checkpoint.

The post-remediation asset recheck found 18 exact not-eligible overlay composites with zero pixel mismatches, 54 package/live achievement triplet files with zero mismatches, 65 separate built-in ImageGen flag masters with 195 unique runtime TGAs, and 14 semantic animation packages with 142 source and 142 processed frames. The later unit/model amendment supersedes the old “zero stale claims” statement for custom-unit model, counter, source, and audio handoffs.

## Resolved first-band strategy design

The pre-lock Wendigo target-priority package is intentionally idempotent. Later calls can add newly valid targets, while an already recorded target keeps its first assigned band because the effects database provides `add_ai_strategy` without a scripted removal counterpart. The post-lock target profile is a separate one-time escalation and is not represented as a dynamic update of the pre-lock package. This fixed-assignment contract is resolved intentional design, not an open audit finding.
