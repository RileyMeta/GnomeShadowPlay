# GnomeShadowPlay
A ShadowPlay-like replacement for GTK.

## Goals of this project
To provide the user with a near one-to-one implimentation of Nvidia ShadowPlay by using a GTK and Python wrapper on top of [GPU-Screen-Recorder](https://git.dec05eba.com/gpu-screen-recorder/about/). 
> [!NOTE]
> Your GPU Hardware should not matter, but please double-check the GPU-Screen-Recorder documentation to make sure there are no tweaks you need to apply.

## Project Design
Right now the project is being written in GTK and Python with a simple structure:
```
└── GPU Replay App/
    ├── main.py
    ├── assets/
    │   ├── recording.svg
    │   ├── recording_stop.svg
    │   ├── replay.svg
    │   ├── streaming.svg
    │   └── streaming_stop.svg
    ├── error_notification.py
    ├── recording_notification.py
    ├── replay_notification.py
    └── streaming_notification.py
```
`main.py` will be ran at system startup, completely invisible to the user, until opened with either a key-combo (default is `Alt`+`z` but can be changed) or by the opening the app from the menu. It will also manage all the individual settings for each action inside GPU-Screen-Recorder, along with housing the individual settings for each action:
> - Recording will have location, audio and screen settings (which will also apply for the Replay).
> - Streaming will have Bitrate, streamkey/login and audio setitngs.
> - Replay will have it's time limit and custom keypress combos to save the replay.
> - There will also be an individual settings button that allows you to manage settings in more detail.
> - An `X` in the top right corner that allows you to close the pop-up if the `Escape` key or other ways do not work.

Each notification will handle the code for both Starting and Stopping their perspective actions, along with some simple functions that change the text and icon based on the action being used.

## Notification Example
[Screencast from 2024-05-17 14-13-42.webm](https://github.com/RileyMeta/GnomeShadowPlay/assets/32332593/08b5e857-ff34-428f-85d0-5ca73294a6c2)


## To-Do List
Finish main.py (the current one is a proof of concept)
- [ ] Create the Settings
- [ ] Create the GUI
- [ ] Create the Calls for individual notifications
- [ ] Add Error Handling

Finish the Notifications
- [ ] Add the individual settings
- [ ] Add the functions for Starting and Stopping
- [ ] Add Error Handling
