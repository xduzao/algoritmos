def selection_sort(nums):
    #Percorre o vetor inteiro
    # O valor de i corresponde a quantos elementos foram ordenados
    for i in range(len(nums)):
        # Assume-se que o primeiro elemento do segmento não ordenado é o menor
        lowest_value_index = i
        #Iteração pelos elementos não ordenados
        for j in range(i + 1, len(nums)):
            #Verifica qual o menor valor
            if nums[j] < nums[lowest_value_index]:
                lowest_value_index = j
        
        #Troca o menor elemento pelo primeiro elemento não ordenado
        nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]



