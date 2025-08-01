# Changelog

## master

New changelog.
- Make --help more clear. 
- Add bash completion.

## v0.4

- Deprecating /var/qi/installed_packages.list file in count recipe function.
- Add show recent installed packages function, update README.
- Update doc and add html for doc.
- Add qipy usage/help, accesible using `qipy h` or `qipy help`.
- Add simple manpage.
- Add default help (-h / --help).
- Remove pkg_file function.

## v0.3

- Make second argument as optional.
- Set release=0 for all recipes template.
- Enable show info and view recipe for unique package with name@category type only.
- /var/qi/installed_packages.list file is obsolete, but still useful.
- Add initial develepmont for qic.

## v0.2

- Add recipe(s) counter and view recipe function. 
- change templates directory to /etc/qipy/recipe-templates.
- make sure existing recipe isn't overwritten when copying recipe template. 
- Add function to search local package(s).

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
