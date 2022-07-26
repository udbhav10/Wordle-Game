from tkinter import messagebox
from tkinter import *
import random
from nltk.corpus import words

wordlist = ['aback',
'abase',
'abate',
'abbey',
'abbot',
'abhor',
'abide',
'abled',
'abode',
'abort',
'about',
'above',
'abuse',
'abyss',
'acorn',
'acrid',
'actor',
'acute',
'adage',
'adapt',
'adept',
'admin',
'admit',
'adobe',
'adopt',
'adore',
'adorn',
'adult',
'affix',
'afire',
'afoot',
'afoul',
'after',
'again',
'agape',
'agate',
'agent',
'agile',
'aging',
'aglow',
'agony',
'agora',
'agree',
'ahead',
'aider',
'aisle',
'alarm',
'album',
'alert',
'algae',
'alibi',
'alien',
'align',
'alike',
'alive',
'allay',
'alley',
'allot',
'allow',
'alloy',
'aloft',
'alone',
'along',
'aloof',
'aloud',
'alpha',
'altar',
'alter',
'amass',
'amaze',
'amber',
'amble',
'amend',
'amiss',
'amity',
'among',
'ample',
'amply',
'amuse',
'angel',
'anger',
'angle',
'angry',
'angst',
'anime',
'ankle',
'annex',
'annoy',
'annul',
'anode',
'antic',
'anvil',
'aorta',
'apart',
'aphid',
'aping',
'apnea',
'apple',
'apply',
'apron',
'aptly',
'arbor',
'ardor',
'arena',
'argue',
'arise',
'armor',
'aroma',
'arose',
'array',
'arrow',
'arson',
'artsy',
'ascot',
'ashen',
'aside',
'askew',
'assay',
'asset',
'atoll',
'atone',
'attic',
'audio',
'audit',
'augur',
'aunty',
'avail',
'avert',
'avian',
'avoid',
'await',
'awake',
'award',
'aware',
'awash',
'awful',
'awoke',
'axial',
'axiom',
'axion',
'azure',
'bacon',
'badge',
'badly',
'bagel',
'baggy',
'baker',
'baler',
'balmy',
'banal',
'banjo',
'barge',
'baron',
'basal',
'basic',
'basil',
'basin',
'basis',
'baste',
'batch',
'bathe',
'baton',
'batty',
'bawdy',
'bayou',
'beach',
'beady',
'beard',
'beast',
'beech',
'beefy',
'befit',
'began',
'begat',
'beget',
'begin',
'begun',
'being',
'belch',
'belie',
'belle',
'belly',
'below',
'bench',
'beret',
'berry',
'berth',
'beset',
'betel',
'bevel',
'bezel',
'bible',
'bicep',
'biddy',
'bigot',
'bilge',
'billy',
'binge',
'bingo',
'biome',
'birch',
'birth',
'bison',
'bitty',
'black',
'blade',
'blame',
'bland',
'blank',
'blare',
'blast',
'blaze',
'bleak',
'bleat',
'bleed',
'bleep',
'blend',
'bless',
'blimp',
'blind',
'blink',
'bliss',
'blitz',
'bloat',
'block',
'bloke',
'blond',
'blood',
'bloom',
'blown',
'bluer',
'bluff',
'blunt',
'blurb',
'blurt',
'blush',
'board',
'boast',
'bobby',
'boney',
'bongo',
'bonus',
'booby',
'boost',
'booth',
'booty',
'booze',
'boozy',
'borax',
'borne',
'bosom',
'bossy',
'botch',
'bough',
'boule',
'bound',
'bowel',
'boxer',
'brace',
'braid',
'brain',
'brake',
'brand',
'brash',
'brass',
'brave',
'bravo',
'brawl',
'brawn',
'bread',
'break',
'breed',
'briar',
'bribe',
'brick',
'bride',
'brief',
'brine',
'bring',
'brink',
'briny',
'brisk',
'broad',
'broil',
'broke',
'brood',
'brook',
'broom',
'broth',
'brown',
'brunt',
'brush',
'brute',
'buddy',
'budge',
'buggy',
'bugle',
'build',
'built',
'bulge',
'bulky',
'bully',
'bunch',
'bunny',
'burly',
'burnt',
'burst',
'bused',
'bushy',
'butch',
'butte',
'buxom',
'buyer',
'bylaw',
'cabal',
'cabby',
'cabin',
'cable',
'cacao',
'cache',
'cacti',
'caddy',
'cadet',
'cagey',
'cairn',
'camel',
'cameo',
'canal',
'candy',
'canny',
'canoe',
'canon',
'caper',
'caput',
'carat',
'cargo',
'carol',
'carry',
'carve',
'caste',
'catch',
'cater',
'catty',
'caulk',
'cause',
'cavil',
'cease',
'cedar',
'cello',
'chafe',
'chaff',
'chain',
'chair',
'chalk',
'champ',
'chant',
'chaos',
'chard',
'charm',
'chart',
'chase',
'chasm',
'cheap',
'cheat',
'check',
'cheek',
'cheer',
'chess',
'chest',
'chick',
'chide',
'chief',
'child',
'chili',
'chill',
'chime',
'china',
'chirp',
'chock',
'choir',
'choke',
'chord',
'chore',
'chose',
'chuck',
'chump',
'chunk',
'churn',
'chute',
'cider',
'cigar',
'cinch',
'circa',
'civic',
'civil',
'clack',
'claim',
'clamp',
'clang',
'clank',
'clash',
'clasp',
'class',
'clean',
'clear',
'cleat',
'cleft',
'clerk',
'click',
'cliff',
'climb',
'cling',
'clink',
'cloak',
'clock',
'clone',
'close',
'cloth',
'cloud',
'clout',
'clove',
'clown',
'cluck',
'clued',
'clump',
'clung',
'coach',
'coast',
'cobra',
'cocoa',
'colon',
'color',
'comet',
'comfy',
'comic',
'comma',
'conch',
'condo',
'conic',
'copse',
'coral',
'corer',
'corny',
'couch',
'cough',
'could',
'count',
'coupe',
'court',
'coven',
'cover',
'covet',
'covey',
'cower',
'coyly',
'crack',
'craft',
'cramp',
'crane',
'crank',
'crash',
'crass',
'crate',
'crave',
'crawl',
'craze',
'crazy',
'creak',
'cream',
'credo',
'creed',
'creek',
'creep',
'creme',
'crepe',
'crept',
'cress',
'crest',
'crick',
'cried',
'crier',
'crime',
'crimp',
'crisp',
'croak',
'crock',
'crone',
'crony',
'crook',
'cross',
'croup',
'crowd',
'crown',
'crude',
'cruel',
'crumb',
'crump',
'crush',
'crust',
'crypt',
'cubic',
'cumin',
'curio',
'curly',
'curry',
'curse',
'curve',
'curvy',
'cutie',
'cyber',
'cycle',
'cynic',
'daddy',
'daily',
'dairy',
'daisy',
'dally',
'dance',
'dandy',
'datum',
'daunt',
'dealt',
'death',
'debar',
'debit',
'debug',
'debut',
'decal',
'decay',
'decor',
'decoy',
'decry',
'defer',
'deign',
'deity',
'delay',
'delta',
'delve',
'demon',
'demur',
'denim',
'dense',
'depot',
'depth',
'derby',
'deter',
'detox',
'deuce',
'devil',
'diary',
'dicey',
'digit',
'dilly',
'dimly',
'diner',
'dingo',
'dingy',
'diode',
'dirge',
'dirty',
'disco',
'ditch',
'ditto',
'ditty',
'diver',
'dizzy',
'dodge',
'dodgy',
'dogma',
'doing',
'dolly',
'donor',
'donut',
'dopey',
'doubt',
'dough',
'dowdy',
'dowel',
'downy',
'dowry',
'dozen',
'draft',
'drain',
'drake',
'drama',
'drank',
'drape',
'drawl',
'drawn',
'dread',
'dream',
'dress',
'dried',
'drier',
'drift',
'drill',
'drink',
'drive',
'droit',
'droll',
'drone',
'drool',
'droop',
'dross',
'drove',
'drown',
'druid',
'drunk',
'dryer',
'dryly',
'duchy',
'dully',
'dummy',
'dumpy',
'dunce',
'dusky',
'dusty',
'dutch',
'duvet',
'dwarf',
'dwell',
'dwelt',
'dying',
'eager',
'eagle',
'early',
'earth',
'easel',
'eaten',
'eater',
'ebony',
'eclat',
'edict',
'edify',
'eerie',
'egret',
'eight',
'eject',
'eking',
'elate',
'elbow',
'elder',
'elect',
'elegy',
'elfin',
'elide',
'elite',
'elope',
'elude',
'email',
'embed',
'ember',
'emcee',
'empty',
'enact',
'endow',
'enema',
'enemy',
'enjoy',
'ennui',
'ensue',
'enter',
'entry',
'envoy',
'epoch',
'epoxy',
'equal',
'equip',
'erase',
'erect',
'erode',
'error',
'erupt',
'essay',
'ester',
'ether',
'ethic',
'ethos',
'etude',
'evade',
'event',
'every',
'evict',
'evoke',
'exact',
'exalt',
'excel',
'exert',
'exile',
'exist',
'expel',
'extol',
'extra',
'exult',
'eying',
'fable',
'facet',
'faint',
'fairy',
'faith',
'FALSE',
'fancy',
'fanny',
'farce',
'fatal',
'fatty',
'fault',
'fauna',
'favor',
'feast',
'fecal',
'feign',
'fella',
'felon',
'femme',
'femur',
'fence',
'feral',
'ferry',
'fetal',
'fetch',
'fetid',
'fetus',
'fever',
'fewer',
'fiber',
'fibre',
'ficus',
'field',
'fiend',
'fiery',
'fifth',
'fifty',
'fight',
'filer',
'filet',
'filly',
'filmy',
'filth',
'final',
'finch',
'finer',
'first',
'fishy',
'fixer',
'fizzy',
'fjord',
'flack',
'flail',
'flair',
'flake',
'flaky',
'flame',
'flank',
'flare',
'flash',
'flask',
'fleck',
'fleet',
'flesh',
'flick',
'flier',
'fling',
'flint',
'flirt',
'float',
'flock',
'flood',
'floor',
'flora',
'floss',
'flour',
'flout',
'flown',
'fluff',
'fluid',
'fluke',
'flume',
'flung',
'flunk',
'flush',
'flute',
'flyer',
'foamy',
'focal',
'focus',
'foggy',
'foist',
'folio',
'folly',
'foray',
'force',
'forge',
'forgo',
'forte',
'forth',
'forty',
'forum',
'found',
'foyer',
'frail',
'frame',
'frank',
'fraud',
'freak',
'freed',
'freer',
'fresh',
'friar',
'fried',
'frill',
'frisk',
'fritz',
'frock',
'frond',
'front',
'frost',
'froth',
'frown',
'froze',
'fruit',
'fudge',
'fugue',
'fully',
'fungi',
'funky',
'funny',
'furor',
'furry',
'fussy',
'fuzzy',
'gaffe',
'gaily',
'gamer',
'gamma',
'gamut',
'gassy',
'gaudy',
'gauge',
'gaunt',
'gauze',
'gavel',
'gawky',
'gayer',
'gayly',
'gazer',
'gecko',
'geeky',
'geese',
'genie',
'genre',
'ghost',
'ghoul',
'giant',
'giddy',
'gipsy',
'girly',
'girth',
'given',
'giver',
'glade',
'gland',
'glare',
'glass',
'glaze',
'gleam',
'glean',
'glide',
'glint',
'gloat',
'globe',
'gloom',
'glory',
'gloss',
'glove',
'glyph',
'gnash',
'gnome',
'godly',
'going',
'golem',
'golly',
'gonad',
'goner',
'goody',
'gooey',
'goofy',
'goose',
'gorge',
'gouge',
'gourd',
'grace',
'grade',
'graft',
'grail',
'grain',
'grand',
'grant',
'grape',
'graph',
'grasp',
'grass',
'grate',
'grave',
'gravy',
'graze',
'great',
'greed',
'green',
'greet',
'grief',
'grill',
'grime',
'grimy',
'grind',
'gripe',
'groan',
'groin',
'groom',
'grope',
'gross',
'group',
'grout',
'grove',
'growl',
'grown',
'gruel',
'gruff',
'grunt',
'guard',
'guava',
'guess',
'guest',
'guide',
'guild',
'guile',
'guilt',
'guise',
'gulch',
'gully',
'gumbo',
'gummy',
'guppy',
'gusto',
'gusty',
'gypsy',
'habit',
'hairy',
'halve',
'handy',
'happy',
'hardy',
'harem',
'harpy',
'harry',
'harsh',
'haste',
'hasty',
'hatch',
'hater',
'haunt',
'haute',
'haven',
'havoc',
'hazel',
'heady',
'heard',
'heart',
'heath',
'heave',
'heavy',
'hedge',
'hefty',
'heist',
'helix',
'hello',
'hence',
'heron',
'hilly',
'hinge',
'hippo',
'hippy',
'hitch',
'hoard',
'hobby',
'hoist',
'holly',
'homer',
'honey',
'honor',
'horde',
'horny',
'horse',
'hotel',
'hotly',
'hound',
'house',
'hovel',
'hover',
'howdy',
'human',
'humid',
'humor',
'humph',
'humus',
'hunch',
'hunky',
'hurry',
'husky',
'hussy',
'hutch',
'hydro',
'hyena',
'hymen',
'hyper',
'icily',
'icing',
'ideal',
'idiom',
'idiot',
'idler',
'idyll',
'igloo',
'iliac',
'image',
'imbue',
'impel',
'imply',
'inane',
'inbox',
'incur',
'index',
'inept',
'inert',
'infer',
'ingot',
'inlay',
'inlet',
'inner',
'input',
'inter',
'intro',
'ionic',
'irate',
'irony',
'islet',
'issue',
'itchy',
'ivory',
'jaunt',
'jazzy',
'jelly',
'jerky',
'jetty',
'jewel',
'jiffy',
'joint',
'joist',
'joker',
'jolly',
'joust',
'judge',
'juice',
'juicy',
'jumbo',
'jumpy',
'junta',
'junto',
'juror',
'kappa',
'karma',
'kayak',
'kebab',
'khaki',
'kinky',
'kiosk',
'kitty',
'knack',
'knave',
'knead',
'kneed',
'kneel',
'knelt',
'knife',
'knock',
'knoll',
'known',
'koala',
'krill',
'label',
'labor',
'laden',
'ladle',
'lager',
'lance',
'lanky',
'lapel',
'lapse',
'large',
'larva',
'lasso',
'latch',
'later',
'lathe',
'latte',
'laugh',
'layer',
'leach',
'leafy',
'leaky',
'leant',
'leapt',
'learn',
'lease',
'leash',
'least',
'leave',
'ledge',
'leech',
'leery',
'lefty',
'legal',
'leggy',
'lemon',
'lemur',
'leper',
'level',
'lever',
'libel',
'liege',
'light',
'liken',
'lilac',
'limbo',
'limit',
'linen',
'liner',
'lingo',
'lipid',
'lithe',
'liver',
'livid',
'llama',
'loamy',
'loath',
'lobby',
'local',
'locus',
'lodge',
'lofty',
'logic',
'login',
'loopy',
'loose',
'lorry',
'loser',
'louse',
'lousy',
'lover',
'lower',
'lowly',
'loyal',
'lucid',
'lucky',
'lumen',
'lumpy',
'lunar',
'lunch',
'lunge',
'lupus',
'lurch',
'lurid',
'lusty',
'lying',
'lymph',
'lynch',
'lyric',
'macaw',
'macho',
'macro',
'madam',
'madly',
'mafia',
'magic',
'magma',
'maize',
'major',
'maker',
'mambo',
'mamma',
'mammy',
'manga',
'mange',
'mango',
'mangy',
'mania',
'manic',
'manly',
'manor',
'maple',
'march',
'marry',
'marsh',
'mason',
'masse',
'match',
'matey',
'mauve',
'maxim',
'maybe',
'mayor',
'mealy',
'meant',
'meaty',
'mecca',
'medal',
'media',
'medic',
'melee',
'melon',
'mercy',
'merge',
'merit',
'merry',
'metal',
'meter',
'metro',
'micro',
'midge',
'midst',
'might',
'milky',
'mimic',
'mince',
'miner',
'minim',
'minor',
'minty',
'minus',
'mirth',
'miser',
'missy',
'mocha',
'modal',
'model',
'modem',
'mogul',
'moist',
'molar',
'moldy',
'money',
'month',
'moody',
'moose',
'moral',
'moron',
'morph',
'mossy',
'motel',
'motif',
'motor',
'motto',
'moult',
'mound',
'mount',
'mourn',
'mouse',
'mouth',
'mover',
'movie',
'mower',
'mucky',
'mucus',
'muddy',
'mulch',
'mummy',
'munch',
'mural',
'murky',
'mushy',
'music',
'musky',
'musty',
'myrrh',
'nadir',
'naive',
'nanny',
'nasal',
'nasty',
'natal',
'naval',
'navel',
'needy',
'neigh',
'nerdy',
'nerve',
'never',
'newer',
'newly',
'nicer',
'niche',
'niece',
'night',
'ninja',
'ninny',
'ninth',
'noble',
'nobly',
'noise',
'noisy',
'nomad',
'noose',
'north',
'nosey',
'notch',
'novel',
'nudge',
'nurse',
'nutty',
'nylon',
'nymph',
'oaken',
'obese',
'occur',
'ocean',
'octal',
'octet',
'odder',
'oddly',
'offal',
'offer',
'often',
'olden',
'older',
'olive',
'ombre',
'omega',
'onion',
'onset',
'opera',
'opine',
'opium',
'optic',
'orbit',
'order',
'organ',
'other',
'otter',
'ought',
'ounce',
'outdo',
'outer',
'outgo',
'ovary',
'ovate',
'overt',
'ovine',
'ovoid',
'owing',
'owner',
'oxide',
'ozone',
'paddy',
'pagan',
'paint',
'paler',
'palsy',
'panel',
'panic',
'pansy',
'papal',
'paper',
'parer',
'parka',
'parry',
'parse',
'party',
'pasta',
'paste',
'pasty',
'patch',
'patio',
'patsy',
'patty',
'pause',
'payee',
'payer',
'peace',
'peach',
'pearl',
'pecan',
'pedal',
'penal',
'pence',
'penne',
'penny',
'perch',
'peril',
'perky',
'pesky',
'pesto',
'petal',
'petty',
'phase',
'phone',
'phony',
'photo',
'piano',
'picky',
'piece',
'piety',
'piggy',
'pilot',
'pinch',
'piney',
'pinky',
'pinto',
'piper',
'pique',
'pitch',
'pithy',
'pivot',
'pixel',
'pixie',
'pizza',
'place',
'plaid',
'plain',
'plait',
'plane',
'plank',
'plant',
'plate',
'plaza',
'plead',
'pleat',
'plied',
'plier',
'pluck',
'plumb',
'plume',
'plump',
'plunk',
'plush',
'poesy',
'point',
'poise',
'poker',
'polar',
'polka',
'polyp',
'pooch',
'poppy',
'porch',
'poser',
'posit',
'posse',
'pouch',
'pound',
'pouty',
'power',
'prank',
'prawn',
'preen',
'press',
'price',
'prick',
'pride',
'pried',
'prime',
'primo',
'print',
'prior',
'prism',
'privy',
'prize',
'probe',
'prone',
'prong',
'proof',
'prose',
'proud',
'prove',
'prowl',
'proxy',
'prude',
'prune',
'psalm',
'pubic',
'pudgy',
'puffy',
'pulpy',
'pulse',
'punch',
'pupal',
'pupil',
'puppy',
'puree',
'purer',
'purge',
'purse',
'pushy',
'putty',
'pygmy',
'quack',
'quail',
'quake',
'qualm',
'quark',
'quart',
'quash',
'quasi',
'queen',
'queer',
'quell',
'query',
'quest',
'queue',
'quick',
'quiet',
'quill',
'quilt',
'quirk',
'quite',
'quota',
'quote',
'quoth',
'rabbi',
'rabid',
'racer',
'radar',
'radii',
'radio',
'rainy',
'raise',
'rajah',
'rally',
'ralph',
'ramen',
'ranch',
'randy',
'range',
'rapid',
'rarer',
'raspy',
'ratio',
'ratty',
'raven',
'rayon',
'razor',
'reach',
'react',
'ready',
'realm',
'rearm',
'rebar',
'rebel',
'rebus',
'rebut',
'recap',
'recur',
'recut',
'reedy',
'refer',
'refit',
'regal',
'rehab',
'reign',
'relax',
'relay',
'relic',
'remit',
'renal',
'renew',
'repay',
'repel',
'reply',
'rerun',
'reset',
'resin',
'retch',
'retro',
'retry',
'reuse',
'revel',
'revue',
'rhino',
'rhyme',
'rider',
'ridge',
'rifle',
'right',
'rigid',
'rigor',
'rinse',
'ripen',
'riper',
'risen',
'riser',
'risky',
'rival',
'river',
'rivet',
'roach',
'roast',
'robin',
'robot',
'rocky',
'rodeo',
'roger',
'rogue',
'roomy',
'roost',
'rotor',
'rouge',
'rough',
'round',
'rouse',
'route',
'rover',
'rowdy',
'rower',
'royal',
'ruddy',
'ruder',
'rugby',
'ruler',
'rumba',
'rumor',
'rupee',
'rural',
'rusty',
'sadly',
'safer',
'saint',
'salad',
'sally',
'salon',
'salsa',
'salty',
'salve',
'salvo',
'sandy',
'saner',
'sappy',
'sassy',
'satin',
'satyr',
'sauce',
'saucy',
'sauna',
'saute',
'savor',
'savoy',
'savvy',
'scald',
'scale',
'scalp',
'scaly',
'scamp',
'scant',
'scare',
'scarf',
'scary',
'scene',
'scent',
'scion',
'scoff',
'scold',
'scone',
'scoop',
'scope',
'score',
'scorn',
'scour',
'scout',
'scowl',
'scram',
'scrap',
'scree',
'screw',
'scrub',
'scrum',
'scuba',
'sedan',
'seedy',
'segue',
'seize',
'semen',
'sense',
'sepia',
'serif',
'serum',
'serve',
'setup',
'seven',
'sever',
'sewer',
'shack',
'shade',
'shady',
'shaft',
'shake',
'shaky',
'shale',
'shall',
'shalt',
'shame',
'shank',
'shape',
'shard',
'share',
'shark',
'sharp',
'shave',
'shawl',
'shear',
'sheen',
'sheep',
'sheer',
'sheet',
'sheik',
'shelf',
'shell',
'shied',
'shift',
'shine',
'shiny',
'shire',
'shirk',
'shirt',
'shoal',
'shock',
'shone',
'shook',
'shoot',
'shore',
'shorn',
'short',
'shout',
'shove',
'shown',
'showy',
'shrew',
'shrub',
'shrug',
'shuck',
'shunt',
'shush',
'shyly',
'siege',
'sieve',
'sight',
'sigma',
'silky',
'silly',
'since',
'sinew',
'singe',
'siren',
'sissy',
'sixth',
'sixty',
'skate',
'skier',
'skiff',
'skill',
'skimp',
'skirt',
'skulk',
'skull',
'skunk',
'slack',
'slain',
'slang',
'slant',
'slash',
'slate',
'slave',
'sleek',
'sleep',
'sleet',
'slept',
'slice',
'slick',
'slide',
'slime',
'slimy',
'sling',
'slink',
'sloop',
'slope',
'slosh',
'sloth',
'slump',
'slung',
'slunk',
'slurp',
'slush',
'slyly',
'smack',
'small',
'smart',
'smash',
'smear',
'smell',
'smelt',
'smile',
'smirk',
'smite',
'smith',
'smock',
'smoke',
'smoky',
'smote',
'snack',
'snail',
'snake',
'snaky',
'snare',
'snarl',
'sneak',
'sneer',
'snide',
'sniff',
'snipe',
'snoop',
'snore',
'snort',
'snout',
'snowy',
'snuck',
'snuff',
'soapy',
'sober',
'soggy',
'solar',
'solid',
'solve',
'sonar',
'sonic',
'sooth',
'sooty',
'sorry',
'sound',
'south',
'sower',
'space',
'spade',
'spank',
'spare',
'spark',
'spasm',
'spawn',
'speak',
'spear',
'speck',
'speed',
'spell',
'spelt',
'spend',
'spent',
'sperm',
'spice',
'spicy',
'spied',
'spiel',
'spike',
'spiky',
'spill',
'spilt',
'spine',
'spiny',
'spire',
'spite',
'splat',
'split',
'spoil',
'spoke',
'spoof',
'spook',
'spool',
'spoon',
'spore',
'sport',
'spout',
'spray',
'spree',
'sprig',
'spunk',
'spurn',
'spurt',
'squad',
'squat',
'squib',
'stack',
'staff',
'stage',
'staid',
'stain',
'stair',
'stake',
'stale',
'stalk',
'stall',
'stamp',
'stand',
'stank',
'stare',
'stark',
'start',
'stash',
'state',
'stave',
'stead',
'steak',
'steal',
'steam',
'steed',
'steel',
'steep',
'steer',
'stein',
'stern',
'stick',
'stiff',
'still',
'stilt',
'sting',
'stink',
'stint',
'stock',
'stoic',
'stoke',
'stole',
'stomp',
'stone',
'stony',
'stood',
'stool',
'stoop',
'store',
'stork',
'storm',
'story',
'stout',
'stove',
'strap',
'straw',
'stray',
'strip',
'strut',
'stuck',
'study',
'stuff',
'stump',
'stung',
'stunk',
'stunt',
'style',
'suave',
'sugar',
'suing',
'suite',
'sulky',
'sully',
'sumac',
'sunny',
'super',
'surer',
'surge',
'surly',
'sushi',
'swami',
'swamp',
'swarm',
'swash',
'swath',
'swear',
'sweat',
'sweep',
'sweet',
'swell',
'swept',
'swift',
'swill',
'swine',
'swing',
'swirl',
'swish',
'swoon',
'swoop',
'sword',
'swore',
'sworn',
'swung',
'synod',
'syrup',
'tabby',
'table',
'taboo',
'tacit',
'tacky',
'taffy',
'taint',
'taken',
'taker',
'tally',
'talon',
'tamer',
'tango',
'tangy',
'taper',
'tapir',
'tardy',
'tarot',
'taste',
'tasty',
'tatty',
'taunt',
'tawny',
'teach',
'teary',
'tease',
'teddy',
'teeth',
'tempo',
'tenet',
'tenor',
'tense',
'tenth',
'tepee',
'tepid',
'terra',
'terse',
'testy',
'thank',
'theft',
'their',
'theme',
'there',
'these',
'theta',
'thick',
'thief',
'thigh',
'thing',
'think',
'third',
'thong',
'thorn',
'those',
'three',
'threw',
'throb',
'throw',
'thrum',
'thumb',
'thump',
'thyme',
'tiara',
'tibia',
'tidal',
'tiger',
'tight',
'tilde',
'timer',
'timid',
'tipsy',
'titan',
'tithe',
'title',
'toast',
'today',
'toddy',
'token',
'tonal',
'tonga',
'tonic',
'tooth',
'topaz',
'topic',
'torch',
'torso',
'torus',
'total',
'totem',
'touch',
'tough',
'towel',
'tower',
'toxic',
'toxin',
'trace',
'track',
'tract',
'trade',
'trail',
'train',
'trait',
'tramp',
'trash',
'trawl',
'tread',
'treat',
'trend',
'triad',
'trial',
'tribe',
'trice',
'trick',
'tried',
'tripe',
'trite',
'troll',
'troop',
'trope',
'trout',
'trove',
'truce',
'truck',
'truer',
'truly',
'trump',
'trunk',
'truss',
'trust',
'truth',
'tryst',
'tubal',
'tuber',
'tulip',
'tulle',
'tumor',
'tunic',
'turbo',
'tutor',
'twang',
'tweak',
'tweed',
'tweet',
'twice',
'twine',
'twirl',
'twist',
'twixt',
'tying',
'udder',
'ulcer',
'ultra',
'umbra',
'uncle',
'uncut',
'under',
'undid',
'undue',
'unfed',
'unfit',
'unify',
'union',
'unite',
'unity',
'unlit',
'unmet',
'unset',
'untie',
'until',
'unwed',
'unzip',
'upper',
'upset',
'urban',
'urine',
'usage',
'usher',
'using',
'usual',
'usurp',
'utile',
'utter',
'vague',
'valet',
'valid',
'valor',
'value',
'valve',
'vapid',
'vapor',
'vault',
'vaunt',
'vegan',
'venom',
'venue',
'verge',
'verse',
'verso',
'verve',
'vicar',
'video',
'vigil',
'vigor',
'villa',
'vinyl',
'viola',
'viper',
'viral',
'virus',
'visit',
'visor',
'vista',
'vital',
'vivid',
'vixen',
'vocal',
'vodka',
'vogue',
'voice',
'voila',
'vomit',
'voter',
'vouch',
'vowel',
'vying',
'wacky',
'wafer',
'wager',
'wagon',
'waist',
'waive',
'waltz',
'warty',
'waste',
'watch',
'water',
'waver',
'waxen',
'weary',
'weave',
'wedge',
'weedy',
'weigh',
'weird',
'welch',
'welsh',
'wench',
'whack',
'whale',
'wharf',
'wheat',
'wheel',
'whelp',
'where',
'which',
'whiff',
'while',
'whine',
'whiny',
'whirl',
'whisk',
'white',
'whole',
'whoop',
'whose',
'widen',
'wider',
'widow',
'width',
'wield',
'wight',
'willy',
'wimpy',
'wince',
'winch',
'windy',
'wiser',
'wispy',
'witch',
'witty',
'woken',
'woman',
'women',
'woody',
'wooer',
'wooly',
'woozy',
'wordy',
'world',
'worry',
'worse',
'worst',
'worth',
'would',
'wound',
'woven',
'wrack',
'wrath',
'wreak',
'wreck',
'wrest',
'wring',
'wrist',
'write',
'wrong',
'wrote',
'wrung',
'wryly',
'yacht',
'yearn',
'yeast',
'yield',
'young',
'youth',
'zebra',
'zesty',
'zonal']

alphabet = ['Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']

root = Tk()
root.title("Wordle")
root.iconbitmap('Artboard 1.ico')
mainframe = Frame(root,borderwidth=1,relief=SOLID)
mainframe.grid(row=0,column=0)
# root.geometry("335x420")
# root.eval('tk::PlaceWindow . N')

def CreateSpace():
    global guessedletters
    guessedletters = []
    global greenletters
    greenletters = []
    global guessnum
    guessnum = 0
    global Label11,Label12,Label13,Label14,Label15,Label21,Label22,Label23,Label24,Label25,Label31,Label32,Label33,Label34,Label35,Label41,Label42,Label43,Label44,Label45,Label51,Label52,Label53,Label54,Label55,Label61,Label62,Label63,Label64,Label65
    global LabelList1,LabelList2,LabelList3,LabelList4,LabelList5,LabelList6
    global LabelGrid
    global word
    word = random.choice(wordlist)
    # word = 'gauge'
    word = word.upper()

    Label11 = Label(mainframe,borderwidth=1, relief="solid",width=7,height=3)
    Label12 = Label(mainframe,borderwidth=1, relief="solid",width=7,height=3)
    Label13 = Label(mainframe,borderwidth=1, relief="solid",width=7,height=3)
    Label14 = Label(mainframe,borderwidth=1, relief="solid",width=7,height=3)
    Label15 = Label(mainframe,borderwidth=1, relief="solid",width=7,height=3)

    Label21 = Label(mainframe,borderwidth=1, relief="solid",width=7,height=3)
    Label22 = Label(mainframe,borderwidth=1, relief="solid",width=7,height=3)
    Label23 = Label(mainframe,borderwidth=1, relief="solid",width=7,height=3)
    Label24 = Label(mainframe,borderwidth=1, relief="solid",width=7,height=3)
    Label25 = Label(mainframe,borderwidth=1, relief="solid",width=7,height=3)

    Label31 = Label(mainframe,borderwidth=1, relief="solid",width=7,height=3)
    Label32 = Label(mainframe,borderwidth=1, relief="solid",width=7,height=3)
    Label33 = Label(mainframe,borderwidth=1, relief="solid",width=7,height=3)
    Label34 = Label(mainframe,borderwidth=1, relief="solid",width=7,height=3)
    Label35 = Label(mainframe,borderwidth=1, relief="solid",width=7,height=3)

    Label41 = Label(mainframe,borderwidth=1, relief="solid",width=7,height=3)
    Label42 = Label(mainframe,borderwidth=1, relief="solid",width=7,height=3)
    Label43 = Label(mainframe,borderwidth=1, relief="solid",width=7,height=3)
    Label44 = Label(mainframe,borderwidth=1, relief="solid",width=7,height=3)
    Label45 = Label(mainframe,borderwidth=1, relief="solid",width=7,height=3)

    Label51 = Label(mainframe,borderwidth=1, relief="solid",width=7,height=3)
    Label52 = Label(mainframe,borderwidth=1, relief="solid",width=7,height=3)
    Label53 = Label(mainframe,borderwidth=1, relief="solid",width=7,height=3)
    Label54 = Label(mainframe,borderwidth=1, relief="solid",width=7,height=3)
    Label55 = Label(mainframe,borderwidth=1, relief="solid",width=7,height=3)

    Label61 = Label(mainframe,borderwidth=1, relief="solid",width=7,height=3)
    Label62 = Label(mainframe,borderwidth=1, relief="solid",width=7,height=3)
    Label63 = Label(mainframe,borderwidth=1, relief="solid",width=7,height=3)
    Label64 = Label(mainframe,borderwidth=1, relief="solid",width=7,height=3)
    Label65 = Label(mainframe,borderwidth=1, relief="solid",width=7,height=3)



    LabelList1 = [Label11,Label12,Label13,Label14,Label15]
    LabelList2 = [Label21,Label22,Label23,Label24,Label25]
    LabelList3 = [Label31,Label32,Label33,Label34,Label35]
    LabelList4 = [Label41,Label42,Label43,Label44,Label45]
    LabelList5 = [Label51,Label52,Label53,Label54,Label55]
    LabelList6 = [Label61,Label62,Label63,Label64,Label65]

    LabelGrid = [LabelList1,LabelList2,LabelList3,LabelList4,LabelList5,LabelList6]

    for i in range(6):
        for j in range(5):
            (LabelGrid[i])[j].grid(row=i+2,column=j,pady=2)

    CreateKeyboard()


def inputtoguess(event):
    letters = []
    for x in word:
        letters.append(x)


    global guessnum
    global guessbutton
    guess_word = guess.get().upper()

    if ((guess_word.lower() not in [w for w in words.words() if len(w) == 5]) and (guess_word.lower() not in wordlist)):
       messagebox.showerror('Error', 'Not a valid guess')
       guess.delete(0, END)
       return

    keyboardcolor(guess_word)
    for i in range(5):

        letterindex = alphabet.index(guess_word[i])
        # print(letterindex)
        if guess_word[i] == word[i]:
            (LabelGrid[guessnum])[i] = Label(mainframe,text = guess_word[i],borderwidth=1, relief="solid",width=7,height=3,fg='white',bg='#6aaa64')
            letters.remove(guess_word[i])

        else:
            (LabelGrid[guessnum])[i] = Label(mainframe, text=guess_word[i], borderwidth=1, relief="solid",width=7, height=3,fg='white', bg='#787c7e')

    for i in range(5):
        if guess_word[i] in letters and guess_word[i] != word[i]:
            (LabelGrid[guessnum])[i] = Label(mainframe, text=guess_word[i],borderwidth=1, relief="solid", width=7, height=3,fg='white',bg='#c9b458')
            letters.remove(guess_word[i])

        ((LabelGrid[guessnum])[i]).grid(row=guessnum+2, column=i, pady=2)
    # print(guessedletters)
    guess.delete(0, END)

    guessbutton = Button(mainframe, text="Guess", command=lambda: inputtoguess(guessnum+1),width=7,height=3)

    guessbutton.grid(row=8, column=0)
    # guessbutton.bind('<Enter>', on_enter)
    # guessbutton.bind('<Leave>', on_leave)
    guessnum+=1

    if guess_word == word:
        res = messagebox.askquestion('VICTORY', 'YOU WON! Do you want to start a new game?')
        if res == 'yes':
            CreateSpace()
        else:
            root.quit()

    elif(guessnum == 6):
        res = messagebox.askquestion('ATTEMPTS OVER', 'YOU LOST! The word was ' + word + '! Do you want to start a new game?')
        if res == 'yes':
            CreateSpace()
        else:
            root.quit()


def keyboardcolor(guess):
    global guessedletters
    global keyboard
    global greenletters
    for i in range(5):
        guessedletters.append(guess[i])
        if guess[i] in greenletters:
            continue
        letterindex = alphabet.index(guess[i])
        if guess[i] == word[i]:
            keyboard[letterindex].config(fg='white',bg='#6aaa64')
            greenletters.append(guess[i])
        elif guess[i] in word:
            keyboard[letterindex].config(fg='white', bg='#c9b458')
        else:
            keyboard[letterindex].config(fg='white', bg='#787c7e')



def CreateKeyboard():
    global EnterButton
    global Backspace
    global keyQ, keyW, keyE, keyR, keyT, keyY, keyU, keyI, keyO, keyP, keyA, keyS, keyD, keyF, keyG, keyH, keyI, keyJ, keyK, keyL, keyZ, keyX, keyC, keyV, keyB, keyN, keyM
    global keyboard
    global keyframe
    keyframe = Frame(root,borderwidth=1,relief=SOLID)
    keyQ = Button(keyframe, text=alphabet[0], borderwidth=1, relief="solid", width=5, height=2, command = lambda: PressKey(0))
    keyW = Button(keyframe, text=alphabet[1], borderwidth=1, relief="solid", width=5, height=2, command = lambda: PressKey(1))
    keyE = Button(keyframe, text=alphabet[2], borderwidth=1, relief="solid", width=5, height=2, command = lambda: PressKey(2))
    keyR = Button(keyframe, text=alphabet[3], borderwidth=1, relief="solid", width=5, height=2, command = lambda: PressKey(3))
    keyT = Button(keyframe, text=alphabet[4], borderwidth=1, relief="solid", width=5, height=2, command = lambda: PressKey(4))
    keyY = Button(keyframe, text=alphabet[5], borderwidth=1, relief="solid", width=5, height=2, command = lambda: PressKey(5))
    keyU = Button(keyframe, text=alphabet[6], borderwidth=1, relief="solid", width=5, height=2, command = lambda: PressKey(6))
    keyI = Button(keyframe, text=alphabet[7], borderwidth=1, relief="solid", width=5, height=2, command = lambda: PressKey(7))
    keyO = Button(keyframe, text=alphabet[8], borderwidth=1, relief="solid", width=5, height=2, command = lambda: PressKey(8))
    keyP = Button(keyframe, text=alphabet[9], borderwidth=1, relief="solid", width=5, height=2, command = lambda: PressKey(9))
    keyA = Button(keyframe, text=alphabet[10], borderwidth=1, relief="solid", width=5, height=2, command = lambda: PressKey(10))
    keyS = Button(keyframe, text=alphabet[11], borderwidth=1, relief="solid", width=5, height=2, command = lambda: PressKey(11))
    keyD = Button(keyframe, text=alphabet[12], borderwidth=1, relief="solid", width=5, height=2, command = lambda: PressKey(12))
    keyF = Button(keyframe, text=alphabet[13], borderwidth=1, relief="solid", width=5, height=2, command = lambda: PressKey(13))
    keyG = Button(keyframe, text=alphabet[14], borderwidth=1, relief="solid", width=5, height=2, command = lambda: PressKey(14))
    keyH = Button(keyframe, text=alphabet[15], borderwidth=1, relief="solid", width=5, height=2, command = lambda: PressKey(15))
    keyJ = Button(keyframe, text=alphabet[16], borderwidth=1, relief="solid", width=5, height=2, command = lambda: PressKey(16))
    keyK = Button(keyframe, text=alphabet[17], borderwidth=1, relief="solid", width=5, height=2, command = lambda: PressKey(17))
    keyL = Button(keyframe, text=alphabet[18], borderwidth=1, relief="solid", width=5, height=2, command = lambda: PressKey(18))
    keyZ = Button(keyframe, text=alphabet[19], borderwidth=1, relief="solid", width=5, height=2, command = lambda: PressKey(19))
    keyX = Button(keyframe, text=alphabet[20], borderwidth=1, relief="solid", width=5, height=2, command = lambda: PressKey(20))
    keyC = Button(keyframe, text=alphabet[21], borderwidth=1, relief="solid", width=5, height=2, command = lambda: PressKey(21))
    keyV = Button(keyframe, text=alphabet[22], borderwidth=1, relief="solid", width=5, height=2, command = lambda: PressKey(22))
    keyB = Button(keyframe, text=alphabet[23], borderwidth=1, relief="solid", width=5, height=2, command = lambda: PressKey(23))
    keyN = Button(keyframe, text=alphabet[24], borderwidth=1, relief="solid", width=5, height=2, command = lambda: PressKey(24))
    keyM = Button(keyframe, text=alphabet[25], borderwidth=1, relief="solid", width=5, height=2, command = lambda: PressKey(25))
    keyboard = [keyQ, keyW, keyE, keyR, keyT, keyY, keyU, keyI, keyO, keyP, keyA, keyS, keyD, keyF, keyG, keyH, keyJ, keyK, keyL, keyZ, keyX, keyC, keyV, keyB, keyN, keyM]

    keyframe.grid(row=9,column=0)
    for i in range(10):
        keyboard[i].grid(row=0,column=i+7,padx=1)
    EnterButton = Button(keyframe,text="ENTER",borderwidth=1, relief="solid",width=5,height=5,command = lambda: inputtoguess(0))
    EnterButton.grid(row=1,column=7,padx=1,rowspan=2)
    for i in range(9):
        keyboard[i+10].grid(row=1, column=i+8,padx=1)
    for i in range(7):
        keyboard[i+19].grid(row=2,column=i+8,padx=1)
    Backspace = Button(keyframe, text="BACK", borderwidth=1, relief="solid", width=11, height=2, command=back)
    Backspace.grid(row=2, column=15, padx=1,columnspan=2)

def PressKey(i):
    temp = guess.get()
    guess.delete(0, END)
    guess.insert(0, temp + alphabet[i].lower())

def back():
    temp = guess.get()
    length = len(temp)
    guess.delete(0,END)
    guess.insert(0,temp[0:length-1])

# def on_enter(e):
#
#     guessbutton.config(background='#6aaa64', foreground= "white")
#
# def on_leave(e):
#
#     guessbutton.config(background= 'SystemButtonFace', foreground= 'black')
#
#
# def on_enter_exit(e):
#
#     exitbutton.config(background='#6aaa64', foreground= "white")
#
# def on_leave_exit(e):
#
#     exitbutton.config(background= 'SystemButtonFace', foreground= 'black')
#
# def on_enter_restart(e):
#
#     restartbutton.config(background='#6aaa64', foreground= "white")
#
# def on_leave_restart(e):
#
#     restartbutton.config(background= 'SystemButtonFace', foreground= 'black')

def theme():
    global keyboard
    if clicked.get() == "Dark Mode":
        root.config(bg='black')
        keyframe.config(bg='black')
        mainframe.config(bg='black')
        drop.config(bg='black',fg='white')
        guessbutton.config(bg='black',fg='white',activebackground='white',activeforeground='black')
        exitbutton.config(bg='black',fg='white',activebackground='white',activeforeground='black')
        restartbutton.config(bg='black',fg='white',activebackground='white',activeforeground='black')
        guess.config(bg='black',fg='white',insertbackground='white')
        for i in range(guessnum,6):
            for j in range(5):
                (LabelGrid[i])[j].config(bg='black',fg='white',borderwidth=5,relief=GROOVE)
        for x in alphabet:
            if x not in guessedletters:
                ind = alphabet.index(x)
                keyboard[ind].config(bg='black',fg='white',activebackground='white',activeforeground='black',borderwidth=2,relief=GROOVE)
        EnterButton.config(bg='black',fg='white',activebackground='white',activeforeground='black',borderwidth=2,relief=GROOVE)
        Backspace.config(bg='black',fg='white',activebackground='white',activeforeground='black',borderwidth=2,relief=GROOVE)

    else:
        root.config(bg='#f0f0f0')
        keyframe.config(bg='#f0f0f0')
        mainframe.config(bg='#f0f0f0')
        drop.config(bg='#f0f0f0',fg='black')
        guessbutton.config(bg='#f0f0f0',fg='black',activebackground='black',activeforeground='white')
        exitbutton.config(bg='#f0f0f0',fg='black',activebackground='black',activeforeground='white')
        restartbutton.config(bg='#f0f0f0',fg='black',activebackground='black',activeforeground='white')
        guess.config(bg='#f0f0f0',fg='black',insertbackground='black')
        for i in range(guessnum,6):
            for j in range(5):
                (LabelGrid[i])[j].config(bg='#f0f0f0',fg='black',borderwidth=5,relief=GROOVE)
        for x in alphabet:
            if x not in guessedletters:
                ind = alphabet.index(x)
                keyboard[ind].config(bg='#f0f0f0',fg='black',activebackground='black',activeforeground='white',borderwidth=2,relief=GROOVE)
        EnterButton.config(bg='#f0f0f0',fg='black',activebackground='black',activeforeground='white',borderwidth=2,relief=GROOVE)
        Backspace.config(bg='#f0f0f0',fg='black',activebackground='black',activeforeground='white',borderwidth=2,relief=GROOVE)
    root.after(200, theme)


clicked = StringVar()
clicked.set("Light Mode")
drop = OptionMenu(mainframe, clicked, "Dark Mode", "Light Mode")

drop.grid(row=0,column=0,columnspan=2,sticky=W)


guess = Entry(mainframe, width=23,font=('Arial 18'),borderwidth=5,relief=SUNKEN,justify="center")
guess.grid(row=1,column=0,columnspan=5)
guess.focus_set()

CreateSpace()

guessbutton = Button(mainframe, text = "Guess", command = lambda: inputtoguess(0),width=7,height=3)
guessbutton.grid(row=8,column=0)
restartbutton = Button(mainframe, text = "  New \n Game", command = CreateSpace,width=7,height=3)
restartbutton.grid(row=8,column=1)
exitbutton = Button(mainframe, text="Exit Game",width=25,height=3,command=root.quit)
exitbutton.grid(row=8,column=2,columnspan=3)

theme()

# guessbutton.bind('<Enter>', on_enter)
# guessbutton.bind('<Leave>', on_leave)
# exitbutton.bind('<Enter>', on_enter_exit)
# exitbutton.bind('<Leave>', on_leave_exit)
# restartbutton.bind('<Enter>', on_enter_restart)
# restartbutton.bind('<Leave>', on_leave_restart)
root.bind('<Return>', inputtoguess)


root.mainloop()
