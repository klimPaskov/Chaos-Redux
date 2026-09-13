# Event 065 Random Trait

## Part 2: Trait Pool, Registry, Weighting, and Rolls

## Trait universe

For Event 65, the complete pool is the final loaded **country-leader trait database** used by the country-leader trait effect.

The authoritative inclusion test is engine ownership and effect compatibility.

A source entry belongs in the pool when the final loaded game treats it as a country-leader trait definition that can be named by `add_country_leader_trait`.

This interpretation includes all roles stored in that database, even when their normal use is not the current political leader.

The pool therefore includes:

- political leader traits
- advisor traits
- political advisor traits
- theorist traits
- army, navy, and air high-command traits stored in the country-leader database
- manufacturer and industrial concern traits stored in the country-leader database
- country-specific and route-specific traits
- traits attached to historical figures
- traits attached to councils, regencies, committees, animals, or unusual characters
- DLC-defined traits when their definitions are loaded
- every Chaos Redux trait in the same database
- hidden, negative, mixed, empty, or narrow traits when the engine still treats them as valid source entries

The pool does not cross into a separate engine database merely because that database also uses the word `trait`.

The implementation must not import unit commander traits, operative traits, Military Industrial Organization upgrade traits, ship-designer modules, terrain traits, or other non-country-leader records unless engine inspection proves that they are also valid country-leader trait definitions.

## Load-order rule

The registry mirrors the final loaded definition set.

When vanilla and Chaos Redux define the same trait ID, the final load-order winner appears once.

An overridden ID is not counted as two independent outcomes.

The manifest records both the original source and the final owning definition when that information can be resolved.

Duplicate definitions inside the same load result are an error that must be reported.

A repeated trait ID in generated roll logic is also an error.

## Source discovery

The implementation must use a generator or equivalent reproducible build step.

The generator scans:

- the active vanilla country-leader trait roots
- the Chaos Redux country-leader trait roots
- any additional Chaos Redux event-owned country-leader trait files that load through the same database

The generator must parse Clausewitz structure.

A regular-expression-only scan is not sufficient as the final parser because nested blocks, comments, aliases, and repeated keys can create false entries.

The implementation agent must confirm the exact source roots against the current game version and offline documentation before finalizing the generator.

## Generated registry

The generator creates one canonical registry entry per final source trait ID.

Each entry records at least:

- stable numeric Event 65 registry index
- source trait ID
- final source family
- final source file
- final definition hash
- vanilla or Chaos Redux origin
- DLC or content condition when verified
- localisation name status
- localisation description status
- icon or presentation status when the source system exposes one
- featured status
- featured reason tags
- final baseline weight
- final Evolution II weight
- final Evolution III weight
- duplicate or override notes
- parser status
- runtime inclusion status
- explicit exclusion reason when technical exclusion is unavoidable

The complete schema is defined in `handoffs/065_random_trait_trait_registry_schema.md`.

## Inclusion policy

The default is inclusion.

The generator must not remove a trait because it is:

- too strong
- too weak
- useless on a political leader
- harmful
- beneficial
- strange
- contradictory
- historically specific
- country-specific
- ideology-specific
- gendered
- associated with a dead or absent person
- associated with an animal
- associated with a company
- normally used only as an advisor
- normally hidden behind a DLC route
- likely to look absurd
- checked by another game system
- an upgraded or downgraded form of another trait

Those qualities are part of the event.

## Technical exclusions

A source entry may be excluded only when one of these conditions is proven:

1. The parsed block is not a country-leader trait definition in the final engine database.
2. The entry is malformed and cannot load.
3. The entry is an unresolved alias with no independent trait identity.
4. The trait ID does not exist after load-order resolution.
5. The current engine rejects the trait through every supported country-leader application path.
6. Applying the trait causes a hard script error, crash, infinite loop, or deterministic desynchronization that cannot be fixed without changing the source trait itself.

Every technical exclusion must appear in the generated manifest.

A hidden manual exclusion list is forbidden.

A large technical exclusion count blocks the claim that the pool is complete.

## Missing localisation

A valid trait remains in the pool when its normal name or description localisation is missing.

The generator flags the gap.

The implementation must add a bounded Event 65 fallback display mapping so the player never sees a raw key in the Event 65 report.

The fallback must describe the source trait identity without inventing effects.

It does not replace or rewrite the source trait's own localisation outside Event 65.

## Native application

The preferred effect is the native source trait itself.

The implementation must call the normal country-leader trait effect with the source ID.

It must not replace ordinary source traits with generic approximations.

If a small number of valid database entries cannot be attached through the normal effect but are still part of the promised trait universe, the scripted-system architect must document the exact failure and propose the narrowest source-faithful fallback.

That fallback requires explicit review before implementation.

## Registry freshness

The complete pool is complete only for the game and mod build used to generate it.

The generator must support a check mode that compares current source definitions with committed generated outputs.

The check fails when:

- a new source trait is missing
- a source trait was removed but remains live without a legacy reason
- a source definition changed without a new hash
- a trait ID appears more than once in the generated roll pool
- a featured classification refers to a missing source trait
- a generated localisation selector refers to a missing registry index
- a generated weight total does not match the emitted entries

The repository validation workflow should run this check after game updates and after Chaos Redux adds or removes country-leader traits.

## Weight model

### Uniform forms

Baseline and Evolution I use a uniform distribution.

Every eligible source trait has weight `100`.

The number `100` is a readable normalization anchor.

Only weight ratios matter.

### Featured tag

Evolution II and Evolution III use one non-stacking featured tag.

A source trait is featured when at least one reviewed reason applies:

- powerful
- unusually broad
- unusually severe
- unusually beneficial
- unusually harmful
- bizarre
- extreme
- rare in normal gameplay
- tied to a narrow historical route
- unique to an unusual character
- defined by Chaos Redux

A trait with several reason tags still receives one featured weight.

The reasons remain in the manifest for review.

Positive and negative polarity do not change the weight by themselves.

### Planned weights

| Event form | Ordinary trait | Featured trait | Maximum individual ratio |
| --- | ---: | ---: | ---: |
| Baseline | 100 | 100 | 1.00 |
| Evolution I | 100 | 100 | 1.00 |
| Evolution II | 100 | 125 | 1.25 |
| Evolution III | 100 | 150 | 1.50 |

These values are initial balance targets.

They must be centralized in Event 65 script constants.

They must be evaluated against the generated pool before acceptance.

The probability auditor may recommend a lower featured weight when the featured class is too large.

The auditor must not increase the maximum ratio beyond the user-requested modest weighting without a design revision.

## Featured classification process

The generator assigns ordinary status by default.

Chaos Redux origin automatically supplies the `chaos_redux` featured reason.

Other reasons come from a reviewed override file.

The override file must be human-readable and contain one source trait ID per row.

Automated heuristics may propose candidates based on rarity, source uniqueness, modifier count, route usage, or naming patterns.

Heuristics cannot silently make final classifications.

The generated manifest records whether a featured reason came from source origin, reviewed override, or accepted heuristic.

## Probability mass safeguards

The weighting must preserve the event's broad random character.

For every supported content profile:

1. Every eligible ordinary trait has positive probability.
2. Every eligible featured trait has positive probability.
3. No single featured trait has more than 1.25 times the probability of an ordinary trait at Evolution II.
4. No single featured trait has more than 1.50 times the probability of an ordinary trait at Evolution III.
5. The ordinary class must remain the largest probability class when it is the largest class under uniform weighting.
6. Evolution II ordinary probability mass must remain at least 70 percent of its uniform-class probability mass.
7. Evolution III ordinary probability mass must remain at least 55 percent of its uniform-class probability mass.
8. A trait with several featured reasons receives no stacked multiplier.
9. A Chaos Redux trait is boosted once, not once for source origin plus each unusual property.
10. Content gates, duplicate rejection, and saturation must renormalize over the remaining eligible pool without creating zero-probability ordinary entries.

## Roll independence

Each trait slot begins with a fresh draw from the stage distribution.

After an accepted trait is added, that source ID leaves the recipient's eligible set for later slots.

The resulting multi-trait package is therefore weighted sampling without replacement.

This is the only correct way to combine the user's independent-roll direction with the requirement that each slot add a genuinely new trait.

The implementation and localisation must not claim that later slots are statistically independent after earlier accepted traits are removed.

They remain fresh random draws from the remaining complete eligible pool.

## Collision rules

A proposed source ID is rejected when any of the following is true:

- the active leader currently has that source trait
- the leader's Event 65 ledger records that source ID from an earlier firing
- the source ID was accepted in an earlier slot of the current firing
- the source definition is not loaded in the current content profile
- the target role became invalid before application
- the source effect failed and inspection confirms no trait was added

A rejected proposal does not consume a trait slot.

The roll continues until the slot succeeds or the recipient is saturated.

## Event 65 grant ledger

The event needs a persistent recipient-level history of source IDs granted by Event 65.

The ledger exists to:

- prevent duplicate grants after another system removes a visible trait
- distinguish prior Event 65 grants from traits the leader began with
- support exact saturation checks
- support debug and acceptance evidence
- preserve repeat behavior through save and load

The ledger should live on the exact trait recipient.

Character scope is preferred when the country-leader role uses a stable character object.

If traits are role-local and not character-local, the ledger must use the same role identity.

Country scope alone is not sufficient when a leader can leave office and later return.

The scripted-system architect must verify the final scope before coding.

## Roll implementation

The final implementation may use a generated conditional random list, a generated hierarchical dispatcher, a generated index map, or another engine-supported method.

The method must satisfy all of these conditions:

- exact stage weights
- exact exclusion of ineligible source IDs
- no hidden thematic filters
- no duplicate source entries
- bounded execution
- correct behavior near saturation
- deterministic host-authoritative multiplayer behavior
- generated complete coverage that is not manually curated
- inspectable output
- exact probability evidence through the HOI4 probability tools

A huge hand-maintained flat list is not an acceptable long-term source of truth.

A generated flat list can be valid when the generator, manifest, and freshness check are committed and performance is acceptable.

## Performance architecture

The generator may partition the complete pool into balanced dispatch groups to reduce evaluation cost.

Any hierarchy must preserve exact entry weights.

A group must be selected in proportion to the sum of its eligible entry weights or use an exact rejection method whose conditional distribution is proven.

A convenient group count is not a reason to distort probability.

High-saturation fallback behavior must remain correct.

A deterministic first-match fallback is not acceptable when it creates measurable bias among the last eligible traits.

## Side effects from source traits

The event adds the real trait.

Normal modifiers and normal script checks tied to that trait can therefore react.

This can create strong, weak, absurd, or route-specific consequences.

Those consequences are part of the design.

The implementation must not sanitize them merely because the receiving leader is unusual.

Hard errors, crashes, infinite loops, corrupted save state, and deterministic multiplayer desynchronization remain defects.

## Third-party mod scope

The promised pool covers vanilla Hearts of Iron IV and Chaos Redux.

Traits added only by unrelated third-party mods are not automatically imported.

This keeps the generated registry reproducible and prevents Event 65 from claiming support for unknown external script behavior.

Compatibility work can be added later through an explicit extension registry.

## Required generated evidence

A completed pool build must produce:

- the generated runtime pool
- the stable index map
- the featured override source
- the full trait manifest
- total trait count
- counts by vanilla and Chaos Redux origin
- counts by ordinary and featured class
- counts by content gate
- duplicate and override report
- missing localisation report
- parser error report
- technical exclusion report
- definition hash summary
- generated-output checksum
- probability input manifest
- check-mode result
