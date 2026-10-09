# Event 033 storm-clock repair acceptance

Disposition: implemented source candidate under the accepted bounded repair, with comparison and native acceptance still incomplete.
Acceptance basis: the user's three-day active-only mortality, generation-safe targeting and idempotent cleanup requirements, Part 4's mortality timing and Part 7's forecast and active-duration contracts.
The parent reviewed the complete storm-clock handoff and sealed actual-source replay before granting the architect the two-file patch scope.

The accepted repair anchors each class clock at its actual opening, excludes dispatch outside `start <= now < end`, validates the exact current-generation state/slot/serial record before mutation, and distinguishes expired pending forecasts from genuine active episodes.
Pending cancellation must not create impact history, active-episode closure, a severe cooldown draw or another slot's active-count debit.
Active retirement preserves existing cleanup ordering, parent membership and modifier restoration, prior loss history, counter accounting and one cooldown draw.
Mortality rates, duration tuning, costs, weights, overlap policy, worker order, report-history policy and public meters are outside this patch grant.

The immutable before runtime is `3eb102bf6168362eadd58188d45791cd81f9713dc379d9e08da325334e65bd48` with triggers `ae069680a185d0a0aa24d301fe62d158edab09a1a8d7d4ca0a36752dfa974f86`.
The sealed runner is `241c252df0060dcd616ba8b0319566066e79a9474e8242d1e1bb7d431a027b5f`, with nine principal scenarios and forty-four variants.
Its before result has nineteen passes and twenty-five source-contract failures with no fixture failure.
Those failures remain historical and must not be overwritten as a repaired pass.
Physical callbacks in this replay are dispatch and entry-guard witnesses, not successful population or damage transactions.

F8 before-source and named fixtures are separately retained under `validation/probability/useful_windows_2026_10_09/`.
The mission-adapter baseline and sweep remain partial because ninety-three and ninety-two model inputs respectively are unresolved.
They do not establish actor/target eligibility, real costs, reserves, marginal benefit or actual pulse clocks.
A changed predicate still requires a separately pinned after capture and the same-named probability comparison, with those limits intact.

The focused Event 20 scan is retained in `parent_event_root_scan.json`.
It reports zero indexed helpers and therefore cannot establish this repair's helper or lifecycle coverage.
The graph descriptor is a structural comparison input, not verified helper execution or native clock evidence.
Legacy report migration, actual state-population-loss proof, reload, multiplayer, performance, assets/audio and final event acceptance remain unfinished.

The candidate runtime is `48b6c9b8ddcbacc8fafc002551735b7ade269929ecb36fa7beb5e6cc0a2ecabe`, with triggers `d284abdeb77e548c6d1d157f3bb5fb9c9b6ae548a86df2de222451efab21e6b5`.
The parent reviewed every changed source hunk and independently reran the sealed clock test at both final pins, reproducing forty-four passes and no source or fixture failure.
Runtime reversal replaces only the two current processor bodies with their archived counterparts and reproduces the entire before file byte-for-byte.
The six earlier non-sealed regression suites pass at the candidate, while dated F6/F7 receipts retain their original source identity.
Native clock-assignment validation remains `SCRIPT_CHECK_PARTIAL`, with argument blocks unchecked and `valid = null`.
The installed `set_variable` section was read at `effects_documentation.md:7888-7895`, revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`.
No source-only pass or unavailable graph artifact is promoted to native physics or event completion.
The parent independently reran the auxiliary exact-reversal, AST/loop-confinement and nine direct public-slot/serial predicate checks from the reviewed reproduction program.
The after medical projection `probability-e316c635aac6f8b6338b1d31` retains four cases, zero reported changes and ninety-three unresolved model inputs.
It selects two copies of unchanged B7D decision bytes and uses current shared helpers on both sides.
It therefore does not prove a historical 3EB/AE069-to-48B/D284 helper eligibility or clock delta, and that required comparison remains unresolved.
This native/model limitation is not a passing balance certificate or a reason to fabricate missing actor, target, quote or benefit facts.
