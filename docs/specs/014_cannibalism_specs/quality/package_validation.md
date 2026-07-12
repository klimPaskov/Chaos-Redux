# Package Validation

Status date: 2026-07-13

## Structural and gameplay-definition evidence

- Focus IDs are unique and exact at 72 warlord, 108 unified, and 28 Wendigo focuses.
- Every focus has its AI block, focus-specific reward helper, localisation, and unique registered icon.
- Both target scorers and both decision-weight MTTH entries exist. Exactly six unified targeted decisions consume the shared unified weight.
- All eight maintained mission IDs and seven added action IDs exist once and retain their target, cost, progress, outcome, AI, and cleanup contracts.
- Four terminal-hunt surfaces exist and preserve the pulse-only final lock.
- The ordinary two-Pack and receipt-backed one-Pack paths use the same complete-batch capacity check before population consumption.
- Receipt epochs initialize without retroactive credit, prune inactive enemies through a bounded registry, reset on re-war, and clear on shutdown.
- The transformed original ZZZ country disables normal queue recruitment for `Wendigo Pack` before its first post-merge focus and retains only the two paid scripted muster paths.
- The staged achievement tracker has 18 permanently unavailable presentation entries, zero gameplay effects, zero costs, zero cooldowns, and zero AI blocks. Its 18 status selectors call the 18 real achievement completion triggers.
- Two Event Details world-end rows retain distinct IDs, toggles, terminal flags, and super-event mappings.

## Asset and presentation evidence

- Runtime focus icons: 208 of 208.
- Regional warlord portraits: 56 of 56.
- Achievement assets: 18 triplets, 54 DDS files.
- Closure package: 21 distinct assets with generated sources, processed finals, runtime DDS files, hashes, and contact sheets.
- Super-event action images: four distinct 457x328 DDS files.
- Revealed leader animations: one 12-frame ordinary sheet and one 16-frame transformed sheet, both made from independently generated source frames.
- Event 014 texture references across nine `.gfx` files: 816 total, 598 unique paths, zero missing files.
- Super-event audio IDs 49, 50, 52, and 53 have unique 44.1 kHz OGG and WAV files and a rights/source record. ID 51 is not used by Event 014.

## Secrecy evidence

- Public Hannibal identity is written only after `cannibalism_reveal_complete` in ordinary and Wendigo transactions.
- Pre-reveal events, evolution rows, decisions, focuses, GUI, Event Details, achievement tracker rows, scenario text, reports, portraits, terminal rows, and audio presentation use neutral military, cell, network, commune, island, and Host language.
- Event Details world-end rows do not enter the dynamic list before reveal.
- The tracker does not expose late achievements before their corresponding exploitation, Island Host, Evolution II, convergence, reveal, merge, or aftermath stage.
- No ancient-general, Carthaginian, Punic, actor-likeness, living Indigenous ceremonial, sacred, tribal, or authenticity framing is accepted in the current package.

## Audit limitations

The evidence above is definition-level, filesystem, source-manifest, and audit evidence. This documentation reconciliation did not launch an in-game runtime session and does not claim runtime scenario testing. The final localisation/secrecy and asset/audio audits are completion-ready at P0/P1/P2/P3 all zero. `event014_final_completion_audit_2026-07-13.md` is completion-ready with P0/P1/P2 zero and one accepted non-blocking P3. The authoritative workbook and update helper record `Events!M15` and `Scenarios!F10` as `Implemented`.

The post-remediation asset recheck found 18 exact not-eligible overlay composites with zero pixel mismatches, 54 package/live achievement triplet files with zero mismatches, 14 animation packages with 142 source and 142 processed frames and zero contract gaps, and zero stale claims in the reconciled asset manifests.

## Accepted bounded constraint

The pre-lock Wendigo target-priority package is idempotent. Later calls can add newly valid targets, but an already recorded target is not dynamically removed or re-banded because the effects database provides `add_ai_strategy` without a scripted removal counterpart. The post-lock target profile is a separate one-time escalation and is not represented as a dynamic update of the pre-lock package.
