#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.
!x:: ; alt+x
Click, 2
Sleep 100
; Send, ^+{Right down}{Right up}^+{Right down}{Right up} ; Works for FantasyPros
Send, ^+{Right down}{Right up} ; Works for ESPN
Sleep 300
Send, ^c ; copy selected text
Sleep 200
Send, {Alt down}{tab}
Send, {Alt up}
Sleep 200
Send, ^v ; paste
Sleep 200
Send, ^s ; save
Sleep 200
Send, {Enter}-{Space} ; start a new line
Sleep 200
Send, {Alt down}{tab}
Send, {Alt up}
Sleep 200
Click, down
Click, up
return