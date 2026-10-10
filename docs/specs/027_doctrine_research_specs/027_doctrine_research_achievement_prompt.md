# Achievement prompt: Event 027 Doctrine Research

## Status

The three achievements are implemented in `common/scripted_effects/027_doctrine_research_achievement_effects.txt`, registered in the root Chaos Redux achievement registry, localised, and given final icon triplets.
Part 4 owns their requirements, shared rules, and disqualifiers; this prompt keeps only what a change to them must re-check.

Use this prompt when revisions R1 to R7 change the flow, when a new doctrine domain is registered, or when achievement tracking is touched.
Do not create a second registry or a new `unique_id` file.

## Validation cases

### `027_doctrine_research_first_lesson`

- Pass: an Evolution I curriculum adopts a Grand Doctrine in a domain that was empty at its start, then advances a subdoctrine in that domain.
- Pass: the same with Chaos Warfare adopted into an empty `land` folder and a Chaos Warfare track advanced.
- Fail: adoption followed by a step in another domain.
- Fail: adoption followed only by native combat mastery.
- Fail: adoption and step in different curricula.
- Hold: save and reload between the two choices.

### `027_doctrine_research_single_school`

- Pass: an empty five-level track assigned and advanced by all five Evolution IV choices.
- Pass: a held branch at level 0 advanced five times.
- Fail: the fifth choice targets another track.
- Fail: the first choice adopts a Grand Doctrine.
- Fail: banked mastery completes the branch after four event steps.
- Hold: save and reload between every choice.

### `027_doctrine_research_joint_curriculum`

- Pass: four tracks of one Army Grand Doctrine.
- Pass: tracks spread across one land Grand Doctrine, Navy, and Air.
- Pass: an Evolution IV curriculum whose fifth choice repeats a track.
- Pass: two Special Forces subdoctrines counted separately.
- Fail: four steps that touch fewer than four tracks.
- Fail: one of the four levels comes from faction sharing.
- Hold: save and reload after three distinct tracks.

## Revision checks

- R2 and R3 change how a step is triggered, not what a receipt records; every case above must still pass with the one-click step and the "advance again" option.
- R5 delegated steps count as the country's own receipts, so a fully delegated Evolution IV curriculum can still satisfy any achievement whose route the AI happens to take.
- R6 removes the summary counters from the page; the achievement checks keep reading the receipts directly.

## Text

Titles and descriptions state the public requirement in the project writing style and never mention receipts, ledgers, arrays, or debug state.
Run `chaosx_localisation_auditor` on any changed achievement key.
