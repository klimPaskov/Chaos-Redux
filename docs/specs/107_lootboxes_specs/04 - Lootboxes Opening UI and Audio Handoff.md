# 04. Lootboxes Opening UI and Audio Handoff

## 1. Purpose and fixed contract

This document specifies the presentation of Event 107's purchased lootbox, from arrival through five accepted interactions to the genuine reward receipt.
It is a design and implementation handoff, not executable engine code or evidence that native behavior has been verified.
New interface labels, asset identifiers, and descriptive names below are working labels.
Localisation direction describes intended meaning only, with final player-facing wording authored and reviewed during production.
The established rarity names remain Common, Rare, Epic, Mythic, and Legendary in that order.

The purchase costs exactly **50 Political Power**.
Opening and resuming cost nothing.
A country owns at most one purchased pending box, with its purchase-time sealed result, reward evolution snapshot, delivery policy, and accepted click stage saved.
The player interacts with the illustrated chest itself exactly five times.
The fifth accepted interaction asks the core system to resolve the already sealed delivery once, including its one hidden-influence increase, before the final result is presented.
The UI never rolls a prize, pays a cost, changes influence, or grants a reward independently.

The window must feel immediate, physical, and responsive while the campaign remains visible behind a gentle dimming layer.
Its sequence never requires an hour or day of campaign time to pass.
It does not pause the campaign, seize another player's interface, or play another country's opening sounds.
Closing at any point preserves the appropriate pending opening or committed result.

Hidden influence, omen odds, thresholds, recovery formulas, and the connection between openings and later adverse effects are absent from the category, window, tooltips, reward receipt, and Event Details.
Cracks and lid movement show this box's opening progress only.
An omen is never a receipt row, a defective shipment, a reduced prize, or an additional charge.

## 2. Ownership and integration boundary

01 - Event Identity and Core Loop.md owns payment, purchase-time sealing, delivery, persistence, and exactly-once resolution.
02 - Rewards, Probabilities and Evolutions.md owns rarity, Premium selection, bundle construction, eligibility, and reward amounts.
03 - Hidden Influence and Peace Recovery.md owns all concealed consequences.
05 - Decisions, AI and Integration.md owns the ordinary purchase/resume entry points and AI equivalent.
06 - Achievements and Validation.md owns package-wide acceptance and achievement coverage.

If the parent accepts this dedicated window, `chaosx_event_ui_worker` owns its bounded layout and available visual review under `chaos-redux-scripted-gui` and `chaos-redux-subagents`. Any MCP render is optional evidence when the live route is exposed and useful; the worker follows the current retry limit and falls back to source review when a route is unavailable.
The parent retains transaction semantics, gameplay, balance, shared registries, final integration, and completion claims.
The shared event log, Event Details framework, settings interface, and other shared consumers remain parent-owned.
Existing approved reward icons and texticons may be referenced after their actual consumers are inspected.
The opening worker's asset scope is the accepted coverage in Section 11.

## 3. Durable state and presentation state

The core exposes an authoritative owner, purchase identity, lifecycle status, accepted stage, sealed presentation variant, and committed delivery receipt.
It retains the exact reward manifest, provider version, deterministic delivery policy, and reward evolution snapshot behind that presentation contract.
The UI reads only the public subset appropriate to the current phase.
Rarity and contents remain inaccessible to visible elements, tooltips, sound selection, and hidden-panel rendering until resolution permits their reveal.
They must not be accidentally exposed by a selected-state fixture or an untranslated localisation key.

| State | What the player sees and can do | Authoritative behavior |
| --- | --- | --- |
| No pending box | Normal category purchase entry and exact 50 PP cost | Core validates and pays once before opening the window |
| Arrival, stage 0 | Sealed chest enters, lands, and settles | Existing paid purchase remains unchanged |
| Ready, stages 0 to 3 | Chest at the saved damage stage, ready for the next strike | A valid fresh interaction advances exactly one stage |
| Ready, stage 4 | Straining lid and rarity-neutral light | Next valid interaction is the fifth and final one |
| Resolving | Final physical opening begins, further chest input is unavailable | Core completes every sealed component and records one completed opening and influence increase |
| Technical recovery | Restrained unresolved status and a working close control | Core retains the same transaction, finishes only missing components, and withholds successful completion until delivery is whole |
| Result ready | Rarity name, genuine prizes, readable benefits, close control | UI displays the immutable receipt and performs no further grant |
| Closed while pending | Campaign visible, free resume available in the category | Sealed result and stage survive unchanged |
| Closed after resolution | Campaign visible, core permits the next purchase when appropriate | Reopening retained presentation cannot resolve the old purchase again |

An interaction request carries the current purchase identity and expected stage.
The core rechecks ownership and lifecycle before accepting it.
Repeated events, stale controls, rapid input, or an old result window cannot advance a different purchase.
The fifth interaction must not leave a durable state that looks successfully completed but remains eligible for another grant.
All irreversible components are preflighted by the core, which owns ordered application, durable component receipts, and supported recovery when native rollback is unavailable.
If presentation is interrupted after successful commitment, resumption displays the committed result.
If delivery was interrupted before completion, the UI follows the same resolving or recovery state without inventing a sixth claim interaction, rerolling, or showing a partial bundle as a full prize.

Arrival, shake playback position, particles, and sound tails are disposable presentation details.
Save/reload preserves the meaningful stage, not an arbitrary video frame or a half-played sound.
Resume starts from the corresponding stable chest drawing.
It never replays a purchase charge or pretends that replayed animation is another accepted click.

## 4. Implementation questions and evidence limits

Before selecting syntax or playback mechanisms, inspect the current native GUI documentation, a close vanilla example, and the actual Chaos Redux consumer through the current reference workflow in `AGENTS.md`.
Use MCP only to answer a concrete question: make the initial read-only call and at most one useful corrected retry, then continue with local source and installed documentation if the route is unavailable or inconclusive.
Tool availability and a successful preview do not establish native runtime behavior.
Source review can establish what the implementation requests; it cannot be reported as observed animation, audio, multiplayer, save, or live timing behavior.
No agent should launch HOI4, request a user-run session, or wait for live-game evidence.

| Capability to establish | Required evidence | Permitted presentation adaptation |
| --- | --- | --- |
| Immediate opening after purchase | Source path and any available behavior observation that a local window appears without campaign-time advancement | Open an event-owned native window through a verified existing attachment or entry pattern; record native behavior as unobserved when no live observation exists |
| Five distinct real-time responses | Native input and frame-playback contract plus available stage evidence; live timing remains user-owned | Keep five visible accepted responses; do not substitute a one-click reveal or a campaign-day wait |
| Animation completion and input timing | Exact supported callback, control state, or real-time gating behavior from current source and references | Use documented fresh-press behavior and explicit busy feedback; do not invent support |
| Close, Escape, and resumption | Native close behavior, Escape handling, saved stage, and preserved purchase identity in source; runtime behavior remains a separate claim | Keep a real close control and the required Escape behavior; do not claim runtime parity from source alone |
| Optional keyboard activation | Verified native focus and activation behavior if the optional route is implemented | Add supported keyboard operation without inventing shortcuts or treating a held key as five actions |
| Local multiplayer interface and audio | Source owner/context rules; actual isolation requires separate-client live evidence | Use local presentation bindings, with no global visibility or pause workaround; do not claim isolation from source review alone |
| Optional reduced-motion option | Existing supported preference or an explicitly accepted event-owned control | Use five discrete source-drawn stages and restrained transitions, never automatic opening |

If current source and references show that the engine cannot support a distinct visible response for each accepted interaction, the required behavior remains unresolved and must not be silently reduced.
An unavailable preview or live-game observation is an evidence limitation, not proof that native support is absent or an automatic source-completion gate.
An automatic single-click reveal, five daily decisions, a GIF in place of a runtime animation, or a long unskippable cutscene is not an acceptable adaptation.
Optional keyboard and reduced-motion enhancements remain accurately marked as unverified until their native route is established.
Assess these optional enhancements separately from the required pointer, close, Escape, five-stage, and local-presentation gates.
Do not manufacture engine fields or treat a source-only mockup as a completed interaction.

## 5. Composition and screen sizes

Use a restrained native HOI4 frame with dark painted metal, subtle period texture, and clear typography.
The chest is the focal point, with generous clearance for its lid, dust, and short burst.
Avoid a storefront, inventory grid, progress dashboard, ornate card collection, or large panels of instructions.
The campaign remains recognizable through a translucent dimming layer.
This layer cannot intercept controls outside the declared modal context or interfere with another multiplayer client.

At 1920x1080 and UI scale 1, begin with an approximately 760x700 central composition and a 512x512 animation canvas.
These are reference targets to verify against the actual native frame and painted bounds, not assumed engine dimensions.
Reserve a compact header, the chest region, a concise instruction or status line, a distinct close control, and a result area that replaces the opening instruction when needed.
The result may expand within the same frame rather than push the chest or close control offscreen.

| Review target | Layout requirement |
| --- | --- |
| 1920x1080, scale 1 | Full chest canvas, clear lid/burst clearance, readable receipt without excessive empty space |
| 1600x900 and 1366x768 at supported scales | Smaller margins and shorter decorative frame, with intact controls and readable text |
| 1280x720 if supported by the mod | Compact result composition and bounded scrolling, with no clipped close control or hidden prize row |
| Higher resolution and larger supported UI scales | Native scaling preserves glyphs, art proportions, and hit regions together |
| Long names and localisation stress | Real wrapping or scrolling within declared bounds, never smaller unreadable text |

Measure painted artwork, transparent padding, logical containers, rendered glyphs, and effective click regions separately.
A centered texture box does not prove a centered label or clickable chest.
Do not enlarge a render or change UI scale to conceal defects.
The supported matrix becomes explicit after native consumer inspection.
Any proposed exclusion of an expected resolution must be recorded for parent review.

## 6. Chest identity and concealed rarity

The shell design is a substantial period crate with timber, reinforced corners, straps, hinges, and a convincing lock.
Its opening reactions use the same identity and stable center across all five stages.
Keep the principal chest body inside a consistent footprint while the lid, fittings, dust, and minor particles provide secondary movement.

Use four presentation variants to cover independent visible evolution features:

| Variant | Distinguishing feature | What it must not imply |
| --- | --- | --- |
| Ordinary, standard appearance | Restrained timber and practical iron fittings | Common-only contents |
| Premium, standard appearance | More elaborate reinforcement and recognizable premium hardware | Any guaranteed rarity or bonus count |
| Ordinary, Chaos Loot appearance | Subtly unusual construction and impossible but coherent joinery | High influence, an omen, or a particular reward tier |
| Premium, Chaos Loot appearance | The same Chaos-era vocabulary combined with Premium hardware | Legendary certainty or a more cursed individual box |

The shared framework uses 200, 400, and 600 Chaos as eligibility thresholds for Premium Boxes, Bonus Drops, and Chaos Loot respectively.
The interface follows the shared owner's actual enabled and unlocked state, including its pacing, rather than unlocking features from a raw Chaos comparison.
Once Premium Boxes is active, Premium is an automatic random upgrade on the same purchase row and for the same 50 PP.
Ordinary boxes retain a real nonzero chance.
Once Bonus Drops is active, the result supports its expanded sealed bundles while the opening retains five interactions and concealed contents.
Once Chaos Loot is active, eligible new purchases can use the matching shell appearance without revealing influence or the rolled reward family.
Freeze the chosen shell, complete reward manifest, delivery policy, and relevant reward evolution snapshot at purchase.
A later unlock, setting change, or fall in global Chaos cannot transform that paid box's presentation or replace its sealed contents.

All pre-reveal light uses the same restrained neutral vocabulary across rarities.
Avoid rarity-colored seams, tier-specific particles, more luxurious sounds for a sealed Legendary, or damage that varies with hidden influence.
Any of the five tiers can emerge from every eligible shell.

## 7. Five-stage motion and timing

The following frame counts are initial art-planning targets for 512x512 frames.
Tune them after native playback and usability review.
The artist must justify any lower count through smooth native-size evidence, not production convenience.
All meaningful changes require real source artwork or source layers.

| Sequence | Initial frame target | Timing band | Physical reading and sound anchor |
| --- | --- | --- | --- |
| Arrival | 10 to 16 | About 0.4 to 0.65 seconds | Quick rise, modest overshoot, weighted landing and soft settle |
| Accepted click 1 | 8 to 12 | About 0.25 to 0.45 seconds | Front face compresses, returns, then rocks with a dry tap |
| Accepted click 2 | 10 to 14 | About 0.3 to 0.5 seconds | Stronger lurch and rebound, with metal and hinge rattle |
| Accepted click 3 | 12 to 16 | About 0.35 to 0.6 seconds | Seal splits or a clear crack appears, followed by dust and a heavier landing |
| Accepted click 4 | 14 to 18 | About 0.4 to 0.7 seconds | Lid strains, fittings move, neutral light escapes, then the chest settles under tension |
| Accepted click 5 | 18 to 24 | About 0.6 to 0.95 seconds | Latch fails, lid springs, body rises and lands, then the fully open result is revealed |

Use a consistent verified playback rate, initially around 24 to 30 frames per second, and record the exact final rate per sequence.
The fifth interaction begins a larger physical opening, but rarity art and its distinctive sound enter only after the chest visibly opens.
Core delivery is already complete before rarity art, its sound, and the successful result presentation are allowed to appear.
The closing control remains available through the flourish.

Common, Rare, Epic, Mythic, and Legendary each receive their own reveal family, initially around 12, 14, 16, 20, and 24 frames respectively.
Their effective flourish bands range from roughly half a second to just over one second after opening, with higher tiers richer and slightly longer.
Legendary is the strongest presentation and Mythic the second strongest.
All remain responsive and leave an ordinary static result the player can read.

## 8. Hit regions, input rhythm, and closing

The chest's stable painted body is the primary interaction surface.
Inspect whether the native consumer supports alpha-aware input before using it.
If it uses rectangles, align the visible interactive face and verified native hit region so the player strikes the chest, not transparent dust or a large invisible background box.
Any composite control solution must avoid overlap that sends one press twice.
Hover feedback and any enabled native keyboard-focus treatment identify the actual usable face without suggesting a separate confirmation button.

Accept one deliberate fresh press per stage.
A held mouse button, held key, window-opening press, stale focus event, or repeat callback must not consume several stages.
A one-input buffer is desirable only when documented native support can guarantee its behavior.
Otherwise show a brief consistent busy treatment while a response resolves, with no stage advance and no successful-impact sound for rejected input.
Do not let a queued batch silently skip the player's five visible interactions.

Closing or Escape before the fifth accepted interaction retains the purchase and saved stage.
The category offers a free resume action through its normal entry point, with the paid status clear and no second purchase available.
Resuming starts from the appropriate stable stage, with a quiet optional presentation cue rather than another purchase sound.
Closing after the fifth interaction dismisses only the presentation and preserves either the completed receipt or the core's unresolved recovery state.
Reopening a retained receipt cannot produce another reward, influence charge, achievement increment, or reveal-triggered gameplay effect.

Disable purchase for insufficient PP, an existing pending opening, an in-flight authoritative purchase, or an invalid owner context, using only truthful public reasons supplied by the core.
If certified delivery is temporarily unavailable, use restrained technical availability feedback supplied by the core without exposing sealed contents or internal provider identifiers.
Disable chest input while resolving or when its purchase identity is stale.
Never explain disabled controls through hidden influence, omen state, or private peaceful-recovery conditions.

## 9. Result and bundle readability

The result presents the rolled rarity by its established name, an unmistakable tier symbol or shape as well as color, and the complete genuine delivery receipt.
Suggested visual accents are restrained neutral for Common, blue for Rare, violet for Epic, a distinct warm red or copper treatment for Mythic, and gold for Legendary.
Final colors must be checked against existing HOI4 art, contrast, and each other.
These accents appear only after opening.

Show concrete awarded amounts and meaningful destinations or durations where relevant.
Equipment, fuel, manpower, experience, research help, construction, and temporary benefits should use the existing truthful naming and icon conventions of their owning systems.
Each receipt entry states the concrete benefit and its usable amount or scope.
Avoid hidden modifier identifiers, raw localisation keys, or implementation history.

Use a compact receipt of approximately one to four visible component groups, with a supported bounded scroll region for longer equipment manifests and supporting detail.
The layout must show that further rows exist and make every prize inspectable.
Related amounts may be grouped only when the grouping preserves the actual benefits and destinations.
Never omit a bonus because it does not fit the panel.
These rows are receipt records, not a new resource dashboard or a way to expose concealed mechanic values.

The receipt comes from actual successful delivery, including real receiving support required by the deterministic sealed policy.
Opening-time capacity calculations can change the amount of that support without changing the purchased reward.
Display this support beneath the related component so the ordinary four-group bundle remains readable.

| Delivered family | Receipt detail required |
| --- | --- |
| Fuel and equipment | Full actual quantity, concrete model or reserve, and any real receiving capacity added for that award |
| Experience | Exact service and usable quantity, including genuine storage or cap support and meaningful usage conditions |
| Buildings and construction | Actual state and improvement, retained awarded value, and any legal capacity support used |
| Research assistance | Exact charges, strength, supported scope, and any real duration beginning at reveal |
| Timed support | Full retained duration or contribution, actual application timing, and any supported queue or extension |

Capacity-support conditions must be truthful and must not suggest that unused awarded value can be deleted when support retires.
A retained queued program can show its actual timing, but material contents cannot become a voucher, pending claim, or separately redeemed reward.
The receipt adds no claim button and never asks the player to choose a replacement for a sealed component.

After a short readable flourish, the result remains until dismissed.
There is no automatic dismissal that can hide the player's rewards.
The closing action has no economic effect.
The next purchase returns through the existing category rather than a new store or inventory screen.

## 10. Accessibility and sensory restraint

Use consistent high-contrast native text, stable control placement, and non-color tier and control-state cues.
Keep meaningful information readable without sound.
Avoid full-screen flashes, rapid repeated flicker, exaggerated camera shake, or long particles obscuring the reward.
The dimming layer should support the chest rather than black out the campaign.

If a verified reduced-motion preference or an accepted event-owned control is available, retain the same five accepted interactions using source-drawn staged damage, short restrained responses, and a clear final opening.
Do not substitute a static picture for the requested normal animation.
Reduced motion must not change the sealed result, PP cost, influence outcome, or timing of core delivery.
Keyboard focus and activation are added only through a proven native pattern, with visible focus and repeat-input protection.

## 11. Required asset coverage

The following planning row ids define the bounded opening presentation package.
Each production manifest expands repeated families into exact variant and phase rows.
They are not final sprite names.
The parent registers stable runtime names and paths before art production.

| Row | Required output | Coverage and consumer |
| --- | --- | --- |
| LB-REF-01 | Opening composition reference | Normal sealed window, damaged Premium variant, full result, crowded bundle, and compact layout views |
| LB-ICON-01 | Restrained standard category icon | One separately authored category-family icon, only if the accepted native category uses it |
| LB-SHELL-01 | Ordinary standard chest family | Arrival, saved rests 0 to 4, five distinct click responses, fully opened static state |
| LB-SHELL-02 | Premium standard chest family | Same complete phase set, recognizable Premium hardware, no rarity leakage |
| LB-SHELL-03 | Ordinary Chaos appearance | Same complete phase set, public evolution appearance only |
| LB-SHELL-04 | Premium Chaos appearance | Same complete phase set, preserving both shell distinctions |
| LB-TIER-01 to 05 | Five distinct rarity reveal families | Common, Rare, Epic, Mythic, Legendary, with real frames and static post-reveal art |
| LB-UI-01 | Bounded decorative window layers | Only accepted background, framing, dim layer, or ornaments that cannot use inspected native assets |
| LB-UI-02 | Required native control states | Close, chest hover/busy, any enabled focus state, result navigation, and disabled treatment as actual consumers require |
| LB-RECEIPT-01 | Existing reward-icon crosswalk | Exact approved icon and texticon references for each receipt reward family and any real receiving support |
| LB-AUDIO-01 to 12 | Opening and tier sound families | The cue table below, with licensed sources, derivatives, and local playback consumers |

107_lootboxes_asset_prompt.md also carries the accepted package rows LB-REPORT-01 to 04 for the initial and three evolution reports, LB-DEC-01 to 02 for purchase and resume decision icons, and LB-ACH-01 to 04 for achievement triplets.
Their native consumers remain the ordinary report, decision, and achievement systems.
06 - Achievements and Validation.md and 107_lootboxes_achievement_prompt.md own the exact achievement keys, eligibility, and full production details.
These additions do not expand the opening window's controls or disclose sealed rarity and hidden consequences through report art.

No decision category picture is commissioned.
The category-picture eligibility rule excludes its use where the current category or its attached interface is complex.
Keep the category restrained and use only the appropriate standard icon after inspection.
Do not add a picture merely to fill space or duplicate the dedicated opening window.

UI control states need not all become new custom textures if the inspected native family already supplies them.
Every reused asset still needs its exact consumer and state mapping.
Decorative art cannot contain fake buttons, receipt text, rarity labels, or dynamic values.

## 12. Frame production and runtime texture budget

Start with an accepted seed and explicit per-phase frame plans.
For every frame, record motion state, changed drawing, anchor, source lineage, and loop or terminal role.
Subsequent edits preserve identity, canvas, palette, perspective, material character, and unchanged regions.
An animated squash or moving lid must exist in source frames, not be manufactured by moving or filtering a single still.
Shared motifs within the chest family are allowed, but every delivered variant must pass its own complete stage and silhouette review.

Use transparent source and processed PNGs where the consumer requires alpha.
Keep a common contact anchor and enough canvas margin for the lid and burst.
Produce horizontal sheet PNG/DDS, static fallback PNG/DDS, native-size contact sheets, and review-only GIFs.
The final engine asset is the verified frame sheet and native sprite binding, never the GIF.

At 512 pixels per frame, a 32-frame horizontal sheet reaches 16384 pixels.
No texture side may exceed that limit.
Keep each short phase in its own sheet rather than combine the whole opening into an oversized strip.
If an accepted longer animation requires strip assembly, use the frame-animation skill's synchronized vertical-strip method and verify seams and playback alignment.

The complete four-shell family has a material texture-memory cost at this canvas.
Measure delivered byte sizes and runtime behavior before accepting the final size and frame budget.
A smaller verified native canvas, tighter legitimate framing, or reuse of appropriate native chrome can be accepted when the large central composition, detail, smoothness, and five responses remain intact.
Do not assume unused sheets are unloaded.
Use the current 2D texture delivery contract for these UI assets.
Required normal-animation quality cannot be traded away silently for memory savings.

## 13. Audio cue plan

All cues derive from licensed physical recordings or licensed authored sound-effect sources.
They are short UI feedback, not a super-event soundtrack.
No soundtrack reuse, uncited effect, synthesized beep, test tone, or oscillator stand-in is assumed.
Final timing follows accepted animation frames, not a game-day scheduler.

| Row | Cue family | Initial duration direction and synchronization |
| --- | --- | --- |
| LB-AUDIO-01 | Purchase and arrival | Short delivery/landing accent, about 0.3 to 0.6 seconds, once after confirmed purchase |
| LB-AUDIO-02 | First accepted strike | Dry timber tap and light fitting response, about 0.1 to 0.25 seconds, at visible compression |
| LB-AUDIO-03 | Second accepted strike | Heavier knock and metal rattle, about 0.15 to 0.35 seconds, aligned to impact and rebound |
| LB-AUDIO-04 | Third accepted strike | Seal crack, heavier landing, small debris, about 0.2 to 0.45 seconds |
| LB-AUDIO-05 | Fourth accepted strike | Hinge strain and restrained pressure release, about 0.25 to 0.55 seconds, still rarity-neutral |
| LB-AUDIO-06 | Final physical opening | Latch break, springing lid, and landing, about 0.4 to 0.8 seconds, distinct frame anchors |
| LB-AUDIO-07 | Common reveal | Modest bright physical accent, brief and satisfying without implying a bad prize |
| LB-AUDIO-08 | Rare reveal | More resonant layered metallic or glass accent after full opening |
| LB-AUDIO-09 | Epic reveal | Richer layered resonance and short sparkling tail |
| LB-AUDIO-10 | Mythic reveal | Distinct deeper and brighter layers, second-highest richness |
| LB-AUDIO-11 | Legendary reveal | Most exceptional short layered flourish, clear final resolution, controlled peak level |
| LB-AUDIO-12 | Optional resume/close feedback | Restrained native or licensed cues, no purchase replay and no gameplay meaning |

Small strike variations may use two or three licensed alternatives within the same physical family.
Use a documented cosmetic selection method independent of sealed reward selection.
Variation, gain, pitch character, or repetition must not encode rarity, influence, omen state, or future bundle count.
No sound plays for an unaccepted stage as though it succeeded.

Respect the player's existing effects-volume and mute settings through the verified local UI audio route.
Do not route these cues through global super-event audio ids or change shared music settings.
Control overlap so rapid valid interactions do not stack several loud tails, and stop or fade local tails appropriately on close.
The strongest rarity should sound richer rather than dangerously louder.
Check final codec, sample rate, channels, and gain against the exact installed UI-sound precedent rather than borrowing a unit-voice preset.

## 14. Audio and art production handoff

The production worker supplies each source page and download, creator, title, retrieval date, exact licence and permitted modifications, attribution text, immutable source file, and derivative recipe.
Record source and final hashes, trim/fade/mix steps, final format, duration, peak/clipping measurements, and the cue's animation-frame anchors.
Every layered effect must account for every audible source and compatible use terms.
An attribution row alone does not establish that a particular derivative is licensed or sounds correct.
If a required cue cannot be sourced, preserve the visual work and report that cue as blocked.

The asset prompt is 107_lootboxes_asset_prompt.md.
Production follows current event-assets, frame-animation, and scripted-GUI contracts.
Use the current reference catalogs and actual consumer definitions before finalizing dimensions, alpha, sprite states, and sound delivery.
Preserve source/processed/runtime separation and exact ImageGen request lineage.
Keep active evidence under the event workspace, then promote durable provenance, coverage, and accepted handoff facts at actual event completion.
This planning task produces no image, animation, audio file, provider job, or final art claim.

## 15. Reference and evidence workflow

Before implementation, create or select accepted composition references for the opening, materially different result states, and compact layout.
Map every reference region to native ids, painted bounds, usable interiors, controls, assets, and state bindings.
Record justified native adaptations.
The parent may accept a direction within the existing user-authorized design without inventing a new approval gate.

Use targeted GUI MCP inspect/render calls when their live schemas are exposed and the results answer a concrete layout question.
Apply the current `AGENTS.md` limit: one initial read-only call and at most one useful corrected retry, followed by source review if the route is unavailable or inconclusive.
For a new window with no baseline, record that fact and inspect the first renderable native container when available.
Review returned images when available, correct confirmed defects, and keep exact source and scenario identities.
The optional rewrite route is not a substitute for source review, and its failure does not forbid direct application of an already authorized reviewed edit.

Required scenario families include all four shells at stages 0 to 4, each fifth-click opening, all five rarity results, a long bonus bundle, resumed pending stages, a resumed committed receipt, insufficient PP, busy input, stale ownership, and closing during each phase.
Include long labels, missing-localisation diagnostics, click regions, normal/hover/disabled states, any enabled focus state, and the declared resolution/scale matrix.
Use coherent route-valid fixtures, with stress cases identified separately.

Add results near resource caps, changed building or research destinations, real receiving support, and queued timed benefits under the certified provider policy.
Compare the sealed manifest to the final delivery receipt and visible component groups.
Cover an evolution threshold reached before shared unlock, a disabled shared evolution, access granted after an existing unlock, and an unlock while a paid box waits.
The pending box retains its purchase snapshot in every case.

The runtime handoff also names interruption cases at every saved stage, immediately before final acceptance, and after core commitment but before the result is visible.
Pair the result with the core receipt in each case.
Check two human countries opening different boxes concurrently, an AI opening with no human window, observer or changed-country context, and simultaneous control attempts where the game supports shared country control.
Audio cases include muted effects, reduced effects volume, interrupted tails, resume, and rapid rejected input.
None may leak another country's sound, repeat a purchase cue, or alter delivery.

Compare matched before/after artifacts when those artifacts are available; do not treat a missing optional render as a source defect or completion gate.
Review centering, clipping, margins, typography, alpha seams, lid clearance, background coverage, scrolling, state visibility, and hitboxes.
When a render is available, inspect the image itself; a passed boolean or artifact path does not replace visual review.
If rendering is unavailable, inspect source geometry, assets, text, and state wiring and record that visual behavior was not observed.

MCP and offline previews do not execute campaign transactions or prove multiplayer isolation, save/reload behavior, audio playback, input callbacks, or live timing.
Source review can establish the implementation path, while runtime claims require actual user-provided observation. Agents do not launch HOI4, request a run, or wait for that evidence; its absence limits the behavior claim without gating otherwise complete source work.
Never claim these checks have run in this planning package.

## 16. Completion and blocking findings

The presentation source is complete only when every accepted asset row has its source, final runtime registration, actual consumer, conditional binding, and current review record.
The parent also needs the GUI worker's reference mapping, available matched visual evidence, audio source/format evidence, and the core owner's source evidence that displayed results match the committed receipt.

Acceptance requires five distinct accepted responses, rarity-neutral pre-reveal states, full genuine bundle and capacity-support readability, saved pending progress and reward snapshot, free resume, one complete final outcome, and local-only interface/audio without campaign-time dependence.
It also requires complete normal animation, static fallbacks, working closing behavior, truthful disabled causes, and no hidden-system disclosure.

If current source or a useful check confirms missing native real-time support, unresolved ownership, unsupported required input, inadequate texture performance, absent licensed audio, invalid alpha, or an unreviewed accepted row, report that concrete blocker.
An unavailable optional MCP route or absent live-game observation is recorded as a limit on the corresponding claim; it does not by itself block otherwise complete source work.
No fallback may silently remove the tactile sequence or change its gameplay boundary.
Report every parent-accepted adaptation and any optional accessibility capability that remains unavailable.

