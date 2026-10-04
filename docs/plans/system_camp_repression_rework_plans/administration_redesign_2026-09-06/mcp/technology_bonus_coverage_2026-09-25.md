# Administration research-category MCP coverage

Disposition: implemented category references with static inspector evidence; runtime award validation remains unresolved.
Acceptance basis: the user-authorized institutional program contract in `accepted_implementation.md`.

The connected `hoi4.tech_inspect` `bonus_coverage` route completed for all three categories used by the paid institutional programs. The scoped rows reported:

| Category | Technologies | Static coverage | Graph revision |
| --- | ---: | --- | --- |
| `industry` | 43 | Covered; 290 projected bonus sources | `59a1423bb7df50526988cd35efce1534c3a0a712e23df9b304d20885d9279f4d` |
| `support_tech` | 38 | Covered; 143 projected bonus sources | `3e05d295924309afd71c114a6ef731a822a572fd365be71d45479599efab9473` |
| `engineers_tech` | 5 | Covered; 18 projected bonus sources | `3e05d295924309afd71c114a6ef731a822a572fd365be71d45479599efab9473` |

Source artifact URIs:

- `industry`: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2b56dfefe98f2b8ec6c26d13bd1ab60f5132c9a7174c9c43c75691ea47b67cef/7a2be8f8ba090eaa3b067309adc6f5a62450b3180c484fa96da2044d4a388835/technology-bonus_coverage-59a1423bb7df.json`
- `support_tech`: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/68d1c21cb4b477f380ed37068d82984203ef091d04fe235fdead4bb7abefe684/80ba1b6caf3bd6db54eca7479fdbe76f07fb09fe0a646799c0d0c99bb0a3d2d7/technology-bonus_coverage-3e05d2959243.json`
- `engineers_tech`: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4a6a3514165bc01a91d4b0f284abbcaa0b386377b2749d780ec1380facf612a7/0da88be90c07803264f11c0b05e3b001cf68b91bc501d7ad30b0ea36e187e8bb/technology-bonus_coverage-3e05d2959243.json`

The inspector is static and explicitly does not resolve runtime meta-generated bonus values or exact research choices. It therefore proves the category IDs and eligible technology coverage, but not that a particular program paid, completed, awarded a one-use bonus or observed the two-per-year cap in the engine. Those conditions have parsed-source scenarios and still require runtime evidence. The full `industry` report includes an unrelated vanilla `naval` missing-category finding; it does not concern an administration program.
