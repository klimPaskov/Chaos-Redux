# Event 024 catalog alignment

Disposition: implemented alignment verified on 7 October 2026, with native and probability acceptance still unresolved.
No in-game wording, workbook or repository CSV was edited during this check.

The authoritative workbook's Event 24 entry is `Events!A25:M25`.
Its name matches `chaosx.nr24.1.t` and `chaosx.event_name.24`.
Cells C25-F25 exactly match `chaosx.event_details.24` and `video_game_in_sweden.evolution.1.body` through `.3.body` in `localisation/english/024_hearts_of_iron_l_english.yml:461-467`.
G25-I25 are empty, J25 is Minor Fire-Once, K25 is 1, L25 is empty and M25 is Needs Testing.
No row in Cluster Memberships or Scenarios identifies Event 24.
The evolution columns contain descriptions, not title-and-body pairs.

The status acceptance basis is the user-bound package's `024_video_game_in_sweden_catalog_alignment.md:51-59`, which explicitly recommends Needs Testing for implemented but not live-tested content.
This event-specific instruction takes precedence over the current event skill's post-20 default.
`Implemented` in that package's future status recommendation is not a valid workbook Legend label and must not be used.
Any future promotion to Playable still requires explicit user approval and complete acceptance evidence.

The repository exporter was run into a unique temporary verification directory without saving the workbook or overwriting the shared exports.
It produced 166 Events rows, 20 Clusters rows and 17 Scenarios rows.
All three generated files exactly matched the current repository exports by SHA-256.
The workbook hash remained unchanged during that run.

| Verified artifact | SHA-256 |
| --- | --- |
| Authoritative XLSX | `9cfac64aa2d6d734b9e1d494929b8a515edc0b99089c854bcc9b3806e5e8a53d` |
| Events CSV | `629183fe9c411c912d3a7ca08b73151d417669dc6000d25172b27635e8216799` |
| Clusters CSV | `b08015ac4cc8f54cbfcb8c8a810abdaae2bfd64c7ef1d4c6afc9d2e493b83f13` |
| Scenarios CSV | `95d667fa6c1d5e874b0c51c61efb465b814ae484f6dc48616680238ec85dc5e9` |

These hashes identify the checked shared-worktree state, not ownership or approval of other agents' catalogue edits.
The workbook and its three exports were already modified by other work and remain outside this documentation commit.
Repeat the alignment check if final localisation changes.
No catalogue-only change remains queued for the current wording.
