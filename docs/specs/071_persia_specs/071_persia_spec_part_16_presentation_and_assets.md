# 071 Persia: presentation, visual assets, and 3D brief

## Presentation hierarchy

The opening receives one major news event. Regional milestones and political disputes use news or country events according to their audience. Ordinary construction progress stays in the decision interface. A player should not receive a global announcement for every workshop or shipment.

Final player-facing titles, descriptions, options, focus names, achievement wording, quotations, and slogans are not written in this planning package. The following entries provide their subject, tone, audience, and visual direction. The localisation worker must write final copy after the source and implementation checks.

## News and country-event directions

| Moment | Audience | Text direction | Image direction |
|---|---|---|---|
| Imperial restoration | Global news plus relevant diplomatic recipients | Explain the government continuity, declared ambitions, and actual new military strength | Contemporary Iranian ceremony with visible military mobilization, adapted to the current executive |
| First durable satrapy | Regional and global milestone | Explain the accepted charter and the subject's retained institutions | Modern administrative delegation and a distinct local identity |
| Mesopotamian settlement | Regional news | State the actual political result and controller | Modern forces and administration in the settled region, not an ancient battle |
| Persepolis institution completed | Global milestone | Explain the restored site's contemporary use without claiming the ruins became an intact ancient city | Conserved ancient setting with clearly modern ceremonial facilities |
| Guard command established | Persian military event, later news for major Evolution II milestone | Explain the force's role, recruitment limits, and current form | Contemporary guards with researched visual references and fictional imperial insignia clearly distinguished |
| Gulf settlement | Regional news | Describe actual ports, access, and protection commitments | Working naval base, escorts, and transport, not an unearned carrier fleet |
| Route conclusion | Global milestone and eligible super-event | State the completed institutions and their limits | Route-specific assembly, command system, or industrial bloc |
| Imperial guarantee honored or broken | Relevant states and global news when significant | Identify the actual commitment and response | Diplomacy or military mobilization relevant to that commitment |
| Major fragmentation | Global news, optional earned collapse super-event | Describe the surviving center and actual breakaways | Divided modern administration, withdrawn banners, and dispersed forces without invented atrocities |

Country-level option tone can be dry or ironic where the project style supports it. It must not make serious political consequences unreadable. Historical references need a source check before becoming an allusion or quotation.

## Super-event gates

The route conclusions can each support a distinct super-event after the relevant institutional result has remained intact for 180 days and legitimacy is at least 80. Achaemenid presentation centers on the chartered network. Sasanian presentation centers on the functioning command system. Modern presentation centers on the industrial and security bloc.

A collapse super-event is reserved for an empire that previously earned a route super-event and then loses its central institution plus a substantial part of its settled network. A small early failed restoration receives news only. The collapse super-event can fire once.

Each planned super-event requires separate researched title direction, description, cultural reference or verified quotation, image, and a distinct licensed audio choice. This package does not select unresearched final music or quotes. Missing research is a blocker, not permission to ship placeholders.

## Identity assets

The same Iranian country needs an opening imperial identity and route-appropriate political variants. Produce all relevant ideology names, cosmetic identities, and flag ladders after reviewing installed content. Preserve correct country history and a valid leader under each supported transition.

Historical flag designs require reliable references and a faithful flat ImageGen reconstruction. Alternate-history route flags also use ImageGen, but are documented as invented designs. Do not claim that a modern rectangular national flag is an attested ancient imperial standard without evidence.

Flags require normal 82 by 52, medium 41 by 26, and small 10 by 7 outputs under the supplied asset rules. Inspect the actual pipeline before conversion. Geometry, color, orientation, and symbols must be compared manually to the chosen design reference. No waving cloth, scenery, perspective, fake lettering, or gradients.

## Portraits

Use the existing living Iranian and regional roster wherever suitable. New real leaders require sourced identity and chronology. A fictional official must be clearly documented as fictional. An institutional image is acceptable when the government is intentionally represented by an institution.

All portraits go through `chaosx_portrait_creator`. Grounded subjects require a sourced head-and-shoulders reference with identity preserved. Leader output is 156 by 210. A separate 65 by 67 adviser output is required only when that actual consumer exists. Final portrait styling uses the user's RunPod workflow. Do not silently replace it with an unrelated local pipeline.

The current archive contains no portrait reference images or installed roster. This plan does not claim to have inspected or produced them.

## Asset families

| Family | Required scope | Native target from supplied rules |
|---|---|---|
| Focus icons | Common trunk, all route branches, shared military and development, crisis anchors | 94 by 86 |
| National spirit icons | Three staged institution families, including healthy and crisis replacements | 64 by 64 |
| Decision and mission icons | Restoration, settlement, guard, project, hearing, intervention | 32 by 32 |
| Achievement icons | All planned achievements with required state variants | 64 by 64 |
| News art | Major presentation moments with reuse only when the scene genuinely matches | 397 by 153, black and white |
| Report art | Country-level political and military scenes | 210 by 176 |
| Super-event art | Three route conclusions and one earned collapse | 457 by 328 |
| Guard counters | Each required actual subunit family and frame state | Match inspected native reference exactly |
| Guard equipment art | Only actual new equipment consumers | Match inspected native consumer |
| GUI assets | Meter, selected region states, charter and guard elements | Derived from accepted native layout |

All assets in this package are planned, not produced. A numerical target from the supplied skill is not a claim that the installed consumer has been tested. Inspect the actual reference before final conversion.

## Canonical references

Use the canonical asset root from the supplied planning skill:

`C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\.agents\skills\chaos-redux-event-assets\assets\vanilla_reference`

Inspect its catalog and matching categories before production. Relevant subfolders include `icons/national_focus`, `icons/ideas`, `icons/achievements`, `icons/decision_categories`, `event_art/news`, `event_art/report`, `event_art/super_event`, `flags`, `portraits/leaders`, and the actual unit pipelines. Resolve the repository's current mounted path rather than assuming this old Windows path is the live checkout.

The rich Event 071 GUI does not require a decorative category picture. If a later approved simple category uses one, inspect `icons/decision_categories/pictures`, create the required labeled contact sheet if missing, and update its reference catalog before production.

## Immortals 3D production brief

The baseline model is a modern Iranian imperial guard infantryman suitable for the game's period. Its identity comes from a practical uniform, restrained imperial insignia, equipment, and posture. It is not an ancient warrior carrying a modern rifle as an unexplained costume.

The mountain and desert interpretation needs a practical adaptation of clothing and carried equipment. The heavy and mechanized interpretation needs appropriate protective and operational gear. Reuse one properly designed body across compatible variants when it remains visually and technically suitable. Do not commission a new body for every focus upgrade.

A firearm is a separate controlled weapon asset. The dedicated 3D pipeline skill requires a fresh Meshy 7 weapon-free body task and a separate Meshy 7 firearm task. The firearm-equipped character proceeds to Blender rigging, weights, attachment, and actions under the required model configuration. Do not run firearm characters through Meshy rigging and animation. The supplied planning prose and some TOMLs contain an older Blender-gun instruction. This package follows the dedicated 3D pipeline for new firearm geometry and flags the conflict for the skill maintainer.

Modern professional concept art, game art, or tabletop references provide the 3D input basis under the supplied pipeline. Historical and museum material can inform research, but cannot be substituted as a direct 3D source when the pipeline disallows it. Respect source rights and NoAI or no-derivative restrictions. Do not use a disallowed image merely because it is easy to find.

The final asset must match the inspected vanilla scale, skeleton, attachment behavior, action names, and export pipeline. Required actions include the actual consumer's movement, idle, firing, and death states. The precise list comes from the installed unit consumer. The weapon must follow hands and fire direction without sliding or becoming part of a fused torso mesh.

The body, firearm, textures, rig, actions, entity, unit consumer, counters, and sound routing are one acceptance unit. A nice render alone is not completion.

## Audio and animation

Guard sounds must use a verified licensed source or an appropriate existing game sound with documented fit. Do not generate audio. Check whether the game's country-tag infantry voice routing supports the desired scope. Do not create a duplicate Iranian tag merely to obtain a guard voice set.

Super-event audio must have a usable structure and a planned 60 to 120 second segment. Composition rights and recording rights are separate. A historical melody does not automatically make a modern recording free to use. Check collision with existing super-event audio and follow the shared playback helper.

Static presentation is the default. No animated portrait, flag, or GUI effect is required by this plan. Later animation needs a separate accepted purpose, required frame states, a static fallback, and pipeline validation.

## Acceptance and evidence

The asset manifest records consumer, native size, source or generation method, rights, conversion, review, and wiring status. Every missing final asset stays visibly incomplete. No placeholder is marked final. Final acceptance requires correct files, actual consumers, matching native presentation, and the prescribed in-game or MCP evidence where available.
