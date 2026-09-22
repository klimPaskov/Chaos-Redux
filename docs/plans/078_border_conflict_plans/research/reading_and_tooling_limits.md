# Reading and tooling limits

## What was fully read

The complete text of all 42 supplied text files was processed before writing the specification.
The nested `subagents.zip` was extracted, and all 20 role definitions inside it were included in that reading.
The archive container itself is not counted as a text file.
The manifest gives each supplied path, byte count, line count, word count, SHA-256 hash, and the coverage recorded by the reading passes.

An initially oversized source output was reread in bounded segments before drafting.
The final coverage check requires every line of every supplied text file to be covered by the reading records.
The existence of a file or a search hit was not treated as a full read.

The old Event 078 script and the additional MTTH skill from the pinned repository were also read in full.
Relevant parts of the offline Effects page were inspected as excerpts and are labelled accordingly.

## Required external work that remains incomplete

The instructions in the supplied files refer to installed vanilla files, native documentation, project implementations, asset references, and tooling beyond the archive.
Not all of those required external sources were available or fully reviewed.
In particular, the installed Hearts of Iron IV build and its vanilla files were not accessible in this runtime.
The offline wiki collection was found in the remote repository, but it was not read in its entirety.
The relevant Effects page was read only in the recorded ranges.

The current complete timer, weight, evolution, cluster, history, achievement, shared Chaos, border-war, and MTTH implementations were not all inspected end to end.
Search excerpts supplied leads and cautions, not full-file completion.
The authoritative workbook was not fetched or edited.
The canonical visual reference shelf, asset processors, and live owning image consumers were not visually inspected.

Consequently, the statement that all supplied text files were read must not be expanded into a claim that every external dependency required by those files was fully read.
The external reading requirement is incomplete.

## Subagent and tool execution

The role definitions were read and used to divide the implementation work into bounded handoffs.
No `collaboration.spawn_agent` action was available to execute them.
The surfaced Codex connector required a valid outer turn token, which was not available.
No token was fabricated and no role was presented as having run.
A plugin search did not supply the missing HOI4 or project collaboration capability.

No `hoi4.probability_inspect`, evaluate, sweep, simulate, compare, or render action was executed.
No game-version timing adapter was run.
No native GUI inspection, GUI render, live game, multiplayer test, or save/load test was executed.
No independent improvement-loop, completion, localization, or probability review was executed.

The parent design review in this package is a single-author review.
It is not an independent specialist closure.
The specialist files are prepared task briefs with requested evidence, not returned reports.

## What the planning package does and does not establish

The package expands all baseline and evolution mechanics from the user brief and records the added design choices explicitly.
It does not replace native border wars with normal wars, simulated outcomes, or a serialized country queue.
Its description of the intended mechanics is complete enough for an implementation attempt and acceptance review.
Its native feasibility and runtime correctness are not established.

No gameplay implementation, localization final, generated image, edited workbook, or runtime-ready asset was produced.
Only planning documents, prompt files, source-reading evidence, and package consistency checks are delivered.
No missing engine proof is described as a passed test.
The package was not shortened by omitting one of the user's three evolution concepts.
The requested subagent execution and complete external-source verification remain explicit unfinished requirements.
