# Guided Project - Sprint 1 Module 3

## What is Docker?

Docker is a tool for spinning up "containers." containers are basically light-weight operating systems complete with any tools that we specify, that can be easily recreated or "shipped" along with our projects. The hope is that if we can specify not only our project setup and package dependencies (pipfile) but also our entire *operating system* setup then we can put an end to the problems of something working on one person's machine but not another's.

![and Docker was born meme](/images/docker-was-born.jpeg)

Docker is controlled through a Command Line Interface (CLI) so we're going to be doing all of our work with docker from the Command line.

## What is a Dockerfile?

A Dockerfile is a text file where we indicate the operating system of the container that we want to build as well as any tools that we would like to be installed in that operating system. When we execute this file using docker it will create a Docker Image. The purpose of the Dockerfile is to make it easy for us as humans to give the operating system specifications in one place using fairly simple commands.

## What is a Docker Image?

An image is a ready-to-go operating system with all of the tools that we indicated in the Dockerfile already installed to it. Sometimes the installation of these tools takes a long time, so if we need to quickly spin up a container, we can do so in miliseconds with this pre-built "image". I don't know why they used that word for it. I think it's really confusing. A better word for it would be a ready-to-go "template" or "snapshot" of the operating system.

## What is a Docker Container?

A docker container is a running version of the operating system that gets built from the image. The image basically sits on standby until we tell it to turn on. Once it's on and running it is officially a Docker Container.

The process of building Docker Containers is always as follows:

Dockerfile --> Image --> Container

## Guided Project Walkthrough

You will need to create a [Docker Hub account](https://www.docker.com/get-started) in order to use the interactive playground that we will be using to explore Docker.

Once you have an account visit the [Docker Playground](labs.play-with-docker.com) and log in with your Docker Hub account, and then hit the "Start" button.

![Play with Docker](/images/play-with-docker.png)

Click "Add New Instance"

![Add New Instance](/images/add-a-new-instance.png)

Check to make sure our instance has Docker

(The dollar signs at the front just tell you that this is a Command line command, you don't need to include the dollar sign in what you type in the Command Line.)

`$ docker --version`

If you're trying out these commands on your local machine, the above command might not do anything for you until you have download docker to your machine.

![The same command but on my machine](/images/docker-on-my-machine.png)

When we create a new instance the playground starts running a Virtual Machine in our browser - Basically mimicking each of our own local operating systems. The virtual machine that the playground gives us is a Linux-based virtual machine running an operating system called "Alpine" (There's a million and one different Linux operating systems, this is just one of them). So you may see a different file structure on this virtual machine than what you're used to on your local operating system, but the major commands that we have been using in Git Bash should be the same as what we're going to use in the Docker playground (and the same as what you're going to try out on your own during the assignment on your local machine.)

Try a few commands

`$ ls`

`$ ls -1`

Navigate around through the Alpine Linux files for a second to orient yourself. Good luck, there's not really anywhere to go.

Many Command Line tools have help documentation that you can access within the command line to know what possible commands you might run.

`$ docker --help`

Run a command in a new container.

`$ docker run hello-world`

Hello world is a pre-defined Docker image that is going ot create a container.

![Docker has lots of shared images](/images/a-library-of-shared-docker-images.png)

To try something more ambitions, you can run a Ubunto container with: docker run -it ubuntu bash. Lets try it!

`$ docker run -it ubuntu bash`

This run command will actually build our first container that contains an operating system! We'll be using Ubuntu which is another (quite popular) flavor of Linux.

the `-it` flag in the above command makes the new container interactive

the inclusion of `bash` at the end automatically launches the command line of our new Ubuntu operating system inside of the new container.

Leave the container by using the `$ exit` command

`$ exit`

Now we're going to practice setting up a whole container with a few of the tools that we would need to run a python project. Once this is done we would theoretically be able to not only ship our project and dependencies with our pipfile, but also provide all of the operating system configurations for our project by providing the container image as well.

Create a new Ubuntu container:

`$ docker run -it ubuntu bash`

Because we're in a Ubuntu operating system we have to run Ubuntu-friendly commands.

`$ apt update`

`$ apt upgrade`

Next we're presented with a yes or no question. This question shows one of the beautiful things about containers. With containers we don't predefine a certain amount of resources that it has access to from the get-go. Rather, the container prompts us when it needs more resources for us to give it permission to use those resources. In this way the container is always running with "no space left on device."

![No Space Left on Device](/images/no-space-left-on-device.png)

However, answering these yes or no questions is something that we'll have to build into our Docker images so that if we want to automate the setup of this same container, we will be able to automatically answer these yes or no questions.

You can answer yes by simply typing the letter "y" as a command line command

`$ y`

Next we'll install Python3 to the container.

`$ apt install python3`

Give the container permission to use additional resources

`$ y`

Run a little python REPL by running `python`

`$ python`

Play around in the REPL a little bit. You'll see that it's the same REPL we've been working with all week, it just doesn't have access to our package because our package isn't in the container yet.

Exit the REPL

`$ exit()`

Install pip and curl all in one go

`$ apt install python3-pip curl`

Curl is a tool that will allow us to download non-python related packages to our container.

Make sure we have pip3 after installing it.

`$ which pip3`

`$ which python3`

Install Pandas and Numpy!

`$ pip3 install pandas numpy`

Start the python REPL again, but this time import pandas and numpy and use them to do something inside of the REPL to prove to ourselves that they installed correctly and that we have access to them.

`$ python`

Inside of the REPL:

`>>> import pandas as pd`
`>>> import numpy as np`
`>>> pd.DataFrame()`

Now let's exit our container

`$ exit`

Now that we're back in Alpine, lets try and use numpy and Pandas in our base Alpine operating system.

First we'll make sure we have Python. This command should work because the Alpine operating system in the playground comes with python pre-installed for us.

`$ which python3`

Start the REPL.

`$ python3`

Try using NumPy and Pandas

`>>> import pandas as pd`
`>>> import numpy as np`
`>>> pd.DataFrame()`

Doesn't work, does it? That's because we didn't install NumPy and Pandas to Alpine, we only installed them inside of our Ubuntu container. This is just showing that we truly were in a complete separate operating system running inside of a container.

Let's go back into a new Ubuntu container

`$ docker run -it ubuntu bash`

Check for Python

`$ which python3`

We don't have it, because this new Ubuntu container is different from the last one we made, it's fresh and blank and we'd need to run all of the same commands that we ran above to get back to the point where we had python, numpy, and pandas. What a pain right? Maybe there's a way that we could just run all of the commands that we want to all at once...

There's a problem though. That we only have access to the playground through the command line, so we can't just open up VSCode in here to make a dockerfile. We need to use a text editor that can run in the command line, so we'll use one called "nano."

Check for nano.

`$ which nano`

Install nano. We want to install this to the Alpine machine whose commands for installing things start with `apk`

`$ apk --help`

From the help command we learn that we can install packages using the `add` command.

`$ apk add nano`

Check for successful installation.

`$ nano --version`

Make a dockerfile using nano. It is *very* important to capitalize the name of this file.

`$ nano Dockerfile`

If ther's no Dockerfile in the directory that we're currently in then nano will create it. If there is one available then nano will open it for us to edit.

Specify the OS of the container right at the top of the Dockerfile

```
FROM ubuntu  

# just helps python run a little faster
ENV PYTHONBUFFER=1

RUN apt update && apt ugrade -y && apt install python3 python3-pip curl -y && pip3 install numpy pandas
```

And that's a Dockefile! However, there's one improvement that I'd like to make to the file to make it a little more readable. Our `RUN` command is getting a little long, we can use back slashes `\` to break it up into new lines.

```
FROM ubuntu  

# just helps python run a little faster
ENV PYTHONBUFFER=1

RUN apt update && \
    apt ugrade -y && \
    apt install python3 python3-pip curl -y && \
    pip3 install numpy pandas
```

When you're done editing, exit out of nano by pressing `ctrl + x` or `command + x` if you're on a mac.

It will ask you if you want to save the file, enter `y` for "yes." and then hit `enter` to save the file under the same filename as it had previously.

We can display the contents of our Dockerfile to the terminal to look at it. This is sometimes easier than entering nano if we just want ot make sure that it has everything in it that we want.

`$ cat Dockerfile`

Let's use the help command to figure out how to build an image from this Dockerfile.

`$ docker --help`

Build the image. the `.` tells docker to look in our current directory for a dockerfile. It will automatically find it and use it. We can also indicate the name of the dockerfile explicity if we wanted to:  `$ docker build Dockerfile`. The `-t` flag allows us to provide a name or "tag" for the image. We'll call ours `myimage`. The image name *has* to be lowercase.

`$ docker build . -t myimage`

If had published our lambdta package to PyPI we could have it be installed along with Pandas and Numpy, that would be so cool!

Now we can start up a container with all of the settings that were installed in our image very quickly by running

`docker run -it myimage bash`

So our Dockerfile is like our pipfile that holds all of our configurations. The Docker image is like a blank version of our operating system with all of the tools pre-installed, and we can easily sping up as many versions of that operating system complete with tools and packages in miliseconds now.

Check to see that the tools were actually installed by playing around with Python, pandas, numpy, curl, pip3, etc.

Ok, so we're done with the container, lets destroy it for fun to teach a vauable lesson. Let's commit the cardinal sin.

DO **NOT** DO THIS ON YOUR LOCAL MACHINE, JUST ON THE PLAYGROUND.

DO **NOT** DO THIS ON YOUR LOCAL MACHINE, JUST ON THE PLAYGROUND.

DO **NOT**DO THIS ON YOUR LOCAL MACHINE, JUST ON THE PLAYGROUND.

`rm -rf *`

DO **NOT** DO THIS ON YOUR LOCAL MACHINE, JUST ON THE PLAYGROUND.

DO **NOT** DO THIS ON YOUR LOCAL MACHINE, JUST ON THE PLAYGROUND.

DO **NOT** DO THIS ON YOUR LOCAL MACHINE, JUST ON THE PLAYGROUND.

This will delete everything in the container, but leave our Alpine system untouched. So if you ran this same command in your regular bash it could delete your whole operating system. There are not as many fail-safes in place as you might think there should be when doing something like this.

The exit command will take us back to our untouched Alpine machine.

`exit`

And that's pretty much it!

---

Let's try out some other commands for kicks.

List the docker images that we have made/used:

`docker image ls`

Remove images by id

`docker image rm <id>`

List running containers

`docker container ls`

List all containers that we have made even if they're note running

`docker container ls -a`

Remove containers even if they're not running

`docker container rm -f <id>`

Start up a container

`docker container start <id>`

Check to see that it's running

`docker container ls`

Close down the container without having to go into its bash and type `exit`.

`docker container kill <id>`