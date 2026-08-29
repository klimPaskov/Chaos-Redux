# Achievement implementation prompt: Event 027 Doctrine Research

Implement the complete Event 027 achievement set from the accepted source specification.

Read first:

- `AGENTS.md`
- `.agents/skills/chaos-redux-events/SKILL.md`
- `.agents/skills/chaos-redux-event-assets/SKILL.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`
- `docs/specs/027_doctrine_research_specs/027_doctrine_research_spec_part_4_presentation_assets_achievements.md`
- `docs/specs/027_doctrine_research_specs/027_doctrine_research_acceptance_criteria.md`
- the final Event 027 implementation, batch ledger, doctrine adapter registry, and current root achievement registry

Use the single root Chaos Redux achievement registry. Do not create a second achievement registry or a new `unique_id` file.

The labels below are working labels. Write final titles and descriptions in the normal project style after checking achievement text for clarity, uniqueness, and fit. Do not expose hidden variables, receipts, or debug state.

## Achievement 1

### Working key

`027_first_lesson`

### Public requirement

During one Event 027 batch, establish a Grand Doctrine in one doctrine domain, then use a later choice in the same batch to create an Event 027 mastery step in that same domain.

### Exact tracking contract

- record the current Event 027 batch identity
- record the domain of a successful Grand Doctrine adoption
- adoption must occur through one Event 027 choice
- a later successful Event 027 mastery receipt must use the same batch and domain
- the mastery receipt may select an empty track or advance an active branch
- the branch must be at Mastery I or higher after the receipt
- native progress can coexist, but only the Event 027 receipt satisfies the second part

### Eligibility

- human-controlled country when the batch begins
- batch size at least two
- normal project achievement eligibility

### Disqualifiers

- mastery occurs in another domain
- no later Event 027 mastery receipt exists
- the country is removed before completion
- the save uses a project-defined achievement-disqualifying debug or force route

### Validation cases

- pass with Evolution I adoption then same-domain mastery
- fail with adoption then another-domain mastery
- fail with adoption then native combat mastery only
- fail when adoption and mastery occur in different Event 027 batches
- survive save and reload between the two choices

## Achievement 2

### Working key

`027_single_school`

### Public requirement

During one Evolution IV batch, use all five choices to grant five Event 027 mastery steps to one five-level subdoctrine branch, and finish that branch.

### Exact tracking contract

- human-controlled country when the batch begins
- batch contains exactly five Evolution IV choices
- first successful mastery receipt records domain, Grand Doctrine, track, and subdoctrine identities
- every later successful choice must produce an Event 027 mastery receipt with the same identities
- count exactly five Event 027 mastery receipts
- no choice in the batch may be a Grand Doctrine adoption
- branch must be fully mastered when the fifth receipt resolves or at batch close
- branch must have a verified five-level structure and enough unearned event steps for the route to be possible

### Disqualifiers

- a choice targets another branch
- a choice adopts a Grand Doctrine
- fewer than five Event 027 mastery receipts are recorded
- native banked mastery, combat, faction sharing, focus, decision, another event, or debug progress supplies one of the required five event steps
- the branch completes before the five required receipts and later choices cannot target it
- the batch closes with an unused choice

### Validation cases

- pass with an empty five-level track and five same-branch receipts
- pass with a selected branch at level zero when the local graph uses that state
- fail when choice five targets a second track
- fail when the first choice adopts a Grand Doctrine
- fail when banked mastery completes the branch after four Event 027 receipts
- survive save and reload between every choice

## Achievement 3

### Working key

`027_joint_curriculum`

### Public requirement

During one evolved Event 027 batch, create Event 027 mastery steps in four distinct doctrine tracks.

### Exact tracking contract

- human-controlled country when the batch begins
- batch size at least four
- each successful Event 027 mastery receipt contributes its stable track identity to a deduplicated batch set
- tracks may belong to one Grand Doctrine or several doctrine domains
- repeated mastery in one track counts once
- Grand Doctrine adoption does not count as track development
- unlock when the fourth distinct track receives an Event 027 mastery receipt

### Disqualifiers

- fewer than four distinct tracks receive receipts
- one counted level comes only from native or external mastery
- the country is removed before the fourth distinct receipt
- project achievement eligibility is lost

### Validation cases

- pass with four tracks in one Army Grand Doctrine
- pass with tracks split across Army, Navy, Air, and Chaos Warfare when all are valid
- pass in an Evolution IV batch when the fifth choice repeats one track
- fail with four subdoctrines that share fewer than four stable track identities
- fail when one of the four levels comes from faction sharing
- survive save and reload after three distinct tracks

## Shared achievement safety

Use the Event 027 batch and transaction ledger. Do not infer achievement progress only from the country's final doctrine state.

Every successful Event 027 action needs stable IDs for:

- batch
- action type
- doctrine domain
- Grand Doctrine
- track
- subdoctrine
- event-attributed mastery receipt
- branch completion state

Clear temporary achievement state when the batch closes, the country disappears, or the route becomes disqualified. Preserve the permanent unlocked state through the normal achievement framework.

Prevent these false unlocks:

- native mastery gained while the Event 027 popup is open
- faction doctrine sharing
- focus or decision mastery rewards
- another event's doctrine grant
- debug mastery
- queued batches merging their receipts
- a tag switch applying one country's receipt to another
- save and reload duplicating the final receipt

## Localization

Write final achievement titles and descriptions after the conditions are implemented. The description should state the public requirement clearly. It should not mention internal batch IDs, receipts, arrays, variables, or engine terms the player cannot see.

Use the project writing rules. Keep each title distinct from the official Doctrine of Choice achievement and from existing Chaos Redux achievement names.

## Asset routing

Route icon production through the accepted Event 027 asset prompt and `chaosx_icon_artist` with `fork_context=false`.

Each achievement requires:

- original completed-state art
- completed DDS
- grey DDS
- not-eligible DDS
- filename matching the final root achievement ID
- manifest entry
- contact sheet
- GFX handoff

Do not mark the achievement complete while its icon triplet is missing or provisional.

## Documentation and audit

Update the Event 027 documentation with the final titles, public conditions, tracking summary, disqualifiers, and icon paths.

Run a localization audit for all achievement keys. Include the achievements in the Event 027 completion audit.

Report:

- final achievement IDs
- conditions and disqualifiers implemented
- tracking variables or flags and cleanup behavior
- localization keys
- icon paths and status
- validation scenarios run
- remaining blockers

Do not simplify a condition into event firing, obvious option selection, or final doctrine state alone.
