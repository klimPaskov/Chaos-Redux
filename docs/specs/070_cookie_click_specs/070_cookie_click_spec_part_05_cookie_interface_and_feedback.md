# 070 Cookie Click: interface and feedback

## One event-owned window

The Cookie window opens from its ordinary decision-category entry and from its first presentation event.
It is a dedicated Event 070 surface.
It does not replace the event log, settings interface or shared super-event window.

Use a colorful cookie and lively effects inside a restrained HOI4 metal-and-paper frame.
The cookie is the largest object and the main interaction.
The rest of the window makes today's obligation and next reward easy to read.
Do not turn the interface into a browser game pasted over the strategy map.

Plan a working canvas around 600 by 700 pixels at 1920 by 1080 and UI scale 1.0.
The exact final size and anchor must be adjusted against installed vanilla controls and the production GUI render.
This is a composition budget, not a claim of pixel-validated coordinates.

## Composition

| Region | Planned role | Approximate budget |
| --- | --- | --- |
| Header | Cookie identity, close button, small condition symbol | 50 pixels high |
| Progress strip | Fullness bar, accepted clicks and frozen target | 75 pixels high |
| Main interaction | Large cookie, genuine click hit region, bounded particles | About 320 by 320 pixels |
| Development line | Level and a concise next-band tooltip | 40 pixels high |
| Reward strip | Four milestone slots with paid, upcoming and locked states | 80 pixels high |
| Consequence strip | One current warning, next review or recovery instruction | Up to 70 pixels high |
| Footer | Compact access to relevant preparation or Empire action | Up to 50 pixels high |

Leave breathing room around the cookie.
Its painted limbs, crown, smoke and particles must not cover the close button, a reward tooltip or another active control.
The window should fit with the normal top bar and map controls visible.

The header does not need an ornamental subtitle.
The consequence strip shows only the highest-priority actionable state.
A mature but well-fed cookie does not keep a large permanent warning wall on screen.

## Native controls and art

The cookie image is an asset.
The click hit region is a native gameplay control.
The Fullness bar, level value, counters, reward quantities, tooltips and warning text are native dynamic elements.
None of them are painted into a background image.

The accepted click region follows the cookie's main body.
Decorative crumbs, teeth and smoke cannot unexpectedly capture clicks.
A stable hit region is preferable to one that changes shape with every animation frame.
The visible hover cue shows where a click will count.

A missed click outside the region cannot feed the cookie.
A double-click is two presses only when both are accepted as distinct input events by the verified consumer.
A held mouse button must not silently generate hundreds of clicks.
No auto-feeder, paid batch-completion control or background click macro is part of this design.

Provide keyboard focus and one-press activation if the installed native control supports them.
Keyboard and mouse share the same authoritative helper.
Input accessibility cannot bypass the daily cap or turn one accepted action into an undisclosed reward batch.

## Per-click feedback

Every accepted click triggers a short body reaction, a changing expression, crumbs and a visible progress response.
The body reaction needs genuine art frames showing compression, release and settling.
A script that repeatedly scales a single still is not the final animated asset.

Ordinary clicks show a small feeding increment.
Actual resource numbers appear only when a milestone pays.
Do not display a Political Power number on every click when no Political Power was granted.

Healthy feedback may include hearts, warm sparkles and light crumbs.
Hunger feedback replaces those with dry fragments, cracks, darker crumbs, smoke and abrupt facial reactions.
A recovery sequence visibly removes hostile effects as progress returns.

For rapid clicking, use a fixed small pool of particle slots.
Later clicks refresh or reuse those slots.
No click creates an unbounded list of GUI elements or sound instances.
At high input rates, the count must remain exact even when particles are coalesced.
This is presentation coalescing, not loss of accepted clicks.

## Animation families

Separate six body bands from eight expression families and four evolution overlay states.
Reuse compatible facial anchors across body bands.
Do not request a different complete asset for every exact combination of Level and Fullness.

The minimum meaningful motion package includes an expectant idle, happy idle, satisfied idle, hungry idle, starving tremor, angry motion, threatening motion, click compression, click release, milestone celebration, Level-band transition, recovery, weak-cookie collapse and revolt transformation.
Every body band needs appropriate compatible coverage.
Where an overlay or face sheet can genuinely be reused, record that reuse in the manifest.

Use real source frames, a static fallback, frame metadata, a runtime sheet and a review animation.
A review GIF is not an HOI4 runtime asset.
Frame order, loop behavior, duration, anchor, alpha and consuming sprite type must all be explicit.

The transformation sequence locks the feeding input before it begins.
Skipping or closing the presentation cannot cancel the uprising.
The gameplay commit does not depend on reaching the final animation frame.

## Expression priority

Use the following precedence.

```text
committed revolt
weak death sequence
active revolt warning
severe starvation
angry hunger
recovering from threat
ordinary hunger
full and satisfied
active click reaction
healthy or expectant idle
```

A short click reaction can animate within a dangerous condition without briefly displaying a misleading happy face.
A full cookie stays satisfied until the next cycle.
An evolution overlay never masks the active warning.

## Tooltips

The Fullness tooltip states the target, current accepted count, next milestone and whether a bite is paused.
The Level tooltip states lifetime clicks, completed cycles, current maturity status and the next meaningful development threshold.
Keep internal hunger counters and reward-value arithmetic out of the ordinary tooltip.

The reward tooltip names the actual resource, amount, eligibility and paid state.
A locked future reward does not expose a false exact item.
An invalidated reward states its saved replacement or that it was reduced.

A threatened-region tooltip names the actual state or connected state group.
It should explain whether preparation affects the army, industry or civilian exposure.
It cannot claim all three if the action only affects one component.

## Pet and Empire modes

After revolt, remove the clickable relationship surface permanently.
The same event-owned frame may become a compact Empire command window, retaining Fullness and Level but changing the feeding action to real assets and territorial policy.
There is no clickable cookie that grants the former host's rewards to the Empire.

Empire actions are ordinary named operations with costs and targets.
Show at most five primary actions and no more than three active missions.
The main cookie image becomes the leader's state illustration or animation, with a noninteractive boundary.

For an opposing player, the dedicated pet window is gone.
Relevant defence and reconstruction actions appear in a normal decision category.
Do not give every country a duplicate full Cookie interface.

## Sound and reduced motion

Use a short sourced click or crumb sound with a small concurrency limit.
Milestone, warning, death and transformation sounds have separate roles.
Obey existing game and mod audio settings.
Do not play a full sound for every press at extreme input rates.

A reduced-motion setting replaces looping body and particle motion with approved static state assets.
It retains instant bar movement, accepted-click feedback, milestone feedback and visible warnings.
That is an intentional accessibility presentation mode.
It does not justify omitting the requested full animation package.

The static fallback must preserve all gameplay information when animation is unavailable.
Its existence is not proof that the animated requirement is complete.

## Visual acceptance scenes

Required pet scenes include arrival, first click, every milestone, one click below full, exactly full, excess clicks, a large five-digit target, every Level band, every hunger expression, warning, recovery, death and transformation.
Required Empire scenes include full reserve, shortage, selected territory, unaffordable action, active mission and world-end operation.

Review at 1920 by 1080 at scale 1.0, a smaller supported desktop resolution, and a larger resolution with increased UI scale.
Use the installed game's supported scale settings, not invented values.
Include long country and state names, long localized labels, missing or unavailable reward families and a crowded normal game interface.

The required evidence includes pre-change and post-change inspection, full-window and cropped renders, hit regions, hierarchy, warnings and matching scenario comparisons.
A production render with clipping or misaligned controls fails the design's visual acceptance.
Source review or a successful rewrite transaction does not replace these images.
