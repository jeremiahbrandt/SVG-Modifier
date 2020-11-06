# SVG Modifer
Programmatically modify SVG files from [iconmonstr](https://iconmonstr.com)

1. Download files from git.

        git clone https://github.com/jeremiahbrandt/SVG-Modifier.git

1. Download SVG files from iconmonstr.com into [original-files](original-files/)

1. Modify [Config](config.ini) if necessary.

        [Rectangle_Fills]
        iconmonstr-credit-card-6.svg = yellow
        iconmonstr-email-2.svg = yellow
        iconmonstr-generation-8.svg = green
        iconmonstr-location-1.svg = green
        iconmonstr-lock-3.svg = green
        iconmonstr-marketing-5.svg = yellow
        iconmonstr-monitoring-6.svg = green
        iconmonstr-pencil-9.svg = red
        iconmonstr-police-1.svg = red
        iconmonstr-warning-5.svg = red

1. Run the script with the default filter or create your own.

        py main.py

1. New files will be created in [new-files](new-files).
