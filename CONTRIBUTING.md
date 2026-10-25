# Contributing

Hi there! I am thrilled that you'd like to contribute to this mod. Your help is essential for keeping it great.

Your contribution can range from testing the mod, presenting new features/events, reporting bugs, or translations.

Watch my video to get started: <https://youtu.be/feD3BDelD_U>

## Setup and submitting a pull request

If you're unfamiliar with GitHub, you should watch this video: <https://www.youtube.com/watch?v=k5D37W6h56o>

### Restore Git LFS assets

Chaos Redux stores runtime art, source images, and audio with Git LFS.
If a `.dds`, `.png`, `.tga`, `.wav`, or `.ogg` file opens as three lines beginning with `version https://git-lfs.github.com/spec/v1`, the working copy contains an LFS pointer instead of the real asset.

Install Git LFS once, fetch the required image and audio objects, and hydrate the working tree:

```powershell
git lfs install
git lfs pull --include="gfx/**,*.png,*.wav,*.ogg,*.flac,*.mp3,*.opus"
git lfs checkout 'gfx/**' '*.png' '*.wav' '*.ogg' '*.flac' '*.mp3' '*.opus'
```

Do not classify an asset as broken from file size alone.
Small flags and interface glyphs can legitimately remain under 1 KB; the LFS pointer signature and image or audio decoding are the reliable checks.

### Run the repository checks

Before opening a pull request or pushing, run the read-only repository checks from the mod root:

```powershell
python -B .tools/check.py full
```

It needs Python 3.9 or newer with Pillow, NumPy, SciPy and openpyxl, Node.js, and the installed game; set `HOI4_GAME_DIR` if Hearts of Iron IV is not in the default Steam folder.
It must exit `0`, or every remaining error must be explained in the pull request or push notes.
During work, `python -B .tools/check.py quick` checks only what your changed files can affect; [`.tools/README.md`](.tools/README.md) explains every check and its limits.
These checks cover file integrity, references and syntax; they do not replace testing the mod in game.

## AGENTS.md, Skills and Subagents

This repo intentionally leaves the coding agent resources visible, so if you want to, you can fork the repo and contribute directly.

Read [CLAUDE.md](CLAUDE.md) (or [AGENTS.md](AGENTS.md) for other runtimes) and the relevant [repository skill](.claude/skills/) before changing project content.
Use the [documentation index](docs/README.md) to find the owning design, implementation summary, and working plan.
Canonical specialist instructions live in [.claude/agents/](.claude/agents/).
Generated runtime definitions follow the [synchronizer guidance](.tools/sync/README.md) and the active runtime's ownership restrictions.

Watch the tutorial videos: <https://www.youtube.com/watch?v=pH_VpBs0mIk&list=PLh6JmuEabQioc4V8IYGEsMtqiw-xemeX3>

## Contact

You can reach me directly from Discord. My tag: `zin1496`.
