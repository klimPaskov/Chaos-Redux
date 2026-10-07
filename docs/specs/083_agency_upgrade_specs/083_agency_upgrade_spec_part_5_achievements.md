# Agency Upgrade: achievement pursuits

The following two pursuits are additions to the expanded design. They reward using the agency after the event rather than receiving a favorable roll. Both are visible through the existing achievement system. Their role labels are working labels, not final localisation.

## A1: establishing an independent service

**Working key:** `chaosx_083_independent_service`.

**Title direction:** Emphasize a small country's transition from depending on others for intelligence to carrying out consequential work of its own. Avoid presenting the automatic creation of an agency as the achievement.

**Description direction:** State the required starting situation, two different major targets, qualifying operations, and the 360-day limit precisely. The final description must distinguish a completed operation from merely placing an operative abroad.

**Eligibility:** At the first non-debug Event 83 firing received by that player-controlled country, it is independent, is not a major, and has no intelligence agency immediately before the award. This first qualifying firing opens one 360-day attempt for that country's campaign lineage.

**Unlock conditions:** Within that window, successfully complete qualifying native intelligence operations against two different independent major countries. Each operation must include at least one operative supplied and recruited through Event 83. At least one of the two targets must be at war with the player when the qualifying operation begins and when it completes. The player must remain independent through both completions.

**Target and operation rules:** A target may not be a subject of the player or a member of the player's faction at either operation start or completion. It must be an independent major at both points. Qualifying operations are native operations whose recorded successful completion delivers an intelligence, infiltration, sabotage, or comparable hostile-operation outcome against that target. Ordinary ongoing operative missions, cancelled operations, failed operations, rescue-only operations, and debug-created completions do not count. Resolve the exact supported operation identifiers against the installed definitions before implementation.

**Disqualifiers:** Becoming a subject, switching the tracked country lineage, using debug or manual test rewards for credit, or missing the 360-day deadline ends the attempt. Becoming a major through normal play does not disqualify the player after eligibility was established. A later Event 83 firing does not restart this attempt. Normal operative losses do not permanently disqualify it if the player can still meet the conditions with surviving or later Event 83 recruits.

**Difficulty:** Hard. A new minor agency must create useful operations against real major powers while preserving political independence. The target diversity, hostile-war condition, normal material costs, and deadline prevent passive receipt from earning it.

**Tracking:** Freeze the initial eligibility result and start date. Track two distinct target country lineages and confirmed operation-completion records, with participant provenance captured when each operation starts. Recheck target relations and successful completion at the end. An operation started before the attempt opens does not count. Record eligibility and disqualification through the shared achievement system.

**Icon direction:** A small, distinct signal source reaching two larger guarded emblems. Use an economical composition rather than national flags or tiny lettering.

## A2: sustained reach under pressure

**Working key:** `chaosx_083_sustained_reach`.

**Title direction:** Express the difficulty of maintaining foreign reach while protecting the institution at home. Avoid glorifying indiscriminate surveillance or implying that the world has become fully transparent.

**Description direction:** Specify the Evolution III window, two major targets, 50-strength networks, 30 uninterrupted days, home protection, and one successful operation. The final wording must make simultaneous maintenance clear.

**Eligibility:** Any player-controlled country receiving a non-debug Intelligence States package. That firing opens a 180-day attempt. A later genuine Intelligence States firing can open a fresh attempt, but does not extend the deadline or copy completed progress from an earlier attempt.

**Unlock conditions:** During one attempt, maintain a native intelligence network of at least 50 strength against each of two different independent major countries for 30 consecutive days. Throughout those same 30 days, keep at least one eligible operative actively assigned to native counter-intelligence at home. At least one Event 83 recruit must be contributing to each qualifying foreign network and at least one Event 83 recruit must be the home operative. Also successfully complete one qualifying hostile native operation against either qualifying target during the same 180-day attempt, with an Event 83 recruit among its participants.

**Target and operation rules:** Both targets remain independent majors outside the player's faction and are not the player's subjects throughout the qualifying 30-day interval. Measure the native target-network value used by operations, not the sum of unrelated regional values. Use the same non-rescue successful-operation classification as A1. A qualifying operation must begin after the attempt opens and finish before its deadline.

**Reset and failure:** A network below 50, a home operative leaving counter-intelligence, loss of the required participating provenance, or either target becoming invalid resets the uninterrupted-day counter. The attempt can still succeed before its deadline. Completed foreign-operation credit is retained within that attempt, but never imported from another attempt. The achievement requires both components before expiration. Do not merge 15 days from one pair of targets with 15 days from another.

**Difficulty:** Hard. The player must maintain several active commitments while finding the personnel and resources for an operation. The award itself, the passage of 180 days, and the random choice of upgrades do not unlock it.

**Tracking:** Evaluate only countries with an open attempt. Preserve target-pair identity, the current continuous interval, operative provenance, successful-operation credit, and deadline in the save. A bounded daily check for this active 30-day challenge is appropriate if verified native callbacks cannot provide the same evidence. Do not add a permanent all-country achievement scan.

**Icon direction:** Two outward lines balanced by a strong central shield. Maintain a different silhouette from A1 while keeping the pair visually related.

## Evidence required before shipping

The implementation must prove that it can identify Event 83 recruits, actual operation participants and completions, the native target-network value, and active home counter-intelligence assignment. A hidden counter that increments whenever a player closes an event report is not a substitute.

Use the existing achievement registry and existing test-disqualification mechanism. The proposed working keys need a collision check before becoming final internal IDs. Missing hooks are implementation blockers and must be reported rather than replacing either pursuit with an automatic award.
