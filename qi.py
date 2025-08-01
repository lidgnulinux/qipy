#!/usr/bin/python3

import glob, os
import argparse
import shutil
import subprocess
import re
# from urllib.request import urlretrieve 
# import requests

parser=argparse.ArgumentParser(description="simple qi wrapper.", add_help=False)
parser.add_argument("opt1", nargs='?')
parser.add_argument("opt2", nargs='?')
parser.add_argument('-h', '--help', action='store_true', help='Show this help message and exit.')
args=parser.parse_args()

def packages():
  os.chdir("/var/lib/qi")
  for file in sorted(glob.glob("*_*." + "recipe")):
      package = file.rstrip('\n').split('_')[:2]
      print(*package, sep=" ")

# to get the "installed_packages.list" file, generate the list using this command :
# find /var/lib/qi/ -name "*_*.recipe" -printf '%f\n' | sort | sed 's/.recipe$//' > /var/qi/installed_packages.list 

def search(keyword):
#  with open("/var/qi/installed_packages.list", 'r') as f:
#    for line in f.readlines():
#      if keyword in line:
#          package=line.split('_')[:2]
#          print(*package, sep=" ")
  for file in sorted(glob.glob("/var/lib/qi/"+"*"+keyword+"*.recipe")):
      package = file.rstrip('\n').split("/var/lib/qi/")[1].split('_')[:2]
      print(*package, sep=" ")

def info(keyword):
  package = glob.glob("/var/lib/qi/"+keyword+"_"+"*.txt")
  pkg = '/'.join(package)
  if os.path.isfile(pkg):
    with open(pkg, 'r') as f:
      for line in f.readlines():
        if not re.match("QI", line):
          print(line, end="")
  else:
      package = glob.glob("/var/lib/qi/"+keyword+"@"+"*.txt") 
      pkg = '/'.join(package)
      with open(pkg, 'r') as f:
        for line in f.readlines():
          if not re.match("QI", line):
            print(line, end="")

def recipe(keyword):
  recipe = glob.glob("/var/lib/qi/"+keyword+"_"+"*.recipe")
  rcp = '/'.join(recipe)
  if os.path.isfile(rcp):
    with open(rcp, 'r') as f:
      subprocess.run(['less'], stdin=f)
  else:
    recipe = glob.glob("/var/lib/qi/"+keyword+"@"+"*.recipe")
    rcp = '/'.join(recipe)
    with open(rcp, 'r') as f:
      subprocess.run(['less'], stdin=f)

def get_source(keyword):
  package = glob.glob("/var/lib/qi/"+keyword+"_"+"*.txt")
  pkg = '/'.join(package)
  with open(pkg, 'r') as f:
    for line in f.readlines():
      if 'fetch' in line:
        print("Download the" + " " + keyword + " " + "source code")
        url=line.split('"')[1]
        file=url.split('/')[-1]
        subprocess.call(["wget", "-c", url])

def pkg_contents(keyword):
  package = glob.glob("/usr/pkg/"+keyword+"_*")
  pkg = '/'.join(package)
  for root, dirs, files in os.walk(pkg):
    for file in files:
      list_contents=os.path.join(root, file).split("/usr/pkg/")[1]
      package_name_vers=pkg.split("/usr/pkg/")[1]
      print(package_name_vers, ":", "/"+list_contents.split(package_name_vers + "/")[1])
  
def get_template(keyword):
  file = 'recipe'
  if keyword=="meson" and not os.path.isfile(file):
    shutil.copy("/etc/qipy/recipe-templates/meson_build.recipe", "recipe")
  elif keyword=="make" and not os.path.isfile(file):
    shutil.copy("/etc/qipy/recipe-templates/make_build.recipe", "recipe")
  elif keyword=="cmake" and not os.path.isfile(file):
    shutil.copy("/etc/qipy/recipe-templates/cmake_build.recipe", "recipe")
  else:
      print ("specify template you want / make sure there's no existing recipe !") 

def get_recipe(keyword):
  rcp = glob.glob("/usr/pkg/"+keyword+"_"+"*"+"/var/lib/qi/"+"*.recipe")
  rcp2 = '/'.join(rcp)
  file = 'recipe'
  if os.path.isfile(file):
    print("There is a recipe file, not copying to prevent overwriting. Please rename or remove the recipe file first !")
  else:
    shutil.copy(rcp2, "recipe")

def count_recipe():
#  with open("/var/qi/installed_packages.list", 'r') as f: 
#    contents = f.read()
#    line_count = contents.count('\n')
#    print("Total package(s): ", line_count, "package(s).")
  count = 0
  try:
    for item in os.listdir("/usr/pkg"):
      item_path = os.path.join("/usr/pkg", item)
      if os.path.isdir(item_path):
        count += 1
  except FileNotFoundError:
    print("FNFE")
  except PermissionError:
    print("PE")
  print(count, "packages installed")

def local_packages(keyword):
  arch=sorted(glob.glob("/var/cache/qi/packages/amd64/"+"*"+keyword+"*_*.tlz"))
  noarch=sorted(glob.glob("/var/cache/qi/packages/noarch/"+"*"+keyword+"*_*.tlz"))
  for file in (arch,noarch):
      for files in file:
          package = files.rstrip('\n')
          print(*package, sep="")

def recent_packages(k):
  os.chdir("/var/lib/qi")
  recent_list = sorted(glob.glob("*_*." + "recipe"), key=lambda x: os.path.getmtime(x), reverse=True)
  k = int(k)
  for file in recent_list[:k]:
      package = file.rstrip('\n').split('_')[:2]
      print(*package, sep=" ")

BO = "\033[1m"
RE = "\033[0m"

qipy_usage = f"""
{BO}Qipy{RE} - simple info tool for qi package manager

{BO}Qipy usage{RE} :

    {BO}content{RE}, {BO}c <package>{RE}	List contents of a package.
    {BO}count{RE}, {BO}cn{RE}			Count installed package(s).
    {BO}help{RE}, {BO}h{RE}			Show help / qipy usage.
    {BO}info{RE}, {BO}i <package>{RE}		Show package information.
    {BO}list{RE}, {BO}l{RE}			List all installed packages.
    {BO}local{RE}, {BO}lc <package>{RE}		Search local package(s).
    {BO}recipe{RE}, {BO}r <package>{RE}		Copy local / installed recipe.
    {BO}recent{RE}, {BO}rc <number{RE}		Show recent installed packages.
    {BO}search{RE}, {BO}s <pattern>{RE}		Search package.
    {BO}source{RE}, {BO}sc <package>{RE}	Download  source code of package.
    {BO}template{RE}, {BO}t <template>{RE}	Create recipe / build template.
    {BO}view{RE}, {BO}v <package>{RE}		View package recipe.

    {BO}PS: {RE} the available template are {BO}cmake{RE}, {BO}make{RE} and {BO}meson{RE}.

"""

if args.opt1 in ("list", "l"):
   packages()
elif args.opt1 in ("recent", "rc"):
   recent_packages(args.opt2)
elif args.opt1 in ("search", "s"):
   search(args.opt2)
elif args.opt1 in ("info", "i"):
   info(args.opt2)
elif args.opt1 in ("source", "sc"):
   get_source(args.opt2)
elif args.opt1 in ("template", "t"):
   get_template(args.opt2)
elif args.opt1 in ("content", "c"):
   pkg_contents(args.opt2)
elif args.opt1 in ("recipe", "r"):
   get_recipe(args.opt2)
elif args.opt1 in ("count", "cn"):
   count_recipe()
elif args.opt1 in ("view", "v"):
   recipe(args.opt2)
elif args.opt1 in ("local", "lc"):
   local_packages(args.opt2)
elif args.opt1 in ("help", "h"):
   print(qipy_usage)
elif args.help:
   print(qipy_usage)
else:
    print(qipy_usage)
