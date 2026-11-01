# Player-facing text direction

Read the relevant complete section before writing any direction for event titles, descriptions, option text, report and news text, decision and focus text, achievement text, GUI labels, super-event text, or a localisation handoff. The planning spec defines direction only and never final localisation.

## Tone and presentation direction standard

For every player-facing text surface, the planning spec should define the writing direction and leave finished wording to implementation. This includes event titles, event descriptions, report text, news text, focus text, decision text, option text, achievement text, super-event setup, GUI labels, route flavour, event-detail text, and spreadsheet-facing summaries.

Give the coding agent clear direction for:

- actor or viewpoint
- force driving the event
- information visible to the player
- information that should remain uncertain
- tone, severity, and humour mode
- references that need research
- words, frames, or clichés to avoid
- dynamic actors, states, countries, values, or routes that final text should mention

Do not provide pasteable localisation. Do not include `sample line`, `possible line`, `placeholder text`, `temporary title`, or exact draft wording that could be copied into localisation. When a structural label is needed for a file, row, route, branch, asset, or prompt, mark it as a working label, not final localisation.

Text direction should avoid bland map-summary framing and generic communications clichés. Do not make the emotional center of an event a changed map, a line of advance, a staff-table scene, a failed broadcast, or another stock image of crisis administration.

When planning player-facing warning, threat, suspicious-report, and escalation text, do not instruct the coding agent to say that something is a warning, that something is not a warning, that a threat is coming, or that a danger signal has appeared. The text should show the pattern through partial information: fearful witnesses, rumours, anomalies, mysterious powers seen, and similar signs.

A report can make the player uneasy without naming the unease. Use mystery, information gaps, fear, rumours, and similar techniques. The player should infer that something may be wrong from the content and consequences, not from a label.

When a concept benefits from mystery, fantasy, surrealism, myth, occult signs, prophecy, impossible resolve, strange energy, or unclear public rumours, state that direction clearly without drafting the final prose.

## Event option humour, irony, and cultural remark direction

The planning spec may define what an option should feel like, what stance it represents, and how it should vary by route or actor. It must not write final option text.

Do not let the implementation agent default to bland buttons unless plainness is intentional. Describe the intended option style, such as official denial, sarcastic acceptance, bitter understatement, cultural allusion direction, period propaganda tone, frightened understatement, arrogant boast, administrative absurdity, local proverb direction, or grim irony that condemns the speaker.

For each important option or option family, define:

- who is speaking or reacting
- what the option means mechanically and narratively
- whether the tone should be serious, ironic, sarcastic, cruel, frightened, resigned, bureaucratic, or absurd
- what kinds of cultural references may fit
- which references need research before wording is written
- how route, ideology, chaos tier, campaign state, or country culture should change the reaction

Humour should fit the stakes. Minor chaotic events can use sharper jokes and visible sarcasm. Major disasters, massacres, atrocities, mass death, and real-world suffering should use severity, official euphemism, cynical propaganda, hypocrisy, or self-damning grim irony. Cheap comedy is forbidden there.

Cultural remarks should be treated as research directions unless already sourced. The spec may say that a line should draw from a period slogan, military idiom, folk saying, religious register, old newspaper style, literary echo, propaganda formula, or local public habit. It must not invent the exact remark.

Do not list example option lines. Do not write sample buttons. Do not write placeholder localisation for options. Coding agents may paste those into the game.

Some events need one cutting reaction direction and one plain practical reaction direction. Some need several route-specific reaction directions. The spec should state the intended option tone and purpose, then leave the final wording to the coding agent.

## Writing style

For player-facing text, define the same style as direction only. Event description direction can stay grounded while option direction can use irony, sarcasm, cultural remarks, and humour that fit the actor and stakes.

Avoid:

- generic disaster wording
- empty dramatic language
- making every event apocalyptic
- random chaos without purpose
- implementation code
- excessive technical detail
- filler text that repeats obvious system behavior
- displaying event effects in event details
- long sentences without actually saying anything
- short staccato sentences that are dramatic and just make comprehension more confusing
- option direction that would lead to bland placeholder buttons
- absence notes for systems that are not present, such as saying an event has no world-end scenario or no manual triggerable scenario

Mention implementation only where it matters for the design, such as super-event treatment, custom UI, AI behavior, documentation, assets, dynamic factors, focus tree structure, custom tags, or important system connections.

This planning skill defines direction for player-facing text. It must not write final player-facing localisation. This includes event titles, event option text, event descriptions, news and report prose, decision names, decision descriptions, focus names, focus descriptions, achievement titles, achievement descriptions, GUI labels, event-detail text, spreadsheet-facing wording, super-event titles, super-event button text, super-event quotes, cultural remarks, source-like allusions, and final audio selections.

The planning spec may define tone, actor viewpoint, structure, visible information, route variation, dynamic placeholders that final text should use, and research needs. If a working label is needed for a row, filename, prompt, branch, route, asset, diagram, or internal handoff, mark it clearly as `working label, not final localisation`.

Important super-event boundary: this planning skill may define super-event role, trigger, tone, image direction, quote direction, cultural-remark direction, and audio mood. Any source-dependent wording belongs to `chaos-redux-super-events` and must stay blocked until researched and documented.

### General text writing style

1. Never use the em dash or semicolons in sentences.
2. Absolutely avoid dialectical hedging. Do not frame sentences as thesis, antithesis, synthesis.
    - Dialectical hedging examples:
      - `The invasion is not merely a border crisis, but a crisis of identity.`
      - `The regime is not only losing the war, it is losing itself.`
      - `This is not just a strike. This is a warning.`
      - `The cult is not fighting for land, but for meaning.`
      - `The disaster is both a local tragedy and a global sign.`
      - `The government is neither dead nor alive, but something worse.`
      - `The army did not collapse. It transformed.`
      - `This is less a rebellion than a confession.`
      - `The question is not whether order can return, but what kind of order will survive.`
      - `What looks like defeat is actually a new form of power.`
    - Thesis, antithesis, synthesis examples:
      - `The army claims the province is secure. Refugees say it is already lost. The truth lies between them.`
      - `Some call the new state liberation. Others call it occupation. In reality, it is both.`
      - `The priests call it a miracle. The generals call it a weapon. History will call it both.`
      - `The committee promises order. The opposition sees tyranny. The new system contains both impulses.`
      - `The papers call it a victory. The hospitals call it a defeat. The country has become both at once.`
      - `The rebels ask for justice. The regime asks for peace. The settlement gives neither and both.`
3. Avoid AI-style explanatory templates. Do not write lines that sound prebuilt or reusable across any event.
4. Absolutely avoid staccato sentences. Do not split one simple thought into a chain of tiny lines for artificial weight or dramatic effect. Use complete, readable sentences with enough context to be clear.
    - Staccato examples:
      - `The radios died. The roads emptied. The city listened.`
      - `No orders. No mercy. No dawn.`
      - `The border fell. Then the capital. Then the government.`
      - `They marched. They burned. They vanished.`
      - `A knock at the door. A list on the table. A train in the dark.`
      - `The guns stopped. The screaming did not.`
      - `First hunger. Then anger. Then flags.`
      - `No king. No cabinet. No law.`
      - `Ash in the streets. Smoke over the port. Silence at noon.`
      - `One order. One shot. One missing officer.`
      - `The gate opened. The crowd moved. The guards ran.`
5. Avoid staged contrast formulas. Do not write sentences or paired clauses built as `claim X while officials Y`, `reports say X while authorities Y`, `people do X before governments Y`, `X happens before Y admits it`, or similar. Do not manufacture tension by contrasting unofficial fear with official denial, silence, delay, admission, or reaction. Write the observed fear, behaviour, rumours, anomalies, and consequences directly.
6. Absolutely avoid empty dramatic filler. Do not lean on vague intensity words when concrete detail would do the work.
7. Do not paste instruction text, task labels, prompt fragments, or process notes into in-game text, specs, docs, localisation, spreadsheet fields, or reports.
    - For example, when I say: `Do not reveal the hidden mechanics here.`, don't write `This path purposely doesn't reveal the hidden mechanics`.

### General localisation handoff

When a spec includes text-bearing content, give a localisation handoff, not final copy.

The handoff should list each needed text surface and describe its direction:

- event title direction
- event description direction
- option reaction direction
- news or report direction
- decision name and description direction
- focus name and description direction
- achievement title and description direction
- GUI label direction
- event-detail and event-log wording direction
- dynamic placeholders the coding agent should use
- research gates for quotes, slogans, songs, films, books, speeches, scriptures, proverbs, or other source-dependent references

The coding agent writes the final in-game text during implementation. The planning spec should not provide final prose for the coding agent to paste.
