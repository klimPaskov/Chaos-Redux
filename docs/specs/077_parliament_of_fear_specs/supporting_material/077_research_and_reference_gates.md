# Research record and reference gates

Research was checked on 20 September 2026. References below support narrowly stated distinctions. They do not establish complete compatibility with the user's installed Hearts of Iron IV version.

## Supplied project sources

All 42 text files in `all-project-sources(9).zip`, including the 20 nested subagent TOMLs, were fully read before the design was authored. The reading manifest records byte counts, normalized character counts, and SHA-256 hashes. The archive supplies skills and catalogs, not the full live mod or installed game.

Project design facts in the specification are grounded in `AGENTS.md`, the planning and event skills, `CHAOS_REDUX_MECHANICS.md`, the dynamic helper documentation, the relevant interface, asset, decision, super-event, and validation skills, and the three supplied catalogs. Numerical tuning added by this package is identified as a proposal rather than observed runtime behavior.

## Primary institutional references

### UK Parliament, Confidence motion

Source: https://www.parliament.uk/site-information/glossary/confidence-motion/

The official explanation connects the government's authority to confidence in the House of Commons and describes resignation or dissolution as traditional consequences of lost confidence. It supports treating a parliamentary confidence crisis as a distinct institutional process.

It does not supply a universal constitution for every parliamentary country in the game. The package's 100 influence seats and 51-seat threshold are gameplay abstractions, not a claim about the historical size of the House of Commons.

### US National Archives, Constitution transcript

Source: https://www.archives.gov/founding-docs/constitution-transcript

The constitutional text distinguishes the House's impeachment role from the Senate's trial role and describes removal through impeachment and conviction. This supports the design requirement that losing ordinary legislative support cannot itself remove a president.

The original text contains provisions later amended. It was not treated as a complete statement of every current or 1936 appointment, election, or vacancy rule. Country-specific replacement procedures remain a separate reference gate.

### Library of Congress, Revelations from the Russian Archives, Internal Workings of the Soviet Union

Source: https://www.loc.gov/exhibits/archives/intn.html

The exhibition and its archival-document links were consulted as historical context for accusations spreading through governing institutions. Some broad historical claims in its narrative are disputed or require more careful treatment. This package does not repeat its causal claim about the Kirov murder, use its casualty totals, or derive game probabilities from the exhibition.

No final quotation, historical purge text, or super-event audio was taken from this source. A quotation requires a separate original-document and context check.

## Connected repository evidence

Repository: `klimPaskov/Chaos-Redux`

Pinned search revision: `879b3007d3b6bf75c726c11635473fccda45c569`

Confirmed paths from the connected search:

- `events/077_send_eq.txt`
- `localisation/english/077_send_eq_l_english.yml`
- `events/_chaosx_news.txt`

The existing root identity and legacy equipment-aid purpose were visible in search and partial fetch results. The full fetch arrived as an oversized single-line JSON content field and was truncated. It was not counted as a fully read live source file.

The connected repository also returned `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md`, labeled as a snapshot captured on 19 September 2026. That response was truncated. It confirms availability in the repository, but does not satisfy the mandatory full-page read.

Raw-file retrieval was attempted after the connector truncation. The container request failed with a DNS resolution error. A web raw-file attempt returned a disabled-fetch error. These attempts did not produce a usable complete file.

## Missing full-read references

The following mandatory external material remains unread in full because it was not supplied and could not be fully retrieved through the available route:

- The live event and integration files, including all legacy Event 077 references
- Relevant offline wiki pages for data structures, scopes, triggers, effects, modifiers, localisation, on-actions, events, decisions, ideas, AI, characters, and GUI/interface behavior
- Installed vanilla scripted GUI documentation and the Soviet paranoia GUI and scripted GUI files
- Actual country-specific constitutional, political, character, appointment, and native-purge implementations
- The source workbook and official exporter
- Referenced skill appendices and local resources absent from the archive, including the MTTH skill where required, spreadsheet workflow, native asset templates, image-family references, conversion tool implementations, and exact achievement overlays
- Current shared crisis, universal cost, event log, super-event, achievement, and country-transition implementation contracts

These gaps are implementation blockers for the affected surfaces. They do not become verified facts because a proposed adapter or filename is described in this package.

## Production research gates

Super-event title direction must be turned into final source-checked text. Any quotation needs exact wording, attribution, date, original context, and appropriate use. Audio needs a verified composition and recording, rights review, excerpt timing, and uniqueness against the mod's existing assignments.

Real portraits require identity and likeness sources. Country-specific flags, institutional names, and political roles need grounded references. Abstract institution symbols do not require invented historical people.

## Research limits

The online Paradox Wiki was not used as a substitute for the required offline project snapshot. No native Soviet mechanic values, current engine effects, DLC API details, or exact GUI dimensions are claimed to be verified. The specification's numerical anchors are proposed design values awaiting implementation and probability validation.
