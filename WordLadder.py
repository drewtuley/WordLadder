import copy


def ping_pong_index(start_idx, end_idx):
    delta = end_idx - start_idx
    curr_index = start_idx
    while abs(delta) > 0:
        delta_sign = int(delta / abs(delta))
        next_index = curr_index + delta_sign
        yield (curr_index, next_index)
        curr_index += delta
        delta = abs(delta) - 1
        delta *= -delta_sign
    while curr_index < end_idx:
        yield (curr_index, curr_index + 1)
        curr_index += 1


def recursive_find(src, ladder_steps, idx, max_idx, target, found_dict):
    if idx < max_idx and src in ladder_steps[idx]:
        for fword in ladder_steps[idx][src]:
            if idx + 1 < max_idx + 1:
                found_dict[idx] = fword
                # print('found_list=', found_dict)
                if fword == target and idx == max_idx - 1:
                    print('stop', found_dict)
                recursive_find(fword, ladder_steps, idx + 1, max_idx, end, copy.copy(found_dict))


start = 'mild'
end = 'soft'
max_steps = 6

word_len = len(start)
words = []
letters = 'abcdefghijklmnopqrstuvwxyz'
with open('brit-a-z.txt') as fd:
    for l in fd:
        word = l.strip()
        if len(word) == word_len and '\'' not in word:
            words.append(word)

stages = {0: {start: [start]}, max_steps: {end: [end]}}

for source_step, target_step in ping_pong_index(0, max_steps):
    # print('source={0}, target={1}'.format(source_step, target_step))
    stage = {}
    word_pile = []
    for source_word in stages[source_step]:
        for working_word in stages[source_step][source_word]:
            new_words = []
            for pos in range(0, 4):
                for ltr in letters:
                    if ltr != working_word[pos]:
                        new_word = working_word[0:pos] + ltr + working_word[pos + 1:]
                        if new_word not in new_words and new_word not in word_pile and new_word in words:
                            # print(new_word)
                            new_words.append(new_word)
                            word_pile.append(new_word)
            if len(new_words) > 0:
                # print(working_word, new_words)
                new_words.sort()
                stage[working_word] = new_words
    # print('stage=', stage)
    try:
        if stages[target_step] is not None and len(stages[target_step]) > 0:
            # print('stop reversal')
            prefound_words = []
            for keyword in stage:
                prefound_words.append(keyword)
                for word in stage[keyword]:
                    if word not in prefound_words:
                        prefound_words.append(word)
            words = prefound_words
            words.sort()
            for clear_idx in range(target_step + 1, max_steps + 1):
                stages[clear_idx] = None
        else:
            stages[target_step] = stage
    except KeyError:
        stages[target_step] = stage
    # print('stages=', stages)

# for idx in range(0, max_steps + 1):
#    print('{0}: {1},'.format(idx, stages[idx]))

pstages = {
    0: {'mild': ['mild']},
    1: {'mild': ['gild', 'meld', 'mile', 'milk', 'mill', 'milt', 'mind', 'wild']},
    2: {'gild': ['gill', 'geld', 'gilt', 'gird', 'gold', 'mild', 'wild'],
        'meld': ['held', 'mead', 'melt', 'mend', 'weld'],
        'mile': ['bile', 'file', 'male', 'mice', 'mike', 'milk', 'mill', 'milt', 'mime', 'mine', 'mire', 'mite', 'mole',
                 'mule', 'pile', 'rile', 'tile', 'vile', 'wile'], 'milk': ['bilk', 'mile', 'mink', 'silk'],
        'mill': ['bill', 'dill', 'fill', 'hill', 'kill', 'mall', 'moll', 'mull', 'pill', 'rill', 'sill', 'till',
                 'will'],
        'milt': ['hilt', 'jilt', 'kilt', 'lilt', 'malt', 'mint', 'mist', 'mitt', 'silt', 'tilt', 'wilt'],
        'mind': ['bind', 'find', 'hind', 'kind', 'mini', 'minx', 'rind', 'wind'], 'wild': ['gild', 'wily', 'wold']},
    3: {'geld': ['gels', 'gelt', 'gild', 'gold', 'held', 'meld', 'weld'],
        'gill': ['bill', 'dill', 'fill', 'gall', 'gilt', 'girl', 'gull', 'hill', 'kill', 'mill', 'pill', 'rill', 'sill',
                 'till', 'will'],
        'gilt': ['gift', 'gill', 'girt', 'gist', 'hilt', 'jilt', 'kilt', 'lilt', 'milt', 'silt', 'tilt', 'wilt'],
        'gird': ['bird', 'giro'],
        'gold': ['bold', 'cold', 'fold', 'geld', 'goad', 'golf', 'good', 'hold', 'sold', 'told', 'wold'],
        'mild': ['mile', 'milk', 'mind', 'wild'], 'wild': ['mild', 'wile', 'wily', 'wind'],
        'held': ['head', 'heed', 'hell', 'helm', 'help', 'herd'],
        'mead': ['bead', 'dead', 'lead', 'meal', 'mean', 'meat', 'mend', 'read'],
        'melt': ['belt', 'felt', 'malt', 'meet', 'pelt', 'welt'],
        'mend': ['bend', 'fend', 'lend', 'mead', 'menu', 'rend', 'send', 'tend', 'vend', 'wend'],
        'weld': ['weed', 'well'],
        'bile': ['bale', 'bide', 'bike', 'bilk', 'bite', 'bole', 'file', 'pile', 'rile', 'tile', 'vile'],
        'file': ['bile', 'fide', 'fife', 'film', 'fine', 'fire', 'five'],
        'male': ['dale', 'gale', 'hale', 'kale', 'mace', 'made', 'mage', 'make', 'mall', 'mane', 'mare', 'mate', 'maze',
                 'mole', 'mule', 'pale', 'sale', 'tale', 'vale', 'wale'],
        'mice': ['dice', 'lice', 'mica', 'mike', 'mime', 'mine', 'mire', 'mite', 'nice', 'rice', 'vice'],
        'mike': ['dike', 'hike', 'kike', 'like', 'mice', 'pike'], 'milk': ['mink', 'silk'], 'mill': ['moll', 'mull'],
        'milt': ['melt', 'mint', 'mist', 'mitt'], 'mime': ['dime', 'lime', 'rime', 'time'],
        'mine': ['cine', 'dine', 'line', 'mini', 'minx', 'nine', 'pine', 'sine', 'tine', 'vine', 'wine'],
        'mire': ['dire', 'hire', 'lire', 'mere', 'miry', 'more', 'sire', 'tire', 'wire'],
        'mite': ['cite', 'kite', 'mete', 'mote', 'mute', 'rite', 'site'],
        'mole': ['dole', 'hole', 'male', 'mode', 'mope', 'move', 'pole', 'role', 'sole', 'vole'],
        'mule': ['muse', 'rule', 'yule'], 'pile': ['pipe'], 'rile': ['ride', 'rife', 'ripe', 'rise', 'rive'],
        'tile': ['tide'], 'vile': ['vide', 'vive'], 'wile': ['wide', 'wife', 'wipe', 'wise'], 'bilk': ['balk', 'bulk'],
        'mink': ['dink', 'fink', 'gink', 'jink', 'kink', 'link', 'monk', 'pink', 'rink', 'sink', 'wink'],
        'silk': ['sick', 'silo', 'sulk'], 'bill': ['ball', 'bell', 'boll', 'bull'],
        'dill': ['dell', 'dial', 'doll', 'dull'], 'fill': ['fall', 'fell', 'full'], 'hill': ['hall', 'hull'],
        'kill': ['kiln', 'kilo'], 'mall': ['call', 'mail', 'marl', 'maul', 'pall', 'tall', 'wall'],
        'moll': ['loll', 'moil', 'poll', 'roll', 'toll'], 'mull': ['cull', 'lull', 'null', 'pull'], 'rill': ['rial'],
        'sill': ['sell'], 'till': ['tell'], 'hilt': ['halt', 'hint', 'holt'], 'jilt': ['jolt'],
        'lilt': ['lift', 'lily', 'lint', 'list'], 'malt': ['mart', 'mast', 'matt', 'salt'],
        'mint': ['bint', 'dint', 'pint', 'tint'], 'mist': ['cist', 'fist', 'miss', 'most', 'must'], 'mitt': ['mutt'],
        'silt': ['sift'], 'bind': ['band', 'bins', 'bond', 'bund', 'find', 'hind', 'kind', 'rind'],
        'find': ['bind', 'fins', 'fond', 'fund'], 'hind': ['hand'], 'kind': ['kina', 'king'], 'mini': ['midi'],
        'minx': ['jinx'], 'rind': ['ring'], 'wind': ['wand', 'wing', 'wino', 'wins', 'winy'], 'gild': ['gird'],
        'wily': ['oily', 'wiry'], 'wold': ['wolf', 'wood', 'word']},
    4: {'gelt': ['gilt'], 'bill': ['sill'],
        'gilt': ['gift', 'girt', 'gist', 'hilt', 'jilt', 'kilt', 'lilt', 'milt', 'silt', 'tilt', 'wilt'],
        'sill': ['silk', 'silo'], 'gift': ['lift', 'rift', 'sift'], 'gist': ['list'], 'hilt': ['holt'],
        'lilt': ['lint'], 'silt': ['salt'], 'bold': ['bolt'], 'cold': ['colt'], 'fold': ['food', 'ford'],
        'good': ['goon', 'hood', 'mood', 'rood'], 'sold': ['sole'], 'wold': ['word'], 'meat': ['moat'],
        'malt': ['mart'], 'pelt': ['pert'], 'welt': ['weft'], 'lend': ['lent'], 'bole': ['bore'], 'rile': ['rife'],
        'fife': ['life'], 'fire': ['fore', 'sire'], 'mare': ['more'], 'mist': ['most'], 'lire': ['lore'],
        'mere': ['sere'], 'more': ['core', 'gore', 'morn', 'mort', 'pore', 'sore', 'tore', 'wore', 'yore'],
        'sire': ['sure'], 'sole': ['some'], 'rife': ['riff'], 'toll': ['tool'], 'holt': ['hoot', 'host'],
        'lift': ['left', 'loft'], 'list': ['last', 'lest', 'lost', 'lust'], 'mart': ['fart', 'part', 'tart', 'wart'],
        'cist': ['cost'], 'most': ['dost', 'moot', 'post'], 'sift': ['soft'], 'fond': ['font'],
        'word': ['work', 'worm', 'worn', 'wort']},
    5: {'gilt': ['gift', 'girt', 'gist', 'hilt', 'jilt', 'kilt', 'lilt', 'milt', 'silt', 'tilt', 'wilt'],
        'sill': ['silk', 'silo'], 'gift': ['gilt', 'lift', 'rift', 'sift'], 'gist': ['list'], 'hilt': ['holt'],
        'lilt': ['lint'], 'silt': ['salt', 'sill'], 'lift': ['left', 'life', 'loft'],
        'rift': ['raft', 'rife', 'riff', 'riot'], 'sift': ['soft'], 'list': ['last', 'lest', 'lost', 'lust'],
        'holt': ['bolt', 'colt', 'hoot', 'host'], 'lint': ['lent'], 'bolt': ['boat', 'boot', 'bout'],
        'colt': ['coat', 'coot', 'cost'], 'food': ['fool', 'foot', 'ford', 'hood', 'mood', 'rood'],
        'ford': ['food', 'fore', 'fork', 'form', 'fort', 'word'],
        'goon': ['boon', 'coon', 'loon', 'moon', 'noon', 'soon'], 'hood': ['hoof', 'hook', 'hoop'],
        'mood': ['moor', 'moos', 'moot'], 'rood': ['roof', 'rook', 'room', 'root'], 'sole': ['some', 'sore'],
        'word': ['wore', 'work', 'worm', 'worn', 'wort'], 'moat': ['mort', 'most'],
        'mart': ['fart', 'part', 'tart', 'wart'], 'pert': ['port'], 'weft': ['deft', 'heft'],
        'bore': ['core', 'gore', 'lore', 'more', 'pore', 'tore', 'yore'], 'fore': ['bore'], 'sire': ['sere', 'sure'],
        'more': ['morn'], 'most': ['dost', 'moat', 'post'], 'lore': ['lose'], 'sere': ['sire'],
        'morn': ['porn', 'torn'], 'mort': ['mart', 'sort', 'tort'], 'pore': ['pork'], 'sore': ['sole'],
        'some': ['soma'], 'riff': ['tiff'], 'tool': ['cool', 'took', 'toot'], 'hoot': ['loot', 'soot'],
        'left': ['weft'], 'loft': ['lout', 'toft'], 'lost': ['loss'], 'part': ['pert'], 'tart': ['taut'],
        'post': ['poet', 'pout'], 'soft': ['sofa'], 'font': ['wont']},
    6: {'gift': ['gilt', 'girt', 'gist', 'lift', 'rift', 'sift'], 'girt': ['gift'], 'gist': ['list'],
        'hilt': ['holt', 'jilt', 'kilt', 'lilt', 'milt', 'silt', 'tilt', 'wilt'], 'jilt': ['hilt'], 'lilt': ['lint'],
        'silt': ['salt', 'silk', 'sill', 'silo'], 'lift': ['left', 'life', 'loft'],
        'rift': ['raft', 'rife', 'riff', 'riot'], 'sift': ['soft'], 'list': ['last', 'lest', 'lost', 'lust'],
        'holt': ['bolt', 'colt', 'hoot', 'host'], 'lint': ['lent'], 'left': ['deft', 'heft', 'weft'],
        'loft': ['loot', 'lout', 'toft'], 'riff': ['tiff'], 'riot': ['root', 'ryot'], 'soft': ['sofa', 'soot', 'sort'],
        'lost': ['cost', 'dost', 'lose', 'loss', 'most', 'post'], 'bolt': ['boat', 'boot', 'bout'],
        'colt': ['coat', 'coot'], 'hoot': ['foot', 'hood', 'hoof', 'hook', 'hoop', 'moot', 'toot'], 'boat': ['moat'],
        'boot': ['blot', 'boob', 'book', 'boom', 'boon', 'boor', 'boos'], 'bout': ['gout', 'pout', 'rout', 'tout'],
        'coot': ['clot', 'cook', 'cool', 'coon', 'coop'], 'fool': ['food', 'tool'], 'foot': ['font', 'fool', 'fort'],
        'ford': ['fore', 'fork', 'form', 'word'], 'hood': ['mood', 'rood'], 'mood': ['moon', 'moor', 'moos'],
        'rood': ['roof', 'rook', 'room'], 'food': ['ford'],
        'fore': ['bore', 'core', 'gore', 'lore', 'more', 'pore', 'sore', 'tore', 'wore', 'yore'],
        'fork': ['pork', 'work'], 'form': ['worm'], 'fort': ['fart', 'mort', 'port', 'tort', 'wort'], 'word': ['worn'],
        'boon': ['goon', 'loon', 'noon', 'soon'], 'loon': ['look', 'loom', 'loop'], 'moon': ['morn'], 'soon': ['sown'],
        'hook': ['took'], 'some': ['sole', 'soma'], 'sore': ['sere', 'sire', 'some', 'sure'], 'worn': ['porn', 'torn'],
        'wort': ['wart', 'wont'], 'mort': ['mart'], 'fart': ['part', 'tart'], 'part': ['pert'], 'tart': ['taut'],
        'port': ['poet'], 'soma': ['coma', 'soba', 'soda', 'soya'], 'tiff': ['toff', 'tuff'], 'toot': ['trot'],
        'soot': ['shot', 'slot', 'snot', 'spot', 'swot'], 'lout': ['loud'], 'toft': ['tofu', 'tuft']}
}
for key in stages[0].keys():
    recursive_find(key, stages, 0, max_steps + 1, end, {})
