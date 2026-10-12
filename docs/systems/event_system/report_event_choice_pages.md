# Report event choice pages

## Purpose

Player-facing report events have at most four direct option blocks, keeping every choice visible in a compact event window.

When a report offers more choices, the event uses additional report pages and keeps the original option effects, option triggers, and AI weights.

## Player flow

The original event keeps its title, description, picture, event trigger, and immediate effect, then shows the first group of original responses with a localized `More options` control.

The first continuation page repeats the opening response group without repeating the original immediate effect, so a later `Back to responses` action never reruns setup or consumes a snapshot twice.

Middle pages show up to two original responses plus `Back to responses` and `More options`, while the final page shows up to three original responses plus `Back to responses`.

Each navigation control appears only when an original response on another page is eligible, and a hidden dispatcher routes it to the nearest eligible page using the original option triggers.

The hidden dispatchers have no report picture and execute only their immediate routing effect, so they add no player-facing page or choice.

## AI and scope behavior

Events that already restrict the recipient with `is_ai = no` retain their existing AI path, including the dedicated Event 027 doctrine resolver and Secret Alliance invitation resolver.

For other roots, the original event keeps one AI-only route option and sends the recipient to an AI-gated companion event that contains the complete original option pool without report art.

The AI companion retains the original option triggers, effects, and `ai_chance` blocks, so the authored weighted selection remains in one flat option pool and the navigation controls do not enter AI selection.

The original root remains the only page with its original immediate effect, and the audited roots contain no `after` blocks that need to be transferred.

Event `chaosx.nr15.210` receives its sender through `FROM`, so the root saves that scope as a regular event target and the later player pages and AI companion use the saved target when checking or contacting the sender.

Regular event targets carry through the event chain and clear with that chain; the page flow does not create a persistent global target.

## Timing and assets

The original root retains its existing timeout, and continuation pages copy any explicit `timeout_days` value from that root.

Each continuation page starts a fresh event timeout, so navigating between pages can extend the original decision window by another page interval.

No icons or sprites were added; player pages reuse the original report picture, and AI-only companions omit the report picture.

## Future extension

Use this page pattern when another player-facing report event exceeds four choices, keeping its original option blocks together and routing by their existing triggers.

If the option family has a current AI path, preserve that flat path in an AI-only companion rather than using navigation weights to approximate the original selection.

The flow can be extended with a richer page indicator if the event UI framework provides one without increasing the direct option count.
