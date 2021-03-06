# SplitNotes 2 #

**SplitNotes but bigger***

SplitNotes2 is an application for displaying speedrun notes in sync with livesplit.
Requires *livesplit server* to be running.

There is now a server version included to allow reading from a browser on another device.

## Install/Setup ##

1. Under the Livesplit layout editor add 'LiveSplit Server' (listed under 'control')
2. Download SplitNotes2 from the [**releases page**](https://github.com/DavidCEllis/SplitNotes-2/releases)
3. Extract anywhere and run *splitnotes2.exe*

## Usage ##

1. Connect with livesplit by starting the livesplit server component selecting 
   'Control' and 'Start Server'
2. Right click in the splitnotes window and select 'Open Notes' and find the text file
   containing the notes you wish to use.
   
The formatting for notes basically follows the format used by the original SplitNotes 
with some additional enhancements and exceptions.

1. Comment lines still use square brackets.
2. By default the splits will break on newlines. Multiple newlines and comments are ignored.
3. The notes are now rendered as HTML and so can be formatted as such.

   This means that it's easy to emphasise important part of the notes using basic HTML tags such as
   `<strong>`, `<em>`, and `<mark>`.
   
   The formatter will automatically insert HTML breaks `<br>` between lines, 
   a backslash `\ ` at the end of a line will indicate that the line should **not**
   have a break inserted (useful for headers and lists).
   
## splitnotes2_server.exe ##

Now included is a server version which launches a (local) webhost so you can view the splitnotes
on another device on your local network. Launch splitnotes2_server.exe to start the service.

If the hostname and port defaults aren't usable you can set them by editing server_hostname 
and server_port in settings.json. There is no dialog for editing these settings yet.
   
### Example Notes ###

#### Source ####

```html
<h3>Moonlight Butterfly</h3>\
<em>Buy Crest of Artorias, Tower Kite Shield and max-1 large arrows</em>
<strong>Prompt swap 99 titanite shards</strong>
In Butterfly Fight:\
<ul>\
  <li>Prepare DGH equip in weapon slot 1</li>\
  <li>Sort souls to top of inventory</li>\
  <li>Equip Homeward Bone</li>\
  <li>Mouse cursor in place for prompt swaps</li>\
</ul>\
Kill Moonlight Butterfly (3 Soul Spears)
Darksign

<h3>Lord Vessel</h3>\
Warp to Firelink Shrine
In the warp sort Butterfly's soul above Estus
Talk to Frampt and place the Lordvessel
Warp back up with Frampt
<em>Use prompt swap to sell 99 of each of each soul</em>
<strong>Buy Homing Soulmass and Soul Spear from Griggs</strong>
Homeward Bone

<h3>Hydra</h3>\
<mark>Level 23ATT 15END 10STR 45DEX 66INT</mark>
<strong>Attune FC/GSA/Homing/Spears/Spears/GHSA</strong>
DGH Fall RTSR Setup
Kill Hydra (3 soul spears)
Quitout after obtaining the items
Kill the Gold Crystal Golem
Talk to Dusk
Summon Dusk and buy Hidden Body
Darksign
```

#### Result ####

![Image of splitnotes rendering](resources/demo_notes.png)

## Configuration ##

The settings page offers some customisation and connection settings including:

  * Server hostname and port
  * Show previous/next N splits
  * Custom split separator
  * Base font size
  * Default text and background colour
  * HTML (Jinja2) template and CSS files to use for rendering

--- 

Inspired by (but otherwise unassociated with) the original splitnotes: https://github.com/joeloskarsson/SplitNotes

[*] approximately 19x larger in file size :) (Mostly Qt and PySide2)
