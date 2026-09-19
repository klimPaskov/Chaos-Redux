# Repowiki tooling

The Qoder repository wiki lives under `.qoder/repowiki/`. It has two halves that use different formats, and both are checked by the verifier in this folder.

| Surface | Purpose | Format |
| --- | --- | --- |
| `.qoder/repowiki/en/content/**` | Narrative reference pages, one per catalog entry. | `<cite>` block, table of contents, mermaid diagrams, per-section `**Section sources**`. |
| `.qoder/repowiki/knowledge/en/**` | Short structured module notes used for orientation. | `_module.yaml` plus `overview.md`, `architecture_design.md`, `coding_conventions.md`, `tech_stack.md`, `unique_setup_and_commands.md`. |
| `.qoder/repowiki/en/meta/repowiki-metadata.json` | Catalog and item registry that Qoder reads to render the wiki tree. | JSON, reconciled by `.tmp` helpers or the metadata reconciler. |

## Verifying the wiki

```text
python -B .tools/repowiki/verify_repowiki_refs.py
```

The verifier resolves every `file://<repo-relative-path>#L<a>-L<b>` citation in every page and reports:

- citation targets that no longer exist in the working tree
- line anchors that fall outside the referenced file
- loose whole-file anchors, meaning `#L1-N` where the file ends within ten lines of `N`
- content pages that lost their `<cite>` block
- pages whose top-level headings repeat, which means the page holds its own body twice
- knowledge modules without a `_module.yaml`
- with `--style`, prose lines hard-wrapped mid-sentence

Useful invocations:

```text
python -B .tools/repowiki/verify_repowiki_refs.py --paths          # list only broken targets
python -B .tools/repowiki/verify_repowiki_refs.py --verbose        # per-page findings
python -B .tools/repowiki/verify_repowiki_refs.py --strict         # fail on loose anchors too
python -B .tools/repowiki/verify_repowiki_refs.py --page "CBRN"    # limit to matching pages
python -B .tools/repowiki/verify_repowiki_refs.py --json out.json  # machine-readable report
```

Exit code 0 means the wiki is clean; 1 means at least one finding.
Loose anchors are reported by default but only fail the run under `--strict`, because they are pre-existing debt on pages that have not been refreshed yet.

## What the verifier cannot prove

The verifier checks that a citation resolves and that its anchor is inside the target file.
It cannot check that the anchored lines contain the claim the page makes.

That gap matters, because an anchor that is inside the file but points at unrelated content looks identical to a correct one.
The known instance is the dominant defect this tooling was built to fix: pages cited files such as `chaosx_event_cluster_effects.txt` at `#L29-82`, and every one of those anchors was in range while pointing at nothing relevant.

Treat a passing run as proof that the citations are well formed, never as proof that the pages are correct.
Correctness still requires reading the anchored lines.

## Citation rules

A citation is only evidence when the anchor still points at the lines that prove the claim.

- Cite `file://path#L<a>-L<b>` for a block and `file://path#L<a>` for a single line.
- Re-derive anchors after editing a cited file. Never copy an anchor from an older revision of the wiki.
- Cite the file that owns the behaviour, not a summary of it.
- Keep the `**Section sources**` list of each section consistent with the claims in that section.

## Refreshing the wiki after repository drift

1. Run the verifier and read the broken-target and stale-anchor findings.
2. Refresh the affected pages against the current sources, re-deriving every anchor.
3. Reconcile `repowiki-metadata.json` so its catalogs and items match the pages on disk.
4. Re-run the verifier until it exits 0.
