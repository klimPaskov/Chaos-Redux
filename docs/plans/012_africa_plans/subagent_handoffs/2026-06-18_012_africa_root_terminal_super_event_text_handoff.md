# Event 012 Africa — Root-terminal super-event text disposition

Date: 2026-06-18
Subagent scope: super-event text research only
Status: recommendation ready

## Recommendation

`africa_world_is_one_root_variant_terminal` should **not** become a distinct final super-event role.

It should be documented and treated as an **explicit presentation-sharing decision under base slot `72` (`The World Is One`)**, with slot `79` remaining the only distinct terminal presentation variant because the Archive route changes the terminal register from command to record.

## Why this is the stronger fit

1. Slot `77` already carries the dedicated root-world escalation role.
   - `The World Root Mandate` is the route's researched root reveal and is already framed in the exact “all life under one mandate” register.
   - Source package already in live research and localisation:
     - Job 12:10 KJV, `In whose hand is the soul of every living thing, and the breath of all mankind.`
     - https://www.biblegateway.com/passage/?search=Job+12%3A10&version=KJV

2. Slot `78` already carries the mixed constitutional impossible-parliament role.
   - `Parliament of Root and Fang` is the route's second specific root-facing presentation beat.

3. The terminal role is different from the root reveal role.
   - The terminal `World Is One` branch is defined in the prompt and foundation notes as the point where all continental unifiers have completed their post-unification and world-end prerequisites and the campaign-ending world order begins.
   - That is a different dramatic job from “Africa discovers or legalizes the World Root.”

4. A separate root-terminal slot would duplicate meaning faster than it adds clarity.
   - Root players would see three closely related late presentations: root mandate, root-and-fang escalation, then root-terminal.
   - The current slot spread already gives the high-chaos route more bespoke presentation than the baseline route. Another distinct terminal slot would overspecify the Africa-side route identity at the moment the event is supposed to widen into a cross-continental world-end frame.

5. The Archive exception is materially different in a way the root branch is not.
   - Slot `79` works because it changes the terminal logic's public face from universal command to universal record.
   - The root route, by contrast, is already textually covered by slot `77`; at terminal scale it reads best as a route-conditioned interpretation of the same world-order proclamation, not as a separate final role.

## Exact documentation wording recommended

Use this wording in the parent-facing docs or blocker resolution note:

> `africa_world_is_one_root_variant_terminal` is resolved as a shared-presentation case, not a distinct final super-event role. The Green Covenant / World Root route keeps its bespoke escalation reveals in slot `77` (`The World Root Mandate`) and slot `78` (`Parliament of Root and Fang`), but once the full terminal world-end gate opens it shares base slot `72` (`The World Is One`). Only the Archive-Bestiary route keeps a distinct terminal presentation variant in slot `79`, because that route changes the terminal register from command to record rather than only recoloring the same final proclamation.

## Distinct-slot contingency package if design later forces one

This is **not recommended**, but it is the safest clean package I found if the parent later insists on a distinct root-terminal role.

- Title: `The World Has Roots`
- Main quote: `and the leaves of the tree were for the healing of the nations.`
- Source: Revelation 22:2, King James Version
- Source URL: https://www.biblegateway.com/passage/?search=Revelation+22%3A2&version=KJV
- Button: `The healing of the nations.`
- Description direction: the continental world-root order has outgrown Africa and entered the final world charter; foreign unifiers, impossible delegations, and human states now face a planetary settlement framed as life-law rather than merely federation or conquest
- Attribution confidence: high
- Copyright note: public domain scripture
- Fit note: this avoids repeating Job 12:10 from slot `77`, keeps the root/tree register explicit, and scales better to the cross-continental terminal role than a third reuse of the existing root quote

## Blockers

- No live terminal emitter branch currently distinguishes root-terminal from ordinary slot `72`; the only terminal conditional in live code is `africa_route_archive_bestiary` -> slot `79`.
- No research surface currently establishes a separate final dramatic function for root-terminal beyond “root route reaches the same terminal world-end gate.”
- If design still wants a distinct root-terminal slot, it needs an explicit role statement stronger than “World Root route, but terminal,” otherwise the package will overlap slots `77` and `78`.

## Files inspected

- [docs/specs/012_africa_specs/prompts/012_africa_super_event_prompt.md](/home/klim/projects/chaos_redux/docs/specs/012_africa_specs/prompts/012_africa_super_event_prompt.md)
- [docs/super_events/012_africa_super_event_research.md](/home/klim/projects/chaos_redux/docs/super_events/012_africa_super_event_research.md)
- [docs/events/012_africa_foundation.md](/home/klim/projects/chaos_redux/docs/events/012_africa_foundation.md)
- [docs/specs/012_africa_specs/specs/012_africa_high_chaos_absurd_paths.md](/home/klim/projects/chaos_redux/docs/specs/012_africa_specs/specs/012_africa_high_chaos_absurd_paths.md)
- [docs/specs/012_africa_specs/specs/012_africa_evolutions_world_end_and_scenarios.md](/home/klim/projects/chaos_redux/docs/specs/012_africa_specs/specs/012_africa_evolutions_world_end_and_scenarios.md)
- [docs/specs/012_africa_specs/specs/012_africa_focus_tree_plan.md](/home/klim/projects/chaos_redux/docs/specs/012_africa_specs/specs/012_africa_focus_tree_plan.md)
- [common/scripted_effects/012_africa_effects.txt](/home/klim/projects/chaos_redux/common/scripted_effects/012_africa_effects.txt)
- [common/script_constants/012_africa_constants.txt](/home/klim/projects/chaos_redux/common/script_constants/012_africa_constants.txt)
- [localisation/english/012_african_union_l_english.yml](/home/klim/projects/chaos_redux/localisation/english/012_african_union_l_english.yml)

## External source checks used

- Bertrand Russell, *Why Men Fight* (Project Gutenberg): existing slot `72` quote witness
  - https://www.gutenberg.org/files/55610/55610-h/55610-h.htm
- Alfred, Lord Tennyson, `Locksley Hall` (Project Gutenberg): existing union/world-order button witness
  - https://www.gutenberg.org/files/8601/8601-h/8601-h.htm
- Job 12:7-10 KJV (Bible Gateway): existing root/bestiary package witness
  - https://www.biblegateway.com/passage/?search=Job+12%3A7-10&version=KJV
- Revelation 22:2 KJV (Bible Gateway): contingency distinct root-terminal candidate
  - https://www.biblegateway.com/passage/?search=Revelation+22%3A2&version=KJV
