# Event 012 recent demand repetition audit, 2026-10-03

**R1: the replay guard currently blocks legitimate fresh contracts.**
`common\scripted_effects\012_africa_gods_repetition_effects.txt:13–16` puts ID equality and generation equality directly beside each other inside NOT.
Clausewitz NOT uses NOR, so with both receipt fields present this branch permits recording only when both comparisons are false.
A new ID in the same generation is rejected, and a reused ID in a new generation is also rejected.
Both must be allowed, while the identical ID/generation pair must be rejected.
Parent correction: put the two comparisons inside an explicit AND within NOT, or express either inequality through an OR.
No gameplay source was edited by this audit.

| Replay case, both stored fields present | Required | Current guard |
| --- | --- | --- |
| Same ID and generation | No-op | No-op |
| New ID, same generation | Record once | Incorrectly blocked |
| Same ID, new generation | Record once | Incorrectly blocked |
| New ID and generation | Record once | Allowed |

This blocks the requested fresh sequence: after the first successful record sets count 1 and its ID/generation, subsequent same-generation contracts do not advance the count.
The fourth therefore does not receive the intended existing +10 from this fresh state.
The same gate can block family/type/gap resets, even though the underlying matching predicate correctly recognizes those mismatches.
Disposition: partial source repair until R1 is corrected and the sequence cases are rechecked.

Other bounded findings:

- The sole production remember call is core effects `1801`, after active flag, contract ID/generation, family/type, amount, deadline and open status are written, and only inside successful contract creation.
  Failed quotes/capacity, payment, partial, aid and negotiation paths do not call it.
- The remember helper requires the current contract and valid family, inheriting actual membership proof and rejecting copied matching flags on a nonmember.
- Caller temporary family/type inputs are initialized before the boolean helper, with mobile type initialized before its conditional overwrite.
  Age is private trigger-local scratch, with no ROOT/PREV temporary-variable prefix or unsupported parameter API.
- Matching requires last family/day and, for family 2, present matching last subtype.
  Age zero through 365 is accepted, 366 and negative age are rejected.
  Non-mobile records clear the optional last subtype.
- The scaler no longer reads history count, so negotiation-only or aid-only history cannot independently cause the surcharge.
  Existing threshold 2 and delta 10 are unchanged.
  With the intended replay predicate, counts 0/1/2 before the first three matching creations do not surcharge, and count 3 before the fourth does.
- `repetition_window_days = 365` inherits the existing `gods_of_africa_timing` integer schema.
  The existing once-only history initializer seeds repetition count zero, and no re-entry reset or new clock/meter is introduced.

References read: installed `documentation\triggers_documentation.md:5166–5174` permits conditional triggers, and `6570–6578` defines NOT.
Installed revision is `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29` under `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV`.
Offline `paradox_wiki\Triggers - Hearts of Iron 4 Wiki.md:339–341` explicitly distinguishes AND from NOT/NOR.
The same rule is in `.agents\skills\chaos-redux-events\SKILL.md:647`.
Offline Data structures `435–442` documents trigger-local and unscoped temporaries, revision `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`.

| Source reviewed | SHA-256 |
| --- | --- |
| Repetition effects | `4743a54f62d999586f6f5ee09af35ae13d92dfb01e53b263747dcaad4ee4b58a` |
| Repetition triggers | `a370f6a389708969e2a5bcaa18798ae1351abc47f9aa382bc9a02ccff84b0fe0` |
| Core effects | `6e0989bb465df9ec9df68af1974fc4ea681b5c35c8060680231173163f5c7aa6` |
| Constants | `b3473262a3c9bfce17218773ffea5a1bc5063336bea9b82da7b9a2511bed21f4` |

Acceptance basis is the parent's explicit repair of the accepted recent-repetition requirement, with existing tuning retained.
Only this new handoff was written, with no gameplay/docs elsewhere/skill/Git/index/commit or engine operation.
No new MCP request or wait was made, and native execution remains unconfirmed.
Parent next action is R1 correction, final boundary/sequence review, documentation and its scoped commit.
No full-goal, numeric AI or native acceptance claim is made.

## Narrow R1 resolution

**R1 is resolved in source.**
The current helper at `012_africa_gods_repetition_effects.txt:13–18` explicitly nests the two identity equalities in AND inside NOT.
The missing-field OR branches remain unchanged.
This supersedes the original outstanding finding and partial source disposition.

The four present-field identity cases now match the contract: identical ID/generation is a no-op, while new ID only, new generation only, or both new permit one record.
Thus generation-owned ID reuse, including a fresh generation's ID 1, is not mistaken for replay.
After recording, both markers are stamped, so replay cannot change count, family, optional subtype or day, including after a reset.

A narrow read-only Boolean/sequence sanity model checked fresh same-type commits at days 0/90/180/270.
Counts become 1/2/3/4 and the corresponding pre-commit deltas are 0/0/0/10.
Every repeated same-contract call in that sequence leaves the receipt unchanged.
A fresh changed subtype resets count to 1, age 365 still matches, and a fresh contract after a 366-day gap resets to 1.
These are source/formula checks, not executed engine scenarios or numeric AI evidence.

Current repetition-effects SHA-256: `12a8bb95b2d0a4c57bcf138caf5ddb0bbd4d3f490faf72882c0c2dafc94be357`.
The repetition trigger, core placement and constants hashes remain the previously recorded `a370f6a389708969e2a5bcaa18798ae1351abc47f9aa382bc9a02ccff84b0fe0`, `6e0989bb465df9ec9df68af1974fc4ea681b5c35c8060680231173163f5c7aa6`, and `b3473262a3c9bfce17218773ffea5a1bc5063336bea9b82da7b9a2511bed21f4`.
Final bounded disposition: reviewed source fix with no remaining finding from this audit, native execution unconfirmed, and no wider goal-completion claim.
Only this handoff was appended, with no gameplay, skill, Git/index/commit, MCP request or engine operation.
The existing events skill already covers the NOR rule, so no skill update was required or performed.
