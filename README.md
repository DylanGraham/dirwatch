# dirwatch.py

Watch a file system directory for IN_CLOSE_WRITE changes, and execute a script, with the file name as an argument.

## Motivation

The incrond project seems to have been abandoned and systemd.path doesn't provide a full replacement.
dirwatch was created to solve one use case: When a file is written in the watched directory, execute a script with that file name as an argument.

## Installation

Requires PyInotify: https://github.com/dsoprea/PyInotify/releases
    pip3 install inotify

## Usage

    python3 dirwatch.py <watch directory> <script>

### Example

    python3 dirwatch.py /tmp /home/user/myscript.sh

## Platforms

Tested on Python 3.5.1 and 2.7.11

## License

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
