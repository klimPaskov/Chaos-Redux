# Launch 16 startup results

The unchanged supplied shortcut launched PID 9672 at 12:40:09 local time on 2026-09-05.
Frontend startup completed at 12:41:07 after 58391ms; the process was responsive at the final check, then stopped and its logs archived.
No desktop control, visual main-menu acceptance, or campaign loading was performed.

The archived error.log has 2060 lines and 358074 bytes, SHA256 c52a458ed8ba79f6eff192217cffdc68cb1d323e6f88c4badc16529ed2136c60.
Normalized distinct diagnostic lines decreased from 702 to 697: six previous lines disappear and the only new line is an aggregate error count.
All four tracked sources remained byte-identical during the launch, including the two observed Event 32 files.
Actual before/after source bytes and hashes are archived under logs/launch_16/.

The two Acid Rain legacy mission IDs produced ten missing-decision diagnostics in launch 15 and zero here.
Their current definitions and activation paths do not exist; the final repair removes only the two stale cleanup references and retains the legacy exposure migration, flags, modifiers, and receipts.
No replacement missions or fallback definitions were added.
This resolves the parser regression exposed by the initial keyword repair; old-save migration behavior is still untested.
The final Event 33 source hash is b3274caff6f80424349fb57101144a8ccc4d81da805c0ad21647a0a66081bff5.

The two Great Depression external-adapter cleanup calls produced twelve invalid-effect diagnostics in launch 15 and zero here.
The two scratch amounts are initialized before reads, copied into owner-request inputs, and not observed by caller continuations; only the unsupported cleanup lines were removed.
The adapter source hash is 766a2401cf952333148d28fd1cb0d5ad2b88da743c3a14ff268aed7d0c7ecaef.
Actual famine/migration requests and live outcomes remain untested.
The detailed contracts and MCP partial/cache limitations are in event33_mission15_handoff.md and event35_adapter_temp16_handoff.md.

Other attributable errors still block clean startup, including temporary cleanup calls, target cleanup contracts, unsupported triggers, missing constants, and undefined helpers.
The Great Depression missing cadence helper requires its phase-sensitive contract rather than a fixed-delay substitute.
No campaign, save, feature screenshot, teaser video, or mechanics-guide media replacement has occurred.
No broad redesign or gameplay fallback was introduced, and the comprehensive goal remains active.
