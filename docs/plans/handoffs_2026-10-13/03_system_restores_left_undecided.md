# Handoff 3: gameplay system restores that were left undecided or incomplete

Read `00_common_rules.md` in this folder first.

## Current follow-up direction

The original handoff below has been executed.
The owner subsequently required useful recent content to remain, adapted for depth and dynamic behavior without bloat.
That instruction supersedes blanket replacement with earlier source for this handoff.
Use the current preservation review in `docs/plans/systems_restore_audit_2026-10-13.md` as the outcome and acceptance record, and retain the original tasks below as historical context.
Do not rerun the old blanket rollback against those adapted systems.

## Why

The systems audit (`docs/plans/systems_restore_audit_2026-10-13.md`) restored nothing and left judgement calls. Three plan items were reported incomplete. The owner has now said: "I want everything now restored, fixed and everything that was included in the plan."

## Tasks

1. **Systems audit judgement calls: restore them.**
   - The four French and Belgian camp actions hidden by `72aa7ba56` and deleted by `1850d88c3`: restore from the parent sources the audit identified.
   - Cluster probabilities changed by `4c1513475`: restore the earlier values.
   - Sanctions changed by `fa1322b37`: restore the earlier behaviour.
   - Final Silence's manual scenario changed by `3b5312c87`: restore.
   - Every other entry under "needs the owner's decision" in that audit: restore the earlier state, unless it contradicts an explicit item in `chaos_redux_restore_plan_2026-10-12.md`. Where two coupled systems cannot both be restored, restore the older one and adapt the newer one to it, and record how.
2. **C7, super-event audio.** The owner: "A super event audio should be canceled as soon as next super event fires. Only one super event audio at a time can be heard." The last job found that `99f0b18dd` removed the earlier music route and that sound effects cannot be cancelled. Restore the music-based route from `99f0b18dd^` for super events (music can be replaced by starting another track), make each new super event stop or replace the previous one, and keep the nine original recordings restored in `10292700c`. Verify in the Linux game by firing two super events back to back.
3. **C6, non-human countries.** The owner: "nonhuman countries can't at any circumstances be affected by systems targeted usually at humans, this is absurd and stupid." Guards were added in `b3946629c` and `22802baa3`, but native attacker penalties and delayed sanction cleanup still leak. Close every remaining path listed in `chaos_redux_c6_nonhuman_2026-10-13.md` so the immunity is absolute.
4. **Migration and famine depth (C11 follow-up).** `migration_famine_history_2026-10-13.md` says demographic selectors and machinery recovery could not be restored because no implementation was found in history. Search wider before accepting that: other branches, stashes, `git log --all`, `git fsck --lost-found` dangling commits, the docs and specs for those systems, and the Workshop release of the mod if a copy exists under `C:/Program Files (x86)/Steam/steamapps/workshop/content/394360/`. If an implementation exists anywhere, restore it. If only a spec exists, implement it from the spec and say so.
5. **Outbreak response actions (C12, A12 follow-up).** The owner: "I remember the biowarfare containment system that you could just contain with like by deploying field hospitals, etc. there should be many actions and decisions, but then again not bloated, thats how it was a year ago." Confirm against `biowarfare_restore_comparison_2026-10-12.md` that every action of the year-old flow is back (field hospitals, quarantine, and the rest), each as one decision visible on the map, and that no step added since then remains in the player's way.
6. **Event bonuses (C9).** The last job found no duplicate idea stack. The owner saw duplicates in play: "duplicate ideas are granted". Search for ideas added by more than one path (`add_ideas`, `add_timed_idea`, `swap_ideas`, startup and on_action grants) without a `has_idea` guard, and fix.
7. **Chemical warfare systems.** Compare the current chemical deployment, contamination, cylinder and projector flow with its state at commit `4337957b1f` (19 September) and at about one year ago. Restore any step, decision or mechanic that was removed, and remove steps that were added in the player's way, the same way the biowarfare flow was handled.

## Deliverable

Update `systems_restore_audit_2026-10-13.md` with the action taken per entry and your commits.
