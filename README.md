# SublHandler.app

A small app to send `subl://` URLs to Sublime Text 2, written using AppleScript and Python.

## URL Scheme

SublHandler.app supports the [same URL scheme as TextMate](http://manual.macromates.com/en/using_textmate_from_terminal.html):

- Protocol: `subl://`
- Path: `open`
- Params:
	- URL: Any local file or directory; supports `~`, but not `..`, `file://` is optional
	- Line (optional): Defaults to 1
	- Column (optional): Defaults to 1

All together now:

```
subl://open/?url=~/Sites/project/
subl://open/?url=file://~/Sites/project/
subl://open/?url=/etc/paths&line=2
subl://open/?url=/etc/paths&column=5
subl://open/?url=/etc/paths&line=2&column=25
```

Note that the `line` and `column` parameters will not apply to directories, for obvious reasons.

## Installation

[Download a binary](//github.com/karoun/SublHandler.app/releases) from the releases page.

*Note*: Mountain Lion users will have to allow unsigned binaries in their Security preferences.

Also, make sure that you have both Python and the [`subl` alias installed](http://www.sublimetext.com/docs/2/osx_command_line.html).

## Credit

Icon: [Elliot Jackson](http://drbl.in/gkCw) via [Alex MacCaw](http://blog.alexmaccaw.com/sublime-text)

Idea: [Andrew Sutherland](//github.com/asuth)
