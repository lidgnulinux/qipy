#include <stdio.h>
#include <string.h>
#include <stdarg.h>
#include <getopt.h>
#include <stdlib.h>

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

int main(int argc, char *argv[]) 
{
	char *startup_cmd = NULL;
	int c;

	while ((c = getopt(argc, argv, "s:pv")) != -1) {
		if (c == 'p')
			list_packages();
		else if (c == 'v')
			die("simple qi info tool.");
		else
			goto usage;
	}
	if (optind < argc)
		goto usage;

	return EXIT_SUCCESS;

usage:
	die("Usage: %s [-pv]", argv[0]);
}
