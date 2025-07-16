#include <stdio.h>
#include <string.h>
#include <stdarg.h>
#include <stdlib.h>
#include <unistd.h>

#define MAX_LINE 1024

void
die(const char *fmt, ...) {
	va_list ap;

	va_start(ap, fmt);
	vfprintf(stderr, fmt, ap);
	va_end(ap);

	if (fmt[0] && fmt[strlen(fmt)-1] == ':') {
		fputc(' ', stderr);
		perror(NULL);
	} else {
		fputc('\n', stderr);
	}

	exit(1);
}

static int list_packages()
{
    FILE *file = fopen("/var/qi/installed_packages.list", "r");
    if (!file) {
        perror("Failed to open file");
        return 1;
    }

    char line[256];
    while (fgets(line, sizeof(line), file)) {
        // Remove newline character at end, if any
        line[strcspn(line, "\n")] = 0;

        char package[64], version[64];
        // sscanf parses up to the first two underscores
        if (sscanf(line, "%63[^_]_%63[^_]", package, version) == 2) {
            printf("%s %s\n", package, version);
        }
    }

    fclose(file);
    return 0;
}

void search_packages(const char *pattern)
{
    FILE *file = fopen("/var/qi/installed_packages.list", "r");
    if (!file) {
        perror("Failed to open file");
        return;
    }

    char line[MAX_LINE];

    while (fgets(line, sizeof(line), file)) {
        char package[64], version[64];
        if (sscanf(line, "%63[^_]_%63[^_]", package, version) == 2) {
        	if (strstr(line, pattern)) {
            		printf("%s %s\n", package, version);
		}
        }
    }

    fclose(file);
    return;
}

int main(int argc, char *argv[]) 
{
	// const char *pattern;
	int c;

	while ((c = getopt(argc, argv, "s:hpsv")) != -1) {
		switch (c) {
		case 'p':
			list_packages();
			break;
		case 'v':
			die("simple qi info tool.");
			break;
		case 's':
			search_packages(argv[2]);
			break;
		case 'h':
			goto usage;
			break;
		default:
			goto usage;
		}
	}
	if (optind < argc)
		goto usage;

	return 0;

usage:
	die("Usage: %s [-hpsv]", argv[0]);
}
