# Event 046 achievement implementation prompt

Implement every Event 046 achievement described in `specs/046_the_great_shuffle_spec_part_7_achievements_assets_localisation_and_acceptance.md`.

Read `AGENTS.md`, `chaos-redux-events`, `chaos-redux-event-assets`, and the current achievement registry before editing.

Keep all achievement tracking protected from The Great Shuffle.

Do not allow an achievement flag, counter, selected family, ranking proof, disqualifier, or completion state to enter the shuffle registry.

## Required achievements

### `chaosx_046_shuffle_veteran`

Track five distinct natural successful Event 46 transactions on the same persistent human country scope.

After the fifth, require 365 days of continued existence, independence, and no capitulation.

Cosmetic identity and ordinary government changes may remain eligible when the country scope persists.

### `chaosx_046_from_empty_depots`

Create a qualification only when one Evolution I or later natural firing reduces normalized ordinary equipment-stockpile value by at least 60 percent, reserve manpower by at least 50 percent, and fuel by at least 70 percent.

Within 730 days require fuel at 75 percent of current capacity, at least 95 percent equipment fulfillment across 24 deployed ordinary divisions, and one war victory after qualification.

Use a documented equipment-family score so cheap bulk tokens cannot satisfy the stockpile proof alone.

### `chaosx_046_impossible_geography`

After one Evolution II or later natural firing, identify one player-controlled state in the top world industry decile and bottom population quartile, plus another in the top population decile and bottom industry quartile.

Store the qualifying ranking once.

Require 365 days of ownership or control, supply connection, and no enemy occupation for both states.

### `chaosx_046_government_rebuilt`

After one Evolution III or later natural firing, qualify only when Stability and War Support are each at or below 10 percent, ruling-party support is below 20 percent, and at least two ordinary law categories changed.

Within 540 days require at least 70 percent Stability, 70 percent War Support, 50 percent ruling-party support, continued country identity, and no capitulation.

Exclude countries whose owner systems make the ordinary politics proof invalid.

### `chaosx_046_world_redealt`

Keep hidden until Evolution V is available.

Qualify only when one natural firing commits at least one family from every available capability band and at least 90 percent of the complete eligible safe pool after invalid scopes and declared conflicts are removed.

Require 180 days of continued independent existence.

Do not count a hidden missing core family as unavailable merely to pass the denominator.

### `chaosx_046_three_reversals`

Keep hidden.

After the first qualifying natural firing, choose one approved comparable national family from Stability, War Support, fuel share, reserve manpower, one military experience store, or normalized ordinary equipment value.

Require top world quintile after the first firing, bottom quintile after the second consecutive firing, and top quintile after the third consecutive firing.

Then require a war victory after the third firing.

The same country and comparable family must persist.

## Disqualifiers and source proof

Detect and disqualify Event 46 force mode, debug setup, validation bypass, and player country changes where the existing project provides proof.

Do not invent unreliable console detection.

Normal automatic cluster firing remains eligible when it is ordinary campaign selection.

Each transaction can create achievement proof only after it closes successfully.

An aborted or partially blocked transaction cannot qualify.

Save and load recovery cannot create duplicate progress.

A later Great Shuffle interrupts an exact timed sequence only where the achievement definition says so.

Use sparse tracked-country hooks or existing achievement processing.

Do not add a daily or monthly whole-world scan.

## Registry and localisation

Add the achievements to the single root Chaos Redux achievement registry.

Implement completion triggers, tracking flags and variables, disqualifiers, hidden or visible status, and any needed Event 46 callbacks.

Write final player-facing localisation from the directions in Part 7.

The visible text must explain the feat clearly without showing hidden percentiles, debug flags, internal transaction IDs, or raw family IDs.

## Asset handoff

Use the completed icon triplets from `prompts/046_the_great_shuffle_asset_prompt.md`.

Achievement filenames must match the full IDs and root-only runtime convention.

Do not use placeholders, recolored unrelated icons, or missing variants.

## Evidence and handoff

List every changed achievement ID, tracking identifier, Event 46 callback, localisation key, icon path, and documentation row.

Test the exact cases `A46-062` through `A46-067` from the acceptance matrix.

Report percentile tie handling, save persistence, force-mode disqualification, same-country proof, and no-write protection from Event 46.

Do not mark Event 46 complete while any mapped achievement, icon, localisation, or tracking path is missing.
