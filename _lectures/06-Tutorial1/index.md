---
layout: default
usemathjax: true
title: "Tutorial: An Introduction to the Einstein Toolkit"
author: Roland Haas
institution: National Center for Supercomputing Applications 
shortinst: NCSA
# upload your slides as slides.pdf
# upload your recorded talk as recording.mp4
# all other files in this directory will show up as "additional files"
# alternatively you can override by uncommenting and giving an explict URL:
slides: 
recording: 
---
{% include base.html %}

{%-capture abstract-%}

This course covers the basics of the Einstein Toolkit:

1. A brief history;
2. what the Einstein Toolkit is and can do;
3. How to install the ET (including prerequisites);
4. How to run the ET and create a rudimentary plot of some of the data generated.

All of the above steps are carried out within a Jupyter notebook. This means that there are no hardware requirements for your computer.

Familiarity with the linux command line is required, and some minimal knowledge of Python is helpful.

Note that this course replicates the material available in the online tutorial.

{%-endcapture-%}

<div class="col-xs-12" markdown="1">
{% include lecture.md abstract=abstract %}

## Tutorial server instructions

For the hands-on part of the tutorial we will be using a cloud based
environment to simplify setting up the toolkit, hosted at [Perimeter Institute
of Theoretical Physics](https://www.perimeterinstitute.ca/).

There are two different environments offered:

1. for the Einnstein Toolkit and Self Force 1D tutorials on Monday and Tuesday
2. for the CarpetX tutorial on Friday

Please make sure to select the correct one for the tutorial you are attending.

Each environmen will be available only for the duration of each tutorial.
Data stored persists in between logins but will be removed after the end of the
workshop.

### Creating accounts

Please go to
[https://et2022uidaho.ncsa.illinois.edu](https://et2022uidaho.ncsa.illinois.edu)
and choose a user name and password. Make sure `Password` and `Password2`
match, otherwise account creation will fail.

You will also need to enter a security code into the `Code` field. This code
will be shared at the tutorial days via whiteboard and Zoom chat. Please do not
share that code with anyone.

Account creation is automatic and your account is active the moment you submit
the account creation form.

### Loging in

Once your account has been created you can log in via
[https://et2022uidaho.ncsa.illinois.edu](https://et2022uidaho.ncsa.illinois.edu)
filling out only the `User` and `Password` fields.

### Transferring data out of the tutorial environment

Please select the files you would like to download in Jupyter's file maneger
then use the `Download` button in the toolbar above the list of files to
download them to your laptop.

### Editing files

Jupyter has built in editor for text files that opens automatically if you click
on a source code file.

You can create new files using the `New` button in the file listing and
selecting `Text document`. Once the editor starts up you can rename the file
using the `File/Rename` menu item.

### Restoring your account to a pristine state

If your setup has become corrupted and you would like to start over again from
a fresh setup, please do the following:

1. start a Terminal using the `New` button in the file listing
1. remove all files from your home directory using the command `rm -rf $HOME`
1. stop your environment using the `Quit` button
1. log back in using [https://et2022uidaho.ncsa.illinois.edu](https://et2022uidaho.ncsa.illinois.edu)

This will restore all files to the state they were at your initial login.

[Edit on GitHub](https://github.com/EinsteinToolkit/et2021uiuc/edit/master/{{page.path}})
</div>
