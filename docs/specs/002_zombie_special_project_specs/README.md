# Event 002 Zombie Special Project specifications

The base design source is [`002_zombie_special_project_spec.md`](002_zombie_special_project_spec.md).
The [2026-09-27 cure-raid payload correction](cure_raid_payload_correction_2026-09-27.md) records the bounded stockpiled-equipment contract and its parent acceptance basis.
Read that correction alongside the base specification's Anti-Zombie Bombs deployment section.
It does not approve unrelated offensive-strain design or establish live raid behavior.
The broader event implementation is documented in [`docs/events/002_zombie_outbreak/overview.md`](../../events/002_zombie_outbreak/overview.md).

## Changelog

### 2026-10-10 spec audit

Consistency pass: the specification now opens with an implementation anchor that names the project, raid, equipment, effect and constants owners, so it reads as a contract to maintain rather than unbuilt work.
The containment sections describe the real `zombie_decontaminated_state` modifier, its cure-linked removal trigger and the non-stacking target gate instead of vague "should" wording; the research flow follows the implemented gate order, with live testing and resource allocation after the state-of-the-infected choice; the manpower sacrifice, accident risk, creator cure window and bomb costs point at their constant groups instead of repeating literals; the accident section describes the real base-interval-and-factor model including the two biosecurity technologies that lengthen it; the achievements list carries the implemented identifiers; and the GFX section records the eight installed portrait sprites.
A gap is recorded at Section 11.3: the implemented friendly-strain gate permits only zombie-controlled target states, which is narrower than the Section 6.4 contract.

Design pass: a Shared Chaos Redux system connections section records the condemnation, deaths, Chaos Meter and hostile-capture connections that already exist, so no duplicate hooks are added, and proposes a zombie-outbreak famine adapter following the existing Black Plague adapter contract plus a visible consequence for sharing the creator's cure.
Both proposals and the targeting question are listed under Open questions.

