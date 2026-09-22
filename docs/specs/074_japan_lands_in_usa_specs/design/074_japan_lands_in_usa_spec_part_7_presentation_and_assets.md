# Part 7: Presentation and asset direction

## What the player needs to understand

The first news report announces an established Japanese mainland front.
The Japanese country report identifies the actual landing region, the opening force, the finite support window, and the first useful objective.
The American warning identifies the affected coast and the emergency actions available.
Neither report implies that Japan obtained naval supremacy or that the United States had agreed to transfer California.

Use the selected geography in the text.
California-specific wording is valid only when the landing actually includes California.
Oregon and Washington fallbacks need equally complete wording.
At the largest opening, describe a multi-region western invasion only when the actual footprint supports that statement.
No report should advertise units or aircraft that are still reserved or awaiting capacity.

## Writing direction

The event and evolution names in the user's brief are accepted design names.
Other names in this package are working labels for production.
Final report titles, decision wording, achievement names, super-event text, quotations, and button labels require the writing pass.
Technical asset identifiers never become finished player-facing text by accident.

Keep the tone consistent with Chaos Redux without treating the invasion as harmless.
Japanese acknowledgements can refer to the unexpected scale of the opportunity.
American acknowledgements can use restrained irony about the Pacific no longer being an adequate defense plan.
Do not write those directions verbatim as final lines.
The strategic information must remain clear beneath any humor.

The event can occur under different governments and leaders.
Avoid mandatory references to a particular emperor, president, party, or historical year.
Use the current country and character localisation only when it is supported and appropriate.
Do not portray ethnic Japanese American civilians as an invading force or turn mass internment into an optimal emergency-defense action.
Civilian evacuation and wartime administration can appear in contextual reporting without inventing a compulsory population system.

## News sequence

| Beat | Condition | Main information |
| --- | --- | --- |
| Initial landing | Successful committed footprint and actual opening army | A Japanese army is already operating on the selected American coast |
| Wider western campaign | A second major coastal operating region is genuinely active | Several American approaches now require defense |
| Inland advance | The sustained inland-route milestone is achieved | The fighting has moved beyond a coastal enclave |
| Coastal recovery | The defined original-coast recovery condition is satisfied | The special Japanese mainland entry has been defeated or closed |
| Japanese continental result | Japan remains a material occupier when the United States capitulates in the existing war | The actual war outcome, without claiming Event 074 scripted the peace |

Use once-only receipts for strategic beats and a 30-day spacing target between nonterminal follow-up news.
The initial landing and a genuine terminal result need not wait for that spacing rule.
Minor changes in a province, port damage, a cancelled decision, or a single supply delivery do not deserve global news.
Country reports and mission tooltips carry those details.

Occupation administration and evacuation flavor must be tied to actual control and fighting.
Do not announce a city's evacuation after it has already been recovered or claim a named port was destroyed when the game records it as usable.
Where the exact city is unavailable, use a truthful regional description.

## Interface choice

Use ordinary decision categories with a clear category picture, targeted actions, and native mission progress.
The map, battle planner, air view, and supply view remain the operational interfaces.
There is no separate resource wallet, occupation-management minigame, state-puzzle screen, or full custom window.

Japan has four decision families and the United States has five.
No country shows more than two concurrent event missions.
Display working registered access points and remaining special-support time as the only custom operational readings.
A decision can expose its own remaining lifetime allowance in a tooltip without creating a permanent dashboard counter for every resource.

The implementation must verify the category-picture consumer against the installed version and matching vanilla references.
This package does not claim a nominal image size alone proves the picture will display correctly.
A missing native consumer is a specific presentation blocker, not a reason to build an unrelated scripted GUI.

## Temporary national spirits

At most one event-owned temporary national spirit is visible for Japan and one for the United States.
A Japanese support spirit may communicate the remaining organized support period.
An American emergency-coordination spirit may communicate an active supported operation.
The scope of their actual modifiers must match the design.
An informational national spirit must not conceal a worldwide combat bonus that the text describes as local.

Do not use a separate national spirit for each tier, port, mission, aircraft group, or decision.
Swap or update the event's existing slot when appropriate.
The maximum of three simultaneous event-owned national spirits per country remains respected even if later approved work adds one necessary state.

## Visual identity

Use generated illustrations for this fictional invasion.
The artwork may adopt HOI4's period news and report treatment, but it must not be attributed to a real wartime photograph of a landing that never happened.
Archival material can inform uniforms, transport equipment, port buildings, and coastal geography after source and rights checks.
A source that depicts a different location or conflict must not be presented as evidence of this campaign.

At native size, the composition should show a few readable elements: an unloading operation, a port approach, military vehicles moving off the waterfront, or defenders preparing a western transport junction.
Avoid a dense collage of flags, maps, aircraft, city landmarks, and tiny soldiers in one icon.
Use imagery appropriate to the actual region.
Do not make the Golden Gate Bridge the universal image for every Pacific fallback.

No new country flag, leader identity, unit model, equipment family, map counter, or focus-tree icon is required.
Existing Japanese and American units and commanders use their existing valid assets.
Static art is sufficient for this event.
Animation or a custom 3D unit would require a separate demonstrated gameplay or presentation need and an approved production contract.

## Planned visual manifest

All rows describe planned outputs, not existing or generated files.
The asset worker must inspect the exact native consumer and matching reference family before production.
The dimensions below follow the supplied project rules, with category pictures explicitly requiring consumer confirmation.

| Family | Planned subjects | Count | Native target and treatment |
| --- | --- | ---: | --- |
| Japanese and American reports | Landing command, mainland warning, campaign aftermath | 3 | 210 × 176, sepia report treatment and required alpha/card processing |
| News reports | Initial landing, wider western front, inland advance, coastal recovery | 4 | 397 × 153, black-and-white news treatment |
| Super-event scene | A genuinely large multi-region mainland invasion | 1 | 457 × 328, readable period military scene |
| Japanese decisions | Receive forces, repair unloading, repair corridor, prepare advance | 4 | 32 × 32 symbolic icons |
| American decisions | Mobilize, prepare city, repair rail, prepare counterattack, protect port | 5 | 32 × 32 symbolic icons |
| Missions | Consolidate, connect, advance inland, retain defense, recover coast | 5 | Match the native decision/mission icon consumer, nominally 32 × 32 |
| Category icons | Japanese campaign and American emergency defense | 2 | Inspect matching category-icon consumer before fixing export dimensions |
| Category pictures | Japanese operating coast and American western defense | 2 | Inspect exact consumer, nominal reference 114 × 101 is not sufficient evidence |
| Event-owned spirits | Finite Japanese support and American coordination | 2 | 64 × 64 idea icons |
| Achievements | Five distinct subjects, each in three required states | 15 | 64 × 64 final achievement tiles |

This yields 43 planned runtime image files if every listed family remains necessary after consumer verification.
The two national-spirit images are required only if the implementation actually uses those visible spirits.
Removing an unused spirit removes its asset request and updates the manifest, without claiming that missing art has been completed.
The continental-capitulation report can reuse the aftermath report art with correct text.
A different reuse must be documented against the actual consumer.

## Asset production and provenance

Use `docs/assets/074_japan_lands_in_usa/` as the event workspace.
Read the supplied asset skill and the reference root's `README.md`, `CATALOG.md`, matching family contact sheets, and the exact consumer examples before creating art.
The referenced root is under the repository's `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/` directory.
The source pack's absolute Windows path identifies its original location, not a mounted folder in this session.

For category pictures, inspect `icons/decision_categories/pictures/` and its `contact_sheet.png`.
If the required contact sheet is absent in the implementation environment, the asset worker must create the labeled reference sheet and update the reference indexes before production.
Do not generate a guessed icon and then call it a verified category picture.

Ordinary DDS exports use the prescribed conversion pipeline and actual-byte validation.
Achievement icons use the separate achievement processor and the unchanged project templates.
Every promoted runtime image needs its source mode, source or generation record, crop and alpha decisions, native dimensions, intended consumer, and verification result.
Do not discard blocked source work or reference records as a cleanup shortcut.
Once accepted runtime files and durable provenance exist, remove disposable duplicates under the asset skill's closure rules.

## One tier III super-event

The working presentation slot is the first realized multi-region tier III invasion.
Its condition requires at least 90 percent of the authorized tier III immediate army to have actually been issued, at least three working Pacific ports, and operating access in at least two Pacific mainland states.
Selection of tier III alone is insufficient.
The same episode can satisfy the gate later through normal conquest, but it can display the super-event only once.

This is a presentation gate, not a restriction on the user's army grant.
A tier III opening with only one legal operating region still receives its promised force and ordinary news.
There is no second super-event for acknowledging it, losing the bridgehead, or later completing the same gate again.

No final title, quotation, slogan, button text, or audio track is selected in this package.
Those are research blockers under the supplied super-event skill.
Text and audio specialists must produce checked candidates and a final sourced package before the implementation registers the presentation as complete.
Use sourced audio within the skill's 60–120-second target and do not exceed 120 seconds without approval.
Check the rights of both the composition and the recording.
Do not substitute synthetic audio, a default soundtrack, or an unverified historical speech merely to fill the slot.

The visual can be generated as fictional period artwork.
The quote must have a traceable source and context that fits the selected subject without falsely implying that a historical speaker described this fictional landing.
The design's working evolution name does not authorize an unresearched super-event title.
The dedicated prompt defines registry, sound, and localisation handoff requirements.
