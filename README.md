# Python SSH-chat
This is supposed to be an "upgrade" to [VitaliPom's chat program](https://github.com/VitaliPom/chatapp) that uses curses, Perl, and Python (or PHP). This uses Python and curses.

VitaliPom relies on HTTP requests to write to file, but alternatively Python easy to use file I/O. The source code shows the address connected to, so you can easily take advantage of PHP relying on a POST request that has the Content-type set to application/x-www-form-urlencoded. With this, the only way to take advantage of it is to connect through SSH and use the program to write to file.

The whole purpose of this is to keep the same curses-over-SSH chat feel, without the web 'exploit'.

# Using the program
If you're actually interested in this program, you shouldn't need explanation.

But if I must...

This program uses Python 2, so install it if you don't. Then open your command line, navigate to where the files for this repository is download to, and then run `python main.py`. Its that easy.
