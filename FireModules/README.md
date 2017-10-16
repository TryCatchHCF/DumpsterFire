# DumpsterFire Toolset

DumpsterFire Toolset - "Security Incidents In A Box!"

The DumpsterFire Toolset is a modular, menu-driven, cross-platform tool for building repeatable, time-delayed, distributed security events. Easily create custom event chains for Blue Team drills and sensor / alert mapping. Red Teams can create decoy incidents, distractions, and lures to support and scale their operations. Turn paper tabletop exercises into controlled "live fire" range events. Build event sequences ("narratives") to simulate realistic scenarios and generate corresponding network and filesystem artifacts.

The toolset is designed to be dynamically extensible, allowing you to create your own Fires (event modules) to add to the included collection of toolset Fires. Just write your own Fire module and drop it into the FireModules directory. The DumpsterFire toolset will auto-detect your custom Fires at startup and make them available for use.

<img src=https://github.com/TryCatchHCF/DumpsterFire/blob/master/Screenshots/DumpsterFireMainMenu.png></img>

# Author

Joe Gervais (TryCatchHCF)

# Why

Red Teams and Blue Teams are typically overextended. What's missing is a way to scale each team's capabilites, providing more effective Red Team activity, and more realistic (and helpful) Blue Team / Purple Team exercises. Automation to the rescue! The DumpsterFire Toolset is a cross-platform menu-driven solution that allows you to easily create custom security incidents by combining modular, chained events into a consistent narrative. Those collection of events (DumpsterFires) can then be executed as time-delayed, automated processes. (They can also be triggered immediately, of course.)

The result? While you're in a meeting or out enjoying life, your DumpsterFire is waiting for its date-time trigger to activate. On a Red Team engagement, while you're busy exploiting that exposed service on a forgotten B2B server, your cloned & time-sychronized DumpsterFires are busy lighting up the target organization's SIEM on a far-away subnet, distracting their response team. Blue Teamers can turn table-top paper exercises into "live fire" range events, with controlled, pre-approved DumpsterFire event chains to trigger sensors and alerts, and train your analysts using their actual operational environment. Purple Team operations can now execute methodical, repeatable event chains to consistently map out their sensor and alerting posture. You can generate novel scenarios to test and train your teams, getting ahead of the threat space to be prepared for security contingencies.

Ever wondered how your Blue Team would respond to Mirai bot activity on your internal network? Now you can find out! (Don't worry, the Mirai bot Fire module doesn't pivot, but it does use the same usernames & passwords to brute-force telnet sessions across the target network.)

Don’t have a Red Team but wish you had an easy way to run controlled, repeatable, customized drills against all of your SOC shift teams? Done!

Wish you could support a Red Team engagement against a remote team that’s 7 timezones away, without waking up at 3:00am? Hit that snooze button!

Ever wanted to simultaneously rickroll all of your opponents’ systems during your annual cyberwarfare exercise? "Never gonna give you up!"

See sample DumpsterFires below. And of course the Shenanigans section.

# Tutorial
See my CactusCon 2017 slides (included in project). The slides are written to stand on their own, providing background, approaches, specific use cases, and more. They'll put everything in context, and also won't put you to sleep. Unless they do put you to sleep, in which case you probably needed some rest anyway, so really we all come out ahead here.

# Accountability

DumpsterFire creates a date-time stamped event log so that Red- and Blue teams can coordinate and track events, correlating them to what was detected (or not detected) by your sensors, which alerts did or did not trigger, etc. It also allows teams to confirm which events were part of your operation / exercise, keeping everyone out of trouble. All date-time tracking is performed in UTC, so your global operations can be easily correlated without worrying about conversions between timezones and international date lines.

The auto-generated date-time stamped event logs also provide an effortless value add to your engagements. Generate a collection of DumpsterFires for your client engagements, tailored to their attack surfaces. At the end of your operations you can hand over the logs as a bonus Purple Team deliverable to your client for post-engagement analysis.

<img src=https://github.com/TryCatchHCF/DumpsterFire/blob/master/Screenshots/FireDateTimeStamps.png></img>

# Overview

The DumpsterFire toolset workflow is designed to be user-friendly and robust. Everything can be done from within the menu-driven **dumpsterFireFactory.py** script. Launch the script and the tool will guide you as you go. You can start by browsing the existing Fire modules and saved DumpsterFires. When you're ready to create your own DumpsterFires, the tool will lead through the workflow to get the job done. Finally it will be time to ignite your DumpsterFire. After selecting the DumpsterFire of your choice, you'll review the DumpsterFire's Fire modules and settings. If everything looks good, light it up!

When you're building a DumpsterFire, after you've chosen all of the Fire modules you wish to include, the tool will loop through the list of Fires. If a Fire has options for custom settings, the tool will call that Fire's Configure() method to present you with prompts for its settings (e.g. a target network's IP address).

Once all of the Fires have been configured, you'll then be given the option to assign individual time delays to your Fires. This allows the DumpsterFire to better mimic real operations when executing its chain of events. For example, the first Fire may visit various hacking Websites, the next Fire then downloads a few common hacking tools before launching the third Fire which starts scanning the local network. If this all happened within seconds of each other, no SOC analyst is going to believe it was a human. By adding several minutes or even hours between those events, you create a more realistic chain of events.

After all of the Fires have been configured and optional individual Fire delays assigned, you'll be asked to name your DumpsterFire. Do not use spaces or odd special characterse, just stick to letters, numbers, underscores, and hyphens.

Voila! You have now created your first DumpsterFire. Time to light one up!

When you're ready to ignite a DumpsterFire, the tool will first show you the DumpsterFire's settings. If everything looks good, you'll be asked if you want to assign a date-time delay before igniting. All date-time processing is done in UTC to ensure consistent execution regardless of your DumpsterFire's location of execution. Otherwise you can decline the date-time delay and execution will begin immediately after you give final confirmation.

As the DumpsterFire executes, you'll be given regular date-time stamped feedback on each Fire's status and critical events. This not only helps you track progress, but also provides a chronological record of your DumpsterFire's activities - critical in coordinating and deconflicting your events from the general background noise that floods every SOC. You can also hand over the chronological record to your external clients after your operations are complete, as a value-added record of your activites that they can use to review their sensor and alert settings. All with no extra effort on your part.

# Shenanigans

April 1st happens! So do cyber wargames or your best friend's birthday. Some circumstances call for a little extra something. Finally infiltrate your opponent's perimeter in that net wars competition? Celebrate with Shenanigans while locking in your victory! Best friend leave their screen unlocked on game night? Sharing is caring! DumpsterFire's Shenanigans let you add some flavor to your operation. 

Want to open the system's default browser and stream all of that Rick Astley awesomeness? After setting their system volume to maximum? How about opening any URL you choose? Or setting the system's shell aliases to pretend the filesystem is corrupted? 

<img src=https://github.com/TryCatchHCF/DumpsterFire/blob/master/Screenshots/DumpsterFireShenanigans.png></img>

# Files & Directories

**dumpsterFireFactory.py** - Menu-driven tool for creating, configuring, scheduling, and executing DumpsterFires

**FireModules/** - Directory that contains subdirectories of Fires, each subdirectory is a specific Category of Fires to keep your Fire modules organized. Fires are added to a DumpsterFire to create a chain of events and actions.

**DumpsterFires/** - Directory containing your collection of DumpsterFires

**igniteDumpsterFire.py** - Headless script, invoked at command line with the filename of the DumpsterFire you wish to execute. Useful for igniting distributed DumpsterFires.

**testFireModule.py** - Utility script for unit testing the Class methods of your custom Fire modules, without the hassle of running through the entire DumpsterFire Factory process to debug. Also useful for running a single Fire to check your settings. **testFireModule.py** will prompt you for configuration settings were applicable.

**&#95;&#95;init&#95;&#95;.py** files - Required to make Python treat directories as containing Python packages, allows DumpsterFire toolset to find and load Fire modules.

# Requirements
Python 2.7.x

# Run DumpsterFire Factory
$ ./dumpsterFireFactory.py

# Creating a DumpsterFire:

The menu-driven DumpsterFire Factory script guides you through each step, with context-appropriate help along the way.

<img src=https://github.com/TryCatchHCF/DumpsterFire/blob/master/Screenshots/DumpsterFireBuildHelp.png></img>

# Sample DumpsterFires

In our first example, we have a DumpsterFire that could be either a SOC drill or a Red Team distraction. The DumpsterFire first does a Google search for hacking tools. The next Fire opens Web sessions to various hacking Websites. Next, a following Fire downloads some common hacking tools. Then a port scan targets the subnetwork, followed by bruteforce login attempts against a single host via Telnet. The final Fire runs a series of Linux commands. Note that between each Fire, the creator of this DumpsterFire has inserted some time delays. This makes the flow of events appear more realistic.

<img src=https://github.com/TryCatchHCF/DumpsterFire/blob/master/Screenshots/DumpsterFire_Wayward_Employee.png></img>

In the next example, Purple Teamers have created a DumpsterFire to help analyze and validate their sensor and alerting configurations. This DumpsterFire runs a choreographed series of port scans, each targeting different collections of ports & services, with varying probe rates as well. They've inserted a 5 minute delay between each scanning Fire to simplify isolating the traffic associated with each scanning Fire. When they run this DumpsterFire, they'll also see date-timestamps at the beginning of each Fire to help them deconflict the Fire's network activity vs. other network events.

<img src=https://github.com/TryCatchHCF/DumpsterFire/blob/master/Screenshots/DumpsterFire_Purple_Team.png></img>

# Customizing Your Dumpster Fires

DumpsterFire's modular design gives you flexibility to create any number of event-chain narratives. Fire modules that have configurable settings allow you to set target networks or system, etc. There are a few Fire modules, however, that give you immediate flexibility to greatly expand your DumpsterFire event sequences.

Without creating any new FireModule classes, you can use these existing "custom" Fire modules to leverage and extend your DumpsterFires:

- FireModules/Websurfing/custom_url.py
- FireModules/FileDownloads/download_custom_url.py
- FireModules/OSCommand/os_linux_unix_command.py
- FireModules/OSCommand/os_win_cmd_command.py
- FireModules/OSCommand/os_osx_applescript_command.py

You can add any number of these to your DumpsterFire, each with its own custom actions. For example, you could chain together a dozen 'custom_url.py' Fire modules to build a complete, tailored browsing narrative. You could then have various 'OSCommand/' Fire instances that execute system commands to further reinforce your desired narrative of events. The 'OSCommand/' Fires in particular give you incredible flexbility. Each individual Fire in your DumpsterFire event chain takes any shell commands that are appropriate for the host's OS:

Linux/Unix (& OSX terminal):

find /home -name '*.bash_history' -exec cat {} \; ; echo "Never gonna give you up" > rickroll.txt ; wall rickroll.txt

Windows (cmd.exe):

(Example)

OSX (AppleScript):

(Example)

# Write Your Own Custom Fire Modules

DumpsterFire is ready to use out of the box, but it's real value is in how easily you can extend DumpsterFire's scenario toolchest by creating your own custom Fire modules. By creating and tailoring Fire modules to match your specific needs, you can quickly expand the types of DumpsterFire scenarios you can build and execute. Simply write your new Fire module and drop it into an existing directory under FireModules/ and the DumpsterFire toolset will automatically load it at runtime & make it available.

Want to keep your custom Fire modules completely separate in their own Category? Easy! Just create a new directory under FireModules/ and the DumpsterFire toolset will auto-detect and make it available as a new Category of Fires.

<img src=https://github.com/TryCatchHCF/DumpsterFire/blob/master/Screenshots/DumpsterFire_Custom_Categories.png></img>

Your Fire module inherits from a class called FireModule. As a starting point, you can copy an existing Fire module. Be sure to change the filename and all classname references in the file to match your new Fire. (Update the Category path referencesin the class's constructor methods too, if needed.)

**Configure()** - Prompts user for input, populates FireModule’s parameters

**Description()** - Return a string containing a description of the FireModule

**GetParameters()** - Returns a single string of Fire's parameters

**SetParameters( string )** - Takes a single string & populates Fire's members

**ActivateLogging( boolean )** - Sets flag for Fire to generate a log of its activities (great for review) NOTE: For initial release, logging to stdout is always on.

**Ignite()** - Executes Fire's actions

# Utility Scripts

Testing Python classes can be annoying, especially when you want to unit test each of the class's methods, forcing you to slog through all the application's use cases to make sure each class method is executed in proper order. Bleh. So I've written and included a script that will properly invoke each method of your new FireModule-derived classes, enabling you to quickly churn-and-burn your way through debugging. You're welcome. :-)  Also a great way to run a Fire by itself to test your settings, see what it does, etc.

At the command line, give the **testFireModule.py** script the relative filepath to your custom Fire module. The test script will call each of the required FireModule methods for you, in proper sequence (getting configuration prior to saving, etc.). The test script doesn't use exception handling, because Python only gives you useful errors (like pointing out that missing double-quote) when it crashes. Crash and burn your way to a successful custom Fire!

