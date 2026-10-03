# Country Package Matrix

Design and implementation are separate: the current parent instruction preserves eight reusable slots, three origins and 56 distinct regional HOI4-style finals as accepted and unfinished. The [2026-10-03 continuation report](../../../plans/014_cannibalism_plans/2026-10-03_continuation_report.md) and [resume packet](../../../plans/014_cannibalism_plans/resume_packet.md) bound current implementation evidence. Seven bespoke model packages, nine gameplay families, approved Bone Riders cavalry/Network Cadre infantry visual reuse, vanilla `elephantry` and no animation toggle remain unchanged.

| Package | Spawn basis | Starting problem | Military identity | Economy | Political routes | AI identity | Final ambition |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Island Host, any free CBA-CBH slot | Silent island or isolated coast | Blockade and weak repair | Reavers, port garrison, landing parties | Convoy raids and island Larders | Tyrant, council, confederacy, network | Naval raider | Archipelago domination or unification host |
| Siege Commune, any free CBA-CBH slot | Besieged city or fortress | Encirclement and bombardment | Urban assault, tunnels, captured police | Dense feeding districts and workshops | Tyrant, council, network | Defensive and relief-route hunter | Break siege and expand urban state |
| March Host, any free CBA-CBH slot | Defecting frontline formations | Low civilian base and constant hunger | Mobile warbands, trucks, cavalry | Depot seizure and mobile Larder | Tyrant, confederacy, defiance | Aggressive mobile conqueror | Continental Host or unification host |
| Unified Hannibal, CBL | Evolution III host | Warlord integration and world hostility | Legions, Bone Guard, three origin specialists | Continental Larder and captured industry | Central, confederated, ritual state | Shared scored targets, absorption, infiltration | Ordinary world end |
| Wendigo Hannibal, original ZZZ in place | Valid Wendigo merge | Protect transformation anchors and preserve countdown Larder | Existing ZZZ forces, paid-only Pack musters, inherited units | Supernatural hunger and Larder | 28-focus transformation overlay | Scored pre-lock targets, terminal hunt, separate post-lock conquest | Strongest terminal world end |

## Required files per package

Every package needs:

- tag or transformation identity
- country definition and history
- names and adjectives
- party and ideology localisation
- leader and portrait
- flags in all sizes
- starting ideas
- focus tree assignment
- decisions and missions
- starting units and templates
- equipment and manpower logic
- commander roster
- AI strategy
- shared special-country classification
- actual-nonhuman classification when valid
- event log actor mapping
- asset manifest entries
- defeat and cleanup logic

The 2026-07-15 country-package zero audit is historical frozen-tranche evidence, not current full-package proof. The design requires seven regional portrait/name variants per origin-agnostic slot, for 56 distinct final portraits. The current 64 warlord sprite aliases reference 56 distinct existing regional DDS textures, which does not prove final-art acceptance. Archive recovery covers the 16 HATE subset packages; archive status for the remaining 40 is unknown pending the portrait audit. The [worker receipt](../../../plans/014_cannibalism_plans/subagent_handoffs/2026-10-03_event014_portrait_receipt_repair.md), [archive recovery](../../../plans/014_cannibalism_plans/subagent_handoffs/2026-10-03_portrait_source_archive_recovery.md) and [parent review](../../../plans/014_cannibalism_plans/evidence/2026-10-03_portrait_archive_parent_review.json) resolve original/crop/candidate and reproducibility evidence for those 16 HATE subset packages only, accepted at the archive boundary in `f440c5329`. Rights, final-art, visual/live acceptance and protected static Hannibal external provenance remain open. Constituent technology union and original-ZZZ Pack recruitment behavior retain their prior definition-level evidence; this curation supplies no new engine validation.

Current event/helper comparison, technology coverage, attributable GUI acceptance and probability scenarios remain incomplete. The curator's matching event/focus/GUI/technology read-only routes returned `not available to the model`; source evidence is not equivalent MCP proof. Preserve the [probability specialist's scenario-specific handoff](../../../plans/014_cannibalism_plans/subagent_handoffs/2026-10-03_event014_decision_probability_audit.md). Follow the continuation checkpoint for changing model export/manifest recovery; this matrix asserts no newly restored model source fields or manifests.

The current `interface/014_cannibalism.gfx` mapping has 64 warlord aliases referencing 56 distinct existing texture paths, confirmed by the curator and the parent's independent regex scan. Exact archive recovery covers the 16 HATE packages H01-H16 only; archive status for the remaining 40 regional textures is unknown pending the parent-owned portrait audit. Actual subject gender/human identity/framing, source approval and final-art acceptance remain unresolved. Neither path coverage nor the August source-gate `PASS` claim approves all 56 sources, finals or a new generation route.
