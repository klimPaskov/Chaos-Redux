# Event 012 ordinary membership authority audit, 2026-10-03

**Verdict: U1's weak ordinary-relation predicate is resolved in source, with no defect found in this bounded change.**
Acceptance basis is the parent's explicit membership-proof repair following victor tranche `49b8a77`.
Only this handoff was written, with no gameplay, other docs, skill, Git/index/commit, MCP query or HOI4 launch.

`common\scripted_triggers\012_africa_gods_triggers.txt:163–179` now requires a real committed current host and actual `gods_of_africa_participants` membership through the host scope's PREV, alongside the existing live-country, participant flag, generation equality and non-exemption checks.
Matching copied/stale participant flags and generation without host-array membership therefore fail.
The registered alias at `195–197` delegates to that same proof and introduces no duplicate scope change.

Registration at `common\scripted_effects\012_africa_gods_effects.txt:310–363` uses its independent enrollment predicate.
History initialization at lifecycle effects `4–35` does not require the current-relation predicate.
The host array append at core effects `355–358` precedes participant floor refresh and `.602`, so genuine entry is not blocked by its own missing pre-enrollment membership.

Manual entry-gate traces and a read-only helper-dependency check confirmed that ordinary demand creation, current/expiry contracts, full/partial/substitute capacity, defiance/reconciliation, protection and voluntary aid inherit the strengthened proof.
Wrath/history mutations, offender marking, leniency and raw punishment guards use it directly or through those gates.
This covers the ordinary relation gateways, without claiming that private cleanup/implementation helpers require live authority.

Ordinary demand cleanup at core effects `2244` removes neither live membership nor the participant flag, preserving `.604` eligibility after successful contract cleanup.
Defiance also retains membership.
Archive/clean-participant remove membership and the participant flag, while finalization/cancellation clear participant authority and the owner later clears its roster.

`.608` uses its frozen settlement-host/standing/pending proof, and `.615` plus the victor branch of `.612` use recipient-owned episode receipts.
None requires the ordinary current predicate, so emptying the live roster does not invalidate those otherwise valid historical receipts.
Victory capture still uses actual FROM membership before cleanup.
The added current-host predicate checks existence/commit flags/generation, not host capitulation, so it does not reject the defeated host merely for being capitulated at the authorized capture boundary.

Source revision reviewed:

| File | SHA-256 |
| --- | --- |
| Core triggers | `8abaf42a84646715583f705b31150b786b6050cc4e428c36c91126c88deae28d` |
| Core effects | `ea62d37f38e9c3f19c1c9be6e6a483281f7358d93998028176b87c6349096a2f` |
| Settlement receipt triggers | `f56c45b8813807be97f69f72af3ea05e97cbffc7529febd4a19c8856f3dfd4d1` |
| Victor receipt triggers | `b52e6183b2a27ac71109d6a3b16a374fd2d3de9ce05598a490a10de31d562d91` |

Disposition: implemented and source-reviewed U1 repair.
Country-object copying, ID reuse, actual array/queued-event persistence and existing MCP/native acceptance remain unconfirmed.
This does not establish engine inheritance behavior, close U3, or claim full Gods completion.
Parent next action is documentation alignment and its scoped commit with these limits retained.
Skills applied: events, subagents, event planning, improvement loop and relevant decision lifecycle guidance already read in this audit session.
No skill was changed and no simplification was introduced.
