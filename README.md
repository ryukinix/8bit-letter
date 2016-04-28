# 8bit-letter

This repository contains a prototype of a 8-bit letter using **python** + **pygame** _(SDL interface)_.

![8bit-letter](8bit-letter-example.gif)

## Installation

You will **need** of:

* [Python](https://www.python.org/)
* [Pygame](http://www.pygame.org/download.shtml)

To install pygame in linux debian-based you have two options:

* Using **apt**:
  ```bash
  sudo apt-get install python-pygame
  ```

* Using **pip**:
  ```bash
  sudo pip install pygame
  ```

And now only execute the `gchr.py`!

## Usage

 Key  |      Action       |
------| ----------------  |
 ESC  |       Exit        |
 F10  |    Input Mode     |

## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## Credits

  * Me (Manoel Vilela)

## License

MIT

## Roadmap

- [X] basic alfanum characters in pieces.py 
- [X] Input mode
  - [-] A smart method to write the buffer
  - [X] A way to use backspace
