# NutritionBalancer
The code needed to run a hydroponics system on rasperry Pi

## Get the sensor libraries
### EC
git clone https://github.com/u-fire/Isolated_EC.git --depth=1
### SHT20
git clone https://github.com/u-fire/uFire_SHT20.git --depth=1
### ISE
git clone https://github.com/u-fire/Isolated_ISE.git --depth=1


## Install dependencies
pip3 install smbus


Raspberry Pi
Before you can run anything, you will need to enable software I2C; the Pi's hardware implementation has a clock-stretching bug that will prevent it from working with the probe (or any other device that uses clock-stretching).

sudo nano /boot/config.txt and scroll to the bottom
Add dtoverlay=i2c-gpio,i2c_gpio_sda=<pin>,i2c_gpio_scl=<pin> replacing <pin> with whatever pin you'd like to use. Refer here for the pin functions, you will need to use the orange GPIO xx labels in the picture to locate the pins.
ctrl + x to exit, y to save, and enter to confirm the filename.
Reboot

dtoverlay=i2c-gpio,i2c_gpio_sda=2,i2c_gpio_scl=3