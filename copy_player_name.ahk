#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.
^+x:: ; ctrl+shift+x
Click, down
Click, up
Click, down
Click, up
Sleep 100
; Send, ^+{Right down}{Right up}^+{Right down}{Right up} ; Works for FantasyPros
Send, ^+{Right down}{Right up} ; Works for ESPN
Sleep 100
Send, ^c ; copy selected text
Sleep 100
Send, {Alt down}{tab}
Send, {Alt up}
Sleep 100
Send, ^v ; paste
Sleep 50
Send, ^s ; save
Sleep 50
Send, {Enter}-{Space} ; start a new line
Sleep 100
Send, {Alt down}{tab}
Send, {Alt up}
Sleep 100
Click, down
Click, up
return