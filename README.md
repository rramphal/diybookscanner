# Noisebridge DIY Book Scanner

## Dependencies

#### Linux

* `apt-get install gphoto2` on your **Debian**-based distro
* `yum install gphoto2` on your **Fedora**-based distro

#### macOS

1. [Install Homebrew](http://brew.sh/)
2. `brew install gphoto2`

**NOTE**: On Mac, the *PTPCamera* process often takes control of the camera.
This script will automatically kill any running processes.

## Running

This is a scanning script provided for use with the [Noisebridge](https://www.noisebridge.net/) [book scanner](https://www.noisebridge.net/wiki/Book_scanner).
It captures and saves images from cameras via the *gphoto2* library.

To use, make a new directory for the book to be scanned.
Copy in the relevant script from this repo and
run the script from within that directory (usually `python scan.py`).
Follow the prompts from the scripts to capture images.
Images will be saved as `imgXXXXX.jpg` in the current directory.

Images from both cameras are captured every time the enter key is pressed.
The capturing with two cameras, the script also writes out an HTML file
which can be used to view the images as they are scanned.

**NOTE**: It has been observed that sometimes *MacBook Pro*s
seem to confuse multiple USB cameras with the same name,
interpreting them as one camera jumping between ports.
One solution is to use two computers, each attached to a single camera
(one for the left and one for the right)
and both run the `scan_single_camera.py` script
modified for use with a single camera.
Unfortunately, this means that you'll have to
press ENTER on both computers to advance scanning.

*The single camera script has been stripped of the
HTML preview file function and will not rotate the images.
In the future, it will be improved to allow the user to specify
whether or not the current camera is being used to scan
left pages or right pages, allowing for the script
to rotate the images.*
