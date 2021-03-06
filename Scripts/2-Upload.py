#!/usr/bin/env python
import os
import json

# Get Steam settings
steamData = open("steam.json")
steamConfig = json.load(steamData)
steamSDKDir = steamConfig["sdkDir"]
steamBuilder = steamConfig["builder"]
steamCommand = steamConfig["command"]
steamAppFile = steamConfig["appFile"]
steamUser = steamConfig["user"]
steamPassword = steamConfig["password"]
steamData.close()

# Generate paths
buildAppFile = os.path.join("..", steamAppFile)
buildRootDir = os.path.join(steamSDKDir, "tools", "ContentBuilder")

# Generate full command line
commandLine = os.path.join(steamBuilder, steamCommand)
commandLine += " +login " + steamUser + " " + steamPassword
commandLine += " +run_app_build " + buildAppFile
commandLine += " +quit"

# Call
currentPath = os.getcwd()
os.chdir(buildRootDir)
os.system(commandLine)
os.chdir(currentPath)
