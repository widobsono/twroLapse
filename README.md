# TwRO-Lapse

Simple Raspberry camera timelapse, using piCamera. With special scheduling and flexible settings. Inspired by [Geerling's Timelapse](https://github.com/geerlingguy/pi-timelapse) and [Jacquin's Pi-AllSky](https://github.com/thomasjacquin/allsky). The ui will be based on Pi-AllSky GUI.

The python script will take some images and then convert it to `.mp4` using `ffmpeg`.

#### Run on Startup
Copy the `twrolapse.service` file into the `Systemd` unit file location: `sudo cp twrolapse.service /etc/systemd/system/twrolapse.service`

Reload the Systemd daemon (`sudo systemctl daemon-reload`) to load in the new unit file. To Run on Boot `sudo systemctl enable twrolapse`


#### TODO List
- [x] `2021/07/09` Initial test, taking pictures and convert to `.mp4`
- [x] `2021/07/12` Auto-Run on Startup using `systemctl service` and tidy up scheduling
- [ ] Making `install.sh` script for requirements and dependencies, easy-install :)
- [ ] Saving log-files
- [ ] Build callibration script (Dark, Flat and Bias)
- [ ] Auto-sync with cloud Storage

#### Updates Log
`2021/07/09` v0.1.0 First Build

`2021/07/12` Add Scheduling, Start on Boot and Video Maker
- Time divided into 3 parts, Day (06-18), Night PM (18-24) and Night AM (00-06), mainly because camera settings
- Start on boot using `systemctl` thanks to [Geerling's Timelapse](https://github.com/geerlingguy/pi-timelapse)
- Integrate a simple python script to generate timelapse video, we have to set the time of creating the timelapse inside `twro.config` under the `[Storage]` section.
