from re import match, search, findall, MULTILINE

if __name__ == '__main__':
    text = 'This movie is not so bad'
    print(search('.', text))
    text = '\nThis movie is not so bad'
    print(search('.', text))
    print('\n')

    text = 'This movie is not so bad'
    print(findall('.', text))
    print(findall('^.', text))
    print('\n')

    text = 'This movie\nis not\nso bad'
    print(findall('.', text))
    print(findall('^.', text))
    print(findall('^.', text, MULTILINE))
    print(findall('.$', text))
    print(findall('.$', text, MULTILINE))

    print('\n')
    # Classes de caracteres
    print(findall('[aeiou]', 'Adalberto Fernandes'))  # [aeiou -> classe de caracteres]
    print(findall('[aeiou]', 'Adalberto Fernandes'))  # [aeiou] -> come se fosse ou
    print(findall('[^aeiou]', 'Adalberto Fernandes'))  # [^aeiou] -> diferente destes caracteres
    print(findall('[a-f]', 'Adalberto Fernandes'))  # de a a f
    print(findall('[a-fA-Z]', 'Adalberto Fernandes'))  # de a a f minúsculo e de A a Z maiúsculo
    print(findall('[a-zA-Z0-9_]', 'Adalberto Fernandes_2'))  # de a a z, de A a Z, de 0 a 9 e _
    print(findall('[\w]', 'Adalberto Fernandes_2'))  # o mesmo que o de cima
    print(findall('\w', 'Adalberto Fernandes_2'))  # o mesmo que o de cima

    # Sequências especiais

    # \d == [0-9]
    # \D == [^0-9]
    # \s == [\t\n\r\f\v]
    # \S == [^\t\n\r\f\v]
    # \w == [a-zA-Z0-9_]
    # \W == [^a-zA-Z0-9_]

    # # Repetições
    #
    # from re import match, search, findall
    #
    # ## Quantidades específicas
    #
    #
    # match(r'\d{4}', '1234’)  4 repetições
    #            < re.Match
    # object;
    # span = (0, 4), match = '1234' >
    #
    # match(r'\d{4}', '123’)  retorna None pq não bate
    #
    #      match(r'\d{4}', '12345')
    #      < re.Match
    # object;
    # span = (0, 4), match = '1234' >


    #  ## Quantidade mínima
    #
    # match(r'\d{2,}', '12')
    #      < re.Match
    # object;
    # span = (0, 2), match = '12' >
    #
    # match(r'\d{2,}', '1234567')
    #      < re.Match
    # object;
    # span = (0, 7), match = '1234567' >
    #
    # match(r'\d{2,}', '1')
    #
    # match(r'\d{2,}?', '1234567’) ? == indica o mínimo possível
    #            < re.Match
    # object;
    # span = (0, 2), match = '12' >


    #
    # ## Min e Max
    #
    # match(r'\d{2,4}?', '12345')
    #      < re.Match
    # object;
    # span = (0, 2), match = '12' >
    #
    # match(r'\d{2,4}', '12345')
    #      < re.Match
    # object;
    # span = (0, 4), match = '1234' >
    #
    # match(r'\d{2,4}', '1234')
    #      < re.Match
    # object;
    # span = (0, 4), match = '1234' >
    #
    # match(r'\d{2,4}', '123')
    #      < re.Match
    # object;
    # span = (0, 3), match = '123' >
    #
    # match(r'\d{2,4}', '12')
    #      < re.Match
    # object;
    # span = (0, 2), match = '12' >
    #
    # match(r'\d{2,4}', '1')
    #
    # match(r'\d{2,4}?', '12345')
    #      < re.Match
    # object;
    # span = (0, 2), match = '12' >


    # # 0 ou 1 ocorrência
    #
    #
    # match(r'\d{0,1]', '12345')
    #
    # match(r'\d{0,1}', '12345')
    #      < re.Match
    # object;
    # span = (0, 1), match = '1' >
    #
    # match(r'\d{,1}', '12345')
    #      < re.Match
    # object;
    # span = (0, 1), match = '1' >
    #
    # match(r'\d{,1}?', '12345')
    #      < re.Match
    # object;
    # span = (0, 0), match = '' >
    #
    # match(r'\d?', '12345')
    #      < re.Match
    # object;
    # span = (0, 1), match = '1' >
    #
    # match(r'\d??', '12345')
    #      < re.Match
    # object;
    # span = (0, 0), match = '' >


    # ## 0 ou mais vezes
    #
    # match(r'\d{0,0}', '12345')
    #      < re.Match
    # object;
    # span = (0, 0), match = '' >
    #
    # match(r'\d{0,}', '12345')
    #      < re.Match
    # object;
    # span = (0, 5), match = '12345' >
    #
    # match(r'\d{,}', '12345')
    #      < re.Match
    # object;
    # span = (0, 5), match = '12345' >
    #
    # match(r'\d*', '12345')
    #      < re.Match
    # object;
    # span = (0, 5), match = '12345' >
    #
    # match(r'\d*?', '12345')
    #      < re.Match
    # object;
    # span = (0, 0), match =‘'>
    #

    ## 1 ou mais vezes
    #
    # match(r'\d{1,}', '12345')
    #      < re.Match
    # object;
    # span = (0, 5), match = '12345' >
    #
    # match(r'\d{1,}?', '12345')
    #      < re.Match
    # object;
    # span = (0, 1), match = '1' >
    #
    # match(r'\d+', '12345')
    #      < re.Match
    # object;
    # span = (0, 5), match = '12345' >
    #
    # match(r'\d+?', '12345')
    #      < re.Match
    # object;
    # span = (0, 1), match = '1’>

    # Grupo de Captura
    #  html = '<input type="text" id="id_cpf" name="cpf">'
    #
    #  pattern = r'<(.+?) type="(.+?)" id="(.+?)" name="(.+?)"'
    #
    #  m = match(pattern, html)
    #
    #  m.groups()
    # ('input', 'text', 'id_cpf', 'cpf')
    #  m.group(1)
    # 'input'
    #
    #  m.group(2)
    # 'text'
    #
    #  m.group(1, 2, 3)
    # ('input', 'text', 'id_cpf')

    # html1 = '<input type="text" id="id_cpf" name="cpf">'
    #
    # html2 = '<input id="id_cpf" name="cpf" type="text">'
    #
    # pattern = r'<(.+?) type="(.+?)" id="(.+?)" name="(.+?)"'
    #
    # pattern
    # '<(.+?) type="(.+?)" id="(.+?)" name="(.+?)"'
    #
    # pattern = '<(.+?) (?:(?:type="(.+?)"|id="(.+?)"|name="(.+?)") ?)*'
    #
    # pattern
    # '<(.+?) (?:(?:type="(.+?)"|id="(.+?)"|name="(.+?)") ?)*'
    #
    # m = match(pattern, html1)
    #
    # m
    # <re.Match object; span=(0, 41), match='<input type="text" id="id_cpf" name="cpf"'>
    #
    # m.groups()
    # ('input', 'text', 'id_cpf', 'cpf')
    #
    # m = match(pattern, html2)
    #
    # m
    # <re.Match object; span=(0, 41), match='<input id="id_cpf" name="cpf" type="text"'>
    #
    # m.groups()
    # ('input', 'text', 'id_cpf', 'cpf')

    # Named Groups

    # >> > html1 = '<input type="text" id="id_cpf" name="cpf">'
    # >> >
    # >> > html2 = '<input id="id_cpf" name="cpf" type="text">'
    # >> >
    # >> > pattern = '<(.+?) (?:(?:type="(.+?)"|id="(.+?)"|name="(.+?)") ?)*'
    # >> >
    # >> > pattern = '<(?P<tag>.+?) (?:(?:type="(?P<type>.+?)"|id="(?P<id>.+?)"|name="(?P<name>.+?)") ?)*'
    # >> >
    # >> > m = match(pattern, html1)
    # >> >
    # >> > m
    # < re.Match
    # object;
    # span = (0, 41), match = '<input type="text" id="id_cpf" name="cpf"' >
    # >> >
    # >> > m.groups()
    # ('input', 'text', 'id_cpf', 'cpf')
    # >> >
    # >> > m.groupdict()
    # {'tag': 'input', 'type': 'text', 'id': 'id_cpf', 'name': 'cpf'}
    # >> >
    # >> > m.groupdict(1)
    # {'tag': 'input', 'type': 'text', 'id': 'id_cpf', 'name': 'cpf'}
    # >> >
