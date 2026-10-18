# restore pinch gesture on macos tahoe

MacOS Tahoe removed the  four-finger pinch gesture that could be mapped to open apps window or 'launchpad'.

Here's how to restore it:

```bash
defaults write -g TrackpadFourFingerPinchGesture -int 2
defaults write -g TrackpadFiveFingerPinchGesture -int 2

defaults write com.apple.AppleMultitouchTrackpad TrackpadFourFingerPinchGesture -int 2
defaults write com.apple.AppleMultitouchTrackpad TrackpadFiveFingerPinchGesture -int 2

defaults write com.apple.driver.AppleBluetoothMultitouch.trackpad TrackpadFourFingerPinchGesture -int 2
defaults write com.apple.driver.AppleBluetoothMultitouch.trackpad TrackpadFiveFingerPinchGesture -int 2

killall cfprefsd
killall Dock
```

restart your machine.