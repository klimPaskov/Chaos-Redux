# Event 028 resolver reentry guards

Disposition: bounded source correction implemented; mandatory artifact-backed event comparison and native reentry observation remain blocked/open.
Acceptance basis: the full package requires fire-once, once-per-state processing, persistent outcomes and exploit-safe cleanup.
The [physical integration proposal](subagent_handoffs/physical_receipts_20261003.md) identified the duplicate-callback failure branch independently of the still-open planning/capital gates.

## Correction

The impact branch of `chaosx.nr28.4` rejects an already started, impact-recorded, resolved, miss-recorded or fail-closed transaction.
The failure branch also rejects all five cases.
A duplicate callback therefore cannot replace an earlier impact outcome/history payload with fail-closed or reissue news and cleanup.
The fresh valid transaction still enters the existing impact branch.
An unstarted invalid locked transaction still uses the existing explicit fail-closed outcome; its accepted invalid-state policy is not widened by this patch.
No target, population, cost, AI weight, timeframe or new fallback is introduced.

## Actual-source guard cases

The source fixture parses the actual before Git blob and actual after event file, locating the real impact/failure `limit` bodies.
Sixteen named cases cross a declared valid/invalid result from the existing locked-transaction validator with eight flag sets: FRESH, STARTED, IMPACT, RESOLVED, MISS, FAILED, ALL and UNRELATED.
The before source reproduces failure-branch selection for a started callback and an invalid already-recorded/resolved impact, plus impact-branch selection for recorded/resolved/miss/failed flags when the declared locked validator is true.
The corrected guards select no branch for all those prior-outcome cases.
Fresh and unrelated-only flag sets preserve the original valid-impact/invalid-failure selection.
All sixteen cases passed.

Before blob SHA-256: `e9c436b8d1393f354bf5be6235ccc2fb4205e0413309eaad7daf60267f9ba943`.
After physical event-file SHA-256: `3d1f01d678b0de75c2fe087d1b7042aa230f606890938ed1ee67d6e648c5c048`.
This is guard-only execution under declared validator results; the locked validator and branch effect bodies are not executed by the fixture.
Unknown guard predicates fail the fixture rather than becoming successful effect stubs.
No native timing, physical damage, helper lifecycle or country-state proof is claimed.

## Required MCP evidence and exact blocker

The matching pre-change `.4` trace is the fresh focused result at revision `f0e16475c8407b53ed214cb41838952142f1cd8c62e083191f7d8916d82ac506`, with helper expansion disabled and deferred helper/lifecycle coverage.
Its artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e1b4b50cbaa488d39deea5bc1326515fc059fa6bc6a4c4153df8cba5f170f1e9/c290c6dda3669299e369bcfa0d18bc3ca98ddccc3349dbd593e22a55834397b9/event-trace-f0e16475c840.json`.
The parent invoked `hoi4.event_compare` with that `before.artifactUri`, the exact `.4` selector, bounds of four chain/render nodes and rendering disabled.
The initial string-reference request was rejected for its shape and corrected to the required object; that mistake is not classified as a missing route.
The corrected request returned `ARTIFACT_NOT_FOUND`, blocker message `Artifact provenance manifest is unavailable`, no artifacts, and validation false.
The same provenance-manifest failure was independently reproduced by the probability, presentation and map workers, including narrowly bounded artifact reads.
The route is exposed and callable; its required before-artifact delivery is blocked.
Source-only guard results are not equivalent event comparison or native evidence.

The late no-backup capital policy, pre-physical aligned planning proof, journal-owned rollback, successful-receipt publication order, graphical-only effects and provincial/railway/queue surfaces remain open.
This correction must not be used to claim that the full resolver transaction is complete.
