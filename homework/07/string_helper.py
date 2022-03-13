def csv_to_list(csv):
    """Function will turn a given string to a 2d dim list type.
    Parameter
    ---------
    csv: 'String'
        The string will be separeted using commas and turn into a list.
    Return
    ------
    value: 'list'
        Function returns a 2d dim list.
    """
    two_dim_list = []
    split_again = ""
    #tänne tulee yks iso merkkijono pötkö -> 'numero,sana,sana\nnumero,sana,sana\nnumero,sana,sana'
    #split() makes the splitted sections into a list()!!
    #split() katkaistaan toi iso pötkö merkkijono rivinvaihtojen perusteella, tulee sitten tommonen:
    #['numero,sana,sana', 'numero,sana,sana','numero,sana,sana'] <- split jakaa noi tollasiin 
    splitted = csv.split("\n") 
    for word in splitted:
        #käydään läpi joka ikistä elementtiä läpi, (['numero,sana,sana'] on yks elementti, ja niitä on paljon ydhessä listassa)
        #katkaistaan elementti osiksi 'pilkun perusteella' ja laitetaan ne uuteen listaan eli tohon 'two_dim_list'
        #-> [['numero', 'sana', 'sana'],['numero', 'sana', 'sana'],['numero', 'sana', 'sana']]
        split_again = word.split(",") 
        two_dim_list.append(split_again)
    return two_dim_list

x = "1,etu,suku\n2,ekanimi,tokanimi"

"""
1,etu,suku
2,ekanimi,tokanimi
3,en,ymmärrä
"""
print(csv_to_list(x))