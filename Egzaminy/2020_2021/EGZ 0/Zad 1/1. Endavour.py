def tanagram(x, y, t):
    def string_to_number_array(s):
        return [ord(char) - ord('a') for char in s]

    x_list = string_to_number_array(x)
    y_list = string_to_number_array(y)

    def buble_sort(napis,iteracje):

        for _ in range(iteracje):
            for  i in range(len(napis)-1):

                if napis[i] > napis[i+1]:
                    napis[i],napis[i+1] = napis[i+1],napis[i]

        return napis

    x_sorted = buble_sort(x_list,t)
    print(x_sorted)

    y_sorted = buble_sort(y_list,t)
    print(y_sorted)

    if x_sorted == y_sorted:
        return True
    return False

x = 'kotomysz'
y = 'tokmysoz'

tanagram(x,y,3)
