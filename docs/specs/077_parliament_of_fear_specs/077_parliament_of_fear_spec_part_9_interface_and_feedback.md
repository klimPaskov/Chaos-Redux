# Parliament of Fear
## Part 9. Chamber interface and player feedback

### Main location

The chamber is a scripted interface attached to the event's decision category. It uses the familiar Hearts of Iron IV visual language of dark metal framing, paper records, compact controls, and legible state information. It must look like an in-game political management panel rather than a separate web dashboard.

Because the chamber is the category's main visual and interaction surface, the category does not also receive a decorative picture competing for the same space. The reference composition and exact native layout must be approved and rendered before implementation is accepted.

### Information hierarchy

The top area identifies the institution and current country. Paranoia is the dominant value. Governing support and filled seats are the only supporting persistent values. Global Chaos remains in the shared mod interface and is not duplicated as another meter inside this system.

The chamber occupies the center. A selected bloc or seat group opens its case summary and relevant character information. Four primary action controls remain in a stable location. A small area below them shows the active inquiry, appointment queue, and current objective.

Case evidence is contextual. Institutional impairment is shown through concise status text and existing national-spirit detail. Neither becomes a permanent row of extra gauges.

### Seat arrangement

The 100 seats use a clear semicircular or council-like arrangement with stable positions throughout one crisis. Seats belonging to the same bloc sit together where possible. A bloc's position does not move whenever one member becomes suspected, so the player can follow which group is changing.

The base silhouette and fill show support or vacancy. Evidence markers sit on top. An accused loyal seat can therefore display both its dependable-support identity and an accusation mark. Suspicion must not overwrite support color and make the player think those votes have already been lost.

A purged seat briefly shows a removal transition and then becomes visibly empty. Vacancy is represented by a distinct empty shape, not simply a dark color. Suspended seats use a separate mark and explain why they are temporarily nonfunctional.

### Accessible status language

Color is supported by shape, icon, pattern, and tooltip text. Loyal and dependable-by-agreement seats have distinguishable markers. Uncertain seats remain visibly occupied. Suspected and accused overlays differ in shape. Vacant seats have a clear outline or gap that remains legible in a low-contrast display.

A reduced-motion setting or static rendering path must preserve every warning and state distinction. A pulse is never the only indication that a bloc has become accused.

### Selection and action preview

Selecting a bloc shows its influence count, current support relationship, case status, relevant agreement, and notable people. These are contextual details for the selected target. The player sees which information is known and which remains uncertain.

Selecting an action mode shows the exact current price, the expected duration, the known character or office risks, and the uncertainty of the outcome. When more than three resources or sacrifice descriptions are relevant, the compact price line shows at most three values and the rest appears in the expanded explanation. No action uses more than four spendable cost types.

A changed target or changed country state invalidates an old price preview. Confirmation obtains the current validated result before any payment or removal occurs. The interface cannot retain a cheap preview from before a bloc gained influence and apply it to a larger purge.

### Low-pressure appearance

The chamber is orderly, with clear seat grouping, restrained paper accents, and little motion. Case records resemble ordinary administrative work. Empty seats remain visible but do not obscure the rest of the chamber.

The interface should communicate that the crisis can be managed. It should not begin with a screen full of blood, prison imagery, or warnings unrelated to the current cases.

### Rising pressure

As Paranoia rises, relevant case markers and documentary overlays become more prominent. Redactions, crossed-out names, stamped restrictions, and competing reports can appear around the actual affected groups. The content remains legible and interactive.

Warning effects are bounded to selected or newly affected elements. The entire chamber does not flash continuously. Large dark overlays cannot hide the current support count, action costs, or the close control.

### Extreme pressure and emptiness

At high Paranoia, the visual emphasis shifts toward absences and contradictory records. Empty seats accumulate where removals occurred. Investigators and replacement appointees can receive the same accusation markers as previous targets. The interface conveys a state turning on its own personnel without falsely marking every seat as guilty.

A Great Purge preview highlights the threatened groups. After a wave, only actually affected seats and institutions change. The design does not play a generic empty-chamber sequence when the country's chamber remains mostly filled.

### Motion

One restrained warning animation family is justified for a newly accused bloc or an imminent purge demand. It uses actual authored frames, with a static warning state available at all times. The animation is brief on state change and does not loop over every seat indefinitely.

Important motion consists of state transitions: an accusation marker appearing, a seat being vacated, or an appointment restoring a holder. The reference asset plan defines the frames and their consumers. A still image with a brightness pulse does not satisfy a real frame-animation deliverable.

### Contextual dossiers

A dossier contains a compact portrait when a real eligible figure is linked, the figure's current relevant role, the known allegation, source quality, corroboration, and the office at risk. Abstract groups use an institutional symbol. The interface must not invent a portrait and present it as a historical individual.

The dossier's history distinguishes allegation, finding, and government action. It can show that a person was removed before being cleared. It does not rewrite the finding to make every government action appear justified.

### Required visual states

The reference and render review cover an orderly opening, an accused but loyal bloc, a narrow majority, an underfilled chamber, a protected figure, an active inquiry, a prepared plot warning, a Great Purge preview, a post-purge chamber, and stable recovery. They also cover a country without a real portrait for the selected institutional group.

Each state must remain usable at the baseline supported resolution and at smaller supported resolutions and UI scales. Exact native dimensions, font sizes, element positions, clipping rules, hitboxes, and scroll behavior belong in the implementation reference map after inspecting the real host category.

### Player-facing acceptance

The player can identify their support, occupied seats, most urgent case, and available response without leaving the main panel. The meaning of an accused loyal seat is clear. Irreversible losses are named before commitment. The interface remains usable when most seats are empty and when text is longer than the English reference.

Rendering alone does not prove that actions execute correctly. The visual and gameplay validations are separate requirements.
