class Elementos:
    def __init__(self, nome, sigla):
        self.nome = nome.title()
        self.sigla = sigla.title()

    def __str__(self):
        return f'Elemento: {self.nome}({self.sigla})'


class Classificacao(Elementos):
    def __init__(self, nome, sigla, familia, periodo, propriedade):
        super().__init__(nome, sigla)
        self._familia = familia.upper()
        self._periodo = periodo
        self._propriedade = propriedade.title()

    def __len__(self):
        return len(self.nome)

    @property
    def periodo(self):
        return f'{self.nome}({self.sigla}) {self._periodo}º Periodo'

    @property
    def familia(self):
        return f'{self.nome}({self.sigla}) Família {self._familia}'

    @property
    def propriedade(self):
        return f'{self.nome}({self.sigla}) Grupos dos {self._propriedade}'

    def __str__(self):
        return f'{self.nome}({self.sigla}) Família {self._familia} {self._periodo}º Período  ({self._propriedade})'


def extrator_de_parametros(string):
    string = string + '-'
    tamanho_na_lista = 0
    for posicao in range(100):
        parametro_de_busca = '-'
        buscar_palavra = string.find(parametro_de_busca)
        palavra_achada = string[:buscar_palavra]
        lista_de_parametros.append(palavra_achada)
        tamanho_na_lista += len(lista_de_parametros[posicao])
        string = string[buscar_palavra + 1:]
    return lista_de_parametros


def limpar_parametros(parametro):
    while True:
        if '' in parametro:
            parametro.remove('')
        else:
            break
    return parametro


def definir_utilizacao(parametros):
    funcao = parametros[0]
    if funcao == 'família':
        index = 1
        posicao = 0
        while True:
            if posicao < len(parametros) - 1:
                if parametros[index] in lista_de_elementos:
                    print(lista_de_elementos[parametros[index]].familia)

                else:
                    print(f'Erro {parametros[index]}')
                index += 1
                posicao += 1
            else:
                break

    elif funcao == 'período':
        index = 1
        posicao = 0
        while True:
            if posicao < len(parametros) - 1:
                if parametros[index] in lista_de_elementos:
                    print(lista_de_elementos[parametros[index]].periodo)

                else:
                    print(f'Erro {parametros[index]}')
                index += 1
                posicao += 1
            else:
                break
    elif funcao == 'propriedade':
        index = 1
        posicao = 0
        while True:
            if posicao < len(parametros) - 1:
                if parametros[index] in lista_de_elementos:
                    print(lista_de_elementos[parametros[index]].propriedade)
                else:
                    print(f'Erro {parametros[index]}')
                index += 1
                posicao += 1
            else:
                break


hidrogenio = Classificacao('hidrogênio', 'h', 'ia', 1, 'não metais')
helio = Classificacao('hélio', 'he', 'viiia', 1, 'gases nobres')
litio = Classificacao('lítio', 'li', 'ia', 2, 'metais alcalinos')
berilio = Classificacao('berílio', 'be', 'iia', 2, 'metais alcalinos terrossos')
boro = Classificacao('boro', 'b', 'iiia', 2, 'semimetais')
carbono = Classificacao('carbono', 'c', 'iva', 2, 'não metais')
nitrogenio = Classificacao('nitrogênio', 'n', 'va', 2, 'não metais')
oxigenio = Classificacao('oxigenio', 'o', 'via', 2, 'não metais')
fluor = Classificacao('flúor', 'f', 'viia', 2, 'halogênios')
neonio = Classificacao('neônio', 'ne', 'viia', 2, 'gases nobres')
sodio = Classificacao('sódio', 'na', 'ia', 3, 'metais alcalinos')
magnesio = Classificacao('magnésio', 'mg', 'iia', 3, 'metais alcalinos terrossos')
aluminio = Classificacao('aluminio', 'al', 'iiia', 3, 'outros metais')
silicio = Classificacao('sílicio', 'si', 'iva', 3, 'semimetais')
fosforo = Classificacao('fósforo', 'p', 'va', 3, 'não metais')
enxofre = Classificacao('enxofre', 's', 'via', 3, 'não metais')
cloro = Classificacao('cloro', 'cl', 'viia', 3, 'halogênios')
argonio = Classificacao('argônio', 'ar', 'viiia', 4, 'gases nobres')
potassio = Classificacao('potássio', 'k', 'ia', 4, 'metais alcalinos')
calcio = Classificacao('cálcio', 'ca', 'iia', 4, 'metais alcalinos terrossos')
escandio = Classificacao('escândio', 'sc', 'iiib', 4, 'metais de transição')
titanio = Classificacao('titânio', 'ti', 'ivb', 4, 'metais de transição')
vanadio = Classificacao('vanádio', 'v', 'vb', 4, 'metais de transição')
cromo = Classificacao('cromo', 'cr', 'vib', 4, 'metais de transição')
manganes = Classificacao('mangánes', 'mn', 'viib', 4, 'metais de transição')
ferro = Classificacao('ferro', 'fe', 'viiib', 4, 'metais de transição')
cobalto = Classificacao('cobalto', 'co', 'viiib', 4, 'metais de transição')
niquel = Classificacao('níquel', 'ni', 'viib', 4, 'metais de transição')
cobre = Classificacao('cobre', 'cu', 'ib', 4, 'metais de transição')
zinco = Classificacao('zinco', 'zn', 'iib', 4, 'metais de transição')
galio = Classificacao('gálio', 'ga', 'iiia', 4, 'outros metais')
germanio = Classificacao('germânio', 'ge', 'iva', 4, 'semimetais')
arsenio = Classificacao('arsênio', 'as', 'va', 4, 'semimetais')
selenio = Classificacao('selênio', 'se', 'via', 4, 'não metais')
bromo = Classificacao('bromo', 'br', 'viia', 4, 'halogênios')
criptonio = Classificacao('criptônio', 'kr', 'viiia', 4, 'gases nobres')
rubidio = Classificacao('rubidio', 'rb', 'ia', 5, 'metais alcalinos')
estroncio = Classificacao('estrôncio', 'sr', 'iia', 5, 'metais alcalinos terrossos')
itrio = Classificacao('ítrio', 'y', 'iiib', 5, 'metais de transição')
zirconio = Classificacao('zircônio', 'zr', 'ivb', 5, 'metais de transição')
niobio = Classificacao('nióbio', 'nb', 'vb', 5, 'metais de transição')
molibdenio = Classificacao('molibdênio', 'mo', 'vib', 5, 'metais de transição')
tecnecio = Classificacao('tecnécio', 'tc', 'viib', 5, 'metais de transição')
rutenio = Classificacao('rutênio', 'ru', 'viiib', 5, 'metais de transição')
rodio = Classificacao('ródio', 'rh', 'viiib', 5, 'metais de transição')
paladio = Classificacao('paládio', 'pd', 'viiib', 5, 'metais de transição')
prata = Classificacao('prata', 'ag', 'ib', 5, 'metais de transição')
cadmo = Classificacao('cádmo', 'cd', 'iib', 5, 'metais de transição')
indio = Classificacao('índio', 'in', 'iiia', 5, 'outros metais')
estanho = Classificacao('estanho', 'sn', 'iva', 5, 'outros metais')
antimonio = Classificacao('antimônio', 'sb', 'va', 5, 'semimetais')
telurio = Classificacao('telúrio', 'te', 'via', 5, 'semimetais')
iodo = Classificacao('iodo', 'i', 'viia', 5, 'halogênios')
xenonio = Classificacao('xenônio', 'xe', 'viiia', 5, 'gases nobres')
cesio = Classificacao('césio', 'cs', 'ia', 6, 'metais alcalinos')
bario = Classificacao('bário', 'ba', 'iia', 6, 'metais alcalinos terrossos')
hafnio = Classificacao('háfnio', 'hf', 'ivb', 6, 'metais de transição')
tantalo = Classificacao('tântalo', 'ta', 'vb', 6, 'metais de transição')
tungstenio = Classificacao('tungstênio', 'w', 'vib', 6, 'metais de transição')
renio = Classificacao('rênio', 're', 'viib', 6, 'metais de transição')
osmio = Classificacao('ósmio', 'os', 'viiib', 6, 'metais de transição')
iridio = Classificacao('irídio', 'ir', 'viiib', 6, 'metais de transição')
platina = Classificacao('platina', 'pt', 'viiib', 6, 'metais de transição')
ouro = Classificacao('ouro', 'au', 'ib', 6, 'metais de transição')
mercurio = Classificacao('mercúrio', 'hg', 'iib', 6, 'metais de transição')
talio = Classificacao('tálio', 'tl', 'iiia', 6, 'outros metais')
chumbo = Classificacao('chumbo', 'pb', 'iva', 6, 'outros metais')
bismuto = Classificacao('bismuto', 'bi', 'va', 6, 'outros metais')
polonio = Classificacao('polônio', 'po', 'via', 6, 'semimetais')
astato = Classificacao('ástato', 'at', 'viia', 6, 'halogênios')
radonio = Classificacao('radônio', 'rn', 'viiia', 6, 'gases nobres')
francio = Classificacao('frâncio', 'fr', 'ia', 7, 'metais alcalinos')
radio = Classificacao('rádio', 'ra', 'iia', 7, 'metais alcalinos terrossos')
rutherfordio = Classificacao('rutherfórdio', 'rf', 'ivb', 7, 'metais de transição')
dubnio = Classificacao('dúbnio', 'db', 'vb', 7, 'metais de transição')
seaborgio = Classificacao('seabórgio', 'sg', 'vib', 7, 'metais de transição')
bohrio = Classificacao('bóhrio', 'bh', 'viib', 7, 'metais de transição')
hassio = Classificacao('hássio', 'hs', 'viiib', 7, 'metais de transição')
meitnerio = Classificacao('meintério', 'mt', 'viiib', 7, 'metais de transição')
darmstadio = Classificacao('darmstádio', 'ds', 'viiib', 7, 'metais de transição')
roentgenio = Classificacao('roentgênio', 'rg', 'ib', 7, 'metais de transição')
copernico = Classificacao('coperníco', 'cn', 'iib', 7, 'metais de transição')
nihonium = Classificacao('nihonium', 'nh', '', 7, 'outros metais')
flerovio = Classificacao('fleróvio', 'fl', '', 7, 'outros metais')
moscovio = Classificacao('moscóvio', 'mc', '', 7, 'outros metais')
livermorio = Classificacao('livermório', 'lv', '', 7, 'outros metais')
tenesso = Classificacao('tenesso', 'ts', '', 7, 'halogênios')
oganesson = Classificacao('oganesso', 'og', '', 7, 'gases nobres')
lantanio = Classificacao('lantânio', 'la', 'iiib', 6, 'lantanídeos')
cerio = Classificacao('cério', 'ce', 'iiib', 6, 'lantanídeos')
praseodimio = Classificacao('paseodímio', 'pr', 'iiib', 6, 'lantanídeos')
neodimio = Classificacao('neodímio', 'nd', 'iiib', 6, 'lantanídeos')
promecio = Classificacao('promécio', 'pm', 'iiib', 6, 'lantanídeos')
samario = Classificacao('samário', 'sm', 'iiib', 6, 'lantanídeos')
europio = Classificacao('európio', 'eu', 'iiib', 6, 'lantanídeos')
gadolinio = Classificacao('gadolínio', 'gd', 'iiib', 6, 'lantanídeos')
terbio = Classificacao('térbio', 'tb', 'iiib', 6, 'lantanídeos')
disprosio = Classificacao('disprósio', 'dy', 'iiib', 6, 'lantanídeos')
holmio = Classificacao('hólmio', 'ho', 'iiib', 6, 'lantanídeos')
erbio = Classificacao('érbio', 'er', 'iiib', 6, 'lantanídeos')
tulio = Classificacao('túlio', 'tm', 'iiib', 6, 'lantanídeos')
iterbio = Classificacao('itérbio', 'yb', 'iiib', 6, 'lantanídeos')
lutecio = Classificacao('lutécio', 'lu', 'iiib', 6, 'lantanídeos')
actinio = Classificacao('actínio', 'ac', 'iiib', 7, 'actinídeos')
torio = Classificacao('tório', 'th', 'iiib', 7, 'actinídeos')
protactinio = Classificacao('protactínio', 'pa', 'iiib', 7, 'actinídeos')
uranio = Classificacao('urânio', 'u', 'iiib', 7, 'actinídeos')
neptunio = Classificacao('neptúnio', 'np', 'iiib', 7, 'actinídeos')
plutonio = Classificacao('plutônio', 'pu', 'iiib', 7, 'actinídeos')
americio = Classificacao('amerício', 'am', 'iiib', 7, 'actinídeos')
curio = Classificacao('cúrio', 'cm', 'iiib', 7, 'actinídeos')
berquelio = Classificacao('berquélio', 'bk', 'iiib', 7, 'actinídeos')
californio = Classificacao('califórnio', 'cf', 'iiib', 7, 'actinídeos')
einstenio = Classificacao('einstênio', 'es', 'iiib', 7, 'actinídeos')
fermio = Classificacao('férmio', 'fm', 'iiib', 7, 'actinídeos')
mendelevio = Classificacao('mendelévio', 'md', 'iiib', 7, 'actinídeos')
nobelio = Classificacao('nobélio', 'no', 'iiib', 7, 'actinídeos')
laurencio = Classificacao('laurêncio', 'lr', 'iiib', 7, 'actinídeos')

lista_de_elementos = {'hidrogênio': hidrogenio, 'hélio': helio, 'lítio': litio, 'berílio': berilio, 'boro': boro,
                      'carbono': carbono, 'nitrogênio': nitrogenio, 'oxigênio': oxigenio, 'fluor': fluor,
                      'nêonio': neonio, 'sódio': sodio, 'magnésio': magnesio, 'aluminio': aluminio, 'sílicio': silicio,
                      'fósforo': fosforo, 'enxofre': enxofre, 'cloro': cloro, 'argônio': argonio, 'potássio': potassio,
                      'cálcio': calcio, 'escândio': escandio, 'titânio': titanio, 'vanádio': vanadio, 'cromo': cromo,
                      'mangánes': manganes, 'ferro': ferro, 'cobalto': cobalto, 'níquel': niquel, 'cobre': cobre,
                      'zinco': zinco, 'gálio': galio, 'germânio': germanio, 'arsênio': arsenio, 'selênio': selenio,
                      'bromo': bromo, 'criptônio': criptonio, 'rubidio': rubidio, 'estrôncio': estroncio,
                      'ítrio': itrio, 'zircônio': zirconio, 'nióbio': niobio, 'molibdênio': molibdenio,
                      'tecnécio': tecnecio, 'rutênio': rutenio, 'ródio': rodio, 'paládio': paladio, 'prata': prata,
                      'cádmo': cadmo, 'índio': indio, 'estanho': estanho, 'antimônio': antimonio, 'telúrio': telurio,
                      'iodo': iodo, 'xenônio': xenonio, 'césio': cesio, 'bário': bario, 'háfnio': hafnio,
                      'tântalo': tantalo, 'tungstênio': tungstenio, 'ósmio': osmio, 'irídio': iridio,
                      'platina': platina, 'ouro': ouro, 'mercúrio': mercurio, 'tálio': talio, 'chumbo': chumbo,
                      'bismuto': bismuto, 'polônio': polonio, 'ástato': astato, 'radônio': radonio, 'frâncio': francio,
                      'rádio': radio, 'rutherfórdio': rutherfordio, 'dúbnio': dubnio, 'seabórgio': seaborgio,
                      'bóhrio': bohrio, 'hássio': hassio, 'meitnério': meitnerio, 'darmstádio': darmstadio,
                      'roentgênio': roentgenio, 'coperníco': copernico, 'lantânio': lantanio, 'cério': cerio,
                      'praseodímio': praseodimio, 'neodímio': neodimio, 'promécio': promecio, 'samário': samario,
                      'európio': europio, 'gadolínio': gadolinio, 'térbio': terbio, 'disprósio': disprosio,
                      'hólmio': holmio, 'érbio': erbio, 'túlio': tulio, 'itérbio': iterbio, 'lutécio': lutecio,
                      'actínio': actinio, 'tório': torio, 'protactínio': protactinio, 'urânio': uranio,
                      'neptúnio': neptunio, 'plutônio': plutonio, 'amerício': americio, 'cúrio': curio,
                      'berquélio': berquelio, 'califórnio': californio, 'einstênio': einstenio, 'férmio': fermio,
                      'mendelévio': mendelevio, 'nobélio': nobelio, 'laurêncio': laurencio}


lista = ['stop', 'elementos', 'família', '/key', 'período', 'propriedade']


while True:
    pesquisa = input('Pesquisa...?').lower().strip().replace(' ', '-')
    lista_de_parametros = []
    extrator_de_parametros(pesquisa)
    limpar_parametros(lista_de_parametros)

    print(lista_de_parametros)
    print(len(lista_de_parametros))
    if len(lista_de_parametros) >= 2:
        try:
            definir_utilizacao(lista_de_parametros)
        except KeyError:
            try:
                print(f'Não encontrado: {lista_de_parametros[0]}')
            except IndexError:
                print(f'Valor errado')
    else:
        try:
            print(lista_de_elementos[pesquisa])
        except KeyError:
            try:
                print(f'Não encontrado: {lista_de_parametros[0]}')
            except IndexError:
                print(f'Valor errado')
