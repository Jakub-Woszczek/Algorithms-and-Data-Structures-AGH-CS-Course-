def tanagram(x, y, t):
    def string_to_number_array(s):
        return [ord(char) - ord('a') for char in s]

    x_list = string_to_number_array(x)
    y_list = string_to_number_array(y)
    n = len(x_list)

    flaga = False

    for i in range(n):
        szukana = x_list[i]

        for j in range(max(0,i-t),min(n,i+t+1)):
            if y_list[j] == szukana:
                y_list[j] = None
                flaga = True
                break

        if flaga == False:
            print(f'nie znalazłem {szukana}')
            return False
        flaga = False
    return True


x = 'kotomysz'
y = 'tokmysoz'
x_2 = "abcdeabcdeabcdeabcde"
y_2 = "edcbaedcbaedcbaedcba"
x_3 = 'pfrgcmihwlwzywddjpqqgjzzuwjazdfyvqhjxvbbuapeayprxeadyjcapakjfadxzoqipzvskyakfngijvyvmzfgxuumfnfwpictvwncathjngmyvocjckzmwohsidrbgxnmaqrlghrcfuuayjqthpwkiksdlohnkunuhzladofnkquyxhwfkoolcohjahfahrarjlynxplynoqusqeiqulllkccnqpcmsabcelkyeelkbepldopqubfmphp'
y_3 = 'wnaipelljvihyluymhjakrygmwhfapwaykcjqcjlrhceqvnbqnhahtgsledjozwigahlqczculjxmzmwmgjmochfdpobbnikpenfujzkyxxrvlodrcdjzoixjpsykadlkdvkpguqhspuelzuuaaagrqoapaeyhyjlfqpkvwswmszpqqhfkfdnffychouffrpkzvmbpnhatxdfcacqocxatacninbnykoqozqxkefplbgjuypundwliurwyvu'


print(tanagram(x,y,18))