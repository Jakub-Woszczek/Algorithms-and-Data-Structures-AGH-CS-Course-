def garek( A ):

    n = len(A)
    left_i = 0
    right_i = n-1

    def Garek_s__Turn(T,left,right,Gareks_sum):
        if T[left] == T[right]:
            picked = 1 if T[left + 1] < T[right - 1] else 0 # jedynka dla wybranej lewej a zero dla prawej

            if picked == 1:
                Gareks_sum += T[left]
                left += 1
            else:
                Gareks_sum += T[right]
                right -= 1

        else:
            if T[left] < T[right]:
                Gareks_sum += T[right]
                right -= 1
            else:
                Gareks_sum += T[left]
                left += 1

        return Gareks_sum,left,right

    def My_fcking_turn(T,left,right,My_sum):
        if T[left] == T[right]:
            picked = 1 if T[left + 1] < T[right - 1] else 0  # jedynka dla wybranej lewej a zero dla prawej

            if picked == 1:
                My_sum += T[left]
                left += 1
            else:
                My_sum += T[right]
                right -= 1

        else:
            if T[left] < T[right]: # Wygląda jakby pick prawy
                if T[left + 1] < T[right - 1]:
                    pick = 1
                    # Pick lewy
                else:
                    # Pick prawy
                    pick = 1

            else: # T[left] > T[right] ----> pick lewy
                if T[left + 1] > T[right - 1]:
                    # Pick prawy
                    pick = 1
                else:
                    # Pick lewy
                    pick = 1


        return

    turn = 2
    while left_i != right_i:
        if turn % 2 == 0:
            My_fcking_turn()

        else:
            Garek_s__Turn()

        turn += 1


    return


T = [2, 7, 46, 7, 26, 3, 50, 9, 22, 37]
print(garek(T))