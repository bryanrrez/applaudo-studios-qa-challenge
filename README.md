## Code Challenge - Appium + REST Assured

### Requeriments

You'll need to install Python on your computer. Here I'll leave the link to Python [page](https://www.python.org/), so you can install the lastest version.

Also, you will have to install Appium Server or Appium Client, whichever you feel more comfortable with. Android Studio is a must since it will help you emulate an Android device so you don't need to use a physical device to run the mobile test developed.

I will add couple of links to YouTube so you can setup your PC to be able to run the mobile tests. API tests don't need any dependencies other than the ones that will be install with the virtual environment.

**Note**: Python version 3.8 or later is required.

#### Links

[How to install Appium on MacOS](https://www.youtube.com/watch?v=7APcLr-cBM8&list=PLhW3qG5bs-L8npSSZD6aWdYFQ96OEduhk&index=5)

[How to install Appium on Windows](https://www.youtube.com/watch?v=x-hBpgM5je8&list=PLhW3qG5bs-L8npSSZD6aWdYFQ96OEduhk&index=4)

[How to connect a real android device on Windows](https://www.youtube.com/watch?v=82KXSli1wPA&list=PLhW3qG5bs-L8npSSZD6aWdYFQ96OEduhk&index=6)

[How to connect a real android device on MacOS](https://www.youtube.com/watch?v=BEF-d1xjV4Q&list=PLhW3qG5bs-L8npSSZD6aWdYFQ96OEduhk&index=7)

[How to install APK file on Virtual Device (emulator) using Appium Server Desktop](https://www.youtube.com/watch?v=8zS55sXr_7M)


### How to install?

After you install Python you have to install a Python library called pipenv. This library will help you to setup the project on a virtual environment.

To install it, just run the script `pip3 install pipenv` on a Terminal or Command Prompt.

After you successfully install pipenv, proceed to execute the command `pipenv install` on the project directory using a Terminal or Command Prompt. You will note that all dependencies such as Selenium and Pytest will start to download and install.

When everything is done proceed to execute `pipenv shell` on the project main directory to enter the virtual envrionment created by pipenv. After this you proceed to execute the command `pipenv run pytest`, this command will run all test cases detected by pytest, which is a Python test framework.

### How do you know you are already inside the virtual environment?

While being on the Terminal or Command Prompt, and after executing the command `pipenv shell` you will note that the path suddenly change and starts with the name of the project as a prefix.

### How to run the project?

The first thing to note is that the project counts with a config file where you have to specify the `deviceName` and `platformVersion` of your Android device.

After setting that up, it's turn to execute the command `pipenv run pytest` on the main directory. It should start to run all the test cases developed.