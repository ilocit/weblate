#
# Copyright © 2012–2022 Michal Čihař <michal@cihar.com>
#
# This file is part of Weblate <https://weblate.org/>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

# We ignore some words which are usually untranslated
IGNORE_WORDS = {
    "abc",
    "accelerator",
    "account",
    "action",
    "actions",
    "active",
    "add",
    "addons",
    "address",
    "admin",
    "administrator",
    "administration",
    "aes",
    "africa",
    "agenda",
    "agent",
    "alarm",
    "album",
    "alias",
    "aliases",
    "aliasing",
    "alt",
    "altitude",
    "amazon",
    "amex",
    "android",
    "antialias",
    "antialiasing",
    "apertium",
    "api",
    "applet",
    "appliance",
    "appliances",
    "apt",
    "aptitude",
    "area",
    "array",
    "artica",
    "artist",
    "artwork",
    "async",
    "attribute",
    "attribution",
    "atom",
    "audio",
    "auth",
    "author",
    "auto",
    "autostart",
    "authentication",
    "avatar",
    "azure",
    "backend",
    "backspace",
    "backup",
    "badge",
    "balance",
    "baltic",
    "bank",
    "banner",
    "bar",
    "baseball",
    "battery",
    "bazaar",
    "begin",
    "beta",
    "bios",
    "bit",
    "bitbucket",
    "bitcoin",
    "bitcoins",
    "bitmap",
    "bitmaps",
    "bitnami",
    "bitrate",
    "block",
    "blog",
    "bluetooth",
    "bool",
    "boolean",
    "boot",
    "bootloader",
    "box",
    "branch",
    "broadcast",
    "browser",
    "bsd",
    "buffer",
    "byte",
    "bytes",
    "bzip",
    "cable",
    "cache",
    "captcha",
    "caps",
    "cardinality",
    "cdrom",
    "celery",
    "core",
    "charset",
    "charsets",
    "chat",
    "china",
    "classic",
    "click",
    "client",
    "clipboard",
    "cloud",
    "club",
    "cmd",
    "cockpit",
    "code",
    "codec",
    "collation",
    "color",
    "command",
    "commit",
    "component",
    "components",
    "compression",
    "conductor",
    "configuration",
    "console",
    "contact",
    "contacts",
    "context",
    "control",
    "cookie",
    "cookies",
    "copyright",
    "creation",
    "criteria",
    "crypt",
    "csd",
    "csv",
    "ctrl",
    "cvs",
    "cyrillic",
    "dashboard",
    "data",
    "database",
    "databases",
    "date",
    "datum",
    "dbm",
    "debconf",
    "debian",
    "debug",
    "deepl",
    "default",
    "definition",
    "del",
    "delete",
    "demo",
    "description",
    "design",
    "designer",
    "desktop",
    "destination",
    "detail",
    "details",
    "developer",
    "devscripts",
    "dialog",
    "diaspora",
    "diners",
    "ding",
    "diplomat",
    "direction",
    "directory",
    "disc",
    "distance",
    "distribution",
    "distro",
    "dns",
    "doc",
    "docs",
    "doctor",
    "document",
    "documentation",
    "dollar",
    "download",
    "downloads",
    "doxygen",
    "dpkg",
    "dpi",
    "drizzle",
    "droid",
    "dropbox",
    "dtd",
    "dummy",
    "dump",
    "editor",
    "eib",
    "ellipsis",
    "email",
    "end",
    "engine",
    "engines",
    "enter",
    "enterprise",
    "enum",
    "error",
    "esc",
    "escape",
    "eta",
    "ethereum",
    "ethernet",
    "exchange",
    "excel",
    "expert",
    "explore",
    "export",
    "express",
    "expression",
    "extension",
    "extra",
    "extras",
    "event",
    "events",
    "facebook",
    "false",
    "fame",
    "fanfare",
    "farm",
    "fauna",
    "fax",
    "fediverse",
    "fedora",
    "feeds",
    "feet",
    "file",
    "files",
    "filter",
    "filters",
    "finance",
    "finalisation",
    "fingerprint",
    "firefox",
    "firewall",
    "firmware",
    "fjord",
    "flash",
    "flattr",
    "float",
    "flora",
    "font",
    "form",
    "format",
    "forum",
    "freemind",
    "freeplane",
    "frequency",
    "full",
    "fulltext",
    "function",
    "gamma",
    "gammu",
    "gas",
    "general",
    "genre",
    "gentoo",
    "geo",
    "geocache",
    "geocaching",
    "geometry",
    "get",
    "gettext",
    "global",
    "glosbe",
    "gnu",
    "gmail",
    "golf",
    "google",
    "ghz",
    "gib",
    "git",
    "gitea",
    "github",
    "gitlab",
    "gpl",
    "gps",
    "gpx",
    "graphic",
    "graphics",
    "grant",
    "gratis",
    "greeter",
    "gtk",
    "gvim",
    "gzip",
    "hack",
    "hacks",
    "hall",
    "handle",
    "handler",
    "hardware",
    "hash",
    "hashed",
    "hdmi",
    "headset",
    "help",
    "hex",
    "histogram",
    "hmpf",
    "home",
    "homebrew",
    "homepage",
    "honeypot",
    "hong",
    "hook",
    "horizontal",
    "horror",
    "host",
    "hosted",
    "hosting",
    "hostname",
    "hostel",
    "hotel",
    "hpa",
    "html",
    "http",
    "https",
    "hut",
    "hybrid",
    "hyperlink",
    "iban",
    "icmp",
    "icon",
    "icons",
    "icu",
    "ids",
    "idea",
    "ieee",
    "ignore",
    "irc",
    "irda",
    "illustration",
    "image",
    "imap",
    "imei",
    "imsi",
    "import",
    "inconsistent",
    "index",
    "india",
    "indigo",
    "individual",
    "info",
    "information",
    "infrastructure",
    "inline",
    "inno",
    "innodb",
    "innosetup",
    "input",
    "ins",
    "insert",
    "insights",
    "instagram",
    "install",
    "installation",
    "int",
    "integer",
    "interface",
    "interlingua",
    "internet",
    "international",
    "intl",
    "intro",
    "introduction",
    "ion",
    "ios",
    "ipsum",
    "iptables",
    "ipv",
    "irix",
    "isbn",
    "isdn",
    "ismn",
    "iso",
    "issn",
    "isrc",
    "item",
    "items",
    "jabber",
    "jami",
    "java",
    "javascript",
    "jdbc",
    "join",
    "joins",
    "joomla",
    "jpeg",
    "jpg",
    "kappa",
    "karaoke",
    "kbps",
    "kernel",
    "keycloak",
    "kgz",
    "kib",
    "kill",
    "knoppix",
    "kong",
    "korfbal",
    "label",
    "labels",
    "land",
    "latex",
    "latin",
    "latitude",
    "layout",
    "ldif",
    "leap",
    "legal",
    "level",
    "libgammu",
    "liberapay",
    "libre",
    "lime",
    "linestring",
    "link",
    "links",
    "linux",
    "list",
    "litecoin",
    "lithium",
    "lock",
    "local",
    "locales",
    "log",
    "logcheck",
    "login",
    "logo",
    "logos",
    "longitude",
    "lord",
    "lorem",
    "ltr",
    "lua",
    "lzma",
    "lzo",
    "mac",
    "macos",
    "magazine",
    "magazines",
    "magenta",
    "mah",
    "manager",
    "mandrake",
    "mandriva",
    "manual",
    "mail",
    "mailbird",
    "mailbox",
    "mailboxes",
    "maildir",
    "mailing",
    "majordomo",
    "mako",
    "mapillary",
    "markdown",
    "master",
    "material",
    "matrix",
    "max",
    "maximum",
    "media",
    "mediawiki",
    "medium",
    "menu",
    "merchandise",
    "mercurial",
    "merge",
    "mesh",
    "message",
    "messageformat",
    "messages",
    "meta",
    "metadata",
    "metal",
    "metre",
    "metres",
    "mhz",
    "mib",
    "micropayment",
    "micropayments",
    "microsoft",
    "migration",
    "mile",
    "min",
    "minimum",
    "mint",
    "minus",
    "minute",
    "minutes",
    "mm²",
    "mode",
    "model",
    "module",
    "modules",
    "monero",
    "monitor",
    "mono",
    "monument",
    "motel",
    "motif",
    "mouse",
    "mozilla",
    "mph",
    "mysql",
    "multiplayer",
    "musical",
    "musicbottle",
    "name",
    "namecoin",
    "namecoins",
    "navigation",
    "navy",
    "net",
    "netfilter",
    "network",
    "neutral",
    "next",
    "nimh",
    "node",
    "none",
    "normal",
    "note",
    "notes",
    "notify",
    "notification",
    "notifications",
    "null",
    "num",
    "number",
    "numeric",
    "oauth",
    "obex",
    "office",
    "offline",
    "offset",
    "ogg",
    "online",
    "ons",
    "opac",
    "open",
    "opendocument",
    "openmaps",
    "openpgp",
    "openstreet",
    "opensuse",
    "openvpn",
    "opera",
    "operator",
    "option",
    "options",
    "orange",
    "orientation",
    "original",
    "osm",
    "osmand",
    "osx",
    "output",
    "overhead",
    "package",
    "page",
    "pager",
    "pages",
    "panel",
    "parameter",
    "parameters",
    "park",
    "parking",
    "partition",
    "partitions",
    "parser",
    "party",
    "password",
    "patreon",
    "pause",
    "paypal",
    "pdf",
    "pdu",
    "per",
    "percent",
    "perfume",
    "personal",
    "performance",
    "php",
    "phpmyadmin",
    "pib",
    "picasa",
    "pin",
    "ping",
    "pirate",
    "pirates",
    "pixel",
    "pixels",
    "placement",
    "plan",
    "platform",
    "playlist",
    "plugin",
    "plugins",
    "plural",
    "plurals",
    "plus",
    "png",
    "podcast",
    "podcasts",
    "point",
    "points",
    "polygon",
    "polymer",
    "pool",
    "port",
    "portable",
    "portrait",
    "position",
    "post",
    "postgresql",
    "posts",
    "postscript",
    "ppp",
    "pppoe",
    "pre",
    "prefix",
    "premium",
    "prince",
    "privacy",
    "private",
    "procedure",
    "procedures",
    "process",
    "processing",
    "profiling",
    "program",
    "progress",
    "project",
    "promotion",
    "property",
    "properties",
    "protocol",
    "provider",
    "proxy",
    "public",
    "pull",
    "push",
    "python",
    "query",
    "question",
    "questions",
    "radar",
    "radio",
    "radius",
    "rate",
    "react",
    "reality",
    "realm",
    "rebase",
    "recaptcha",
    "recent",
    "reddit",
    "redhat",
    "reg",
    "regexp",
    "region",
    "relation",
    "relations",
    "release",
    "render",
    "replication",
    "repository",
    "report",
    "reports",
    "reset",
    "resource",
    "responsive",
    "restart",
    "restaurant",
    "restaurants",
    "return",
    "rich",
    "richtext",
    "rijndael",
    "roadmap",
    "robot",
    "role",
    "roles",
    "root",
    "route",
    "routine",
    "routines",
    "ruby",
    "rss",
    "rst",
    "rtl",
    "salt",
    "sauna",
    "saver",
    "scalable",
    "scenario",
    "score",
    "screen",
    "screenshot",
    "screensaver",
    "script",
    "scripts",
    "scripting",
    "scroll",
    "sdk",
    "sector",
    "seed",
    "selinux",
    "send",
    "sergeant",
    "serie",
    "series",
    "server",
    "servers",
    "service",
    "set",
    "setup",
    "shell",
    "shift",
    "signature",
    "sim",
    "singular",
    "sip",
    "site",
    "skype",
    "slack",
    "slash",
    "slide",
    "slideshow",
    "slot",
    "slots",
    "slug",
    "sms",
    "smsc",
    "smsd",
    "smtp",
    "snapshot",
    "snapshots",
    "snmp",
    "socket",
    "social",
    "software",
    "solaris",
    "source",
    "spam",
    "spatial",
    "spline",
    "spoiler",
    "sponsor",
    "sponsors",
    "sport",
    "sprint",
    "sql",
    "sqlite",
    "squid",
    "ssh",
    "ssl",
    "sso",
    "stack",
    "standard",
    "start",
    "starttls",
    "stat",
    "statement",
    "stats",
    "status",
    "stereo",
    "stop",
    "string",
    "strings",
    "structure",
    "studio",
    "stun",
    "style",
    "submit",
    "subquery",
    "substring",
    "suggestion",
    "suggestions",
    "sum",
    "sunos",
    "supermarket",
    "support",
    "surfing",
    "suse",
    "svg",
    "symbol",
    "synaptic",
    "syndication",
    "syntax",
    "system",
    "swap",
    "tab",
    "table",
    "tables",
    "tabs",
    "tada",
    "tag",
    "tags",
    "taiwan",
    "taxi",
    "taxon",
    "tbx",
    "tcp",
    "team",
    "teams",
    "technologies",
    "technology",
    "telegram",
    "telnet",
    "template",
    "tent",
    "term",
    "termbase",
    "terminal",
    "test",
    "texy",
    "text",
    "theme",
    "theora",
    "thread",
    "thriller",
    "threads",
    "thunderbird",
    "tls",
    "tib",
    "timer",
    "tip",
    "todo",
    "todos",
    "token",
    "top",
    "tor",
    "total",
    "tour",
    "trailer",
    "transfer",
    "transformation",
    "transformations",
    "transistor",
    "transport",
    "tray",
    "trigger",
    "triggers",
    "true",
    "tutorial",
    "type",
    "twiki",
    "twitter",
    "ubuntu",
    "udp",
    "uefi",
    "ukolovnik",
    "unicode",
    "unique",
    "unit",
    "universal",
    "unix",
    "update",
    "upload",
    "upnp",
    "url",
    "user",
    "utf",
    "variable",
    "variables",
    "vcalendar",
    "vcard",
    "vector",
    "vendor",
    "version",
    "versions",
    "vertical",
    "video",
    "view",
    "views",
    "vim",
    "vip",
    "virus",
    "visa",
    "vkontakte",
    "vorbis",
    "volume",
    "vote",
    "votes",
    "vue",
    "wammu",
    "web",
    "webdav",
    "webextension",
    "webgl",
    "weblate",
    "webmail",
    "website",
    "widget",
    "widgets",
    "wifi",
    "wiki",
    "wikipedia",
    "wildcard",
    "windowed",
    "windows",
    "word",
    "www",
    "xen",
    "xhtml",
    "xkeys",
    "xliff",
    "xml",
    "yahoo",
    "yaml",
    "yard",
    "zcash",
    "zen",
    "zero",
    "zeta",
    "zip",
    "zombie",
    "zone",
    "zoo",
    "zoom",
    "zstd",
    # Currencies
    "btc",
    "eur",
    "usd",
    # Months are same in some languages
    "january",
    "february",
    "march",
    "april",
    "may",
    "june",
    "july",
    "august",
    "september",
    "october",
    "november",
    "december",
    "jan",
    "feb",
    "mar",
    "apr",
    "jun",
    "jul",
    "aug",
    "sep",
    "oct",
    "nov",
    "dec",
    # Week names shotrcuts
    "mon",
    "tue",
    "wed",
    "thu",
    "fri",
    "sat",
    "sun",
    # Roman numbers
    "iii",
    # Architectures
    "alpha",
    "amd",
    "arm",
    "aarch",
    "hppa",
    "powerpc",
    "sparc",
    # whole alphabet
    "abcdefghijklmnopqrstuvwxyz",
}

"""
Set of non word characters, generated using ./scripts/generate-non-word-chars
"""
NON_WORD_CHARS = (
    "\x00",
    "\x01",
    "\x02",
    "\x03",
    "\x04",
    "\x05",
    "\x06",
    "\x07",
    "\x08",
    "\t",
    "\n",
    "\x0b",
    "\x0c",
    "\r",
    "\x0e",
    "\x0f",
    "\x10",
    "\x11",
    "\x12",
    "\x13",
    "\x14",
    "\x15",
    "\x16",
    "\x17",
    "\x18",
    "\x19",
    "\x1a",
    "\x1b",
    "\x1c",
    "\x1d",
    "\x1e",
    "\x1f",
    " ",
    "!",
    '"',
    "#",
    "%",
    "&",
    "'",
    "(",
    "*",
    ",",
    ".",
    "/",
    ":",
    ";",
    "?",
    "@",
    "[",
    "\\",
    "^",
    "`",
    "{",
    "\x7f",
    "\x80",
    "\x81",
    "\x82",
    "\x83",
    "\x84",
    "\x85",
    "\x86",
    "\x87",
    "\x88",
    "\x89",
    "\x8a",
    "\x8b",
    "\x8c",
    "\x8d",
    "\x8e",
    "\x8f",
    "\x90",
    "\x91",
    "\x92",
    "\x93",
    "\x94",
    "\x95",
    "\x96",
    "\x97",
    "\x98",
    "\x99",
    "\x9a",
    "\x9b",
    "\x9c",
    "\x9d",
    "\x9e",
    "\x9f",
    "\xa0",
    "¡",
    "§",
    "¨",
    "¯",
    "´",
    "¶",
    "¸",
    "¿",
    "˂",
    "˃",
    "˄",
    "˅",
    "˒",
    "˓",
    "˔",
    "˕",
    "˖",
    "˗",
    "˘",
    "˙",
    "˚",
    "˛",
    "˜",
    "˝",
    "˞",
    "˟",
    "˥",
    "˦",
    "˧",
    "˨",
    "˩",
    "˪",
    "˫",
    "˭",
    "˯",
    "˰",
    "˱",
    "˲",
    "˳",
    "˴",
    "˵",
    "˶",
    "˷",
    "˸",
    "˹",
    "˺",
    "˻",
    "˼",
    "˽",
    "˾",
    "˿",
    "͵",
    ";",
    "΄",
    "΅",
    "·",
    "՚",
    "՛",
    "՜",
    "՝",
    "՞",
    "՟",
    "։",
    "׀",
    "׃",
    "׆",
    "׳",
    "״",
    "؉",
    "؊",
    "،",
    "؍",
    "؛",
    "؞",
    "؟",
    "٪",
    "٫",
    "٬",
    "٭",
    "۔",
    "܀",
    "܁",
    "܂",
    "܃",
    "܄",
    "܅",
    "܆",
    "܇",
    "܈",
    "܉",
    "܊",
    "܋",
    "܌",
    "܍",
    "߷",
    "߸",
    "߹",
    "࠰",
    "࠱",
    "࠲",
    "࠳",
    "࠴",
    "࠵",
    "࠶",
    "࠷",
    "࠸",
    "࠹",
    "࠺",
    "࠻",
    "࠼",
    "࠽",
    "࠾",
    "࡞",
    "।",
    "॥",
    "॰",
    "৽",
    "੶",
    "૰",
    "౷",
    "಄",
    "෴",
    "๏",
    "๚",
    "๛",
    "༄",
    "༅",
    "༆",
    "༇",
    "༈",
    "༉",
    "༊",
    "་",
    "༌",
    "།",
    "༎",
    "༏",
    "༐",
    "༑",
    "༒",
    "༔",
    "༺",
    "༼",
    "྅",
    "࿐",
    "࿑",
    "࿒",
    "࿓",
    "࿔",
    "࿙",
    "࿚",
    "၊",
    "။",
    "၌",
    "၍",
    "၎",
    "၏",
    "჻",
    "፠",
    "፡",
    "።",
    "፣",
    "፤",
    "፥",
    "፦",
    "፧",
    "፨",
    "᙮",
    "\u1680",
    "᚛",
    "᛫",
    "᛬",
    "᛭",
    "᜵",
    "᜶",
    "។",
    "៕",
    "៖",
    "៘",
    "៙",
    "៚",
    "᠀",
    "᠁",
    "᠂",
    "᠃",
    "᠄",
    "᠅",
    "᠇",
    "᠈",
    "᠉",
    "᠊",
    "᥄",
    "᥅",
    "᨞",
    "᨟",
    "᪠",
    "᪡",
    "᪢",
    "᪣",
    "᪤",
    "᪥",
    "᪦",
    "᪨",
    "᪩",
    "᪪",
    "᪫",
    "᪬",
    "᪭",
    "᭚",
    "᭛",
    "᭜",
    "᭝",
    "᭞",
    "᭟",
    "᭠",
    "᯼",
    "᯽",
    "᯾",
    "᯿",
    "᰻",
    "᰼",
    "᰽",
    "᰾",
    "᰿",
    "᱾",
    "᱿",
    "᳀",
    "᳁",
    "᳂",
    "᳃",
    "᳄",
    "᳅",
    "᳆",
    "᳇",
    "᳓",
    "᾽",
    "᾿",
    "῀",
    "῁",
    "῍",
    "῎",
    "῏",
    "῝",
    "῞",
    "῟",
    "῭",
    "΅",
    "`",
    "´",
    "῾",
    "\u2000",
    "\u2001",
    "\u2002",
    "\u2003",
    "\u2004",
    "\u2005",
    "\u2006",
    "\u2007",
    "\u2008",
    "\u2009",
    "\u200a",
    "‖",
    "‗",
    "‚",
    "„",
    "†",
    "‡",
    "‣",
    "․",
    "‥",
    "…",
    "‧",
    "\u202f",
    "‰",
    "‱",
    "′",
    "″",
    "‴",
    "‵",
    "‶",
    "‷",
    "‸",
    "※",
    "‼",
    "‽",
    "‾",
    "⁁",
    "⁂",
    "⁃",
    "⁅",
    "⁇",
    "⁈",
    "⁉",
    "⁊",
    "⁋",
    "⁌",
    "⁍",
    "⁎",
    "⁏",
    "⁐",
    "⁑",
    "⁓",
    "⁕",
    "⁖",
    "⁗",
    "⁘",
    "⁙",
    "⁚",
    "⁛",
    "⁜",
    "⁝",
    "⁞",
    "\u205f",
    "⁽",
    "₍",
    "⌈",
    "⌊",
    "〈",
    "❨",
    "❪",
    "❬",
    "❮",
    "❰",
    "❲",
    "❴",
    "⟅",
    "⟦",
    "⟨",
    "⟪",
    "⟬",
    "⟮",
    "⦃",
    "⦅",
    "⦇",
    "⦉",
    "⦋",
    "⦍",
    "⦏",
    "⦑",
    "⦓",
    "⦕",
    "⦗",
    "⧘",
    "⧚",
    "⧼",
    "⳹",
    "⳺",
    "⳻",
    "⳼",
    "⳾",
    "⳿",
    "⵰",
    "⸀",
    "⸁",
    "⸆",
    "⸇",
    "⸈",
    "⸋",
    "⸎",
    "⸏",
    "⸐",
    "⸑",
    "⸒",
    "⸓",
    "⸔",
    "⸕",
    "⸖",
    "⸘",
    "⸙",
    "⸛",
    "⸞",
    "⸟",
    "⸢",
    "⸤",
    "⸦",
    "⸨",
    "⸪",
    "⸫",
    "⸬",
    "⸭",
    "⸮",
    "⸰",
    "⸱",
    "⸲",
    "⸳",
    "⸴",
    "⸵",
    "⸶",
    "⸷",
    "⸸",
    "⸹",
    "⸼",
    "⸽",
    "⸾",
    "⸿",
    "⹁",
    "⹂",
    "⹃",
    "⹄",
    "⹅",
    "⹆",
    "⹇",
    "⹈",
    "⹉",
    "⹊",
    "⹋",
    "⹌",
    "⹍",
    "⹎",
    "⹏",
    "⹒",
    "\u3000",
    "、",
    "。",
    "〃",
    "〈",
    "《",
    "「",
    "『",
    "【",
    "〔",
    "〖",
    "〘",
    "〚",
    "〝",
    "〽",
    "゛",
    "゜",
    "・",
    "꓾",
    "꓿",
    "꘍",
    "꘎",
    "꘏",
    "꙳",
    "꙾",
    "꛲",
    "꛳",
    "꛴",
    "꛵",
    "꛶",
    "꛷",
    "꜀",
    "꜁",
    "꜂",
    "꜃",
    "꜄",
    "꜅",
    "꜆",
    "꜇",
    "꜈",
    "꜉",
    "꜊",
    "꜋",
    "꜌",
    "꜍",
    "꜎",
    "꜏",
    "꜐",
    "꜑",
    "꜒",
    "꜓",
    "꜔",
    "꜕",
    "꜖",
    "꜠",
    "꜡",
    "꞉",
    "꞊",
    "꡴",
    "꡵",
    "꡶",
    "꡷",
    "꣎",
    "꣏",
    "꣸",
    "꣹",
    "꣺",
    "꣼",
    "꤮",
    "꤯",
    "꥟",
    "꧁",
    "꧂",
    "꧃",
    "꧄",
    "꧅",
    "꧆",
    "꧇",
    "꧈",
    "꧉",
    "꧊",
    "꧋",
    "꧌",
    "꧍",
    "꧞",
    "꧟",
    "꩜",
    "꩝",
    "꩞",
    "꩟",
    "꫞",
    "꫟",
    "꫰",
    "꫱",
    "꭛",
    "꭪",
    "꭫",
    "꯫",
    "﮲",
    "﮳",
    "﮴",
    "﮵",
    "﮶",
    "﮷",
    "﮸",
    "﮹",
    "﮺",
    "﮻",
    "﮼",
    "﮽",
    "﮾",
    "﮿",
    "﯀",
    "﯁",
    "﴿",
    "︐",
    "︑",
    "︒",
    "︓",
    "︔",
    "︕",
    "︖",
    "︗",
    "︙",
    "︰",
    "︵",
    "︷",
    "︹",
    "︻",
    "︽",
    "︿",
    "﹁",
    "﹃",
    "﹅",
    "﹆",
    "﹇",
    "﹉",
    "﹊",
    "﹋",
    "﹌",
    "﹐",
    "﹑",
    "﹒",
    "﹔",
    "﹕",
    "﹖",
    "﹗",
    "﹙",
    "﹛",
    "﹝",
    "﹟",
    "﹠",
    "﹡",
    "﹨",
    "﹪",
    "﹫",
    "！",
    "＂",
    "＃",
    "％",
    "＆",
    "＇",
    "（",
    "＊",
    "，",
    "．",
    "／",
    "：",
    "；",
    "？",
    "＠",
    "［",
    "＼",
    "＾",
    "｀",
    "｛",
    "｟",
    "｡",
    "｢",
    "､",
    "･",
    "￣",
    "𐄀",
    "𐄁",
    "𐄂",
    "𐎟",
    "𐏐",
    "𐕯",
    "𐡗",
    "𐤟",
    "𐤿",
    "𐩐",
    "𐩑",
    "𐩒",
    "𐩓",
    "𐩔",
    "𐩕",
    "𐩖",
    "𐩗",
    "𐩘",
    "𐩿",
    "𐫰",
    "𐫱",
    "𐫲",
    "𐫳",
    "𐫴",
    "𐫵",
    "𐫶",
    "𐬹",
    "𐬺",
    "𐬻",
    "𐬼",
    "𐬽",
    "𐬾",
    "𐬿",
    "𐮙",
    "𐮚",
    "𐮛",
    "𐮜",
    "𐽕",
    "𐽖",
    "𐽗",
    "𐽘",
    "𐽙",
    "𑁇",
    "𑁈",
    "𑁉",
    "𑁊",
    "𑁋",
    "𑁌",
    "𑁍",
    "𑂻",
    "𑂼",
    "𑂾",
    "𑂿",
    "𑃀",
    "𑃁",
    "𑅀",
    "𑅁",
    "𑅂",
    "𑅃",
    "𑅴",
    "𑅵",
    "𑇅",
    "𑇆",
    "𑇇",
    "𑇈",
    "𑇍",
    "𑇛",
    "𑇝",
    "𑇞",
    "𑇟",
    "𑈸",
    "𑈹",
    "𑈺",
    "𑈻",
    "𑈼",
    "𑈽",
    "𑊩",
    "𑑋",
    "𑑌",
    "𑑍",
    "𑑎",
    "𑑏",
    "𑑚",
    "𑑛",
    "𑑝",
    "𑓆",
    "𑗁",
    "𑗂",
    "𑗃",
    "𑗄",
    "𑗅",
    "𑗆",
    "𑗇",
    "𑗈",
    "𑗉",
    "𑗊",
    "𑗋",
    "𑗌",
    "𑗍",
    "𑗎",
    "𑗏",
    "𑗐",
    "𑗑",
    "𑗒",
    "𑗓",
    "𑗔",
    "𑗕",
    "𑗖",
    "𑗗",
    "𑙁",
    "𑙂",
    "𑙃",
    "𑙠",
    "𑙡",
    "𑙢",
    "𑙣",
    "𑙤",
    "𑙥",
    "𑙦",
    "𑙧",
    "𑙨",
    "𑙩",
    "𑙪",
    "𑙫",
    "𑙬",
    "𑜼",
    "𑜽",
    "𑜾",
    "𑠻",
    "𑥄",
    "𑥅",
    "𑥆",
    "𑧢",
    "𑨿",
    "𑩀",
    "𑩁",
    "𑩂",
    "𑩃",
    "𑩄",
    "𑩅",
    "𑩆",
    "𑪚",
    "𑪛",
    "𑪜",
    "𑪞",
    "𑪟",
    "𑪠",
    "𑪡",
    "𑪢",
    "𑱁",
    "𑱂",
    "𑱃",
    "𑱄",
    "𑱅",
    "𑱰",
    "𑱱",
    "𑻷",
    "𑻸",
    "𑿿",
    "𒑰",
    "𒑱",
    "𒑲",
    "𒑳",
    "𒑴",
    "𖩮",
    "𖩯",
    "𖫵",
    "𖬷",
    "𖬸",
    "𖬹",
    "𖬺",
    "𖬻",
    "𖭄",
    "𖺗",
    "𖺘",
    "𖺙",
    "𖺚",
    "𖿢",
    "𛲟",
    "𝪇",
    "𝪈",
    "𝪉",
    "𝪊",
    "𝪋",
    "𞥞",
    "𞥟",
    "🏻",
    "🏼",
    "🏽",
    "🏾",
    "🏿",
)
