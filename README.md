# TwRO-Lapse

Simple Raspberry camera timelapse, using piCamera. With special scheduling and flexible settings. Inspired by [Geerling's Timelapse](https://github.com/geerlingguy/pi-timelapse) and [Jacquin's Pi-AllSky](https://github.com/thomasjacquin/allsky). The ui will be based on Pi-AllSky GUI.

The python script will take some images and then convert it to `.mp4` using `ffmpeg`.

#### Run on Startup
Copy the `twrolapse.service` file into the `Systemd` unit file location: `sudo cp twrolapse.service /etc/systemd/system/twrolapse.service`

Reload the Systemd daemon (`sudo systemctl daemon-reload`) to load in the new unit file. To Run on Boot `sudo systemctl enable twrolapse`


#### TODO List
- [x] `2021/07/09` Initial test, taking pictures and convert to `.mp4`
- [x] Auto-Run on Startup using `systemctl service` and tidy up scheduling
- [ ] Saving log-files
- [ ] Build callibration script (Dark, Flat and Bias)
- [ ] Auto-sync with cloud Storage

#### Updates Log
- `2021/07/09` v0.1.0 First Build
