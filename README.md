# Open fuji recipes Profiles

collection of Film Simulation Recipes parsed from [matthieurobin/open-fuji-recipes](https://github.com/matthieurobin/open-fuji-recipes/) and converted into profiles you can use in Fuji X Raw Studio.

## Motivation
I was inspired by [plamf/fuji-x-weekly-simulation-profiles](https://github.com/plamf/fuji-x-weekly-simulation-profiles) that allows you to use many recipes at once.
So I created this to use more recipes.

## Disclaimer
I can't confirm that every value in every recipe is 100% accurate, but I have tested it.
I only have an X-Trans IV sensors camera, so I only made it for that.


## how do I use these Profiles with Fuji X Raw Studio?
### Prerequisites
1. Python 3.10 (I recommend typing `python` in the command prompt and installing it from the Windows store, otherwise install from here https://www.python.org/downloads/)
2. Fuji X Raw Studio (https://fujifilm-x.com/en-gb/support/download/software/x-raw-studio/)

((Optional)) If you want to do the conversion yourself, you'll need to `pip install lxml`

### Making the profiles work with your camera
1. You'll need to create a master profile with X Raw Studio to use as a template. This is needed because we have to copy your camera model, serial number and some other fixed values to the profiles in order to make them work. You don't need to apply any special settings, since we will only use this profile as an empty husk for metadata. You have to do this for every different camera model you're using.
2. Find the profile you just created. On Windows, they are usually here `%USERPROFILE%\AppData\Local\com.fujifilm.denji\X_RAW_STUDIO`, or on Mac `~/Library/Application Support/com.fujifilm.denji/X_RAW_STUDIO`
3. Copy the path of your master profile
4. clone the repo or download from releases
5. Open a command shell/terminal in the cloned folder and run 'git submodule init & git submodule update'
6. Open a command shell/terminal in the folder with your profiles of choice and run this command on Windows: `python fx-templater.py "path/to/your/master/profile.FP1"`, or on Mac: `python3 fx-templater.py "path/to/your/master/profile.FP1"`
7. The converted profiles should appear in a subfolder called `converted`
8. Copy the profiles into the same path where you got your master template from
9. You can now delete the master template and start Fuji X Raw Studio. All the profiles should be there!

## Additional resources
Please contribute to https://github.com/matthieurobin/open-fuji-recipes/ to make more recipes available.

I used `fx-templater.py` as it is in [plamf/fuji-x-weekly-simulation-profiles](https://github.com/plamf/fuji-x-weekly-simulation-profiles)
If you like my work, be sure to check out that repository as well.

How to use simulation recipes in Fuji X Raw Studio and save them to your camera: https://www.youtube.com/watch?v=IrGVsvo0Dx0
