# Changelog

## master

New changelog.

- Add recipe(s) counter and view recipe function. 
- change templates directory to /etc/qipy/recipe-templates.
- make sure existing recipe isn't overwritten when copying recipe template. 

## v0.1

This version is the first release. Still have simple functions and features, like :

- List all installed recipes.
- Search recipe.
- Show package information.
- Create a recipe template for particular build method (`meson` build, `make` build and `cmake` build).
- Check which package(s) contain particular file, it's like `apt-file find` and `pacman -F`.
- Check contents of package, it's like `apt-file list` and `pacman -Fl`.
- Download source code of package, it's still slow and will be improved later.
- Copy local / installed recipe.

We still have no clue about how python's argparse work but we will dig it later.


### Todo

- Fix argparse format.
- Port to other language.
- (Later addition).
