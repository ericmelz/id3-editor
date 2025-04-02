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
  * `The Escape 02-05.mp3`  (Title=`The Escape`, Disc=`02`, Track=`05`)
* Maybe (depends on how audio-ds handles title text):
  * Preserve information in the original title
    * e.g., `1-09 While Dorothy Was.wav` => `Wizard of Oz 01-09 While Dorthy Was.mp3`
* Maybe: preserve original CDs so as not to corrupt .wavs
* Maybe: handle folder structures with all files or nested discs
  * Example 1:
    * David Baldacci
      * The Keeper Disc 1
        * 01-01.wav
	* 01-02.wav
      * The Keeper Disc 2
        * 02-01.wav
	* 02-02.wav
  * Example 2:
    * L Frank Baum
      * The Wonderful Wizard of Oz
        * 01-01.wav
	* 01-02.wav
        * 02-01.wav
	* 02-02.wav
* Maybe: handle folder structures with multiple nested discs but different titles
  * Example:
    * David Baldacci
      * The Keeper Disc 1
      * The Keeper Disc 2
      * The Escape Disc 1
      * The Escape Disc 2

## Observations

## Design

### Software


### UI