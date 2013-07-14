# SublHandler.app

A small app to send `subl://` URLs to Sublime Text 2, written using AppleScript and Python.

## URL Scheme

SublHandler.app supports the following URL scheme:

- Protocol: `subl://`
- Path: Any local file or directory; supports `~`, but not `..`
- Params (optional): 
	- Line: Defaults to 1
	- Column: Defaults to 1

All together now:

```
subl://~/Sites/project/
subl:///etc/paths?line=2
subl:///etc/paths?column=5
subl:///etc/paths?line=2&column=25
```

Note that the `line` and `column` parameters will not apply to directories, for obvious reasons.

## Installation

[Download a binary](//github.com/karoun/SublHandler.app/releases) from the releases page.

*Note*: Mountain Lion users will have to allow unsigned binaries in their Security preferences.

Also, make sure that you have both Python and the [`subl` alias installed](http://www.sublimetext.com/docs/2/osx_command_line.html).

## Credit

Icon: [Elliot Jackson](http://drbl.in/gkCw) via [Alex MacCaw](http://blog.alexmaccaw.com/sublime-text)

Idea: [Andrew Sutherland](//:github.com/asuth)
