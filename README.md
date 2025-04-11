# Qipy, simple qi wrapper tool.

## What's qipy ?

Qipy is a simple wrapper for qi package manager, written in python. Its main function is to show informations about package, 
like name, version, installed files, etc. I made it to check installed packages on Dragora.

## Features.

Qipy has some simple features, like :
- List all installed recipes.
- Search recipe.
- Show package information.
- Create a recipe template for particular build method (`meson` build, `make` build and `cmake` build).
- Check which package(s) contain particular file, it's like `apt-file find` and `pacman -F`.
- Check contents of package, it's like `apt-file list` and `pacman -Fl`.
- Download source code of package, it's still slow and will be improved later.
- Copy local / installed recipe.
- Count & view recipe.
- Search local package(s).

## Usage.

It's easy to use qipy. We just need to run these commands :


- List all installed recipes.

	```
	$ qipy list recipe
	$ qipy l recipe
	```

- Search package.

	```
	$ qipy search <pattern>
	$ qipy s <pattern>
	```

- Show package information.

	```
	$ qipy info <name of package>
	$ qipy i <name of package>
	```

- Create recipe / build template.

	```
	$ qipy template make
	$ qipy t make
	```

- Find which package own a file.

	```
	$ qipy file <name of file>
	$ qipy f <name of file>
	```

- List contents of a package.

	```
	$ qipy content <name of package>
	$ qipy c <name of package>
	```

- Download source code of package.

	```
	$ qipy source <name of package>
	$ qipy sc <name of package>
	```

- Copy local / installed recipe.

	```
	$ qipy recipe <name of package>
	$ qipy r <name of package>
	```

- Count & view recipe.

	```
	$ qipy count recipe 
	$ qipy cn  recipe
	$ qipy view <name of package>
	$ qipy v <name of package>
	```

- Search local package(s).

	```
	$ qipy local <name of package>
	$ qipy lc <name of package>
	```
