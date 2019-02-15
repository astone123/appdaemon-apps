AppDaemon apps that run on my Home Assistant server 🏡

## Configuration

- Hassio 2.8
- Hassio AppDaemon addon using AppDaemon version 3

To run these apps with the Hassio AppDaemon addon, you need to specify the following dependencies in your configuration:

```json
"system_packages": [
    "build-base",
    "python-dev python3-dev",
    "jpeg-dev",
    "zlib-dev",
    "freetype-dev",
    "lcms2-dev",
    "openjpeg-dev",
    "tiff-dev",
    "tk-dev",
    "tcl-dev",
    "harfbuzz-dev",
    "fribidi-dev"
  ],
  "python_packages": [
    "colorthief"
  ]
```

## Apps

- [HADashboard](https://www.home-assistant.io/docs/ecosystem/hadashboard/) (my configurations are under `dashboards/`)
- [Music Lights](https://github.com/astone123/appdaemon-apps/blob/master/apps/music_lights.py)
