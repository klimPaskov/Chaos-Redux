# CBRN takeover decisions

## Authority

Disposition: implemented within the user-authorized 2026-10-06 takeover scope.
The user authorizes correction of weak design and assigns inherited CBRN changes to this workstream.
Current source proves implementation, while the accepted September amendment and named achievement requirements establish design intent.

## Armored delivery category and retired art

Rename the category to `category_cbrn_armored_delivery_support`, displayed as Armored Delivery Detachments.
The same three chassis detachments remain members, and every doctrine modifier retains its value.
The old label described eighteen removed companies and could mislead division-design choices.
Remove the 63 orphan non-support chemical-tank sprites and 108 unreferenced tank textures after checking runtime references.
The 108 include the 45 older unreferenced files and the 63 textures orphaned by this pass.
Preserve the eight shared category and Livens textures until their original replacements are wired.
The installed roster is 79 units, with 55 combat battalions and 24 support companies, rather than copying earlier stale counts.

## Achievement candidate review

The inherited uncommitted tranche contains three attempted achievements and their hooks.
The Air Is Still Breathable and The Antidote Arrived are adopted after correcting their proof and adding localisation.
The first requires confirmed enemy exposure during the specific major-war relation that later ends in a major capitulation, with protection maintained by existing country refreshes.
Pair-specific war flags are reset on `on_war_relation_added`, preventing an earlier attack from satisfying a later war.
The second tracks one nerve-agent containment episode on its actual state, from the first protected nerve release through severe contamination, medical care and decontamination to zero contamination.
All chemical deaths during the open episode count, including subsequent agents and continuing deaths.
Failed protection or excessive losses prevent a fresh attempt until that contamination is removed, and a controller change invalidates the episode.
Advanced mask research alone does not qualify without real advanced or sealed issue.
The exact cleanup hook lives inside the state contamination-delta owner, replacing the inherited duplicated caller hooks.
The continuing-death caller initializes the death output before invoking the shared helper.
No extra popup or recurring world scan is introduced.

Disposition: rejected for the inherited No Wind Is Friendly candidate.
Its positive proportional friendly damage measures ordinary risk, not a forecast-failure outcome, and taking a state does not prove recovery of the affected army.
Its helper-local damage outputs were also read after return, and its single state actor could be overwritten.
The candidate is preserved in `subagent_handoffs/2026-10-06_rejected_no_wind_candidate.txt` as evidence and removed from loaded runtime rather than shipped as a weaker substitute.

Disposition: blocked for No Wind Is Friendly and Unbroken Supply Corridor.
The former needs an actual forecast-failure outcome and affected-army recovery proof.
The latter needs exact assigned-army supply and the completed offensive objective linked to its corridor.
Current country stock, commander service, national modifiers, railways and state cleanup do not establish those facts.
The installed unit-leader dynamic-variable documentation exposes no current assigned-army supply value, and reference searches for `has_army_supply` and `supply_ratio` return no rule.
No exception or removal of these accepted achievements is inferred from the older July skip note.

## Evidence boundaries

The parent tool inventory does not expose HOI4 routes, but the delegated specialist sessions do expose and call them.
This is a client exposure gap, not proof that the service is absent.
Source-only checks cannot close native raid refund/payment behavior or visual acceptance.
The previous audio decision preserves the active files and their timing, but runtime sound provenance still requires a source/license crosswalk.

## Air contamination news

Disposition: implemented within the shared callback reached by chemical and biological consequences.
A single large contamination increase previously sent four distinct news popups for the four thresholds.
The callback still marks every crossed threshold and every corresponding one-shot news flag, but it announces only the highest threshold reached by that update.
Only the three lower news calls receive upper-bound guards, without changing contamination values, consequences, threshold state or the Fallout request handoff.
This reduces a jump across all four thresholds from four popups to one and prevents later backtracking from repeating skipped notices.

## Inherited evidence and parser repair

Disposition: implemented.
The inherited `parent_before_evaluate_request.json` contained only a UTF-8 BOM, with no request or JSON object, so it is removed after review.
The inherited protective-aid `startup_error.json` preserves a genuine October 3 missing-request-file failure and is committed as historical route evidence, without representing current service health.
The occupied/export suite's imported parser rejected a native bare advisor-token list in the owned protection source.
Its local parser now accepts bare list members and still parses the same operators and blocks, leaving the shared Event 026 VM unchanged.
The 106 sabotage cases, 21 immediate-protection cases and 46 occupied/export cases pass against the current source.
These source models do not replace native payment, damage or timer acceptance.
