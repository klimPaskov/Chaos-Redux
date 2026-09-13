# Doctrine track-index parser repair

Disposition: implemented syntax repair; native full-file retest and exact-track gameplay validation pending.

The installed documentation and offline Effects wiki describe `add_mastery.index`, but launches 08–10 reject that child in every existing exact-mastery branch.
The installed binary contains the alternate `track_index` token.
Launch 09 tested that token in an unreferenced helper with amount zero; the engine rejected the amount, making that test inconclusive.
Launch 10 repeated the unreferenced helper with amount one and the same folder, subdoctrine, track, and ordinal zero.
No probe-specific error, unknown `track_index`, or amount error appeared in the completed fresh parser passes.
Both disposable helpers were archived and removed without execution.

The parent changed only the 107 `index` child names to `track_index` inside the 107 existing `add_mastery` blocks in `common/scripted_effects/027_doctrine_research_exact_mastery_effects.txt`.
All amounts, folders, track types, subdoctrines, ordinal values, loops, readbacks, and fail-closed conditions remain byte-identical.
The ordinal inventory remains 30 zeroes, 32 ones, 21 twos, and 24 threes.
Exact reversal of the 107 names reconstructs the complete immediate original.
The original and hash manifest are under `pre_patch_mastery_track_index/` and `doctrine_track_index_repair.json`.

This uses the spelling accepted by the installed parser; it does not omit the ordinal or broaden the intended target set.
Acceptance of one unreferenced parser fixture does not prove that the native effect awards mastery exclusively to that ordinal.
The next launch must test all production branches for parser errors.
Live validation must then cover indices zero through three, both Special Forces tracks, unchanged non-selected tracks, banked mastery, one-level completion, and transaction readback.
Any unexpected broad application remains a blocker; no index-free fallback is accepted.

The earlier read-only `doctrine_mastery_index_analysis.md` remains historical evidence for the documented syntax failure.
Its claim that the alternate spelling has no parser evidence is superseded by launch 10, while its exact-target runtime limitation remains unresolved.
Its recorded technology inspection/render evidence is partial and does not certify this effect-field repair.

The post-patch technology comparison requested the recorded baseline revision `90e33d754169693e59b0484cbf76dcd86b6a2dc22d3004ac3ef370c8899fe177` against current sources.
It returned `TECH_REVISION_NOT_CACHED` with the explicit blocker "Requested technology revision is not cached".
No technology-graph equivalence or effect semantics are inferred from that failed comparison.
