# Package Validation

> Historical planning validation note, reconciled 2026-08-02: this file records archive and specification checks, not live gameplay proof. The former independent-Rat-Nation and unresolved registry wording is superseded by the registered Diseases cluster `8`, scenario `SCN-012`, and the two-tag `RTA`/`RTX` contract.

## Result

The revised Event 20 Black Plague planning package passed its final artifact checks after the user corrections were incorporated. These checks validate the planning files and archive structure. They do not validate unimplemented gameplay.

## Structural checks

- Every planned Markdown file exists and is nonempty.
- Nine specification parts are present in sequence.
- Part 9 defines the triggerable instant-chaos scenario.
- All required prompt files are present.
- The goal prompt contains 3,998 characters before its final newline.
- The package includes AI, decision, state, evolution, country, focus, achievement, asset, tuning, catalog, scenario, and acceptance matrices.
- Three readable Mermaid design diagrams are present.
- The source-read ledger and limitations disclosure remain complete and honest.
- All relative Markdown links resolve.
- Every Markdown file decodes as UTF-8.
- No continuation prompt remains.
- No em dash or sentence semicolon remains in the planning prose.

## Correction coverage checks

- The scenario is directly launchable through the shared triggerable scenario system, subject only to impossible or terminal conflicts.
- Scenario intensities seed multiple continents and many states.
- Scenario setup forces Evolutions I through IV, seeds internal broods under the reusable `RTA` carrier, and creates or preserves the separate `RTX` Rat King.
- Scenario setup does not grant Evolution V or world end.
- Black Plague-specific decisions appear inside the shared disease category.
- Cleaning city rats, food storage, sewer, flea, transport, demolition, hospital, quarantine, cordon, and treatment actions are represented.
- Every established Black Plague state uses a black mapmode base colour.
- Phase and special status overlays preserve the black base.
- Other diseases retain their normal mapmode colours.

## Coverage checks

The completion audit maps every user requirement to a specification surface. The improvement review reaches the anti-bloat stop condition after incorporating the later corrections. Manual role reviews cover the supplied planning, decision, focus, country, localisation, system, documentation, asset, super-event, and completion standards.

## Archive checks

The final ZIP is built from the `docs/` tree. The archive receives a CRC test, extraction test, file-list comparison, and byte-for-byte hash comparison against the source directory. The checksum file records the SHA-256 of the final ZIP.

## Boundaries

No gameplay code, final visual asset, audio file, spreadsheet edit, or in-game balance result is represented as complete. The live mapmode resolver, scenario transaction behavior, black fog, and performance remain user-owned validation surfaces. The scenario registry identifiers and two-tag capacity are recorded as current static evidence, not unresolved planning work.
