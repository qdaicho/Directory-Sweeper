## Inspiration
My folders are always messy. That's why I decided to program a solution to this problem.

## What it does
When you start the program, it asks for a cluttered directory to organize. Once you click it, it'll immediately begin organizing the directory. It will create an organized folder and within it, it'll have a folder for every file type [Text Files, Video Files, Image Files, etc].

## How I built it
This software was programmed with Python.

## Challenges I ran into
Not many other than having to manually make long lists of file extension types. 

## Accomplishments that I'm proud of
This is a working software that can be used on any platform. I'm proud that this can be used right away by people.

## What I learned
Learned a bit more about the shutil library.

## What's next for Folder Organizer
Maybe I'll make a web app next time so they won't have to download the software on their own computer.


- Give a directory to organize
- list all the files in the directory and organize them in the follwing format

If a folder is empty, then that folder will not be created

How to program:

	- Create a list of all file types that will be in each folder
	- Ask the user for a directory
	- List all the files in the directory
	- Group elements of the list into folder lists by file extension
	- Make sure to delete elements of a list once moved
	- Make a folder for every folder list
	- If a folder list is empty, don't create that folder
	- Using the shutil.move method, move all files in each folder to their respective folders
	- Print completed afterwards
	