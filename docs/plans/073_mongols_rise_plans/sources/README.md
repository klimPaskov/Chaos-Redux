# Supplied source records

The original brief is preserved byte-for-byte in [073_mongols_rise_original_brief.md](073_mongols_rise_original_brief.md).

The [source read ledger](source_read_ledger.csv) identifies all 43 textual items read: 22 top-level project sources, 20 nested subagent profiles, and the original brief. It records byte counts, line counts, and SHA-256 identities. These hashes identify the sources and do not independently prove comprehension.

The [archive identity record](source_archive_identity.json) records the supplied archive and nested subagent archive. The source archives themselves are not repackaged here. The implementation agent should read the current local owning skills and referenced files, not assume that an old snapshot replaces them.

Read [the full limits statement](../audits/01_read_status_and_limits.md) before interpreting the ledger. Full reading of supplied files does not mean every linked local reference, the entire repository, or all vanilla game files were available.
