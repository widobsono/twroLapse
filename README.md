# TwRO-Lapse

Simple Raspberry camera timelapse, using piCamera. With special scheduling and flexible settings. Inspired by [Geerling's Timelapse](https://github.com/geerlingguy/pi-timelapse) and [Jacquin's Pi-AllSky](https://github.com/thomasjacquin/allsky). The ui will be based on Pi-AllSky GUI.

The python script will take some images and then convert it to `.mp4` using `ffmpeg`.


#### TODO List
- [x] `2021/07/09` Initial test, taking pictures and convert to `.mp4`
- [ ] Auto-Run on Startup using `systemctl service` and tidy up scheduling
- [ ] Saving log-files
- [ ] Build callibration script (Dark, Flat and Bias)
- [ ] Auto-sync with cloud Storage

#### Updates Log
- `2021/07/09` v0.1.0 First Build
