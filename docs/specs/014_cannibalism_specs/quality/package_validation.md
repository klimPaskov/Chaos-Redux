# Package Validation

Status date: 2026-07-15

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
- Live idea pictures: 37 of 37 registered; the eight repaired icons are unique 68x68 DDS files with independent image-generated sources.
- Regional warlord portraits: 56 of 56.
- Achievement assets: 18 triplets, 54 DDS files.
- Closure package: 21 distinct assets with generated sources, processed finals, runtime DDS files, hashes, and contact sheets.
- Super-event action images: four distinct 457x328 DDS files.
- Revealed leader animations: one 12-frame ordinary sheet and one 16-frame transformed sheet, both made from independently generated source frames.
- Event 014 texture references across nine `.gfx` files: 812 total, 598 unique paths, zero missing files.
- Super-event audio IDs 49, 50, 52, and 53 have unique 44.1 kHz OGG and WAV files and a rights/source record. ID 51 is not used by Event 014.
- The runtime audio inventory is eight files: four OGG and four WAV.
- No custom subunit or equipment identifiers were added. Existing battalion and equipment surfaces remain in use, so no bespoke unit-counter or equipment art is required. This is a verified scope disposition, not a fallback.

## Secrecy evidence

- Public Hannibal identity is written only after `cannibalism_reveal_complete` in ordinary and Wendigo transactions.
- Pre-reveal events, evolution rows, decisions, focuses, GUI, Event Details, achievement tracker rows, scenario text, reports, portraits, terminal rows, and audio presentation use neutral military, cell, network, commune, island, and Host language.
- Event Details world-end rows do not enter the dynamic list before reveal.
- The tracker does not expose late achievements before their corresponding exploitation, Island Host, Evolution II, convergence, reveal, merge, or aftermath stage.
- No actor likeness or borrowed living Indigenous ceremonial, sacred, tribal, or authenticity framing is accepted in the current package.

## Audit limitations

The evidence above is definition-level, filesystem, source-manifest, and audit evidence. This documentation reconciliation did not launch an in-game runtime session and does not claim runtime scenario testing. The current 2026-07-15 country-package, decision/mission, focus-tree, asset, and documentation evidence reports P0/P1/P2/P3 all zero. The authoritative workbook and update helper record `Events!M15` and `Scenarios!F10` as `Fully Functional`. `event014_final_completion_audit_2026-07-13.md` is preserved only as a historical pre-origin-removal checkpoint.

The post-remediation asset recheck found 18 exact not-eligible overlay composites with zero pixel mismatches, 54 package/live achievement triplet files with zero mismatches, 14 animation packages with 142 source and 142 processed frames and zero contract gaps, and zero stale claims in the reconciled asset manifests.

## Resolved first-band strategy design

The pre-lock Wendigo target-priority package is intentionally idempotent. Later calls can add newly valid targets, while an already recorded target keeps its first assigned band because the effects database provides `add_ai_strategy` without a scripted removal counterpart. The post-lock target profile is a separate one-time escalation and is not represented as a dynamic update of the pre-lock package. This fixed-assignment contract is resolved intentional design, not an open audit finding.
