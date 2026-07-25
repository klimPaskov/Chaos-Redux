# Exact portrait-owner audit

The audit searched exact subject names and likely character keys in these five roots: current Chaos Redux, vanilla HOI4, Kaiserreich `1521695605`, reference `2265420196`, and reference `1458561226`.

The searched paths were `common/characters`, `history/countries`, `gfx/leaders`, `interface`, and `localisation/english`. Common-name pools and unrelated prose were excluded from the ownership decision so surname fragments could not create false positives.

## Results

| Candidate | Chaos Redux | Vanilla | Kaiserreich 1521695605 | Reference 2265420196 | Reference 1458561226 | Decision |
| --- | --- | --- | --- | --- | --- | --- |
| Fernand Jacquet | NO_MATCH | NO_MATCH | NO_MATCH | NO_MATCH | NO_MATCH | Selected additive commander candidate, subject to source-rights review |
| Charles de Broqueville | NO_MATCH | NO_MATCH | NO_MATCH | NO_MATCH | NO_MATCH | Alternate research only; not a selected civic replacement |
| Albert Devèze | NO_MATCH | ACTIVE `BEL_albert_deveze` in `common/characters/BEL.txt` and `history/countries/BEL - Belgium.txt` | NO_MATCH | NO_MATCH | NO_MATCH | Blocked by vanilla owner |
| Jules Destrée | ACTIVE AFX owner | NO_MATCH in audited vanilla owner paths | NO_MATCH in audited owner paths | NO_MATCH in audited owner paths | NO_MATCH in audited owner paths | Approved existing runtime civic owner |
| Gérard Leman | NO_MATCH | NO_MATCH | NO_MATCH | NO_MATCH | NO_MATCH | Rejected because deceased in 1920 |
| Henri Denis | NO_MATCH in current package audit | NO_MATCH | ACTIVE Kaiserreich owner per parent audit | NO_MATCH | NO_MATCH | Blocked by Kaiserreich owner |

## Command shape

The search used case-insensitive word-boundary matching for each subject and key variant and was run from each root with `rg` restricted to the five ownership paths above. No fuzzy surname-only hit was treated as an owner.

## Interpretation

Jacquet is the only selected new source and is safe for additive commander review, subject to the documented unknown-photographer rights uncertainty. De Broqueville has no exact owner but remains alternate research only because Destrée is the approved current civic owner and the de Broqueville portrait is not a requested replacement. Devèze cannot be selected without an explicit safe transfer decision. Destrée is active in Chaos Redux and must not be cloned or replaced. Historical viability was checked separately from ownership; a no-match does not by itself prove that a candidate is appropriate for every role.
