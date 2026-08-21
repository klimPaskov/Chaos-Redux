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

## AGENTS.md, Skills and Subagents

This repo intentionally leaves the coding agent resources visible, so if you want to, you can fork the repo and contribute directly.

Watch the tutorial videos: <https://www.youtube.com/watch?v=pH_VpBs0mIk&list=PLh6JmuEabQioc4V8IYGEsMtqiw-xemeX3>

## Contact

You can reach me directly from Discord. My tag: `zin1496`.
