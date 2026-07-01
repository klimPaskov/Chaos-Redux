# Event 011 Secret Alliance Country Overlay and Focus Notes

Event 011 does not create new tags by default. It creates an overlay on existing countries through flags, temporary ideas, roles, AI strategies, and event targets.

## Country overlay package

| Overlay | Applied to | Contents | Cleanup |
| --- | --- | --- | --- |
| Founder member | three initial minor countries | member flag, founder role, confidence, hidden idea, promise memory | remove on exit, annexation, reveal defeat, pact collapse |
| Recruit member | invited minor countries | member flag, recruit role, confidence, hidden idea, promised gain | remove on exit or invalidation |
| Major patron | one valid major at Evolution II or III | patron flag, liaison idea, member support decisions, AI strategy | remove if exposed and split, defeated, invalid, or pact collapses |
| Confirmed member | member revealed by evidence | public signatory flag, exposed idea, decision target visibility | convert to war member or remove after settlement |
| Formal war member | member after war reveal | faction membership, war idea, war AI strategy | remove after peace or defeat |
| Target country | original player target | pressure idea, dossier values, decision category, counter-network idea | aftermath cleanup after collapse, victory, defeat, or tag invalidation |

## Focus tree handling

The event should not replace focus trees for existing countries. Pact membership is an overlay. Existing countries should keep their normal focus trees unless the broader Chaos Redux implementation later defines an additive event-specific branch.

Focus hooks may still matter:

- existing focuses that improve intelligence, diplomacy, security, or border defense can reduce investigation costs or improve counter-readiness
- existing focuses that create claims against the target can raise candidate membership score
- existing focuses that form or join factions can make a country less eligible or more dangerous as a patron
- target focuses that improve agency, stability, war support, forts, railways, or diplomacy can support counterplay
- member focuses that produce war goals against the target should trigger reveal if they create direct war

## Country package audit notes

Use `chaosx_country_package_auditor` only for narrow event overlay risks:

- member flags and ideas are removed when a country exits or is annexed
- no existing country has its tree replaced by the event by accident
- special chaos countries and nonhuman actors are excluded through shared classification triggers
- subjects, faction members, and majors obey the eligibility and patron rules
- AI strategies do not persist after pact cleanup

## Asset implications

No new country flags, ideology flags, cosmetic tags, or real leader portraits are required. The asset team should not replace existing flags for countries chosen as pact members.
