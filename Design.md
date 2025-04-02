# Requirements + Design

## High-level requirements
Converts sets of CDs for an audiobook to a standardized format.
Format will be one folder with appropriately named files in the
appropriate format.

* convert .wav files to .mp3 files
* use id3 tags for
  * author (artist?)
  * title
  * track num on disc
  * disc num
  * total discs
* rename files to Title disc-track, E.g.,
  * The Escape 02-05.mp3  (Title=The Escape, Disc=02, Track=05)
* Maybe (depends on how audio-ds handles title text):
  * Preserve information in the original title
    * e.g., 1-09 While Dorothy Was.wav => 01-09 While Dorthy Was.mp3

## Observations

## Design